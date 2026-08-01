"""Target portfolio construction (§13).

Turns a factor score vector into target weights subject to every constraint in
§13 and §9:

* `MAX_POSITION_PCT` of NAV per name
* `MAX_SECTOR_PCT` per sector
* `MIN_POSITIONS` names held
* the participation constraint — no position larger than a configured fraction
  of trailing median daily traded value
* exclusion of ASM/GSM stage 2+ names

Constraints are enforced by iterated projection: clip the violations,
redistribute the freed weight to names with headroom, repeat. That converges
in a handful of passes and, unlike a one-shot clip-and-renormalise, does not
quietly reintroduce a violation while fixing another.

If the constraints cannot all be met the result says so rather than silently
returning something that violates one. A portfolio that cannot be built is
information — usually that the book is too large for the tier — and turning it
into a plausible-looking weight vector destroys that information.
"""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from typing import Any, Sequence

import numpy as np
import pandas as pd


class ConstructionError(RuntimeError):
    """The declared constraints cannot be satisfied."""


@dataclass(frozen=True)
class Constraints:
    capital_inr: float
    max_position_pct: float = 4.0
    max_sector_pct: float = 25.0
    min_positions: int = 25
    max_participation_pct: float = 5.0
    max_surveillance_stage: int = 1
    #: Names to hold. None = min_positions.
    target_positions: int | None = None

    def describe(self) -> dict[str, Any]:
        return dict(vars(self))


@dataclass
class TargetPortfolio:
    as_of_date: str
    weights: pd.Series           # fraction of NAV, sums to <= 1
    notional: pd.Series          # rupees
    days_to_liquidate: pd.Series
    sectors: pd.Series
    excluded: dict[str, list[str]] = field(default_factory=dict)
    binding_constraints: list[str] = field(default_factory=list)
    cash_weight: float = 0.0

    @property
    def n_positions(self) -> int:
        return int((self.weights > 0).sum())

    def sector_weights(self) -> pd.Series:
        return self.weights.groupby(self.sectors.reindex(self.weights.index)).sum()

    def summary(self) -> dict[str, Any]:
        return {
            "as_of_date": self.as_of_date,
            "n_positions": self.n_positions,
            "invested_weight": float(self.weights.sum()),
            "cash_weight": self.cash_weight,
            "max_position_weight": float(self.weights.max()) if len(self.weights) else 0.0,
            "max_sector_weight": float(self.sector_weights().max())
            if len(self.weights) else 0.0,
            "worst_days_to_liquidate": float(self.days_to_liquidate.max())
            if len(self.days_to_liquidate) else 0.0,
            "binding_constraints": list(self.binding_constraints),
        }


