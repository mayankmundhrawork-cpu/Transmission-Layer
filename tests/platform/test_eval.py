"""Evaluation harness and statistical protocol tests (§10, §11) — the CP8 gate.

CP8: "run the harness on a deliberately random factor (seeded noise) and
confirm it reports NOT SIGNIFICANT after correction."

A harness that reported NOT SIGNIFICANT for everything would pass that
trivially, so `test_cp8_harness_can_detect_a_real_signal` plants a factor with
genuine predictive content and asserts the IC machinery finds it. The pair is
the actual calibration check: reads zero on a blank sample, reads non-zero on a
real one.
"""
from __future__ import annotations

import datetime as dt
import warnings

import numpy as np
import pandas as pd
import pytest

from src.eval.crosssec import (
    PreprocessSpec, cross_section_frame, forward_returns, preprocess,
    rank_normalise, sector_neutralise, winsorise, zscore,
)
from src.eval.harness import Harness
from src.eval.ic import evaluate_ic, ic_autocorrelation, spearman_ic
from src.eval.portfolios import (
    assign_quantiles, compute_turnover, portfolio_weights, quantile_portfolios,
)
from src.eval.report import render
from src.eval.stats import (
    Trial, TrialRegistry, benjamini_hochberg, deflated_sharpe_ratio,
    effective_n_from_correlation, effective_n_from_exposures, newey_west_tstat,
    sharpe_ratio,
)
from src.factors.base import Factor, FactorContext
from src.prereg.registry import PreregError, load
from src.store.schema import connect
from tests.platform.world import build_fundamentals, build_world

PREREG_PATH = "prereg/PREREG-000-noise-control.json"


@pytest.fixture(scope="module")
def study_conn(tmp_path_factory):
    conn = connect(tmp_path_factory.mktemp("db") / "platform.sqlite")
    world = build_world(conn)
    build_fundamentals(conn, world.isins)
    yield conn
    conn.close()


@pytest.fixture
def prereg():
    return load(PREREG_PATH)


@pytest.fixture(scope="module")
def noise_result(study_conn):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return Harness(study_conn).run(load(PREREG_PATH))


# ===========================================================================
# CP8 — the gate
# ===========================================================================

def test_cp8_noise_factor_is_not_significant(noise_result):
    """A factor that is empty by construction must not clear correction."""
    verdict = noise_result.verdict
    assert verdict.significant is False
    assert verdict.verdict == "NOT SIGNIFICANT"
    assert verdict.deflated_sharpe < 0.95


def test_cp8_verdict_shows_both_corrected_and_uncorrected(noise_result):
    """§11: a factor clearing the uncorrected threshold and failing the
    corrected one is reported as NOT SIGNIFICANT with both numbers shown."""
    summary = noise_result.verdict.summary()
    assert "uncorrected p" in summary
    assert "deflated Sharpe" in summary
    assert "BH threshold" in summary
    assert "effective independent bets" in summary


def test_cp8_effective_n_is_below_raw_n(noise_result):
    """§11: firing counts are not observations. A cross-section of correlated
    names is worth fewer independent bets than its headcount."""
    verdict = noise_result.verdict
    assert verdict.effective_n < verdict.raw_n
    assert verdict.effective_n > 1


def test_cp8_kill_conditions_fire(noise_result):
    assert any("NOT SIGNIFICANT" in c for c in noise_result.kill_conditions_triggered)


def _planted_panel(correlation: float, *, periods: int = 40, names: int = 120,
                   seed: int = 5):
    """Score/forward-return pairs with a known cross-sectional correlation.

    The synthetic market's prices are independent random walks, so no *real*
    factor has predictive power in it — a planted factor there would correctly
    measure zero. To test that the harness can detect signal when signal
    exists, the signal has to be put into the data, which is what this does.
    """
    rng = np.random.default_rng(seed)
    scores, forwards = {}, {}
    for period in range(periods):
        date = f"20{20 + period // 4:02d}-{3 * (period % 4) + 3:02d}-28"
        score = rng.normal(size=names)
        noise = rng.normal(size=names)
        forward = (correlation * score
                   + np.sqrt(max(1.0 - correlation ** 2, 0.0)) * noise) * 0.08
        index = pd.Index([f"INE{i:03d}A0100{i % 10}" for i in range(names)])
        scores[date] = pd.Series(score, index=index)
        forwards[date] = pd.Series(forward, index=index)
    return scores, forwards


