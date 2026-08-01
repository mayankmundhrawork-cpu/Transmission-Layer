"""ISIN-keyed security master (§3.3, §6).

The master answers, for any historical date: what was this ISIN called, was it
listed, was it suspended, what sector was it in, and — if it stopped existing —
what happened to it.

Why ISIN and not symbol (§3.3): NSE symbols are recycled and renamed. A
platform keyed on symbol splices two unrelated companies' return series
together at a rename and calls the join a stock. Every table here keys on ISIN;
`symbol` is a *validity-dated attribute*, so `symbol_at(isin, date)` and
`resolve_symbol(symbol, date)` both give the right answer for the date asked
about rather than for today.

Delisting is recorded, not deleted (§3.2). A company that delisted in 2017 is
still in the master, still has its listing window, and still appears in
`universe.as_of(t)` for t inside that window. That is the whole survivorship
defence: the code has no way to express "currently listed names only" without
someone deliberately writing that filter.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass
from typing import Any, Iterable, Sequence

import pandas as pd

DateLike = str | dt.date | pd.Timestamp


def as_iso(date: DateLike) -> str:
    if isinstance(date, str):
        return dt.date.fromisoformat(date).isoformat()
    if isinstance(date, pd.Timestamp):
        return date.date().isoformat()
    return date.isoformat()


@dataclass(frozen=True)
class SecurityRecord:
    """A security as it stood on a particular date."""

    isin: str
    symbol: str | None
    name: str | None
    sector: str | None
    listing_date: str | None
    delisting_date: str | None
    delisting_reason: str | None
    is_listed: bool
    is_suspended: bool


class SecurityMaster:
    """Reads and writes the ISIN master. All queries are date-parameterised."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    # -- writes ------------------------------------------------------------

    def upsert_security(self, isin: str, *, first_seen: str | None = None,
                        last_seen: str | None = None, source_doc_hash: str | None = None) -> None:
        _validate_isin(isin)
        self.conn.execute(
            "INSERT INTO security (isin, first_seen, last_seen, source_doc_hash)"
            " VALUES (?,?,?,?)"
            " ON CONFLICT(isin) DO UPDATE SET"
            "   first_seen = MIN(COALESCE(security.first_seen, excluded.first_seen),"
            "                    COALESCE(excluded.first_seen, security.first_seen)),"
            "   last_seen  = MAX(COALESCE(security.last_seen, excluded.last_seen),"
            "                    COALESCE(excluded.last_seen, security.last_seen))",
            (isin, first_seen, last_seen, source_doc_hash),
        )

    def set_attribute(
        self, isin: str, attr: str, value: str, valid_from: DateLike,
        *, valid_to: DateLike | None = None, source_doc_hash: str | None = None,
    ) -> None:
        """Record an attribute value effective from a date.

        Setting a *new* value closes the previous open interval at the day
        before, so the history is a partition rather than a pile of overlapping
        claims. Re-asserting the same value is a no-op — sources repeat
        themselves daily and each repeat must not manufacture an interval.
        """
        _validate_isin(isin)
        frm = as_iso(valid_from)
        current = self.conn.execute(
            "SELECT valid_from, value FROM security_attr"
            " WHERE isin=? AND attr=? AND valid_to IS NULL"
            " ORDER BY valid_from DESC LIMIT 1",
            (isin, attr),
        ).fetchone()

        if current is not None:
            if current["value"] == value:
                return
            if current["valid_from"] > frm:
                # Out-of-order arrival: insert as a closed historical interval
                # rather than corrupting the current one.
                self.conn.execute(
                    "INSERT OR REPLACE INTO security_attr"
                    " (isin, attr, value, valid_from, valid_to, source_doc_hash)"
                    " VALUES (?,?,?,?,?,?)",
                    (isin, attr, value, frm,
                     _day_before(current["valid_from"]), source_doc_hash),
                )
                return
            self.conn.execute(
                "UPDATE security_attr SET valid_to=? WHERE isin=? AND attr=? AND valid_from=?",
                (_day_before(frm), isin, attr, current["valid_from"]),
            )

        self.conn.execute(
            "INSERT OR REPLACE INTO security_attr"
            " (isin, attr, value, valid_from, valid_to, source_doc_hash)"
            " VALUES (?,?,?,?,?,?)",
            (isin, attr, value, frm, as_iso(valid_to) if valid_to else None, source_doc_hash),
        )

    def set_listing(
        self, isin: str, *, listing_date: DateLike | None = None,
        delisting_date: DateLike | None = None, delisting_reason: str | None = None,
        exchange: str = "NSE", source_doc_hash: str | None = None,
    ) -> None:
        _validate_isin(isin)
        self.conn.execute(
            "INSERT INTO listing (isin, exchange, listing_date, delisting_date,"
            " delisting_reason, source_doc_hash) VALUES (?,?,?,?,?,?)"
            " ON CONFLICT(isin, exchange) DO UPDATE SET"
            "   listing_date     = COALESCE(excluded.listing_date, listing.listing_date),"
            "   delisting_date   = COALESCE(excluded.delisting_date, listing.delisting_date),"
            "   delisting_reason = COALESCE(excluded.delisting_reason, listing.delisting_reason),"
            "   source_doc_hash  = COALESCE(excluded.source_doc_hash, listing.source_doc_hash)",
            (isin, exchange, as_iso(listing_date) if listing_date else None,
             as_iso(delisting_date) if delisting_date else None,
             delisting_reason, source_doc_hash),
        )

    def add_suspension(self, isin: str, start_date: DateLike,
                       end_date: DateLike | None = None, reason: str | None = None,
                       source_doc_hash: str | None = None) -> None:
        self.conn.execute(
            "INSERT INTO suspension (isin, start_date, end_date, reason, source_doc_hash)"
            " VALUES (?,?,?,?,?)"
            " ON CONFLICT(isin, start_date) DO UPDATE SET"
            "   end_date = COALESCE(excluded.end_date, suspension.end_date)",
            (isin, as_iso(start_date), as_iso(end_date) if end_date else None,
             reason, source_doc_hash),
        )

    def add_succession(
        self, predecessor: str, successor: str | None, event_type: str,
        effective_date: DateLike, *, share_ratio: float | None = None,
        source_doc_hash: str | None = None,
    ) -> None:
        """Record that one ISIN became another (or ceased to exist)."""
        if event_type not in {"merger", "demerger", "scheme", "name_change", "isin_change"}:
            raise ValueError(f"unknown succession event type {event_type!r}")
        self.conn.execute(
            "INSERT OR REPLACE INTO isin_succession"
            " (predecessor_isin, successor_isin, event_type, effective_date,"
            "  share_ratio, source_doc_hash) VALUES (?,?,?,?,?,?)",
            (predecessor, successor, event_type, as_iso(effective_date),
             share_ratio, source_doc_hash),
        )

    def add_surveillance(self, isin: str, list_type: str, stage: int,
                         start_date: DateLike, end_date: DateLike | None = None,
                         source_doc_hash: str | None = None) -> None:
        if list_type not in {"asm", "gsm"}:
            raise ValueError(f"unknown surveillance list {list_type!r}")
        self.conn.execute(
            "INSERT INTO surveillance (isin, list_type, stage, start_date, end_date, source_doc_hash)"
            " VALUES (?,?,?,?,?,?)"
            " ON CONFLICT(isin, list_type, start_date) DO UPDATE SET"
            "   end_date = COALESCE(excluded.end_date, surveillance.end_date),"
            "   stage    = excluded.stage",
            (isin, list_type, int(stage), as_iso(start_date),
             as_iso(end_date) if end_date else None, source_doc_hash),
        )

    # -- point-in-time reads -----------------------------------------------

    def attribute_at(self, isin: str, attr: str, date: DateLike) -> str | None:
        row = self.conn.execute(
            "SELECT value FROM security_attr"
            " WHERE isin=? AND attr=? AND valid_from<=?"
            "   AND (valid_to IS NULL OR valid_to>=?)"
            " ORDER BY valid_from DESC LIMIT 1",
            (isin, attr, as_iso(date), as_iso(date)),
        ).fetchone()
        return row["value"] if row else None

    def symbol_at(self, isin: str, date: DateLike) -> str | None:
        return self.attribute_at(isin, "symbol", date)

    def resolve_symbol(self, symbol: str, date: DateLike) -> str | None:
        """ISIN that carried this symbol on this date.

        The inverse of :meth:`symbol_at`, and the reason the master exists: NSE
        reassigns symbols, so this question has a different answer on different
        dates and any code that assumes otherwise is wrong somewhere it will
        not notice.
        """
        row = self.conn.execute(
            "SELECT isin FROM security_attr"
            " WHERE attr='symbol' AND value=? AND valid_from<=?"
            "   AND (valid_to IS NULL OR valid_to>=?)"
            " ORDER BY valid_from DESC LIMIT 1",
            (symbol, as_iso(date), as_iso(date)),
        ).fetchone()
        return row["isin"] if row else None

    def is_listed_at(self, isin: str, date: DateLike) -> bool:
        """Was this ISIN listed on this date?

        Open on the left (a listing date in the future means not yet listed)
        and closed on the right at the delisting date — a stock trades *on* its
        final day, and dropping that day loses the delisting return, which is
        exactly the observation survivorship bias erases.
        """
        d = as_iso(date)
        row = self.conn.execute(
            "SELECT listing_date, delisting_date FROM listing WHERE isin=?", (isin,)
        ).fetchone()
        if row is None:
            return False
        if row["listing_date"] and row["listing_date"] > d:
            return False
        if row["delisting_date"] and row["delisting_date"] < d:
            return False
        return True

    def is_suspended_at(self, isin: str, date: DateLike) -> bool:
        d = as_iso(date)
        row = self.conn.execute(
            "SELECT 1 FROM suspension WHERE isin=? AND start_date<=?"
            "   AND (end_date IS NULL OR end_date>=?) LIMIT 1",
            (isin, d, d),
        ).fetchone()
        return row is not None

    def surveillance_stage_at(self, isin: str, date: DateLike,
                              list_type: str | None = None) -> int:
        """Highest surveillance stage in force on a date; 0 if none."""
        d = as_iso(date)
        sql = ("SELECT MAX(stage) s FROM surveillance WHERE isin=? AND start_date<=?"
               " AND (end_date IS NULL OR end_date>=?)")
        args: list[Any] = [isin, d, d]
        if list_type:
            sql += " AND list_type=?"
            args.append(list_type)
        row = self.conn.execute(sql, args).fetchone()
        return int(row["s"]) if row and row["s"] is not None else 0

    def get(self, isin: str, date: DateLike) -> SecurityRecord | None:
        row = self.conn.execute("SELECT 1 FROM security WHERE isin=?", (isin,)).fetchone()
        if row is None:
            return None
        listing = self.conn.execute(
            "SELECT listing_date, delisting_date, delisting_reason FROM listing WHERE isin=?",
            (isin,),
        ).fetchone()
        return SecurityRecord(
            isin=isin,
            symbol=self.symbol_at(isin, date),
            name=self.attribute_at(isin, "name", date),
            sector=self.attribute_at(isin, "sector", date),
            listing_date=listing["listing_date"] if listing else None,
            delisting_date=listing["delisting_date"] if listing else None,
            delisting_reason=listing["delisting_reason"] if listing else None,
            is_listed=self.is_listed_at(isin, date),
            is_suspended=self.is_suspended_at(isin, date),
        )

    def listed_on(self, date: DateLike) -> list[str]:
        """Every ISIN listed on a date — including ones since delisted (§3.2).

        This is the survivorship-safe primitive. There is deliberately no
        `currently_listed()` convenience alongside it; if you want today's
        names, ask for today's date.
        """
        d = as_iso(date)
        return [
            r["isin"] for r in self.conn.execute(
                "SELECT isin FROM listing"
                " WHERE (listing_date IS NULL OR listing_date<=?)"
                "   AND (delisting_date IS NULL OR delisting_date>=?)"
                " ORDER BY isin",
                (d, d),
            )
        ]

    def delisted_between(self, start: DateLike, end: DateLike) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT isin, delisting_date, delisting_reason FROM listing"
            " WHERE delisting_date BETWEEN ? AND ? ORDER BY delisting_date",
            (as_iso(start), as_iso(end)),
        ))

    # -- succession --------------------------------------------------------

    def successor_of(self, isin: str, date: DateLike | None = None) -> sqlite3.Row | None:
        sql = "SELECT * FROM isin_succession WHERE predecessor_isin=?"
        args: list[Any] = [isin]
        if date is not None:
            sql += " AND effective_date<=?"
            args.append(as_iso(date))
        sql += " ORDER BY effective_date DESC LIMIT 1"
        return self.conn.execute(sql, args).fetchone()

    def succession_chain(self, isin: str, *, max_hops: int = 10) -> list[dict[str, Any]]:
        """Follow an ISIN forward through mergers/renames to its final identity.

        Returns the hops taken. A terminated chain (liquidation) ends with a
        `successor_isin` of None, which callers must treat as "the return
        series ends here", not as "data missing" — the distinction is the
        difference between a -100% return and a silent survivorship gap.
        """
        chain: list[dict[str, Any]] = []
        seen = {isin}
        current = isin
        for _ in range(max_hops):
            row = self.successor_of(current)
            if row is None:
                break
            hop = dict(row)
            chain.append(hop)
            nxt = row["successor_isin"]
            if nxt is None or nxt in seen:
                break  # terminated, or a cycle in the source data
            seen.add(nxt)
            current = nxt
        return chain

    def terminal_isin(self, isin: str) -> str | None:
        """Final ISIN after following the chain; None if the security terminated."""
        chain = self.succession_chain(isin)
        if not chain:
            return isin
        return chain[-1]["successor_isin"]

    # -- bulk helpers ------------------------------------------------------

    def observe_from_prices(self, frame: pd.DataFrame, source_doc_hash: str | None = None) -> int:
        """Learn the master from a bhavcopy: ISINs, symbols, and trading dates.

        This is how listing windows get established without a separate listing
        feed — first and last date observed trading bound the window, and an
        explicit delisting record from the delisted-securities list refines it.
        """
        written = 0
        for row in frame.itertuples(index=False):
            isin = getattr(row, "isin", None)
            if not isin or not isinstance(isin, str) or not isin.strip():
                continue
            isin = isin.strip()
            if not _looks_like_isin(isin):
                continue
            date = as_iso(pd.Timestamp(row.date).date())
            self.upsert_security(isin, first_seen=date, last_seen=date,
                                 source_doc_hash=source_doc_hash)
            if getattr(row, "symbol", None):
                self.set_attribute(isin, "symbol", str(row.symbol), date,
                                   source_doc_hash=source_doc_hash)
            written += 1
        return written

    def close_listing_windows(self) -> int:
        """Set listing_date/delisting_date from observed trading where unknown.

        Deliberately conservative: it only fills gaps and never overwrites a
        date that came from an actual delisting notice, because "last day we
        saw it trade" and "the day it was delisted" are different facts and
        only the second one is authoritative.
        """
        return self.conn.execute(
            "INSERT INTO listing (isin, exchange, listing_date, delisting_date)"
            " SELECT isin, 'NSE', first_seen, NULL FROM security"
            " WHERE isin NOT IN (SELECT isin FROM listing)"
        ).rowcount


def _day_before(iso_date: str) -> str:
    return (dt.date.fromisoformat(iso_date) - dt.timedelta(days=1)).isoformat()


def _looks_like_isin(value: str) -> bool:
    """Indian ISINs are INE/INF/INA + 9 alphanumerics. Cheap shape check that
    keeps '-', 'nan', and stray header text out of the primary key."""
    return len(value) == 12 and value[:2].isalpha() and value[2:].isalnum()


def _validate_isin(isin: str) -> None:
    if not isinstance(isin, str) or not _looks_like_isin(isin):
        raise ValueError(f"not a valid ISIN: {isin!r}")
