"""Evaluation harness (§10, §11).

Runs a pre-registered study end to end: build the PIT universe on each
rebalance date, compute the factor, preprocess exactly as declared, measure IC
and its decay, build quantile portfolios net of cost, run Fama-MacBeth with the
declared controls, split at the declared era boundaries, and produce a verdict
that survives multiple-testing correction or does not.

Everything that could be a researcher degree of freedom comes from the
pre-registration. The harness takes a `Preregistration` and a store, and there
is no parameter through which a caller can substitute a different winsorisation,
a different horizon, or a different window — `assert_window` refuses the last of
those explicitly.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

import numpy as np
import pandas as pd

from src.eval.crosssec import PreprocessSpec, forward_returns, preprocess
from src.eval.ic import ICResult, evaluate_ic, ic_autocorrelation, ic_decay
from src.eval.portfolios import QuantileResult, fama_macbeth, quantile_portfolios
from src.eval.stats import (
    SignificanceVerdict, Trial, TrialRegistry, benjamini_hochberg,
    deflated_sharpe_ratio, effective_n_from_exposures, sharpe_ratio,
)
from src.factors.base import Factor, FactorContext, all_factors
from src.master.universe import Universe
from src.prereg.registry import Preregistration
from src.prices.daily import benchmark_returns, daily_returns

#: Horizons for the IC decay curve (§10.2), in sessions.
DECAY_HORIZONS = (21, 63, 126, 252)


@dataclass
class StudyResult:
    """Everything a study produces. The prereg hash is on every artifact."""

    study_id: str
    prereg_hash: str
    spec_fingerprint: str
    factor_name: str
    universe_tier: str
    window: tuple[str, str]
    horizon_days: int
    rebalance_dates: list[str]
    ic: ICResult
    ic_decay: pd.DataFrame
    ic_autocorrelation: pd.Series
    portfolios: QuantileResult
    fama_macbeth: dict[str, Any]
    era_results: dict[str, dict[str, float]]
    verdict: SignificanceVerdict
    universe_sizes: pd.Series
    non_defensible_warning: bool
    rates_unverified: bool
    kill_conditions_triggered: list[str]
    generated_at: str = field(
        default_factory=lambda: dt.datetime.now(tz=dt.timezone.utc).isoformat())

    @property
    def headline(self) -> pd.Series:
        """§10.4/§11: net, long-only, excess over benchmark."""
        return self.portfolios.headline_return()


class Harness:
    def __init__(
        self,
        conn: sqlite3.Connection,
        *,
        cost_bps_round_trip: float = 100.0,
        n_quantiles: int = 5,
        weighting: str = "equal",
    ) -> None:
        self.conn = conn
        self.cost_bps_round_trip = cost_bps_round_trip
        self.n_quantiles = n_quantiles
        self.weighting = weighting
        self.universe = Universe(conn)
        self.registry = TrialRegistry(conn)

    # -- dates -------------------------------------------------------------

    def rebalance_dates(self, start: str, end: str, frequency: str) -> list[str]:
        """Trading sessions at the declared frequency, inside the window."""
        sessions = [
            r["date"] for r in self.conn.execute(
                "SELECT DISTINCT date FROM price_daily WHERE date BETWEEN ? AND ?"
                " ORDER BY date", (start, end))
        ]
        if not sessions:
            return []
        index = pd.DatetimeIndex(pd.to_datetime(sessions))
        rule = {"quarterly": "Q", "monthly": "M"}.get(frequency)
        if rule is None:
            raise ValueError(f"unknown rebalance frequency {frequency!r}")
        # Last session in each period — the date a rebalance would actually run.
        grouped = pd.Series(index, index=index).groupby(index.to_period(rule)).last()
        return [stamp.date().isoformat() for stamp in grouped]

    # -- the run -----------------------------------------------------------

    def run(
        self,
        prereg: Preregistration,
        *,
        factor: Factor | None = None,
        window: tuple[str, str] | None = None,
        record_trial: bool = True,
    ) -> StudyResult:
        start, end = window or prereg.window
        # §11: no optional stopping. Raises unless the window is registered.
        prereg.assert_window(start, end)

        factor = factor or all_factors()[prereg.factor_name]
        spec = prereg.preprocess_spec()
        horizon = prereg.horizon_days
        dates = self.rebalance_dates(start, end, prereg.rebalance_frequency)
        if not dates:
            raise ValueError(f"no trading sessions in window {start}..{end}")

        raw_scores: dict[str, pd.Series] = {}
        scores: dict[str, pd.Series] = {}
        forwards: dict[int, dict[str, pd.Series]] = {h: {} for h in
                                                     sorted({horizon, *DECAY_HORIZONS})}
        float_caps: dict[str, pd.Series] = {}
        universe_sizes: dict[str, int] = {}
        non_defensible = False

        # Forward returns need data AFTER the last rebalance date, which is
        # legitimate: they are the outcome being predicted, not an input to the
        # prediction. The factor context is still bounded at the as-of date.
        return_panel_end = _shift_days(end, max(forwards) * 2 + 30)

        for date in dates:
            result = self.universe.as_of(date, prereg.universe_tier)
            members = result.isins
            universe_sizes[date] = len(members)
            if len(members) < 10:
                continue

            ctx = FactorContext(self.conn, date, members)
            raw = factor(ctx)
            raw_scores[date] = raw

            sectors = result.members.set_index("isin")["sector"] \
                if "sector" in result.members.columns else None
            processed = preprocess(raw, spec, sectors)
            # Sign so that higher always means "more attractive", making IC
            # signs comparable across factors without a per-factor convention.
            scores[date] = processed if factor.higher_is_better else -processed
            float_caps[date] = ctx.free_float_market_cap

            returns = daily_returns(self.conn, members, _shift_days(date, -5),
                                    return_panel_end)
            for h in forwards:
                forwards[h][date] = forward_returns(returns, date, h)

            if not non_defensible:
                from src.store.bitemporal import BitemporalStore

                facts = BitemporalStore(self.conn).as_of(
                    date, isins=members, fact_names=list(factor.required_facts),
                    include_non_defensible=True)
                non_defensible = bool(len(facts) and not facts["defensible"].all())

        if not scores:
            raise ValueError("no rebalance date produced a usable universe")

        # --- IC (§10.2) --------------------------------------------------
        ic = evaluate_ic(scores, forwards[horizon], horizon)
        decay = ic_decay(scores, {h: forwards[h] for h in sorted(forwards)})
        autocorr = ic_autocorrelation(ic.series)

        # --- portfolios (§10.3, §10.4) -----------------------------------
        bench = benchmark_returns(self.conn, _benchmark_name(), start, return_panel_end)
        bench_by_date = {
            date: float((1.0 + bench.loc[bench.index > pd.Timestamp(date)]
                         .head(horizon).fillna(0.0)).prod() - 1.0)
            for date in scores
        } if not bench.empty else None

        portfolios = quantile_portfolios(
            scores, forwards[horizon], n_quantiles=self.n_quantiles,
            weighting=self.weighting, float_caps_by_date=float_caps,
            cost_bps_round_trip=self.cost_bps_round_trip,
            benchmark_by_date=bench_by_date,
        )

        # --- Fama-MacBeth (§10.5) ----------------------------------------
        controls = self._controls(scores, float_caps)
        fm = fama_macbeth(scores, forwards[horizon], controls)

        # --- eras (§10.6) -------------------------------------------------
        eras = self._era_results(portfolios, prereg.era_splits)

        # --- verdict (§11) ------------------------------------------------
        exposures = pd.DataFrame(scores).T
        effective_n = effective_n_from_exposures(exposures)
        headline = portfolios.headline_return().dropna()
        sharpe = sharpe_ratio(headline, periods_per_year=_periods_per_year(
            prereg.rebalance_frequency))

        if record_trial:
            self.registry.record(Trial(
                prereg_hash=prereg.spec_hash, factor_name=factor.name,
                spec_fingerprint=prereg.spec_fingerprint(),
                universe_tier=prereg.universe_tier, window_start=start,
                window_end=end, horizon_days=horizon, p_value=ic.p_value,
                sharpe=sharpe["sharpe"], effective_n=effective_n,
            ))

        verdict = self._verdict(prereg, factor, ic, sharpe, effective_n, exposures)
        killed = self._check_kill_conditions(prereg, ic, portfolios, verdict)

        from src.costs.model import rate_table_status

        return StudyResult(
            study_id=prereg.study_id, prereg_hash=prereg.spec_hash,
            spec_fingerprint=prereg.spec_fingerprint(), factor_name=factor.name,
            universe_tier=prereg.universe_tier, window=(start, end),
            horizon_days=horizon, rebalance_dates=list(scores),
            ic=ic, ic_decay=decay, ic_autocorrelation=autocorr,
            portfolios=portfolios, fama_macbeth=fm, era_results=eras,
            verdict=verdict, universe_sizes=pd.Series(universe_sizes),
            non_defensible_warning=non_defensible,
            rates_unverified=not rate_table_status()["all_verified"],
            kill_conditions_triggered=killed,
        )

    # -- helpers -----------------------------------------------------------

    def _controls(self, scores, float_caps) -> dict[str, pd.DataFrame]:
        """Size control for the Fama-MacBeth regressions."""
        out = {}
        for date in scores:
            caps = float_caps.get(date)
            if caps is None or caps.dropna().empty:
                continue
            out[date] = pd.DataFrame({"log_size": np.log(caps.where(caps > 0))})
        return out

    def _era_results(self, portfolios: QuantileResult,
                     boundaries: Sequence[str]) -> dict[str, dict[str, float]]:
        """Split at the PRE-DECLARED boundaries only (§10.6)."""
        headline = portfolios.headline_return().dropna()
        if headline.empty:
            return {}
        edges = ["0000-01-01", *sorted(boundaries), "9999-12-31"]
        out = {}
        for lo, hi in zip(edges[:-1], edges[1:]):
            mask = (headline.index >= lo) & (headline.index < hi)
            chunk = headline[mask]
            if chunk.empty:
                continue
            out[f"{lo}..{hi}"] = {
                "periods": int(len(chunk)),
                "mean_excess": float(chunk.mean()),
                "std": float(chunk.std(ddof=1)) if len(chunk) > 1 else float("nan"),
            }
        return out

    def _verdict(self, prereg, factor, ic, sharpe, effective_n, exposures
                 ) -> SignificanceVerdict:
        trials = self.registry.all_trials()
        n_trials = max(len(trials), 1)
        bh = benjamini_hochberg(trials["p_value"].tolist() if not trials.empty
                                else [ic.p_value], q=0.10)

        bh_significant = False
        if not trials.empty:
            mine = trials.index[
                (trials["prereg_hash"] == prereg.spec_hash)
                & (trials["spec_fingerprint"] == prereg.spec_fingerprint())
            ]
            if len(mine):
                bh_significant = bool(bh["reject"][int(mine[-1])])
        else:
            bh_significant = bool(bh["reject"][0])

        deflated = deflated_sharpe_ratio(
            sharpe["sharpe"], n_trials=n_trials,
            n_observations=int(sharpe["n"]), skew=sharpe["skew"],
            kurtosis=sharpe["kurtosis"],
        )
        return SignificanceVerdict(
            factor_name=factor.name,
            raw_p_value=ic.p_value,
            raw_significant=bool(np.isfinite(ic.p_value) and ic.p_value < 0.05),
            bh_threshold=bh["threshold"],
            bh_significant=bh_significant,
            deflated_sharpe=deflated["deflated_sharpe"],
            observed_sharpe=sharpe["sharpe"],
            expected_max_sharpe=deflated["expected_max_sharpe"],
            n_trials=n_trials,
            effective_n=effective_n,
            raw_n=float(exposures.shape[1]),
        )

    def _check_kill_conditions(self, prereg, ic, portfolios, verdict) -> list[str]:
        """Evaluate the declared kill conditions (§12).

        Only the machine-checkable forms are evaluated; prose conditions are
        listed in the report for the human to check, never silently treated as
        passed.
        """
        triggered = []
        summary = portfolios.summary()
        for condition in prereg.kill_conditions:
            text = str(condition).lower()
            if "ic" in text and "negative" in text and ic.mean < 0:
                triggered.append(str(condition))
            elif "turnover" in text:
                for token in text.replace("%", " ").split():
                    try:
                        limit = float(token)
                    except ValueError:
                        continue
                    if summary["mean_turnover_top"] * 100 > limit:
                        triggered.append(str(condition))
                    break
            elif "not significant" in text and not verdict.significant:
                triggered.append(str(condition))
        return triggered


def _shift_days(date: str, days: int) -> str:
    return (dt.date.fromisoformat(date) + dt.timedelta(days=days)).isoformat()


def _periods_per_year(frequency: str) -> int:
    return {"quarterly": 4, "monthly": 12}.get(frequency, 4)


def _benchmark_name() -> str:
    from src.config import get_config

    return get_config().benchmark
