"""Historical pattern search & event replay (v5 feature 5).

Makes two years of per-series history queryable by PATTERN:
  find_matches(conditions)      dates where all conditions held (AND),
                                clustered so one episode counts once
  aftermath(dates, responses)   forward stats at +5/+20 sessions per response:
                                median, hit-rate, range, median path
  analogues_for_event(...)      nearest historical z-vector analogues for a
                                live event — "today most resembles ..."

Condition metrics: z20 (engine-consistent rolling z), level, d1pct, pctile
(1y percentile). Operators: >= and <=. All computed vectorized over the
committed prices.csv; nothing here touches the core.

Run: python patterns.py   (self-test over live data)
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from settings import ANALOGUE_TOP, PATTERN_HORIZONS, PATTERN_MIN_GAP

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"
CACHE_JSON = DATA_DIR / "pattern_cache.json"
CACHE_MAX = 120

Z_WIN = 20      # engine Z_WIN_SHORT semantics: today vs the PRIOR 20 sessions
PCT_WIN = 252


# ── vectorized metric matrices ─────────────────────────────────────────
def load_prices() -> pd.DataFrame:
    return pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()


def metric_frame(prices: pd.DataFrame, metric: str) -> pd.DataFrame:
    if metric == "level":
        return prices
    if metric == "z20":
        m = prices.shift(1).rolling(Z_WIN).mean()
        sd = prices.shift(1).rolling(Z_WIN).std(ddof=0)
        return (prices - m) / sd
    if metric == "d1pct":
        return prices.pct_change(fill_method=None) * 100.0
    if metric == "pctile":
        return prices.rolling(PCT_WIN, min_periods=60).rank(pct=True) * 100.0
    raise ValueError(f"unknown metric {metric}")


# ── query engine ───────────────────────────────────────────────────────
def _cluster(dates: pd.DatetimeIndex, min_gap: int,
             index: pd.DatetimeIndex) -> list[pd.Timestamp]:
    """Collapse runs of matching dates into episode starts (>=min_gap apart)."""
    pos = {d: i for i, d in enumerate(index)}
    out, last_i = [], None
    for d in dates:
        i = pos.get(d)
        if i is None:
            continue
        if last_i is None or i - last_i >= min_gap:
            out.append(d)
        last_i = i
    return out


def find_matches(prices: pd.DataFrame, conditions: list[dict],
                 min_gap: int = PATTERN_MIN_GAP) -> list[pd.Timestamp]:
    """conditions: [{series, metric, op('>='|'<='), value}] AND-ed."""
    mask = pd.Series(True, index=prices.index)
    for c in conditions:
        sid = c["series"]
        if sid not in prices.columns:
            return []
        mf = metric_frame(prices, c["metric"])[sid]
        cond = mf >= c["value"] if c["op"] == ">=" else mf <= c["value"]
        mask &= cond.fillna(False)
    return _cluster(prices.index[mask], min_gap, prices.index)


def aftermath(prices: pd.DataFrame, dates: list[pd.Timestamp],
              response_ids: list[str],
              horizons: tuple[int, ...] = PATTERN_HORIZONS) -> dict:
    """Forward % moves of each response series after each match date."""
    idx = prices.index
    pos = {d: i for i, d in enumerate(idx)}
    out: dict[str, dict] = {}
    max_h = max(horizons)
    for rid in response_ids:
        if rid not in prices.columns:
            continue
        s = prices[rid]
        per_h: dict[int, list[float]] = {h: [] for h in horizons}
        paths: list[list[float]] = []
        for d in dates:
            i = pos.get(d)
            if i is None or s.iloc[i] != s.iloc[i] or s.iloc[i] == 0:
                continue
            base = s.iloc[i]
            for h in horizons:
                if i + h < len(idx) and s.iloc[i + h] == s.iloc[i + h]:
                    per_h[h].append((s.iloc[i + h] / base - 1) * 100.0)
            path = [(s.iloc[i + k] / base - 1) * 100.0
                    for k in range(0, min(max_h, len(idx) - 1 - i) + 1)
                    if s.iloc[i + k] == s.iloc[i + k]]
            if len(path) >= 3:
                paths.append(path)
        stats = {}
        for h, vals in per_h.items():
            if not vals:
                continue
            arr = np.array(vals)
            stats[f"+{h}d"] = {
                "n": len(arr),
                "median_pct": round(float(np.median(arr)), 2),
                "hit_rate_up": round(float((arr > 0).mean()), 2),
                "min_pct": round(float(arr.min()), 2),
                "max_pct": round(float(arr.max()), 2),
            }
        median_path = []
        if paths:
            L = min(len(p) for p in paths)
            median_path = [round(float(np.median([p[k] for p in paths])), 2)
                           for k in range(L)]
        out[rid] = {"stats": stats, "median_path": median_path}
    return out


def run_query(conditions: list[dict], response_ids: list[str],
              prices: pd.DataFrame | None = None) -> dict:
    """Cached end-to-end query."""
    prices = prices if prices is not None else load_prices()
    data_date = prices.index.max().strftime("%Y-%m-%d")
    key = hashlib.sha1(json.dumps(
        [conditions, sorted(response_ids), data_date],
        sort_keys=True, default=str).encode()).hexdigest()[:16]
    cache = _load_cache()
    if key in cache:
        return cache[key]
    dates = find_matches(prices, conditions)
    res = {
        "key": key, "data_date": data_date,
        "conditions": conditions, "responses": sorted(response_ids),
        "match_dates": [d.strftime("%Y-%m-%d") for d in dates],
        "n_matches": len(dates),
        "aftermath": aftermath(prices, dates, response_ids) if dates else {},
        "computed_at": datetime.now(timezone.utc).isoformat(),
    }
    cache[key] = res
    _save_cache(cache)
    return res


# ── event replay / analogues ───────────────────────────────────────────
def analogues_for_event(member_ids: list[str],
                        prices: pd.DataFrame | None = None,
                        responses: list[str] | None = None,
                        top: int = ANALOGUE_TOP) -> dict:
    """Historical dates whose member z-vector most resembles today's.
    Excludes the trailing 10 sessions; episode-deduped; returns aftermath of
    the members plus core macro responses."""
    prices = prices if prices is not None else load_prices()
    members = [m for m in member_ids if m in prices.columns]
    if not members:
        return {"analogues": []}
    Z = metric_frame(prices, "z20")[members]
    # per-member last VALID z: series pause on different holidays, so the
    # global last index row can be NaN for a subset (e.g. CBOT closed while
    # NY trades). A <=2-session skew is acceptable for similarity search.
    today = pd.Series({m: (Z[m].dropna().iloc[-1] if Z[m].notna().any()
                           else np.nan) for m in members})
    members = [m for m in members if today[m] == today[m]]
    if not members:
        return {"analogues": []}
    Z, today = Z[members], today[members]
    hist = Z.iloc[:-10].dropna()
    if len(hist) < 30:
        return {"analogues": []}
    dist = np.sqrt(((hist - today) ** 2).sum(axis=1) / len(members))
    ranked = dist.sort_values()
    picked: list[pd.Timestamp] = []
    pos = {d: i for i, d in enumerate(prices.index)}
    for d in ranked.index:
        if len(picked) >= top:
            break
        if all(abs(pos[d] - pos[p]) >= PATTERN_MIN_GAP for p in picked):
            picked.append(d)
    responses = responses or list(dict.fromkeys(
        members + ["sp500", "hy_oas", "dxy", "comex_gold"]))
    responses = [r for r in responses if r in prices.columns]
    am = aftermath(prices, picked, responses)
    return {
        "member_z_today": {m: round(float(today[m]), 2) for m in members},
        "analogues": [{
            "date": d.strftime("%Y-%m-%d"),
            "distance": round(float(dist[d]), 2),
            "member_z": {m: round(float(hist.loc[d, m]), 2) for m in members},
        } for d in picked],
        "aftermath": am,
    }


# ── cache ──────────────────────────────────────────────────────────────
def _load_cache() -> dict:
    if CACHE_JSON.exists():
        try:
            return json.loads(CACHE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_cache(cache: dict) -> None:
    if len(cache) > CACHE_MAX:
        items = sorted(cache.items(),
                       key=lambda kv: kv[1].get("computed_at", ""), reverse=True)
        cache = dict(items[:CACHE_MAX])
    CACHE_JSON.write_text(json.dumps(cache), encoding="utf-8")


if __name__ == "__main__":
    prices = load_prices()
    # the user's own example: 10y moves >=8bps in a session -> DXY next week?
    q = run_query(
        conditions=[{"series": "ust_10y", "metric": "d1pct", "op": ">=", "value": 2.0}],
        response_ids=["dxy", "comex_gold", "sp500"], prices=prices)
    print(f"query: ust_10y 1d >= +2% -> {q['n_matches']} episodes")
    for rid, r in q["aftermath"].items():
        print(f"  {rid:12} {r['stats']}")
    # analogue self-test on a live event
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    snap = build_snapshot()
    ev = build_events(snap, prices, recent_items())
    if ev["events"]:
        e = ev["events"][0]
        a = analogues_for_event([m["id"] for m in e["members"]], prices)
        print(f"\nanalogues for '{e['label']}': z today {a['member_z_today']}")
        for an in a["analogues"]:
            print(f"  {an['date']} dist={an['distance']} z={an['member_z']}")
