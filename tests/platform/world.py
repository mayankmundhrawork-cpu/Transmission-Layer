"""A synthetic market with the awkward cases already in it.

Real NSE history is not reachable from CI, and a test world made only of
well-behaved names would pass every survivorship and look-ahead test by
accident. So this world is built to contain, deliberately:

* ``DELISTED`` — trades from the start, delisted 2021-06-30. The survivorship
  canary (§18.2). If it is missing from a 2021-01 universe, the platform is
  quietly forward-looking.
* ``RENAMED`` — trades as ``OLDNAME`` until 2020-06-30, ``NEWNAME`` after. The
  §3.3 canary: symbol is an attribute, ISIN is the key.
* ``MERGED`` — delisted 2022-03-31 into ``ACQUIRER`` at 0.7 shares each. The
  succession-chain canary.
* ``ILLIQUID`` — real prices, ~₹40k/day turnover. Must fail the liquidity
  screen without failing anything else.
* ``PENNY`` — trades below the ₹5 floor.
* ``NEWLISTING`` — first trades 2023-01-02, so it fails the 250-session
  history screen for its first year.
* ``SURVEILLED`` — ASM stage 2 for 2021-03-01..2021-05-31 only.

Everything is seeded, so a failure is reproducible.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.master.security import SecurityMaster
from src.store.schema import transaction

START = dt.date(2018, 1, 1)
END = dt.date(2023, 12, 29)

#: name -> (isin, symbol, base price, daily turnover ₹, annual drift, vol)
SPECIALS: dict[str, tuple[str, str, float, float, float, float]] = {
    "DELISTED":   ("INE900A01001", "DELISTCO",  120.0, 8_000_000, -0.10, 0.35),
    "RENAMED":    ("INE901A01002", "OLDNAME",   250.0, 12_000_000, 0.08, 0.28),
    "MERGED":     ("INE902A01003", "MERGECO",   340.0, 15_000_000, 0.12, 0.26),
    "ACQUIRER":   ("INE903A01004", "ACQCO",     480.0, 40_000_000, 0.11, 0.24),
    "ILLIQUID":   ("INE904A01005", "THINCO",     65.0,     40_000, 0.05, 0.45),
    "PENNY":      ("INE905A01006", "PENNYCO",     3.2,  6_000_000, -0.06, 0.18),
    "NEWLISTING": ("INE906A01007", "FRESHCO",   180.0, 20_000_000, 0.15, 0.32),
    "SURVEILLED": ("INE907A01008", "WATCHCO",    95.0,  9_000_000, 0.03, 0.50),
}

DELISTING_DATE = dt.date(2021, 6, 30)
MERGER_DATE = dt.date(2022, 3, 31)
RENAME_DATE = dt.date(2020, 7, 1)
NEWLISTING_DATE = dt.date(2023, 1, 2)
SURVEILLANCE_START = dt.date(2021, 3, 1)
SURVEILLANCE_END = dt.date(2021, 5, 31)


@dataclass
class World:
    conn: sqlite3.Connection
    sessions: list[str]
    isins: list[str]
    ordinary: list[str]  # plain names with no special behaviour

    def isin(self, name: str) -> str:
        return SPECIALS[name][0]


def trading_sessions(start: dt.date = START, end: dt.date = END) -> list[str]:
    return [d.date().isoformat() for d in pd.bdate_range(start, end)]


def _walk(n: int, base: float, drift: float, vol: float, rng: np.random.Generator) -> np.ndarray:
    steps = rng.normal(drift / 252.0, vol / np.sqrt(252.0), n)
    return base * np.exp(np.cumsum(steps))


def build_world(conn: sqlite3.Connection, *, n_ordinary: int = 40, seed: int = 7) -> World:
    """Populate master + price_daily + index membership with the world above."""
    with transaction(conn):
        return _build_world(conn, n_ordinary=n_ordinary, seed=seed)


def _build_world(conn: sqlite3.Connection, *, n_ordinary: int, seed: int) -> World:
    rng = np.random.default_rng(seed)
    master = SecurityMaster(conn)
    sessions = trading_sessions()
    price_rows: list[tuple] = []
    all_isins: list[str] = []

    def emit(isin: str, symbol: str, days: list[str], closes: np.ndarray,
             turnover: float, turnover_jitter: float = 0.35) -> None:
        prev = closes[0]
        for day, close in zip(days, closes):
            hi = close * (1 + abs(rng.normal(0, 0.006)))
            lo = close * (1 - abs(rng.normal(0, 0.006)))
            tv = max(0.0, turnover * (1 + rng.normal(0, turnover_jitter)))
            price_rows.append((
                isin, day, symbol, "EQ", float(prev), float(hi), float(lo),
                float(close), float(prev), tv / max(close, 0.01), tv, 500.0, None,
                "synthetic",
            ))
            prev = close

    # --- ordinary names ---------------------------------------------------
    ordinary: list[str] = []
    for i in range(n_ordinary):
        isin = f"INE{i:03d}A0100{i % 10}"
        symbol = f"STOCK{i:03d}"
        ordinary.append(isin)
        all_isins.append(isin)
        closes = _walk(len(sessions), 50 + 25 * (i % 20), 0.10 + 0.01 * (i % 7),
                       0.22 + 0.01 * (i % 11), rng)
        emit(isin, symbol, sessions, closes, 5_000_000 + 900_000 * (i % 13))
        master.upsert_security(isin, first_seen=sessions[0], last_seen=sessions[-1])
        master.set_attribute(isin, "symbol", symbol, sessions[0])
        master.set_attribute(isin, "sector", f"SECTOR{i % 8}", sessions[0])
        master.set_listing(isin, listing_date=sessions[0])

    # --- specials ---------------------------------------------------------
    for name, (isin, symbol, base, turnover, drift, vol) in SPECIALS.items():
        all_isins.append(isin)
        days = sessions
        if name == "DELISTED":
            days = [d for d in sessions if d <= DELISTING_DATE.isoformat()]
        elif name == "MERGED":
            days = [d for d in sessions if d <= MERGER_DATE.isoformat()]
        elif name == "NEWLISTING":
            days = [d for d in sessions if d >= NEWLISTING_DATE.isoformat()]

        closes = _walk(len(days), base, drift, vol, rng)
        master.upsert_security(isin, first_seen=days[0], last_seen=days[-1])
        master.set_attribute(isin, "sector", "SECTOR0" if name != "ACQUIRER" else "SECTOR1",
                             days[0])

        if name == "RENAMED":
            before = [d for d in days if d < RENAME_DATE.isoformat()]
            after = [d for d in days if d >= RENAME_DATE.isoformat()]
            emit(isin, "OLDNAME", before, closes[:len(before)], turnover)
            emit(isin, "NEWNAME", after, closes[len(before):], turnover)
            master.set_attribute(isin, "symbol", "OLDNAME", days[0])
            master.set_attribute(isin, "symbol", "NEWNAME", RENAME_DATE)
        else:
            emit(isin, symbol, days, closes, turnover)
            master.set_attribute(isin, "symbol", symbol, days[0])

        master.set_listing(isin, listing_date=days[0])

    master.set_listing(SPECIALS["DELISTED"][0], delisting_date=DELISTING_DATE,
                       delisting_reason="delisted by exchange (non-compliance)")
    master.set_listing(SPECIALS["MERGED"][0], delisting_date=MERGER_DATE,
                       delisting_reason="merged into ACQCO")
    master.add_succession(SPECIALS["MERGED"][0], SPECIALS["ACQUIRER"][0], "merger",
                          MERGER_DATE, share_ratio=0.7)
    master.add_surveillance(SPECIALS["SURVEILLED"][0], "asm", 2,
                            SURVEILLANCE_START, SURVEILLANCE_END)

    conn.executemany(
        "INSERT OR REPLACE INTO price_daily (isin, date, symbol, series, open, high,"
        " low, close, prev_close, volume, turnover, trades, deliv_qty, source_doc_hash)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        price_rows,
    )

    # --- index membership -------------------------------------------------
    # Everything is in the index from day one; the delisted and merged names
    # leave on their exit dates, and NEWLISTING joins when it lists.
    for isin in all_isins:
        eff_from, eff_to = sessions[0], None
        if isin == SPECIALS["DELISTED"][0]:
            eff_to = DELISTING_DATE.isoformat()
        elif isin == SPECIALS["MERGED"][0]:
            eff_to = MERGER_DATE.isoformat()
        elif isin == SPECIALS["NEWLISTING"][0]:
            eff_from = NEWLISTING_DATE.isoformat()
        for index_name in ("NIFTY 500", "NIFTY TOTAL MARKET"):
            conn.execute(
                "INSERT OR REPLACE INTO index_membership"
                " (index_name, isin, effective_from, effective_to, method, source_doc_hash)"
                " VALUES (?,?,?,?,'published','synthetic')",
                (index_name, isin, eff_from, eff_to),
            )

    _build_benchmark(conn, sessions, rng)
    return World(conn=conn, sessions=sessions, isins=all_isins, ordinary=ordinary)


def _build_benchmark(conn: sqlite3.Connection, sessions: list[str],
                     rng: np.random.Generator) -> None:
    closes = _walk(len(sessions), 10_000.0, 0.11, 0.16, rng)
    conn.executemany(
        "INSERT OR REPLACE INTO benchmark_daily"
        " (index_name, date, close, total_return_close, source_doc_hash)"
        " VALUES ('NIFTY_500_TRI',?,?,?,'synthetic')",
        [(day, float(c), float(c)) for day, c in zip(sessions, closes)],
    )


def rebalance_dates(freq: str = "quarterly", start: dt.date = dt.date(2019, 3, 29),
                    end: dt.date = dt.date(2023, 12, 29)) -> list[str]:
    """Quarter- or month-end sessions inside the world's price history."""
    rule = "QE" if freq == "quarterly" else "ME"
    stamps = pd.date_range(start, end, freq=rule)
    sessions = set(trading_sessions())
    out = []
    for stamp in stamps:
        day = stamp.date()
        for _ in range(7):  # walk back to the last actual session
            if day.isoformat() in sessions:
                out.append(day.isoformat())
                break
            day -= dt.timedelta(days=1)
    return out


