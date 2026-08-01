"""Price and return layer tests (§5).

The property being defended: corporate actions are applied *at* the ex-date,
never retroactively over history. Back-adjusting a whole price series is the
convenient thing to do and is quietly a look-ahead construction — it rewrites
what a price "was" using an event that had not happened yet.
"""
from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd
import pytest

from src.prices.daily import (
    benchmark_returns, circuit_locked, corporate_action_factors, daily_returns,
    next_transactable_session, price_panel, realised_volatility, trailing_return,
)
from src.store.schema import connect, transaction

ISIN = "INE001A01001"


@pytest.fixture
def conn(tmp_path):
    c = connect(tmp_path / "db.sqlite")
    yield c
    c.close()


def seed_prices(conn, isin=ISIN, closes=None, dates=None, prev_first=None,
                highs=None, lows=None):
    dates = dates or [d.date().isoformat()
                      for d in pd.bdate_range("2021-01-01", periods=len(closes))]
    rows = []
    prev = prev_first if prev_first is not None else closes[0]
    for i, (day, close) in enumerate(zip(dates, closes)):
        hi = highs[i] if highs else close * 1.01
        lo = lows[i] if lows else close * 0.99
        rows.append((isin, day, "SYM", "EQ", close, hi, lo, close, prev,
                     1000.0, close * 1000.0, 50.0, None, "test"))
        prev = close
    with transaction(conn):
        conn.executemany(
            "INSERT OR REPLACE INTO price_daily (isin, date, symbol, series, open,"
            " high, low, close, prev_close, volume, turnover, trades, deliv_qty,"
            " source_doc_hash) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    return dates


def add_action(conn, isin, action_type, ex_date, ratio_to=None, amount=None):
    conn.execute(
        "INSERT OR REPLACE INTO corporate_action (isin, action_type, ex_date,"
        " ratio_from, ratio_to, amount, purpose, published_at, source_doc_hash)"
        " VALUES (?,?,?,1.0,?,?,'test',?,'h')",
        (isin, action_type, ex_date, ratio_to, amount, ex_date),
    )


# --- panels -----------------------------------------------------------------

def test_price_panel_is_wide_and_sorted(conn):
    seed_prices(conn, closes=[100.0, 101.0, 102.0])
    panel = price_panel(conn, [ISIN])
    assert list(panel.columns) == [ISIN]
    assert len(panel) == 3
    assert panel.index.is_monotonic_increasing


def test_price_panel_respects_date_bounds(conn):
    dates = seed_prices(conn, closes=[100.0, 101.0, 102.0, 103.0])
    panel = price_panel(conn, [ISIN], start=dates[1], end=dates[2])
    assert len(panel) == 2


def test_empty_isin_list_yields_empty_panel(conn):
    assert price_panel(conn, []).empty


# --- returns ----------------------------------------------------------------

def test_simple_returns(conn):
    seed_prices(conn, closes=[100.0, 110.0, 99.0])
    r = daily_returns(conn, [ISIN])[ISIN]
    assert pd.isna(r.iloc[0]), "the first observation has no prior close"
    assert r.iloc[1] == pytest.approx(0.10)
    assert r.iloc[2] == pytest.approx(-0.10)


def test_split_is_adjusted_on_the_ex_date_only(conn):
    """A 1:5 split: raw close drops 100 -> 20, and the true return is ~0."""
    dates = seed_prices(conn, closes=[100.0, 20.0, 21.0])
    add_action(conn, ISIN, "split", dates[1], ratio_to=5.0)

    r = daily_returns(conn, [ISIN])[ISIN]
    assert r.iloc[1] == pytest.approx(0.0), (
        "the split day shows a -80% return — the share ratio was not applied"
    )
    assert r.iloc[2] == pytest.approx(0.05)


def test_history_is_not_rewritten_by_a_later_split(conn):
    """The price series stays raw. A factor reading a price level on a past
    date must see the number that was actually printed on that date."""
    dates = seed_prices(conn, closes=[100.0, 20.0, 21.0])
    add_action(conn, ISIN, "split", dates[1], ratio_to=5.0)
    panel = price_panel(conn, [ISIN])
    assert panel[ISIN].iloc[0] == pytest.approx(100.0), (
        "the pre-split close was 100 and must remain 100; back-adjusting it to "
        "20 would show a price nobody could have observed on that date"
    )


def test_bonus_is_adjusted(conn):
    dates = seed_prices(conn, closes=[100.0, 50.0])
    add_action(conn, ISIN, "bonus", dates[1], ratio_to=2.0)  # 1:1 bonus
    assert daily_returns(conn, [ISIN])[ISIN].iloc[1] == pytest.approx(0.0)


def test_dividend_is_added_back(conn):
    dates = seed_prices(conn, closes=[100.0, 95.0])
    add_action(conn, ISIN, "dividend", dates[1], amount=5.0)
    r = daily_returns(conn, [ISIN])[ISIN]
    assert r.iloc[1] == pytest.approx(0.0), "a pure dividend drop is not a loss"
    r_ex = daily_returns(conn, [ISIN], include_dividends=False)[ISIN]
    assert r_ex.iloc[1] == pytest.approx(-0.05)


def test_unparsed_ratio_does_not_corrupt_the_return(conn):
    """classify_action returns no ratio when it cannot parse one. That must
    leave the return alone rather than silently multiplying it."""
    dates = seed_prices(conn, closes=[100.0, 101.0])
    add_action(conn, ISIN, "split", dates[1], ratio_to=None)
    assert daily_returns(conn, [ISIN])[ISIN].iloc[1] == pytest.approx(0.01)


def test_gap_in_trading_does_not_manufacture_a_return(conn):
    """A suspension then resumption is not a one-day move."""
    seed_prices(conn, closes=[100.0, 101.0], dates=["2021-01-04", "2021-01-05"])
    seed_prices(conn, closes=[150.0], dates=["2021-06-01"])
    r = daily_returns(conn, [ISIN])[ISIN]
    assert len(r.dropna()) == 2, "the resume day must not be treated as a return"


# --- trailing statistics ----------------------------------------------------

def test_trailing_return_skips_the_recent_window(conn):
    """12-1 momentum (§8): skip the most recent month."""
    dates = seed_prices(conn, closes=[100.0] * 20 + [200.0])
    full = trailing_return(daily_returns(conn, [ISIN]), dates[-1], lookback=21, skip=0)
    skipped = trailing_return(daily_returns(conn, [ISIN]), dates[-1], lookback=20, skip=1)
    assert full[ISIN] == pytest.approx(1.0)
    assert skipped[ISIN] == pytest.approx(0.0), "the doubling day must be skipped"


def test_trailing_return_requires_enough_observations(conn):
    """8 observations out of 252 is not a 12-month return."""
    dates = seed_prices(conn, closes=[100.0] * 8)
    result = trailing_return(daily_returns(conn, [ISIN]), dates[-1], lookback=252)
    assert pd.isna(result[ISIN])


def test_realised_volatility_is_annualised(conn):
    rng = np.random.default_rng(4)
    closes = list(100 * np.exp(np.cumsum(rng.normal(0, 0.02, 300))))
    dates = seed_prices(conn, closes=closes)
    vol = realised_volatility(daily_returns(conn, [ISIN]), dates[-1], lookback=252)
    assert 0.20 < vol[ISIN] < 0.45, "0.02 daily sigma is ~32% annualised"


# --- circuits ---------------------------------------------------------------

def test_circuit_lock_detected_at_a_band(conn):
    """Zero intraday range at a 5% move is the lock signature."""
    seed_prices(conn, closes=[100.0, 105.0], dates=["2021-01-04", "2021-01-05"],
                highs=[101.0, 105.0], lows=[99.0, 105.0])
    assert circuit_locked(conn, ISIN, "2021-01-05") is True
    assert circuit_locked(conn, ISIN, "2021-01-04") is False


def test_a_move_with_intraday_range_is_not_a_lock(conn):
    seed_prices(conn, closes=[100.0, 105.0], dates=["2021-01-04", "2021-01-05"],
                highs=[101.0, 106.0], lows=[99.0, 104.0])
    assert circuit_locked(conn, ISIN, "2021-01-05") is False


def test_a_flat_day_off_a_band_is_not_a_lock(conn):
    seed_prices(conn, closes=[100.0, 100.5], dates=["2021-01-04", "2021-01-05"],
                highs=[101.0, 100.5], lows=[99.0, 100.5])
    assert circuit_locked(conn, ISIN, "2021-01-05") is False


def test_trade_carries_forward_to_the_next_transactable_session(conn):
    """§9: a stock locked on a rebalance date is not transactable at that price."""
    seed_prices(conn, closes=[100.0, 105.0, 110.25, 111.0],
                dates=["2021-01-04", "2021-01-05", "2021-01-06", "2021-01-07"],
                highs=[101.0, 105.0, 110.25, 112.0],
                lows=[99.0, 105.0, 110.25, 110.0])
    assert next_transactable_session(conn, ISIN, "2021-01-05") == "2021-01-07", (
        "two consecutive upper-circuit sessions must be carried through"
    )


def test_next_transactable_returns_none_when_never_unlocked(conn):
    seed_prices(conn, closes=[100.0, 105.0], dates=["2021-01-04", "2021-01-05"],
                highs=[101.0, 105.0], lows=[99.0, 105.0])
    assert next_transactable_session(conn, ISIN, "2021-01-05", max_forward=1) is None


def test_missing_price_is_not_a_lock(conn):
    assert circuit_locked(conn, ISIN, "2021-01-04") is False


# --- benchmark --------------------------------------------------------------

def test_benchmark_returns_use_total_return_level(conn):
    with transaction(conn):
        conn.executemany(
            "INSERT INTO benchmark_daily (index_name, date, close, total_return_close)"
            " VALUES ('NIFTY_500_TRI',?,?,?)",
            [("2021-01-04", 100.0, 100.0), ("2021-01-05", 101.0, 102.0)],
        )
    r = benchmark_returns(conn, "NIFTY_500_TRI")
    assert r.iloc[1] == pytest.approx(0.02), "TRI level must win over price level"


def test_missing_benchmark_is_empty_not_an_error(conn):
    assert benchmark_returns(conn, "NOSUCH").empty


# --- corporate action factors ----------------------------------------------

def test_multiple_actions_on_one_day_compound(conn):
    dates = seed_prices(conn, closes=[100.0, 20.0])
    add_action(conn, ISIN, "split", dates[1], ratio_to=5.0)
    add_action(conn, ISIN, "dividend", dates[1], amount=2.0)
    factors = corporate_action_factors(conn, [ISIN])
    row = factors[factors["ex_date"] == dates[1]].iloc[0]
    assert row["share_ratio"] == pytest.approx(5.0)
    assert row["dividend"] == pytest.approx(2.0)
