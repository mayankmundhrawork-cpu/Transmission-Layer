"""XBRL financial-results filings (§5).

Fundamentals come from filings, indexed on **publication date**. Under SEBI
LODR a company has 45 days after a quarter end to file and 60 after a year
end, and that gap is the look-ahead trap: a factor built from "the quarter
ending 31 March" on 31 March is using a number that was not public for another
six weeks.

The architecture that makes this survivable:

* **The filing index carries the timestamp.** NSE's financial-results endpoint
  returns a `broadCastDate` per filing — when the exchange disseminated it.
  That, not the period end and not the fetch date, is `published_at`.
* **The XBRL document carries the numbers.** It has no reliable dissemination
  timestamp of its own, so it is parsed for facts only.
* **No timestamp, no fact.** A filing whose broadcast date cannot be
  established is rejected. §5 is explicit that it is not guessed, and the
  temptation to fall back on period-end plus a nominal lag is exactly how mass
  near zero shows up in acceptance test 3.

The tag map is data, not code, so extending coverage does not mean editing
parsing logic.
"""
from __future__ import annotations

import datetime as dt
import json
import re
from dataclasses import dataclass, field
from typing import Any, Iterator, Mapping, Sequence

from lxml import etree

from src.archive.fetchers.base import ArchiveFetcher, SkipDocument
from src.archive.fetchers.nse import ARCHIVES, NSE_HOME

#: XBRL element local-name -> canonical fact name. Ind-AS filings use several
#: spellings for the same concept across taxonomy versions; the first match in
#: document order wins, so more specific names are listed first.
FACT_MAP: dict[str, str] = {
    # --- income statement ---
    "RevenueFromOperations": "revenue",
    "Revenue": "revenue",
    "OtherIncome": "other_income",
    "TotalIncome": "total_income",
    "Income": "total_income",
    "TotalExpenses": "total_expenses",
    "Expenses": "total_expenses",
    "CostOfMaterialsConsumed": "cost_of_materials",
    "PurchasesOfStockInTrade": "purchases_stock_in_trade",
    "ChangesInInventoriesOfFinishedGoodsWorkInProgressAndStockInTrade": "inventory_change",
    "EmployeeBenefitExpense": "employee_cost",
    "FinanceCosts": "finance_cost",
    "DepreciationDepletionAndAmortisationExpense": "depreciation",
    "ProfitBeforeExceptionalItemsAndTax": "pbt_before_exceptional",
    "ProfitBeforeTax": "profit_before_tax",
    "TaxExpense": "tax_expense",
    "CurrentTax": "current_tax",
    "ProfitLossForPeriodFromContinuingOperations": "net_profit_continuing",
    "ProfitLossForPeriodAttributableToOwnersOfParent": "net_profit",
    "ProfitLossForPeriod": "net_profit",
    "BasicEarningsLossPerShareFromContinuingAndDiscontinuedOperations": "eps_basic",
    "BasicEarningsLossPerShare": "eps_basic",
    "DilutedEarningsLossPerShare": "eps_diluted",
    # --- balance sheet ---
    "Assets": "total_assets",
    "CurrentAssets": "current_assets",
    "NoncurrentAssets": "noncurrent_assets",
    "PropertyPlantAndEquipment": "ppe",
    "Inventories": "inventories",
    "TradeReceivablesCurrent": "trade_receivables",
    "CashAndCashEquivalents": "cash",
    "Equity": "total_equity",
    "EquityAttributableToOwnersOfParent": "total_equity",
    "EquityShareCapital": "share_capital",
    "OtherEquity": "other_equity",
    "BorrowingsCurrent": "borrowings_current",
    "BorrowingsNoncurrent": "borrowings_noncurrent",
    "CurrentLiabilities": "current_liabilities",
    "NoncurrentLiabilities": "noncurrent_liabilities",
    "Liabilities": "total_liabilities",
    "TradePayablesCurrent": "trade_payables",
    # --- cash flow ---
    "CashFlowsFromUsedInOperatingActivities": "cfo",
    "CashFlowsFromUsedInInvestingActivities": "cfi",
    "CashFlowsFromUsedInFinancingActivities": "cff",
    "PurchaseOfPropertyPlantAndEquipment": "capex",
    # --- India-specific disclosures (§8) ---
    "PercentageOfShareholdingOfPromoterAndPromoterGroup": "promoter_holding_pct",
    "PercentageOfSharesPledgedOfPromoterAndPromoterGroup": "promoter_pledge_pct",
    "NumberOfSharesPledged": "promoter_pledged_shares",
    "TotalNumberOfSharesHeldByPromoterAndPromoterGroup": "promoter_shares",
}

