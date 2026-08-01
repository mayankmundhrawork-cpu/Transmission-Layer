"""Portfolio construction, rebalance, execution, and LLM layer tests (§13-§15)."""
from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd
import pytest

from src.costs.model import CostModel
from src.execution.adapter import ExecutionAdapter
from src.execution.dhan_live import DhanLiveAdapter, LiveExecutionBlocked
from src.execution.paper import PaperAdapter
from src.llm.contract import (
    Extraction, ExtractionRejected, Objection, ReviewResult, validated_extractions,
)
from src.llm.stub import StubAdapter
from src.portfolio.construct import Constraints, ConstructionError, construct
from src.portfolio.rebalance import build_plan


def make_inputs(n=40, sectors_count=8, turnover=10_000_000.0):
    isins = [f"INE{i:03d}A0100{i % 10}" for i in range(n)]
    scores = pd.Series(np.linspace(1.0, 2.0, n), index=isins)
    sectors = pd.Series([f"SECTOR{i % sectors_count}" for i in range(n)], index=isins)
    adv = pd.Series(turnover, index=isins)
    return scores, sectors, adv


@pytest.fixture
def constraints():
    return Constraints(capital_inr=1_000_000.0, max_position_pct=4.0,
                       max_sector_pct=25.0, min_positions=25)


# ===========================================================================
# §13 construction
# ===========================================================================

def test_weights_respect_the_position_cap(constraints):
    scores, sectors, adv = make_inputs()
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    assert target.weights.max() <= constraints.max_position_pct / 100.0 + 1e-9


def test_weights_respect_the_sector_cap():
    """Force a concentrated sector map so the cap has to bind.

    FINANCE has to sit at the TOP of the ranking, or the top-25 selection never
    picks enough of it for the cap to matter.
    """
    scores, _, adv = make_inputs(n=40)
    sectors = pd.Series([f"S{i}" for i in range(20)] + ["FINANCE"] * 20,
                        index=scores.index)
    constraints = Constraints(capital_inr=1_000_000.0, max_position_pct=10.0,
                              max_sector_pct=25.0, min_positions=25)
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    assert target.sector_weights().max() <= 0.25 + 1e-9
    assert "sector_cap" in target.binding_constraints


def test_min_positions_is_honoured(constraints):
    scores, sectors, adv = make_inputs()
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    assert target.n_positions >= constraints.min_positions


def test_too_few_eligible_names_is_an_error_not_a_concentrated_book(constraints):
    """A portfolio that cannot be built is information — usually that the book
    is too large for the tier. Silently building a concentrated one destroys it."""
    scores, sectors, adv = make_inputs(n=10)
    with pytest.raises(ConstructionError, match="MIN_POSITIONS"):
        construct(scores, constraints=constraints, sectors=sectors,
                  median_turnover=adv, as_of_date="2023-06-30")


def test_participation_constraint_caps_illiquid_names(constraints):
    """A name trading ₹100k/day cannot take 4% of a ₹10L book at a 5% cap.

    The illiquid names must be top-ranked, otherwise they are never selected
    and the constraint has nothing to bind on.
    """
    scores, sectors, adv = make_inputs(n=40)
    illiquid = adv.index[-5:]      # highest scores -> certain to be selected
    adv[illiquid] = 100_000.0      # 5% of this is ₹5,000 = 0.5% of a ₹10L NAV
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    for isin in illiquid:
        assert isin in target.weights.index
        assert target.weights[isin] <= 0.005 + 1e-9, (
            "an illiquid name took a full position despite the participation cap"
        )
    assert "participation" in target.binding_constraints


def test_surveillance_names_are_excluded(constraints):
    scores, sectors, adv = make_inputs()
    stages = pd.Series(0, index=scores.index)
    blocked = scores.index[-3:]   # the highest-scoring names
    stages[blocked] = 2
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, surveillance_stage=stages,
                       as_of_date="2023-06-30")
    assert not set(blocked) & set(target.weights.index)
    assert target.excluded["surveillance_stage_2_plus"] == list(blocked)


def test_non_trading_names_are_excluded(constraints):
    scores, sectors, adv = make_inputs()
    adv.iloc[-2:] = 0.0
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    assert not set(adv.index[-2:]) & set(target.weights.index)


def test_uninvestable_capacity_becomes_cash_not_a_violation():
    """When participation caps everything, the shortfall is cash — not an
    over-weight position quietly exceeding a limit."""
    scores, sectors, _ = make_inputs(n=40)
    adv = pd.Series(50_000.0, index=scores.index)
    constraints = Constraints(capital_inr=10_000_000.0, max_position_pct=4.0,
                              max_sector_pct=100.0, min_positions=25)
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    assert target.cash_weight > 0.5
    assert target.weights.sum() + target.cash_weight == pytest.approx(1.0, abs=1e-6)
    assert "capacity" in target.binding_constraints


