"""P7 — false-discovery control (BH implemented; scan wiring TODO).

Scanning ~90 instruments x several descriptors each run manufactures
"anomalies" at naive thresholds. Benjamini-Hochberg controls the expected
false-discovery rate across the scan.

Implemented: benjamini_hochberg() with known-answer tests. TODO (P7
remainder): map zc / resid_z to p-values (two-sided normal as first
approximation, empirical-quantile p as upgrade), run BH across each digest's
candidate set, and attach `bh_significant` + the effective threshold to the
anomaly records + digest.
"""
from __future__ import annotations

import numpy as np


def benjamini_hochberg(pvals: list[float], q: float = 0.10) -> dict:
    """Classic step-up BH. Returns rejection mask + the largest significant
    p (the effective threshold), controlling FDR at q."""
    p = np.asarray(pvals, dtype=float)
    n = len(p)
    if n == 0:
        return {"reject": [], "threshold": None, "q": q, "n": 0}
    order = np.argsort(p)
    ranked = p[order]
    crit = q * (np.arange(1, n + 1) / n)
    below = ranked <= crit
    k = int(np.max(np.nonzero(below)[0]) + 1) if below.any() else 0
    thr = float(ranked[k - 1]) if k else None
    reject = p <= thr if thr is not None else np.zeros(n, dtype=bool)
    return {"reject": reject.tolist(), "threshold": thr, "q": q, "n": n,
            "n_rejected": int(reject.sum())}


def z_to_p(z: float) -> float:
    """Two-sided normal p-value for a z-score (first-pass mapping; the
    empirical-quantile upgrade is the P7 TODO)."""
    from math import erf, sqrt
    return 2.0 * (1.0 - 0.5 * (1.0 + erf(abs(z) / sqrt(2.0))))
