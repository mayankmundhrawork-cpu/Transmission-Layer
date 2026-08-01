"""Cost, impact, and price-layer tests (§9, §18.6) — the CP5 gate.

The headline test is the hand-computed round trip. The rest defend the
property §18.6 asks for: no path through this code produces a zero-cost trade
or a fill at mid.
"""
from __future__ import annotations

import datetime as dt
import warnings

import numpy as np
import pandas as pd
import pytest

from src.costs.impact import (
    amihud_lambda, corwin_schultz_spread, days_to_liquidate, impact_bps,
    panel_lambda, rolling_lambda, spread_bps, violates_participation,
)
from src.costs.model import CostModel, UnverifiedRates, load_rate_tables, rate_table_status
from src.costs.worked_example import (
    BUY_DATE, BUY_PRICE, EXPECTED_BUY_TOTAL, EXPECTED_ROUND_TRIP,
    EXPECTED_ROUND_TRIP_BPS, EXPECTED_SELL_TOTAL, IMPACT_BPS, QUANTITY,
    SELL_DATE, SELL_PRICE, SPREAD_BPS,
)


@pytest.fixture
def model():
    return CostModel(warn_unverified=False)


# ===========================================================================
# CP5 — hand-computed round trip
# ===========================================================================

def test_cp5_round_trip_matches_hand_computation(model):
    """The CP5 gate. Derivation is in src/costs/worked_example.py."""
    trip = model.round_trip(
        buy_price=BUY_PRICE, sell_price=SELL_PRICE, quantity=QUANTITY,
        buy_date=BUY_DATE, sell_date=SELL_DATE,
        spread_bps=SPREAD_BPS, impact_bps=IMPACT_BPS,
    )
    assert trip.buy.total == pytest.approx(EXPECTED_BUY_TOTAL, abs=1e-4)
    assert trip.sell.total == pytest.approx(EXPECTED_SELL_TOTAL, abs=1e-4)
    assert trip.total == pytest.approx(EXPECTED_ROUND_TRIP, abs=1e-4)
    assert trip.bps == pytest.approx(EXPECTED_ROUND_TRIP_BPS, abs=1e-2)


def test_cp5_every_component_matches_by_hand(model):
    buy = model.leg("buy", price=500.0, quantity=100, date="2023-06-15",
                    spread_bps=40.0, impact_bps=15.0)
    assert buy.stt == pytest.approx(50.0)
    assert buy.stamp_duty == pytest.approx(7.5)
    assert buy.exchange_txn == pytest.approx(1.625)
    assert buy.sebi_fee == pytest.approx(0.05)
    assert buy.gst == pytest.approx(0.3015)
    assert buy.dp_charges == 0.0, "DP charges are levied on the sell leg only"
    assert buy.spread == pytest.approx(100.0), "half of a 40bps spread"
    assert buy.impact == pytest.approx(75.0)

    sell = model.leg("sell", price=550.0, quantity=100, date="2023-09-15",
                     spread_bps=40.0, impact_bps=15.0)
    assert sell.stamp_duty == 0.0, "stamp duty is buy-side only from 2020-07"
    assert sell.dp_charges == pytest.approx(13.5)
    assert sell.gst == pytest.approx(2.76165, abs=1e-5)


def test_worked_example_runs_and_prints(capsys):
    from src.costs.worked_example import main

    assert main() == 0
    out = capsys.readouterr().out
    assert "ROUND TRIP" in out
    assert "MISMATCH" not in out
    assert "UNVERIFIED" in out, "the verification warning must be impossible to miss"


# ===========================================================================
# §18.6 — cost floor
# ===========================================================================

@pytest.mark.acceptance
def test_acceptance_6_no_trade_can_be_costless(model):
    """No combination of inputs produces a zero-cost trade."""
    cases = [
        dict(side="buy", price=100.0, quantity=1, date="2010-04-01"),
        dict(side="sell", price=100.0, quantity=1, date="2010-04-01"),
        dict(side="buy", price=1.0, quantity=1, date="2024-12-31"),
        dict(side="sell", price=10000.0, quantity=10000, date="2018-01-01"),
    ]
    for case in cases:
        # Even with spread and impact explicitly zeroed, statutory cost remains.
        cost = model.leg(spread_bps=0.0, impact_bps=0.0, **case)
        assert cost.total > 0, f"zero-cost trade produced for {case}"
        assert cost.statutory > 0


