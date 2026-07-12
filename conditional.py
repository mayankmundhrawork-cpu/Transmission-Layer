"""P2 — conditional statistics: vol-standardised return z-scores.

Replaces the *gate* role of the naive levels-z (which drowns a 2-sigma move
in a quiet regime inside a noisy 20-day lookback) with:

  zc_t = r_t / sigma_{t|t-1}

where sigma is EWMA (RiskMetrics lambda=0.94) volatility computed from
returns STRICTLY BEFORE t — point-in-time by construction. The full-history
zc matrix is cheap, vectorised and deterministic, so it also serves
patterns/backtests. GARCH(1,1) (`arch`) refines the LATEST sigma per series
when available (CI); on failure/timeout the EWMA figure stands. Monthly /
sparse series are excluded — conditional stats are for daily series only.

Levels-z (z20) is retained everywhere for display continuity; zc is the
anomaly gate input. Run: python conditional.py
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"
COND_JSON = DATA_DIR / "conditional.json"

EWMA_LAMBDA = 0.94
MIN_OBS = 60            # returns needed before zc is emitted
GARCH_MIN_OBS = 250     # returns needed before a GARCH fit is attempted
GARCH_TIME_BUDGET = 45  # seconds across ALL fits per run


def daily_ids() -> list[str]:
    """Series eligible for conditional stats (daily/eod, non-derived)."""
    from registry import load_registry
    return [s["id"] for s in load_registry()
            if s.get("freq") in ("eod", "daily") and s["source"] != "derived"]


def ewma_sigma(rets: pd.DataFrame, lam: float = EWMA_LAMBDA) -> pd.DataFrame:
    """sigma_{t|t-1}: EWMA std of squared returns THROUGH t-1 (PIT).
    ewm(alpha=1-lam, adjust=False) reproduces the RiskMetrics recursion
    sigma2_t = lam*sigma2_{t-1} + (1-lam)*r2_t; shifting by one bar makes
    the estimate strictly prior to the return it standardises."""
    r2 = rets.pow(2)
    sigma2 = r2.ewm(alpha=1 - lam, adjust=False).mean().shift(1)
    return np.sqrt(sigma2)


def zc_frame(prices: pd.DataFrame, ids: list[str] | None = None) -> pd.DataFrame:
    """Full-history vol-conditional return z matrix (EWMA-based, PIT)."""
    cols = [c for c in (ids or prices.columns) if c in prices.columns]
    rets = prices[cols].pct_change(fill_method=None)
    sig = ewma_sigma(rets)
    zc = rets / sig
    # first MIN_OBS observations per column are unreliable — mask them
    counts = rets.notna().cumsum()
    return zc.where(counts >= MIN_OBS)


def _garch_sigma_latest(ret: pd.Series) -> float | None:
    """One-step-ahead GARCH(1,1) sigma for the LAST return (fit excludes it).
    Returns None on any failure — EWMA stands. Deterministic given data."""
    try:
        from arch import arch_model
    except ImportError:
        return None
    r = ret.dropna() * 100.0  # rescale for optimiser stability
    if len(r) < GARCH_MIN_OBS:
        return None
    try:
        am = arch_model(r.iloc[:-1], mean="Zero", vol="GARCH", p=1, q=1,
                        rescale=False)
        res = am.fit(disp="off", show_warning=False,
                     options={"maxiter": 200})
        f = res.forecast(horizon=1, reindex=False)
        sig = float(np.sqrt(f.variance.values[-1, 0])) / 100.0
        if not np.isfinite(sig) or sig <= 0:
            return None
        return sig
    except Exception:
        return None


def build_conditional(prices: pd.DataFrame | None = None) -> dict:
    """Latest conditional snapshot per daily series; persisted for the app."""
    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    ids = [c for c in daily_ids() if c in prices.columns]
    rets = prices[ids].pct_change(fill_method=None)
    sig_ewma = ewma_sigma(rets)

    out: dict[str, dict] = {}
    t0 = time.monotonic()
    garch_fits = 0
    for sid in ids:
        r = rets[sid].dropna()
        if len(r) < MIN_OBS:
            continue
        last_ret = float(r.iloc[-1])
        # PIT sigma aligned to the date of the last return
        se = sig_ewma[sid].reindex(r.index).iloc[-1]
        if not np.isfinite(se) or se <= 0:
            continue
        sg = None
        if time.monotonic() - t0 < GARCH_TIME_BUDGET:
            sg = _garch_sigma_latest(r)
            if sg is not None:
                garch_fits += 1
        sigma = sg if sg is not None else float(se)
        out[sid] = {
            "ret_1d_pct": round(last_ret * 100.0, 3),
            "sigma_ewma_pct": round(float(se) * 100.0, 3),
            "sigma_garch_pct": None if sg is None else round(sg * 100.0, 3),
            "zc": round(last_ret / sigma, 2),
            "zc_ewma": round(last_ret / float(se), 2),
            "method": "garch" if sg is not None else "ewma",
            "asof": r.index[-1].strftime("%Y-%m-%d"),
        }
    state = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "lambda": EWMA_LAMBDA,
        "garch_fits": garch_fits,
        "series": out,
    }
    COND_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_conditional() -> dict:
    if COND_JSON.exists():
        try:
            return json.loads(COND_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"series": {}}


if __name__ == "__main__":
    st = build_conditional()
    rows = st["series"]
    print(f"conditional: {len(rows)} series, {st['garch_fits']} garch fits")
    ranked = sorted(rows.items(), key=lambda kv: -abs(kv[1]["zc"]))
    for sid, r in ranked[:8]:
        print(f"  {sid:22} zc={r['zc']:+5.2f} ({r['method']}) "
              f"ret={r['ret_1d_pct']:+.2f}% sigma={r['sigma_ewma_pct']:.2f}%")
