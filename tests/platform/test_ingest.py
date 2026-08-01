"""Archive → store ingest tests (§5, §6).

The property under test is that ingest is a pure function of the archive: the
same bytes always yield the same store, and a rebuild from scratch is a no-op
in terms of results.
"""
from __future__ import annotations

import datetime as dt

import pytest

from src.archive.store import Archive
from src.store.ingest import Ingestor, classify_action, _collapse_intervals
from src.store.schema import connect
from tests.platform.fixtures import BHAVCOPY_LEGACY, BHAVCOPY_SECWISE, zipped


@pytest.fixture
def setup(tmp_path):
    archive = Archive(tmp_path / "archive")
    conn = connect(tmp_path / "db.sqlite")
    yield archive, conn, Ingestor(archive, conn)
    archive.close()
    conn.close()


def _archive_bhavcopy(archive, key: str, content: bytes = BHAVCOPY_LEGACY):
    return archive.put(source="nse.bhavcopy", doc_key=key, url=f"https://x/{key}",
                       content=zipped(content))


# --- bhavcopy ---------------------------------------------------------------

def test_ingest_writes_prices_and_master(setup):
    archive, conn, ing = setup
    _archive_bhavcopy(archive, "2015-01-15")
    report = ing.ingest_bhavcopy()

    assert report.documents == 1
    assert report.rows_written == 2  # RELIANCE + TINYCO; bond and zero-price dropped
    row = conn.execute(
        "SELECT * FROM price_daily WHERE isin='INE002A01018' AND date='2015-01-15'"
    ).fetchone()
    assert row["close"] == pytest.approx(1015.50)
    assert row["symbol"] == "RELIANCE"
    assert conn.execute(
        "SELECT COUNT(*) c FROM security"
    ).fetchone()["c"] == 2


def test_every_row_traces_to_its_source_document(setup):
    archive, conn, ing = setup
    entry = _archive_bhavcopy(archive, "2015-01-15")
    ing.ingest_bhavcopy()
    hashes = {r["source_doc_hash"] for r in conn.execute(
        "SELECT source_doc_hash FROM price_daily")}
    assert hashes == {entry.content_hash}
    assert archive.read(entry.content_hash), "the hash must resolve back to bytes"


def test_ingest_is_idempotent(setup):
    archive, conn, ing = setup
    _archive_bhavcopy(archive, "2015-01-15")
    ing.ingest_bhavcopy()
    before = conn.execute("SELECT COUNT(*) c FROM price_daily").fetchone()["c"]

    second = ing.ingest_bhavcopy()
    assert second.documents == 0, "already-ingested documents are skipped"
    assert conn.execute("SELECT COUNT(*) c FROM price_daily").fetchone()["c"] == before


def test_reingest_forced_produces_identical_rows(setup):
    archive, conn, ing = setup
    _archive_bhavcopy(archive, "2015-01-15")
    ing.ingest_bhavcopy()
    snapshot = conn.execute(
        "SELECT isin, date, close FROM price_daily ORDER BY isin").fetchall()

    ing.ingest_bhavcopy(skip_ingested=False)
    assert [tuple(r) for r in conn.execute(
        "SELECT isin, date, close FROM price_daily ORDER BY isin")] == \
        [tuple(r) for r in snapshot]


def test_symbol_only_layout_resolves_through_the_master(setup):
    """The security-wise file has no ISIN column. Resolving through the master
    as of the trade date is what keeps §3.3 intact."""
    archive, conn, ing = setup
    _archive_bhavcopy(archive, "2015-01-15")          # teaches ISIN <-> symbol
    ing.ingest_bhavcopy()

    archive.put(source="nse.bhavcopy", doc_key="2021-01-15", url="https://x/2",
                content=BHAVCOPY_SECWISE)
    report = ing.ingest_bhavcopy()

    row = conn.execute(
        "SELECT * FROM price_daily WHERE date='2021-01-15' AND isin='INE002A01018'"
    ).fetchone()
    assert row is not None, "RELIANCE should resolve to its ISIN from the master"
    assert row["close"] == pytest.approx(2015.50)  # CLOSE_PRICE, not LAST_PRICE
    assert report.unresolved_symbols == 0