#: Elements naming the entity or the filing's nature rather than a number.
META_TAGS = {
    "ISIN": "isin",
    "Symbol": "symbol",
    "NameOfTheCompany": "company_name",
    "ResultType": "result_type",
    "NatureOfReportStandaloneConsolidated": "result_type",
    "DateOfStartOfReportingPeriod": "period_start",
    "DateOfEndOfReportingPeriod": "period_end",
    "ReportingQuarter": "reporting_quarter",
}

XBRL_INDEX_SOURCE = "nse.results_index"
XBRL_DOC_SOURCE = "nse.xbrl"


class NseResultsIndexFetcher(ArchiveFetcher):
    """The financial-results filing index. `doc_key` is ``"<from>_<to>_<period>"``.

    This document is the one that matters: it is where `broadCastDate` lives.
    """

    source = XBRL_INDEX_SOURCE
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        start, end, period = (doc_key.split("_") + ["Quarterly"])[:3]
        f, t = _ddmmyyyy(start), _ddmmyyyy(end)
        return [
            f"{NSE_HOME}/api/corporates-financial-results?index=equities"
            f"&from_date={f}&to_date={t}&period={period}"
        ]

    def headers_for(self, doc_key: str) -> Mapping[str, str]:
        return {"Accept": "application/json, text/plain, */*",
                "Referer": f"{NSE_HOME}/companies-listing/corporate-filings-financial-results"}

    def validate(self, content: bytes, doc_key: str) -> None:
        super().validate(content, doc_key)
        if content.lstrip()[:1] not in (b"[", b"{"):
            raise SkipDocument(f"{doc_key}: results index is not JSON")


class NseXbrlFetcher(ArchiveFetcher):
    """An individual XBRL filing. `doc_key` is the archive-relative file name."""

    source = XBRL_DOC_SOURCE
    home_url = NSE_HOME

    def urls_for(self, doc_key: str) -> Sequence[str]:
        if doc_key.startswith("http"):
            return [doc_key]
        return [f"{ARCHIVES}/corporate/xbrl/{doc_key}"]

    def validate(self, content: bytes, doc_key: str) -> None:
        super().validate(content, doc_key)
        head = content[:512].lstrip().lower()
        if not head.startswith(b"<?xml") and b"<xbrl" not in head:
            raise SkipDocument(f"{doc_key}: not an XBRL document")


def _ddmmyyyy(iso_date: str) -> str:
    d = dt.date.fromisoformat(iso_date)
    return f"{d.day:02d}-{d.month:02d}-{d.year}"


# ---------------------------------------------------------------------------
# Filing index
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FilingRef:
    """One filing as announced in the index — including when it went public."""

    isin: str | None
    symbol: str | None
    period_start: str | None
    period_end: str | None
    published_at: str
    xbrl_url: str | None
    period_type: str
    result_type: str | None = None

    @property
    def doc_key(self) -> str | None:
        if not self.xbrl_url:
            return None
        return self.xbrl_url.rsplit("/", 1)[-1]


def parse_results_index(content: bytes) -> list[FilingRef]:
    """Extract filing references, dropping any without a broadcast timestamp.

    The drop is deliberate and silent-by-count rather than silent-by-guess:
    callers see how many were rejected via the returned length versus the raw
    record count, and the ledger records the document either way.
    """
    payload = json.loads(content.decode("utf-8", "replace"))
    if isinstance(payload, dict):
        for key in ("data", "records", "resultSet", "rows"):
            if isinstance(payload.get(key), list):
                payload = payload[key]
                break
        else:
            payload = [payload]

    refs: list[FilingRef] = []
    for record in payload:
        if not isinstance(record, dict):
            continue
        published = _first(record, "broadCastDate", "broadcastDate", "bcastDate",
                           "exchdisstime", "creation_Date")
        if not published:
            continue  # §5: no publication timestamp, no fact
        stamp = _parse_timestamp(published)
        if stamp is None:
            continue
        refs.append(FilingRef(
            isin=_first(record, "isin", "ISIN"),
            symbol=_first(record, "symbol", "SYMBOL"),
            period_start=_parse_date(_first(record, "fromDate", "from_date")),
            period_end=_parse_date(_first(record, "toDate", "to_date")),
            published_at=stamp,
            xbrl_url=_first(record, "xbrl", "xbrlFile", "xbrl_attachment"),
            period_type=_period_type(_first(record, "period", "relatingTo", "audited")),
            result_type=_first(record, "consolidated", "resultType"),
        ))
    return refs


def _first(record: Mapping[str, Any], *names: str) -> Any:
    lowered = {str(k).lower(): v for k, v in record.items()}
    for name in names:
        value = lowered.get(name.lower())
        if value not in (None, "", "-", "NA"):
            return value
    return None


def _period_type(raw: Any) -> str:
    text = str(raw or "").strip().lower()
    if "annual" in text or "year" in text:
        return "A"
    if "half" in text:
        return "H"
    return "Q"


def _parse_date(raw: Any) -> str | None:
    if raw is None:
        return None
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return dt.datetime.strptime(str(raw).strip(), fmt).date().isoformat()
        except ValueError:
            continue
    return None


