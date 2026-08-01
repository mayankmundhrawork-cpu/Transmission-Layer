"""Factor library tests (§8) — the CP7 gate.

CP7: "every factor computes on ten historical dates with no `latest()` call
reachable from the call stack."

The reachability half is enforced two ways at once here: the runtime guard in
`bitemporal.latest` inspects the whole call stack and would raise if any factor
reached it, and `test_no_leak.py` fails CI if the name appears in this package
at all. This module adds the third: it actually runs everything, so a factor
that would only touch the forbidden path on a rarely-taken branch gets executed
rather than merely inspected.
"""
from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd
import pytest

from src.factors.base import Factor, FactorContext, all_factors, safe_divide
from src.master.universe import Universe
from src.store.bitemporal import LookAheadViolation
from src.store.schema import connect
from tests.platform.world import build_fundamentals, build_world, rebalance_dates

#: The ten historical dates CP7 asks for.
CP7_DATES = rebalance_dates("quarterly", dt.date(2021, 3, 31), dt.date(2023, 9, 29))


@pytest.fixture(scope="module")
def world(tmp_path_factory):
    conn = connect(tmp_path_factory.mktemp("db") / "platform.sqlite")
    w = build_world(conn)
    build_fundamentals(conn, w.isins)
    yield w
    conn.close()


@pytest.fixture(scope="module")
def contexts(world):
    """One FactorContext per CP7 date, built once and shared."""
    universe = Universe(world.conn)
    out = {}
    for date in CP7_DATES[:10]:
        members = universe.as_of(date, "nifty500").isins
        out[date] = FactorContext(world.conn, date, members)
    return out


def test_cp7_dates_are_ten_real_dates(contexts):
    assert len(contexts) == 10
    assert all(len(ctx.universe) > 20 for ctx in contexts.values())


# ===========================================================================
# CP7 — every factor, every date
# ===========================================================================

@pytest.mark.parametrize("factor_name", sorted(all_factors()))
def test_cp7_factor_computes_on_ten_dates(factor_name, contexts):
    """Every registered factor produces a usable score on all ten dates."""
    factor = all_factors()[factor_name]
    coverage = []
    for date, ctx in contexts.items():
        try:
            score = factor(ctx)
        except LookAheadViolation as exc:  # pragma: no cover - the point of the test
            pytest.fail(f"{factor_name} reached unfiltered fundamentals: {exc}")

        assert isinstance(score, pd.Series)
        assert list(score.index) == list(ctx.universe), "score must cover the universe"
        assert score.dtype == "float64"
        assert not np.isinf(score.dropna()).any(), f"{factor_name} produced inf on {date}"
        coverage.append(score.notna().mean())

    # A factor that is NaN everywhere computes without erroring and is useless.
    # Two exemptions, both deliberate: flags are legitimately sparse, and
    # lookahead_canary MUST be empty — see the dedicated test below.
    if factor_name == "lookahead_canary":
        return
    threshold = 0.0 if factor_name in ("auditor_change", "auditor_qualification") else 0.5
    assert max(coverage) > threshold, (
        f"{factor_name} produced no usable values on any of the ten dates "
        f"(coverage {[f'{c:.0%}' for c in coverage]}) — it computes, but it "
        "does not compute anything"
    )


@pytest.mark.acceptance
def test_cp7_no_factor_can_reach_latest(contexts):
    """Runtime half of the CP7 condition, exercised rather than inspected."""
    ctx = contexts[list(contexts)[-1]]
    for name, factor in all_factors().items():
        try:
            factor(ctx)
        except LookAheadViolation as exc:  # pragma: no cover
            pytest.fail(f"{name}: {exc}")


@pytest.mark.acceptance
def test_lookahead_canary_is_empty_on_every_date(contexts):
    """The canary tries to score names by their own FUTURE return.

    It must come back entirely NaN on every date, because `FactorContext` is
    bounded at the as-of date and exposes no path to later data. A single
    non-NaN value here means research code has been handed a time machine, and
    every result the platform has ever produced would be suspect.
    """
    canary = all_factors()["lookahead_canary"]
    for date, ctx in contexts.items():
        score = canary(ctx)
        assert score.isna().all(), (
            f"{date}: the look-ahead canary produced {score.notna().sum()} "
            "non-null values — future data is reachable from a factor"
        )


