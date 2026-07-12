"""P4 — assumption ledger scorer + change-point dating.

Loads assumptions.yaml (standing priors as hypotheses) and scores each one
against live rolling correlations at generation time:

  VALID              20d AND 60d corr clear in the expected sign
  WEAK               neither window clear / windows disagree
  INVERTED           20d corr clear in the WRONG sign, or the contra check
                     fires (e.g. gold clearly trading WITH nifty)
  INSUFFICIENT_DATA  < MIN_PAIRED_OBS paired observations

Change-points: `ruptures` (PELT, rbf) on the rolling-60d correlation series
dates when a relationship regime last shifted — so "gold left safe-haven"
gets a date, not a silent assumption. ruptures is optional (guarded import,
py3.14 has no wheel locally); fallback = largest 20-session jump in the
rolling corr.

Consumers: engine (co-occurrence gating), thesis prompt (channel status),
digest/brief header, app panel. Run: python assumptions.py
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
STATE_JSON = DATA_DIR / "assumptions_state.json"

CLEAR = 0.25            # |corr| at/above this is a "clear" reading
MIN_PAIRED_OBS = 40
CP_WINDOW = 60          # rolling-corr window fed to change-point detection


def _load_ledger() -> list[dict]:
    conf = yaml.safe_load((Path(__file__).parent / "assumptions.yaml").read_text())
    return conf["assumptions"]


def _corr(rets: pd.DataFrame, a: str, b: str, window: int) -> tuple[float | None, int]:
    if a not in rets.columns or b not in rets.columns:
        return None, 0
    df = rets[[a, b]].dropna().tail(window)
    n = len(df)
    if n < min(MIN_PAIRED_OBS, window) * 0.75:
        return None, n
    c = df[a].corr(df[b])
    return (None if pd.isna(c) else float(c)), n


def _rolling_corr_series(rets: pd.DataFrame, a: str, b: str) -> pd.Series:
    if a not in rets.columns or b not in rets.columns:
        return pd.Series(dtype=float)
    df = rets[[a, b]].dropna()
    return df[a].rolling(CP_WINDOW).corr(df[b]).dropna()


def _changepoint_date(corr_series: pd.Series) -> str | None:
    """Date the most recent regime shift in a rolling correlation."""
    s = corr_series.dropna()
    if len(s) < 120:
        return None
    try:
        import ruptures as rpt
        algo = rpt.Pelt(model="rbf", min_size=30).fit(s.to_numpy().reshape(-1, 1))
        bkps = algo.predict(pen=5)
        idxs = [i for i in bkps if i < len(s)]
        return s.index[idxs[-1]].strftime("%Y-%m-%d") if idxs else None
    except ImportError:
        # fallback: largest absolute 20-session jump in the rolling corr
        jump = (s - s.shift(20)).abs()
        if jump.dropna().empty:
            return None
        return jump.idxmax().strftime("%Y-%m-%d")
    except Exception:
        return None


def _status(c20, c60, sign, contra_c20) -> str:
    if c20 is None and c60 is None:
        return "INSUFFICIENT_DATA"
    # contra fires => inverted regardless of the primary channel reading
    if contra_c20 is not None and abs(contra_c20) >= CLEAR:
        return "INVERTED"
    if c20 is not None and abs(c20) >= CLEAR and np.sign(c20) != sign:
        return "INVERTED"
    ok20 = c20 is not None and abs(c20) >= CLEAR and np.sign(c20) == sign
    ok60 = c60 is not None and abs(c60) >= CLEAR and np.sign(c60) == sign
    if ok20 and ok60:
        return "VALID"
    if ok20 or ok60:
        return "WEAK"     # one window clear, the other not — degraded
    return "WEAK"


def score_assumptions(prices: pd.DataFrame | None = None) -> dict:
    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    rets = prices.pct_change(fill_method=None)

    out: dict[str, dict] = {}
    for a in _load_ledger():
        drv, tgt, sign = a["driver"], a["target"], int(a["expected_sign"])
        c20, n20 = _corr(rets, drv, tgt, 20)
        c60, n60 = _corr(rets, drv, tgt, 60)
        contra_c20 = None
        contra = a.get("contra")
        if contra:
            cc, _ = _corr(rets, tgt, contra["series"], 20)
            bad = int(contra["bad_sign"])
            # only counts against the prior when clearly in the BAD sign
            contra_c20 = cc if (cc is not None and np.sign(cc) == bad) else None
        status = "INSUFFICIENT_DATA" if max(n20, n60) < MIN_PAIRED_OBS * 0.5 \
            else _status(c20, c60, sign, contra_c20)
        cp = _changepoint_date(_rolling_corr_series(rets, drv, tgt))
        out[a["name"]] = {
            "driver": drv, "target": tgt, "expected_sign": sign,
            "status": status,
            "corr20": None if c20 is None else round(c20, 2),
            "corr60": None if c60 is None else round(c60, 2),
            "contra_series": (contra or {}).get("series"),
            "contra_corr20": None if contra_c20 is None else round(contra_c20, 2),
            "last_changepoint": cp,
            "channel": a["channel"],
            "linked_group": a.get("linked_group"),
        }

    state = {"updated": datetime.now(timezone.utc).isoformat(),
             "clear_threshold": CLEAR, "assumptions": out}
    STATE_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_assumptions_state() -> dict:
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"assumptions": {}}


def group_status(linked_group: str, state: dict | None = None) -> str | None:
    """Ledger status for an engine co-occurrence group (None = ungoverned)."""
    state = state or load_assumptions_state()
    for rec in state.get("assumptions", {}).values():
        if rec.get("linked_group") == linked_group:
            return rec["status"]
    return None


if __name__ == "__main__":
    st = score_assumptions()
    for name, r in st["assumptions"].items():
        extra = f" contra({r['contra_series']})={r['contra_corr20']}" \
            if r["contra_corr20"] is not None else ""
        cp = f" cp={r['last_changepoint']}" if r["last_changepoint"] else ""
        print(f"  {r['status']:17} {name:24} corr20={r['corr20']} "
              f"corr60={r['corr60']}{extra}{cp}")
