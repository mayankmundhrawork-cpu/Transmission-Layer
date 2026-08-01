"""Cross-sectional preprocessing (§10.1).

Winsorise, z-score, optionally sector-neutralise. Every choice comes from the
pre-registration — there is no tuning loop here and no default that quietly
becomes a decision.

That is why :class:`PreprocessSpec` has no defaults for the percentiles: a
researcher who has not stated where they winsorise has not stated their
specification, and silently picking 1%/99% would make an unregistered choice on
their behalf and then hide it.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class PreprocessSpec:
    """Declared preprocessing. Comes from a §12 pre-registration."""

    winsorise_lower_pct: float
    winsorise_upper_pct: float
    standardise: bool = True
    sector_neutralise: bool = False
    #: Rank-transform before standardising. Robust to remaining outliers but
    #: discards magnitude, so it is a declared choice rather than a default.
    rank_transform: bool = False

    def __post_init__(self) -> None:
        if not 0.0 <= self.winsorise_lower_pct < self.winsorise_upper_pct <= 100.0:
            raise ValueError(
                f"winsorisation percentiles must satisfy 0 <= lower < upper <= 100, "
                f"got {self.winsorise_lower_pct} and {self.winsorise_upper_pct}"
            )

    def describe(self) -> dict[str, Any]:
        return dict(vars(self))


def winsorise(scores: pd.Series, lower_pct: float, upper_pct: float) -> pd.Series:
    """Clip to the declared percentiles. Percentiles are computed on the
    observed (non-null) cross-section only."""
    valid = scores.dropna()
    if valid.empty:
        return scores
    lo, hi = np.percentile(valid, [lower_pct, upper_pct])
    return scores.clip(lower=lo, upper=hi)


def zscore(scores: pd.Series) -> pd.Series:
    """Standardise cross-sectionally. Zero-variance cross-sections return NaN
    rather than dividing by zero — a factor with no dispersion has no ranking
    to offer and pretending otherwise produces inf."""
    valid = scores.dropna()
    if len(valid) < 2:
        return pd.Series(np.nan, index=scores.index)
    sd = valid.std(ddof=1)
    if not np.isfinite(sd) or sd == 0:
        return pd.Series(np.nan, index=scores.index)
    return (scores - valid.mean()) / sd


def rank_normalise(scores: pd.Series) -> pd.Series:
    """Map to a standard normal via ranks — an inverse-normal transform."""
    from scipy.stats import norm

    valid = scores.dropna()
    if len(valid) < 3:
        return pd.Series(np.nan, index=scores.index)
    ranks = valid.rank(method="average")
    quantiles = ranks / (len(ranks) + 1.0)
    return pd.Series(norm.ppf(quantiles), index=valid.index).reindex(scores.index)


def sector_neutralise(scores: pd.Series, sectors: pd.Series) -> pd.Series:
    """Demean within sector.

    Without this, a value factor in Indian equities is substantially a bet
    against financials, whose book-to-price sits structurally higher than the
    rest of the market. Whether that bet is wanted is a study design question —
    which is why this is declared in the pre-registration and not applied by
    default.

    Sectors with a single name cannot be demeaned meaningfully and become NaN,
    rather than a deterministic zero that would look like a neutral score.
    """
    aligned = sectors.reindex(scores.index)
    known = aligned.notna() & scores.notna()
    if not known.any():
        return pd.Series(np.nan, index=scores.index)

    out = pd.Series(np.nan, index=scores.index, dtype="float64")
    grouped = scores[known].groupby(aligned[known])
    sizes = grouped.transform("size")
    demeaned = scores[known] - grouped.transform("mean")
    out.loc[known] = demeaned.where(sizes >= 2)
    return out


def preprocess(
    scores: pd.Series, spec: PreprocessSpec, sectors: pd.Series | None = None
) -> pd.Series:
    """Apply the declared pipeline, in the declared order."""
    if spec.sector_neutralise and sectors is None:
        raise ValueError(
            "the pre-registration declares sector neutralisation but no sector "
            "map was supplied; running without it would silently change the spec"
        )

    out = winsorise(scores, spec.winsorise_lower_pct, spec.winsorise_upper_pct)
    if spec.rank_transform:
        out = rank_normalise(out)
    if spec.sector_neutralise and sectors is not None:
        out = sector_neutralise(out, sectors)
    if spec.standardise:
        out = zscore(out)
    return out.rename(scores.name)


def forward_returns(
    returns: pd.DataFrame, as_of: pd.Timestamp | str, horizon_days: int
) -> pd.Series:
    """Compound return over the `horizon_days` sessions AFTER `as_of`.

    Strictly after: the as-of session itself is excluded, because a signal
    computed from that day's close cannot capture that day's move. Including it
    is a one-day look-ahead that shows up as a suspiciously strong IC at short
    horizons.
    """
    stamp = pd.Timestamp(as_of)
    future = returns.loc[returns.index > stamp]
    if future.empty:
        return pd.Series(dtype="float64")
    window = future.head(horizon_days)
    # Require most of the horizon present, so a name that delists three days in
    # does not contribute a "3-month return" made of three days.
    enough = window.notna().sum() >= max(int(horizon_days * 0.5), 1)
    compounded = (1.0 + window.fillna(0.0)).prod() - 1.0
    return compounded.where(enough)


def cross_section_frame(
    scores: pd.Series, forward: pd.Series, sectors: pd.Series | None = None
) -> pd.DataFrame:
    """Align a score vector with its forward returns, dropping unusable rows."""
    frame = pd.DataFrame({"score": scores, "forward": forward})
    if sectors is not None:
        frame["sector"] = sectors.reindex(frame.index)
    return frame.dropna(subset=["score", "forward"])
