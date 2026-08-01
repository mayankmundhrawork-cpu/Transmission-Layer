"""Growth factors (§8)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register


def _cagr(history: pd.DataFrame, years: int) -> pd.Series:
    """Compound annual growth from the oldest to the newest published period.

    Only rows with a positive starting value get a CAGR. Growth from a loss or
    from zero is not a percentage — a company going from -10 to +5 has no
    meaningful "growth rate", and computing one produces a large positive
    number that ranks it alongside genuine compounders. NaN is correct.
    """
    if history.shape[1] < years + 1:
        return pd.Series(np.nan, index=history.index)
    window = history.iloc[:, -(years + 1):]
    start = window.iloc[:, 0]
    end = window.iloc[:, -1]
    valid = start.notna() & end.notna() & (start > 0) & (end > 0)
    cagr = (end / start) ** (1.0 / years) - 1.0
    return cagr.where(valid)


class RevenueCagr3Y(Factor):
    """3-year revenue CAGR from published annual filings."""

    name = "revenue_cagr_3y"
    category = "growth"
    required_facts = ("revenue",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return _cagr(ctx.fact_history("revenue", periods=6,
                                      min_publication_lag_days=self.min_publication_lag_days), 3)


class RevenueCagr5Y(Factor):
    """5-year revenue CAGR."""

    name = "revenue_cagr_5y"
    category = "growth"
    required_facts = ("revenue",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return _cagr(ctx.fact_history("revenue", periods=6,
                                      min_publication_lag_days=self.min_publication_lag_days), 5)


class EarningsCagr3Y(Factor):
    """3-year net profit CAGR."""

    name = "earnings_cagr_3y"
    category = "growth"
    required_facts = ("net_profit",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return _cagr(ctx.fact_history("net_profit", periods=6,
                                      min_publication_lag_days=self.min_publication_lag_days), 3)


class EarningsCagr5Y(Factor):
    """5-year net profit CAGR."""

    name = "earnings_cagr_5y"
    category = "growth"
    required_facts = ("net_profit",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return _cagr(ctx.fact_history("net_profit", periods=6,
                                      min_publication_lag_days=self.min_publication_lag_days), 5)


register(RevenueCagr3Y())
register(RevenueCagr5Y())
register(EarningsCagr3Y())
register(EarningsCagr5Y())