def construct(
    scores: pd.Series,
    *,
    constraints: Constraints,
    sectors: pd.Series,
    median_turnover: pd.Series,
    surveillance_stage: pd.Series | None = None,
    as_of_date: str | dt.date = "",
    higher_is_better: bool = True,
    score_tilt: bool = False,
) -> TargetPortfolio:
    """Build a target weight vector from a score vector.

    `score_tilt=False` (the default) weights held names equally. Tilting by
    score is available but off by default: score-proportional weights are a
    composite with implicit weights, and §2 is explicit that a weighted sum
    whose weights were not fit out-of-sample is not meaningful.
    """
    date = as_of_date if isinstance(as_of_date, str) else as_of_date.isoformat()
    excluded: dict[str, list[str]] = {}
    ranked = scores.dropna()
    if not higher_is_better:
        ranked = -ranked

    # --- eligibility -----------------------------------------------------
    if surveillance_stage is not None:
        stages = surveillance_stage.reindex(ranked.index).fillna(0)
        blocked = ranked.index[stages > constraints.max_surveillance_stage]
        if len(blocked):
            excluded["surveillance_stage_2_plus"] = list(blocked)
            ranked = ranked.drop(blocked)

    adv = median_turnover.reindex(ranked.index).fillna(0.0)
    untradeable = ranked.index[adv <= 0]
    if len(untradeable):
        excluded["no_traded_value"] = list(untradeable)
        ranked = ranked.drop(untradeable)

    if ranked.empty:
        raise ConstructionError(
            f"{date}: no eligible names after exclusions {list(excluded)}"
        )

    n_target = constraints.target_positions or constraints.min_positions
    if len(ranked) < constraints.min_positions:
        raise ConstructionError(
            f"{date}: only {len(ranked)} eligible names but MIN_POSITIONS is "
            f"{constraints.min_positions}. Widen the universe, relax the screens, "
            "or lower MIN_POSITIONS — do not build a more concentrated book by "
            "accident."
        )

    selected = ranked.nlargest(min(n_target, len(ranked)))

    # --- initial weights --------------------------------------------------
    if score_tilt:
        tilt = selected - selected.min() + 1e-9
        weights = tilt / tilt.sum()
    else:
        weights = pd.Series(1.0 / len(selected), index=selected.index)

    # --- constraint caps --------------------------------------------------
    position_cap = constraints.max_position_pct / 100.0
    sector_cap = constraints.max_sector_pct / 100.0
    participation_cap = (
        adv.reindex(selected.index) * constraints.max_participation_pct / 100.0
        / constraints.capital_inr
    )
    per_name_cap = pd.Series(position_cap, index=selected.index).combine(
        participation_cap, min)

    binding: list[str] = []
    if (per_name_cap < position_cap - 1e-12).any():
        binding.append("participation")

    sector_map = sectors.reindex(selected.index).fillna("UNKNOWN")
    weights = _project(weights, per_name_cap, sector_map, sector_cap, binding)

    invested = float(weights.sum())
    if invested < 0.999:
        binding.append("capacity")

    notional = weights * constraints.capital_inr
    dtl = pd.Series({
        isin: (notional[isin] / (adv[isin] * constraints.max_participation_pct / 100.0)
               if adv.get(isin, 0.0) > 0 else float("inf"))
        for isin in weights.index
    })

    return TargetPortfolio(
        as_of_date=date, weights=weights.sort_values(ascending=False),
        notional=notional, days_to_liquidate=dtl, sectors=sector_map,
        excluded=excluded, binding_constraints=sorted(set(binding)),
        cash_weight=max(0.0, 1.0 - invested),
    )


def _project(
    weights: pd.Series, per_name_cap: pd.Series, sectors: pd.Series,
    sector_cap: float, binding: list[str], *, max_iterations: int = 50,
) -> pd.Series:
    """Iteratively clip to the caps and redistribute the freed weight.

    A single clip-and-renormalise would push other names back over their caps;
    iterating to a fixed point is what makes the result actually feasible.
    """
    weights = weights.copy()
    for _ in range(max_iterations):
        changed = False

        over = weights > per_name_cap + 1e-12
        if over.any():
            binding.append("position_cap")
            freed = float((weights[over] - per_name_cap[over]).sum())
            weights[over] = per_name_cap[over]
            weights = _redistribute(weights, per_name_cap, freed)
            changed = True

        sector_totals = weights.groupby(sectors).sum()
        breaching = sector_totals[sector_totals > sector_cap + 1e-12]
        if len(breaching):
            binding.append("sector_cap")
            for sector, total in breaching.items():
                members = sectors.index[sectors == sector]
                scale = sector_cap / total
                freed = float(weights[members].sum() * (1.0 - scale))
                weights[members] = weights[members] * scale
                others = sectors.index[sectors != sector]
                weights = _redistribute(
                    weights, per_name_cap, freed, eligible=others)
            changed = True

        if not changed:
            break
    return weights


def _redistribute(
    weights: pd.Series, caps: pd.Series, amount: float,
    eligible: pd.Index | None = None,
) -> pd.Series:
    """Spread freed weight over names with headroom, proportional to headroom."""
    if amount <= 1e-15:
        return weights
    index = eligible if eligible is not None else weights.index
    headroom = (caps.reindex(index) - weights.reindex(index)).clip(lower=0.0)
    total = float(headroom.sum())
    if total <= 1e-15:
        return weights  # nowhere to put it; the shortfall becomes cash
    weights = weights.copy()
    weights.loc[index] = weights.loc[index] + headroom * (min(amount, total) / total)
    return weights
