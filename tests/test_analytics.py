"""Known-answer fixtures for the measured-transmission engine (P2/P3/P4/P6/P7).

Run: pytest -q tests/
"""
import numpy as np
import pandas as pd
import pytest

rng = np.random.default_rng(7)


# ── P2: conditional z ───────────────────────────────────────────────────
def test_ewma_zc_sees_quiet_regime_moves():
    """A +2% move after a quiet stretch must score FAR higher on zc than the
    same move inside a wild stretch — the exact failure of naive z."""
    from conditional import ewma_sigma
    quiet = rng.normal(0, 0.002, 300)   # 0.2% daily vol
    wild = rng.normal(0, 0.02, 300)     # 2% daily vol
    move = 0.02
    r_quiet = pd.Series(np.append(quiet, move))
    r_wild = pd.Series(np.append(wild, move))
    zq = (r_quiet / ewma_sigma(r_quiet.to_frame(0))[0]).iloc[-1]
    zw = (r_wild / ewma_sigma(r_wild.to_frame(0))[0]).iloc[-1]
    assert zq > 5.0            # screaming in a quiet regime
    assert zw < 2.0            # unremarkable in a wild one
    assert zq > 4 * zw


def test_ewma_sigma_is_point_in_time():
    """sigma at t must not depend on the return at t."""
    from conditional import ewma_sigma
    r = pd.Series(rng.normal(0, 0.01, 100))
    base = ewma_sigma(r.to_frame(0))[0].iloc[-1]
    r_shocked = r.copy()
    r_shocked.iloc[-1] = 0.50           # absurd same-day shock
    shocked = ewma_sigma(r_shocked.to_frame(0))[0].iloc[-1]
    assert base == pytest.approx(shocked)


# ── P3: rolling residuals ───────────────────────────────────────────────
def test_rolling_residual_recovers_planted_beta():
    """y = 0.8*f + tiny noise -> residuals ~ noise, idiosyncratic shock at
    the end must appear in the residual, not the prediction."""
    from factors import rolling_residuals
    n = 400
    f = pd.Series(rng.normal(0, 0.01, n), name="f")
    noise = rng.normal(0, 0.0005, n)
    y = 0.8 * f + noise
    y.iloc[-1] += 0.03                  # planted idiosyncratic shock
    rr = rolling_residuals(pd.Series(y), f.to_frame())
    resid = rr["resid"].dropna()
    assert abs(resid.iloc[-1] - 0.03) < 0.005      # shock lands in residual
    assert resid.iloc[:-1].abs().mean() < 0.002    # otherwise ~noise-sized


# ── P4: assumption scorer ───────────────────────────────────────────────
def _write_prices(tmp_path, gold_beta):
    n = 300
    idx = pd.bdate_range("2025-01-01", periods=n)
    vix = rng.normal(0, 0.02, n)
    nifty = -0.5 * vix + rng.normal(0, 0.005, n)
    gold = gold_beta * vix + rng.normal(0, 0.004, n)
    lvl = lambda r: 100 * np.exp(np.cumsum(r))
    return pd.DataFrame({"vix": lvl(vix), "nifty_50": lvl(nifty),
                         "comex_gold": lvl(gold), "sp500": lvl(nifty)},
                        index=idx)


def test_assumption_scorer_flags_inversion():
    from assumptions import score_assumptions
    # gold moving WITH equities / against vol -> safe haven must INVERT
    prices = _write_prices(None, gold_beta=-0.6)
    st = score_assumptions(prices)
    assert st["assumptions"]["safe_haven_gold"]["status"] == "INVERTED"
    # gold rising with vol -> safe haven VALID
    prices = _write_prices(None, gold_beta=+0.6)
    st = score_assumptions(prices)
    assert st["assumptions"]["safe_haven_gold"]["status"] == "VALID"
    # vix-equity inverse must be VALID in both fixtures (planted -0.5 beta)
    assert st["assumptions"]["vix_equity_inverse"]["status"] == "VALID"


# ── P6: OU half-life ────────────────────────────────────────────────────
def test_ou_half_life_recovers_planted_theta():
    from spreads import ou_half_life
    theta, n = 0.05, 2000               # true half-life = ln2/theta ~ 13.9d
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = x[t - 1] - theta * x[t - 1] + rng.normal(0, 0.1)
    hl, _ = ou_half_life(pd.Series(x))
    true_hl = np.log(2) / theta
    assert hl == pytest.approx(true_hl, rel=0.3)


def test_ou_half_life_none_for_random_walk():
    from spreads import ou_half_life
    rw = pd.Series(np.cumsum(rng.normal(0, 1, 1500)))
    hl, _ = ou_half_life(rw)
    assert hl is None or hl > 200       # no (fast) mean reversion detected


# ── P5: lead-lag verification ───────────────────────────────────────────
def test_leadlag_recovers_planted_lead():
    """target follows driver by exactly 2 sessions -> k=2, significant."""
    from leadlag import _best_lag, verify_transmission
    n = 500
    dr = pd.Series(rng.normal(0, 0.01, n))
    tg = 0.7 * dr.shift(2) + pd.Series(rng.normal(0, 0.004, n))
    k, ccf = _best_lag(dr, tg)
    assert k == 2 and ccf > 0.5
    lvl = lambda r: pd.Series(100 * np.exp(np.cumsum(r.fillna(0))))
    prices = pd.DataFrame({"drv": lvl(dr), "tgt": lvl(tg)})
    v = verify_transmission("drv", "tgt", prices, zc_latest={})
    assert v["historically_significant"] and v["lead_days"] == 2
    assert v["emit"] is False            # driver hasn't moved -> no setup


def test_leadlag_rejects_independent_series():
    from leadlag import verify_transmission
    n = 500
    lvl = lambda r: pd.Series(100 * np.exp(np.cumsum(r)))
    prices = pd.DataFrame({"a": lvl(rng.normal(0, 0.01, n)),
                           "b": lvl(rng.normal(0, 0.01, n))})
    v = verify_transmission("a", "b", prices, zc_latest={})
    assert v is None or not v["historically_significant"]


# ── P6: Hurst ───────────────────────────────────────────────────────────
def test_hurst_orders_processes_correctly():
    from spreads import hurst_exponent
    n = 1500
    ou = np.zeros(n)
    for t in range(1, n):
        ou[t] = ou[t - 1] * 0.85 + rng.normal(0, 1)      # strongly mean-rev
    trend = np.cumsum(rng.normal(0.05, 0.5, n))          # drifting walk
    h_ou = hurst_exponent(pd.Series(ou))
    h_tr = hurst_exponent(pd.Series(trend))
    assert h_ou < 0.5 < h_tr
    assert h_ou < h_tr


# ── P7: Benjamini-Hochberg ──────────────────────────────────────────────
def test_bh_textbook_example():
    from fdr import benjamini_hochberg
    # classic: with q=0.25 over these 6 p-values, the first 4 are rejected
    p = [0.01, 0.04, 0.10, 0.12, 0.30, 0.50]
    out = benjamini_hochberg(p, q=0.25)
    assert out["n_rejected"] == 4
    assert out["reject"][:4] == [True] * 4 and not any(out["reject"][4:])


def test_bh_no_rejections_on_uniform():
    from fdr import benjamini_hochberg
    out = benjamini_hochberg([0.6, 0.7, 0.9], q=0.10)
    assert out["n_rejected"] == 0 and out["threshold"] is None
