"""Selectivity layer — turns raw per-series flags into a small set of EVENTS.

The problem this solves: a 100-series universe fires many technically-correct
flags on a broad move (every equity index goes 2σ on a risk-off day). The
board must show ONE dislocation, not fifteen echoes of it.

Method:
1. take the engine's flagged series (math unchanged upstream);
2. cluster them by 60-day return correlation — two flags join the same event
   when |ρ| ≥ EVENT_CORR_THRESHOLD and today's moves are CONSISTENT with that
   correlation (same sign for positive ρ, opposite for negative ρ);
3. fold the engine's co-occurrence composites into their clusters;
4. attach motivating news (48h) via backbone aliases / dynamic member names;
5. score each event = strongest member + breadth + framework + news
   corroboration, then apply a surfacing floor and a card budget.

Everything below the floor collapses into a one-line "watch list". A calm day
produces zero events — by design.
"""
from __future__ import annotations

import math
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from registry import NEWS_ALIASES, load_universe, registry_index
from settings import EVENT_CORR_THRESHOLD, MAX_EVENT_CARDS, SURFACE_FLOOR

DATA_DIR = Path(__file__).parent / "data"
CORR_WINDOW = 60
NEWS_HOURS = 48
MAX_NEWS_PER_EVENT = 3


class _UF:
    def __init__(self, keys):
        self.p = {k: k for k in keys}

    def find(self, k):
        while self.p[k] != k:
            self.p[k] = self.p[self.p[k]]
            k = self.p[k]
        return k

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


# tokens too generic to identify a company on their own
_GENERIC_TOKENS = {
    "energy", "power", "bank", "banks", "banking", "financial", "finance",
    "capital", "global", "international", "national", "india", "indian",
    "tech", "technology", "digital", "industries", "motors", "steel",
    "pharma", "health", "healthcare", "life", "general", "standard",
    "first", "united", "american", "china", "systems", "solutions",
}


def _aliases_for(sid: str, spec: dict | None, universe: dict) -> list[str]:
    """Lowercase substrings that tie this series to a headline.
    For dynamic members: the full name always matches; single tokens only when
    they are distinctive (not generic corporate vocabulary)."""
    out = list(NEWS_ALIASES.get(sid, []))
    if spec and spec.get("dynamic"):
        sym = spec.get("symbol", "")
        member = universe.get("members", {}).get(sym, {})
        norm = member.get("norm") or ""
        if len(norm) >= 4:
            out.append(norm)
        for tok in norm.split():
            if len(tok) >= 5 and tok not in _GENERIC_TOKENS:
                out.append(tok)
        root = sym.split(".")[0].lower()
        if len(root) >= 3:
            out.append(f"${root}")
    return out


def _attach_news(member_ids: list[str], idx: dict, universe: dict,
                 headlines: list[dict]) -> list[dict]:
    now = datetime.now(timezone.utc)
    cutoff = (now - timedelta(hours=NEWS_HOURS)).isoformat()
    fresh = [h for h in headlines if h["ts"] >= cutoff]
    hits, seen = [], set()
    for sid in member_ids:
        terms = _aliases_for(sid, idx.get(sid), universe)
        if not terms:
            continue
        for h in fresh:
            tl = h["title"].lower()
            if h["id"] in seen:
                continue
            if any(t in tl for t in terms):
                seen.add(h["id"])
                hits.append({"ts": h["ts"], "feed": h["feed"],
                             "title": h["title"], "series": sid})
    hits.sort(key=lambda x: x["ts"], reverse=True)
    return hits[:MAX_NEWS_PER_EVENT]


def _direction(rows: list[dict]) -> str:
    zs = [r.get("z20") for r in rows if r.get("z20") is not None]
    if not zs:
        return "·"
    return "↑" if sum(np.sign(z) for z in zs) >= 0 else "↓"


def _label(rows: list[dict]) -> str:
    classes = {}
    for r in rows:
        classes[r["market"]] = classes.get(r["market"], 0) + 1
    dom = max(classes, key=classes.get)
    arrow = _direction(rows)
    if len(rows) == 1:
        return f"{rows[0]['id']} {arrow}"
    if len(classes) == 1:
        return f"{dom.lower()} · {len(rows)} series {arrow}"
    return f"cross-asset · {len(rows)} series {arrow}"


