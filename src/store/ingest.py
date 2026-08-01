"""Archive → derived store (§5, §6, §7).

Ingest is a pure function of the archive. Delete the database, re-run, and you
get the same store back; that property is what makes "reproducible from a git
commit plus an archive snapshot" true rather than aspirational.

Every write records the source document hash, so any row in the store can be
traced to the bytes it came from.

One wrinkle worth naming: the security-wise bhavcopy layout (2020→) omits ISIN
and publishes only symbols. Rather than key those rows on symbol — which would
break §3.3 — ingest resolves symbol to ISIN *through the master as of that
trade date*. Rows whose symbol cannot be resolved on that date are counted and
reported, never guessed.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass, field
from typing import Any, Iterable

import pandas as pd

from src.archive.fetchers.nse import parse_bhavcopy
from src.archive.store import Archive, ArchiveEntry, utc_now
from src.master.security import SecurityMaster, as_iso
from src.store.schema import FUNDAMENTALS_TABLE as _FUNDAMENTALS_TABLE, transaction


@dataclass
class IngestReport:
    stage: str
    documents: int = 0
    rows_written: int = 0
    securities_seen: int = 0
    unresolved_symbols: int = 0
    errors: list[tuple[str, str]] = field(default_factory=list)

    def __str__(self) -> str:
        out = (f"{self.stage}: {self.documents} documents, {self.rows_written} rows, "
               f"{self.securities_seen} securities")
        if self.unresolved_symbols:
            out += f", {self.unresolved_symbols} unresolved symbols"
        if self.errors:
            out += f", {len(self.errors)} errors"
        return out


class Ingestor:
    def __init__(self, archive: Archive, conn: sqlite3.Connection) -> None:
        self.archive = archive
        self.conn = conn
        self.master = SecurityMaster(conn)

    # -- provenance --------------------------------------------------------

    def _log(self, stage: str, doc_hash: str | None, doc_key: str | None,
             rows: int, note: str | None = None) -> None:
        self.conn.execute(
            "INSERT INTO ingest_log (stage, doc_hash, doc_key, rows_written, ingested_at, note)"
            " VALUES (?,?,?,?,?,?)",
            (stage, doc_hash, doc_key, rows, utc_now().isoformat(), note),
        )

    def ingested_keys(self, stage: str) -> set[str]:
        return {
            r["doc_key"] for r in self.conn.execute(
                "SELECT DISTINCT doc_key FROM ingest_log WHERE stage=? AND doc_key IS NOT NULL",
                (stage,),
            )
        }

    # -- bhavcopy ----------------------------------------------------------

    def ingest_bhavcopy(self, *, doc_keys: Iterable[str] | None = None,
                        skip_ingested: bool = True) -> IngestReport:
        """Load archived bhavcopies into price_daily and the security master."""
        report = IngestReport(stage="bhavcopy")
        keys = list(doc_keys) if doc_keys is not None else self.archive.doc_keys("nse.bhavcopy")
        if skip_ingested:
            done = self.ingested_keys("bhavcopy")
            keys = [k for k in keys if k not in done]

        for key in sorted(keys):
            entry = self.archive.latest_entry("nse.bhavcopy", key)
            if entry is None:
                continue
            try:
                frame = parse_bhavcopy(
                    self.archive.read_entry(entry), dt.date.fromisoformat(key)
                )
            except Exception as exc:  # a bad document must not stop the backfill
                report.errors.append((key, f"{type(exc).__name__}: {exc}"))
                self._log("bhavcopy", entry.content_hash, key, 0, note=str(exc))
                continue

            # One transaction per document: a full backfill is thousands of
            # documents, and one transaction for all of them would hold a write
            # lock for the entire run while losing everything on any failure.
            with transaction(self.conn):
                rows, unresolved = self._write_bhavcopy_frame(frame, key, entry)
                self._log("bhavcopy", entry.content_hash, key, rows)
            report.documents += 1
            report.rows_written += rows
            report.unresolved_symbols += unresolved

        report.securities_seen = self.conn.execute(
            "SELECT COUNT(*) c FROM security"
        ).fetchone()["c"]
        return report

    def _write_bhavcopy_frame(
        self, frame: pd.DataFrame, doc_key: str, entry: ArchiveEntry
    ) -> tuple[int, int]:
        date = doc_key
        has_isin = frame["isin"].notna() & (frame["isin"].astype(str).str.len() == 12)

        # Rows that carry an ISIN teach the master; rows that don't are resolved
        # against what the master already knows for that date.
        known = frame[has_isin].copy()
        if not known.empty:
            self.master.observe_from_prices(known, source_doc_hash=entry.content_hash)

        unknown = frame[~has_isin].copy()
        unresolved = 0
        if not unknown.empty:
            resolved = []
            for sym in unknown["symbol"]:
                isin = self.master.resolve_symbol(str(sym), date)
                resolved.append(isin)
                if isin is None:
                    unresolved += 1
            unknown["isin"] = resolved
            unknown = unknown[unknown["isin"].notna()]

        combined = pd.concat([known, unknown], ignore_index=True)
        if combined.empty:
            return 0, unresolved

        payload = [
            (
                str(r.isin), date, str(r.symbol), str(r.series),
                _f(r.open), _f(r.high), _f(r.low), _f(r.close), _f(r.prev_close),
                _f(r.volume), _f(r.turnover), _f(r.trades), _f(r.deliv_qty),
                entry.content_hash,
            )
            for r in combined.itertuples(index=False)
        ]
        self.conn.executemany(
            "INSERT INTO price_daily (isin, date, symbol, series, open, high, low,"
            " close, prev_close, volume, turnover, trades, deliv_qty, source_doc_hash)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            " ON CONFLICT(isin, date) DO UPDATE SET"
            "   close=excluded.close, open=excluded.open, high=excluded.high,"
            "   low=excluded.low, prev_close=excluded.prev_close,"
            "   volume=excluded.volume, turnover=excluded.turnover,"
            "   trades=excluded.trades, deliv_qty=excluded.deliv_qty,"
            "   source_doc_hash=excluded.source_doc_hash",
            payload,
        )
        # Keep last_seen current so listing windows can be inferred later.
        self.conn.execute(
            "UPDATE security SET last_seen=? WHERE last_seen IS NULL OR last_seen<?",
            (date, date),
        )
        return len(payload), unresolved

    # -- delisted / suspended ---------------------------------------------

    def ingest_delisted(self) -> IngestReport:
        """Load the delisted and suspended security lists (§3.2)."""
        report = IngestReport(stage="delisted")
        for doc_key in ("delisted", "suspended"):
            entry = self.archive.latest_entry("nse.delisted", doc_key)
            if entry is None:
                continue
            try:
                frame = _read_tabular(self.archive.read_entry(entry))
            except Exception as exc:
                report.errors.append((doc_key, str(exc)))
                continue

            rows = 0
            for record in frame.to_dict("records"):
                isin = _pick(record, "ISIN", "ISIN NUMBER", "ISIN_NUMBER")
                if not isin or len(str(isin).strip()) != 12:
                    continue
                isin = str(isin).strip()
                date = _pick_date(record, "DATE OF DELISTING", "DELISTING DATE",
                                  "DATE", "EFFECTIVE DATE", "SUSPENSION DATE")
                reason = _pick(record, "REASON", "REASON FOR DELISTING", "PURPOSE") or doc_key
                symbol = _pick(record, "SYMBOL", "SECURITY SYMBOL")
                name = _pick(record, "NAME OF COMPANY", "COMPANY NAME", "SECURITY NAME")

                self.master.upsert_security(isin, source_doc_hash=entry.content_hash)
                if symbol and date:
                    self.master.set_attribute(isin, "symbol", str(symbol).strip(), date,
                                              source_doc_hash=entry.content_hash)
                if name and date:
                    self.master.set_attribute(isin, "name", str(name).strip(), date,
                                              source_doc_hash=entry.content_hash)
                if doc_key == "delisted" and date:
                    self.master.set_listing(isin, delisting_date=date,
                                            delisting_reason=str(reason),
                                            source_doc_hash=entry.content_hash)
                elif date:
                    self.master.add_suspension(isin, date, reason=str(reason),
                                               source_doc_hash=entry.content_hash)
                rows += 1

            report.documents += 1
            report.rows_written += rows
            self._log("delisted", entry.content_hash, doc_key, rows)
        return report

    # -- corporate actions -------------------------------------------------

    def ingest_corporate_actions(self) -> IngestReport:
        """Load corporate actions, including the ones that change identity."""
        report = IngestReport(stage="corp_actions")
        for entry, raw in self.archive.iter_documents("nse.corporate_actions"):
            try:
                frame = _read_tabular(raw)
            except Exception as exc:
                report.errors.append((entry.doc_key, str(exc)))
                continue

            rows = 0
            for record in frame.to_dict("records"):
                isin = _pick(record, "ISIN", "isin")
                ex_date = _pick_date(record, "EX-DATE", "EX DATE", "exDate", "ExDate")
                purpose = str(_pick(record, "PURPOSE", "subject", "SUBJECT") or "")
                if not isin or not ex_date or len(str(isin).strip()) != 12:
                    continue
                isin = str(isin).strip()
                action, ratio_from, ratio_to, amount = classify_action(purpose)
                self.master.upsert_security(isin, source_doc_hash=entry.content_hash)
                self.conn.execute(
                    "INSERT OR REPLACE INTO corporate_action"
                    " (isin, action_type, ex_date, record_date, ratio_from, ratio_to,"
                    "  amount, purpose, published_at, source_doc_hash)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (isin, action, ex_date,
                     _pick_date(record, "RECORD DATE", "recDate"),
                     ratio_from, ratio_to, amount, purpose,
                     _pick_date(record, "BC_START_DATE", "announcementDate") or ex_date,
                     entry.content_hash),
                )
                rows += 1
            report.documents += 1
            report.rows_written += rows
            self._log("corp_actions", entry.content_hash, entry.doc_key, rows)
        return report

    # -- index membership --------------------------------------------------

    def ingest_index_constituents(self, index_names: dict[str, str] | None = None,
                                  effective_from: str | None = None) -> IngestReport:
        """Load *current* index constituent lists.

        These give membership as of the fetch date only. Historical membership
        comes from circular reconstruction (§5) and is written with
        ``method='circular'`` so a study can tell reconstructed rows from
        published ones — and so acceptance test 4 can check them.
        """
        report = IngestReport(stage="index_constituents")
        slug_to_name = index_names or {
            "nifty500": "NIFTY 500",
            "niftysmallcap250": "NIFTY SMALLCAP 250",
            "niftymidcap150": "NIFTY MIDCAP 150",
            "nifty50": "NIFTY 50",
            "niftytotalmarket": "NIFTY TOTAL MARKET",
        }
        for entry, raw in self.archive.iter_documents("nse.index_constituents"):
            index_name = slug_to_name.get(entry.doc_key)
            if index_name is None:
                continue
            try:
                frame = _read_tabular(raw)
            except Exception as exc:
                report.errors.append((entry.doc_key, str(exc)))
                continue

            eff = effective_from or entry.fetched_at.date().isoformat()
            rows = 0
            for record in frame.to_dict("records"):
                isin = _pick(record, "ISIN Code", "ISIN", "isin")
                if not isin or len(str(isin).strip()) != 12:
                    continue
                self.conn.execute(
                    "INSERT OR REPLACE INTO index_membership"
                    " (index_name, isin, effective_from, effective_to, method, source_doc_hash)"
                    " VALUES (?,?,?,NULL,'published',?)",
                    (index_name, str(isin).strip(), eff, entry.content_hash),
                )
                rows += 1
            report.documents += 1
            report.rows_written += rows
            self._log("index_constituents", entry.content_hash, entry.doc_key, rows)
        return report

    # -- fundamentals (§7) -------------------------------------------------

    def ingest_fundamentals(self, *, skip_ingested: bool = True) -> IngestReport:
        """Join XBRL documents to their broadcast timestamps and store facts.

        The join is the point. An XBRL document on its own has numbers but no
        credible publication time; the results index has the broadcast time but
        no numbers. A document with no matching index entry is *rejected* —
        §5 — because the alternative is inventing a publication date, and an
        invented date is indistinguishable from look-ahead in the output.
        """
        from src.archive.fetchers.xbrl import (
            XBRL_DOC_SOURCE, XBRL_INDEX_SOURCE, parse_results_index, parse_xbrl,
        )
        from src.store.bitemporal import BitemporalStore, Fact, FactRejected

        report = IngestReport(stage="fundamentals")
        store = BitemporalStore(self.conn)

        # 1. Build the publication-timestamp index from every archived index doc.
        refs: dict[str, Any] = {}
        for entry, raw in self.archive.iter_documents(XBRL_INDEX_SOURCE):
            try:
                for ref in parse_results_index(raw):
                    if ref.doc_key:
                        # Earliest broadcast wins: a filing re-announced later
                        # was still public from its first dissemination.
                        prior = refs.get(ref.doc_key)
                        if prior is None or ref.published_at < prior.published_at:
                            refs[ref.doc_key] = ref
            except Exception as exc:
                report.errors.append((entry.doc_key, str(exc)))

        done = self.ingested_keys("fundamentals") if skip_ingested else set()

        # 2. Walk the XBRL documents **in publication order**.
        # revision_seq is assigned by arrival, so processing in filename order
        # would give a restatement a lower revision than the original whenever
        # the restatement's file happened to sort first — and as_of() resolves
        # by highest revision_seq, so the store would then serve the superseded
        # figure forever. Publication order is the only correct order here.
        def _pub_order(key: str) -> tuple[str, str]:
            ref = refs.get(key)
            return (ref.published_at if ref else "9999", key)

        for doc_key in sorted(self.archive.doc_keys(XBRL_DOC_SOURCE), key=_pub_order):
            if doc_key in done:
                continue
            entry = self.archive.latest_entry(XBRL_DOC_SOURCE, doc_key)
            if entry is None:
                continue

            ref = refs.get(doc_key)
            if ref is None:
                report.errors.append((doc_key, "no publication timestamp in any index"))
                self._log("fundamentals", entry.content_hash, doc_key, 0,
                          note="rejected: no broadcast timestamp")
                continue

            try:
                filing = parse_xbrl(self.archive.read_entry(entry))
            except Exception as exc:
                report.errors.append((doc_key, f"{type(exc).__name__}: {exc}"))
                self._log("fundamentals", entry.content_hash, doc_key, 0, note=str(exc))
                continue

            isin = _clean_isin(filing.isin) or _clean_isin(ref.isin)
            if not isin and (filing.symbol or ref.symbol):
                isin = self.master.resolve_symbol(
                    str(filing.symbol or ref.symbol).strip(),
                    filing.period_end or ref.period_end or "9999-12-31",
                )
            if not isin:
                report.unresolved_symbols += 1
                self._log("fundamentals", entry.content_hash, doc_key, 0,
                          note="unresolved ISIN")
                continue

            period_end = filing.period_end or ref.period_end
            period_start = filing.period_start or ref.period_start or period_end
            rows = 0
            with transaction(self.conn):
                for fact_name, value in filing.facts.items():
                    try:
                        store.add_fact(Fact(
                            isin=isin, fact_name=fact_name,
                            period_type=filing.period_type,
                            period_start=period_start, period_end=period_end,
                            value=value, published_at=ref.published_at,
                            source_doc_hash=entry.content_hash,
                            revision_seq=self._revision_for(
                                isin, fact_name, period_end, entry.content_hash,
                                ref.published_at, store,
                            ),
                            defensible=True,
                        ))
                        rows += 1
                    except FactRejected as exc:
                        report.errors.append((doc_key, str(exc)))
                self._log("fundamentals", entry.content_hash, doc_key, rows)
            report.documents += 1
            report.rows_written += rows

        return report

    def _revision_for(self, isin: str, fact_name: str, period_end: str,
                      doc_hash: str, published_at: str, store: Any) -> int:
        """Revision number for an incoming fact.

        Re-ingesting the same document must not manufacture a restatement, so a
        fact already present with this document hash and timestamp keeps its
        revision. Anything genuinely new gets the next sequence number.
        """
        existing = self.conn.execute(
            f"SELECT revision_seq FROM {_FUNDAMENTALS_TABLE}"
            " WHERE isin=? AND fact_name=? AND period_end=?"
            "   AND source_doc_hash=? AND published_at=?",
            (isin, fact_name, period_end, doc_hash, published_at),
        ).fetchone()
        if existing is not None:
            return int(existing["revision_seq"])
        return store.next_revision(isin, fact_name, period_end)

    def ingest_screener_prototype(self, doc_source: str = "screener.fundamentals") -> IngestReport:
        """Ingest screener.in facts as NON-DEFENSIBLE (§5).

        Prototyping only. Every fact lands with `defensible=0`, and any study
        that touches one prints a prominent warning in its report. The flag is
        set here, at the boundary, so there is no path by which a screener fact
        can enter the store looking like a filing-sourced one.
        """
        from src.store.bitemporal import BitemporalStore, Fact, FactRejected

        report = IngestReport(stage="screener")
        store = BitemporalStore(self.conn)
        for entry, raw in self.archive.iter_documents(doc_source):
            try:
                frame = _read_tabular(raw)
            except Exception as exc:
                report.errors.append((entry.doc_key, str(exc)))
                continue
            rows = 0
            with transaction(self.conn):
                for record in frame.to_dict("records"):
                    isin = _clean_isin(_pick(record, "isin", "ISIN"))
                    period_end = _pick_date(record, "period_end", "period", "date")
                    published = _pick_date(record, "published_at", "filing_date")
                    if not isin or not period_end or not published:
                        continue
                    for key, value in record.items():
                        name = str(key).strip().lower()
                        if name in ("isin", "period_end", "period", "date",
                                    "published_at", "filing_date"):
                            continue
                        number = _f(value)
                        if number is None:
                            continue
                        try:
                            store.add_fact(Fact(
                                isin=isin, fact_name=name, period_type="A",
                                period_start=period_end, period_end=period_end,
                                value=number, published_at=f"{published}T00:00:00+00:00",
                                source_doc_hash=entry.content_hash,
                                revision_seq=store.next_revision(isin, name, period_end),
                                defensible=False,
                            ))
                            rows += 1
                        except FactRejected:
                            continue
                self._log("screener", entry.content_hash, entry.doc_key, rows,
                          note="NON-DEFENSIBLE: prototyping source")
            report.documents += 1
            report.rows_written += rows
        return report

    # -- surveillance ------------------------------------------------------

    def ingest_surveillance(self) -> IngestReport:
        """Collapse daily ASM/GSM snapshots into stage intervals.

        Snapshots are daily but membership is sticky, so storing one row per
        name per day would be ~99% redundant. Consecutive days at the same
        stage become one interval; a gap closes it.
        """
        report = IngestReport(stage="surveillance")
        observations: dict[tuple[str, str], list[tuple[str, int]]] = {}

        for entry, raw in self.archive.iter_documents("nse.surveillance"):
            list_type, _, date = entry.doc_key.partition("_")
            try:
                frame = _read_tabular(raw)
            except Exception:
                continue
            for record in frame.to_dict("records"):
                symbol = _pick(record, "symbol", "SYMBOL", "Symbol")
                if not symbol:
                    continue
                isin = self.master.resolve_symbol(str(symbol).strip(), date)
                if not isin:
                    report.unresolved_symbols += 1
                    continue
                stage = _stage_of(record)
                observations.setdefault((isin, list_type), []).append((date, stage))
            report.documents += 1

        rows = 0
        for (isin, list_type), obs in observations.items():
            for start, end, stage in _collapse_intervals(sorted(obs)):
                self.master.add_surveillance(isin, list_type, stage, start, end)
                rows += 1
        report.rows_written = rows
        self._log("surveillance", None, None, rows)
        return report


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _clean_isin(value: Any) -> str | None:
    """Normalise an ISIN, returning None for anything that is not one."""
    if value is None:
        return None
    text = str(value).strip().upper()
    return text if len(text) == 12 and text[:2].isalpha() and text[2:].isalnum() else None


def _f(value: Any) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(out) else out


def _read_tabular(raw: bytes) -> pd.DataFrame:
    """Read CSV or JSON — NSE serves the same logical table as either."""
    import io
    import json

    head = raw[:64].lstrip()
    if head[:1] in (b"{", b"["):
        payload = json.loads(raw.decode("utf-8", "replace"))
        if isinstance(payload, dict):
            for key in ("data", "records", "rows", "result"):
                if isinstance(payload.get(key), list):
                    payload = payload[key]
                    break
            else:
                payload = [payload]
        return pd.DataFrame(payload)
    return pd.read_csv(io.BytesIO(raw), dtype=str, skipinitialspace=True)


def _pick(record: dict[str, Any], *names: str) -> Any:
    """First non-empty value among candidate column names, case-insensitively."""
    lowered = {str(k).strip().lower(): v for k, v in record.items()}
    for name in names:
        value = lowered.get(name.strip().lower())
        if value is not None and str(value).strip() not in ("", "nan", "-"):
            return value
    return None


def _pick_date(record: dict[str, Any], *names: str) -> str | None:
    value = _pick(record, *names)
    if value is None:
        return None
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d %b %Y"):
        try:
            return dt.datetime.strptime(str(value).strip(), fmt).date().isoformat()
        except ValueError:
            continue
    try:
        return pd.Timestamp(str(value)).date().isoformat()
    except Exception:
        return None


def classify_action(purpose: str) -> tuple[str, float | None, float | None, float | None]:
    """Map an NSE corporate-action purpose string to a typed action.

    NSE writes these as free text ("FACE VALUE SPLIT FROM RS.10/- TO RS.2/-",
    "BONUS 1:1"), so this is pattern matching against a messy field. Anything
    unrecognised comes back as ``other`` with no ratio rather than a guess — a
    wrong split ratio silently multiplies a return series by 5.
    """
    import re

    text = (purpose or "").upper()

    if "SPLIT" in text or "SUB-DIVISION" in text or "SUBDIVISION" in text:
        m = re.search(r"RS?\.?\s*([\d.]+)\s*/?-?\s*TO\s*RS?\.?\s*([\d.]+)", text)
        if m:
            old, new = float(m.group(1)), float(m.group(2))
            if new > 0:
                # Face value 10 -> 2 means each share becomes 5.
                return "split", 1.0, old / new, None
        return "split", None, None, None

    if "BONUS" in text:
        m = re.search(r"(\d+)\s*[:/]\s*(\d+)", text)
        if m:
            new, held = float(m.group(1)), float(m.group(2))
            if held > 0:
                # Bonus a:b -> holder ends with (b+a)/b shares per b held.
                return "bonus", 1.0, (held + new) / held, None
        return "bonus", None, None, None

    if "RIGHT" in text:
        return "rights", None, None, None

    if "DIVIDEND" in text:
        m = re.search(r"(?:RS\.?|INR)\s*([\d.]+)", text)
        return "dividend", None, None, float(m.group(1)) if m else None

    # Order matters: "DEMERGER" contains "MERGER". Checking merger first
    # classifies every demerger as a merger, which points the succession chain
    # the wrong way — the predecessor survives a demerger and does not survive
    # a merger.
    if "DEMERGER" in text or "SPIN" in text:
        return "demerger", None, None, None
    if "AMALGAMAT" in text or "MERGER" in text or "SCHEME OF ARRANGEMENT" in text:
        return "merger", None, None, None
    if "NAME CHANGE" in text or "CHANGE IN NAME" in text or "SYMBOL CHANGE" in text:
        return "name_change", None, None, None

    return "other", None, None, None


def _stage_of(record: dict[str, Any]) -> int:
    value = _pick(record, "stage", "asmStage", "gsmStage", "STAGE", "Stage")
    if value is None:
        return 1  # on the list at all is stage 1 unless stated otherwise
    import re

    m = re.search(r"(\d+)", str(value))
    return int(m.group(1)) if m else 1


def _collapse_intervals(observations: list[tuple[str, int]]) -> list[tuple[str, str | None, int]]:
    """Consecutive daily observations at one stage become one interval.

    "Consecutive" allows a weekend-sized gap; a longer break, or a stage
    change, closes the interval.
    """
    out: list[tuple[str, str | None, int]] = []
    if not observations:
        return out
    start, stage = observations[0]
    prev = start
    for date, this_stage in observations[1:]:
        gap = (dt.date.fromisoformat(date) - dt.date.fromisoformat(prev)).days
        if this_stage != stage or gap > 4:
            out.append((start, prev, stage))
            start, stage = date, this_stage
        prev = date
    out.append((start, prev, stage))
    return out
