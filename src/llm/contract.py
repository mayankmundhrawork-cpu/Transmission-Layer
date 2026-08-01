"""LLM interface contract (§15).

Four jobs, all behind typed JSON schemas so the provider is a one-file swap.
Default `LLM_MODE=stub` returns deterministic no-ops, so the whole system runs
without an API key.

The constraint that shapes every type here is §15's closing line: **the model
layer has a veto and a pen. It never has a vote.** Concretely, and enforced by
the dataclasses rather than by discipline:

* :class:`Extraction` carries a `source_doc_hash` and a `char_offset`. An
  extraction that cannot be located in the source is discarded — `validate`
  does the discarding, not a reviewer.
* :class:`Objection` has no score, no confidence, and no `approved` field.
  There is nowhere to put a positive judgement, so adversarial review cannot
  become endorsement by drift.
* No type in this module carries a numeric estimate of value, growth, quality,
  or probability. §2 forbids LLM-generated numbers entering a calculation, and
  the absence of a field is a stronger guarantee than a convention.
"""
from __future__ import annotations

import datetime as dt
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Literal, Sequence

ExtractionKind = Literal[
    "auditor_qualification",
    "auditor_change",
    "promoter_pledge",
    "related_party_transaction",
    "delisting_circular",
    "merger_circular",
]


class ExtractionRejected(ValueError):
    """An extracted field could not be located in its source document."""


@dataclass(frozen=True)
class Extraction:
    """One field extracted from a filing, verifiable against the original.

    `char_offset` and `quoted_text` together are what make this checkable: the
    quoted span must actually appear at that offset in the source document. An
    LLM that invents a plausible disclosure fails that check mechanically.
    """

    kind: ExtractionKind
    field_name: str
    value: str | float | bool | None
    source_doc_hash: str
    char_offset: int
    quoted_text: str
    extracted_at: str = field(
        default_factory=lambda: dt.datetime.now(tz=dt.timezone.utc).isoformat())

    def validate_against(self, document: str) -> None:
        """Verify the quoted span really sits at the claimed offset.

        Raises rather than returning False: §15 says an extraction that cannot
        be located is discarded, and a boolean return invites a caller to
        ignore it.
        """
        if self.char_offset < 0 or not self.quoted_text:
            raise ExtractionRejected(
                f"{self.field_name}: no locatable citation (offset "
                f"{self.char_offset}, quote {self.quoted_text!r})")
        window = document[self.char_offset: self.char_offset + len(self.quoted_text)]
        if window != self.quoted_text:
            raise ExtractionRejected(
                f"{self.field_name}: quoted text is not at offset "
                f"{self.char_offset} in document {self.source_doc_hash[:12]}. "
                "Extraction discarded — an unverifiable extraction is a "
                "hallucination that happens to be well formatted."
            )

    def as_dict(self) -> dict[str, Any]:
        return dict(vars(self))


@dataclass(frozen=True)
class Objection:
    """One argument for rejecting a study (§15.3).

    Deliberately has no severity score and no confidence. A ranked objection
    list becomes a risk score, a risk score becomes an input, and §2 forbids an
    LLM number entering a calculation. The `category` field is for grouping,
    not for weighting.
    """

    category: Literal[
        "look_ahead", "survivorship", "specification_tuning",
        "cost_optimism", "multiple_testing", "data_quality", "other",
    ]
    claim: str
    what_would_settle_it: str

    def as_dict(self) -> dict[str, Any]:
        return dict(vars(self))


@dataclass(frozen=True)
class ReviewResult:
    """The output of adversarial review. Objections only — it cannot approve."""

    prereg_hash: str
    objections: list[Objection]
    reviewed_at: str = field(
        default_factory=lambda: dt.datetime.now(tz=dt.timezone.utc).isoformat())

    @property
    def n_objections(self) -> int:
        return len(self.objections)

    def summary(self) -> str:
        if not self.objections:
            # Note the wording: NOT "no problems found".
            return ("Adversarial review raised no objections it could articulate. "
                    "That is not an endorsement — it is the absence of one.")
        lines = [f"{len(self.objections)} objections raised against "
                 f"{self.prereg_hash[:12]}:"]
        for i, objection in enumerate(self.objections, 1):
            lines.append(f"  {i}. [{objection.category}] {objection.claim}")
            lines.append(f"     would be settled by: {objection.what_would_settle_it}")
        return "\n".join(lines)


@dataclass(frozen=True)
class PreregDraft:
    """A drafted §12 specification. A DRAFT — never auto-committed (§15.2)."""

    spec: dict[str, Any]
    notes: str = ""

    def to_json(self) -> str:
        import json

        return json.dumps(self.spec, indent=2, sort_keys=False)


@dataclass(frozen=True)
class ForensicsResult:
    """Offline attribution across the study ledger (§15.4). No latency budget."""

    observations: list[str]
    studies_examined: int


class LLMAdapter(ABC):
    """The provider interface. One file per provider, swapped by config."""

    name: str = ""

    @abstractmethod
    def extract(self, document: str, kind: ExtractionKind,
                source_doc_hash: str) -> list[Extraction]:
        """Filing text -> structured fields, each with a verifiable citation."""

    @abstractmethod
    def draft_prereg(self, hypothesis: str, context: dict[str, Any]) -> PreregDraft:
        """Hypothesis -> a §12 JSON draft for a human to review and commit."""

    @abstractmethod
    def adversarial_review(self, report_markdown: str, prereg_hash: str) -> ReviewResult:
        """Argue ONLY for rejection. Cannot approve, score, or raise confidence."""

    @abstractmethod
    def forensics(self, ledger_markdown: str, studies: Sequence[dict[str, Any]]
                  ) -> ForensicsResult:
        """Offline attribution across the study ledger."""


def validated_extractions(
    extractions: Sequence[Extraction], document: str
) -> tuple[list[Extraction], list[str]]:
    """Keep only extractions that can be located in the source (§15.1).

    Returns (kept, discarded_reasons). Discarding is the default behaviour and
    the caller gets told how much was thrown away — a silent drop would hide a
    model that is confabulating at scale.
    """
    kept, discarded = [], []
    for extraction in extractions:
        try:
            extraction.validate_against(document)
        except ExtractionRejected as exc:
            discarded.append(str(exc))
            continue
        kept.append(extraction)
    return kept, discarded