def test_the_guard_would_actually_fire_from_a_factor(contexts):
    """Positive control: prove the CP7 assertion is not vacuous."""
    import types

    ctx = contexts[list(contexts)[0]]
    module = types.ModuleType("src.factors.rogue")
    exec("def run(ctx):\n    return ctx._store.latest()", module.__dict__)
    with pytest.raises(LookAheadViolation):
        module.run(ctx)


# ===========================================================================
# Point-in-time behaviour
# ===========================================================================

def test_scores_change_across_dates(contexts):
    """A factor returning the same vector on every date is reading something
    static — almost always today's snapshot rather than the as-of date's."""
    factor = all_factors()["earnings_yield"]
    dates = list(contexts)
    early = factor(contexts[dates[0]])
    late = factor(contexts[dates[-1]])
    common = early.index.intersection(late.index)
    assert not np.allclose(
        early[common].fillna(-1).to_numpy(), late[common].fillna(-1).to_numpy()
    )


def test_context_cannot_be_asked_about_another_date(world):
    """The context takes its date at construction and exposes no parameter to
    query past it — the bound is structural, not a convention."""
    ctx = FactorContext(world.conn, "2021-03-31", world.ordinary[:5])
    import inspect

    for method in (ctx.facts, ctx.fact_history):
        params = set(inspect.signature(method).parameters)
        assert "date" not in params and "as_of_date" not in params


def test_prices_are_bounded_at_the_as_of_date(world):
    ctx = FactorContext(world.conn, "2021-03-31", world.ordinary[:5])
    assert ctx.closes.index.max() <= pd.Timestamp("2021-03-31")
    assert ctx.returns.index.max() <= pd.Timestamp("2021-03-31")


def test_facts_are_bounded_by_publication_not_period(world):
    """A March year-end filed in June must be invisible in April."""
    isin = world.ordinary[0]
    april = FactorContext(world.conn, "2021-04-15", [isin]).facts(["revenue"])
    july = FactorContext(world.conn, "2021-07-31", [isin]).facts(["revenue"])
    assert april["revenue"].iloc[0] != july["revenue"].iloc[0] or pd.isna(
        april["revenue"].iloc[0]
    )


def test_min_publication_lag_is_respected(world):
    class Lagged(Factor):
        name = "lagged_test_factor"
        min_publication_lag_days = 400

        def compute(self, ctx):
            return ctx.facts(["revenue"],
                             min_publication_lag_days=self.min_publication_lag_days)["revenue"]

    isin = world.ordinary[0]
    ctx = FactorContext(world.conn, "2021-07-31", [isin])
    assert Lagged()(ctx).iloc[0] != all_factors()["earnings_yield"].compute(ctx).iloc[0]


# ===========================================================================
# Definitions
# ===========================================================================

def test_size_uses_free_float_not_full_cap(contexts):
    """§8 is specific about this: with promoter holdings at 50-75%, a full-cap
    size factor is substantially a promoter-holding factor in disguise."""
    ctx = contexts[list(contexts)[-1]]
    free = all_factors()["log_free_float_mcap"](ctx)
    full = all_factors()["log_mcap"](ctx)
    common = free.dropna().index.intersection(full.dropna().index)
    assert len(common) > 10
    assert (free[common] < full[common]).all(), "float cap must be below full cap"
    assert not np.allclose(free[common], full[common])


def test_accruals_and_roe_have_opposite_conventions():
    assert all_factors()["accruals"].higher_is_better is False
    assert all_factors()["roe"].higher_is_better is True


def test_momentum_skips_the_recent_month(contexts):
    ctx = contexts[list(contexts)[-1]]
    mom = all_factors()["momentum_12_1"](ctx)
    rev = all_factors()["short_term_reversal"](ctx)
    common = mom.dropna().index.intersection(rev.dropna().index)
    assert len(common) > 10
    # If momentum included the last month these would be strongly correlated.
    assert abs(np.corrcoef(mom[common], rev[common])[0, 1]) < 0.7


