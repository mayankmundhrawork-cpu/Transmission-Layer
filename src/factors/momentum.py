"""Momentum factors (§8)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register
from src.prices.daily import trailing_return


class Momentum12_1(Factor):
    """12-month return skipping the most recent month.

    Jegadeesh & Titman (1993), with the one-month skip from Fama & French
    (1996). The skip is not cosmetic: one-month reversal is a distinct and
    opposite-signed effect, and including the most recent month blends two
    phenomena into one score and weakens both.
    """

    name = "momentum_12_1"
    category = "momentum"

    def compute(self, ctx: FactorContext) -> pd.Series:
        return trailing_return(ctx.returns, ctx.as_of_date, lookback=231, skip=21)


class Momentum6_1(Factor):
    """6-month return skipping the most recent month."""

    name = "momentum_6_1"
    category = "momentum"

    def compute(self, ctx: FactorContext) -> pd.Series:
        return trailing_return(ctx.returns, ctx.as_of_date, lookback=105, skip=21)


class ShortTermReversal(Factor):
    """Most recent month's return. Lower is better (reversal).

    Jegadeesh (1990). Carried as a separate factor rather than folded into
    momentum precisely because its sign is opposite.
    """

    name = "short_term_reversal"
    category = "momentum"
    higher_is_better = False

    def compute(self, ctx: FactorContext) -> pd.Series:
        return trailing_return(ctx.returns, ctx.as_of_date, lookback=21, skip=0)


class ResidualMomentum(Factor):
    """12-1 momentum of returns residual to market and size.

    Blitz, Huij & Martens (2011), "Residual Momentum". Stripping the market and
    size exposures out before measuring momentum leaves a signal that is far
    less volatile than raw momentum and does not load on the crash risk that
    makes raw momentum periodically catastrophic.

    Regression is run on the trailing window ending at the as-of date, and the
    residual series is then compounded over 12-1 — so nothing here sees past
    the as-of date.
    """

    name = "residual_momentum"
    category = "momentum"

    def compute(self, ctx: FactorContext) -> pd.Series:
        returns = ctx.returns
        if returns.empty or len(returns) < 60:
            return pd.Series(np.nan, index=pd.Index(ctx.universe))

        window = returns.tail(252)
        # Equal-weighted market proxy and a size proxy built from the same
        # panel, so the regression needs no external factor series.
        market = window.mean(axis=1)
        size = ctx.free_float_market_cap.reindex(window.columns)
        log_size = np.log(size.where(size > 0))

        residuals = {}
        for isin in window.columns:
            y = window[isin]
            valid = y.notna() & market.notna()
            if valid.sum() < 60:
                residuals[isin] = np.nan
                continue
            X = np.column_stack([
                np.ones(valid.sum()),
                market[valid].to_numpy(),
                # Size is cross-sectional and constant through the window, so it
                # cannot enter as a time-series regressor; it scales the market
                # loading instead (a size-tilted market beta).
                market[valid].to_numpy() * (log_size.get(isin, np.nan)
                                            if np.isfinite(log_size.get(isin, np.nan))
                                            else 0.0),
            ])
            yv = y[valid].to_numpy()
            try:
                beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
            except np.linalg.LinAlgError:
                residuals[isin] = np.nan
                continue
            resid = pd.Series(yv - X @ beta, index=y[valid].index)
            # 12-1: drop the most recent month of residuals before compounding.
            resid = resid.iloc[:-21] if len(resid) > 21 else resid.iloc[:0]
            residuals[isin] = (1.0 + resid).prod() - 1.0 if len(resid) >= 120 else np.nan
        return pd.Series(residuals)


register(Momentum12_1())
register(Momentum6_1())
register(ShortTermReversal())
register(ResidualMomentum())
