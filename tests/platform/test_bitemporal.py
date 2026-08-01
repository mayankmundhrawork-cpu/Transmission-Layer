"""Bitemporal store tests (§3.1, §7) — including §18 acceptance tests 1 and 3.

CP4 is the checkpoint the spec calls the most important in the build, and
these are its gate. The failure being defended against does not look like a
failure: a look-ahead pipeline produces a plausible backtest with good numbers,
and nothing in the output says the numbers were not available at the time.
"""
from __future__ import annotations

import datetime as dt

import pandas as pd
import pytest

from src.archive.store import Archive
from src.store.bitemporal import (
    BitemporalStore, Fact, FactRejected, LookAheadViolation,
)
from src.store.ingest import Ingestor
from src.store.schema import FUNDAMENTALS_TABLE, connect
from tests.platform.fixtures import make_results_index, make_xbrl

ISIN = "INE002A01018"


@pytest.fixture
def store(tmp_path):
    conn = connect(tmp_path / "db.sqlite")
    yield BitemporalStore(conn)
    conn.close()


def fact(**kw) -> Fact:
    base = dict(
        isin=ISIN, fact_name="net_profit", period_type="A",
        period_start="2020-04-01", period_end="2021-03-31", value=1000.0,
        published_at="2021-05-30T13:15:00+00:00", source_doc_hash="doc-1",
    )
    base.update(kw)
    return Fact(**base)


# ===========================================================================
# §18 ACCEPTANCE TEST 1 — look-ahead canary (restatement)
# ===========================================================================

@pytest.fixture
def restatement_world(tmp_path):
    """A company that files FY21 results, then restates them 14 months later.

    Built through the real ingest path — archive bytes in, facts out — so the
    test covers the join between the filing index (which carries the broadcast
    timestamp) and the XBRL document (which carries the numbers).
    """
    archive = Archive(tmp_path / "archive")
    conn = connect(tmp_path / "db.sqlite")

    archive.put(
        source="nse.results_index", doc_key="2021_2022", url="https://x/idx",
        content=make_results_index([
            {"from": "01-Apr-2020", "to": "31-Mar-2021",
             "broadcast": "30-May-2021 18:45:00", "xbrl": "original.xml"},
            {"from": "01-Apr-2020", "to": "31-Mar-2021",
             "broadcast": "15-Aug-2022 11:20:00", "xbrl": "restated.xml"},
        ]),
    )
    archive.put(source="nse.xbrl", doc_key="original.xml", url="https://x/o",
                content=make_xbrl(net_profit=1000.0, revenue=8000.0,
                                  total_assets=50000.0))
    archive.put(source="nse.xbrl", doc_key="restated.xml", url="https://x/r",
                content=make_xbrl(net_profit=700.0, revenue=8000.0,
                                  total_assets=50000.0))

    report = Ingestor(archive, conn).ingest_fundamentals()
    assert not report.errors, report.errors
    yield BitemporalStore(conn), report
    archive.close()
    conn.close()


@pytest.mark.acceptance
def test_acceptance_1_lookahead_canary_restatement(restatement_world):
    """`as_of(t)` returns the ORIGINAL figure before the restatement was
    published and the RESTATED figure after — and the two differ."""
    store, _ = restatement_world

    before = store.as_of("2022-01-01")
    after = store.as_of("2023-01-01")

    original = _value(before, "net_profit")
    restated = _value(after, "net_profit")

    assert original == pytest.approx(1000.0), (
        "as_of(2022-01-01) returned the restated figure, which was not public "
        "until 2022-08-15 — the store is leaking the future"
    )
    assert restated == pytest.approx(700.0)
    assert original != restated, (
        "the canary is only meaningful if the two figures actually differ; "
        "identical values would let a look-ahead bug pass unnoticed"
    )


@pytest.mark.acceptance
def test_acceptance_1_original_is_invisible_before_it_was_filed(restatement_world):
    """Nothing at all is visible before the first filing date."""
    store, _ = restatement_world
    assert store.as_of("2021-04-01").empty, (
        "FY21 results were broadcast 2021-05-30; nothing about that period "
        "should be readable on 2021-04-01"
    )
    assert not store.as_of("2021-06-01").empty