def test_equal_weighting_is_the_default(constraints):
    """§2: a score-proportional weight vector is a composite with implicit
    weights that were never fit out-of-sample."""
    scores, sectors, adv = make_inputs()
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    held = target.weights[target.weights > 0]
    assert held.std() < 1e-9, "default weighting should be equal"


def test_days_to_liquidate_is_reported_per_position(constraints):
    scores, sectors, adv = make_inputs()
    target = construct(scores, constraints=constraints, sectors=sectors,
                       median_turnover=adv, as_of_date="2023-06-30")
    assert len(target.days_to_liquidate) == target.n_positions
    assert (target.days_to_liquidate > 0).all()


def test_lower_is_better_factor_is_inverted(constraints):
    scores, sectors, adv = make_inputs(n=40)
    high = construct(scores, constraints=constraints, sectors=sectors,
                     median_turnover=adv, higher_is_better=True)
    low = construct(scores, constraints=constraints, sectors=sectors,
                    median_turnover=adv, higher_is_better=False)
    assert set(high.weights.index) != set(low.weights.index)


# ===========================================================================
# §13 rebalance
# ===========================================================================

@pytest.fixture
def plan():
    isins = [f"INE{i:03d}A0100{i % 10}" for i in range(5)]
    return build_plan(
        target_weights=pd.Series([0.2] * 5, index=isins),
        current_quantities=pd.Series({isins[0]: 100, isins[1]: 50}),
        prices=pd.Series(100.0, index=isins),
        portfolio_value=1_000_000.0,
        as_of_date="2023-06-30",
        median_turnover=pd.Series(50_000_000.0, index=isins),
        cost_model=CostModel(warn_unverified=False),
    )


def test_plan_diffs_current_against_target(plan):
    assert len(plan.orders) == 5
    assert all(o.side == "buy" for o in plan.orders)


def test_every_order_carries_an_estimated_cost(plan):
    assert all(o.estimated_cost > 0 for o in plan.orders)
    assert plan.total_cost > 0


def test_sells_are_ordered_before_buys():
    isins = ["INE001A01001", "INE002A01002"]
    p = build_plan(
        target_weights=pd.Series({isins[0]: 1.0}),
        current_quantities=pd.Series({isins[1]: 100}),
        prices=pd.Series(100.0, index=isins),
        portfolio_value=100_000.0, as_of_date="2023-06-30",
        cost_model=CostModel(warn_unverified=False),
    )
    assert p.orders[0].side == "sell", "a rebalance cannot buy with cash it has not raised"


def test_circuit_locked_orders_are_flagged():
    isins = ["INE001A01001"]
    p = build_plan(
        target_weights=pd.Series({isins[0]: 1.0}),
        current_quantities=pd.Series(dtype="float64"),
        prices=pd.Series(100.0, index=isins),
        portfolio_value=100_000.0, as_of_date="2023-06-30",
        circuit_locked=pd.Series({isins[0]: True}),
        cost_model=CostModel(warn_unverified=False),
    )
    assert p.orders[0].circuit_locked
    assert "not transactable" in p.orders[0].note
    assert len(p.blocked_orders) == 1


def test_names_without_a_price_are_reported_not_guessed():
    p = build_plan(
        target_weights=pd.Series({"INE001A01001": 1.0}),
        current_quantities=pd.Series(dtype="float64"),
        prices=pd.Series({"INE001A01001": np.nan}),
        portfolio_value=100_000.0, as_of_date="2023-06-30",
        cost_model=CostModel(warn_unverified=False),
    )
    assert p.unresolved == ["INE001A01001"]
    assert p.orders == []


def test_confirmation_text_echoes_notional_and_count(plan):
    text = plan.confirmation_text()
    assert "orders" in text and "total notional" in text and "estimated cost" in text


# ===========================================================================
# §14 paper execution
# ===========================================================================

def test_paper_adapter_is_the_default_and_not_live():
    assert PaperAdapter.is_live is False
    assert issubclass(PaperAdapter, ExecutionAdapter)


def test_paper_fills_are_recorded_with_cost_attribution(tmp_path, plan):
    with PaperAdapter(tmp_path / "ledger.sqlite",
                      CostModel(warn_unverified=False)) as adapter:
        result = adapter.execute(plan)
        assert len(result.fills) == 5
        assert result.total_cost > 0
        attribution = adapter.cost_attribution()
        assert attribution["stt"] > 0
        assert attribution["spread"] > 0


