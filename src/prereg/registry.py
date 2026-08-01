"""Pre-registration registry (§12).

A study is a committed JSON file in `prereg/`. It is loaded, hashed, and
verified; the pipeline may not write to it (§3.6).

The hash is the mechanism that makes the whole thing work. Every output
artifact records the hash of the specification it was run under, so:

* changing a spec after results exist does not invalidate the old report — it
  creates a *new study* with a new hash, and the old report remains valid for
  the spec it names;
* a report cannot be silently re-attributed to a spec it was not run under;
* "we always meant to test it this way" is checkable rather than assertable.

Read-only is enforced in three places: this module opens files only for
reading, `assert_pipeline_cannot_write` fails loudly if a write path is
attempted, and a test asserts no module under `src/` writes into `prereg/`.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Sequence

#: Fields §12 requires. A spec missing any of these is not a pre-registration —
#: it is a plan, and plans are what you write after seeing results.
REQUIRED_FIELDS = (
    "study_id",
    "hypothesis",
    "factor",
    "preprocessing",
    "universe_tier",
    "evaluation_window",
    "rebalance_frequency",
    "forward_return_horizon_days",
    "null_structure",
    "primary_metric",
    "secondary_metrics",
    "era_splits",
    "kill_conditions",
    "interpretation_asymmetry",
)

REQUIRED_PREPROCESSING_FIELDS = (
    "winsorise_lower_pct", "winsorise_upper_pct", "standardise", "sector_neutralise",
)

REQUIRED_PRIMARY_METRIC_FIELDS = ("name", "threshold", "relative_to")


class PreregError(ValueError):
    """A pre-registration is missing, malformed, or has been altered."""


class PreregWriteAttempt(RuntimeError):
    """The pipeline tried to write to prereg/. §3.6 forbids it."""


@dataclass(frozen=True)
class Preregistration:
    """A loaded, hashed study specification."""

    study_id: str
    path: Path
    spec_hash: str
    raw: dict[str, Any]

    # -- convenience accessors --------------------------------------------

    @property
    def hypothesis(self) -> str:
        return self.raw["hypothesis"]

    @property
    def factor_name(self) -> str:
        return self.raw["factor"]["name"]

    @property
    def universe_tier(self) -> str:
        return self.raw["universe_tier"]

    @property
    def window(self) -> tuple[str, str]:
        w = self.raw["evaluation_window"]
        return w["start"], w["end"]

    @property
    def horizon_days(self) -> int:
        return int(self.raw["forward_return_horizon_days"])

    @property
    def rebalance_frequency(self) -> str:
        return self.raw["rebalance_frequency"]

    @property
    def primary_metric(self) -> dict[str, Any]:
        return self.raw["primary_metric"]

    @property
    def era_splits(self) -> list[str]:
        return list(self.raw.get("era_splits") or [])

    @property
    def kill_conditions(self) -> list[str]:
        return list(self.raw.get("kill_conditions") or [])

    @property
    def interpretation_asymmetry(self) -> dict[str, Any]:
        return self.raw["interpretation_asymmetry"]

    def preprocess_spec(self):
        from src.eval.crosssec import PreprocessSpec

        p = self.raw["preprocessing"]
        return PreprocessSpec(
            winsorise_lower_pct=float(p["winsorise_lower_pct"]),
            winsorise_upper_pct=float(p["winsorise_upper_pct"]),
            standardise=bool(p["standardise"]),
            sector_neutralise=bool(p["sector_neutralise"]),
            rank_transform=bool(p.get("rank_transform", False)),
        )

    def spec_fingerprint(self) -> str:
        """Hash of the specification choices that define a distinct *trial*.

        Deliberately narrower than `spec_hash`: editing the hypothesis prose
        changes the file hash but does not create a new statistical test, while
        changing the winsorisation percentiles does. The multiple-testing
        counter keys on this.
        """
        material = {
            "factor": self.raw["factor"],
            "preprocessing": self.raw["preprocessing"],
            "universe_tier": self.raw["universe_tier"],
            "rebalance_frequency": self.raw["rebalance_frequency"],
            "horizon": self.raw["forward_return_horizon_days"],
            "primary_metric": self.raw["primary_metric"],
        }
        blob = json.dumps(material, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(blob.encode()).hexdigest()[:16]

    def assert_window(self, start: str, end: str) -> None:
        """§11: no optional stopping.

        The harness refuses to run on a window differing from the registered
        one unless an extension has been registered first — and an extension is
        only valid if it declares it was made before results were viewed.
        """
        registered_start, registered_end = self.window
        if (start, end) == (registered_start, registered_end):
            return

        for extension in self.raw.get("window_extensions", []):
            if (extension.get("start") == start and extension.get("end") == end):
                if not extension.get("declared_before_results_viewed"):
                    raise PreregError(
                        f"{self.study_id}: window extension to {start}..{end} does "
                        "not declare that it was made before results were viewed. "
                        "An extension declared afterwards is optional stopping."
                    )
                return

        raise PreregError(
            f"{self.study_id}: requested window {start}..{end} differs from the "
            f"registered window {registered_start}..{registered_end}, and no "
            "extension covering it has been registered. Register the extension "
            "first — running a different window and reporting it as the "
            "registered study is optional stopping."
        )

    def provenance(self) -> dict[str, Any]:
        """Stamped into every output artifact."""
        return {
            "study_id": self.study_id,
            "prereg_hash": self.spec_hash,
            "spec_fingerprint": self.spec_fingerprint(),
            "prereg_file": self.path.name,
        }


def hash_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path: Path | str) -> Preregistration:
    """Load, validate, and hash a pre-registration. Read-only."""
    path = Path(path)
    if not path.exists():
        raise PreregError(f"no pre-registration at {path}")

    spec_hash = hash_file(path)
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PreregError(f"{path.name}: not valid JSON — {exc}") from exc

    validate(raw, label=path.name)
    return Preregistration(
        study_id=raw["study_id"], path=path, spec_hash=spec_hash, raw=raw
    )


def validate(raw: dict[str, Any], label: str = "<spec>") -> None:
    """Check every §12 field is present and structurally sound."""
    missing = [f for f in REQUIRED_FIELDS if f not in raw]
    if missing:
        raise PreregError(
            f"{label}: missing required §12 fields: {', '.join(missing)}. "
            "A specification missing these is a plan, not a pre-registration."
        )

    if not isinstance(raw.get("factor"), dict) or "name" not in raw["factor"]:
        raise PreregError(f"{label}: 'factor' must be an object with a 'name'")

    preprocessing = raw.get("preprocessing")
    if not isinstance(preprocessing, dict):
        raise PreregError(f"{label}: 'preprocessing' must be an object")
    missing_pp = [f for f in REQUIRED_PREPROCESSING_FIELDS if f not in preprocessing]
    if missing_pp:
        raise PreregError(
            f"{label}: preprocessing is missing {', '.join(missing_pp)}. "
            "§10.1 requires every preprocessing choice be declared, not defaulted."
        )

    window = raw.get("evaluation_window")
    if not isinstance(window, dict) or "start" not in window or "end" not in window:
        raise PreregError(f"{label}: 'evaluation_window' needs 'start' and 'end'")
    if window["start"] >= window["end"]:
        raise PreregError(f"{label}: evaluation window start must precede end")

    metric = raw.get("primary_metric")
    if not isinstance(metric, dict):
        raise PreregError(f"{label}: 'primary_metric' must be an object")
    missing_m = [f for f in REQUIRED_PRIMARY_METRIC_FIELDS if f not in metric]
    if missing_m:
        raise PreregError(
            f"{label}: primary_metric is missing {', '.join(missing_m)}. "
            "§12 requires the threshold be stated against the benchmark."
        )
    if metric["relative_to"] in (None, "", "absolute"):
        raise PreregError(
            f"{label}: primary_metric.relative_to must name a benchmark. "
            "§11: a factor returning 14% when the benchmark returned 15% is a "
            "negative result, and an absolute threshold cannot express that."
        )

    asymmetry = raw.get("interpretation_asymmetry")
    if not isinstance(asymmetry, dict) or not asymmetry.get("null_result_does_not_rule_out"):
        raise PreregError(
            f"{label}: interpretation_asymmetry must state what a null result "
            "does NOT rule out. Without it, a null gets read as a refutation."
        )

    if not raw.get("kill_conditions"):
        raise PreregError(
            f"{label}: declare at least one kill condition. A study that cannot "
            "fail is not a test."
        )


def load_all(directory: Path | str) -> dict[str, Preregistration]:
    directory = Path(directory)
    if not directory.exists():
        return {}
    out = {}
    for path in sorted(directory.glob("*.json")):
        prereg = load(path)
        out[prereg.study_id] = prereg
    return out


def assert_pipeline_cannot_write(path: Path | str) -> None:
    """§3.6 guard. Call before any write that might land inside prereg/."""
    resolved = Path(path).resolve()
    for parent in (resolved, *resolved.parents):
        if parent.name == "prereg":
            raise PreregWriteAttempt(
                f"the pipeline attempted to write to {resolved}, inside prereg/. "
                "Pre-registrations are read-only to the code (§3.6): a spec the "
                "pipeline can edit is not a pre-registration."
            )


# ---------------------------------------------------------------------------
# Ledger (§12)
# ---------------------------------------------------------------------------

LEDGER_STATUSES = ("registered", "run", "GO", "NO-GO", "unresolved")


@dataclass
class LedgerEntry:
    study_id: str
    spec_hash: str
    status: str
    date: str
    note: str = ""

    def __post_init__(self) -> None:
        if self.status not in LEDGER_STATUSES:
            raise ValueError(
                f"status must be one of {LEDGER_STATUSES}, got {self.status!r}")


def render_ledger(entries: Sequence[LedgerEntry]) -> str:
    """Render `prereg/LEDGER.md`.

    Negative results stay in the ledger permanently (§12). This function has no
    filter parameter and no way to omit a NO-GO — the only honest ledger is a
    complete one, and a ledger showing only successes is a marketing document.
    """
    header = [
        "# Study ledger",
        "",
        "Every study ever registered in this repo, with its status. Negative",
        "results stay here permanently — a ledger showing only what worked is a",
        "record of survivorship, not of research.",
        "",
        "| Study | Spec hash | Status | Date | Note |",
        "|---|---|---|---|---|",
    ]
    rows = [
        f"| {e.study_id} | `{e.spec_hash[:12]}` | {e.status} | {e.date} | {e.note} |"
        for e in entries
    ]
    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    footer = [
        "",
        f"**{len(entries)} " + ("study" if len(entries) == 1 else "studies")
        + " registered.** "
        + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())),
        "",
        "_Multiple-testing note: every row here counts against the "
        "Benjamini-Hochberg correction applied in `src/eval/stats.py`. "
        "The count is the point._",
    ]
    return "\n".join([*header, *rows, *footer]) + "\n"
