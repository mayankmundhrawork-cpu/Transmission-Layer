"""The bitemporal fundamentals store — the single read path (§3.1, §7).

Every fundamental fact carries two times: the **period** it describes and the
**publication timestamp** at which it became public. `as_of(date)` returns only
what was public at `date`, resolving restatements by taking the highest
`revision_seq` among visible rows.

Why this is the centre of the platform: under SEBI LODR a company has up to 45
days after quarter end to file results and 60 after year end. A factor computed
on 31 March using the quarter ending 31 March is using a number that did not
exist for another six weeks. That is not a small bias — it is most of the
apparent alpha in naive fundamental backtests, and it is invisible in the
output because the backtest looks entirely reasonable.

Three layers stop it here:

1. **`as_of` is the only read.** `latest()` exists for exploration and is
   guarded at runtime: calling it from `src.factors` or `src.eval` raises.
2. **The table name is hostile.** ``_fundamental_fact_private`` is not
   something you type by accident.
3. **A static test** (`tests/platform/test_no_leak.py`, §18.5) fails the build
   if any module under `factors/` or `eval/` so much as mentions either.

Restatements are new rows, never updates — enforced by a SQLite trigger. That
makes restatement sensitivity of accruals and quality factors *measurable*
rather than invisible, which is the point of §7.
"""
from __future__ import annotations

import datetime as dt
import inspect
import sqlite3
from dataclasses import dataclass
from typing import Any, Iterable, Sequence

import pandas as pd

from src.store.schema import FUNDAMENTALS_TABLE, transaction

#: Modules that must never reach unfiltered fundamentals. Research code reads
#: `as_of` or it does not read at all.
FORBIDDEN_CALLER_PREFIXES = ("src.factors", "src.eval")

FACT_COLUMNS = [
    "isin", "fact_name", "period_type", "period_start", "period_end", "value",
    "unit", "source_doc_hash", "published_at", "revision_seq", "defensible",
]

PERIOD_TYPES = frozenset({"Q", "H", "A", "TTM"})


class LookAheadViolation(RuntimeError):
    """Raised when research code reaches for data it could not have had."""


class FactRejected(ValueError):
    """Raised when a fact cannot be admitted — usually a missing publication date.

    §5: "If a filing's publication timestamp cannot be established, the fact is
    rejected, not guessed."
    """


@dataclass(frozen=True)
class Fact:
    isin: str
    fact_name: str
    period_type: str
    period_start: str
    period_end: str
    value: float | None
    published_at: str
    source_doc_hash: str
    unit: str = "INR"
    revision_seq: int = 0
    defensible: bool = True


def _assert_caller_allowed(function_name: str) -> None:
    """Refuse calls originating in research modules.

    Walks the whole stack, not just the immediate caller: a helper in
    `src.store` called from `src.factors` is still a factor reading unfiltered
    fundamentals, and stopping at depth one would let that through.
    """
    frame = inspect.currentframe()
    try:
        while frame is not None:
            module = frame.f_globals.get("__name__", "")
            if module.startswith(FORBIDDEN_CALLER_PREFIXES):
                raise LookAheadViolation(
                    f"{function_name}() was called from {module}, which is research "
                    "code. Unfiltered fundamentals are not readable from "
                    f"{FORBIDDEN_CALLER_PREFIXES}; use store.as_of(date) so the "
                    "result is limited to what was public on that date."
                )
            frame = frame.f_back
    finally:
        del frame


