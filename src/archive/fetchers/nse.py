"""NSE fetchers and parsers (§5).

The bhavcopy is the backbone: it is simultaneously the price series, the
listing record, and the raw material for the point-in-time universe. Getting it
right for the full history matters more than anything else in the data layer.

NSE has published it under three layouts since 2010:

* **Legacy** (to ~2020-07) — `.../historical/EQUITIES/2015/JAN/cm01JAN2015bhav.csv.zip`
* **Security-wise full** (2020→) — `sec_bhavdata_full_01012021.csv`, which adds
  delivery quantity; that is the only free source of the deliverable-volume
  series, and delivery ratio is a real liquidity signal in the smallcap tier.
* **UDiFF** (2024-07→) — `BhavCopy_NSE_CM_0_0_0_20240705_F_0000.csv.zip`, a
  wholly renamed schema covering all segments.

`parse_bhavcopy` normalises all three onto one column set, so nothing
downstream ever branches on which era a date came from.
"""
from __future__ import annotations

import datetime as dt
import io
import zipfile
from typing import Any, Mapping, Sequence

import pandas as pd

from src.archive.fetchers.base import ArchiveFetcher, SkipDocument
from src.archive.http import NotFound

NSE_HOME = "https://www.nseindia.com"
ARCHIVES = "https://nsearchives.nseindia.com"
ARCHIVES_LEGACY = "https://archives.nseindia.com"

MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")

#: Canonical bhavcopy schema. Everything downstream reads these names only.
BHAVCOPY_COLUMNS = [
    "date", "isin", "symbol", "series", "open", "high", "low", "close",
    "last", "prev_close", "volume", "turnover", "trades", "deliv_qty", "deliv_pct",
]

#: Equity series worth keeping. EQ is the rolling-settlement mainline; BE/BZ are
#: trade-to-trade (surveillance) series that are still genuinely investable and
#: must NOT be dropped — excluding them would quietly remove exactly the
#: stressed smallcaps whose behaviour a risk factor is supposed to capture.
EQUITY_SERIES = frozenset({"EQ", "BE", "BZ", "SM", "ST", "IT"})


def _dmy(d: dt.date) -> str:
    return f"{d.day:02d}{d.month:02d}{d.year}"


def _ddMONyyyy(d: dt.date) -> str:
    return f"{d.day:02d}{MONTHS[d.month - 1]}{d.year}"


def _ymd(d: dt.date) -> str:
    return f"{d.year}{d.month:02d}{d.day:02d}"


def _as_date(doc_key: str) -> dt.date:
    return dt.date.fromisoformat(doc_key)


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------

class NseBhavcopyFetcher(ArchiveFetcher):
    """Daily full-segment equity bhavcopy. `doc_key` is an ISO date."""

    source = "nse.bhavcopy"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        d = _as_date(doc_key)
        urls: list[str] = []
        # Newest layout first: most backfills run forward from a recent date,
        # and a 404 costs a full rate-limit interval.
        if d >= dt.date(2024, 1, 1):
            urls.append(
                f"{ARCHIVES}/content/cm/BhavCopy_NSE_CM_0_0_0_{_ymd(d)}_F_0000.csv.zip"
            )
        if d >= dt.date(2020, 1, 1):
            urls.append(f"{ARCHIVES}/products/content/sec_bhavdata_full_{_dmy(d)}.csv")
        urls.append(
            f"{ARCHIVES}/content/historical/EQUITIES/{d.year}/{MONTHS[d.month - 1]}"
            f"/cm{_ddMONyyyy(d)}bhav.csv.zip"
        )
        urls.append(
            f"{ARCHIVES_LEGACY}/content/historical/EQUITIES/{d.year}/{MONTHS[d.month - 1]}"
            f"/cm{_ddMONyyyy(d)}bhav.csv.zip"
        )
        return urls

    def headers_for(self, doc_key: str) -> Mapping[str, str]:
        return {"Referer": f"{NSE_HOME}/all-reports"}

    def validate(self, content: bytes, doc_key: str) -> None:
        super().validate(content, doc_key)
        # A 200 carrying an HTML error page is NSE's favourite failure mode.
        head = content[:512].lstrip().lower()
        if head.startswith(b"<!doctype html") or head.startswith(b"<html"):
            raise SkipDocument(f"{doc_key}: HTML returned instead of a bhavcopy")
        # Parse it now rather than discovering at ingest time that we archived
        # a document we cannot read.
        frame = parse_bhavcopy(content, _as_date(doc_key))
        if frame.empty:
            raise SkipDocument(f"{doc_key}: bhavcopy parsed to zero rows")

    def meta_for(self, doc_key: str, url: str) -> dict[str, Any]:
        return {"trade_date": doc_key, "layout": _layout_of(url)}

    def frame(self, doc_key: str) -> pd.DataFrame | None:
        """Parsed bhavcopy for a date, read from the archive. Never the network."""
        raw = self.cached_bytes(doc_key)
        return None if raw is None else parse_bhavcopy(raw, _as_date(doc_key))


