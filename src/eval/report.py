"""Study report generation (§19).

Reporting style is a specification, not a preference:

* **Result first**, including negative ones, with the pre-registration hash at
  the top.
* **No executive summary that softens a null.** There is no "however" section
  and no place to put one.
* **No code path only exercised on positive results.** The renderer is one
  function with no branch on the verdict — a NO-GO report has exactly the same
  sections, in the same order, as a GO. That property is asserted by a test,
  because it is the one that silently rots first.
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from src.eval.harness import StudyResult
from src.prereg.registry import Preregistration


def render(result: StudyResult, prereg: Preregistration) -> str:
    """Render a study report. Identical structure regardless of the verdict."""
    verdict = result.verdict
    headline = result.headline.dropna()
    summary = result.portfolios.summary()

    lines: list[str] = []
    add = lines.append

    # --- result first (§19) ----------------------------------------------
    add(f"# {result.study_id} — {verdict.verdict}")
    add("")
    add(f"**Pre-registration hash:** `{result.prereg_hash}`  ")
    add(f"**Spec fingerprint:** `{result.spec_fingerprint}`  ")
    add(f"**Factor:** {result.factor_name}  ")
    add(f"**Universe:** {result.universe_tier}  ")
    add(f"**Window:** {result.window[0]} to {result.window[1]} "
        f"({len(result.rebalance_dates)} rebalances, {result.horizon_days}-session horizon)  ")
    add(f"**Generated:** {result.generated_at}")
    add("")
    add("## Result")
    add("")
    add(f"**{verdict.verdict}.**")
    add("")
    add("```")
    add(verdict.summary())
    add("```")
    add("")
    add(f"Headline statistic — net-of-cost long-only excess over the benchmark, "
        f"per {result.horizon_days}-session period:")
    add("")
    add(f"- mean: **{_pct(headline.mean())}**")
    add(f"- std: {_pct(headline.std(ddof=1)) if len(headline) > 1 else 'n/a'}")
    add(f"- periods: {len(headline)}")
    add(f"- cumulative: {_pct((1 + headline.fillna(0)).prod() - 1)}")
    add("")

    # --- warnings, before anything that could be read as a positive ------
    warnings = _warnings(result)
    add("## Warnings")
    add("")
    if warnings:
        for warning in warnings:
            add(f"- {warning}")
    else:
        add("- None.")
    add("")

    # --- hypothesis and interpretation -----------------------------------
    add("## Hypothesis")
    add("")
    add(f"> {prereg.hypothesis}")
    add("")
    add("## What this result rules out, and what it does not")
    add("")
    asymmetry = prereg.interpretation_asymmetry
    add(f"**A null result rules out:** {asymmetry.get('null_result_rules_out', 'not declared')}")
    add("")
    add(f"**A null result does NOT rule out:** "
        f"{asymmetry.get('null_result_does_not_rule_out', 'not declared')}")
    add("")
    if asymmetry.get("positive_result_does_not_establish"):
        add(f"**A positive result does not establish:** "
            f"{asymmetry['positive_result_does_not_establish']}")
        add("")

    # --- IC ---------------------------------------------------------------
    add("## Information coefficient")
    add("")
    ic = result.ic
    add(f"- mean rank IC: **{ic.mean:.4f}**")
    add(f"- Newey-West t-statistic: **{ic.t_stat:.2f}** (p = {ic.p_value:.4f})")
    add(f"- IC std: {ic.std:.4f}, information ratio: {ic.information_ratio:.3f}")
    add(f"- hit rate: {_pct(ic.hit_rate)} of periods positive")
    add(f"- mean breadth: {ic.mean_breadth:.0f} names per cross-section")
    add("")
    if not result.ic_autocorrelation.empty:
        ac = result.ic_autocorrelation
        add(f"IC autocorrelation (lag 1: {ac.iloc[0]:.2f}) is why the t-statistic "
            "above uses the autocorrelation-adjusted standard error; the naive "
            "figure would be materially larger and materially wrong.")
        add("")
    add("### Decay")
    add("")
    add(_table(result.ic_decay[["horizon_days", "mean_ic", "t_stat_nw", "p_value",
                                "hit_rate", "n_periods"]]))
    add("")

    # --- portfolios -------------------------------------------------------
    add("## Quantile portfolios")
    add("")
    add(f"{result.portfolios.n_quantiles} quantiles, {result.portfolios.weighting}-weighted, "
        "net of modelled transaction cost.")
    add("")
    add(_table(_quantile_table(result)))
    add("")
    add("### Long-only versus long-short (§10.4)")
    add("")
    add(f"- long-only excess (net, **primary**): {_pct(summary['mean_long_only_excess_net'])}")
    add(f"- long-short (net, secondary): {_pct(summary['mean_long_short_net'])}")
    add(f"- long-short (gross, never the headline): {_pct(summary['mean_long_short_gross'])}")
    add(f"- share of the long-short premium in the short leg: "
        f"{_pct(summary['short_leg_contribution'])}")
    add("")
    add(_short_leg_note(summary["short_leg_contribution"]))
    add("")
    add(f"Mean turnover in the top quantile: {_pct(summary['mean_turnover_top'])} per "
        f"rebalance; cost drag {_pct(summary['mean_cost_drag_top'])} per period.")
    add("")

    # --- Fama-MacBeth -----------------------------------------------------
    add("## Fama-MacBeth")
    add("")
    if result.fama_macbeth.get("n_periods"):
        rows = [
            {"variable": name, "mean_coefficient": stats["mean"],
             "t_stat_nw": stats["t_stat_nw"]}
            for name, stats in result.fama_macbeth["coefficients"].items()
        ]
        add(_table(pd.DataFrame(rows)))
        add("")
        add(f"{result.fama_macbeth['n_periods']} cross-sectional regressions.")
    else:
        add("Not estimated — too few usable cross-sections.")
    add("")

    # --- eras -------------------------------------------------------------
    add("## Era splits")
    add("")
    add("Boundaries are pre-declared; no split was chosen after seeing results.")
    add("")
    if result.era_results:
        add(_table(pd.DataFrame([
            {"era": era, **stats} for era, stats in result.era_results.items()
        ])))
    else:
        add("No era boundaries declared.")
    add("")

    # --- kill conditions --------------------------------------------------
    add("## Kill conditions")
    add("")
    for condition in prereg.kill_conditions:
        triggered = condition in result.kill_conditions_triggered
        add(f"- [{'x' if triggered else ' '}] {condition}"
            + ("  **TRIGGERED**" if triggered else ""))
    add("")

    # --- universe ---------------------------------------------------------
    add("## Universe")
    add("")
    sizes = result.universe_sizes
    add(f"Members per rebalance: min {sizes.min()}, median {sizes.median():.0f}, "
        f"max {sizes.max()}.")
    add("")

    # --- reproduction -----------------------------------------------------
    add("## Reproduction")
    add("")
    add("This result is reproducible from the git commit plus an archive snapshot. "
        "Every fact used was read through `store.as_of(date)`, and every row in "
        "the derived store carries the hash of the source document it came from.")
    add("")
    add(f"- pre-registration: `{prereg.path.name}` (sha256 `{result.prereg_hash}`)")
    add(f"- registered trials counted in the correction: {result.verdict.n_trials}")
    add("")
    return "\n".join(lines)


def _warnings(result: StudyResult) -> list[str]:
    out = []
    if result.non_defensible_warning:
        out.append(
            "**NON-DEFENSIBLE DATA.** This study touches facts sourced from "
            "screener.in, which is a prototyping source only (§5). No conclusion "
            "here is defensible without re-running against filing-sourced facts."
        )
    if result.rates_unverified:
        out.append(
            "**UNVERIFIED COST RATES.** The statutory rate table has not been "
            "checked against primary sources (§9). Every net-of-cost figure in "
            "this report inherits whatever error it contains."
        )
    if result.kill_conditions_triggered:
        out.append(
            f"**KILL CONDITION TRIGGERED:** "
            + "; ".join(result.kill_conditions_triggered)
        )
    if result.ic.n_periods < 20:
        out.append(
            f"**SHORT SERIES.** Only {result.ic.n_periods} rebalance periods. "
            "Any t-statistic on this is fragile regardless of its value."
        )
    if result.verdict.effective_n < result.verdict.raw_n / 4:
        out.append(
            f"**LOW BREADTH.** {result.verdict.raw_n:.0f} names but only "
            f"{result.verdict.effective_n:.1f} effective independent bets — the "
            "cross-section is highly correlated and the raw N is misleading."
        )
    return out


def _short_leg_note(share: float) -> str:
    if not np.isfinite(share):
        return "Short-leg contribution could not be computed."
    if share > 0.6:
        return (
            f"**{share:.0%} of the long-short premium comes from the short leg.** "
            "Shorting Indian smallcaps is not practically available — borrow is "
            "thin to nonexistent below the F&O universe. This factor's premium "
            "therefore lives mostly where it cannot be captured, and the "
            "long-short number should not be read as an achievable return."
        )
    return (
        f"{share:.0%} of the long-short premium comes from the short leg, so the "
        "long-only statistic captures most of the effect."
    )


def _quantile_table(result: StudyResult) -> pd.DataFrame:
    net = result.net_returns if hasattr(result, "net_returns") else result.portfolios.net_returns
    gross = result.portfolios.gross_returns
    return pd.DataFrame({
        "quantile": net.columns,
        "mean_gross": [gross[q].mean() for q in net.columns],
        "mean_net": [net[q].mean() for q in net.columns],
        "mean_turnover": [result.portfolios.turnover[q].mean() for q in net.columns],
        "cost_drag": [result.portfolios.cost_drag[q].mean() for q in net.columns],
    })


def _table(frame: pd.DataFrame) -> str:
    if frame is None or frame.empty:
        return "_(no data)_"
    formatted = frame.copy()
    for column in formatted.columns:
        if pd.api.types.is_float_dtype(formatted[column]):
            formatted[column] = formatted[column].map(lambda v: f"{v:.4f}"
                                                      if np.isfinite(v) else "n/a")
    header = "| " + " | ".join(str(c) for c in formatted.columns) + " |"
    divider = "|" + "|".join("---" for _ in formatted.columns) + "|"
    rows = ["| " + " | ".join(str(v) for v in row) + " |"
            for row in formatted.itertuples(index=False)]
    return "\n".join([header, divider, *rows])


def _pct(value: float) -> str:
    return f"{value:.2%}" if np.isfinite(value) else "n/a"


def write_report(result: StudyResult, prereg: Preregistration,
                 directory: Path | str) -> Path:
    """Write the report, keyed by pre-registration hash (§16)."""
    from src.prereg.registry import assert_pipeline_cannot_write

    directory = Path(directory)
    path = directory / f"{result.study_id}__{result.prereg_hash[:12]}.md"
    assert_pipeline_cannot_write(path)  # §3.6: never write into prereg/
    directory.mkdir(parents=True, exist_ok=True)
    path.write_text(render(result, prereg), encoding="utf-8")
    return path
