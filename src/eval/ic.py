"""Information coefficient and its decay (§10.2).

Spearman rank IC per rebalance date against forward returns at the declared
horizon. The reported t-statistic uses the autocorrelation-adjusted standard
error, because IC series built from overlapping forward windows are strongly
autocorrelated and the naive t-statistic on such a series is inflated — at
quarterly rebalancing with a six-month horizon, typically by a factor of two.

The decay curve is diagnostic rather than decorative: a factor whose IC is
large at one month and gone by three is a trading signal that cannot survive
quarterly rebalancing plus costs, and that shows up here before it shows up in
a portfolio backtest.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

import numpy as np
import pandas as pd
from scipy import stats as sps

from src.eval.stats import newey_west_tstat


@dataclass
class ICResult:
    """IC time series and its summary statistics."""

    horizon_days: int
    series: pd.Series
    mean: float
    std: float
    t_stat: float
    p_value: float
    hit_rate: float
    n_periods: int
    mean_breadth: float

    @property
    def information_ratio(self) -> float:
        """IC mean / IC std — the stability of the signal, not its size."""
        return float(self.mean / self.std) if self.std > 0 else float("nan")

    def summary(self) -> dict[str, Any]:
        return {
            "horizon_days": self.horizon_days,
            "mean_ic": self.mean,
            "ic_std": self.std,
            "t_stat_nw": self.t_stat,
            "p_value": self.p_value,
            "hit_rate": self.hit_rate,
            "n_periods": self.n_periods,
            "mean_breadth": self.mean_breadth,
            "information_ratio": self.information_ratio,
        }


def spearman_ic(scores: pd.Series, forward: pd.Series) -> tuple[float, int]:
    """Rank IC for one cross-section. Returns (ic, breadth)."""
    frame = pd.DataFrame({"s": scores, "f": forward}).dropna()
    if len(frame) < 5:
        return float("nan"), len(frame)
    # Constant scores have no ranking; scipy returns NaN with a warning, and
    # NaN is the right answer.
    if frame["s"].nunique() < 2 or frame["f"].nunique() < 2:
        return float("nan"), len(frame)
    ic = sps.spearmanr(frame["s"], frame["f"]).statistic
    return float(ic), len(frame)


def pearson_ic(scores: pd.Series, forward: pd.Series) -> tuple[float, int]:
    frame = pd.DataFrame({"s": scores, "f": forward}).dropna()
    if len(frame) < 5 or frame["s"].nunique() < 2 or frame["f"].nunique() < 2:
        return float("nan"), len(frame)
    return float(np.corrcoef(frame["s"], frame["f"])[0, 1]), len(frame)


def ic_series(
    scores_by_date: Mapping[str, pd.Series],
    forwards_by_date: Mapping[str, pd.Series],
    *,
    method: str = "spearman",
) -> tuple[pd.Series, pd.Series]:
    """IC and breadth per rebalance date."""
    fn = spearman_ic if method == "spearman" else pearson_ic
    ics, breadths = {}, {}
    for date in sorted(set(scores_by_date) & set(forwards_by_date)):
        ic, breadth = fn(scores_by_date[date], forwards_by_date[date])
        ics[date] = ic
        breadths[date] = breadth
    return (pd.Series(ics, name="ic", dtype="float64"),
            pd.Series(breadths, name="breadth", dtype="float64"))


def evaluate_ic(
    scores_by_date: Mapping[str, pd.Series],
    forwards_by_date: Mapping[str, pd.Series],
    horizon_days: int,
    *,
    method: str = "spearman",
    newey_west_lags: int | None = None,
) -> ICResult:
    """Full IC evaluation for one horizon."""
    ics, breadths = ic_series(scores_by_date, forwards_by_date, method=method)
    clean = ics.dropna()

    mean, t_stat = newey_west_tstat(clean, lags=newey_west_lags)
    std = float(clean.std(ddof=1)) if len(clean) > 1 else float("nan")
    p_value = (float(2.0 * (1.0 - sps.norm.cdf(abs(t_stat))))
               if np.isfinite(t_stat) else float("nan"))
    hit_rate = float((clean > 0).mean()) if len(clean) else float("nan")

    return ICResult(
        horizon_days=horizon_days, series=ics, mean=float(mean) if np.isfinite(mean) else float("nan"),
        std=std, t_stat=t_stat, p_value=p_value, hit_rate=hit_rate,
        n_periods=len(clean),
        mean_breadth=float(breadths.reindex(clean.index).mean()) if len(clean) else 0.0,
    )


def ic_decay(
    scores_by_date: Mapping[str, pd.Series],
    forwards_by_horizon: Mapping[int, Mapping[str, pd.Series]],
    *,
    method: str = "spearman",
) -> pd.DataFrame:
    """IC across horizons — the decay curve (§10.2).

    A factor with a strong 21-day IC that is flat by 63 days is a signal the
    quarterly rebalance in this platform's default configuration cannot
    harvest. Better to see that here than after a portfolio backtest.
    """
    rows = []
    for horizon in sorted(forwards_by_horizon):
        result = evaluate_ic(scores_by_date, forwards_by_horizon[horizon],
                             horizon, method=method)
        rows.append(result.summary())
    return pd.DataFrame(rows)


def ic_autocorrelation(ics: pd.Series, max_lag: int = 6) -> pd.Series:
    """Autocorrelation of the IC series — the justification for the NW adjustment."""
    clean = pd.Series(ics).dropna()
    if len(clean) < 4:
        return pd.Series(dtype="float64")
    return pd.Series(
        {lag: float(clean.autocorr(lag)) for lag in range(1, min(max_lag, len(clean) - 2) + 1)},
        name="ic_autocorrelation",
    )