class NseCorporateActionsFetcher(ArchiveFetcher):
    """Corporate actions: splits, bonuses, rights, dividends, mergers, renames.

    `doc_key` is ``"<from>_<to>"`` ISO dates; NSE serves this as a date-ranged
    query rather than a per-day file.
    """

    source = "nse.corporate_actions"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        start, _, end = doc_key.partition("_")
        f = _fmt_ddmmyyyy(start)
        t = _fmt_ddmmyyyy(end)
        return [
            f"{NSE_HOME}/api/corporates-corporateActions?index=equities&from_date={f}&to_date={t}",
            f"{ARCHIVES}/content/equities/corpaction_{f}_{t}.csv",
        ]

    def headers_for(self, doc_key: str) -> Mapping[str, str]:
        return {
            "Accept": "application/json, text/plain, */*",
            "Referer": f"{NSE_HOME}/companies-listing/corporate-filings-actions",
        }


class NseDelistedFetcher(ArchiveFetcher):
    """Delisted and suspended securities — the survivorship-bias antidote (§3.2)."""

    source = "nse.delisted"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        return {
            "delisted": [f"{ARCHIVES}/content/equities/DELISTED_ISIN.csv",
                         f"{NSE_HOME}/api/corporates-delisted"],
            "suspended": [f"{ARCHIVES}/content/equities/SUSPENDED_ISIN.csv",
                          f"{NSE_HOME}/api/corporates-suspended"],
        }.get(doc_key, [])

    def headers_for(self, doc_key: str) -> Mapping[str, str]:
        return {"Referer": f"{NSE_HOME}/market-data/securities-available-for-trading"}


class NseIndexConstituentsFetcher(ArchiveFetcher):
    """Current index constituent lists. `doc_key` is the index slug.

    NSE publishes only the *current* membership. Historical membership is
    reconstructed from index-maintenance circulars — see
    :mod:`src.master.universe`, which records the reconstruction method in the
    archive as §5 requires.
    """

    source = "nse.index_constituents"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        return [f"{ARCHIVES}/content/indices/ind_{doc_key}list.csv"]


class NseIndexCircularFetcher(ArchiveFetcher):
    """Index-maintenance circulars (constituent changes with effective dates)."""

    source = "nse.index_circular"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        return [f"{ARCHIVES}/content/press/{doc_key}"]


class NseAsmGsmFetcher(ArchiveFetcher):
    """ASM/GSM surveillance stage lists. Stage 2+ names are excluded from the
    universe on the date they are in it (§6) — a constraint that is only
    meaningful point-in-time, so the daily snapshot is what we archive."""

    source = "nse.surveillance"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        kind, _, date_s = doc_key.partition("_")
        if kind == "asm":
            return [f"{NSE_HOME}/api/reportASM",
                    f"{ARCHIVES}/content/equities/asm_{_dmy(dt.date.fromisoformat(date_s))}.csv"]
        return [f"{NSE_HOME}/api/reportGSM",
                f"{ARCHIVES}/content/equities/gsm_{_dmy(dt.date.fromisoformat(date_s))}.csv"]

    def headers_for(self, doc_key: str) -> Mapping[str, str]:
        return {"Accept": "application/json, text/plain, */*",
                "Referer": f"{NSE_HOME}/reports/asm-gsm"}


