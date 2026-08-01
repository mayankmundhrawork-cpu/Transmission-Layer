"""India-specific factors (§8).

§8 asks for these to be treated as first-class, not as an afterthought, and the
reasoning is sound: promoter behaviour is disclosed quarterly under LODR, is
mechanically informative about insider expectations, and is far less studied
than the standard factor zoo. In the smallcap tier a rising promoter pledge is
among the more plausible sources of genuine edge available from public
disclosure.

All of these come from shareholding-pattern and annual-report filings and are
therefore bitemporal facts like any other — read through `store.as_of`, with
the same publication-lag discipline. A pledge percentage is only usable from
the date the shareholding pattern was filed, not from the quarter it describes.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register, safe_divide


class PromoterHolding(Factor):
    """Promoter and promoter-group holding, percent of equity."""

    name = "promoter_holding"
    category = "india"
    period_type = "Q"
    required_facts = ("promoter_holding_pct",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return ctx.facts(["promoter_holding_pct"], period_type=self.period_type,
                         min_publication_lag_days=self.min_publication_lag_days
                         )["promoter_holding_pct"]


class PromoterHoldingChange(Factor):
    """Year-on-year change in promoter holding, percentage points.

    Promoters increasing their stake is a costly, public signal; reducing it is
    the same signal inverted. The level matters less than the direction, which
    is why this is carried separately from the level factor.
    """

    name = "promoter_holding_change"
    category = "india"
    period_type = "Q"
    required_facts = ("promoter_holding_pct",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        history = ctx.fact_history(
            "promoter_holding_pct", period_type=self.period_type, periods=5,
            min_publication_lag_days=self.min_publication_lag_days,
        )
        return _change(history, lag=4)


class PromoterPledge(Factor):
    """Percent of promoter holding that is pledged. Lower is better.

    A pledged promoter stake is leverage sitting on top of the equity, and an
    invisible one: a price fall can trigger a margin call that forces the
    lender to sell into the same fall. Several of the sharpest Indian smallcap
    collapses have this shape.
    """

    name = "promoter_pledge"
    category = "india"
    period_type = "Q"
    higher_is_better = False
    required_facts = ("promoter_pledge_pct",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(["promoter_pledge_pct"], period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        return facts["promoter_pledge_pct"]


class PromoterPledgeChange(Factor):
    """Year-on-year change in pledge percentage. Lower is better."""

    name = "promoter_pledge_change"
    category = "india"
    period_type = "Q"
    higher_is_better = False
    required_facts = ("promoter_pledge_pct",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        history = ctx.fact_history(
            "promoter_pledge_pct", period_type=self.period_type, periods=5,
            min_publication_lag_days=self.min_publication_lag_days,
        )
        return _change(history, lag=4)


class AuditorChangeFlag(Factor):
    """1.0 if the auditor changed in the trailing year, else 0.0. Lower is better.

    Extracted from annual-report filings by the §15 extraction layer, which
    records a source document hash and character offset for every field — so a
    flag here is verifiable against the original document rather than being an
    LLM's opinion. §2 forbids the model producing a *rating*; a located,
    citable boolean is a different thing.
    """

    name = "auditor_change"
    category = "india"
    higher_is_better = False
    required_facts = ("auditor_change_flag",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return ctx.facts(["auditor_change_flag"], period_type=self.period_type,
                         min_publication_lag_days=self.min_publication_lag_days
                         )["auditor_change_flag"]


class AuditorQualificationFlag(Factor):
    """1.0 if the audit opinion was qualified, else 0.0. Lower is better."""

    name = "auditor_qualification"
    category = "india"
    higher_is_better = False
    required_facts = ("auditor_qualification_flag",)

    def compute(self, ctx: FactorContext) -> pd.Series:
        return ctx.facts(["auditor_qualification_flag"], period_type=self.period_type,
                         min_publication_lag_days=self.min_publication_lag_days
                         )["auditor_qualification_flag"]


class RelatedPartyIntensity(Factor):
    """Related-party transaction value / revenue. Lower is better.

    A scaled measure of how much of the business runs through connected
    entities. Scaling by revenue is what makes it comparable across sizes; the
    raw rupee figure is mostly a size factor.
    """

    name = "rpt_intensity"
    category = "india"
    higher_is_better = False
    required_facts = ("related_party_value", "revenue")

    def compute(self, ctx: FactorContext) -> pd.Series:
        facts = ctx.facts(list(self.required_facts), period_type=self.period_type,
                          min_publication_lag_days=self.min_publication_lag_days)
        return safe_divide(facts["related_party_value"], facts["revenue"])


def _change(history: pd.DataFrame, lag: int) -> pd.Series:
    """Difference between the newest published value and the one `lag` periods
    earlier. Percentage-point change, not a growth rate — these series are
    already percentages and a ratio of percentages is not interpretable."""
    if history.shape[1] < lag + 1:
        return pd.Series(np.nan, index=history.index)
    return history.iloc[:, -1] - history.iloc[:, -(lag + 1)]


register(PromoterHolding())
register(PromoterHoldingChange())
register(PromoterPledge())
register(PromoterPledgeChange())
register(AuditorChangeFlag())
register(AuditorQualificationFlag())
register(RelatedPartyIntensity())