def test_cp8_harness_can_detect_a_real_signal():
    """Power control. Without it, "NOT SIGNIFICANT for everything" passes CP8.

    Feeds the IC machinery a panel with a planted cross-sectional correlation
    and asserts it recovers it and calls it significant.
    """
    scores, forwards = _planted_panel(0.15)
    result = evaluate_ic(scores, forwards, 63)
    assert result.mean > 0.08, (
        f"planted IC of 0.15 was measured as {result.mean:.4f} — the harness "
        "cannot recover a signal that is actually there"
    )
    assert result.p_value < 0.01
    assert result.hit_rate > 0.7


def test_cp8_harness_reports_nothing_on_an_empty_panel():
    """The other half of the calibration pair: reads ~zero on a blank sample."""
    scores, forwards = _planted_panel(0.0)
    result = evaluate_ic(scores, forwards, 63)
    assert abs(result.mean) < 0.03
    assert result.p_value > 0.05


def test_cp8_verdict_flips_to_significant_on_strong_statistics(tmp_path):
    """The verdict machinery is capable of returning SIGNIFICANT — otherwise
    the noise result proves nothing."""
    from src.eval.stats import SignificanceVerdict

    strong = SignificanceVerdict(
        factor_name="strong", raw_p_value=0.0001, raw_significant=True,
        bh_threshold=0.01, bh_significant=True, deflated_sharpe=0.99,
        observed_sharpe=0.6, expected_max_sharpe=0.2, n_trials=20,
        effective_n=40.0, raw_n=200.0,
    )
    assert strong.significant is True
    assert strong.verdict == "SIGNIFICANT"


def test_cp8_report_renders_for_a_null_result(noise_result, prereg):
    text = render(noise_result, prereg)
    assert text.startswith("# PREREG-000-noise-control — NOT SIGNIFICANT")
    assert noise_result.prereg_hash in text
    assert "## Result" in text
    assert "does NOT rule out" in text


def test_cp8_report_has_no_positive_only_code_path(noise_result, prereg):
    """§19: report generation must not have a code path only exercised on
    positive results. Assert a forced-positive verdict renders the same
    sections in the same order."""
    import copy

    null_text = render(noise_result, prereg)
    positive = copy.deepcopy(noise_result)
    object.__setattr__(positive.verdict, "bh_significant", True)
    object.__setattr__(positive.verdict, "deflated_sharpe", 0.99)
    positive_text = render(positive, prereg)

    def sections(text):
        return [l for l in text.splitlines() if l.startswith("## ")]

    assert sections(null_text) == sections(positive_text), (
        "a positive result renders different sections than a null one"
    )
    assert positive_text.splitlines()[0].endswith("SIGNIFICANT")


# ===========================================================================
# §11 — no optional stopping
# ===========================================================================

def test_unregistered_window_is_refused(study_conn, prereg):
    with pytest.raises(PreregError, match="optional stopping"):
        Harness(study_conn).run(prereg, window=("2019-01-01", "2021-12-31"))


def test_registered_window_extension_is_allowed(prereg, tmp_path):
    import json

    raw = dict(prereg.raw)
    raw["window_extensions"] = [{
        "start": "2019-01-01", "end": "2024-12-31",
        "declared_before_results_viewed": True,
    }]
    path = tmp_path / "extended.json"
    path.write_text(json.dumps(raw), encoding="utf-8")
    load(path).assert_window("2019-01-01", "2024-12-31")


def test_extension_not_declared_before_results_is_refused(prereg, tmp_path):
    import json

    raw = dict(prereg.raw)
    raw["window_extensions"] = [{
        "start": "2019-01-01", "end": "2024-12-31",
        "declared_before_results_viewed": False,
    }]
    path = tmp_path / "late.json"
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(PreregError, match="before results were viewed"):
        load(path).assert_window("2019-01-01", "2024-12-31")


# ===========================================================================
# §11 — effective N
# ===========================================================================

def test_effective_n_equals_n_for_independent_names():
    assert effective_n_from_correlation(np.eye(50)) == pytest.approx(50.0)


def test_effective_n_is_one_when_everything_moves_together():
    assert effective_n_from_correlation(np.ones((40, 40))) == pytest.approx(1.0, abs=0.01)


