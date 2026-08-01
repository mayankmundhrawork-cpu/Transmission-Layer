"""Database schema for the derived store (§3, §6, §7).

Everything here is *derived* — rebuildable from the archive by re-running
ingest. Nothing in this database is a source of truth; the archive is.

Two design decisions carry invariants rather than preferences:

**ISIN is the primary key (§3.3).** Symbols change, companies rename, and a
research platform keyed on symbol silently splices two different companies'
return series together at a rename. `symbol` lives in `security_attr` as a
validity-dated attribute, and every other table joins on ISIN.

**The fundamentals table has a deliberately hostile name (§3.1).**
``_fundamental_fact_private`` is not meant to be typed anywhere except
`src/store/bitemporal.py`. The name is the first line of defence, the runtime
guard in `bitemporal.py` is the second, and the static import test in
`tests/platform/test_no_leak.py` is the third. Any one of them alone would be
a suggestion; together they are an invariant.
"""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

#: §3.1 — the only module permitted to name this table is src/store/bitemporal.py
#: (plus src/store/ingest.py, which writes it). Reading it anywhere else is the
#: look-ahead bug this whole platform exists to make impossible.
FUNDAMENTALS_TABLE = "_fundamental_fact_private"

SCHEMA = f"""
PRAGMA journal_mode=WAL;
-- WAL + NORMAL is durable across process crashes (only a host power loss can
-- lose the last commits), and this database is derived — a lost tail is fixed
-- by re-running ingest. FULL would fsync every statement, which turns a
-- million-row price backfill into an hour of disk sync.
PRAGMA synchronous=NORMAL;
PRAGMA foreign_keys=ON;

-- ===== §6 security master =================================================

CREATE TABLE IF NOT EXISTS security (
    isin            TEXT PRIMARY KEY,
    first_seen      TEXT,          -- first date observed in any source
    last_seen       TEXT,          -- last date observed trading
    source_doc_hash TEXT
);

-- Validity-dated attributes. `symbol` lives here, never as an identifier.
CREATE TABLE IF NOT EXISTS security_attr (
    isin            TEXT NOT NULL,
    attr            TEXT NOT NULL,   -- symbol | name | sector | industry | exchange
    value           TEXT NOT NULL,
    valid_from      TEXT NOT NULL,
    valid_to        TEXT,            -- NULL = still current
    source_doc_hash TEXT,
    PRIMARY KEY (isin, attr, valid_from)
);
CREATE INDEX IF NOT EXISTS ix_attr_lookup ON security_attr(attr, value, valid_from);
CREATE INDEX IF NOT EXISTS ix_attr_isin   ON security_attr(isin, attr);

CREATE TABLE IF NOT EXISTS listing (
    isin             TEXT NOT NULL,
    exchange         TEXT NOT NULL DEFAULT 'NSE',
    listing_date     TEXT,
    delisting_date   TEXT,           -- NULL = still listed
    delisting_reason TEXT,
    source_doc_hash  TEXT,
    PRIMARY KEY (isin, exchange)
);
CREATE INDEX IF NOT EXISTS ix_listing_delisting ON listing(delisting_date);

CREATE TABLE IF NOT EXISTS suspension (
    isin            TEXT NOT NULL,
    start_date      TEXT NOT NULL,
    end_date        TEXT,            -- NULL = still suspended
    reason          TEXT,
    source_doc_hash TEXT,
    PRIMARY KEY (isin, start_date)
);

-- §6: the succession chain, so a return series can be followed across a merger
-- or explicitly terminated rather than silently ending.
CREATE TABLE IF NOT EXISTS isin_succession (
    predecessor_isin TEXT NOT NULL,
    successor_isin   TEXT,           -- NULL = terminated (liquidation, no successor)
    event_type       TEXT NOT NULL,  -- merger | demerger | scheme | name_change | isin_change
    effective_date   TEXT NOT NULL,
    share_ratio      REAL,           -- successor shares per predecessor share
    source_doc_hash  TEXT,
    PRIMARY KEY (predecessor_isin, effective_date, event_type)
);

CREATE TABLE IF NOT EXISTS corporate_action (
    isin            TEXT NOT NULL,
    action_type     TEXT NOT NULL,   -- split | bonus | rights | dividend | merger | demerger | name_change
    ex_date         TEXT NOT NULL,
    record_date     TEXT,
    ratio_from      REAL,            -- e.g. split 1:5 -> from=1, to=5
    ratio_to        REAL,
    amount          REAL,            -- dividend per share
    -- NOT NULL DEFAULT '' so it can sit in the primary key: two dividends can
    -- share an ex-date (interim + special) and are distinguished by purpose.
    purpose         TEXT NOT NULL DEFAULT '',
    published_at    TEXT,            -- announcement timestamp: PIT adjustment needs it
    source_doc_hash TEXT,
    PRIMARY KEY (isin, action_type, ex_date, purpose)
);
CREATE INDEX IF NOT EXISTS ix_ca_exdate ON corporate_action(ex_date);

-- §5/§6: index membership with effective dates. `method` records how a row was
-- derived — 'published' for an official list, 'circular' for a reconstruction.
CREATE TABLE IF NOT EXISTS index_membership (
    index_name      TEXT NOT NULL,
    isin            TEXT NOT NULL,
    effective_from  TEXT NOT NULL,
    effective_to    TEXT,
    method          TEXT NOT NULL DEFAULT 'published',
    source_doc_hash TEXT,
    PRIMARY KEY (index_name, isin, effective_from)
);
CREATE INDEX IF NOT EXISTS ix_index_window ON index_membership(index_name, effective_from, effective_to);

-- ASM/GSM stage history. Stage 2+ excludes a name from the universe on the
-- dates it was actually in that stage — a constraint only meaningful PIT.
CREATE TABLE IF NOT EXISTS surveillance (
    isin            TEXT NOT NULL,
    list_type       TEXT NOT NULL,   -- asm | gsm
    stage           INTEGER NOT NULL,
    start_date      TEXT NOT NULL,
    end_date        TEXT,
    source_doc_hash TEXT,
    PRIMARY KEY (isin, list_type, start_date)
);
CREATE INDEX IF NOT EXISTS ix_surv_window ON surveillance(start_date, end_date);

-- ===== §5 prices ==========================================================

CREATE TABLE IF NOT EXISTS price_daily (
    isin        TEXT NOT NULL,
    date        TEXT NOT NULL,
    symbol      TEXT,
    series      TEXT,
    open        REAL, high REAL, low REAL, close REAL, prev_close REAL,
    volume      REAL,
    turnover    REAL,               -- rupees, always
    trades      REAL,
    deliv_qty   REAL,
    source_doc_hash TEXT,
    PRIMARY KEY (isin, date)
);
CREATE INDEX IF NOT EXISTS ix_price_date ON price_daily(date);

CREATE TABLE IF NOT EXISTS shares_outstanding (
    isin            TEXT NOT NULL,
    as_of_date      TEXT NOT NULL,
    total_shares    REAL,
    free_float_pct  REAL,           -- 100 - promoter - locked-in
    published_at    TEXT NOT NULL,  -- PIT: shareholding patterns are filed with a lag
    source_doc_hash TEXT,
    PRIMARY KEY (isin, as_of_date, published_at)
);

CREATE TABLE IF NOT EXISTS benchmark_daily (
    index_name  TEXT NOT NULL,
    date        TEXT NOT NULL,
    close       REAL NOT NULL,
    total_return_close REAL,
    source_doc_hash TEXT,
    PRIMARY KEY (index_name, date)
);

-- ===== §7 bitemporal fundamentals =========================================
-- Read ONLY through src/store/bitemporal.as_of(). See this module's docstring.

CREATE TABLE IF NOT EXISTS {FUNDAMENTALS_TABLE} (
    fact_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    isin            TEXT NOT NULL,
    fact_name       TEXT NOT NULL,
    period_type     TEXT NOT NULL,   -- Q | H | A | TTM
    period_start    TEXT NOT NULL,
    period_end      TEXT NOT NULL,
    value           REAL,
    unit            TEXT NOT NULL DEFAULT 'INR',
    source_doc_hash TEXT NOT NULL,
    published_at    TEXT NOT NULL,   -- the whole point: when this became public
    revision_seq    INTEGER NOT NULL DEFAULT 0,
    defensible      INTEGER NOT NULL DEFAULT 1,
    UNIQUE (isin, fact_name, period_type, period_end, revision_seq)
);
CREATE INDEX IF NOT EXISTS ix_fact_asof ON {FUNDAMENTALS_TABLE}(published_at);
CREATE INDEX IF NOT EXISTS ix_fact_key  ON {FUNDAMENTALS_TABLE}(isin, fact_name, period_end);

-- §7: restatements are new rows, never updates. Enforced, not documented.
CREATE TRIGGER IF NOT EXISTS fundamentals_no_update
    BEFORE UPDATE ON {FUNDAMENTALS_TABLE}
BEGIN SELECT RAISE(ABORT,
    'fundamentals are append-only: a restatement is a new row with a higher revision_seq'); END;

-- ===== §11 multiple-testing registry ======================================
-- Persisted across runs. Every factor-specification pair ever evaluated in
-- this repo counts against the FDR correction, including the ones you would
-- rather forget.

CREATE TABLE IF NOT EXISTS trial_registry (
    trial_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    prereg_hash     TEXT NOT NULL,
    factor_name     TEXT NOT NULL,
    spec_fingerprint TEXT NOT NULL,
    universe_tier   TEXT NOT NULL,
    window_start    TEXT NOT NULL,
    window_end      TEXT NOT NULL,
    horizon_days    INTEGER NOT NULL,
    p_value         REAL,
    sharpe          REAL,
    effective_n     REAL,
    run_at          TEXT NOT NULL,
    UNIQUE (prereg_hash, factor_name, spec_fingerprint, window_start, window_end, horizon_days)
);

CREATE TRIGGER IF NOT EXISTS trial_registry_no_delete
    BEFORE DELETE ON trial_registry
BEGIN SELECT RAISE(ABORT,
    'the trial registry is permanent: deleting trials would understate the multiple-testing burden'); END;

-- ===== ingest provenance ==================================================

CREATE TABLE IF NOT EXISTS ingest_log (
    ingest_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    stage       TEXT NOT NULL,
    doc_hash    TEXT,
    doc_key     TEXT,
    rows_written INTEGER NOT NULL DEFAULT 0,
    ingested_at TEXT NOT NULL,
    note        TEXT
);
"""


@contextmanager
def transaction(conn: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    """Group writes into one commit.

    The connection runs in autocommit (``isolation_level=None``) so that reads
    never sit inside an implicit transaction. That makes every bulk write
    N transactions unless it is wrapped — which is the difference between a
    price backfill taking seconds and taking an hour.
    """
    conn.execute("BEGIN")
    try:
        yield conn
    except Exception:
        conn.execute("ROLLBACK")
        raise
    else:
        conn.execute("COMMIT")


def connect(db_path: Path | str) -> sqlite3.Connection:
    """Open (creating if needed) the derived store."""
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def open_store_db(db_path: Path | str | None = None) -> sqlite3.Connection:
    if db_path is None:
        from src.config import get_config

        db_path = get_config().db_dir / "platform.sqlite"
    return connect(db_path)


def rebuild(db_path: Path | str) -> sqlite3.Connection:
    """Drop and recreate. The derived store is disposable by design — if this
    is destructive in a way that matters, something has been stored here that
    should have been in the archive."""
    path = Path(db_path)
    for suffix in ("", "-wal", "-shm"):
        Path(str(path) + suffix).unlink(missing_ok=True)
    return connect(path)
