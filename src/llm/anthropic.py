"""Anthropic adapter (§15) — the swap-in for `LLM_MODE=live`.

One file, same contract as the stub. Nothing outside this module knows which
provider is in use.

Every prompt here is written to make the §2 and §15 constraints hard to violate
even if the model tried:

* Extraction is told to return a character offset and an exact quote, and every
  returned field is then *mechanically verified* against the document by
  `validated_extractions`. A confabulated disclosure fails the offset check and
  is discarded without a human looking at it.
* Adversarial review is given a response schema with no approval field, no
  score, and no confidence. It cannot express endorsement because there is
  nowhere to put one, and any prose that tries is discarded by the parser.
* Nothing here is permitted to return a valuation, a growth rate, a moat
  rating, a target price, or a probability. The parsers drop numeric fields
  that are not one of the structurally expected ones.

If the API is unavailable, every method raises rather than falling back to the
stub. A silent downgrade would mean a study ran with no extraction and no
review while its report said otherwise.
"""
from __future__ import annotations

import json
import re
from typing import Any, Sequence

from src.config import Config, get_config
from src.llm.contract import (
    Extraction, ExtractionKind, ForensicsResult, LLMAdapter, Objection,
    PreregDraft, ReviewResult,
)

DEFAULT_MODEL = "claude-sonnet-4-5"
MAX_DOCUMENT_CHARS = 400_000

EXTRACTION_SYSTEM = """\
You extract structured facts from Indian company filings.

Rules, all mandatory:
1. Return ONLY facts stated in the document. Never infer, estimate, or complete.
2. For every field, return the exact character offset in the document where the
   supporting text begins, and the exact quoted text at that offset. Both are
   verified mechanically against the source; a mismatch discards the field.
3. If a field is not stated in the document, omit it. An omitted field is
   correct; a guessed one is a defect.
4. Never return a valuation, a growth forecast, a quality rating, a target
   price, or a probability. You are not being asked for judgement.

Respond with JSON only: {"extractions": [{"field_name": str, "value": ...,
"char_offset": int, "quoted_text": str}]}
"""

REVIEW_SYSTEM = """\
You are an adversarial reviewer of quantitative factor research. Your ONLY job
is to argue for rejection.

You may not approve, endorse, score, rank, rate, or express confidence in any
result. You have no mechanism for saying a study is good. If you find nothing
to object to, return an empty list — that is the absence of an objection, not
an endorsement, and you must not describe it as one.

Look specifically for:
- look-ahead paths that are not closed
- survivorship leaks in the universe construction
- specification choices that look tuned to the result
- cost assumptions that look optimistic, especially impact in illiquid names
- multiple-testing burden that is understated

Respond with JSON only: {"objections": [{"category": one of
["look_ahead","survivorship","specification_tuning","cost_optimism",
"multiple_testing","data_quality","other"], "claim": str,
"what_would_settle_it": str}]}

Do not include any other key. Fields named "score", "confidence", "severity",
"rating", or "approved" will be discarded.
"""

#: Keys stripped from any model response. §2: no LLM-generated number may
#: enter a calculation, and the cheapest way to guarantee that is to make such
#: fields unrepresentable downstream.
FORBIDDEN_KEYS = frozenset({
    "score", "confidence", "severity", "rating", "approved", "probability",
    "target_price", "valuation", "growth_rate", "moat", "recommendation",
})


class AnthropicUnavailable(RuntimeError):
    """The provider could not be reached or is not configured."""


