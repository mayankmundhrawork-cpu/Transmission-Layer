"""Quantile portfolios, turnover, and cost drag (§10.3, §10.4).

Two things here are non-negotiable per the spec:

**Long-only spread is the headline (§10.4).** Shorting Indian smallcaps is not
practically available — SLB borrow is thin to nonexistent below the F&O
universe, and the F&O universe is not the smallcap tier. So the primary
statistic is top-quantile-minus-benchmark. Long-short is computed and reported
as secondary, and where the two diverge sharply the report says explicitly that
the premium lives in the short leg and is not accessible.

**Net of cost, always (§11).** Gross series are computed because the
decomposition is informative, but `headline_return` returns the net series and
there is no code path that makes a gross figure the headline.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

import numpy as np
import pandas as pd


@dataclass
class QuantileResult:
    """Quantile portfolio returns and their cost decomposition."""

    n_quantiles: int
    gross_returns: pd.DataFrame     # index=date, columns=quantile
    net_returns: pd.DataFrame
    turnover: pd.DataFrame
    cost_drag: pd.DataFrame
    weights_by_date: dict[str, dict[int, pd.Series]] = field(default_factory=dict)
    benchmark: pd.Series | None = None
    weighting: str = "equal"

    # -- primary statistic (§10.4) ----------------------------------------

    @property
    def top_quantile(self) -> int:
        return self.n_quantiles

    def long_only_spread(self, net: bool = True) -> pd.Series:
        """Top quantile minus benchmark — THE headline statistic (§10.4)."""
        returns = self.net_returns if net else self.gross_returns
        top = returns[self.top_quantile]
        if self.benchmark is None:
            return top.rename("long_only_excess")
        aligned = self.benchmark.reindex(top.index)
        return (top - aligned).rename("long_only_excess")

    def long_short(self, net: bool = True) -> pd.Series:
        """Top minus bottom. SECONDARY — not practically available here."""
        returns = self.net_returns if net else self.gross_returns
        return (returns[self.top_quantile] - returns[1]).rename("long_short")

    def short_leg_contribution(self) -> float:
        """Fraction of the long-short premium coming from the short leg.

        §10.4: where long-only and long-short diverge sharply, the premium
        lives in the short leg and is not accessible. This quantifies "sharply"
        so the report does not have to hand-wave it.
        """
        ls = self.long_short().mean()
        lo = self.long_only_spread().mean()
        if not np.isfinite(ls) or ls == 0:
            return float("nan")
        return float((ls - lo) / ls)

    def headline_return(self) -> pd.Series:
        """The number that goes at the top of a report: net, long-only, excess."""
        return self.long_only_spread(net=True)

    def summary(self) -> dict[str, Any]:
        long_only = self.long_only_spread()
        return {
            "n_quantiles": self.n_quantiles,
            "weighting": self.weighting,
            "periods": int(len(self.net_returns)),
            "mean_long_only_excess_net": float(long_only.mean()),
            "mean_long_short_net": float(self.long_short().mean()),
            "mean_long_short_gross": float(self.long_short(net=False).mean()),
            "short_leg_contribution": self.short_leg_contribution(),
            "mean_turnover_top": float(self.turnover[self.top_quantile].mean()),
            "mean_cost_drag_top": float(self.cost_drag[self.top_quantile].mean()),
        }


def assign_quantiles(scores: pd.Series, n_quantiles: int) -> pd.Series:
    """Rank into 1..n_quantiles, 1 = lowest score.

    Uses ranks rather than value cuts so a skewed factor still yields balanced
    buckets — value factors in this universe are heavily right-skewed and
    equal-width bins would put 80% of names in one bucket.
    """
    clean = scores.dropna()
    if len(clean) < n_quantiles:
        return pd.Series(dtype="float64", index=scores.index)
    ranks = clean.rank(method="first")
    buckets = np.ceil(ranks * n_quantiles / len(ranks)).clip(1, n_quantiles)
    return buckets.reindex(scores.index)


def portfolio_weights(
    members: pd.Index, weighting: str = "equal",
    float_caps: pd.Series | None = None,
) -> pd.Series:
    """Weights within one quantile bucket."""
    if len(members) == 0:
        return pd.Series(dtype="float64")
    if weighting == "equal":
        return pd.Series(1.0 / len(members), index=members)
    if weighting == "float":
        if float_caps is None:
            raise ValueError("float weighting requires float_caps")
        caps = float_caps.reindex(members).astype(float)
        caps = caps.where(caps > 0)
        total = caps.sum()
        if not np.isfinite(total) or total <= 0:
            return pd.Series(1.0 / len(members), index=members)
        return (caps / total).fillna(0.0)
    raise ValueError(f"unknown weighting {weighting!r}; expected 'equal' or 'float'")


def compute_turnover(previous: pd.Series | None, current: pd.Series) -> float:
    """One-way turnover between two weight vectors, in [0, 1].

    Half the sum of absolute weight changes: buying 100% of a new portfolio and
    selling 100% of the old is 100% one-way turnover, not 200%.
    """
    if previous is None or previous.empty:
        return 1.0 if len(current) else 0.0
    combined = previous.reindex(previous.index.union(current.index)).fillna(0.0)
    target = current.reindex(combined.index).fillna(0.0)
    return float((target - combined).abs().sum() / 2.0)


def quantile_portfolios(
    scores_by_date: Mapping[str, pd.Series],
    forwards_by_date: Mapping[str, pd.Series],
    *,
    n_quantiles: int = 5,
    weighting: str = "equal",
    float_caps_by_date: Mapping[str, pd.Series] | None = None,
    cost_bps_round_trip: float = 100.0,
    benchmark_by_date: Mapping[str, float] | None = None,
) -> QuantileResult:
    """Build quantile portfolios and their gross/net return series.

    `cost_bps_round_trip` is applied as `turnover x cost`, which charges the
    portion of the book actually traded. Charging the full round-trip cost on
    100% of the book every period would overstate drag; charging nothing would
    understate it to zero, which §18.6 forbids.
    """
    dates = sorted(set(scores_by_date) & set(forwards_by_date))
    quantiles = list(range(1, n_quantiles + 1))
    gross_rows, net_rows, turnover_rows, cost_rows = [], [], [], []
    previous: dict[int, pd.Series] = {}
    weights_by_date: dict[str, dict[int, pd.Series]] = {}

    for date in dates:
        scores = scores_by_date[date]
        forward = forwards_by_date[date]
        buckets = assign_quantiles(scores, n_quantiles)
        if buckets.dropna().empty:
            continue

        caps = float_caps_by_date.get(date) if float_caps_by_date else None
        gross, net, turns, costs = {}, {}, {}, {}
        weights_by_date[date] = {}

        for q in quantiles:
            members = buckets[buckets == q].index
            members = members.intersection(forward.dropna().index)
            if len(members) == 0:
                gross[q] = net[q] = np.nan
                turns[q] = costs[q] = np.nan
                continue

            weights = portfolio_weights(members, weighting, caps)
            weights_by_date[date][q] = weights

            period_return = float((weights * forward.reindex(members)).sum())
            turnover = compute_turnover(previous.get(q), weights)
            drag = turnover * cost_bps_round_trip / 1e4

            gross[q] = period_return
            turns[q] = turnover
            costs[q] = drag
            net[q] = period_return - drag
            previous[q] = weights

        gross_rows.append(pd.Series(gross, name=date))
        net_rows.append(pd.Series(net, name=date))
        turnover_rows.append(pd.Series(turns, name=date))
        cost_rows.append(pd.Series(costs, name=date))

    def frame(rows):
        return (pd.DataFrame(rows).reindex(columns=quantiles) if rows
                else pd.DataFrame(columns=quantiles))

    benchmark = None
    if benchmark_by_date is not None:
        benchmark = pd.Series(
            {d: benchmark_by_date.get(d, np.nan) for d in dates}, dtype="float64"
        ).reindex([r.name for r in net_rows])

    return QuantileResult(
        n_quantiles=n_quantiles, gross_returns=frame(gross_rows),
        net_returns=frame(net_rows), turnover=frame(turnover_rows),
        cost_drag=frame(cost_rows), weights_by_date=weights_by_date,
        benchmark=benchmark, weighting=weighting,
    )


def fama_macbeth(
    scores_by_date: Mapping[str, pd.Series],
    forwards_by_date: Mapping[str, pd.Series],
    controls_by_date: Mapping[str, pd.DataFrame] | None = None,
) -> dict[str, Any]:
    """Fama-MacBeth cross-sectional regressions with the declared controls (§10.5).

    Period-by-period cross-sectional regressions, then a time-series t-test on
    the coefficient series — using the autocorrelation-adjusted standard error,
    since overlapping forward windows make the coefficient series serially
    correlated just as they do the IC.
    """
    from src.eval.stats import newey_west_tstat

    coefficients: dict[str, dict[str, float]] = {}
    for date in sorted(set(scores_by_date) & set(forwards_by_date)):
        frame = pd.DataFrame({"score": scores_by_date[date],
                              "forward": forwards_by_date[date]})
        if controls_by_date and date in controls_by_date:
            frame = frame.join(controls_by_date[date], how="left")
        frame = frame.dropna()
        if len(frame) < 10:
            continue

        y = frame.pop("forward").to_numpy()
        names = list(frame.columns)
        X = np.column_stack([np.ones(len(frame)), frame.to_numpy()])
        try:
            beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        except np.linalg.LinAlgError:
            continue
        coefficients[date] = dict(zip(["intercept", *names], beta))

    if not coefficients:
        return {"n_periods": 0, "coefficients": {}}

    panel = pd.DataFrame(coefficients).T
    out: dict[str, Any] = {"n_periods": len(panel), "coefficients": {}}
    for name in panel.columns:
        mean, t_stat = newey_west_tstat(panel[name])
        out["coefficients"][name] = {
            "mean": float(mean), "t_stat_nw": float(t_stat),
            "std": float(panel[name].std(ddof=1)),
        }
    out["series"] = panel
    return out
