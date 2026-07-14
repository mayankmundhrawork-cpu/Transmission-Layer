"""P3 — factor/residual engine: the mechanical "priced vs unexplained" test.

For each instrument, roll a 60d OLS of its daily returns on its configured
factor block (factors.yaml). Point-in-time: the betas estimated on the
window ENDING t-1 are applied to day-t factor returns, so the prediction
never sees the day it explains.

  residual_t = r_t − beta_{t-1}' f_t
  resid_z    = residual_t / std(prior 60 residuals)

Emitted per instrument: residual, resid_z, R² (latest window, HC0-robust
fit), and the top contributing factors — so the digest can SAY "80%
explained by DXY + oil → residual small → priced" instead of asserting it.

Run: python factors.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"
STATE_JSON = DATA_DIR / "factor_state.json"
CONF = yaml.safe_load((Path(__file__).parent / "factors.yaml").read_text())

WINDOW = int(CONF.get("window", 60))
MIN_OBS = int(CONF.get("min_obs", 45))


def _class_key(spec: dict) -> str:
    mkt = spec["market"]
    sym = spec.get("symbol") or ""
    if mkt == "EQUITIES":
        return "EQUITIES_IN" if sym.endswith((".NS", ".BO")) else "EQUITIES_GLB"
    if mkt == "INDICES":
        return "INDICES_IN" if spec["id"].startswith("nifty") else "INDICES_GLB"
    return mkt


def factor_set(spec: dict) -> list[str] | None:
    """Configured factors for an instrument; None means excluded."""
    if spec["market"] in CONF.get("exclude_classes", []):
        return None
    ov = CONF.get("overrides", {}).get(spec["id"])
    if ov == "exclude":
        return None
    factors = ov if ov else CONF.get("class_defaults", {}).get(_class_key(spec), [])
    return [f for f in factors if f != spec["id"]] or None


def rolling_residuals(y: pd.Series, X: pd.DataFrame,
                      window: int = WINDOW) -> pd.DataFrame:
    """PIT rolling OLS: betas from the window ending t-1, applied to f_t.
    Returns DataFrame [pred, resid] indexed like y."""
    from statsmodels.regression.rolling import RollingOLS
    import statsmodels.api as sm
    df = pd.concat([y.rename("_y"), X], axis=1).dropna()
    if len(df) < window + 5:
        return pd.DataFrame(columns=["pred", "resid"])
    Xc = sm.add_constant(df[X.columns])
    ro = RollingOLS(df["_y"], Xc, window=window, min_nobs=MIN_OBS,
                    missing="drop").fit(params_only=True)
    betas = ro.params.shift(1)          # <- the PIT shift
    pred = (betas * Xc).sum(axis=1, min_count=len(Xc.columns))
    resid = df["_y"] - pred
    return pd.DataFrame({"pred": pred, "resid": resid})


def _latest_fit_stats(y: pd.Series, X: pd.DataFrame) -> tuple[float, dict]:
    """R² + per-factor contribution (beta_i * f_i,t) on the latest window,
    HC0-robust single fit for the reported numbers."""
    import statsmodels.api as sm
    df = pd.concat([y.rename("_y"), X], axis=1).dropna().tail(WINDOW)
    if len(df) < MIN_OBS:
        return float("nan"), {}
    Xc = sm.add_constant(df[X.columns])
    res = sm.OLS(df["_y"], Xc).fit(cov_type="HC0")
    last_f = df[X.columns].iloc[-1]
    contrib = {c: float(res.params.get(c, 0.0) * last_f[c]) for c in X.columns}
    return float(res.rsquared), contrib


def resid_z_series(y: pd.Series, X: pd.DataFrame,
                   window: int = WINDOW) -> pd.Series:
    """Full-history PIT residual z: residual_t / std(prior `window` residuals).
    Backtest substrate for scorecard.py."""
    rr = rolling_residuals(y, X, window)
    if rr.empty:
        return pd.Series(dtype=float)
    resid = rr["resid"]
    sd = resid.shift(1).rolling(window, min_periods=MIN_OBS).std(ddof=0)
    return (resid / sd).dropna()


def build_factor_state(prices: pd.DataFrame | None = None) -> dict:
    from registry import load_registry
    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    rets = prices.pct_change(fill_method=None)

    out: dict[str, dict] = {}
    for spec in load_registry():
        sid = spec["id"]
        if sid not in rets.columns:
            continue
        fs = factor_set(spec)
        if not fs:
            continue
        fs = [f for f in fs if f in rets.columns]
        if len(fs) < 2:
            continue
        y = rets[sid]
        X = rets[fs]
        rr = rolling_residuals(y, X)
        if rr.empty or rr["resid"].dropna().empty:
            continue
        resid = rr["resid"].dropna()
        # resid_z: latest residual vs the std of the PRIOR window of residuals
        prior = resid.iloc[:-1].tail(WINDOW)
        if len(prior) < MIN_OBS or prior.std(ddof=0) == 0:
            continue
        rz = float(resid.iloc[-1] / prior.std(ddof=0))
        r2, contrib = _latest_fit_stats(y, X)
        actual = float(y.reindex(resid.index).iloc[-1])
        pred = float(rr["pred"].reindex(resid.index).iloc[-1])
        top = sorted(contrib.items(), key=lambda kv: -abs(kv[1]))[:3]
        explained_share = None
        if actual not in (0.0,) and np.isfinite(actual) and abs(actual) > 1e-9:
            explained_share = max(0.0, min(1.5, pred / actual)) if \
                np.sign(pred) == np.sign(actual) else 0.0
        out[sid] = {
            "asof": resid.index[-1].strftime("%Y-%m-%d"),
            "factors": fs,
            "actual_ret_pct": round(actual * 100.0, 3),
            "pred_ret_pct": round(pred * 100.0, 3),
            "resid_pct": round(float(resid.iloc[-1]) * 100.0, 3),
            "resid_z": round(rz, 2),
            "r2_60d": None if not np.isfinite(r2) else round(r2, 3),
            "explained_share": None if explained_share is None
                               else round(explained_share, 2),
            "top_contributors": [{"factor": f, "contrib_pct": round(v * 100, 3)}
                                 for f, v in top],
        }

    state = {"updated": datetime.now(timezone.utc).isoformat(),
             "window": WINDOW, "series": out}
    STATE_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_factor_state() -> dict:
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"series": {}}


if __name__ == "__main__":
    st = build_factor_state()
    rows = st["series"]
    print(f"factor state: {len(rows)} instruments")
    ranked = sorted(rows.items(), key=lambda kv: -abs(kv[1]["resid_z"]))
    for sid, r in ranked[:8]:
        tc = ", ".join(f"{t['factor']}{t['contrib_pct']:+.2f}%"
                       for t in r["top_contributors"][:2])
        print(f"  {sid:22} resid_z={r['resid_z']:+5.2f} "
              f"actual={r['actual_ret_pct']:+.2f}% pred={r['pred_ret_pct']:+.2f}% "
              f"R2={r['r2_60d']} [{tc}]")