class NseFnoBanFetcher(ArchiveFetcher):
    """F&O ban-list history. `doc_key` is an ISO date."""

    source = "nse.fno_ban"
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        d = _as_date(doc_key)
        return [f"{ARCHIVES}/archives/fo/sec_ban/fo_secban_{_dmy(d)}.csv"]


def _fmt_ddmmyyyy(iso_date: str) -> str:
    d = dt.date.fromisoformat(iso_date)
    return f"{d.day:02d}-{d.month:02d}-{d.year}"


def _layout_of(url: str) -> str:
    if "BhavCopy_NSE_CM" in url:
        return "udiff"
    if "sec_bhavdata_full" in url:
        return "secwise"
    return "legacy"


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _unzip_if_needed(content: bytes) -> bytes:
    if content[:2] != b"PK":
        return content
    with zipfile.ZipFile(io.BytesIO(content)) as zf:
        names = [n for n in zf.namelist() if n.lower().endswith(".csv")]
        if not names:
            raise SkipDocument("zip contains no CSV")
        return zf.read(names[0])


def _num(series: pd.Series) -> pd.Series:
    """Coerce to float. NSE writes '-' for missing and pads numbers with spaces."""
    return pd.to_numeric(
        series.astype(str).str.strip().replace({"-": None, "": None, "nan": None}),
        errors="coerce",
    )


def parse_bhavcopy(content: bytes, trade_date: dt.date | None = None) -> pd.DataFrame:
    """Normalise any NSE bhavcopy layout onto :data:`BHAVCOPY_COLUMNS`.

    Turnover is always rupees. The security-wise layout publishes it in lakhs,
    which is the kind of unit mismatch that produces a liquidity screen that is
    wrong by 10^5 and still looks plausible on a chart — so it is converted
    here, once, rather than trusted to every call site.
    """
    csv_bytes = _unzip_if_needed(content)
    raw = pd.read_csv(io.BytesIO(csv_bytes), dtype=str, skipinitialspace=True)
    raw.columns = [c.strip().upper() for c in raw.columns]

    if "TCKRSYMB" in raw.columns:
        frame = _parse_udiff(raw)
    elif "DELIV_QTY" in raw.columns or "TTL_TRD_QNTY" in raw.columns:
        frame = _parse_secwise(raw)
    elif "TOTTRDQTY" in raw.columns:
        frame = _parse_legacy(raw)
    else:
        raise SkipDocument(f"unrecognised bhavcopy layout, columns={list(raw.columns)[:12]}")

    if trade_date is not None:
        frame["date"] = pd.Timestamp(trade_date)
    frame = frame[frame["series"].isin(EQUITY_SERIES)]
    frame = frame[frame["close"].notna() & (frame["close"] > 0)]
    for col in BHAVCOPY_COLUMNS:
        if col not in frame.columns:
            frame[col] = pd.NA

    # A ragged CSV — one NSE forgot a field on, or a layout revision we have not
    # seen — parses without error and silently shifts every column left. The
    # symptom is a column that should always carry numbers coming out entirely
    # null. Refuse it: a wrong turnover is worse than a missing day, because it
    # survives into the liquidity screen looking like data.
    if not frame.empty:
        for col in ("close", "volume", "turnover"):
            if frame[col].isna().all():
                raise SkipDocument(
                    f"column {col!r} is entirely null after parsing — the source "
                    "layout has probably changed; refusing to archive it as data"
                )

    return frame[BHAVCOPY_COLUMNS].reset_index(drop=True)


