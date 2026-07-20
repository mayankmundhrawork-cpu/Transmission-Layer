"""SYNTH_V2 · S1 — normalized event bus.

One schema for every input so downstream stages join deterministically:

  Event {
    id        sha1-12 of (source, natural key) — stable dedup
    ts        ISO-8601 UTC
    source    market | squawk | rss | release
    kind      move | headline | scheduled
    entities  [registry series ids]        (the join keys)
    topics    [free tags]                  (grouping/dispersion)
    payload   source-specific dict (see adapters)
    salience  0..1, deterministic per source (see _salience_*)
  }

Adapters:
  market   — a series emits an event when today's |zc| exceeds the ADAPTIVE
             bar: the q-quantile (settings.SYNTH_MOVE_QUANTILE, default .98)
             of that series' own |zc| history. No fixed z anywhere.
  squawk   — every DeItaone item, entity-tagged via the 3-layer lexicon.
  rss      — every headline-store item (already deduped), entity-tagged.
  release  — calendar items due within 1 day or released in the last day.

Entity extraction (L1 universe symbols/names → L2 backbone NEWS_ALIASES →
L3 synth_aliases topic map) is word-boundary, precompiled, auditable.
Items that match NOTHING are logged to data/synth/join_misses.json —
the instrumentation that makes "big move / no news" trustworthy and
triggers the embedding upgrade on evidence (ruling 2).

State: data/synth/events.json (rolling SYNTH_EVENT_DAYS).
Run: python synth_events.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
SYNTH_DIR = DATA_DIR / "synth"
EVENTS_JSON = SYNTH_DIR / "events.json"
MISSES_JSON = SYNTH_DIR / "join_misses.json"

MOVE_QUANTILE = 0.98      # adaptive per-series bar on |zc| history
MOVE_MIN_HISTORY = 120
EVENT_DAYS = 7            # rolling bus window
MISS_CAP = 400


# ── lexicon compilation (L1 + L2 + L3) ─────────────────────────────────
def _compile_lexicon():
    """[(compiled_regex, series[], topics[], layer)] — built once per run."""
    from backbone import NEWS_ALIASES
    from registry import load_registry, load_universe
    from synth_aliases import TOPIC_ALIASES, TOPIC_ONLY

    entries: list[tuple[re.Pattern, list[str], list[str], str]] = []

    def rx(phrase: str) -> re.Pattern:
        p = phrase.strip().lower()
        if p.endswith(" "):
            return re.compile(re.escape(p.strip()) + r"\b\s")
        return re.compile(rf"\b{re.escape(p)}\b")

    # L1 — universe: symbols + distinctive name tokens (auto)
    uni = load_universe().get("members", {})
    for spec in load_registry():
        sid = spec["id"]
        if spec.get("dynamic"):
            sym = spec.get("symbol", "")
            m = uni.get(sym, {})
            norm = m.get("norm") or ""
            if len(norm) >= 4:
                entries.append((rx(norm), [sid], [], "L1", {}))
            for tok in norm.split():
                if len(tok) >= 5:
                    entries.append((rx(tok), [sid], [], "L1", {}))
    # L2 — backbone aliases
    for sid, phrases in NEWS_ALIASES.items():
        for p in phrases:
            entries.append((rx(p), [sid], [], "L2", {}))
    # L3 — curated topic map (carries per-series edge weights + watch flag)
    for e in TOPIC_ALIASES:
        w = e.get("weights", {})
        watch = bool(e.get("watch"))
        for p in e["phrases"]:
            entries.append((rx(p), e["series"], e.get("topics", []),
                            "L3:watch" if watch else "L3", w))
    topic_only = [(rx(p), tags) for p, tags in TOPIC_ONLY.items()]
    return entries, topic_only


def tag_text(text: str, lexicon):
    """(entities, topics, layers_hit, entity_weights) for one text.
    entity weight = max weight across matching entries (default 1.0)."""
    entries, topic_only = lexicon
    tl = text.lower()
    ents, topics, layers = [], [], []
    weights: dict[str, float] = {}
    for entry in entries:
        pat, series, tags, layer = entry[0], entry[1], entry[2], entry[3]
        w = entry[4] if len(entry) > 4 else {}
        if pat.search(tl):
            for sid in series:
                ents.append(sid)
                weights[sid] = max(weights.get(sid, 0.0), w.get(sid, 1.0))
            topics += tags
            layers.append(layer)
    for pat, tags in topic_only:
        if pat.search(tl):
            topics += tags
    dedupe = lambda xs: list(dict.fromkeys(xs))
    return dedupe(ents), dedupe(topics), dedupe(layers), weights


# ── salience (deterministic, per source) ───────────────────────────────
def _salience_market(move_pctile: float) -> float:
    return round(min(1.0, max(0.0, (move_pctile - 0.90) / 0.10)), 3)


def _salience_text(source: str, ts: datetime, n_entities: int,
                   now: datetime) -> float:
    src_w = {"squawk": 0.9, "rss": 0.6}.get(source, 0.5)
    age_h = max((now - ts).total_seconds() / 3600.0, 0.0)
    recency = 0.5 ** (age_h / 12.0)          # 12h half-life
    ent_w = min(1.0, 0.4 + 0.2 * n_entities)
    return round(src_w * recency * ent_w, 3)


def _eid(source: str, key: str) -> str:
    return hashlib.sha1(f"{source}|{key}".encode()).hexdigest()[:12]


# ── adapters ───────────────────────────────────────────────────────────
def market_events(prices: pd.DataFrame, now: datetime) -> list[dict]:
    from conditional import zc_frame
    zc = zc_frame(prices)
    out = []
    for sid in zc.columns:
        s = zc[sid].dropna()
        if len(s) < MOVE_MIN_HISTORY:
            continue
        hist = s.abs().iloc[:-1]
        bar = float(hist.quantile(MOVE_QUANTILE))
        z_now = float(s.iloc[-1])
        if abs(z_now) < bar or bar <= 0:
            continue
        pctile = float((hist < abs(z_now)).mean())
        d = s.index[-1]
        out.append({
            "id": _eid("market", f"{sid}|{d:%Y-%m-%d}"),
            "ts": pd.Timestamp(d, tz="UTC").isoformat(),
            "source": "market", "kind": "move",
            "entities": [sid], "topics": [],
            "payload": {"series": sid, "zc": round(z_now, 2),
                        "adaptive_bar": round(bar, 2),
                        "move_pctile": round(pctile, 4),
                        "ret_1d_pct": round(float(
                            prices[sid].pct_change(fill_method=None)
                            .dropna().iloc[-1] * 100), 3)
                        if sid in prices.columns else None},
            "salience": _salience_market(pctile),
        })
    return out


def text_events(now: datetime, lexicon) -> tuple[list[dict], list[dict]]:
    """squawk + rss items → events; also returns join-miss records."""
    from headlines import load_store
    out, misses = [], []
    for it in load_store().get("items", []):
        source = "squawk" if it.get("feed") == "DeItaone" else "rss"
        try:
            ts = datetime.fromisoformat(it["ts"])
        except Exception:
            continue
        ents, topics, layers, wts = tag_text(it["title"], lexicon)
        if not ents and not topics:
            misses.append({"ts": it["ts"], "source": source,
                           "title": it["title"][:160]})
        out.append({
            "id": _eid(source, it["id"]),
            "ts": it["ts"], "source": source, "kind": "headline",
            "entities": ents, "topics": topics,
            "payload": {"title": it["title"], "feed": it.get("feed"),
                        "link": it.get("link", ""), "layers": layers,
                        "store_id": it["id"],
                        "entity_weights": {k: v for k, v in wts.items()
                                           if v != 1.0} or None},
            "salience": _salience_text(source, ts, len(ents), now),
        })
    return out, misses


def release_events(now: datetime) -> list[dict]:
    from release_calendar import build_calendar
    cal = build_calendar()
    out = []
    for r in cal.get("upcoming", []):
        if r["days_until"] > 1:
            continue
        out.append({
            "id": _eid("release", f"{r['name']}|{r['next_date']}"),
            "ts": f"{r['next_date']}T00:00:00+00:00",
            "source": "release", "kind": "scheduled",
            "entities": [], "topics": [f"release:{r['market'].lower()}"],
            "payload": {"name": r["name"], "when": r["next_date"],
                        "threshold": r["threshold"], "url": r["url"],
                        "state": "due"},
            "salience": 0.7 if r["days_until"] == 0 else 0.5,
        })
    for r in cal.get("recent", []):
        out.append({
            "id": _eid("release", f"{r['name']}|{r['released_date']}|out"),
            "ts": f"{r['released_date']}T00:00:00+00:00",
            "source": "release", "kind": "scheduled",
            "entities": [], "topics": [f"release:{r['market'].lower()}"],
            "payload": {"name": r["name"], "when": r["released_date"],
                        "threshold": r["threshold"], "url": r["url"],
                        "state": "released"},
            "salience": 0.8,
        })
    return out


# ── bus build ──────────────────────────────────────────────────────────
def build_bus(prices: pd.DataFrame | None = None) -> dict:
    SYNTH_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    if prices is None:
        prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                             parse_dates=True).sort_index()
    lexicon = _compile_lexicon()

    events: dict[str, dict] = {}
    # keep prior window (stability across ticks)
    if EVENTS_JSON.exists():
        try:
            for e in json.loads(EVENTS_JSON.read_text(encoding="utf-8"))["events"]:
                events[e["id"]] = e
        except Exception:
            pass

    mk = market_events(prices, now)
    tx, misses = text_events(now, lexicon)
    rl = release_events(now)
    for e in mk + tx + rl:
        events[e["id"]] = e          # newest version wins (salience decays)

    cutoff = (now - timedelta(days=EVENT_DAYS)).isoformat()
    kept = [e for e in events.values() if e["ts"] >= cutoff]
    kept.sort(key=lambda e: e["ts"], reverse=True)

    state = {"updated": now.isoformat(),
             "counts": {"market": sum(1 for e in kept if e["source"] == "market"),
                        "squawk": sum(1 for e in kept if e["source"] == "squawk"),
                        "rss": sum(1 for e in kept if e["source"] == "rss"),
                        "release": sum(1 for e in kept if e["source"] == "release")},
             "join_miss_rate": round(len(misses) / max(1, len(tx)), 3),
             "events": kept}
    EVENTS_JSON.write_text(json.dumps(state), encoding="utf-8")

    # rolling miss log (instrumentation for the MiniLM trigger)
    old = []
    if MISSES_JSON.exists():
        try:
            old = json.loads(MISSES_JSON.read_text(encoding="utf-8"))["misses"]
        except Exception:
            pass
    seen = {m["title"] for m in old}
    merged = old + [m for m in misses if m["title"] not in seen]
    MISSES_JSON.write_text(json.dumps(
        {"updated": now.isoformat(), "misses": merged[-MISS_CAP:]}),
        encoding="utf-8")
    return state


def load_bus() -> dict:
    if EVENTS_JSON.exists():
        try:
            return json.loads(EVENTS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"events": [], "counts": {}}


if __name__ == "__main__":
    st = build_bus()
    c = st["counts"]
    print(f"event bus: {sum(c.values())} events "
          f"(market {c['market']} · squawk {c['squawk']} · rss {c['rss']} · "
          f"release {c['release']}) | join-miss rate {st['join_miss_rate']}")
    for e in st["events"][:10]:
        ents = ",".join(e["entities"][:4]) or "-"
        print(f"  [{e['source']:7}] sal {e['salience']:.2f} ents[{ents}] "
              f"{str(e['payload'].get('title') or e['payload'].get('series') or e['payload'].get('name'))[:70]}")