def _parse_timestamp(raw: Any) -> str | None:
    """Parse a broadcast timestamp to an ISO UTC string.

    NSE writes these in IST without a zone marker. Converting explicitly rather
    than storing naive text matters: a 09:00 IST filing is 03:30 UTC the same
    day, and comparing a naive IST stamp against a UTC cutoff shifts every
    publication date by up to a day in the direction that creates look-ahead.
    """
    text = str(raw).strip()
    ist = dt.timezone(dt.timedelta(hours=5, minutes=30))
    for fmt in ("%d-%b-%Y %H:%M:%S", "%d-%b-%Y %H:%M", "%Y-%m-%d %H:%M:%S",
                "%d-%m-%Y %H:%M:%S", "%d-%b-%Y"):
        try:
            stamp = dt.datetime.strptime(text, fmt)
        except ValueError:
            continue
        return stamp.replace(tzinfo=ist).astimezone(dt.timezone.utc).isoformat()
    try:
        stamp = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=ist)
    return stamp.astimezone(dt.timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# XBRL document
# ---------------------------------------------------------------------------

@dataclass
class XbrlFiling:
    """Facts extracted from one XBRL document.

    `published_at` is deliberately absent: it belongs to the index, and joining
    it here is the ingest step's job. Keeping it out of this dataclass means a
    filing cannot accidentally acquire a publication date from its own contents.
    """

    isin: str | None = None
    symbol: str | None = None
    company_name: str | None = None
    result_type: str | None = None
    period_start: str | None = None
    period_end: str | None = None
    period_type: str = "Q"
    facts: dict[str, float] = field(default_factory=dict)
    contexts: dict[str, tuple[str | None, str | None]] = field(default_factory=dict)


def parse_xbrl(content: bytes) -> XbrlFiling:
    """Extract canonical facts from an Ind-AS XBRL instance document."""
    try:
        root = etree.fromstring(content, etree.XMLParser(recover=True, huge_tree=True))
    except etree.XMLSyntaxError as exc:
        raise SkipDocument(f"unparseable XBRL: {exc}") from exc
    if root is None:
        raise SkipDocument("empty XBRL document")

    filing = XbrlFiling()
    filing.contexts = _parse_contexts(root)

    for element in root.iter():
        tag = _localname(element.tag)
        text = (element.text or "").strip()
        if not text:
            continue

        if tag in META_TAGS:
            attr = META_TAGS[tag]
            if getattr(filing, attr, None) in (None, ""):
                if attr in ("period_start", "period_end"):
                    setattr(filing, attr, _parse_date(text))
                else:
                    setattr(filing, attr, text)
            continue

        canonical = FACT_MAP.get(tag)
        if canonical is None or canonical in filing.facts:
            continue  # first occurrence wins; consolidated blocks come first
        value = _to_float(text)
        if value is None:
            continue
        filing.facts[canonical] = value
        # Period from the fact's own context beats a document-level declaration,
        # because a filing carries prior-period comparatives in other contexts.
        window = filing.contexts.get(element.get("contextRef") or "")
        if window and not filing.period_end:
            filing.period_start, filing.period_end = window

    filing.period_type = _infer_period_type(filing)
    if not filing.period_end:
        raise SkipDocument("XBRL document declares no reporting period")
    return filing


def _parse_contexts(root: etree._Element) -> dict[str, tuple[str | None, str | None]]:
    contexts: dict[str, tuple[str | None, str | None]] = {}
    for element in root.iter():
        if _localname(element.tag) != "context":
            continue
        cid = element.get("id")
        if not cid:
            continue
        start = end = None
        for child in element.iter():
            name = _localname(child.tag)
            text = (child.text or "").strip()
            if name == "startDate":
                start = _parse_date(text)
            elif name == "endDate":
                end = _parse_date(text)
            elif name == "instant":
                end = _parse_date(text)
        contexts[cid] = (start, end)
    return contexts


def _infer_period_type(filing: XbrlFiling) -> str:
    if not (filing.period_start and filing.period_end):
        return "Q"
    days = (dt.date.fromisoformat(filing.period_end)
            - dt.date.fromisoformat(filing.period_start)).days
    if days >= 300:
        return "A"
    if days >= 150:
        return "H"
    return "Q"


def _localname(tag: Any) -> str:
    if not isinstance(tag, str):
        return ""
    return tag.rsplit("}", 1)[-1]


def _to_float(text: str) -> float | None:
    cleaned = re.sub(r"[,\s]", "", text)
    if cleaned in ("", "-", "NA", "NIL"):
        return None
    # XBRL writes negatives in parentheses often enough to matter.
    negative = cleaned.startswith("(") and cleaned.endswith(")")
    if negative:
        cleaned = cleaned[1:-1]
    try:
        value = float(cleaned)
    except ValueError:
        return None
    return -value if negative else value