# ---------------------------------------------------------------------------
# Fundamentals (§7/§8) — filed with realistic publication lags
# ---------------------------------------------------------------------------

#: Annual facts and their rough scale relative to revenue.
_ANNUAL_SHAPE = {
    "revenue": 1.0,
    "cost_of_materials": 0.45,
    "purchases_stock_in_trade": 0.08,
    "inventory_change": 0.01,
    "employee_cost": 0.12,
    "finance_cost": 0.04,
    "depreciation": 0.05,
    "profit_before_tax": 0.14,
    "tax_expense": 0.035,
    "net_profit": 0.105,
    "total_assets": 1.6,
    "total_equity": 0.7,
    "borrowings_current": 0.15,
    "borrowings_noncurrent": 0.25,
    "cash": 0.09,
    "cfo": 0.13,
    "capex": 0.07,
    "related_party_value": 0.06,
}


def build_fundamentals(conn: sqlite3.Connection, isins: list[str], *,
                       seed: int = 21, first_fy: int = 2015,
                       last_fy: int = 2023) -> int:
    """Annual and quarterly facts for every ISIN, with LODR-shaped filing lags.

    Annual results are filed 55-75 days after the 31 March year end (the
    statutory limit is 60 for audited annual results; late filers exist).
    Shareholding patterns land 25-45 days after each quarter end. Those lags
    are what acceptance test 3 measures, so they are generated rather than
    assumed.
    """
    from src.store.bitemporal import BitemporalStore, Fact

    rng = np.random.default_rng(seed)
    store = BitemporalStore(conn)
    facts: list[Fact] = []
    shares_rows: list[tuple] = []

    for i, isin in enumerate(isins):
        scale = 5e8 * (1.0 + (i % 17))
        growth = 1.0 + rng.normal(0.11, 0.07)
        margin_drift = rng.normal(1.0, 0.12)
        promoter = float(np.clip(rng.normal(58.0, 12.0), 20.0, 75.0))
        pledge = float(max(0.0, rng.normal(8.0, 14.0)))
        total_shares = float(scale / 40.0)

        for year_index, fy in enumerate(range(first_fy, last_fy + 1)):
            period_start = f"{fy - 1}-04-01"
            period_end = f"{fy}-03-31"
            lag = float(rng.uniform(55, 75))
            published = (pd.Timestamp(period_end) + pd.Timedelta(days=lag)
                         ).tz_localize("UTC").isoformat()
            revenue = scale * (growth ** year_index)

            for name, ratio in _ANNUAL_SHAPE.items():
                noise = 1.0 + rng.normal(0.0, 0.06)
                value = revenue * ratio * noise
                if name in ("profit_before_tax", "net_profit", "tax_expense"):
                    value *= margin_drift
                facts.append(Fact(
                    isin=isin, fact_name=name, period_type="A",
                    period_start=period_start, period_end=period_end,
                    value=float(value), published_at=published,
                    source_doc_hash="synthetic",
                ))

            for name, value in (
                ("auditor_change_flag", float(rng.random() < 0.08)),
                ("auditor_qualification_flag", float(rng.random() < 0.05)),
            ):
                facts.append(Fact(
                    isin=isin, fact_name=name, period_type="A",
                    period_start=period_start, period_end=period_end,
                    value=value, published_at=published,
                    source_doc_hash="synthetic",
                ))

            shares_rows.append((isin, period_end, total_shares,
                                float(100.0 - promoter), published, "synthetic"))

        # Quarterly shareholding disclosures.
        for fy in range(first_fy, last_fy + 1):
            for quarter_end in (f"{fy - 1}-06-30", f"{fy - 1}-09-30",
                                f"{fy - 1}-12-31", f"{fy}-03-31"):
                lag = float(rng.uniform(25, 45))
                published = (pd.Timestamp(quarter_end) + pd.Timedelta(days=lag)
                             ).tz_localize("UTC").isoformat()
                promoter = float(np.clip(promoter + rng.normal(0, 0.4), 15.0, 78.0))
                pledge = float(np.clip(pledge + rng.normal(0, 1.2), 0.0, 95.0))
                for name, value in (("promoter_holding_pct", promoter),
                                    ("promoter_pledge_pct", pledge)):
                    facts.append(Fact(
                        isin=isin, fact_name=name, period_type="Q",
                        period_start=quarter_end, period_end=quarter_end,
                        value=value, published_at=published,
                        source_doc_hash="synthetic",
                    ))

    with transaction(conn):
        for fact in facts:
            store.add_fact(fact)
        conn.executemany(
            "INSERT OR REPLACE INTO shares_outstanding (isin, as_of_date,"
            " total_shares, free_float_pct, published_at, source_doc_hash)"
            " VALUES (?,?,?,?,?,?)", shares_rows)
    return len(facts)