@pytest.mark.acceptance
def test_acceptance_6_default_spread_is_not_free(model):
    """A missing spread estimate must not become a zero cost."""
    cost = model.leg("buy", price=100.0, quantity=100, date="2023-06-15")
    assert cost.spread > 0, "no spread estimate supplied — the default must bite"


@pytest.mark.acceptance
def test_acceptance_6_spread_estimator_never_returns_zero():
    """Corwin-Schultz returns zero or negative on illiquid and circuit-locked
    names — exactly where the true spread is widest. The floor stops that
    becoming a free trade."""
    flat = pd.Series([100.0] * 30)  # zero range every day: locked
    assert spread_bps(flat, flat) >= 10.0
    assert corwin_schultz_spread(flat, flat) == 0.0


@pytest.mark.acceptance
def test_acceptance_6_net_return_is_always_below_gross(model):
    for gross in (-0.20, 0.0, 0.05, 0.50):
        net = model.net_return(gross, entry_notional=100_000,
                               buy_date="2023-06-15", sell_date="2023-09-15")
        assert net < gross, f"gross {gross} did not attract a cost"


def test_zero_quantity_is_the_only_zero_cost(model):
    assert model.leg("buy", price=100.0, quantity=0, date="2023-06-15").total == 0.0


def test_negative_quantity_rejected(model):
    with pytest.raises(ValueError, match="non-negative"):
        model.leg("buy", price=100.0, quantity=-10, date="2023-06-15")


# ===========================================================================
# rate tables as data
# ===========================================================================

def test_rate_table_is_selected_by_effective_date(model):
    """Stamp duty moved to the uniform 0.015% regime on 2020-07-01."""
    old = model.leg("buy", price=100.0, quantity=1000, date="2019-01-01")
    new = model.leg("buy", price=100.0, quantity=1000, date="2021-01-01")
    assert old.stamp_duty < new.stamp_duty
    assert old.rate_table_effective_from == "2017-07-01"
    assert new.rate_table_effective_from == "2020-07-01"


def test_pre_gst_trades_pay_no_gst(model):
    assert model.leg("buy", price=100.0, quantity=1000, date="2015-01-01").gst == 0.0
    assert model.leg("buy", price=100.0, quantity=1000, date="2018-01-01").gst > 0.0


def test_gst_does_not_apply_to_statutory_levies(model):
    """GST on STT would be a tax on a tax. The applies-to list is explicit."""
    cost = model.leg("buy", price=1000.0, quantity=1000, date="2023-06-15")
    gstable = cost.exchange_txn + cost.sebi_fee + cost.brokerage + cost.dp_charges
    assert cost.gst == pytest.approx(gstable * 0.18)
    assert cost.gst < cost.stt * 0.18, "STT is clearly not in the GST base"


def test_earliest_table_used_before_any_effective_date(model):
    cost = model.leg("buy", price=100.0, quantity=100, date="2005-01-01")
    assert cost.rate_table_effective_from == "2010-04-01"


def test_rates_are_data_not_code():
    """Correcting a rate must not require editing a module."""
    from src.costs.model import RATES_PATH

    assert RATES_PATH.suffix == ".yaml"
    assert RATES_PATH.exists()


def test_unverified_rates_warn_loudly():
    """§9 requires verification against official sources. Until that is done,
    the model must say so rather than quietly producing confident numbers."""
    load_rate_tables.cache_clear()
    model = CostModel(warn_unverified=True)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        model.leg("buy", price=100.0, quantity=100, date="2023-06-15")
    assert any(issubclass(w.category, UnverifiedRates) for w in caught)


def test_rate_table_status_reports_verification():
    status = rate_table_status()
    assert status["unverified_count"] == len(status["tables"])
    assert status["all_verified"] is False


# ===========================================================================
# §9 impact — Amihud
# ===========================================================================

def test_amihud_lambda_is_higher_for_the_illiquid_name():
    rng = np.random.default_rng(3)
    returns = pd.Series(rng.normal(0, 0.02, 250))
    liquid = pd.Series(np.full(250, 50_000_000.0))
    thin = pd.Series(np.full(250, 500_000.0))
    assert amihud_lambda(returns, thin) > amihud_lambda(returns, liquid)
    assert amihud_lambda(returns, thin) == pytest.approx(
        amihud_lambda(returns, liquid) * 100, rel=0.01
    )


