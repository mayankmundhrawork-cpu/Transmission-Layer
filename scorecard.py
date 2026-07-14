"""P9 — signal-type hit-rate ledger (implemented).

Replays each signal TYPE against realised forward moves over the full
committed history and stores its precision, so every emitted record carries
"this signal type: X% hit rate, n=N" — a plausible thesis with a 45% track
record must say so.

Signal types measured:

  residual_reversion   |resid_z| >= 2 episodes (5-session dedupe): hit when
                       the instrument's forward 5d return moves AGAINST the
                       residual (unexplained moves mean-revert).
  transmission_follow  lead-pairs: significance estimated on the FIRST HALF
                       of the sample only (no lookahead into evaluation);
                       on the second half, driver days with EWMA-|zc| >= 1.5
                       are events; hit when the target's next-k cumulative
                       return matches sign(beta) x sign(driver move).
  spread_reversion     derived spreads: |dev| >= 2 vs PIT rolling 252d
                       mean/std; hit when |dev| shrinks by >= 25% within
                       max(half-life, 10) sessions.

Caveats stored with the numbers: n is small (2y of dailies), estimates are
in-sample for residual/spread types (episode-level, PIT inputs), and
precision is a base rate, not an edge. Run: python scorecard.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"
STATE_JSON = DATA_DIR / "scorecard.json"

RZ_BAR = 2.0
ZC_BAR = 1.5
DEDUPE = 5
FWD = 5


def _episodes(mask: pd.Series, min_gap: int = DEDUPE) -> list[pd.Timestamp]:
    out, last_i = [], None
    idx = mask.index
    pos = {d: i for i, d in enumerate(idx)}
    for d in idx[mask.fillna(False)]:
        i = pos[d]
        if last_i is None or i - last_i >= min_gap:
            out.append(d)
        last_i = i
    return out


def _fwd_ret(prices: pd.Series, d: pd.Timestamp, horizon: int) -> float | None:
    s = prices.dropna()
    if d not in s.index:
        return None
    i = s.index.get_loc(d)
    if i + horizon >= len(s):
        return None
    return float(s.iloc[i + horizon] / s.iloc[i] - 1)


def score_residual_reversion(prices: pd.DataFrame) -> dict:
    from factors import factor_set, resid_z_series
    from registry import load_registry
    rets = prices.pct_change(fill_method=None)
    n, hits = 0, 0
    for spec in load_registry():
        sid = spec["id"]
        fs = factor_set(spec)
        if not fs or sid not in rets.columns:
            continue
        fs = [f for f in fs if f in rets.columns]
        if len(fs) < 2:
            continue
        rz = resid_z_series(rets[sid], rets[fs])
        if rz.empty:
            continue
        resid_sign = np.sign(rz)
        for d in _episodes(rz.abs() >= RZ_BAR):
            fr = _fwd_ret(prices[sid], d, FWD)
            if fr is None:
                continue
            n += 1
            if np.sign(fr) == -resid_sign.loc[d]:
                hits += 1
    return {"n": n, "hits": hits,
            "hit_rate": None if n == 0 else round(hits / n, 3),
            "definition": f"|resid_z|>={RZ_BAR} -> fwd {FWD}d return opposes residual"}


def score_transmission_follow(prices: pd.DataFrame) -> dict:
    """Split-sample: pair significance from the first half only; events
    evaluated on the second half. No lookahead into the evaluation window."""
    import statsmodels.api as sm
    from conditional import ewma_sigma
    from leadlag import MIN_CORR, _best_lag
    from relations import load_relations

    rets = prices.pct_change(fill_method=None)
    sig = ewma_sigma(rets)
    zc = rets / sig
    half = len(prices) // 2

    n, hits = 0, 0
    seen = set()
    for p in load_relations().get("pairs", []):
        if p.get("lead_rho") is None or abs(p["lead_rho"]) < MIN_CORR:
            continue
        drv, tgt = p["leader"], p["follower"]
        if (drv, tgt) in seen or drv not in rets.columns or tgt not in rets.columns:
            continue
        seen.add((drv, tgt))
        dr1, tg1 = rets[drv].iloc[:half], rets[tgt].iloc[:half]
        k, ccf = _best_lag(dr1, tg1, 5)
        if k is None or abs(ccf) < MIN_CORR:
            continue
        df1 = pd.concat([dr1.shift(k).rename("d"), tg1.rename("t")], axis=1).dropna()
        if len(df1) < 100:
            continue
        res = sm.OLS(df1["t"], sm.add_constant(df1["d"])).fit(
            cov_type="HAC", cov_kwds={"maxlags": k})
        if float(res.pvalues["d"]) >= 0.05:
            continue
        beta_sign = np.sign(float(res.params["d"]))
        # evaluate on the second half
        z2 = zc[drv].iloc[half:]
        for d in _episodes(z2.abs() >= ZC_BAR, min_gap=k):
            i = prices.index.get_loc(d)
            if i + k >= len(prices):
                continue
            tg_path = rets[tgt].iloc[i + 1:i + 1 + k].dropna()
            if tg_path.empty:
                continue
            n += 1
            expected_sign = beta_sign * np.sign(z2.loc[d])
            if np.sign(tg_path.sum()) == expected_sign:
                hits += 1
    return {"n": n, "hits": hits,
            "hit_rate": None if n == 0 else round(hits / n, 3),
            "definition": (f"first-half-significant lead pairs; driver |zc|>="
                           f"{ZC_BAR} on 2nd half -> target next-k cum ret "
                           f"matches beta-implied sign")}


def score_spread_reversion(prices: pd.DataFrame) -> dict:
    from registry import load_registry
    from spreads import ou_half_life
    n, hits = 0, 0
    for spec in load_registry():
        if spec["market"] != "DERIVED" or spec["id"] not in prices.columns:
            continue
        s = prices[spec["id"]].dropna()
        if len(s) < 300:
            continue
        mu = s.shift(1).rolling(252, min_periods=120).mean()
        sd = s.shift(1).rolling(252, min_periods=120).std(ddof=0)
        dev = ((s - mu) / sd).dropna()
        hl, _ = ou_half_life(s)
        horizon = int(max(min(hl or 20, 40), 10))
        for d in _episodes(dev.abs() >= 2.0):
            i = dev.index.get_loc(d)
            if i + horizon >= len(dev):
                continue
            n += 1
            if abs(dev.iloc[i + horizon]) <= 0.75 * abs(dev.loc[d]):
                hits += 1
    return {"n": n, "hits": hits,
            "hit_rate": None if n == 0 else round(hits / n, 3),
            "definition": "|dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% "
                          "within max(half-life,10) sessions"}


def evaluate(prices: pd.DataFrame | None = None) -> dict:
    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    state = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "caveats": ["~2y daily history: n is small; base rates not edges",
                    "residual/spread types are episode-level in-sample with "
                    "PIT inputs; transmission type is split-sample"],
        "types": {
            "residual_reversion": score_residual_reversion(prices),
            "transmission_follow": score_transmission_follow(prices),
            "spread_reversion": score_spread_reversion(prices),
        },
    }
    STATE_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_scorecard() -> dict:
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"types": {}}


if __name__ == "__main__":
    st = evaluate()
    for t, r in st["types"].items():
        print(f"  {t:22} hit-rate {r['hit_rate']} (n={r['n']}) — {r['definition']}")