def test_paper_positions_update(tmp_path, plan):
    with PaperAdapter(tmp_path / "l.sqlite", CostModel(warn_unverified=False)) as a:
        a.execute(plan)
        positions = a.positions()
        assert len(positions) == 5
        assert all(q > 0 for q in positions.values())


def test_paper_ledger_persists(tmp_path, plan):
    with PaperAdapter(tmp_path / "l.sqlite", CostModel(warn_unverified=False)) as a:
        a.execute(plan)
    with PaperAdapter(tmp_path / "l.sqlite") as b:
        assert len(b.fills()) == 5


def test_circuit_locked_orders_are_deferred_not_filled(tmp_path):
    isins = ["INE001A01001"]
    p = build_plan(
        target_weights=pd.Series({isins[0]: 1.0}),
        current_quantities=pd.Series(dtype="float64"),
        prices=pd.Series(100.0, index=isins), portfolio_value=100_000.0,
        as_of_date="2023-06-30", circuit_locked=pd.Series({isins[0]: True}),
        cost_model=CostModel(warn_unverified=False),
    )
    with PaperAdapter(tmp_path / "l.sqlite", CostModel(warn_unverified=False)) as a:
        result = a.execute(p)
        assert result.fills == []
        assert len(result.rejected) == 1
        assert a.fills()[0]["status"] == "deferred", (
            "the intent must be preserved so carry slippage is measurable"
        )


@pytest.mark.acceptance
def test_acceptance_6_no_paper_fill_is_costless(tmp_path, plan):
    """§18.6 through the execution path, not just the cost model."""
    with PaperAdapter(tmp_path / "l.sqlite", CostModel(warn_unverified=False)) as a:
        for fill in a.execute(plan).fills:
            assert fill.cost_total > 0


# ===========================================================================
# §14 live execution gates
# ===========================================================================

def test_live_is_blocked_when_disabled(cfg, plan):
    adapter = DhanLiveAdapter(cfg, confirm_fn=lambda p: "")
    with pytest.raises(LiveExecutionBlocked, match="LIVE_ENABLED is False"):
        adapter.execute(plan)


def test_live_is_blocked_without_a_registered_ip(tmp_path, monkeypatch, plan):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("LIVE_ENABLED", "true")
    from src.config import load_config

    adapter = DhanLiveAdapter(load_config(repo_root=tmp_path), confirm_fn=lambda p: "")
    with pytest.raises(LiveExecutionBlocked, match="DHAN_REGISTERED_IP"):
        adapter.execute(plan)


def test_live_is_blocked_on_ip_mismatch(tmp_path, monkeypatch, plan):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("LIVE_ENABLED", "true")
    monkeypatch.setenv("DHAN_REGISTERED_IP", "203.0.113.9")
    from src.config import load_config

    adapter = DhanLiveAdapter(load_config(repo_root=tmp_path), confirm_fn=lambda p: "")
    monkeypatch.setattr(adapter, "current_wan_ip", lambda: "198.51.100.4")
    with pytest.raises(LiveExecutionBlocked, match="does not match the registered"):
        adapter.execute(plan)


def test_ip_mismatch_message_refuses_to_automate_reregistration(tmp_path, monkeypatch, plan):
    """§14: automatic IP re-registration is deliberately not built. The message
    must say so rather than leaving it as an obvious next feature."""
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("LIVE_ENABLED", "true")
    monkeypatch.setenv("DHAN_REGISTERED_IP", "203.0.113.9")
    from src.config import load_config

    adapter = DhanLiveAdapter(load_config(repo_root=tmp_path), confirm_fn=lambda p: "")
    monkeypatch.setattr(adapter, "current_wan_ip", lambda: "198.51.100.4")
    problems = adapter.preflight(plan)
    assert any("does not automate IP re-registration" in p for p in problems)


def test_live_requires_a_typed_confirmation_matching_the_notional(
        tmp_path, monkeypatch, plan):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("LIVE_ENABLED", "true")
    monkeypatch.setenv("DHAN_REGISTERED_IP", "203.0.113.9")
    from src.config import load_config

    prompts: list[str] = []

    def wrong_answer(prompt):
        prompts.append(prompt)
        return "yes"

    adapter = DhanLiveAdapter(load_config(repo_root=tmp_path),
                              confirm_fn=wrong_answer,
                              token_provider=lambda: "tok")
    monkeypatch.setattr(adapter, "current_wan_ip", lambda: "203.0.113.9")
    with pytest.raises(LiveExecutionBlocked, match="confirmation token did not match"):
        adapter.execute(plan)

    assert "REAL orders with REAL money" in prompts[0]
    assert "total notional" in prompts[0], "the prompt must echo the notional (§14)"
    assert f"{plan.summary()['n_orders']}" in prompts[0]