def test_gross_profitability_is_scaled_by_assets(contexts):
    """Novy-Marx scales by assets, not sales. Scaling by sales would make it a
    margin factor, which is a different (and weaker) thing."""
    ctx = contexts[list(contexts)[-1]]
    gp = all_factors()["gross_profitability"](ctx)
    facts = ctx.facts(["revenue", "cost_of_materials", "purchases_stock_in_trade",
                       "inventory_change", "total_assets"])
    cogs = facts[["cost_of_materials", "purchases_stock_in_trade",
                  "inventory_change"]].sum(axis=1)
    expected = (facts["revenue"] - cogs) / facts["total_assets"]
    valid = gp.dropna().index
    assert np.allclose(gp[valid], expected[valid], rtol=1e-9)


def test_debt_free_company_gets_max_interest_coverage(world):
    """"Cannot compute" and "does not need to" are different states."""
    from src.store.bitemporal import BitemporalStore, Fact

    isin = world.ordinary[1]
    store = BitemporalStore(world.conn)
    for name, value in (("profit_before_tax", 1e8), ("finance_cost", 0.0)):
        store.add_fact(Fact(
            isin=isin, fact_name=name, period_type="A", period_start="2023-04-01",
            period_end="2024-03-31", value=value,
            published_at="2024-06-15T00:00:00+00:00", source_doc_hash="x",
            revision_seq=store.next_revision(isin, name, "2024-03-31"),
        ))
    ctx = FactorContext(world.conn, "2024-09-30", world.ordinary[:6])
    coverage = all_factors()["interest_coverage"](ctx)
    assert pd.notna(coverage[isin])
    assert coverage[isin] == coverage.max()


def test_cagr_from_a_loss_is_nan(world):
    """Growth from a negative base is not a percentage. A large positive number
    would rank a company recovering from a loss alongside a genuine compounder."""
    from src.factors.growth import _cagr

    history = pd.DataFrame(
        [[-10.0, 1.0, 3.0, 5.0], [10.0, 12.0, 14.0, 17.0]],
        index=["A", "B"], columns=["2020-03-31", "2021-03-31", "2022-03-31", "2023-03-31"],
    )
    result = _cagr(history, 3)
    assert pd.isna(result["A"])
    assert result["B"] == pytest.approx((17.0 / 10.0) ** (1 / 3) - 1)


def test_promoter_change_is_percentage_points(world):
    from src.factors.india import _change

    history = pd.DataFrame([[50.0, 51.0, 52.0, 53.0, 55.0]], index=["A"],
                           columns=list("abcde"))
    assert _change(history, lag=4)["A"] == pytest.approx(5.0)


# ===========================================================================
# helpers
# ===========================================================================

def test_safe_divide_guards_negative_denominators():
    """Book-to-price with negative equity produces a large negative number that
    sorts as 'expensive' when the company is insolvent."""
    result = safe_divide(pd.Series([100.0, 100.0]), pd.Series([-50.0, 50.0]))
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == pytest.approx(2.0)


def test_safe_divide_never_returns_inf():
    assert pd.isna(safe_divide(pd.Series([1.0]), pd.Series([0.0])).iloc[0])


def test_factor_must_declare_a_name():
    with pytest.raises(TypeError, match="must declare a `name`"):
        class Nameless(Factor):
            def compute(self, ctx):
                return pd.Series(dtype="float64")


def test_every_factor_declares_metadata():
    for name, factor in all_factors().items():
        described = factor.describe()
        assert described["name"] == name
        assert described["category"] != "other", f"{name} has no category"
        assert described["doc"], f"{name} has no docstring summary"


def test_factors_citing_literature_have_it_in_the_docstring():
    """§8: cite the definition in the docstring."""
    cited = 0
    for factor in all_factors().values():
        doc = factor.__doc__ or ""
        if any(str(year) in doc for year in range(1970, 2025)):
            cited += 1
    assert cited >= 15, f"only {cited} factors cite a source definition"