def test_unresolvable_symbols_are_counted_not_guessed(setup):
    """A symbol the master has never seen must be reported, never assigned a
    made-up ISIN or keyed on the symbol itself."""
    archive, conn, ing = setup
    archive.put(source="nse.bhavcopy", doc_key="2021-01-15", url="https://x/2",
                content=BHAVCOPY_SECWISE)
    report = ing.ingest_bhavcopy()
    assert report.unresolved_symbols == 2
    assert conn.execute("SELECT COUNT(*) c FROM price_daily").fetchone()["c"] == 0


def test_unparseable_document_is_recorded_and_does_not_stop_the_run(setup):
    archive, conn, ing = setup
    archive.put(source="nse.bhavcopy", doc_key="2015-01-14", url="https://x/bad",
                content=b"COL_A,COL_B\n1,2\n")
    _archive_bhavcopy(archive, "2015-01-15")

    report = ing.ingest_bhavcopy()
    assert report.documents == 1
    assert len(report.errors) == 1 and report.errors[0][0] == "2015-01-14"
    assert conn.execute("SELECT COUNT(*) c FROM price_daily").fetchone()["c"] == 2
    note = conn.execute(
        "SELECT note FROM ingest_log WHERE doc_key='2015-01-14'").fetchone()["note"]
    assert note, "the failure reason is recorded in the ingest log"


def test_rebuild_from_archive_reproduces_the_store(tmp_path):
    """The reproducibility claim, tested: a fresh database built from the same
    archive must match row for row."""
    archive = Archive(tmp_path / "archive")
    _archive_bhavcopy(archive, "2015-01-15")

    def build(name):
        conn = connect(tmp_path / name)
        Ingestor(archive, conn).ingest_bhavcopy()
        rows = [tuple(r) for r in conn.execute(
            "SELECT isin, date, close, turnover FROM price_daily ORDER BY isin, date")]
        conn.close()
        return rows

    assert build("a.sqlite") == build("b.sqlite")
    archive.close()


# --- delisted ---------------------------------------------------------------

def test_delisted_list_sets_the_delisting_date(setup):
    archive, conn, ing = setup
    archive.put(
        source="nse.delisted", doc_key="delisted", url="https://x/d",
        content=(b"SYMBOL,NAME OF COMPANY,ISIN,DATE OF DELISTING,REASON\n"
                 b"GONECO,Gone Ltd,INE555A01011,15-JUN-2021,Compulsory delisting\n"),
    )
    ing.ingest_delisted()

    row = conn.execute("SELECT * FROM listing WHERE isin='INE555A01011'").fetchone()
    assert row["delisting_date"] == "2021-06-15"
    assert "Compulsory" in row["delisting_reason"]


def test_suspended_list_creates_a_suspension_interval(setup):
    archive, conn, ing = setup
    archive.put(
        source="nse.delisted", doc_key="suspended", url="https://x/s",
        content=(b"SYMBOL,ISIN,SUSPENSION DATE,REASON\n"
                 b"HALTCO,INE556A01012,01-MAR-2022,Non-compliance\n"),
    )
    ing.ingest_delisted()
    row = conn.execute("SELECT * FROM suspension WHERE isin='INE556A01012'").fetchone()
    assert row["start_date"] == "2022-03-01"


# --- corporate actions ------------------------------------------------------

