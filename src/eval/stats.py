"""Statistical protocol (§11).

This module exists because the default failure mode of factor research is
finding something. Four defences, all mandatory rather than optional:

1. **Effective sample size.** Firing counts are not observations. 400
   cross-sectionally correlated stocks are not 400 independent bets, and a
   t-statistic computed on raw N overstates significance by roughly the square
   root of the ratio. Every t-statistic here takes effective N.

2. **Multiple testing.** Every factor–specification pair ever evaluated in this
   repo is recorded in a persistent registry and counts against the
   Benjamini-Hochberg correction, including the ones you would rather forget.
   The registry cannot be deleted from — a trigger enforces it.

3. **Deflated Sharpe.** Bailey & López de Prado (2014). The expected maximum
   Sharpe under the null grows with the number of trials; a Sharpe that beats
   an uncorrected threshold and fails the deflated one is reported as NOT
   SIGNIFICANT with both numbers shown.

4. **No optional stopping.** The evaluation window comes from the
   pre-registration, and the harness refuses to run on a different one unless
   an extension was registered before results were viewed.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass, field
from typing import Any, Sequence

import numpy as np
import pandas as pd
from scipy import stats as sps

EULER_MASCHERONI = 0.5772156649015329


# ---------------------------------------------------------------------------
# Effective sample size
# ---------------------------------------------------------------------------

def effective_n_from_correlation(correlation: np.ndarray | pd.DataFrame) -> float:
    """Effective number of independent bets from a correlation matrix.

    Uses the participation ratio of the eigenvalue spectrum:

        N_eff = (Σ λ_i)² / Σ λ_i²

    which equals N for a perfectly diagonal matrix and 1 when everything moves
    together. Preferred over the average-correlation formula because it
    responds to the *structure* of the correlation — a market with one dominant
    factor and otherwise independent names is correctly scored as low, where
    the average-correlation version can be fooled by offsetting positive and
    negative pairs.
    """
    matrix = np.asarray(
        correlation.to_numpy() if isinstance(correlation, pd.DataFrame) else correlation,
        dtype=float,
    )
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("correlation must be a square matrix")
    if matrix.shape[0] == 0:
        return 0.0
    matrix = np.nan_to_num(matrix, nan=0.0)
    np.fill_diagonal(matrix, 1.0)

    eigenvalues = np.linalg.eigvalsh(matrix)
    eigenvalues = np.clip(eigenvalues, 0.0, None)
    denominator = float((eigenvalues ** 2).sum())
    if denominator <= 0:
        return float(matrix.shape[0])
    return float((eigenvalues.sum() ** 2) / denominator)


def effective_n_from_exposures(exposures: pd.DataFrame) -> float:
    """Effective independent bets from a panel of factor exposures.

    `exposures` is index=date, columns=isin. §11 asks for the effective number
    of independent bets computed from the cross-sectional correlation structure
    of the exposures, which is what this does.
    """
    usable = exposures.dropna(axis=1, how="all")
    # A name with almost no history contributes a correlation estimated from a
    # handful of points, which is noise that inflates apparent independence.
    usable = usable.loc[:, usable.notna().sum() >= 3]
    if usable.shape[1] <= 1:
        return float(usable.shape[1])
    corr = usable.corr(min_periods=3)
    return effective_n_from_correlation(corr.fillna(0.0))


def newey_west_tstat(series: pd.Series | np.ndarray, lags: int | None = None
                     ) -> tuple[float, float]:
    """Mean and t-statistic with an autocorrelation-adjusted standard error.

    §10.2 requires the IC t-statistic be computed on the autocorrelation-
    adjusted standard error. IC series from overlapping forward-return windows
    are strongly autocorrelated, and the naive t-statistic on such a series is
    inflated — often by a factor of two or more at quarterly rebalancing with
    a 6-month horizon.

    Lag length defaults to the Newey-West rule of thumb, 4(T/100)^(2/9).
    """
    values = np.asarray(pd.Series(series).dropna(), dtype=float)
    n = len(values)
    if n < 3:
        return (float(values.mean()) if n else float("nan"), float("nan"))

    mean = float(values.mean())
    demeaned = values - mean
    if lags is None:
        lags = int(np.floor(4.0 * (n / 100.0) ** (2.0 / 9.0)))
    lags = max(0, min(lags, n - 1))

    gamma0 = float((demeaned @ demeaned) / n)
    variance = gamma0
    for lag in range(1, lags + 1):
        gamma = float((demeaned[lag:] @ demeaned[:-lag]) / n)
        weight = 1.0 - lag / (lags + 1.0)  # Bartlett kernel
        variance += 2.0 * weight * gamma
    if variance <= 0:
        return mean, float("nan")
    se = np.sqrt(variance / n)
    return mean, float(mean / se) if se > 0 else float("nan")


def tstat_with_effective_n(mean: float, sd: float, effective_n: float) -> float:
    """t-statistic using effective rather than raw N (§11)."""
    if effective_n <= 1 or sd <= 0 or not np.isfinite(sd):
        return float("nan")
    return float(mean / (sd / np.sqrt(effective_n)))


# ---------------------------------------------------------------------------
# Multiple testing
# ---------------------------------------------------------------------------

def benjamini_hochberg(p_values: Sequence[float], q: float = 0.10) -> dict[str, Any]:
    """Step-up BH procedure controlling FDR at `q`."""
    p = np.asarray([v for v in p_values], dtype=float)
    n = len(p)
    if n == 0:
        return {"reject": [], "threshold": None, "q": q, "n": 0, "n_rejected": 0}
    finite = np.isfinite(p)
    p_clean = np.where(finite, p, 1.0)

    order = np.argsort(p_clean)
    ranked = p_clean[order]
    critical = q * (np.arange(1, n + 1) / n)
    below = ranked <= critical
    k = int(np.max(np.nonzero(below)[0]) + 1) if below.any() else 0
    threshold = float(ranked[k - 1]) if k else None
    reject = (p_clean <= threshold) & finite if threshold is not None else np.zeros(n, bool)
    return {
        "reject": reject.tolist(), "threshold": threshold, "q": q, "n": n,
        "n_rejected": int(reject.sum()),
    }


def deflated_sharpe_ratio(
    observed_sharpe: float,
    *,
    n_trials: int,
    n_observations: int,
    skew: float = 0.0,
    kurtosis: float = 3.0,
    sharpe_variance: float | None = None,
) -> dict[str, float]:
    """Bailey & López de Prado (2014) deflated Sharpe ratio.

    Returns the probability that the observed Sharpe exceeds what the best of
    `n_trials` random strategies would produce under the null of zero true
    skill. Below ~0.95 the result is not significant however good the raw
    number looks.

    Sharpe ratios here are per-period (not annualised); annualising before
    deflating overstates significance because the T in the formula counts
    observations, not years.
    """
    if n_observations < 2 or n_trials < 1:
        return {"deflated_sharpe": float("nan"), "expected_max_sharpe": float("nan"),
                "n_trials": float(n_trials)}

    # Expected maximum Sharpe under the null across n_trials independent trials.
    variance = sharpe_variance if sharpe_variance is not None else 1.0 / n_observations
    sd = np.sqrt(max(variance, 1e-12))
    if n_trials == 1:
        expected_max = 0.0
    else:
        z1 = sps.norm.ppf(1.0 - 1.0 / n_trials)
        z2 = sps.norm.ppf(1.0 - 1.0 / (n_trials * np.e))
        expected_max = float(sd * ((1.0 - EULER_MASCHERONI) * z1
                                   + EULER_MASCHERONI * z2))

    denominator = 1.0 - skew * observed_sharpe + \
        ((kurtosis - 1.0) / 4.0) * observed_sharpe ** 2
    if denominator <= 0:
        return {"deflated_sharpe": float("nan"), "expected_max_sharpe": expected_max,
                "n_trials": float(n_trials)}

    statistic = ((observed_sharpe - expected_max) * np.sqrt(n_observations - 1)
                 / np.sqrt(denominator))
    return {
        "deflated_sharpe": float(sps.norm.cdf(statistic)),
        "expected_max_sharpe": expected_max,
        "n_trials": float(n_trials),
    }


def sharpe_ratio(returns: pd.Series, periods_per_year: int = 252) -> dict[str, float]:
    """Per-period and annualised Sharpe, with the moments the deflation needs."""
    values = pd.Series(returns).dropna()
    if len(values) < 2:
        return {"sharpe": float("nan"), "annualised": float("nan"),
                "skew": float("nan"), "kurtosis": float("nan"), "n": float(len(values))}
    sd = float(values.std(ddof=1))
    per_period = float(values.mean() / sd) if sd > 0 else float("nan")
    return {
        "sharpe": per_period,
        "annualised": per_period * np.sqrt(periods_per_year) if np.isfinite(per_period)
        else float("nan"),
        "skew": float(sps.skew(values)),
        "kurtosis": float(sps.kurtosis(values, fisher=False)),
        "n": float(len(values)),
    }


# ---------------------------------------------------------------------------
# Persistent trial registry (§11)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Trial:
    prereg_hash: str
    factor_name: str
    spec_fingerprint: str
    universe_tier: str
    window_start: str
    window_end: str
    horizon_days: int
    p_value: float | None = None
    sharpe: float | None = None
    effective_n: float | None = None


class TrialRegistry:
    """Every factor–specification pair ever evaluated, persisted across runs.

    The count matters more than any individual row: it is the N in the
    multiple-testing correction, and it is the number that makes the difference
    between "we found a factor" and "we looked eighty times".

    Deletion is blocked by a database trigger. Removing an inconvenient trial
    would understate the correction, and doing so accidentally is easy enough
    that it should not be possible.
    """

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def record(self, trial: Trial) -> int:
        self.conn.execute(
            "INSERT INTO trial_registry (prereg_hash, factor_name, spec_fingerprint,"
            " universe_tier, window_start, window_end, horizon_days, p_value,"
            " sharpe, effective_n, run_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            " ON CONFLICT(prereg_hash, factor_name, spec_fingerprint, window_start,"
            " window_end, horizon_days) DO UPDATE SET"
            "   p_value=excluded.p_value, sharpe=excluded.sharpe,"
            "   effective_n=excluded.effective_n, run_at=excluded.run_at",
            (trial.prereg_hash, trial.factor_name, trial.spec_fingerprint,
             trial.universe_tier, trial.window_start, trial.window_end,
             trial.horizon_days, trial.p_value, trial.sharpe, trial.effective_n,
             dt.datetime.now(tz=dt.timezone.utc).isoformat()),
        )
        return self.count()

    def count(self) -> int:
        return int(self.conn.execute(
            "SELECT COUNT(*) c FROM trial_registry").fetchone()["c"])

    def all_trials(self) -> pd.DataFrame:
        return pd.read_sql_query(
            "SELECT * FROM trial_registry ORDER BY trial_id", self.conn)

    def fdr_status(self, q: float = 0.10) -> pd.DataFrame:
        """BH correction across the whole registry, not just this run.

        §11: "Apply Benjamini-Hochberg FDR control across that full set." A
        correction applied only within one run is not a correction — it is the
        same p-hacking with an extra step.
        """
        trials = self.all_trials()
        if trials.empty:
            return trials
        result = benjamini_hochberg(trials["p_value"].tolist(), q=q)
        trials["bh_significant"] = result["reject"]
        trials["bh_threshold"] = result["threshold"]
        trials["n_trials_total"] = result["n"]
        return trials


@dataclass
class SignificanceVerdict:
    """The §11 verdict, holding both numbers so neither can be quoted alone."""

    factor_name: str
    raw_p_value: float
    raw_significant: bool
    bh_threshold: float | None
    bh_significant: bool
    deflated_sharpe: float
    observed_sharpe: float
    expected_max_sharpe: float
    n_trials: int
    effective_n: float
    raw_n: float

    @property
    def significant(self) -> bool:
        """Significant only if it survives BOTH corrections."""
        return bool(self.bh_significant and self.deflated_sharpe >= 0.95)

    @property
    def verdict(self) -> str:
        return "SIGNIFICANT" if self.significant else "NOT SIGNIFICANT"

    def summary(self) -> str:
        """§11: both numbers shown, always. A factor clearing the uncorrected
        threshold and failing the corrected one is reported as NOT SIGNIFICANT
        with the uncorrected figure visible next to it."""
        lines = [
            f"{self.factor_name}: {self.verdict}",
            f"  uncorrected p       = {self.raw_p_value:.4f} "
            f"({'passes' if self.raw_significant else 'fails'} at 0.05)",
            f"  BH threshold        = "
            + (f"{self.bh_threshold:.4f}" if self.bh_threshold is not None else "none")
            + f"  across {self.n_trials} registered trials "
            f"({'passes' if self.bh_significant else 'fails'})",
            f"  observed Sharpe     = {self.observed_sharpe:.3f}",
            f"  expected max Sharpe = {self.expected_max_sharpe:.3f} under the null",
            f"  deflated Sharpe     = {self.deflated_sharpe:.4f} "
            f"({'passes' if self.deflated_sharpe >= 0.95 else 'fails'} at 0.95)",
            f"  N                   = {self.raw_n:.0f} raw, "
            f"{self.effective_n:.1f} effective independent bets",
        ]
        if self.raw_significant and not self.significant:
            lines.append(
                "  NOTE: this factor clears the uncorrected threshold and fails "
                "the corrected one. That is the expected behaviour of noise "
                "under repeated testing, not a near miss."
            )
        return "\n".join(lines)
