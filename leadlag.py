"""P5 — lead-lag / transmission verification (implemented).

Theory proposes a channel; this module decides whether it is LIVE before the
board may emit a "setup". A setup requires ALL of:

  1. historically significant lead — lagged OLS target_t ~ driver_{t-k} with
     HAC (Newey-West) errors at the best CCF lag k in 1..MAX_LAG, p < 0.05,
     |corr| >= MIN_CORR, n >= MIN_OBS — then Benjamini-Hochberg across the
     whole scanned pair set (a scan of ~hundreds of pairs manufactures
     significance; fdr.py controls it);
  2. the driver has actually moved (vol-conditional |zc| >= DRIVER_ZC);
  3. the target has NOT already repriced (its response so far is below
     beta-implied, and its own |zc| hasn't matched the move).

Granger causality is reported as EVIDENCE with an explicit caveat — it is
regime-dependent and spuriously triggered; it never gates the emit.

Candidates come from the relations substrate (pairs with a measured lead).
State: data/leadlag_state.json. Run: python leadlag.py
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
STATE_JSON = DATA_DIR / "leadlag_state.json"

MAX_LAG = 5
MIN_CORR = 0.25
MIN_OBS = 150
DRIVER_ZC = 1.5
REPRICE_SHARE = 0.6     # target counted as repriced past this beta-implied share
FDR_Q = 0.10
GRANGER_CAVEAT = ("Granger is regime-dependent and spurious-prone; reported "
                  "as evidence only, never the emit gate")


def _best_lag(dr: pd.Series, tg: pd.Series, max_lag: int = MAX_LAG):
    """(k, corr_k) with the largest |corr(driver_{t-k}, target_t)|, k>=1."""
    best_k, best_c = None, 0.0
    for k in range(1, max_lag + 1):
        df = pd.concat([dr.shift(k), tg], axis=1, keys=["d", "t"]).dropna()
        if len(df) < MIN_OBS:
            continue
        c = df["d"].corr(df["t"])
        if pd.notna(c) and abs(c) > abs(best_c):
            best_k, best_c = k, float(c)
    return best_k, best_c


def verify_transmission(driver: str, target: str,
                        prices: pd.DataFrame,
                        zc_latest: dict | None = None) -> dict | None:
    """Full P5 verification for one directed pair. None = not computable."""
    import statsmodels.api as sm
    if driver not in prices.columns or target not in prices.columns:
        return None
    rets = prices[[driver, target]].pct_change(fill_method=None)
    dr, tg = rets[driver], rets[target]

    k, ccf = _best_lag(dr, tg)
    if k is None:
        return None

    df = pd.concat([dr.shift(k).rename("d"), tg.rename("t")], axis=1).dropna()
    X = sm.add_constant(df["d"])
    res = sm.OLS(df["t"], X).fit(cov_type="HAC", cov_kwds={"maxlags": k})
    beta = float(res.params["d"])
    p_hac = float(res.pvalues["d"])

    granger_p = None
    try:
        import contextlib
        import io
        import warnings
        from statsmodels.tsa.stattools import grangercausalitytests
        with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
            warnings.simplefilter("ignore")
            g = grangercausalitytests(df[["t", "d"]].dropna(), maxlag=k)
        granger_p = round(float(g[k][0]["ssr_ftest"][1]), 4)
    except Exception:
        pass

    significant = p_hac < 0.05 and abs(ccf) >= MIN_CORR and len(df) >= MIN_OBS

    # live-state gates
    zc_latest = zc_latest or {}
    d_zc = (zc_latest.get(driver) or {}).get("zc")
    t_zc = (zc_latest.get(target) or {}).get("zc")
    d_ret = float(dr.dropna().iloc[-1]) if dr.notna().any() else None
    driver_moved = d_zc is not None and abs(d_zc) >= DRIVER_ZC

    target_repriced = None
    expected_move_pct = None
    if driver_moved and d_ret is not None:
        expected = beta * d_ret
        expected_move_pct = round(expected * 100, 3)
        # response so far: target cumulative return over the k sessions
        # available since the driver's move (may be partial — that's the point)
        t_resp = float(tg.dropna().tail(k).sum()) if tg.notna().any() else 0.0
        repriced_share = (t_resp / expected) if expected not in (0.0,) and \
            np.isfinite(expected) and abs(expected) > 1e-9 else 0.0
        target_repriced = bool(repriced_share >= REPRICE_SHARE or
                               (t_zc is not None and abs(t_zc) >= DRIVER_ZC and
                                np.sign(t_zc) == np.sign(expected)))

    return {
        "driver": driver, "target": target,
        "lead_days": k, "ccf": round(ccf, 3),
        "beta": round(beta, 4), "p_hac": round(p_hac, 5),
        "granger_p": granger_p, "granger_caveat": GRANGER_CAVEAT,
        "n_obs": int(len(df)),
        "historically_significant": bool(significant),
        "driver_zc": d_zc, "driver_moved": bool(driver_moved),
        "target_zc": t_zc, "target_repriced": target_repriced,
        "expected_target_move_pct": expected_move_pct,
        "emit": bool(significant and driver_moved and target_repriced is False),
    }


def build_setups(prices: pd.DataFrame | None = None) -> dict:
    """Scan relations lead-pairs, verify each, FDR-control the scan, persist."""
    from conditional import load_conditional
    from fdr import benjamini_hochberg
    from relations import load_relations

    if prices is None:
        prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    zc = load_conditional().get("series", {})
    rel = load_relations()

    seen, results = set(), []
    for p in rel.get("pairs", []):
        lr = p.get("lead_rho")
        if lr is None or abs(lr) < MIN_CORR:
            continue
        pair = (p["leader"], p["follower"])
        if pair in seen:
            continue
        seen.add(pair)
        v = verify_transmission(p["leader"], p["follower"], prices, zc)
        if v is not None:
            results.append(v)

    # multiplicity control across the whole scan
    if results:
        bh = benjamini_hochberg([r["p_hac"] for r in results], q=FDR_Q)
        for r, rej in zip(results, bh["reject"]):
            r["bh_significant"] = bool(rej)
            r["emit"] = bool(r["emit"] and rej)
        eff_thr = bh["threshold"]
    else:
        eff_thr = None

    setups = [r for r in results if r["emit"]]
    setups.sort(key=lambda r: (-abs(r["ccf"]), r["p_hac"]))
    state = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "scanned_pairs": len(results),
        "fdr_q": FDR_Q, "fdr_threshold": eff_thr,
        "n_bh_significant": sum(1 for r in results if r.get("bh_significant")),
        "setups": setups,
        "verified_pairs": [
            {k: r[k] for k in ("driver", "target", "lead_days", "ccf",
                               "beta", "p_hac", "bh_significant")}
            for r in results if r.get("bh_significant")],
    }
    STATE_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_setups() -> dict:
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"setups": [], "verified_pairs": []}


if __name__ == "__main__":
    st = build_setups()
    print(f"leadlag: scanned {st['scanned_pairs']} pairs, "
          f"{st['n_bh_significant']} BH-significant (q={st['fdr_q']}, "
          f"thr={st['fdr_threshold']}), {len(st['setups'])} live setups")
    for s in st["setups"][:6]:
        print(f"  SETUP {s['driver']} -> {s['target']} lead {s['lead_days']}d "
              f"ccf {s['ccf']} beta {s['beta']} p {s['p_hac']} | driver zc "
              f"{s['driver_zc']} -> expected {s['expected_target_move_pct']}%")
    for s in st["verified_pairs"][:8]:
        print(f"  pair  {s['driver']} -> {s['target']} lead {s['lead_days']}d "
              f"ccf {s['ccf']} p {s['p_hac']}")
