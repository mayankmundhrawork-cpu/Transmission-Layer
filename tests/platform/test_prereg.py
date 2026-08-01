"""Pre-registration system tests (§12, §3.6) — the CP9 gate.

The property being defended: a specification cannot be edited into agreement
with results after the fact. Hashing makes the attempt visible; the read-only
guard makes the easy version of it impossible.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from src.prereg.registry import (
    LedgerEntry, PreregError, PreregWriteAttempt, Preregistration,
    assert_pipeline_cannot_write, hash_file, load, load_all, render_ledger,
    validate,
)

REPO = Path(__file__).resolve().parents[2]
PREREG_DIR = REPO / "prereg"
NOISE_SPEC = PREREG_DIR / "PREREG-000-noise-control.json"


@pytest.fixture
def spec_dict():
    return json.loads(NOISE_SPEC.read_text(encoding="utf-8"))


def write_spec(tmp_path, spec, name="s.json"):
    path = tmp_path / name
    path.write_text(json.dumps(spec), encoding="utf-8")
    return path


# --- hashing ----------------------------------------------------------------

def test_spec_is_hashed_on_load():
    prereg = load(NOISE_SPEC)
    assert prereg.spec_hash == hash_file(NOISE_SPEC)
    assert len(prereg.spec_hash) == 64


def test_editing_a_spec_changes_its_hash(tmp_path, spec_dict):
    original = load(write_spec(tmp_path, spec_dict, "a.json"))
    spec_dict["preprocessing"]["winsorise_lower_pct"] = 5.0
    edited = load(write_spec(tmp_path, spec_dict, "b.json"))
    assert original.spec_hash != edited.spec_hash, (
        "an edited spec must be a new study, not the same one with new numbers"
    )


def test_prose_edits_do_not_create_a_new_trial(tmp_path, spec_dict):
    """The trial fingerprint is narrower than the file hash: rewording the
    hypothesis is not a new statistical test, but changing the winsorisation
    is."""
    before = load(write_spec(tmp_path, spec_dict, "a.json"))
    spec_dict["hypothesis"] = spec_dict["hypothesis"] + " (clarified wording)"
    after = load(write_spec(tmp_path, spec_dict, "b.json"))
    assert before.spec_hash != after.spec_hash
    assert before.spec_fingerprint() == after.spec_fingerprint()


def test_specification_edits_do_create_a_new_trial(tmp_path, spec_dict):
    before = load(write_spec(tmp_path, spec_dict, "a.json"))
    spec_dict["forward_return_horizon_days"] = 126
    after = load(write_spec(tmp_path, spec_dict, "b.json"))
    assert before.spec_fingerprint() != after.spec_fingerprint()


def test_provenance_is_stamped(spec_dict):
    provenance = load(NOISE_SPEC).provenance()
    assert set(provenance) == {"study_id", "prereg_hash", "spec_fingerprint",
                               "prereg_file"}


# --- validation -------------------------------------------------------------

@pytest.mark.parametrize("field", [
    "hypothesis", "factor", "preprocessing", "universe_tier",
    "evaluation_window", "null_structure", "primary_metric", "kill_conditions",
    "interpretation_asymmetry", "era_splits", "secondary_metrics",
    "rebalance_frequency", "forward_return_horizon_days",
])
def test_missing_required_field_is_rejected(spec_dict, field):
    spec_dict.pop(field)
    with pytest.raises(PreregError, match=field):
        validate(spec_dict)


def test_preprocessing_must_declare_every_choice(spec_dict):
    """§10.1: all choices come from the pre-registration, not from a default."""
    spec_dict["preprocessing"].pop("winsorise_lower_pct")
    with pytest.raises(PreregError, match="not defaulted"):
        validate(spec_dict)


def test_primary_metric_must_be_relative_to_a_benchmark(spec_dict):
    """§11: a factor returning 14% when the benchmark returned 15% is a
    negative result, and an absolute threshold cannot express that."""
    spec_dict["primary_metric"]["relative_to"] = "absolute"
    with pytest.raises(PreregError, match="negative result"):
        validate(spec_dict)


def test_interpretation_asymmetry_is_mandatory(spec_dict):
    spec_dict["interpretation_asymmetry"] = {"null_result_rules_out": "things"}
    with pytest.raises(PreregError, match="does NOT rule out"):
        validate(spec_dict)


def test_a_study_that_cannot_fail_is_rejected(spec_dict):
    spec_dict["kill_conditions"] = []
    with pytest.raises(PreregError, match="not a test"):
        validate(spec_dict)


def test_backwards_window_is_rejected(spec_dict):
    spec_dict["evaluation_window"] = {"start": "2023-01-01", "end": "2019-01-01"}
    with pytest.raises(PreregError, match="start must precede end"):
        validate(spec_dict)


def test_malformed_json_is_reported_clearly(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(PreregError, match="not valid JSON"):
        load(path)


def test_missing_file_is_reported_clearly(tmp_path):
    with pytest.raises(PreregError, match="no pre-registration"):
        load(tmp_path / "nope.json")


# --- §3.6 read-only ---------------------------------------------------------

def test_pipeline_cannot_write_into_prereg():
    with pytest.raises(PreregWriteAttempt, match="read-only"):
        assert_pipeline_cannot_write(PREREG_DIR / "sneaky.json")


def test_pipeline_cannot_write_into_a_prereg_subdirectory():
    with pytest.raises(PreregWriteAttempt):
        assert_pipeline_cannot_write(PREREG_DIR / "nested" / "deep.json")


def test_writing_elsewhere_is_fine(tmp_path):
    assert_pipeline_cannot_write(tmp_path / "report.md")


def test_no_module_under_src_writes_to_prereg():
    """Static check for the §3.6 invariant.

    Looks for a write call whose *target path* references the prereg
    directory — a string literal containing "prereg", or an identifier like
    PREREG_DIR. Matching any occurrence of the substring would flag
    `path.write_text(render(result, prereg))`, where `prereg` is just the spec
    being rendered, so the check inspects the path expression specifically.

    The guard function itself is exempt: naming the directory is its whole job.
    """
    write_calls = {"write_text", "write_bytes", "open", "mkdir", "touch", "unlink"}
    offenders = []

    def references_prereg_path(node: ast.AST) -> bool:
        for child in ast.walk(node):
            if isinstance(child, ast.Constant) and isinstance(child.value, str):
                if "prereg" in child.value.lower():
                    return True
            if isinstance(child, ast.Name) and "prereg" in child.id.lower() \
                    and child.id.isupper():
                return True
            if isinstance(child, ast.Attribute) and "prereg" in child.attr.lower() \
                    and "dir" in child.attr.lower():
                return True
        return False

    for path in sorted((REPO / "src").rglob("*.py")):
        if path.name == "registry.py" and path.parent.name == "prereg":
            continue
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            name = (func.attr if isinstance(func, ast.Attribute)
                    else func.id if isinstance(func, ast.Name) else "")
            if name not in write_calls:
                continue
            # The path is the receiver for `p.write_text(...)`, or the first
            # argument for `open(...)`.
            target = func.value if isinstance(func, ast.Attribute) else (
                node.args[0] if node.args else None)
            if target is not None and references_prereg_path(target):
                offenders.append(f"{path.relative_to(REPO)}:{node.lineno}")
    assert not offenders, f"writes into prereg/ detected: {offenders}"


def test_the_prereg_write_checker_catches_a_planted_write():
    """Positive control for the check above."""
    planted = 'from pathlib import Path\nPath("prereg/x.json").write_text("{}")\n'
    tree = ast.parse(planted)
    found = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "write_text":
            for child in ast.walk(node.func.value):
                if isinstance(child, ast.Constant) and "prereg" in str(child.value):
                    found = True
    assert found, "the static check would not catch a direct write to prereg/"


# --- the committed specs ----------------------------------------------------

def test_every_committed_spec_is_valid():
    specs = load_all(PREREG_DIR)
    assert specs, "no pre-registrations committed"
    for study_id, prereg in specs.items():
        assert prereg.study_id == study_id
        assert prereg.preprocess_spec() is not None


def test_noise_control_declares_a_positive_result_is_a_bug():
    """The control study's interpretation must say that a positive result is a
    bug report, not a finding — otherwise someone will one day 'discover' it."""
    prereg = load(NOISE_SPEC)
    text = prereg.interpretation_asymmetry["positive_result_does_not_establish"]
    assert "broken" in text.lower() or "bug" in text.lower()


# --- ledger -----------------------------------------------------------------

def test_ledger_renders_all_statuses():
    entries = [
        LedgerEntry("PREREG-000-noise-control", "abc123def456", "NO-GO",
                    "2026-08-01", "control; null is the desired outcome"),
        LedgerEntry("PREREG-001-value", "def456abc123", "registered", "2026-08-01"),
    ]
    text = render_ledger(entries)
    assert "NO-GO" in text
    assert "registered" in text
    assert "2 studies registered" in text


def test_ledger_cannot_omit_negative_results():
    """§12: negative results stay permanently. `render_ledger` has no filter
    parameter, so there is no supported way to produce a ledger of successes."""
    import inspect

    params = set(inspect.signature(render_ledger).parameters)
    assert params == {"entries"}, (
        "render_ledger gained a parameter; if it can filter, a ledger of only "
        "successes becomes expressible"
    )


def test_ledger_rejects_an_unknown_status():
    with pytest.raises(ValueError, match="status must be one of"):
        LedgerEntry("x", "h", "probably fine", "2026-08-01")


def test_committed_ledger_lists_every_committed_spec():
    ledger = (PREREG_DIR / "LEDGER.md")
    assert ledger.exists(), "prereg/LEDGER.md is required by §12"
    text = ledger.read_text(encoding="utf-8")
    for study_id in load_all(PREREG_DIR):
        assert study_id in text, f"{study_id} is not in the ledger"
