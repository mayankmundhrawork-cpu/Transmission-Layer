"""Amihud-family price-impact estimation (§9).

λ is displacement per unit of traded value:

    ILLIQ_i = mean_d( |r_id| / V_id )       [return per rupee traded]

For a trade of value V, expected displacement is λ·V (a return). Executing
across that displacement rather than at the touch costs, on average, half of
it — so the cost fraction of the traded notional is

    impact_fraction = participation_coefficient · λ · V

with `participation_coefficient` defaulting to 0.5 (linear walk from touch to
final price). It is a parameter, not a constant, because the right value
depends on execution style and should come from a pre-registration rather than
from whatever made the backtest look best.

**Shared with the intraday work.** `amihud_lambda` and `impact_bps` take plain
arrays and touch neither the database nor the config, so the intraday λ operand
and this backtest cost model compute the same number from the same code:

    from src.costs.impact import amihud_lambda
    lam = amihud_lambda(returns, turnover)

Spread estimation lives here too. Where quote data exists it should be used
directly; where it does not — which is everywhere in this archive, since
bhavcopy carries no quotes — the Corwin-Schultz high-low estimator is the
defensible fallback, and its failure modes are documented on the function.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

#: Below this, a "return per rupee" estimate is noise: a name that traded ₹5,000
#: in a day produces a λ that would forecast a 40% move on a ₹1 lakh order.
MIN_TURNOVER_INR = 10_000.0

DEFAULT_PARTICIPATION_COEFFICIENT = 0.5


def amihud_lambda(
    returns: pd.Series | np.ndarray,
    turnover: pd.Series | np.ndarray,
    *,
    min_observations: int = 20,
    min_turnover: float = MIN_TURNOVER_INR,
    winsorise: float = 0.01,
) -> float:
    """Amihud illiquidity: mean |return| per rupee of turnover.

    Returns NaN rather than a number when there is not enough to estimate from.
    A λ computed on six observations is not a conservative estimate — it is an
    arbitrary one, and it will be arbitrary in whichever direction makes the
    backtest look better roughly half the time.

    Days with near-zero turnover are dropped, not floored: |r|/V explodes as
    V→0 and a single stale-price day would dominate the mean.
    """
    r = np.asarray(pd.Series(returns).astype(float))
    v = np.asarray(pd.Series(turnover).astype(float))
    if r.shape != v.shape:
        raise ValueError(f"returns and turnover must align: {r.shape} vs {v.shape}")

    usable = np.isfinite(r) & np.isfinite(v) & (v >= min_turnover)
    if usable.sum() < min_observations:
        return float("nan")

    ratio = np.abs(r[usable]) / v[usable]
    if winsorise and len(ratio) >= 20:
        lo, hi = np.quantile(ratio, [winsorise, 1.0 - winsorise])
        ratio = np.clip(ratio, lo, hi)
    return float(np.mean(ratio))


def impact_bps(
    trade_value_inr: float,
    lambda_: float,
    *,
    participation_coefficient: float = DEFAULT_PARTICIPATION_COEFFICIENT,
    cap_bps: float = 1000.0,
) -> float:
    """Expected impact cost in basis points of the traded notional.

    `cap_bps` bounds the estimate. An uncapped λ·V on a very illiquid name can
    imply an impact above 100% of notional, which is not a cost — it is the
    model telling you the trade is impossible. The participation constraint in
    §9 is what should reject such a trade; the cap keeps a backtest that slips
    one through from producing a nonsense number instead of an obvious one.
    """
    if not np.isfinite(lambda_) or lambda_ <= 0 or trade_value_inr <= 0:
        return float("nan")
    fraction = participation_coefficient * lambda_ * trade_value_inr
    return float(min(fraction * 1e4, cap_bps))


def rolling_lambda(
    returns: pd.Series, turnover: pd.Series, window: int = 60, **kwargs
) -> pd.Series:
    """Trailing λ per date — point-in-time by construction (no centring)."""
    frame = pd.DataFrame({"r": returns, "v": turnover}).dropna(how="all")
    out = {}
    values = frame.to_numpy()
    for i in range(len(frame)):
        start = max(0, i - window + 1)
        chunk = values[start: i + 1]
        out[frame.index[i]] = amihud_lambda(chunk[:, 0], chunk[:, 1], **kwargs)
    return pd.Series(out, name="amihud_lambda")


def panel_lambda(
    returns: pd.DataFrame, turnover: pd.DataFrame, *, window: int = 60, **kwargs
) -> pd.Series:
    """λ per ISIN over the trailing `window` sessions of the supplied panels."""
    common = returns.columns.intersection(turnover.columns)
    out = {}
    for isin in common:
        r = returns[isin].tail(window)
        v = turnover[isin].reindex(r.index)
        out[isin] = amihud_lambda(r, v, **kwargs)
    return pd.Series(out, name="amihud_lambda")


# ---------------------------------------------------------------------------
# Spread
# ---------------------------------------------------------------------------

def corwin_schultz_spread(
    high: pd.Series, low: pd.Series, *, clamp: bool = True
) -> float:
    """Corwin & Schultz (2012) high-low spread estimator, as a fraction.

    Uses the ratio of two-day to one-day high-low ranges to separate volatility
    from spread. Well-known failure modes, all of which show up in Indian
    smallcaps:

    * Overnight gaps inflate the two-day range and bias the estimate upward.
    * Circuit-locked days have zero range and produce a zero or negative
      estimate.
    * Negative estimates are common in low-volatility names.

    Negative values are clamped to zero and the caller is expected to floor the
    result with a sane minimum — a zero spread is never a defensible input to a
    backtest (§18.6).
    """
    h = np.asarray(pd.Series(high).astype(float))
    l = np.asarray(pd.Series(low).astype(float))
    if len(h) < 2:
        return float("nan")

    usable = np.isfinite(h) & np.isfinite(l) & (l > 0) & (h >= l)
    h, l = h[usable], l[usable]
    if len(h) < 2:
        return float("nan")

    # One-day log ranges, squared, summed pairwise.
    beta_terms = np.log(h / l) ** 2
    beta = beta_terms[:-1] + beta_terms[1:]

    # Two-day range.
    h2 = np.maximum(h[:-1], h[1:])
    l2 = np.minimum(l[:-1], l[1:])
    gamma = np.log(h2 / l2) ** 2

    k = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))

    spread = spread[np.isfinite(spread)]
    if len(spread) == 0:
        return float("nan")
    estimate = float(np.mean(spread))
    return max(estimate, 0.0) if clamp else estimate


def spread_bps(
    high: pd.Series, low: pd.Series, *, floor_bps: float = 10.0,
    ceiling_bps: float = 500.0,
) -> float:
    """Estimated full spread in bps, floored and capped.

    The floor is not conservatism for its own sake: §18.6 requires that no
    backtest path can produce a zero-cost trade, and an unfloored estimator
    returns zero on exactly the illiquid names where the true spread is widest.
    """
    estimate = corwin_schultz_spread(high, low)
    if not np.isfinite(estimate):
        return floor_bps
    return float(np.clip(estimate * 1e4, floor_bps, ceiling_bps))


def days_to_liquidate(
    position_inr: float, median_daily_turnover_inr: float,
    participation_pct: float = 5.0,
) -> float:
    """Sessions to exit at the participation cap. `inf` if it cannot be exited."""
    capacity = median_daily_turnover_inr * participation_pct / 100.0
    if capacity <= 0:
        return float("inf")
    return position_inr / capacity


def violates_participation(
    trade_inr: float, median_daily_turnover_inr: float,
    max_participation_pct: float = 5.0,
) -> bool:
    """§9: reject any simulated position exceeding the participation cap."""
    if median_daily_turnover_inr <= 0:
        return True
    return trade_inr > median_daily_turnover_inr * max_participation_pct / 100.0