@pytest.mark.acceptance
def test_acceptance_1_boundary_is_the_broadcast_instant(restatement_world):
    """The filing went out at 18:45 IST = 13:15 UTC on 2021-05-30. It is public
    from that instant, and not before."""
    store, _ = restatement_world
    assert store.as_of("2021-05-29").empty
    assert not store.as_of("2021-05-30").empty, (
        "a date argument means end-of-day; a filing broadcast during that day "
        "was public by the close"
    )
    assert store.as_of("2021-05-30T12:00:00+00:00").empty, (
        "at 12:00 UTC the 13:15 UTC broadcast had not happened yet"
    )


@pytest.mark.acceptance
def test_acceptance_1_restatement_history_is_preserved(restatement_world):
    """§7: restatements are new rows. Both versions must remain queryable, or
    restatement sensitivity is not measurable."""
    store, _ = restatement_world
    revisions = store.revisions(ISIN, "net_profit", "2021-03-31")
    assert len(revisions) == 2
    assert list(revisions["value"]) == [1000.0, 700.0]
    assert list(revisions["revision_seq"]) == [0, 1]


@pytest.mark.acceptance
def test_acceptance_1_restatement_survives_out_of_order_archiving(tmp_path):
    """The restatement must win even when its document is archived (and sorts)
    first — revision order follows publication time, not file name."""
    archive = Archive(tmp_path / "archive")
    conn = connect(tmp_path / "db.sqlite")
    archive.put(
        source="nse.results_index", doc_key="idx", url="https://x/i",
        content=make_results_index([
            # "aaa" sorts first but was published LAST
            {"from": "01-Apr-2020", "to": "31-Mar-2021",
             "broadcast": "15-Aug-2022 11:20:00", "xbrl": "aaa_restated.xml"},
            {"from": "01-Apr-2020", "to": "31-Mar-2021",
             "broadcast": "30-May-2021 18:45:00", "xbrl": "zzz_original.xml"},
        ]),
    )
    archive.put(source="nse.xbrl", doc_key="aaa_restated.xml", url="u",
                content=make_xbrl(net_profit=700.0))
    archive.put(source="nse.xbrl", doc_key="zzz_original.xml", url="u",
                content=make_xbrl(net_profit=1000.0))
    Ingestor(archive, conn).ingest_fundamentals()
    store = BitemporalStore(conn)

    assert _value(store.as_of("2022-01-01"), "net_profit") == pytest.approx(1000.0)
    assert _value(store.as_of("2023-01-01"), "net_profit") == pytest.approx(700.0)
    archive.close()
    conn.close()


# ===========================================================================
# §18 ACCEPTANCE TEST 3 — publication lag distribution
# ===========================================================================

@pytest.fixture
def lagged_store(tmp_path):
    """Quarterly facts filed at realistic distances from period end.

    SEBI LODR allows 45 days after a quarter; real filings cluster in the last
    fortnight of that window.
    """
    conn = connect(tmp_path / "db.sqlite")
    store = BitemporalStore(conn)
    rng = __import__("numpy").random.default_rng(11)
    facts = []
    for q, (start, end) in enumerate([
        ("2020-04-01", "2020-06-30"), ("2020-07-01", "2020-09-30"),
        ("2020-10-01", "2020-12-31"), ("2021-01-01", "2021-03-31"),
        ("2021-04-01", "2021-06-30"), ("2021-07-01", "2021-09-30"),
    ]):
        for i in range(40):
            lag = float(rng.uniform(25, 45))
            published = (pd.Timestamp(end) + pd.Timedelta(days=lag)).isoformat()
            facts.append(Fact(
                isin=f"INE{i:03d}A0100{i % 10}", fact_name="net_profit",
                period_type="Q", period_start=start, period_end=end,
                value=100.0 + q, published_at=published, source_doc_hash="d",
            ))
    store.add_facts(facts)
    yield store
    conn.close()