def test_effective_n_falls_between_for_partial_correlation():
    n, rho = 40, 0.5
    corr = np.full((n, n), rho)
    np.fill_diagonal(corr, 1.0)
    result = effective_n_from_correlation(corr)
    assert 1.0 < result < n
    assert result < n / 2, "half-correlated names are worth far fewer than N bets"


def test_effective_n_from_exposures_handles_sparse_names():
    frame = pd.DataFrame(np.random.default_rng(1).normal(size=(20, 5)),
                         columns=list("ABCDE"))
    frame["F"] = np.nan  # never observed
    assert effective_n_from_exposures(frame) <= 5


# ===========================================================================
# §10.2 — Newey-West
# ===========================================================================

def test_newey_west_deflates_an_autocorrelated_series():
    """The reason the adjustment is mandatory: overlapping forward windows
    make the IC series serially correlated, and the naive t is inflated."""
    rng = np.random.default_rng(7)
    innovations = rng.normal(0.05, 0.1, 400)
    ar = [innovations[0]]
    for value in innovations[1:]:
        ar.append(0.8 * ar[-1] + value)
    series = pd.Series(ar)

    _, nw_t = newey_west_tstat(series)
    naive_t = series.mean() / (series.std(ddof=1) / np.sqrt(len(series)))
    assert abs(nw_t) < abs(naive_t), "the adjusted t must be smaller"
    assert abs(naive_t) / abs(nw_t) > 1.5


def test_newey_west_matches_naive_on_iid_data():
    rng = np.random.default_rng(3)
    series = pd.Series(rng.normal(0.02, 0.1, 500))
    _, nw_t = newey_west_tstat(series)
    naive_t = series.mean() / (series.std(ddof=1) / np.sqrt(len(series)))
    assert nw_t == pytest.approx(naive_t, rel=0.35)


def test_newey_west_handles_short_series():
    mean, t = newey_west_tstat(pd.Series([0.1, 0.2]))
    assert np.isnan(t)


# ===========================================================================
# §11 — multiple testing
# ===========================================================================

def test_benjamini_hochberg_known_answer():
    """Benjamini & Hochberg (1995) worked example."""
    p = [0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344,
         0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.000]
    result = benjamini_hochberg(p, q=0.05)
    assert result["n_rejected"] == 4
    assert result["threshold"] == pytest.approx(0.0095)


def test_bh_rejects_nothing_when_all_p_are_large():
    assert benjamini_hochberg([0.4, 0.5, 0.9], q=0.10)["n_rejected"] == 0


def test_bh_gets_stricter_as_trials_accumulate():
    """The whole point of the persistent registry: a p-value that survives at
    5 trials may not at 200."""
    few = benjamini_hochberg([0.02] + [0.5] * 4, q=0.10)
    many = benjamini_hochberg([0.02] + [0.5] * 199, q=0.10)
    assert few["n_rejected"] == 1
    assert many["n_rejected"] == 0


def test_bh_handles_nan_p_values():
    result = benjamini_hochberg([0.001, float("nan"), 0.5], q=0.10)
    assert result["reject"][1] is False


def test_deflated_sharpe_falls_as_trials_grow():
    one = deflated_sharpe_ratio(0.30, n_trials=1, n_observations=60)
    many = deflated_sharpe_ratio(0.30, n_trials=500, n_observations=60)
    assert many["deflated_sharpe"] < one["deflated_sharpe"]
    assert many["expected_max_sharpe"] > one["expected_max_sharpe"]


def test_deflated_sharpe_penalises_negative_skew():
    """Negative skew makes a given Sharpe less impressive — the return series
    is one bad period away from giving it back."""
    symmetric = deflated_sharpe_ratio(0.3, n_trials=10, n_observations=100, skew=0.0)
    skewed = deflated_sharpe_ratio(0.3, n_trials=10, n_observations=100, skew=-1.5)
    assert skewed["deflated_sharpe"] < symmetric["deflated_sharpe"]


def test_sharpe_reports_moments_the_deflation_needs():
    rng = np.random.default_rng(11)
    stats = sharpe_ratio(pd.Series(rng.normal(0.01, 0.05, 200)))
    assert set(stats) >= {"sharpe", "annualised", "skew", "kurtosis", "n"}


# ===========================================================================
# §11 — persistent trial registry
# ===========================================================================

