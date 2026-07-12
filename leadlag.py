"""P5 stub — lead-lag / transmission verification.

Current substrate: relations.py already computes directional lagged
cross-correlation (1..5 sessions, 252d window) every run, and events/theses
consume it. What P5 adds ON TOP (TODO):

  verify_transmission(driver, target) ->
    {lead_days, ccf_strength, lagged_ols_beta, lagged_ols_p (HAC),
     granger_p (with regime caveat), historically_significant: bool,
     driver_has_moved: bool, target_repriced: bool, emit: bool}

Gate: a "setup" is emitted ONLY when (a) the lagged relationship is
historically significant (lagged OLS with HAC SEs — Granger reported as
evidence with explicit caveats, never the trigger), (b) the driver's zc
cleared its bar, and (c) the target's cumulative response since the driver
move is below the historical response curve.

TODO: implement over relations state + conditional zc; add to the anomaly
record contract; FDR-correct across the setups scanned per run (fdr.py).
"""
from __future__ import annotations


def verify_transmission(driver: str, target: str) -> dict:
    raise NotImplementedError(
        "P5: lagged-OLS/CCF verification over relations-state substrate — "
        "see module docstring for the contract.")
