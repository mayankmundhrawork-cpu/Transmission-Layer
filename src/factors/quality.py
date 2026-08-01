"""Quality factors (§8)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register, safe_divide


class ReturnOnEquity(Factor):
    """Net profit / book equity."""

    name = "roe"
    category = "quality"
    required_facts = ("net_profit", "total_equity")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        return safe_divide(facts["net_profit"], facts["total_equity"])


class ReturnOnInvestedCapital(Factor):
    """NOPAT / invested capital.

        NOPAT            = PBT x (1 - effective tax rate)
        invested capital = total equity + total debt - cash

    Effective tax rate is taken from the filing rather than assumed at the
    statutory rate; Indian effective rates vary widely with MAT credits,
    incentives, and the 2019 concessional regime, and a flat assumption would
    make ROIC partly a tax-regime proxy.
    """

    name = "roic"
    category = "quality"
    required_facts = ("profit_before_tax", "tax_expense", "total_equity",
                      "borrowings_current", "borrowings_noncurrent", "cash")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        pbt = facts["profit_before_tax"]
        tax_rate = safe_divide(facts["tax_expense"], pbt).clip(0.0, 0.6).fillna(0.25)
        nopat = pbt * (1.0 - tax_rate)
        invested = (facts["total_equity"]
                    + facts["borrowings_current"].fillna(0.0)
                    + facts["borrowings_noncurrent"].fillna(0.0)
                    - facts["cash"].fillna(0.0))
        return safe_divide(nopat, invested)


class GrossProfitability(Factor):
    """Gross profit / total assets.

    Novy-Marx (2013), "The Other Side of Value: The Gross Profitability
    Premium". Deliberately scaled by *assets*, not sales or equity — that is
    the paper's construction and the reason the factor is not just a
    slow-moving proxy for margin.

        gross profit = revenue - (materials + purchases + inventory change)
    """

    name = "gross_profitability"
    category = "quality"
    required_facts = ("revenue", "cost_of_materials", "purchases_stock_in_trade",
                      "inventory_change", "total_assets")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        cogs = (facts["cost_of_materials"].fillna(0.0)
                + facts["purchases_stock_in_trade"].fillna(0.0)
                + facts["inventory_change"].fillna(0.0))
        gross_profit = facts["revenue"] - cogs
        # With no COGS components at all the "gross profit" is just revenue,
        # which is a different factor wearing this one's name.
        has_cogs = facts[["cost_of_materials", "purchases_stock_in_trade",
                          "inventory_change"]].notna().any(axis=1)
        return safe_divide(gross_profit.where(has_cogs), facts["total_assets"])


class SloanAccruals(Factor):
    """Balance-sheet accruals, scaled by total assets.

    Sloan (1996), "Do Stock Prices Fully Reflect Information in Accruals and
    Cash Flows About Future Earnings?".

        accruals = (net profit - operating cash flow) / total assets

    Signed so that **lower accruals are better** — high accruals predict poor
    subsequent returns. `higher_is_better = False` makes that explicit rather
    than leaving the sign to a convention someone has to remember downstream.
    """

    name = "accruals"
    category = "quality"
    higher_is_better = False
    required_facts = ("net_profit", "cfo", "total_assets")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        accruals = facts["net_profit"] - facts["cfo"]
        return safe_divide(accruals, facts["total_assets"])


class DebtToEquity(Factor):
    """Total debt / book equity. Lower is better."""

    name = "debt_to_equity"
    category = "quality"
    higher_is_better = False
    required_facts = ("borrowings_current", "borrowings_noncurrent", "total_equity")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        debt = (facts["borrowings_current"].fillna(0.0)
                + facts["borrowings_noncurrent"].fillna(0.0))
        return safe_divide(debt, facts["total_equity"])


class EarningsVariability(Factor):
    """Standard deviation of annual earnings growth over trailing periods.

    A stability measure in the sense of the quality literature (e.g. Asness,
    Frazzini & Pedersen (2019), "Quality Minus Junk"). Lower is better.
    """

    name = "earnings_variability"
    category = "quality"
    higher_is_better = False
    required_facts = ("net_profit",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        history = ctx.fact_history(
            "net_profit", period_type=self.period_type, periods=5,
            min_publication_lag_days=self.min_publication_lag_days,
        )
        if history.shape[1] < 3:
            return pd.Series(np.nan, index=history.index)
        # Scale by mean absolute earnings rather than taking growth rates: a
        # year passing through zero makes percentage growth explode, and loss
        # years are common in this tier.
        scale = history.abs().mean(axis=1).replace(0.0, np.nan)
        variability = history.std(axis=1) / scale
        return variability.where(history.notna().sum(axis=1) >= 3)


class InterestCoverage(Factor):
    """EBIT / finance cost.

    A debt-servicing measure. Companies with no borrowing have no finance cost
    and an undefined ratio; they are given the cross-sectional maximum rather
    than NaN, because "cannot compute" and "does not need to" are different
    states and treating a debt-free company as missing would drop exactly the
    names this factor should rank highest.
    """

    name = "interest_coverage"
    category = "quality"
    required_facts = ("profit_before_tax", "finance_cost")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        finance_cost = facts["finance_cost"]
        ebit = facts["profit_before_tax"] + finance_cost.fillna(0.0)
        coverage = safe_divide(ebit, finance_cost)

        debt_free = finance_cost.notna() & (finance_cost <= 0) & facts["profit_before_tax"].notna()
        if debt_free.any() and coverage.notna().any():
            coverage = coverage.copy()
            coverage[debt_free] = coverage.max()
        return coverage


register(ReturnOnEquity())
register(ReturnOnInvestedCapital())
register(GrossProfitability())
register(SloanAccruals())
register(DebtToEquity())
register(EarningsVariability())
register(InterestCoverage())
