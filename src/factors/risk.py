"""Low-risk factors (§8)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register
from src.prices.daily import realised_volatility


class RealisedVolatility(Factor):
    """Trailing 12-month realised volatility, annualised. Lower is better.

    The low-volatility anomaly: Haugen & Heins (1975); Blitz & van Vliet
    (2007), "The Volatility Effect".
    """

    name = "realised_vol"
    category = "risk"
    higher_is_better = False

    def compute(self, ctx: FactorContext) -> pd.Series:
        return realised_volatility(ctx.returns, ctx.as_of_date, lookback=252)


class MarketBeta(Factor):
    """OLS beta against the benchmark over the trailing 2 years. Lower is better.

    Frazzini & Pedersen (2014), "Betting Against Beta". Estimated on the window
    ending at the as-of date; the benchmark series is loaded with the same
    bound, so no future observation can enter the estimate.
    """

    name = "market_beta"
    category = "risk"
    higher_is_better = False

    def compute(self, ctx: FactorContext) -> pd.Series:
        return _betas(ctx)[0]


class IdiosyncraticVolatility(Factor):
    """Volatility of returns residual to the benchmark. Lower is better.

    Ang, Hodrick, Xing & Zhang (2006), "The Cross-Section of Volatility and
    Expected Returns".
    """

    name = "idio_vol"
    category = "risk"
    higher_is_better = False

    def compute(self, ctx: FactorContext) -> pd.Series:
        return _betas(ctx)[1]


def _betas(ctx: FactorContext) -> tuple[pd.Series, pd.Series]:
    """Beta and residual volatility against the benchmark, in one pass.

    Falls back to an equal-weighted market proxy built from the universe when
    no benchmark series is loaded — a study on a store without benchmark data
    should still produce a beta, and the fallback is stated rather than silent.
    """
    returns = ctx.returns
    if returns.empty:
        empty = pd.Series(dtype="float64", index=pd.Index(ctx.universe))
        return empty, empty

    window = returns.tail(504)
    bench = ctx.benchmark
    market = (bench.reindex(window.index) if not bench.empty
              else window.mean(axis=1))

    betas, ivols = {}, {}
    for isin in window.columns:
        y = window[isin]
        valid = y.notna() & market.notna()
        if valid.sum() < 120:
            betas[isin] = np.nan
            ivols[isin] = np.nan
            continue
        x = market[valid].to_numpy()
        yv = y[valid].to_numpy()
        var = x.var()
        if var <= 0:
            betas[isin] = np.nan
            ivols[isin] = np.nan
            continue
        beta = float(np.cov(yv, x)[0, 1] / var)
        alpha = float(yv.mean() - beta * x.mean())
        betas[isin] = beta
        ivols[isin] = float((yv - alpha - beta * x).std() * np.sqrt(252.0))
    return pd.Series(betas), pd.Series(ivols)


register(RealisedVolatility())
register(MarketBeta())
register(IdiosyncraticVolatility())
