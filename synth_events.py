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
MOVE_MIN_HISTORY = 180    # sessions of |zc| needed to trust the adaptive bar
MOVE_FLOOR_HISTORY = 60   # below this there is no market event at all
MOVE_FIXED_BAR = 3.0      # conservative bar used between floor and full hist
MOVE_STALE_SESSIONS = 1   # a series' last bar must be this fresh to fire live
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
def _move_event(sid: str, s: pd.Series, rets: pd.Series, pos: int) -> dict | None:
    """One market event for series `sid` at integer position `pos` of its own
    |zc| series, judged ONLY on history strictly before pos (point-in-time).
    Returns None when the bar is not cleared. Shared by the live adapter and
    the historical backfill so a reconstructed trigger is the same object the
    live tick would have emitted."""
    if pos < MOVE_FLOOR_HISTORY:
        return None                       # ruling 5: no event below the floor
    hist = s.abs().iloc[:pos]
    z_now = float(s.iloc[pos])
    # Short history makes a q98 estimate of a series' own tail unreliable
    # (it is one of ~3 observations). Below MOVE_MIN_HISTORY the bar is a
    # conservative fixed one and the event carries low_history: True.
    low_history = pos < MOVE_MIN_HISTORY
    bar = MOVE_FIXED_BAR if low_history else float(hist.quantile(MOVE_QUANTILE))
    if bar <= 0 or abs(z_now) < bar:
        return None
    pctile = float((hist < abs(z_now)).mean())
    d = s.index[pos]
    ret = rets.get(d)
    return {
        "id": _eid("market", f"{sid}|{d:%Y-%m-%d}"),
        "ts": pd.Timestamp(d, tz="UTC").isoformat(),
        "source": "market", "kind": "move",
        "entities": [sid], "topics": [],
        "payload": {"series": sid, "zc": round(z_now, 2),
                    "adaptive_bar": round(bar, 2),
                    "bar_kind": "fixed" if low_history else "adaptive",
                    "low_history": low_history,
                    "history_n": int(pos + 1),
                    "move_pctile": round(pctile, 4),
                    "ret_1d_pct": None if ret is None or pd.isna(ret)
                    else round(float(ret) * 100, 3)},
        # short history => the percentile itself is a weak estimate, so
        # the event enters the bus discounted rather than suppressed
        "salience": round(_salience_market(pctile) *
                          (0.5 if low_history else 1.0), 3),
    }


def market_events(prices: pd.DataFrame, now: datetime) -> list[dict]:
    """Live adapter: events on the latest bar only.

    A series whose feed has gone quiet still has a "last observation", and
    without the staleness guard its final big move would be re-emitted on
    every tick forever. Only bars within MOVE_STALE_SESSIONS of the matrix's
    own latest date count as live."""
    from conditional import zc_frame
    zc = zc_frame(prices)
    rets = prices.pct_change(fill_method=None)
    cal = prices.index.sort_values()
    fresh_from = cal[max(0, len(cal) - 1 - MOVE_STALE_SESSIONS)]
    out = []
    for sid in zc.columns:
        s = zc[sid].dropna()
        if not len(s) or s.index[-1] < fresh_from:
            continue
        e = _move_event(sid, s, rets.get(sid, pd.Series(dtype=float)), len(s) - 1)
        if e:
            out.append(e)
    return out


def market_events_backfill(prices: pd.DataFrame, sessions: int = 10,
                           zc: pd.DataFrame | None = None) -> list[dict]:
    """Replay the market adapter over the last `sessions` bars.

    The live adapter only ever sees the newest bar, so a bus assembled from a
    frozen snapshot contains whatever happened to be captured live. Detectors
    and base rates need the triggers that WOULD have fired (ruling 8), so this
    re-runs the identical bar per session with strictly-prior history."""
    from conditional import zc_frame
    if zc is None:
        zc = zc_frame(prices)
    rets = prices.pct_change(fill_method=None)
    out = []
    for sid in zc.columns:
        s = zc[sid].dropna()
        r = rets[sid] if sid in rets.columns else pd.Series(dtype=float)
        for pos in range(max(0, len(s) - sessions), len(s)):
            e = _move_event(sid, s, r, pos)
            if e:
                out.append(e)
    out.sort(key=lambda e: e["ts"], reverse=True)
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