@pytest.mark.acceptance
def test_acceptance_3_publication_lag_sits_in_the_statutory_window(lagged_store):
    """The mass must sit near the statutory filing window, not near zero.

    Mass near zero means facts are stamped with their period end rather than
    their filing date — which is the look-ahead bug wearing a disguise, since
    every number would appear available the instant the quarter closed.
    """
    lags = lagged_store.publication_lags("Q")
    assert len(lags) > 0, "no quarterly facts to test — the check is vacuous"

    assert (lags > 0).all(), "a filing cannot precede the period it reports"
    near_zero = (lags < 7).mean()
    assert near_zero < 0.05, (
        f"{near_zero:.1%} of quarterly facts are published within a week of "
        "period end. Real filings take weeks; this indicates published_at is "
        "being set from period_end, which reinstates look-ahead."
    )
    assert 20 <= lags.median() <= 50, (
        f"median publication lag {lags.median():.1f}d is outside the plausible "
        "range for the 45-day LODR window"
    )
    assert lags.max() <= 120


@pytest.mark.acceptance
def test_acceptance_3_detects_a_misindexed_store(tmp_path):
    """A negative control: if published_at were set to period_end, the check
    above must fail. Without this, a passing test 3 proves nothing."""
    conn = connect(tmp_path / "db.sqlite")
    store = BitemporalStore(conn)
    store.add_facts([
        Fact(isin=f"INE{i:03d}A0100{i % 10}", fact_name="net_profit",
             period_type="Q", period_start="2021-01-01", period_end="2021-03-31",
             # the bug: publication stamped at period end
             value=1.0, published_at="2021-03-31T00:00:00+00:00", source_doc_hash="d")
        for i in range(40)
    ])
    lags = store.publication_lags("Q")
    assert (lags < 7).mean() >= 0.05, "the mis-indexing detector must fire here"
    conn.close()


# ===========================================================================
# §3.1 — as_of is the only read path
# ===========================================================================

def test_latest_is_blocked_from_factor_code(store):
    """The runtime half of the §3.1 guard."""
    import types

    store.add_fact(fact())
    module = types.ModuleType("src.factors.sneaky")
    module.__dict__["store"] = store
    exec("def run(store):\n    return store.latest()", module.__dict__)
    with pytest.raises(LookAheadViolation, match="research code"):
        module.run(store)


def test_latest_is_blocked_from_eval_code(store):
    import types

    store.add_fact(fact())
    module = types.ModuleType("src.eval.sneaky")
    exec("def run(store):\n    return store.latest()", module.__dict__)
    with pytest.raises(LookAheadViolation):
        module.run(store)


def test_guard_walks_the_whole_stack_not_just_the_caller(store):
    """A helper in an allowed module called from a factor is still a factor
    reading unfiltered fundamentals."""
    import types

    store.add_fact(fact())
    helper = types.ModuleType("src.store.helper")
    exec("def indirect(store):\n    return store.latest()", helper.__dict__)
    factor = types.ModuleType("src.factors.indirect")
    factor.__dict__["indirect"] = helper.indirect
    exec("def run(store):\n    return indirect(store)", factor.__dict__)
    with pytest.raises(LookAheadViolation):
        factor.run(store)


def test_latest_works_from_exploratory_code(store):
    """It is not forbidden everywhere — only from research modules."""
    store.add_fact(fact())
    assert len(store.latest()) == 1


def test_latest_would_leak_the_future(store):
    """Demonstrates why latest() is guarded rather than merely discouraged."""
    store.add_fact(fact(value=1000.0, revision_seq=0))
    store.add_fact(fact(value=700.0, revision_seq=1,
                        published_at="2022-08-15T05:50:00+00:00"))
    assert _value(store.latest(), "net_profit") == pytest.approx(700.0)
    assert _value(store.as_of("2022-01-01"), "net_profit") == pytest.approx(1000.0)


# ===========================================================================
# §7 semantics
# ===========================================================================

def test_facts_are_append_only(store):
    store.add_fact(fact())
    import sqlite3

    with pytest.raises(sqlite3.IntegrityError, match="append-only"):
        store.conn.execute(f"UPDATE {FUNDAMENTALS_TABLE} SET value = 1")