def test_trial_registry_persists_and_counts(tmp_path):
    conn = connect(tmp_path / "db.sqlite")
    registry = TrialRegistry(conn)
    for i in range(3):
        registry.record(Trial(
            prereg_hash="h", factor_name=f"f{i}", spec_fingerprint=f"s{i}",
            universe_tier="nifty500", window_start="2019-01-01",
            window_end="2023-12-31", horizon_days=63, p_value=0.2,
        ))
    assert registry.count() == 3
    conn.close()

    reopened = connect(tmp_path / "db.sqlite")
    assert TrialRegistry(reopened).count() == 3, "the count must survive a restart"
    reopened.close()


def test_trials_cannot_be_deleted(tmp_path):
    """§11: removing an inconvenient trial would understate the correction."""
    import sqlite3

    conn = connect(tmp_path / "db.sqlite")
    TrialRegistry(conn).record(Trial(
        prereg_hash="h", factor_name="f", spec_fingerprint="s",
        universe_tier="nifty500", window_start="a", window_end="b",
        horizon_days=63, p_value=0.9,
    ))
    with pytest.raises(sqlite3.IntegrityError, match="permanent"):
        conn.execute("DELETE FROM trial_registry")
    conn.close()


def test_rerunning_the_same_spec_does_not_double_count(tmp_path):
    conn = connect(tmp_path / "db.sqlite")
    registry = TrialRegistry(conn)
    trial = Trial(prereg_hash="h", factor_name="f", spec_fingerprint="s",
                  universe_tier="nifty500", window_start="a", window_end="b",
                  horizon_days=63, p_value=0.3)
    registry.record(trial)
    registry.record(trial)
    assert registry.count() == 1
    conn.close()


def test_fdr_status_covers_the_whole_registry(tmp_path):
    conn = connect(tmp_path / "db.sqlite")
    registry = TrialRegistry(conn)
    for i, p in enumerate([0.001, 0.4, 0.6, 0.8]):
        registry.record(Trial(
            prereg_hash="h", factor_name=f"f{i}", spec_fingerprint=f"s{i}",
            universe_tier="t", window_start="a", window_end="b",
            horizon_days=63, p_value=p))
    status = registry.fdr_status()
    assert len(status) == 4
    assert status["n_trials_total"].iloc[0] == 4
    conn.close()


# ===========================================================================
# §10.1 — preprocessing
# ===========================================================================

def test_winsorise_clips_at_declared_percentiles():
    series = pd.Series([-100.0] + [1.0] * 98 + [100.0])
    out = winsorise(series, 1.0, 99.0)
    assert out.min() > -100.0 and out.max() < 100.0


def test_zscore_standardises():
    out = zscore(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0]))
    assert out.mean() == pytest.approx(0.0, abs=1e-12)
    assert out.std(ddof=1) == pytest.approx(1.0)


def test_zscore_of_a_constant_is_nan_not_inf():
    """A factor with no dispersion has no ranking to offer."""
    assert zscore(pd.Series([3.0] * 10)).isna().all()


def test_sector_neutralise_removes_the_sector_mean():
    scores = pd.Series([1.0, 3.0, 10.0, 20.0], index=list("abcd"))
    sectors = pd.Series(["X", "X", "Y", "Y"], index=list("abcd"))
    out = sector_neutralise(scores, sectors)
    assert out["a"] == pytest.approx(-1.0)
    assert out["c"] == pytest.approx(-5.0)


def test_singleton_sector_becomes_nan_not_zero():
    """A deterministic zero would look like a neutral score rather than an
    uncomputable one."""
    scores = pd.Series([1.0, 3.0, 10.0], index=list("abc"))
    sectors = pd.Series(["X", "X", "Y"], index=list("abc"))
    assert pd.isna(sector_neutralise(scores, sectors)["c"])


def test_preprocess_refuses_to_silently_skip_declared_neutralisation():
    spec = PreprocessSpec(1.0, 99.0, sector_neutralise=True)
    with pytest.raises(ValueError, match="silently change the spec"):
        preprocess(pd.Series([1.0, 2.0]), spec, sectors=None)


def test_preprocess_spec_rejects_impossible_percentiles():
    with pytest.raises(ValueError, match="percentiles"):
        PreprocessSpec(99.0, 1.0)


def test_rank_normalise_produces_a_normal_shape():
    out = rank_normalise(pd.Series(np.exp(np.arange(200) / 20.0)))
    assert abs(out.mean()) < 0.05
    assert 0.9 < out.std(ddof=1) < 1.15


