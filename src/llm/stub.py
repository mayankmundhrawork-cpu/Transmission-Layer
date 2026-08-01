"""Stub LLM adapter (§15) — the default.

Deterministic no-ops. `LLM_MODE=stub` is the default precisely so the entire
platform runs, and every test passes, with no API key and no network.

The stub is not a placeholder that returns nothing useful. It returns the
*structurally correct empty answer* for each job:

* `extract` returns no extractions — which is the honest answer when nothing
  read the document.
* `adversarial_review` returns the standing objections that apply to any study
  in this domain regardless of its content. They are real objections, written
  once by a human, and a study author should answer them whether or not a model
  is available to restate them.
* `draft_prereg` returns a §12-shaped skeleton with the fields the author must
  fill in, marked as such.
"""
from __future__ import annotations

from typing import Any, Sequence

from src.llm.contract import (
    Extraction, ExtractionKind, ForensicsResult, LLMAdapter, Objection,
    PreregDraft, ReviewResult,
)

#: Objections that apply to essentially any factor study on Indian smallcaps.
#: Written by a human, not generated. A study that cannot answer these does not
#: need an LLM to be in trouble.
STANDING_OBJECTIONS = [
    Objection(
        category="look_ahead",
        claim="Fundamental facts may be readable before their filing date if any "
              "publication timestamp was inferred rather than observed.",
        what_would_settle_it="The publication-lag histogram (§18.3) showing mass "
                             "in the statutory window and none near zero.",
    ),
    Objection(
        category="survivorship",
        claim="The universe may exclude securities delisted during the window.",
        what_would_settle_it="A named company delisted inside the window that "
                             "appears in universe.as_of(t) before its delisting.",
    ),
    Objection(
        category="cost_optimism",
        claim="Cost assumptions may understate impact in the smallcap tier, where "
              "impact dominates statutory cost at any meaningful size.",
        what_would_settle_it="Days-to-liquidate per position at the intended book "
                             "size, and a verified statutory rate table.",
    ),
    Objection(
        category="multiple_testing",
        claim="The reported significance may not account for every specification "
              "previously evaluated in this repository.",
        what_would_settle_it="The trial registry count used in the correction, "
                             "compared against the study ledger.",
    ),
    Objection(
        category="specification_tuning",
        claim="Preprocessing choices may have been selected after seeing results.",
        what_would_settle_it="The pre-registration hash predating the result "
                             "artifacts, and the absence of near-identical "
                             "fingerprints in the trial registry.",
    ),
]


class StubAdapter(LLMAdapter):
    """No-op adapter. Deterministic, offline, and honest about being empty."""

    name = "stub"

    def extract(self, document: str, kind: ExtractionKind,
                source_doc_hash: str) -> list[Extraction]:
        # No model read the document, so nothing was extracted. Returning a
        # plausible guess here would be worse than returning nothing.
        return []

    def draft_prereg(self, hypothesis: str, context: dict[str, Any]) -> PreregDraft:
        return PreregDraft(
            spec={
                "study_id": "PREREG-XXX-fill-me-in",
                "hypothesis": hypothesis,
                "factor": {"name": context.get("factor", "FILL_IN"),
                           "definition": "FILL_IN"},
                "preprocessing": {
                    "winsorise_lower_pct": "FILL_IN",
                    "winsorise_upper_pct": "FILL_IN",
                    "standardise": "FILL_IN",
                    "sector_neutralise": "FILL_IN",
                },
                "universe_tier": context.get("universe_tier", "FILL_IN"),
                "evaluation_window": {"start": "FILL_IN", "end": "FILL_IN"},
                "rebalance_frequency": "FILL_IN",
                "forward_return_horizon_days": "FILL_IN",
                "null_structure": "FILL_IN",
                "primary_metric": {"name": "FILL_IN", "threshold": "FILL_IN",
                                   "relative_to": "FILL_IN"},
                "secondary_metrics": [],
                "era_splits": [],
                "kill_conditions": [],
                "interpretation_asymmetry": {
                    "null_result_rules_out": "FILL_IN",
                    "null_result_does_not_rule_out": "FILL_IN",
                },
            },
            notes="Stub draft: every FILL_IN is a decision a human must make and "
                  "commit before results exist. This is a form, not a proposal.",
        )

    def adversarial_review(self, report_markdown: str, prereg_hash: str) -> ReviewResult:
        return ReviewResult(prereg_hash=prereg_hash,
                            objections=list(STANDING_OBJECTIONS))

    def forensics(self, ledger_markdown: str, studies: Sequence[dict[str, Any]]
                  ) -> ForensicsResult:
        return ForensicsResult(
            observations=[
                f"{len(studies)} studies in the ledger. Stub mode performs no "
                "attribution; set LLM_MODE=live for narrative forensics.",
            ],
            studies_examined=len(studies),
        )
