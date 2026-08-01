"""Point-in-time universe construction (§3.2, §6).

`Universe.as_of(date, tier)` returns the investable set on a date using only
information available on that date. Every screen is evaluated against data
strictly at or before `date`, and the candidate pool comes from
`SecurityMaster.listed_on(date)`, which includes securities that have since
been delisted, merged, or suspended.

That last point is the entire survivorship defence and it is worth being blunt
about: there is no code path here that filters to "still listed today". Adding
one would require deliberately writing a query against today's date, which is
the kind of thing that shows up in review.

The screens (§6) and why each exists:

* **listed and not suspended** — you cannot buy a suspended scrip.
* **minimum listing history** (250 sessions) — a factor needing trailing data
  cannot be computed on a three-month-old listing, and IPO-window returns are
  a different phenomenon from the one being studied.
* **minimum median traded value** (trailing 60 sessions) — the smallcap tier is
  full of names that print a trade a week. They are not investable at any size
  and their "returns" are stale-price artefacts.
* **price floor** — sub-₹5 scrips have tick-size-dominated returns; a one-tick
  move is 2%+, which manufactures volatility and momentum that cannot be
  captured net of cost.
* **ASM/GSM stage 2+ excluded** — 100% margin, trade-to-trade settlement, and
  in stage 4 a weekly auction. Not transactable on a rebalance schedule.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass, replace
from typing import Any, Iterable, Sequence

import pandas as pd

from src.master.security import DateLike, SecurityMaster, as_iso

#: Tier -> index name whose membership defines the candidate pool. A tier
#: mapped to None takes every listed security instead of an index list.
TIER_INDEX: dict[str, str | None] = {
    "nifty500": "NIFTY 500",
    # "smallcap-inclusive" means the 500 plus the smallcap tier below it, which
    # is what NIFTY TOTAL MARKET spans. Falls back to the unrestricted pool if
    # that membership history has not been reconstructed yet.
    "smallcap_inclusive": "NIFTY TOTAL MARKET",
    "total_market": None,
}


@dataclass(frozen=True)
class UniverseScreens:
    """§6 screen parameters. Defaults are the spec's; a study may declare its
    own in its pre-registration, but never tune them against results."""

    min_listing_sessions: int = 250
    turnover_lookback_sessions: int = 60
    min_median_turnover_inr: float = 2_500_000.0  # ₹25 lakh/day
    min_price_inr: float = 5.0
    max_surveillance_stage: int = 1  # stage 2 and above are excluded
    require_index_membership: bool = True

    def describe(self) -> dict[str, Any]:
        return dict(vars(self))


@dataclass(frozen=True)
class UniverseResult:
    """The universe on a date, plus why everything else was excluded.

    The exclusion counts are not decoration. A universe that halves between two
    quarters is either a real regulatory event or a bug, and CP6 asks you to
    tell the difference — which you cannot do from the surviving names alone.
    """

    date: str
    tier: str
    members: pd.DataFrame  # isin, symbol, sector, close, median_turnover, sessions
    excluded: dict[str, int]
    screens: UniverseScreens

    @property
    def isins(self) -> list[str]:
        return list(self.members["isin"])

    def __len__(self) -> int:
        return len(self.members)


class Universe:
    def __init__(self, conn: sqlite3.Connection, master: SecurityMaster | None = None) -> None:
        self.conn = conn
        self.master = master or SecurityMaster(conn)

    # -- index membership --------------------------------------------------

    def index_members(self, index_name: str, date: DateLike) -> set[str]:
        d = as_iso(date)
        return {
            r["isin"] for r in self.conn.execute(
                "SELECT isin FROM index_membership"
                " WHERE index_name=? AND effective_from<=?"
                "   AND (effective_to IS NULL OR effective_to>=?)",
                (index_name, d, d),
            )
        }

    def has_index_history(self, index_name: str) -> bool:
        row = self.conn.execute(
            "SELECT 1 FROM index_membership WHERE index_name=? LIMIT 1", (index_name,)
        ).fetchone()
        return row is not None

    # -- the main query ----------------------------------------------------

    def as_of(
        self, date: DateLike, tier: str = "smallcap_inclusive",
        screens: UniverseScreens | None = None,
    ) -> UniverseResult:
        """The investable set on `date`, using only data available on `date`."""
        if tier not in TIER_INDEX:
            raise ValueError(f"unknown tier {tier!r}; expected one of {sorted(TIER_INDEX)}")
        screens = screens or UniverseScreens()
        d = as_iso(date)
        excluded: dict[str, int] = {}

        # 1. Everything listed on the date — delisted-inclusive by construction.
        candidates = set(self.master.listed_on(d))
        excluded["not_listed"] = 0  # by definition zero; recorded for symmetry

        # 2. Index membership, if the tier is index-defined and we have history.
        index_name = TIER_INDEX[tier]
        if index_name and screens.require_index_membership:
            if self.has_index_history(index_name):
                members = self.index_members(index_name, d)
                excluded["not_in_index"] = len(candidates - members)
                candidates &= members
            else:
                # Be loud rather than silently widening the universe: a tier
                # that quietly becomes "everything" would make a nifty500 study
                # a total-market study without anyone noticing.
                excluded["index_history_missing"] = 1
        else:
            excluded["not_in_index"] = 0

        if not candidates:
            return UniverseResult(d, tier, _empty_members(), excluded, screens)

        # 3. Suspension.
        before = len(candidates)
        candidates = {i for i in candidates if not self.master.is_suspended_at(i, d)}
        excluded["suspended"] = before - len(candidates)

        # 4. Surveillance stage 2+.
        before = len(candidates)
        candidates = {
            i for i in candidates
            if self.master.surveillance_stage_at(i, d) <= screens.max_surveillance_stage
        }
        excluded["surveillance_stage_2_plus"] = before - len(candidates)

        # 5. Price/liquidity/history screens, all from data at or before `date`.
        stats = self._trailing_stats(candidates, d, screens)
        if stats.empty:
            excluded["no_price_history"] = len(candidates)
            return UniverseResult(d, tier, _empty_members(), excluded, screens)

        excluded["no_price_history"] = len(candidates) - len(stats)

        before = len(stats)
        stats = stats[stats["sessions"] >= screens.min_listing_sessions]
        excluded["insufficient_history"] = before - len(stats)

        before = len(stats)
        stats = stats[stats["close"] >= screens.min_price_inr]
        excluded["below_price_floor"] = before - len(stats)

        before = len(stats)
        stats = stats[stats["median_turnover"] >= screens.min_median_turnover_inr]
        excluded["illiquid"] = before - len(stats)

        stats = stats.sort_values("isin").reset_index(drop=True)
        stats["sector"] = [self.master.attribute_at(i, "sector", d) for i in stats["isin"]]
        stats["symbol"] = [self.master.symbol_at(i, d) for i in stats["isin"]]
        return UniverseResult(d, tier, stats, excluded, screens)

    def _trailing_stats(
        self, isins: Iterable[str], date: str, screens: UniverseScreens
    ) -> pd.DataFrame:
        """Per-ISIN trailing statistics computed strictly at or before `date`."""
        isins = list(isins)
        if not isins:
            return _empty_members()

        # Pull a generous calendar window and take the last N *sessions* per
        # name from it — trading days per calendar day is not constant, and a
        # fixed calendar lookback would silently use fewer sessions around
        # holiday clusters.
        window_start = (
            dt.date.fromisoformat(date)
            - dt.timedelta(days=int(screens.turnover_lookback_sessions * 2.2) + 10)
        ).isoformat()

        placeholders = ",".join("?" * len(isins))
        recent = pd.read_sql_query(
            f"SELECT isin, date, close, turnover FROM price_daily"
            f" WHERE date<=? AND date>=? AND isin IN ({placeholders})"
            f" ORDER BY isin, date",
            self.conn, params=[date, window_start, *isins],
        )
        if recent.empty:
            return _empty_members()

        tail = (
            recent.groupby("isin", group_keys=False)
            .tail(screens.turnover_lookback_sessions)
        )
        agg = tail.groupby("isin").agg(
            close=("close", "last"),
            median_turnover=("turnover", "median"),
            recent_sessions=("close", "size"),
        )

        # Total sessions ever observed on or before the date — the listing
        # history screen. Separate query because the trailing window cannot
        # answer it.
        history = pd.read_sql_query(
            f"SELECT isin, COUNT(*) AS sessions FROM price_daily"
            f" WHERE date<=? AND isin IN ({placeholders}) GROUP BY isin",
            self.conn, params=[date, *isins],
        ).set_index("isin")

        stats = agg.join(history, how="left").fillna({"sessions": 0}).reset_index()
        stats["median_turnover"] = stats["median_turnover"].fillna(0.0)
        return stats

    # -- liquidity helpers used by §9 and §13 ------------------------------

    def median_turnover(self, isin: str, date: DateLike, sessions: int = 60) -> float:
        """Trailing median daily traded value in rupees, at or before `date`."""
        stats = self._trailing_stats(
            [isin], as_iso(date), UniverseScreens(turnover_lookback_sessions=sessions)
        )
        return float(stats["median_turnover"].iloc[0]) if not stats.empty else 0.0

    def days_to_liquidate(
        self, isin: str, notional_inr: float, date: DateLike,
        participation_pct: float = 5.0, sessions: int = 60,
    ) -> float:
        """Sessions needed to exit a position at the participation cap.

        Reported for every held position (§9). `inf` means the name does not
        trade enough to be exited at all at this size, which is a portfolio
        construction error rather than a slow exit.
        """
        adv = self.median_turnover(isin, date, sessions)
        capacity = adv * participation_pct / 100.0
        if capacity <= 0:
            return float("inf")
        return notional_inr / capacity


def _empty_members() -> pd.DataFrame:
    return pd.DataFrame({
        "isin": pd.Series(dtype="object"),
        "close": pd.Series(dtype="float"),
        "median_turnover": pd.Series(dtype="float"),
        "recent_sessions": pd.Series(dtype="int"),
        "sessions": pd.Series(dtype="int"),
    })


def universe_size_series(
    universe: Universe, dates: Sequence[DateLike], tier: str = "smallcap_inclusive",
    screens: UniverseScreens | None = None,
) -> pd.DataFrame:
    """Universe size over time — the CP6 diagnostic.

    Returns the member count and every exclusion count per date, because a
    discontinuity is only interpretable if you can see which screen caused it.
    """
    rows = []
    for date in dates:
        result = universe.as_of(date, tier, screens)
        rows.append({"date": as_iso(date), "members": len(result), **result.excluded})
    return pd.DataFrame(rows).fillna(0)
