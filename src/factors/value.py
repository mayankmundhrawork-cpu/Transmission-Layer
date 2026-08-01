"""Value factors (§8).

Standard definitions. Each docstring cites the definition being implemented.

A note that applies to all of them: the denominator guard in `safe_divide` is
not defensive coding. Book-to-price with negative book equity produces a large
negative number that sorts as "expensive" when the company is in fact
insolvent, and in the Indian smallcap tier negative-equity names are common
enough that letting them through materially changes the top decile. NaN is the
honest answer, and the universe screen — not the factor — is where such names
should be excluded if a study wants them out.
"""
from __future__ import annotations

import pandas as pd

from src.factors.base import Factor, FactorContext, register, safe_divide


class EarningsYield(Factor):
    """Trailing net profit / market cap.

    Basu (1977), "Investment Performance of Common Stocks in Relation to Their
    Price-Earnings Ratios". Inverted here so that higher is cheaper, which
    keeps the sign convention consistent across the value family and avoids the
    infinity at zero earnings that P/E has.
    """

    name = "earnings_yield"
    category = "value"
    required_facts = ("net_profit",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(["net_profit"], period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        return safe_divide(facts["net_profit"], ctx.market_cap)


class BookToPrice(Factor):
    """Book equity / market cap.

    Fama & French (1992), "The Cross-Section of Expected Stock Returns" —
    the HML construction. Book equity is total equity attributable to owners.
    """

    name = "book_to_price"
    category = "value"
    required_facts = ("total_equity",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(["total_equity"], period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        return safe_divide(facts["total_equity"], ctx.market_cap)


class SalesToPrice(Factor):
    """Revenue / market cap.

    Barbee, Mukherji & Raines (1996). Robust where earnings and book are
    distorted — which in this universe means loss-making and
    recently-written-down companies, where earnings yield and book-to-price
    both go NaN or negative and sales-to-price still ranks.
    """

    name = "sales_to_price"
    category = "value"
    required_facts = ("revenue",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(["revenue"], period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        return safe_divide(facts["revenue"], ctx.market_cap)


class EbitdaToEv(Factor):
    """EBITDA / enterprise value.

    Loughran & Wellman (2011), "New Evidence on the Relation Between the
    Enterprise Multiple and Average Stock Returns" — the EV/EBITDA multiple,
    inverted.

        EBITDA = PBT + finance cost + depreciation
        EV     = market cap + total debt - cash

    Capital-structure neutral, which matters here: leverage varies enormously
    across Indian smallcaps and equity-only multiples confound cheapness with
    balance-sheet risk.
    """

    name = "ebitda_to_ev"
    category = "value"
    required_facts = ("profit_before_tax", "finance_cost", "depreciation",
                      "borrowings_current", "borrowings_noncurrent", "cash")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        ebitda = (facts["profit_before_tax"]
                  + facts["finance_cost"].fillna(0.0)
                  + facts["depreciation"].fillna(0.0))
        debt = (facts["borrowings_current"].fillna(0.0)
                + facts["borrowings_noncurrent"].fillna(0.0))
        ev = ctx.market_cap + debt - facts["cash"].fillna(0.0)
        return safe_divide(ebitda, ev)


class FreeCashFlowYield(Factor):
    """(Operating cash flow - capex) / market cap.

    The cash-flow analogue of earnings yield. Harder to manage than accrual
    earnings, which is precisely the argument for it — see Sloan (1996) and the
    accruals factor in quality.py.
    """

    name = "fcf_yield"
    category = "value"
    required_facts = ("cfo", "capex")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(["cfo", "capex"], period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        # Capex is reported as a positive outflow in Ind-AS cash-flow
        # statements; take the magnitude so a sign convention in the filing
        # cannot flip free cash flow's meaning.
        fcf = facts["cfo"] - facts["capex"].abs().fillna(0.0)
        return safe_divide(fcf, ctx.market_cap)


register(EarningsYield())
register(BookToPrice())
register(SalesToPrice())
register(EbitdaToEv())
register(FreeCashFlowYield())
