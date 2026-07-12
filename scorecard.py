"""P9 stub — signal-type hit-rate ledger (validation harness).

Contract (TODO):
  - Every digest's anomaly records (anomalies.json) are archived with their
    generation date (already true: data files are committed per run — the
    git history IS the point-in-time archive).
  - evaluate(as_of, horizon) replays past records against realised forward
    moves: did `unexplained` residual anomalies mean-revert? did emitted
    transmission setups transmit within N days? did suppressed-channel calls
    stay quiet?
  - Realised precision per signal TYPE (residual-reversion, transmission,
    spread-reversion, assumption-break) is stored here and used to WEIGHT
    future scores + printed on every record ("this signal type: 61% hit rate,
    n=38"). A 45% hit-rate thesis must say so.

Storage: data/scorecard.json {signal_type: {n, hits, precision, updated}}.
"""
from __future__ import annotations


def evaluate(as_of: str, horizon_days: int = 5) -> dict:
    raise NotImplementedError("P9: replay archived anomaly records against "
                              "realised forward returns — see docstring.")
