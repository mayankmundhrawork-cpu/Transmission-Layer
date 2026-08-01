"""§18.5 — structural no-leak test.

A static check that no module under `src/factors/` or `src/eval/` reaches the
raw fundamentals table or `latest()`.

This is the layer of the §3.1 defence that does not depend on anyone running
the right code path. The runtime guard in `bitemporal.py` only fires if the
offending line executes; this fires at CI time whether it executes or not, and
catches the version of the mistake that only runs in one rarely-taken branch.

The check has a positive control (`test_the_checker_catches_a_planted_leak`)
because a static analyser that silently matches nothing is worse than no
analyser — it reports success forever.
"""
from __future__ import annotations

import ast
from pathlib import Path

import pytest

from src.store.schema import FUNDAMENTALS_TABLE

SRC = Path(__file__).resolve().parents[2] / "src"
GUARDED_PACKAGES = ("factors", "eval")

#: Names that mean "unfiltered fundamentals" wherever they appear.
FORBIDDEN_NAMES = {"latest", "FUNDAMENTALS_TABLE"}


def guarded_modules() -> list[Path]:
    files: list[Path] = []
    for package in GUARDED_PACKAGES:
        files.extend(sorted((SRC / package).rglob("*.py")))
    return files


def find_leaks(source: str, label: str = "<source>") -> list[str]:
    """Return human-readable descriptions of every leak in a module's source."""
    problems: list[str] = []

    # 1. The private table name, however it is spelled.
    if FUNDAMENTALS_TABLE in source:
        problems.append(
            f"{label}: names the private fundamentals table {FUNDAMENTALS_TABLE!r} "
            "directly; read through store.as_of(date) instead"
        )

    tree = ast.parse(source, filename=label)
    for node in ast.walk(tree):
        # 2. Importing the table name or latest() by any route.
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name in FORBIDDEN_NAMES:
                    problems.append(
                        f"{label}:{node.lineno}: imports {alias.name!r} from "
                        f"{node.module!r}"
                    )
        # 3. Any call to something named `latest`, bound or free.
        if isinstance(node, ast.Call):
            func = node.func
            name = (func.attr if isinstance(func, ast.Attribute)
                    else func.id if isinstance(func, ast.Name) else None)
            if name in FORBIDDEN_NAMES:
                problems.append(
                    f"{label}:{node.lineno}: calls {name}() — research code may "
                    "only read fundamentals through as_of(date)"
                )
        # 4. Attribute access to `.latest` even without calling it (e.g. passing
        #    the bound method somewhere else to be called later).
        if isinstance(node, ast.Attribute) and node.attr in FORBIDDEN_NAMES:
            problems.append(
                f"{label}:{node.lineno}: references .{node.attr}"
            )
    return problems


@pytest.mark.acceptance
@pytest.mark.parametrize("path", guarded_modules(), ids=lambda p: str(p.name))
def test_acceptance_5_no_module_reaches_unfiltered_fundamentals(path: Path):
    """No module under factors/ or eval/ may reach latest() or the raw table."""
    label = str(path.relative_to(SRC.parent))
    problems = find_leaks(path.read_text(encoding="utf-8"), label)
    assert not problems, "look-ahead leak:\n  " + "\n  ".join(problems)


@pytest.mark.acceptance
def test_the_checker_catches_a_planted_leak():
    """Positive control. A static check that matches nothing reports success
    forever; this proves the checker actually fires."""
    planted = [
        f"import pandas as pd\nx = pd.read_sql('SELECT * FROM {FUNDAMENTALS_TABLE}', c)\n",
        "def compute(store):\n    return store.latest()\n",
        "from src.store.schema import FUNDAMENTALS_TABLE\n",
        "def compute(store):\n    fn = store.latest\n    return fn()\n",
    ]
    for source in planted:
        assert find_leaks(source), f"checker failed to flag:\n{source}"


@pytest.mark.acceptance
def test_the_checker_passes_clean_code():
    """Negative control: legitimate as_of usage must not be flagged."""
    clean = (
        "def compute(store, as_of_date, universe):\n"
        "    facts = store.as_of_latest_period(as_of_date, ['revenue'])\n"
        "    return facts.reindex(universe)\n"
    )
    assert find_leaks(clean) == []


def test_guarded_packages_are_actually_scanned():
    """If the glob stops matching — a rename, a moved package — this test
    would pass vacuously. Assert it is looking at real files."""
    modules = guarded_modules()
    assert len(modules) >= 2
    assert any(p.parent.name == "factors" for p in modules)
    assert any(p.parent.name == "eval" for p in modules)


def test_research_packages_do_not_import_the_schema_module():
    """factors/ and eval/ should reach the store through its API, never through
    the schema module where the table name lives."""
    for path in guarded_modules():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == "src.store.schema":
                pytest.fail(
                    f"{path.name}:{node.lineno} imports src.store.schema; "
                    "research code should use src.store.bitemporal.as_of"
                )