def test_fact_without_publication_timestamp_is_rejected(store):
    """§5: rejected, not guessed."""
    with pytest.raises(FactRejected, match="not guessed"):
        store.add_fact(fact(published_at=""))


def test_fact_published_before_its_period_ends_is_rejected(store):
    with pytest.raises(FactRejected, match="cannot be published before"):
        store.add_fact(fact(published_at="2020-06-01T00:00:00+00:00"))


def test_unknown_period_type_rejected(store):
    with pytest.raises(FactRejected, match="period_type"):
        store.add_fact(fact(period_type="WEEKLY"))


def test_next_revision_increments(store):
    assert store.next_revision(ISIN, "net_profit", "2021-03-31") == 0
    store.add_fact(fact())
    assert store.next_revision(ISIN, "net_profit", "2021-03-31") == 1


def test_non_defensible_facts_are_excluded_by_default(store):
    """§5: screener-sourced facts must not silently enter a study."""
    store.add_fact(fact(fact_name="revenue", value=5000.0, defensible=False))
    assert store.as_of("2023-01-01").empty
    assert len(store.as_of("2023-01-01", include_non_defensible=True)) == 1
    assert len(store.non_defensible_facts()) == 1


def test_minimum_publication_lag_shifts_the_cutoff(store):
    """A factor can demand extra margin beyond the broadcast timestamp."""
    store.add_fact(fact())  # published 2021-05-30
    assert not store.as_of("2021-06-05").empty
    assert store.as_of("2021-06-05", min_publication_lag_days=10).empty


def test_as_of_filters_by_isin_and_fact_name(store):
    store.add_fact(fact())
    store.add_fact(fact(fact_name="revenue", value=8000.0))
    store.add_fact(fact(isin="INE111A01011", value=50.0))

    assert len(store.as_of("2023-01-01", isins=[ISIN])) == 2
    assert len(store.as_of("2023-01-01", fact_names=["revenue"])) == 1
    assert store.as_of("2023-01-01", isins=[]).empty


def test_as_of_latest_period_returns_a_wide_frame(store):
    for end, value in [("2020-03-31", 800.0), ("2021-03-31", 1000.0)]:
        store.add_fact(fact(
            period_start=f"{int(end[:4]) - 1}-04-01", period_end=end, value=value,
            published_at=f"{int(end[:4])}-05-30T13:15:00+00:00",
        ))
    wide = store.as_of_latest_period("2021-12-31", ["net_profit"], period_type="A")
    assert wide.loc[ISIN, "net_profit"] == pytest.approx(1000.0)

    earlier = store.as_of_latest_period("2021-01-01", ["net_profit"], period_type="A")
    assert earlier.loc[ISIN, "net_profit"] == pytest.approx(800.0), (
        "on 2021-01-01 only the FY20 filing existed"
    )


def test_stale_facts_are_dropped(store):
    """A company that stopped filing in 2015 must not keep contributing its
    2015 fundamentals to a 2023 factor score."""
    store.add_fact(fact(period_start="2014-04-01", period_end="2015-03-31",
                        published_at="2015-05-30T13:15:00+00:00"))
    assert store.as_of_latest_period("2023-01-01", ["net_profit"]).empty
    assert not store.as_of_latest_period(
        "2023-01-01", ["net_profit"], max_staleness_days=None
    ).empty


def test_missing_fact_becomes_a_nan_column(store):
    store.add_fact(fact())
    wide = store.as_of_latest_period("2022-01-01", ["net_profit", "does_not_exist"])
    assert "does_not_exist" in wide.columns
    assert pd.isna(wide.loc[ISIN, "does_not_exist"])


def test_coverage_summary(store):
    store.add_fact(fact())
    store.add_fact(fact(fact_name="revenue", value=8000.0))
    coverage = store.coverage()
    assert set(coverage["fact_name"]) == {"net_profit", "revenue"}


def _value(frame: pd.DataFrame, fact_name: str) -> float:
    rows = frame[frame["fact_name"] == fact_name]
    assert len(rows) == 1, f"expected exactly one {fact_name} row, got {len(rows)}"
    return float(rows["value"].iloc[0])