def test_a_reflexive_yes_cannot_arm_a_trade(tmp_path, monkeypatch, plan):
    """The token encodes the order count and notional, so confirming requires
    having read them."""
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("LIVE_ENABLED", "true")
    monkeypatch.setenv("DHAN_REGISTERED_IP", "203.0.113.9")
    from src.config import load_config

    for answer in ("y", "yes", "YES", "ok", "", "confirm"):
        adapter = DhanLiveAdapter(load_config(repo_root=tmp_path),
                                  confirm_fn=lambda p, a=answer: a,
                                  token_provider=lambda: "tok")
        monkeypatch.setattr(adapter, "current_wan_ip", lambda: "203.0.113.9")
        with pytest.raises(LiveExecutionBlocked):
            adapter.execute(plan)


# ===========================================================================
# §15 LLM layer
# ===========================================================================

def test_stub_is_the_default_adapter(cfg):
    from src.llm.anthropic import get_adapter

    assert get_adapter(cfg).name == "stub"


def test_stub_extracts_nothing_rather_than_guessing():
    assert StubAdapter().extract("some filing text", "auditor_change", "hash") == []


def test_stub_review_returns_real_standing_objections():
    result = StubAdapter().adversarial_review("# report", "abc")
    assert result.n_objections >= 5
    assert {o.category for o in result.objections} >= {"look_ahead", "survivorship"}


def test_review_result_has_no_way_to_approve():
    """§15: the model layer has a veto and a pen. It never has a vote."""
    fields = set(ReviewResult.__dataclass_fields__)
    assert not fields & {"approved", "score", "confidence", "verdict", "rating"}
    objection_fields = set(Objection.__dataclass_fields__)
    assert not objection_fields & {"severity", "score", "confidence"}


def test_empty_review_is_not_described_as_an_endorsement():
    summary = ReviewResult(prereg_hash="abc", objections=[]).summary()
    assert "not an endorsement" in summary


def test_extraction_must_be_locatable_in_the_source():
    """§15.1: extraction that cannot be located in the source is discarded."""
    document = "The auditor issued a qualified opinion on the accounts."
    offset = document.index("qualified opinion")
    good = Extraction("auditor_qualification", "qualified", True, "h", offset,
                      "qualified opinion")
    good.validate_against(document)  # does not raise

    bad = Extraction("auditor_qualification", "qualified", True, "h", 0,
                     "the auditor resigned in protest")
    with pytest.raises(ExtractionRejected, match="Extraction discarded"):
        bad.validate_against(document)


def test_validated_extractions_reports_what_it_dropped():
    """A silent drop would hide a model confabulating at scale."""
    document = "Promoter pledge stood at 42% of holding."
    offset = document.index("42%")
    kept, discarded = validated_extractions([
        Extraction("promoter_pledge", "pledge_pct", 42.0, "h", offset, "42%"),
        Extraction("promoter_pledge", "pledge_pct", 99.0, "h", 0, "99% pledged"),
    ], document)
    assert len(kept) == 1 and len(discarded) == 1
    assert "discarded" in discarded[0].lower()


def test_negative_offset_is_rejected():
    with pytest.raises(ExtractionRejected, match="no locatable citation"):
        Extraction("auditor_change", "x", True, "h", -1, "").validate_against("doc")


def test_anthropic_adapter_strips_forbidden_keys():
    """§2: no LLM-generated number may enter a calculation."""
    from src.llm.anthropic import FORBIDDEN_KEYS, _strip_forbidden

    cleaned = _strip_forbidden({
        "claim": "look-ahead risk", "score": 0.87, "confidence": "high",
        "target_price": 1200, "what_would_settle_it": "the histogram",
    })
    assert set(cleaned) == {"claim", "what_would_settle_it"}
    assert {"score", "confidence", "probability"} <= FORBIDDEN_KEYS


def test_stub_prereg_draft_is_a_form_not_a_proposal():
    """§15.2: output is a draft for human commit, never auto-committed."""
    draft = StubAdapter().draft_prereg("value works", {"factor": "book_to_price"})
    assert "FILL_IN" in draft.to_json()
    assert "human must make" in draft.notes


def test_stub_draft_has_every_required_prereg_field():
    from src.prereg.registry import REQUIRED_FIELDS

    draft = StubAdapter().draft_prereg("h", {})
    for field in REQUIRED_FIELDS:
        assert field in draft.spec, f"draft skeleton omits {field}"