class BitemporalStore:
    """Reads and writes fundamentals. `as_of` is the sanctioned read path."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    # -- writes ------------------------------------------------------------

    def add_fact(self, fact: Fact) -> int:
        """Append one fact. A restatement is a new row with a higher revision_seq."""
        if fact.period_type not in PERIOD_TYPES:
            raise FactRejected(f"unknown period_type {fact.period_type!r}")
        if not fact.published_at:
            raise FactRejected(
                f"{fact.isin} {fact.fact_name} {fact.period_end}: no publication "
                "timestamp. A fact whose publication date cannot be established "
                "is rejected, not guessed — it is exactly the look-ahead case."
            )
        if fact.published_at < fact.period_end:
            raise FactRejected(
                f"{fact.isin} {fact.fact_name}: published_at {fact.published_at} "
                f"precedes period_end {fact.period_end}. A result cannot be "
                "published before the period it reports has finished."
            )
        cur = self.conn.execute(
            f"INSERT OR REPLACE INTO {FUNDAMENTALS_TABLE}"
            " (isin, fact_name, period_type, period_start, period_end, value, unit,"
            "  source_doc_hash, published_at, revision_seq, defensible)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (fact.isin, fact.fact_name, fact.period_type, fact.period_start,
             fact.period_end, fact.value, fact.unit, fact.source_doc_hash,
             fact.published_at, fact.revision_seq, int(fact.defensible)),
        )
        return int(cur.lastrowid)

    def add_facts(self, facts: Iterable[Fact]) -> int:
        n = 0
        with transaction(self.conn):
            for fact in facts:
                self.add_fact(fact)
                n += 1
        return n

    def next_revision(self, isin: str, fact_name: str, period_end: str) -> int:
        row = self.conn.execute(
            f"SELECT MAX(revision_seq) m FROM {FUNDAMENTALS_TABLE}"
            " WHERE isin=? AND fact_name=? AND period_end=?",
            (isin, fact_name, period_end),
        ).fetchone()
        return 0 if row["m"] is None else int(row["m"]) + 1

    # -- THE read path -----------------------------------------------------

    def as_of(
        self,
        date: str | dt.date | pd.Timestamp,
        *,
        isins: Sequence[str] | None = None,
        fact_names: Sequence[str] | None = None,
        include_non_defensible: bool = False,
        min_publication_lag_days: int = 0,
    ) -> pd.DataFrame:
        """Facts public at `date`, one row per (isin, fact_name, period).

        `min_publication_lag_days` lets a factor demand an extra safety margin
        beyond the publication timestamp — useful when a source's timestamps
        are known to be optimistic, and required by §8 for factors that declare
        a minimum lag.
        """
        cutoff = _as_iso_datetime(date)
        if min_publication_lag_days:
            cutoff = _as_iso_datetime(
                pd.Timestamp(cutoff) - pd.Timedelta(days=min_publication_lag_days)
            )

        where = [f"published_at <= ?"]
        args: list[Any] = [cutoff]
        if not include_non_defensible:
            where.append("defensible = 1")
        if isins is not None:
            if not len(isins):
                return _empty_facts()
            where.append(f"isin IN ({','.join('?' * len(isins))})")
            args.extend(isins)
        if fact_names is not None:
            if not len(fact_names):
                return _empty_facts()
            where.append(f"fact_name IN ({','.join('?' * len(fact_names))})")
            args.extend(fact_names)

        sql = f"""
            SELECT {', '.join(FACT_COLUMNS)} FROM (
                SELECT *, ROW_NUMBER() OVER (
                    PARTITION BY isin, fact_name, period_type, period_end
                    ORDER BY revision_seq DESC, published_at DESC, fact_id DESC
                ) AS rn
                FROM {FUNDAMENTALS_TABLE}
                WHERE {' AND '.join(where)}
            ) WHERE rn = 1
        """
        frame = pd.read_sql_query(sql, self.conn, params=args)
        frame["defensible"] = frame["defensible"].astype(bool)
        return frame

    def as_of_latest_period(
        self,
        date: str | dt.date | pd.Timestamp,
        fact_names: Sequence[str],
        *,
        isins: Sequence[str] | None = None,
        period_type: str = "A",
        include_non_defensible: bool = False,
        min_publication_lag_days: int = 0,
        max_staleness_days: int | None = 550,
    ) -> pd.DataFrame:
        """Most recent published period per (isin, fact_name), as a wide frame.

        This is what factors actually consume: "the latest annual revenue that
        was public on 2019-06-28", indexed by ISIN with one column per fact.

        `max_staleness_days` drops facts whose period ended too long before
        `date`. Without it, a company that stopped filing in 2014 keeps
        contributing its 2014 fundamentals to a 2023 factor score forever —
        which is not look-ahead, but is its mirror image: a stale fact treated
        as current. The default spans an annual period plus the 60-day filing
        window plus slack.
        """
        facts = self.as_of(
            date, isins=isins, fact_names=fact_names,
            include_non_defensible=include_non_defensible,
            min_publication_lag_days=min_publication_lag_days,
        )
        if facts.empty:
            return pd.DataFrame(index=pd.Index([], name="isin"), columns=list(fact_names))

        facts = facts[facts["period_type"] == period_type]
        if max_staleness_days is not None:
            floor = (pd.Timestamp(_as_iso_datetime(date))
                     - pd.Timedelta(days=max_staleness_days)).date().isoformat()
            facts = facts[facts["period_end"] >= floor]
        if facts.empty:
            return pd.DataFrame(index=pd.Index([], name="isin"), columns=list(fact_names))

        latest = (
            facts.sort_values(["isin", "fact_name", "period_end", "revision_seq"])
            .groupby(["isin", "fact_name"], as_index=False)
            .last()
        )
        wide = latest.pivot(index="isin", columns="fact_name", values="value")
        for name in fact_names:
            if name not in wide.columns:
                wide[name] = float("nan")
        wide = wide[list(fact_names)]
        wide.columns.name = None
        return wide

    # -- exploration only --------------------------------------------------

    def latest(
        self, *, isins: Sequence[str] | None = None,
        fact_names: Sequence[str] | None = None,
    ) -> pd.DataFrame:
        """Newest revision of every fact, ignoring publication dates.

        EXPLORATORY ONLY. This is the look-ahead function: it returns
        restatements filed in 2024 for periods ending in 2015. It is guarded so
        that research code cannot call it, and it must never appear in a
        factor, a backtest, or an evaluation path.
        """
        _assert_caller_allowed("latest")
        where, args = ["1=1"], []
        if isins is not None:
            where.append(f"isin IN ({','.join('?' * len(isins))})")
            args.extend(isins)
        if fact_names is not None:
            where.append(f"fact_name IN ({','.join('?' * len(fact_names))})")
            args.extend(fact_names)
        sql = f"""
            SELECT {', '.join(FACT_COLUMNS)} FROM (
                SELECT *, ROW_NUMBER() OVER (
                    PARTITION BY isin, fact_name, period_type, period_end
                    ORDER BY revision_seq DESC, published_at DESC, fact_id DESC
                ) AS rn FROM {FUNDAMENTALS_TABLE} WHERE {' AND '.join(where)}
            ) WHERE rn = 1
        """
        return pd.read_sql_query(sql, self.conn, params=args)

    # -- diagnostics -------------------------------------------------------

    def revisions(self, isin: str, fact_name: str, period_end: str) -> pd.DataFrame:
        """Every version of one fact, oldest first — the restatement history."""
        return pd.read_sql_query(
            f"SELECT {', '.join(FACT_COLUMNS)} FROM {FUNDAMENTALS_TABLE}"
            " WHERE isin=? AND fact_name=? AND period_end=?"
            " ORDER BY revision_seq, published_at",
            self.conn, params=[isin, fact_name, period_end],
        )

    def publication_lags(self, period_type: str = "Q") -> pd.Series:
        """`published_at - period_end` in days, for acceptance test 3 (§18.3).

        Mass near zero means the indexing is wrong — it means facts are being
        stamped with their period end rather than their filing date, which
        silently reinstates the look-ahead this whole module prevents.
        """
        frame = pd.read_sql_query(
            f"SELECT period_end, published_at FROM {FUNDAMENTALS_TABLE}"
            " WHERE period_type=? AND revision_seq=0",
            self.conn, params=[period_type],
        )
        if frame.empty:
            return pd.Series(dtype="float64", name="publication_lag_days")
        lag = (pd.to_datetime(frame["published_at"]).dt.tz_localize(None)
               - pd.to_datetime(frame["period_end"])).dt.total_seconds() / 86400.0
        return lag.rename("publication_lag_days")

    def non_defensible_facts(self) -> pd.DataFrame:
        """Facts sourced from prototyping-only sources (§5). Any study touching
        one must print a prominent warning."""
        return pd.read_sql_query(
            f"SELECT DISTINCT isin, fact_name, source_doc_hash FROM {FUNDAMENTALS_TABLE}"
            " WHERE defensible = 0",
            self.conn,
        )

    def coverage(self) -> pd.DataFrame:
        return pd.read_sql_query(
            f"SELECT fact_name, period_type, COUNT(*) n,"
            f" COUNT(DISTINCT isin) securities, MIN(period_end) first_period,"
            f" MAX(period_end) last_period"
            f" FROM {FUNDAMENTALS_TABLE} GROUP BY fact_name, period_type"
            f" ORDER BY fact_name",
            self.conn,
        )


def _as_iso_datetime(value: str | dt.date | dt.datetime | pd.Timestamp) -> str:
    """Normalise a date to an ISO string comparable against `published_at`.

    A bare date means end of that day: a filing published at 14:30 on the
    rebalance date *was* public at the close, and treating the date as
    midnight would silently drop a day of genuinely available filings.
    """
    if isinstance(value, str):
        return value if len(value) > 10 else f"{value}T23:59:59.999999+00:00"
    if isinstance(value, dt.datetime):
        return value.isoformat()
    if isinstance(value, pd.Timestamp):
        return (value.isoformat() if value.time() != dt.time(0, 0)
                else f"{value.date().isoformat()}T23:59:59.999999+00:00")
    return f"{value.isoformat()}T23:59:59.999999+00:00"


def _empty_facts() -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series(dtype="object") for c in FACT_COLUMNS})
