"""Factor base class and evaluation context (§8).

A factor is a class that declares what it needs and computes a cross-sectional
score:

    compute(as_of_date, universe) -> pd.Series indexed by ISIN

Every factor declares `required_facts` and `min_publication_lag_days`, and
reads fundamentals **only** through `store.as_of` — reached via
:class:`FactorContext`, which bounds every query at the as-of date.

That bounding is structural rather than conventional. `FactorContext` takes the
as-of date in its constructor and passes it into every price and fact query it
makes; a factor cannot ask it for data past that date because there is no
parameter with which to ask. The class also holds no reference to `latest()`,
and the static check in `tests/platform/test_no_leak.py` fails CI if any module
in this package so much as names it.

Scores are returned raw and unstandardised. Winsorising, z-scoring, and sector
neutralisation are §10 preprocessing decisions that belong to a
pre-registration, not to a factor — a factor that standardises internally has
quietly made a specification choice on the researcher's behalf.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Any, Sequence

import numpy as np
import pandas as pd

from src.prices.daily import daily_returns, price_panel
from src.store.bitemporal import BitemporalStore

#: Trailing calendar days of price history loaded by default. Enough for a
#: 3-year beta and a 12-month momentum window with holidays.
DEFAULT_PRICE_LOOKBACK_DAYS = 1200


class FactorContext:
    """Data access for one (as_of_date, universe) evaluation.

    Constructed once per rebalance date and shared across factors, so a panel
    of 40 factors over 20 dates is 20 price loads rather than 800.
    """

    def __init__(
        self,
        conn: sqlite3.Connection,
        as_of_date: str | dt.date,
        universe: Sequence[str],
        *,
        price_lookback_days: int = DEFAULT_PRICE_LOOKBACK_DAYS,
        include_non_defensible: bool = False,
    ) -> None:
        self.conn = conn
        self.as_of_date = _iso(as_of_date)
        self.universe = list(universe)
        self.price_lookback_days = price_lookback_days
        self.include_non_defensible = include_non_defensible
        self._store = BitemporalStore(conn)
        self._fact_cache: dict[tuple, pd.DataFrame] = {}

    # -- fundamentals ------------------------------------------------------

    def facts(
        self, fact_names: Sequence[str], *, period_type: str = "A",
        min_publication_lag_days: int = 0, max_staleness_days: int | None = 550,
    ) -> pd.DataFrame:
        """Wide frame of the latest facts public at the as-of date.

        There is deliberately no `date` parameter: the as-of date is fixed at
        construction, so a factor has no way to ask this context about a
        different date.
        """
        key = (tuple(fact_names), period_type, min_publication_lag_days,
               max_staleness_days)
        if key not in self._fact_cache:
            self._fact_cache[key] = self._store.as_of_latest_period(
                self.as_of_date, fact_names, isins=self.universe,
                period_type=period_type,
                include_non_defensible=self.include_non_defensible,
                min_publication_lag_days=min_publication_lag_days,
                max_staleness_days=max_staleness_days,
            )
        return self._fact_cache[key].reindex(self.universe)

    def fact_history(
        self, fact_name: str, *, period_type: str = "A", periods: int = 5,
        min_publication_lag_days: int = 0,
    ) -> pd.DataFrame:
        """Last `periods` published values per ISIN — index=isin, columns=period_end.

        Used by growth (CAGR over trailing periods) and earnings variability.
        Only periods whose filings were public at the as-of date appear.
        """
        raw = self._store.as_of(
            self.as_of_date, isins=self.universe, fact_names=[fact_name],
            include_non_defensible=self.include_non_defensible,
            min_publication_lag_days=min_publication_lag_days,
        )
        if raw.empty:
            return pd.DataFrame(index=pd.Index(self.universe, name="isin"))
        raw = raw[raw["period_type"] == period_type]
        if raw.empty:
            return pd.DataFrame(index=pd.Index(self.universe, name="isin"))
        wide = raw.pivot_table(index="isin", columns="period_end", values="value",
                               aggfunc="last")
        wide = wide.reindex(sorted(wide.columns), axis=1).iloc[:, -periods:]
        return wide.reindex(self.universe)

    # -- prices ------------------------------------------------------------

    @cached_property
    def _price_start(self) -> str:
        return (dt.date.fromisoformat(self.as_of_date)
                - dt.timedelta(days=self.price_lookback_days)).isoformat()

    @cached_property
    def closes(self) -> pd.DataFrame:
        return price_panel(self.conn, self.universe, self._price_start,
                           self.as_of_date, ("close",))

    @cached_property
    def turnover(self) -> pd.DataFrame:
        return price_panel(self.conn, self.universe, self._price_start,
                           self.as_of_date, ("turnover",))

    @cached_property
    def highs(self) -> pd.DataFrame:
        return price_panel(self.conn, self.universe, self._price_start,
                           self.as_of_date, ("high",))

    @cached_property
    def lows(self) -> pd.DataFrame:
        return price_panel(self.conn, self.universe, self._price_start,
                           self.as_of_date, ("low",))

    @cached_property
    def returns(self) -> pd.DataFrame:
        return daily_returns(self.conn, self.universe, self._price_start,
                             self.as_of_date)

    @cached_property
    def last_close(self) -> pd.Series:
        if self.closes.empty:
            return pd.Series(dtype="float64", index=pd.Index(self.universe))
        return self.closes.ffill().iloc[-1].reindex(self.universe)

    @cached_property
    def benchmark(self) -> pd.Series:
        from src.config import get_config
        from src.prices.daily import benchmark_returns

        return benchmark_returns(self.conn, get_config().benchmark,
                                 self._price_start, self.as_of_date)

    # -- market cap --------------------------------------------------------

    @cached_property
    def shares(self) -> pd.DataFrame:
        """Share counts and free float, as published at or before the as-of date.

        Shareholding patterns are filed with a lag under LODR, so this is a
        bitemporal read like any other: `published_at <= as_of`.
        """
        if not self.universe:
            return pd.DataFrame(columns=["total_shares", "free_float_pct"])
        placeholders = ",".join("?" * len(self.universe))
        frame = pd.read_sql_query(
            "SELECT isin, total_shares, free_float_pct, as_of_date, published_at"
            f" FROM shares_outstanding WHERE published_at <= ? AND isin IN ({placeholders})"
            " ORDER BY isin, as_of_date, published_at",
            self.conn, params=[f"{self.as_of_date}T23:59:59+00:00", *self.universe],
        )
        if frame.empty:
            return pd.DataFrame(columns=["total_shares", "free_float_pct"])
        return (frame.groupby("isin").last()[["total_shares", "free_float_pct"]]
                .reindex(self.universe))

    @cached_property
    def market_cap(self) -> pd.Series:
        """Full market capitalisation in rupees."""
        shares = self.shares.reindex(self.universe)["total_shares"]
        return (self.last_close * shares).rename("market_cap")

    @cached_property
    def free_float_market_cap(self) -> pd.Series:
        """Free-float market cap (§8).

        Indian promoter holdings run 50-75%, so free float and full cap diverge
        sharply and the size factor must use free float. Both are stored;
        defaulting to full cap would make "size" mostly a promoter-holding
        proxy.
        """
        shares = self.shares.reindex(self.universe)
        float_pct = shares["free_float_pct"].fillna(100.0) / 100.0
        return (self.last_close * shares["total_shares"] * float_pct
                ).rename("free_float_market_cap")


class Factor(ABC):
    """Base class for every factor (§8)."""

    #: Stable identifier used in pre-registrations and the trial registry.
    name: str = ""
    #: Facts this factor reads. Declared so coverage can be checked before a run.
    required_facts: tuple[str, ...] = ()
    #: Extra safety margin beyond the publication timestamp, in days.
    min_publication_lag_days: int = 0
    #: Fundamental period this factor consumes.
    period_type: str = "A"
    #: Higher score = more attractive? Declared so quantile portfolios and IC
    #: signs are unambiguous rather than a convention someone has to remember.
    higher_is_better: bool = True
    #: One-line description; the docstring carries the literature citation.
    category: str = "other"

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        # ABCMeta has not populated __abstractmethods__ yet at this point, so
        # ask `compute` directly whether it is still abstract.
        concrete = not getattr(cls.compute, "__isabstractmethod__", False)
        if concrete and not cls.name:
            raise TypeError(f"{cls.__name__} must declare a `name`")

    @abstractmethod
    def compute(self, ctx: FactorContext) -> pd.Series:
        """Raw cross-sectional score indexed by ISIN. NaN where uncomputable."""

    def __call__(self, ctx: FactorContext) -> pd.Series:
        score = self.compute(ctx)
        if not isinstance(score, pd.Series):
            raise TypeError(f"{self.name}.compute must return a Series")
        return score.reindex(ctx.universe).rename(self.name).astype("float64")

    def describe(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "category": self.category,
            "required_facts": list(self.required_facts),
            "min_publication_lag_days": self.min_publication_lag_days,
            "period_type": self.period_type,
            "higher_is_better": self.higher_is_better,
            "doc": (self.__doc__ or "").strip().split("\n")[0],
        }

    def __repr__(self) -> str:
        return f"<Factor {self.name}>"


def safe_divide(numerator: pd.Series, denominator: pd.Series,
                *, positive_denominator: bool = True) -> pd.Series:
    """Elementwise division that returns NaN rather than +/-inf.

    `positive_denominator` guards ratios where a negative denominator inverts
    the ranking's meaning: book-to-price with negative book equity produces a
    large negative number that sorts as "expensive" when the company is
    actually insolvent. NaN is the honest answer.
    """
    num = pd.to_numeric(numerator, errors="coerce")
    den = pd.to_numeric(denominator, errors="coerce")
    den = den.where(den > 0) if positive_denominator else den.where(den != 0)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def _iso(value: str | dt.date | pd.Timestamp) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, pd.Timestamp):
        return value.date().isoformat()
    return value.isoformat()


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

_REGISTRY: dict[str, Factor] = {}


def register(factor: Factor) -> Factor:
    if factor.name in _REGISTRY:
        raise ValueError(f"duplicate factor name {factor.name!r}")
    _REGISTRY[factor.name] = factor
    return factor


def get_factor(name: str) -> Factor:
    try:
        return _REGISTRY[name]
    except KeyError:
        raise KeyError(f"unknown factor {name!r}; known: {sorted(_REGISTRY)}") from None


def all_factors() -> dict[str, Factor]:
    _load_all()
    return dict(_REGISTRY)


def _load_all() -> None:
    from src.factors import (  # noqa: F401  (import for side-effect registration)
        growth, india, momentum, quality, risk, size, value,
    )
