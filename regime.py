"""P4 — regime layer: transparent rules-based risk-on/off + Markov secondary.

Primary label is RULES-BASED (auditable, point-in-time, no fitting):
components are computed for every historical date, so the label is a
SERIES — which also powers regime-conditional percentiles.

  components (each in [0,1], risk-off-ness):
    vix_pct        VIX 1y percentile (and india_vix when available, max)
    breadth_off    share of tracked equity indices BELOW their 50DMA
    corr_off       cross-asset stress: 20d corr(sp500, ust_10y yield chg)
                   NEGATIVE in risk-off (yields fall as equities fall)

  score = mean(components); RISK_OFF >= 0.6, RISK_ON <= 0.35, else NEUTRAL.

Secondary: 2-state MarkovRegression (statsmodels) on sp500 returns with
switching variance — reported as P(high-vol state), evidence not gate.

Run: python regime.py
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
STATE_JSON = DATA_DIR / "regime_state.json"

EQ_INDICES = ["sp500", "nasdaq_100", "dow_jones", "russell_2000", "ftse_100",
              "dax", "cac_40", "stoxx_50", "nikkei_225", "hang_seng",
              "shanghai_comp", "kospi", "taiwan_weighted", "asx_200",
              "bovespa", "nifty_50", "nifty_midcap_100"]

OFF_TH, ON_TH = 0.60, 0.35


def component_frame(prices: pd.DataFrame) -> pd.DataFrame:
    """Historical daily components, all trailing-only (PIT)."""
    comp = pd.DataFrame(index=prices.index)

    # vol percentile: max of VIX and India VIX 1y-rank
    vp = []
    for vid in ("vix", "india_vix"):
        if vid in prices.columns:
            vp.append(prices[vid].rolling(252, min_periods=60)
                      .rank(pct=True))
    if vp:
        comp["vol_pct"] = pd.concat(vp, axis=1).max(axis=1)

    # breadth: share of equity indices below their 50DMA (risk-off-ness)
    idx = [c for c in EQ_INDICES if c in prices.columns]
    if idx:
        below = pd.DataFrame({
            c: (prices[c] < prices[c].rolling(50, min_periods=30).mean())
            .where(prices[c].notna()) for c in idx})
        comp["breadth_off"] = below.mean(axis=1)

    # cross-asset: corr(sp500 ret, ust10y yield change) — negative in risk-off
    if "sp500" in prices.columns and "ust_10y" in prices.columns:
        df = pd.DataFrame({"eq": prices["sp500"].pct_change(fill_method=None),
                           "dy": prices["ust_10y"].diff()}).dropna()
        c = df["eq"].rolling(20).corr(df["dy"])
        comp["corr_off"] = ((-c + 1) / 2).reindex(prices.index)  # -1->1, +1->0

    return comp


def regime_series(prices: pd.DataFrame) -> pd.DataFrame:
    comp = component_frame(prices)
    score = comp.mean(axis=1, skipna=True)
    label = pd.Series("NEUTRAL", index=score.index)
    label[score >= OFF_TH] = "RISK_OFF"
    label[score <= ON_TH] = "RISK_ON"
    label[score.isna()] = "UNKNOWN"
    out = comp.copy()
    out["score"], out["label"] = score, label
    return out


def regime_percentile(series: pd.Series, regimes: pd.Series,
                      current_label: str) -> float | None:
    """Percentile of today's value within SAME-REGIME history (min 40 obs)."""
    s = series.dropna()
    if s.empty:
        return None
    r = regimes.reindex(s.index)
    hist = s[r == current_label]
    if len(hist) < 40:
        return None
    return float((hist < s.iloc[-1]).mean() * 100.0)


def _markov_secondary(prices: pd.DataFrame) -> dict:
    """P(high-vol state) from a 2-state switching-variance model. Evidence
    only; failures degrade to None."""
    try:
        from statsmodels.tsa.regime_switching.markov_regression import \
            MarkovRegression
        r = prices["sp500"].pct_change(fill_method=None).dropna() * 100
        if len(r) < 300:
            return {"p_highvol": None, "note": "insufficient history"}
        m = MarkovRegression(r, k_regimes=2, trend="c",
                             switching_variance=True)
        res = m.fit(em_iter=20, search_reps=0, disp=False)
        probs = res.smoothed_marginal_probabilities
        # identify the high-vol state by its variance parameter
        variances = [res.params[f"sigma2[{i}]"] for i in range(2)] \
            if "sigma2[0]" in res.params.index else None
        if variances is None:
            v0 = r[probs[0] > 0.5].std()
            v1 = r[probs[1] > 0.5].std()
            hi = 0 if v0 > v1 else 1
        else:
            hi = int(np.argmax(variances))
        return {"p_highvol": round(float(probs[hi].iloc[-1]), 3),
                "note": "2-state switching-variance on sp500 returns"}
    except Exception as e:
        return {"p_highvol": None, "note": f"markov failed: {str(e)[:80]}"}


def build_regime(prices: pd.DataFrame | None = None) -> dict:
    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    rs = regime_series(prices)
    last = rs.dropna(subset=["score"]).iloc[-1]
    state = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "label": str(last["label"]),
        "score": round(float(last["score"]), 3),
        "components": {c: (None if pd.isna(last.get(c)) else round(float(last[c]), 3))
                       for c in ("vol_pct", "breadth_off", "corr_off")},
        "thresholds": {"risk_off": OFF_TH, "risk_on": ON_TH},
        "markov": _markov_secondary(prices),
        # streak counted over dates with a computable label only
        "days_in_regime": int(
            (rs.dropna(subset=["score"])["label"][::-1] == last["label"])
            .cummin().sum()),
    }
    STATE_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_regime() -> dict:
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"label": "UNKNOWN"}


if __name__ == "__main__":
    st = build_regime()
    print(f"regime: {st['label']} (score {st['score']}, "
          f"{st['days_in_regime']}d in regime)")
    print(f"  components: {st['components']}")
    print(f"  markov P(high-vol): {st['markov']}")