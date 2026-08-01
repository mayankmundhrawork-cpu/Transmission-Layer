"""CP5 worked example: a hand-computed round trip, printed in full.

    python -m src.costs.worked_example

§17 CP5 asks for the cost model to reproduce a hand computation on a worked
example printed in full. The arithmetic below is done by hand in the comments;
`tests/platform/test_costs.py` asserts the model against these same constants,
so a rate change that alters the answer fails a test rather than silently
shifting every backtest.
"""
from __future__ import annotations

from src.costs.model import CostModel, rate_table_status

# --- the trade -------------------------------------------------------------
QUANTITY = 100
BUY_PRICE = 500.0
SELL_PRICE = 550.0
BUY_DATE = "2023-06-15"
SELL_DATE = "2023-09-15"
SPREAD_BPS = 40.0   # full spread; half is charged per leg
IMPACT_BPS = 15.0

# --- hand computation, rate table effective 2020-07-01 ---------------------
# STT 0.1% both legs · stamp 0.015% buy only · exchange 0.00325% · SEBI
# 0.0001% · GST 18% on (brokerage + exchange + SEBI + DP) · DP ₹13.50 per
# scrip on the sell · brokerage nil on delivery.
#
# BUY   turnover = 100 x 500 = ₹50,000
#   STT          50,000 x 0.001      =  50.0000
#   stamp        50,000 x 0.00015    =   7.5000
#   exchange     50,000 x 0.0000325  =   1.6250
#   SEBI         50,000 x 0.000001   =   0.0500
#   GST          0.18 x (1.6250 + 0.0500 + 0)  =   0.3015
#   explicit                                    =  59.4765
#   spread       50,000 x 20bps      = 100.0000   (half of 40bps)
#   impact       50,000 x 15bps      =  75.0000
#   TOTAL                                       = 234.4765
#
# SELL  turnover = 100 x 550 = ₹55,000
#   STT          55,000 x 0.001      =  55.0000
#   stamp        (buy leg only)      =   0.0000
#   exchange     55,000 x 0.0000325  =   1.7875
#   SEBI         55,000 x 0.000001   =   0.0550
#   DP           ₹13.50 x 1 scrip    =  13.5000
#   GST          0.18 x (1.7875 + 0.0550 + 13.5000) =   2.7617
#   explicit                                    =  73.1042
#   spread       55,000 x 20bps      = 110.0000
#   impact       55,000 x 15bps      =  82.5000
#   TOTAL                                       = 265.6042
#
# ROUND TRIP = 234.4765 + 265.6042 = ₹500.0806
#            = 1e4 x 500.0806 / 50,000 = 100.02 bps of entry notional
EXPECTED_BUY_TOTAL = 234.4765
EXPECTED_SELL_TOTAL = 265.60415
EXPECTED_ROUND_TRIP = 500.08065
EXPECTED_ROUND_TRIP_BPS = 100.0161


def main() -> int:
    model = CostModel(warn_unverified=False)
    trip = model.round_trip(
        buy_price=BUY_PRICE, sell_price=SELL_PRICE, quantity=QUANTITY,
        buy_date=BUY_DATE, sell_date=SELL_DATE,
        spread_bps=SPREAD_BPS, impact_bps=IMPACT_BPS,
    )

    print(__doc__.strip())
    print()
    print(f"Trade: BUY {QUANTITY} @ ₹{BUY_PRICE:,.2f} on {BUY_DATE}, "
          f"SELL @ ₹{SELL_PRICE:,.2f} on {SELL_DATE}")
    print(f"Spread {SPREAD_BPS:.0f}bps (half per leg), impact {IMPACT_BPS:.0f}bps")
    print()
    print(trip.report())
    print()
    print("Hand computation vs model:")
    for label, expected, actual in [
        ("buy leg", EXPECTED_BUY_TOTAL, trip.buy.total),
        ("sell leg", EXPECTED_SELL_TOTAL, trip.sell.total),
        ("round trip", EXPECTED_ROUND_TRIP, trip.total),
        ("round trip bps", EXPECTED_ROUND_TRIP_BPS, trip.bps),
    ]:
        ok = "OK " if abs(expected - actual) < 1e-3 else "MISMATCH"
        print(f"  {ok}  {label:<16s} hand={expected:>12,.4f}  model={actual:>12,.4f}")

    status = rate_table_status()
    if not status["all_verified"]:
        print()
        print("!" * 70)
        print(f"WARNING: {status['unverified_count']} of {len(status['tables'])} rate "
              "tables are UNVERIFIED against primary sources.")
        print("Every net-of-cost figure this platform produces inherits whatever")
        print("error is in them. See the header of src/costs/rates.yaml.")
        print("!" * 70)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
