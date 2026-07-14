"""Analytics pass orchestrator — P2/P3/P4/P6/P8 state, computed per CI run.

Runs after fetch (fresh prices) and before digest/overnight (consumers).
Each stage fail-soft: one failure never blocks the rest.

Run: python analytics.py
"""
from __future__ import annotations

import sys
import traceback

import pandas as pd

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def main() -> int:
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()

    for label, runner in (
        ("conditional", lambda: __import__("conditional").build_conditional(prices)),
        ("factors",     lambda: __import__("factors").build_factor_state(prices)),
        ("assumptions", lambda: __import__("assumptions").score_assumptions(prices)),
        ("regime",      lambda: __import__("regime").build_regime(prices)),
        ("spreads",     lambda: __import__("spreads").build_spreads(prices)),
        ("leadlag",     lambda: __import__("leadlag").build_setups(prices)),
        ("scorecard",   lambda: __import__("scorecard").evaluate(prices)),
        ("anomalies",   lambda: __import__("anomalies_json").build_anomalies()),
    ):
        try:
            st = runner()
            n = len(st.get("series", st.get("assumptions", st.get("records", [])))) \
                if isinstance(st, dict) else "?"
            extra = f" label={st.get('label')}" if label == "regime" else ""
            print(f"analytics/{label}: ok ({n}){extra}")
        except Exception:
            print(f"WARN analytics/{label} failed:\n"
                  + traceback.format_exc()[-400:], file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