def _parse_legacy(raw: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "date": pd.to_datetime(raw.get("TIMESTAMP"), format="%d-%b-%Y", errors="coerce"),
        "isin": raw.get("ISIN", pd.Series(pd.NA, index=raw.index)).astype(str).str.strip(),
        "symbol": raw["SYMBOL"].str.strip(),
        "series": raw["SERIES"].str.strip(),
        "open": _num(raw["OPEN"]), "high": _num(raw["HIGH"]),
        "low": _num(raw["LOW"]), "close": _num(raw["CLOSE"]),
        "last": _num(raw["LAST"]), "prev_close": _num(raw["PREVCLOSE"]),
        "volume": _num(raw["TOTTRDQTY"]), "turnover": _num(raw["TOTTRDVAL"]),
        "trades": _num(raw.get("TOTALTRADES", pd.Series(pd.NA, index=raw.index))),
    })


def _parse_secwise(raw: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "date": pd.to_datetime(raw.get("DATE1"), format="%d-%b-%Y", errors="coerce"),
        "isin": pd.NA,  # this layout omits ISIN; joined on from the master
        "symbol": raw["SYMBOL"].str.strip(),
        "series": raw["SERIES"].str.strip(),
        "open": _num(raw["OPEN_PRICE"]), "high": _num(raw["HIGH_PRICE"]),
        "low": _num(raw["LOW_PRICE"]), "close": _num(raw["CLOSE_PRICE"]),
        "last": _num(raw["LAST_PRICE"]), "prev_close": _num(raw["PREV_CLOSE"]),
        "volume": _num(raw["TTL_TRD_QNTY"]),
        # published in ₹ lakhs, stored in ₹
        "turnover": _num(raw["TURNOVER_LACS"]) * 1e5,
        "trades": _num(raw["NO_OF_TRADES"]),
        "deliv_qty": _num(raw.get("DELIV_QTY", pd.Series(pd.NA, index=raw.index))),
        "deliv_pct": _num(raw.get("DELIV_PER", pd.Series(pd.NA, index=raw.index))),
    })


def _parse_udiff(raw: pd.DataFrame) -> pd.DataFrame:
    # UDiFF covers every segment; keep cash equities only.
    if "FININSTRMTP" in raw.columns:
        raw = raw[raw["FININSTRMTP"].str.strip().str.upper().isin({"STK", "EQ"})]
    if "SGMT" in raw.columns:
        raw = raw[raw["SGMT"].str.strip().str.upper() == "CM"]
    return pd.DataFrame({
        "date": pd.to_datetime(raw.get("TRADDT"), errors="coerce", dayfirst=True),
        "isin": raw.get("ISIN", pd.Series(pd.NA, index=raw.index)).astype(str).str.strip(),
        "symbol": raw["TCKRSYMB"].str.strip(),
        "series": raw["SCTYSRS"].str.strip(),
        "open": _num(raw["OPNPRIC"]), "high": _num(raw["HGHPRIC"]),
        "low": _num(raw["LWPRIC"]), "close": _num(raw["CLSPRIC"]),
        "last": _num(raw["LASTPRIC"]), "prev_close": _num(raw["PRVSCLSGPRIC"]),
        "volume": _num(raw["TTLTRADGVOL"]), "turnover": _num(raw["TTLTRFVAL"]),
        "trades": _num(raw["TTLNBOFTXSEXCTD"]),
    }).reset_index(drop=True)


# ---------------------------------------------------------------------------
# Calendar
# ---------------------------------------------------------------------------

def candidate_trading_days(start: dt.date, end: dt.date) -> list[str]:
    """Weekdays in range, as ISO doc keys.

    Deliberately not a holiday calendar. A hardcoded holiday list is another
    thing that can be wrong; instead we attempt every weekday and let the
    source's 404 tell us it was a holiday, which the ledger records as
    `skipped`. The archive's own record of which dates returned data *is* the
    trading calendar, derived rather than asserted.
    """
    days: list[str] = []
    day = start
    while day <= end:
        if day.weekday() < 5:
            days.append(day.isoformat())
        day += dt.timedelta(days=1)
    return days