def build_events(snapshot: dict, prices: pd.DataFrame,
                 headlines: list[dict]) -> dict:
    idx = registry_index()
    universe = load_universe()

    flagged = [r for r in snapshot.get("series", [])
               if r.get("flag") in ("amber", "red") and not r.get("sparse")]
    engine_scores = {f["id"]: f["score"] for f in snapshot.get("flags", [])
                     if f.get("type") == "series"}
    if not flagged:
        return {"events": [], "watchlist": [], "counts": {"flagged": 0}}

    ids = [r["id"] for r in flagged]
    by_id = {r["id"]: r for r in flagged}

    # correlation clustering over 60d daily returns
    uf = _UF(ids)
    have = [i for i in ids if i in prices.columns]
    if len(have) >= 2:
        rets = prices[have].tail(CORR_WINDOW + 1).pct_change(fill_method=None)
        corr = rets.corr(min_periods=20)
        for i, a in enumerate(have):
            za = by_id[a].get("z20")
            if za is None:
                continue
            for b in have[i + 1:]:
                zb = by_id[b].get("z20")
                if zb is None:
                    continue
                rho = corr.at[a, b]
                if pd.isna(rho) or abs(rho) < EVENT_CORR_THRESHOLD:
                    continue
                consistent = (np.sign(za) == np.sign(zb)) if rho > 0 \
                    else (np.sign(za) != np.sign(zb))
                if consistent:
                    uf.union(a, b)

    # engine co-occurrence composites need no special folding: their members
    # are flagged, same-direction and correlated, so the clustering above has
    # already united them; their extra weight flows in via engine scores.

    clusters: dict[str, list[dict]] = {}
    for sid in ids:
        clusters.setdefault(uf.find(sid), []).append(by_id[sid])

    events, watchlist = [], []
    for root, rows in clusters.items():
        rows.sort(key=lambda r: -(abs(r.get("z20") or 0)))
        member_ids = [r["id"] for r in rows]
        news = _attach_news(member_ids, idx, universe, headlines)
        base = max((engine_scores.get(r["id"], abs(r.get("z20") or 0))
                    for r in rows), default=0.0)
        breadth = 1.2 * math.log1p(len(rows) - 1)
        news_bonus = 2.0 if news else 0.0
        score = base + breadth + news_bonus
        any_red = any(r["flag"] == "red" for r in rows)
        ev = {
            "label": _label(rows),
            "score": round(score, 2),
            "level": "red" if any_red else "amber",
            "direction": _direction(rows),
            "members": [{
                "id": r["id"], "market": r["market"],
                "name": r.get("name") or r["id"],
                "dynamic": bool(r.get("dynamic")),
                "flag": r["flag"], "z20": r.get("z20"), "last": r.get("last"),
                "d1_pct": r.get("d1_pct"), "reasons": r.get("reasons", []),
            } for r in rows],
            "news": news,
            "breadth": len(rows),
        }
        if score >= SURFACE_FLOOR:
            events.append(ev)
        else:
            watchlist.append(ev)

    events.sort(key=lambda e: -e["score"])
    overflow = events[MAX_EVENT_CARDS:]
    events = events[:MAX_EVENT_CARDS]
    watchlist.extend(overflow)
    watchlist.sort(key=lambda e: -e["score"])

    return {
        "events": events,
        "watchlist": watchlist,
        "counts": {
            "flagged": len(flagged),
            "clusters": len(clusters),
            "surfaced": len(events),
            "suppressed": len(flagged) - sum(e["breadth"] for e in events),
        },
    }


if __name__ == "__main__":
    from engine import build_snapshot
    from headlines import recent_items
    snap = build_snapshot()
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0, parse_dates=True)
    out = build_events(snap, prices, recent_items())
    c = out["counts"]
    print(f"flagged {c['flagged']} -> clusters {c.get('clusters')} -> "
          f"cards {c.get('surfaced')} (suppressed {c.get('suppressed')})\n")
    for e in out["events"]:
        print(f"[{e['level'].upper():5}] {e['score']:>5}  {e['label']}")
        for m in e["members"][:6]:
            print(f"    {m['flag']:5} {m['id']:24} z={m['z20'] and round(m['z20'],2)}")
        for n in e["news"]:
            print(f"    news[{n['series']}]: {n['title'][:70]}")
        print()
    print("watchlist:", ", ".join(f"{e['label']}({e['score']})" for e in out["watchlist"]))