@pytest.mark.parametrize("purpose,expected_type,expected_ratio", [
    ("FACE VALUE SPLIT FROM RS.10/- TO RS.2/-", "split", 5.0),
    ("FACE VALUE SPLIT FROM RS.10/- TO RS.1/-", "split", 10.0),
    ("BONUS 1:1", "bonus", 2.0),
    ("BONUS 1:2", "bonus", 1.5),
    ("INTERIM DIVIDEND - RS 5 PER SHARE", "dividend", None),
    ("SCHEME OF ARRANGEMENT", "merger", None),
    ("DEMERGER", "demerger", None),
    ("RIGHTS 1:4", "rights", None),
    ("ANNUAL GENERAL MEETING", "other", None),
])
def test_corporate_action_classification(purpose, expected_type, expected_ratio):
    action, _, ratio_to, _ = classify_action(purpose)
    assert action == expected_type
    if expected_ratio is not None:
        assert ratio_to == pytest.approx(expected_ratio)


def test_unparseable_ratio_yields_no_ratio_rather_than_a_guess():
    """A wrong split ratio silently multiplies a return series by five. None is
    strictly better than a plausible-looking number."""
    action, ratio_from, ratio_to, _ = classify_action("SPLIT (DETAILS AWAITED)")
    assert action == "split"
    assert ratio_from is None and ratio_to is None


def test_dividend_amount_is_extracted():
    _, _, _, amount = classify_action("INTERIM DIVIDEND RS.12.50 PER SHARE")
    assert amount == pytest.approx(12.50)


def test_corporate_actions_ingest_from_json(setup):
    archive, conn, ing = setup
    archive.put(
        source="nse.corporate_actions", doc_key="2021-01-01_2021-03-31",
        url="https://x/ca",
        content=(b'[{"isin":"INE002A01018","exDate":"10-FEB-2021",'
                 b'"subject":"BONUS 1:1","recDate":"11-FEB-2021"}]'),
    )
    report = ing.ingest_corporate_actions()
    assert report.rows_written == 1
    row = conn.execute("SELECT * FROM corporate_action").fetchone()
    assert row["action_type"] == "bonus"
    assert row["ex_date"] == "2021-02-10"
    assert row["ratio_to"] == pytest.approx(2.0)


# --- index constituents -----------------------------------------------------

def test_index_constituents_are_marked_published(setup):
    archive, conn, ing = setup
    archive.put(
        source="nse.index_constituents", doc_key="nifty500", url="https://x/i",
        content=(b"Company Name,Industry,Symbol,Series,ISIN Code\n"
                 b"Reliance Industries Ltd.,Oil Gas,RELIANCE,EQ,INE002A01018\n"),
    )
    ing.ingest_index_constituents(effective_from="2024-01-01")
    row = conn.execute("SELECT * FROM index_membership").fetchone()
    assert row["index_name"] == "NIFTY 500"
    assert row["method"] == "published", "a reconstruction must be distinguishable"
    assert row["effective_from"] == "2024-01-01"


# --- surveillance interval collapsing ---------------------------------------

def test_consecutive_daily_observations_collapse_to_one_interval():
    obs = [("2021-03-01", 2), ("2021-03-02", 2), ("2021-03-03", 2)]
    assert _collapse_intervals(obs) == [("2021-03-01", "2021-03-03", 2)]


def test_weekend_gaps_do_not_split_an_interval():
    obs = [("2021-03-05", 2), ("2021-03-08", 2)]  # Friday then Monday
    assert _collapse_intervals(obs) == [("2021-03-05", "2021-03-08", 2)]


def test_a_real_gap_splits_the_interval():
    obs = [("2021-03-01", 2), ("2021-03-02", 2), ("2021-04-01", 2)]
    assert _collapse_intervals(obs) == [
        ("2021-03-01", "2021-03-02", 2), ("2021-04-01", "2021-04-01", 2),
    ]


def test_stage_change_splits_the_interval():
    obs = [("2021-03-01", 1), ("2021-03-02", 2)]
    assert _collapse_intervals(obs) == [
        ("2021-03-01", "2021-03-01", 1), ("2021-03-02", "2021-03-02", 2),
    ]
