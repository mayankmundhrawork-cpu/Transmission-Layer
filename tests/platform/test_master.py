"""Security master and PIT universe tests (§3.2, §3.3, §6).

Includes acceptance tests 2 (survivorship canary) and 4 (index membership PIT)
from §18. Those two are marked `acceptance` and are the CP3 gate.
"""
from __future__ import annotations

import datetime as dt

import pytest

from src.master.security import SecurityMaster
from src.master.universe import Universe, UniverseScreens, universe_size_series
from src.store.schema import connect
from tests.platform.world import (
    DELISTING_DATE, MERGER_DATE, NEWLISTING_DATE, RENAME_DATE, SPECIALS,
    SURVEILLANCE_END, SURVEILLANCE_START, build_world, rebalance_dates,
)


@pytest.fixture(scope="module")
def world_conn(tmp_path_factory):
    """Built once — it is ~1500 sessions x 48 names and does not change."""
    conn = connect(tmp_path_factory.mktemp("db") / "platform.sqlite")
    build_world(conn)
    yield conn
    conn.close()


@pytest.fixture
def master(world_conn):
    return SecurityMaster(world_conn)


@pytest.fixture
def universe(world_conn):
    return Universe(world_conn)


# ===========================================================================
# §18 ACCEPTANCE TEST 2 — survivorship canary
# ===========================================================================

@pytest.mark.acceptance
def test_acceptance_2_survivorship_canary(universe):
    """A company delisted after HISTORY_START must appear in the universe
    before its delisting and vanish after.

    This is the test that catches the single most common way factor research
    is invalidated: building a universe from names that exist today.
    """
    delisted = SPECIALS["DELISTED"][0]

    before = universe.as_of(dt.date(2021, 1, 15), "nifty500")
    assert delisted in before.isins, (
        "a company that was listed and trading on 2021-01-15 is missing from "
        "the universe for that date — the universe is being built from names "
        "that still exist, which is survivorship bias"
    )

    on_last_day = universe.as_of(DELISTING_DATE, "nifty500")
    assert delisted in on_last_day.isins, (
        "a stock trades on its final day; dropping it loses the delisting "
        "return, which is exactly the observation survivorship bias erases"
    )

    after = universe.as_of(dt.date(2021, 12, 15), "nifty500")
    assert delisted not in after.isins


@pytest.mark.acceptance
def test_acceptance_2_delisted_name_has_price_history_before_delisting(world_conn):
    """Absence after delisting must come from the listing window, not from an
    empty price series — otherwise the test above passes for the wrong reason."""
    delisted = SPECIALS["DELISTED"][0]
    n = world_conn.execute(
        "SELECT COUNT(*) c FROM price_daily WHERE isin=? AND date<?",
        (delisted, DELISTING_DATE.isoformat()),
    ).fetchone()["c"]
    assert n > 250


@pytest.mark.acceptance
def test_acceptance_2_merged_name_is_present_until_the_merger(universe, master):
    merged = SPECIALS["MERGED"][0]
    assert merged in universe.as_of(dt.date(2022, 1, 31), "nifty500").isins
    assert merged not in universe.as_of(dt.date(2022, 6, 30), "nifty500").isins
    # ...and the return series can be followed across the event rather than
    # just stopping (§6).
    assert master.terminal_isin(merged) == SPECIALS["ACQUIRER"][0]


# ===========================================================================
# §18 ACCEPTANCE TEST 4 — index membership is point-in-time
# ===========================================================================

@pytest.mark.acceptance
def test_acceptance_4_index_membership_pit_on_three_dates(universe):
    """Reconstructed constituents on three historical dates must match the
    membership that was actually in force on those dates."""
    checks = [
        # date, must contain, must not contain, why
        (dt.date(2021, 1, 15), SPECIALS["DELISTED"][0], SPECIALS["NEWLISTING"][0],
         "DELISTED was a member; NEWLISTING had not listed yet"),
        (dt.date(2022, 1, 31), SPECIALS["MERGED"][0], SPECIALS["DELISTED"][0],
         "MERGED was still a member; DELISTED had left"),
        (dt.date(2023, 6, 30), SPECIALS["NEWLISTING"][0], SPECIALS["MERGED"][0],
         "NEWLISTING had joined; MERGED had left"),
    ]
    for date, present, absent, why in checks:
        members = universe.index_members("NIFTY 500", date)
        assert present in members, f"{date}: {why}"
        assert absent not in members, f"{date}: {why}"