class AnthropicAdapter(LLMAdapter):
    name = "anthropic"

    def __init__(self, config: Config | None = None, *, client: Any = None,
                 model: str = DEFAULT_MODEL) -> None:
        self.config = config or get_config()
        self.model = model
        self._client = client

    @property
    def client(self) -> Any:
        if self._client is None:
            try:
                import anthropic
            except ImportError as exc:
                raise AnthropicUnavailable(
                    "the `anthropic` package is not installed. Install it, or "
                    "keep LLM_MODE=stub — the platform runs fully without it."
                ) from exc
            self._client = anthropic.Anthropic(
                api_key=self.config.secret("ANTHROPIC_API_KEY").reveal()
            )
        return self._client

    def _complete(self, system: str, user: str, max_tokens: int = 4096) -> str:
        try:
            response = self.client.messages.create(
                model=self.model, max_tokens=max_tokens, system=system,
                messages=[{"role": "user", "content": user}],
            )
        except Exception as exc:  # provider errors are not our taxonomy
            raise AnthropicUnavailable(f"Anthropic request failed: {exc}") from exc
        parts = getattr(response, "content", [])
        return "".join(getattr(part, "text", "") for part in parts)

    # -- §15.1 extraction --------------------------------------------------

    def extract(self, document: str, kind: ExtractionKind,
                source_doc_hash: str) -> list[Extraction]:
        text = document[:MAX_DOCUMENT_CHARS]
        payload = _parse_json(self._complete(
            EXTRACTION_SYSTEM,
            f"Extraction kind: {kind}\n\nDocument:\n{text}",
        ))
        out = []
        for item in payload.get("extractions", []):
            if not isinstance(item, dict):
                continue
            item = _strip_forbidden(item)
            try:
                out.append(Extraction(
                    kind=kind, field_name=str(item["field_name"]),
                    value=item.get("value"),
                    source_doc_hash=source_doc_hash,
                    char_offset=int(item.get("char_offset", -1)),
                    quoted_text=str(item.get("quoted_text", "")),
                ))
            except (KeyError, TypeError, ValueError):
                continue
        # The caller must still run validated_extractions() against the full
        # document; this adapter does not get to decide what counts as located.
        return out

    # -- §15.2 pre-registration drafting -----------------------------------

    def draft_prereg(self, hypothesis: str, context: dict[str, Any]) -> PreregDraft:
        from src.prereg.registry import REQUIRED_FIELDS

        system = (
            "You draft pre-registration specifications for factor research. "
            "Output JSON with exactly these top-level keys: "
            f"{', '.join(REQUIRED_FIELDS)}. "
            "The primary metric's threshold must be stated relative to a "
            "benchmark, never in absolute return. Include at least one kill "
            "condition — a study that cannot fail is not a test. State what a "
            "null result does NOT rule out. Output JSON only."
        )
        spec = _parse_json(self._complete(
            system, f"Hypothesis: {hypothesis}\n\nContext: {json.dumps(context)}"))
        return PreregDraft(
            spec=spec,
            notes="DRAFT — never auto-committed (§15.2). A human must read every "
                  "field, decide whether it is what they actually meant to "
                  "pre-register, and commit it themselves.",
        )

    # -- §15.3 adversarial review ------------------------------------------

    def adversarial_review(self, report_markdown: str, prereg_hash: str) -> ReviewResult:
        payload = _parse_json(self._complete(
            REVIEW_SYSTEM, f"Study report:\n\n{report_markdown[:MAX_DOCUMENT_CHARS]}"))
        objections = []
        valid_categories = {
            "look_ahead", "survivorship", "specification_tuning",
            "cost_optimism", "multiple_testing", "data_quality", "other",
        }
        for item in payload.get("objections", []):
            if not isinstance(item, dict):
                continue
            item = _strip_forbidden(item)
            category = str(item.get("category", "other"))
            objections.append(Objection(
                category=category if category in valid_categories else "other",
                claim=str(item.get("claim", "")).strip(),
                what_would_settle_it=str(item.get("what_would_settle_it", "")).strip(),
            ))
        objections = [o for o in objections if o.claim]
        return ReviewResult(prereg_hash=prereg_hash, objections=objections)

    # -- §15.4 forensics ----------------------------------------------------

    def forensics(self, ledger_markdown: str, studies: Sequence[dict[str, Any]]
                  ) -> ForensicsResult:
        system = (
            "You perform offline forensic attribution across a ledger of factor "
            "studies. Identify patterns across studies: specifications that "
            "recur, families where results cluster, and signs that the ledger's "
            "multiple-testing burden is understated. Do not score, rank, or "
            "recommend. Output JSON: {\"observations\": [str]}"
        )
        payload = _parse_json(self._complete(
            system,
            f"Ledger:\n{ledger_markdown}\n\nStudies:\n{json.dumps(list(studies))[:100_000]}",
            max_tokens=8192,
        ))
        return ForensicsResult(
            observations=[str(o) for o in payload.get("observations", [])],
            studies_examined=len(studies),
        )


def _strip_forbidden(item: dict[str, Any]) -> dict[str, Any]:
    """Drop any key that would smuggle a model-generated judgement into data."""
    return {k: v for k, v in item.items() if k.lower() not in FORBIDDEN_KEYS}


def _parse_json(text: str) -> dict[str, Any]:
    """Parse a JSON response, tolerating a fenced code block around it."""
    text = (text or "").strip()
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1).strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start == -1 or end <= start:
            return {}
        try:
            payload = json.loads(text[start: end + 1])
        except json.JSONDecodeError:
            return {}
    return payload if isinstance(payload, dict) else {}


def get_adapter(config: Config | None = None) -> LLMAdapter:
    """Return the adapter the config selects. Stub is the default (§15)."""
    config = config or get_config()
    if config.llm_mode == "live":
        return AnthropicAdapter(config)
    from src.llm.stub import StubAdapter

    return StubAdapter()