def test_amihud_returns_nan_on_insufficient_data():
    """Not a conservative estimate — an arbitrary one. NaN says so."""
    assert np.isnan(amihud_lambda(pd.Series([0.01] * 5), pd.Series([1e6] * 5)))


def test_amihud_drops_near_zero_turnover_days():
    """|r|/V explodes as V->0; one stale-price day would dominate the mean."""
    returns = pd.Series([0.01] * 100)
    turnover = pd.Series([1e6] * 99 + [1.0])
    clean = amihud_lambda(returns, turnover)
    assert np.isfinite(clean)
    assert clean == pytest.approx(0.01 / 1e6, rel=0.05)


def test_amihud_rejects_misaligned_inputs():
    with pytest.raises(ValueError, match="align"):
        amihud_lambda(pd.Series([0.01] * 10), pd.Series([1e6] * 5))


def test_impact_scales_with_trade_size():
    lam = 1e-9
    small = impact_bps(100_000, lam)
    large = impact_bps(1_000_000, lam)
    assert large == pytest.approx(small * 10, rel=1e-6)


def test_impact_is_capped():
    """An uncapped lambda x V can imply impact above 100% of notional. That is
    the model saying the trade is impossible, not a cost estimate."""
    assert impact_bps(1e9, 1e-6, cap_bps=1000.0) == 1000.0


def test_impact_is_nan_without_a_lambda():
    assert np.isnan(impact_bps(100_000, float("nan")))


def test_rolling_lambda_is_point_in_time():
    """No centring: the value at t uses only data up to t."""
    rng = np.random.default_rng(5)
    idx = pd.date_range("2022-01-01", periods=120, freq="B")
    returns = pd.Series(rng.normal(0, 0.02, 120), index=idx)
    turnover = pd.Series(np.full(120, 5e6), index=idx)
    lam = rolling_lambda(returns, turnover, window=60)

    truncated = rolling_lambda(returns.iloc[:80], turnover.iloc[:80], window=60)
    assert lam.iloc[79] == pytest.approx(truncated.iloc[79]), (
        "a rolling estimate that changes when future data is added is not PIT"
    )


def test_panel_lambda_covers_every_name():
    idx = pd.date_range("2022-01-01", periods=100, freq="B")
    returns = pd.DataFrame({"A": 0.01, "B": 0.02}, index=idx)
    turnover = pd.DataFrame({"A": 1e7, "B": 1e6}, index=idx)
    lam = panel_lambda(returns, turnover)
    assert set(lam.index) == {"A", "B"}
    assert lam["B"] > lam["A"]


# ===========================================================================
# §9 participation and liquidation
# ===========================================================================

def test_participation_constraint_rejects_oversized_trades():
    assert violates_participation(600_000, 10_000_000, 5.0) is True
    assert violates_participation(400_000, 10_000_000, 5.0) is False


def test_participation_rejects_names_that_do_not_trade():
    assert violates_participation(1_000, 0.0, 5.0) is True


def test_days_to_liquidate_matches_by_hand():
    # ₹1,000,000 position, ₹10,000,000 ADV, 5% cap -> ₹500,000/day -> 2 days
    assert days_to_liquidate(1_000_000, 10_000_000, 5.0) == pytest.approx(2.0)
    assert days_to_liquidate(1_000, 0.0) == float("inf")


# ===========================================================================
# spread estimation
# ===========================================================================

def test_corwin_schultz_detects_a_wider_spread():
    rng = np.random.default_rng(9)
    mid = 100 * np.exp(np.cumsum(rng.normal(0, 0.01, 200)))
    tight = pd.Series(mid * 1.001), pd.Series(mid * 0.999)
    wide = pd.Series(mid * 1.02), pd.Series(mid * 0.98)
    assert corwin_schultz_spread(*wide) > corwin_schultz_spread(*tight)


def test_spread_is_capped_and_floored():
    rng = np.random.default_rng(2)
    mid = 100 * np.exp(np.cumsum(rng.normal(0, 0.10, 100)))
    assert 10.0 <= spread_bps(pd.Series(mid * 1.5), pd.Series(mid * 0.5)) <= 500.0


def test_spread_handles_too_little_data():
    assert spread_bps(pd.Series([100.0]), pd.Series([99.0])) == 10.0