@pytest.mark.acceptance
def test_acceptance_4_membership_is_not_just_todays_list(universe):
    """The failure mode being excluded: an index whose membership is the same
    set on every historical date is not point-in-time, it is today's list."""
    sets = [
        frozenset(universe.index_members("NIFTY 500", d))
        for d in (dt.date(2019, 6, 28), dt.date(2021, 12, 31), dt.date(2023, 6, 30))
    ]
    assert len(set(sets)) == len(sets), "membership must differ across dates"


# ===========================================================================
# §3.3 — ISIN is the key, symbol is an attribute
# ===========================================================================

def test_symbol_is_validity_dated(master):
    isin = SPECIALS["RENAMED"][0]
    assert master.symbol_at(isin, dt.date(2019, 1, 15)) == "OLDNAME"
    assert master.symbol_at(isin, RENAME_DATE) == "NEWNAME"
    assert master.symbol_at(isin, dt.date(2023, 1, 15)) == "NEWNAME"


def test_symbol_resolves_to_the_right_isin_for_the_date(master):
    isin = SPECIALS["RENAMED"][0]
    assert master.resolve_symbol("OLDNAME", dt.date(2019, 1, 15)) == isin
    assert master.resolve_symbol("NEWNAME", dt.date(2023, 1, 15)) == isin
    # The old symbol does not resolve after the rename — which is what stops a
    # symbol-keyed join from splicing two companies together.
    assert master.resolve_symbol("OLDNAME", dt.date(2023, 1, 15)) is None


def test_attribute_intervals_do_not_overlap(world_conn, master):
    rows = world_conn.execute(
        "SELECT valid_from, valid_to FROM security_attr"
        " WHERE isin=? AND attr='symbol' ORDER BY valid_from",
        (SPECIALS["RENAMED"][0],),
    ).fetchall()
    assert len(rows) == 2
    assert rows[0]["valid_to"] == (RENAME_DATE - dt.timedelta(days=1)).isoformat()
    assert rows[1]["valid_to"] is None


def test_reasserting_the_same_value_does_not_create_an_interval(tmp_path):
    """Sources republish the same value daily; each repeat must not manufacture
    a new validity interval."""
    conn = connect(tmp_path / "db.sqlite")
    m = SecurityMaster(conn)
    m.upsert_security("INE001A01001")
    for day in ("2020-01-01", "2020-01-02", "2020-01-03"):
        m.set_attribute("INE001A01001", "symbol", "SAME", day)
    assert conn.execute(
        "SELECT COUNT(*) c FROM security_attr WHERE isin='INE001A01001'"
    ).fetchone()["c"] == 1


def test_invalid_isin_is_rejected(tmp_path):
    m = SecurityMaster(connect(tmp_path / "db.sqlite"))
    for bad in ("", "SHORT", "nan", "-", "TOOLONGANISIN123"):
        with pytest.raises(ValueError, match="not a valid ISIN"):
            m.upsert_security(bad)


# ===========================================================================
# §6 screens
# ===========================================================================

def test_listed_on_includes_delisted_names(master):
    """The survivorship-safe primitive. There is no `currently_listed()`."""
    listed = master.listed_on(dt.date(2021, 1, 15))
    assert SPECIALS["DELISTED"][0] in listed
    assert SPECIALS["NEWLISTING"][0] not in listed


def test_illiquid_name_is_screened_out(universe):
    result = universe.as_of(dt.date(2022, 6, 30), "nifty500")
    assert SPECIALS["ILLIQUID"][0] not in result.isins
    assert result.excluded["illiquid"] >= 1


def test_penny_stock_is_screened_out(universe):
    result = universe.as_of(dt.date(2022, 6, 30), "nifty500")
    assert SPECIALS["PENNY"][0] not in result.isins
    assert result.excluded["below_price_floor"] >= 1


def test_new_listing_fails_the_history_screen_then_passes(universe):
    fresh = SPECIALS["NEWLISTING"][0]
    soon = universe.as_of(dt.date(2023, 6, 30), "nifty500")
    assert fresh not in soon.isins, "under 250 sessions of history"
    assert soon.excluded["insufficient_history"] >= 1

    relaxed = universe.as_of(dt.date(2023, 6, 30), "nifty500",
                             UniverseScreens(min_listing_sessions=100))
    assert fresh in relaxed.isins, "passes once the history requirement is met"


def test_surveillance_stage_2_excluded_only_while_in_force(universe):
    """PIT, not permanent: the name is investable before and after its ASM
    window and excluded during it."""
    watched = SPECIALS["SURVEILLED"][0]
    during = universe.as_of(dt.date(2021, 4, 15), "nifty500")
    assert watched not in during.isins
    assert during.excluded["surveillance_stage_2_plus"] == 1

    after = universe.as_of(dt.date(2021, 9, 15), "nifty500")
    assert watched in after.isins


