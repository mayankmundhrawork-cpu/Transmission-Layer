"""P6 — spread / mean-reversion module (half-life implemented; cointegration TODO).

For ratio/spread series (DERIVED class): stationarity evidence (ADF) and the
OU half-life of mean reversion, turning "z20=2.3" into "spread at Xσ,
half-life ≈ N days" — horizon-aware and actionable.

Method: discrete AR(1) on the spread, s_t − s_{t-1} = a + b·s_{t-1} + e;
half-life = −ln(2)/ln(1+b) for −1 < b < 0. ADF p-value from statsmodels.
n≈500 daily obs makes these estimates coarse — reported, with n, never
hidden.

TODO (P6 remainder): Engle-Granger/Johansen for candidate PAIRS (not just
predefined ratios); Hurst exponent; rolling half-life stability.

Run: python spreads.py
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
STATE_JSON = DATA_DIR / "spreads_state.json"

MIN_OBS = 120


def ou_half_life(s: pd.Series) -> tuple[float | None, int]:
    """AR(1) mean-reversion half-life in trading days (None if not reverting)."""
    s = s.dropna()
    n = len(s)
    if n < MIN_OBS:
        return None, n
    lag = s.shift(1).iloc[1:]
    diff = s.diff().iloc[1:]
    X = np.column_stack([np.ones(len(lag)), lag.to_numpy()])
    coef, *_ = np.linalg.lstsq(X, diff.to_numpy(), rcond=None)
    b = float(coef[1])
    if not (-1.0 < b < 0.0):
        return None, n     # no mean reversion detected in-sample
    return float(-np.log(2) / np.log(1 + b)), n


def adf_pvalue(s: pd.Series) -> float | None:
    try:
        from statsmodels.tsa.stattools import adfuller
        s = s.dropna()
        if len(s) < MIN_OBS:
            return None
        return round(float(adfuller(s, autolag="AIC")[1]), 4)
    except Exception:
        return None


def build_spreads(prices: pd.DataFrame | None = None) -> dict:
    from registry import load_registry
    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    out: dict[str, dict] = {}
    for spec in load_registry():
        if spec["market"] != "DERIVED" or spec["id"] not in prices.columns:
            continue
        s = prices[spec["id"]].dropna()
        if len(s) < MIN_OBS:
            continue
        hl, n = ou_half_life(s)
        mu, sd = s.tail(252).mean(), s.tail(252).std(ddof=0)
        sigma_now = None if sd == 0 else round(float((s.iloc[-1] - mu) / sd), 2)
        out[spec["id"]] = {
            "asof": s.index[-1].strftime("%Y-%m-%d"),
            "last": round(float(s.iloc[-1]), 4),
            "sigma_vs_1y": sigma_now,
            "half_life_days": None if hl is None else round(hl, 1),
            "adf_p": adf_pvalue(s),
            "n_obs": n,
        }
    state = {"updated": datetime.now(timezone.utc).isoformat(), "series": out}
    STATE_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_spreads() -> dict:
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"series": {}}


if __name__ == "__main__":
    st = build_spreads()
    for sid, r in st["series"].items():
        print(f"  {sid:24} {r['sigma_vs_1y']:+.2f} sigma vs 1y | "
              f"half-life {r['half_life_days']}d | ADF p={r['adf_p']} "
              f"(n={r['n_obs']})" if r['sigma_vs_1y'] is not None else f"  {sid}")