# ===========================================================================
# §10.2 — forward returns exclude the as-of session
# ===========================================================================

def test_forward_returns_exclude_the_as_of_session():
    """A signal computed from a day's close cannot capture that day's move.
    Including it is a one-day look-ahead that shows up as suspiciously strong
    short-horizon IC."""
    idx = pd.date_range("2021-01-04", periods=10, freq="B")
    returns = pd.DataFrame({"A": [0.5] + [0.01] * 9}, index=idx)
    forward = forward_returns(returns, idx[0], 3)
    assert forward["A"] == pytest.approx((1.01 ** 3) - 1)


def test_forward_returns_require_most_of_the_horizon():
    idx = pd.date_range("2021-01-04", periods=5, freq="B")
    returns = pd.DataFrame({"A": [0.01] * 5}, index=idx)
    assert pd.isna(forward_returns(returns, idx[0], 63)["A"])


def test_forward_returns_empty_at_the_end_of_the_panel():
    idx = pd.date_range("2021-01-04", periods=3, freq="B")
    returns = pd.DataFrame({"A": [0.01] * 3}, index=idx)
    assert forward_returns(returns, idx[-1], 5).empty


# ===========================================================================
# §10.3/§10.4 — portfolios
# ===========================================================================

def test_quantiles_are_balanced_on_a_skewed_factor():
    """Value factors are heavily right-skewed; equal-width bins would put most
    names in one bucket."""
    scores = pd.Series(np.exp(np.linspace(0, 10, 100)))
    buckets = assign_quantiles(scores, 5)
    assert buckets.value_counts().std() <= 1.0


def test_turnover_is_one_way():
    old = pd.Series({"a": 0.5, "b": 0.5})
    new = pd.Series({"c": 0.5, "d": 0.5})
    assert compute_turnover(old, new) == pytest.approx(1.0)
    assert compute_turnover(old, old) == pytest.approx(0.0)


def test_float_weighting_uses_caps():
    weights = portfolio_weights(pd.Index(["a", "b"]), "float",
                                pd.Series({"a": 300.0, "b": 100.0}))
    assert weights["a"] == pytest.approx(0.75)


def test_net_is_always_below_gross_when_turnover_is_positive():
    scores = {"2021-03-31": pd.Series({"a": 1.0, "b": 2.0, "c": 3.0, "d": 4.0,
                                       "e": 5.0, "f": 6.0, "g": 7.0, "h": 8.0,
                                       "i": 9.0, "j": 10.0})}
    forwards = {"2021-03-31": pd.Series({k: 0.05 for k in "abcdefghij"})}
    result = quantile_portfolios(scores, forwards, n_quantiles=5,
                                 cost_bps_round_trip=100.0)
    assert (result.net_returns < result.gross_returns).all().all()


def test_long_only_spread_is_the_headline(noise_result):
    """§10.4: long-only excess is primary, long-short secondary."""
    headline = noise_result.headline
    long_only = noise_result.portfolios.long_only_spread(net=True)
    pd.testing.assert_series_equal(headline, long_only)


def test_short_leg_contribution_is_quantified(noise_result):
    assert "short_leg_contribution" in noise_result.portfolios.summary()


# ===========================================================================
# IC mechanics
# ===========================================================================

def test_spearman_ic_is_one_for_a_perfect_ranking():
    scores = pd.Series(range(20), dtype=float)
    ic, breadth = spearman_ic(scores, scores * 2.0)
    assert ic == pytest.approx(1.0)
    assert breadth == 20


def test_spearman_ic_is_nan_on_a_constant_score():
    ic, _ = spearman_ic(pd.Series([1.0] * 20), pd.Series(range(20), dtype=float))
    assert np.isnan(ic)


def test_ic_needs_a_minimum_cross_section():
    ic, _ = spearman_ic(pd.Series([1.0, 2.0]), pd.Series([1.0, 2.0]))
    assert np.isnan(ic)


def test_ic_autocorrelation_is_reported(noise_result):
    assert isinstance(noise_result.ic_autocorrelation, pd.Series)


def test_ic_decay_covers_multiple_horizons(noise_result):
    assert len(noise_result.ic_decay) >= 4
    assert set(noise_result.ic_decay["horizon_days"]) >= {21, 63, 126, 252}