def test_screens_are_evaluated_at_the_as_of_date_not_today(universe):
    """The liquidity screen must use the trailing window ending at the as-of
    date. If it used all history, a name that became liquid in 2023 would pass
    a 2019 screen."""
    early = universe.as_of(dt.date(2019, 6, 28), "nifty500")
    late = universe.as_of(dt.date(2023, 6, 30), "nifty500")
    assert set(early.isins) != set(late.isins)


def test_exclusion_counts_are_reported(universe):
    result = universe.as_of(dt.date(2022, 6, 30), "nifty500")
    for key in ("illiquid", "below_price_floor", "insufficient_history",
                "surveillance_stage_2_plus", "suspended"):
        assert key in result.excluded
    assert len(result) + sum(
        v for k, v in result.excluded.items() if k != "index_history_missing"
    ) >= len(result)


def test_unknown_tier_rejected(universe):
    with pytest.raises(ValueError, match="unknown tier"):
        universe.as_of(dt.date(2022, 6, 30), "largecap_only")


def test_missing_index_history_is_flagged_not_silently_widened(tmp_path):
    """A tier whose index history is absent must say so rather than quietly
    becoming a total-market study."""
    conn = connect(tmp_path / "db.sqlite")
    build_world(conn)
    conn.execute("DELETE FROM index_membership WHERE index_name='NIFTY 500'")
    result = Universe(conn).as_of(dt.date(2022, 6, 30), "nifty500")
    assert result.excluded.get("index_history_missing") == 1


# ===========================================================================
# §6 succession
# ===========================================================================

def test_succession_chain_records_ratio(master):
    chain = master.succession_chain(SPECIALS["MERGED"][0])
    assert len(chain) == 1
    assert chain[0]["successor_isin"] == SPECIALS["ACQUIRER"][0]
    assert chain[0]["share_ratio"] == pytest.approx(0.7)
    assert chain[0]["event_type"] == "merger"


def test_terminated_chain_returns_none(tmp_path):
    """Liquidation ends the series. None must mean 'the series ends here', not
    'data missing' — the difference is a -100% return versus a silent gap."""
    conn = connect(tmp_path / "db.sqlite")
    m = SecurityMaster(conn)
    m.upsert_security("INE001A01001")
    m.add_succession("INE001A01001", None, "scheme", "2021-01-01")
    assert m.terminal_isin("INE001A01001") is None


def test_succession_cycle_does_not_hang(tmp_path):
    conn = connect(tmp_path / "db.sqlite")
    m = SecurityMaster(conn)
    for isin in ("INE001A01001", "INE002A01002"):
        m.upsert_security(isin)
    m.add_succession("INE001A01001", "INE002A01002", "merger", "2021-01-01")
    m.add_succession("INE002A01002", "INE001A01001", "merger", "2021-06-01")
    assert len(m.succession_chain("INE001A01001")) <= 10


def test_no_successor_returns_self(master):
    isin = SPECIALS["ACQUIRER"][0]
    assert master.terminal_isin(isin) == isin


# ===========================================================================
# liquidity helpers used by §9/§13
# ===========================================================================

def test_days_to_liquidate_scales_with_size(universe):
    isin = SPECIALS["ACQUIRER"][0]
    small = universe.days_to_liquidate(isin, 100_000, dt.date(2022, 6, 30))
    large = universe.days_to_liquidate(isin, 1_000_000, dt.date(2022, 6, 30))
    assert large == pytest.approx(small * 10, rel=1e-6)
    assert small > 0


def test_days_to_liquidate_is_infinite_for_a_non_trading_name(universe):
    """Not a slow exit — a construction error. `inf` says so."""
    assert universe.days_to_liquidate(
        "INE999Z01099", 100_000, dt.date(2022, 6, 30)
    ) == float("inf")


# ===========================================================================
# CP6 diagnostic
# ===========================================================================

def test_universe_size_series_has_no_unexplained_discontinuity(universe):
    """CP6: size over time, with every jump attributable to a known event."""
    dates = rebalance_dates("quarterly", dt.date(2019, 6, 28), dt.date(2023, 12, 29))
    series = universe_size_series(universe, dates, "nifty500")
    assert len(series) == len(dates)
    assert (series["members"] > 30).all(), "the universe should never collapse"

    # Quarter-on-quarter changes should be small and explainable; the world has
    # exactly three membership events, so nothing should move by more than a
    # couple of names at once.
    deltas = series["members"].diff().abs().dropna()
    assert deltas.max() <= 3, (
        f"unexplained universe discontinuity of {deltas.max()} names:\n{series}"
    )
