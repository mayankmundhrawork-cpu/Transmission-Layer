"""Shared fixtures for the factor-platform test suite.

Every test runs against a temporary repo root with a temporary `.env`, so a
developer's real credentials and real archive are never in the blast radius —
and so a test can never silently pass because a live `.env` happened to supply
something the code should have demanded explicitly.
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from src import config as config_mod


@pytest.fixture(autouse=True)
def isolated_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Point config at a throwaway `.env` and clear any inherited platform vars.

    Autouse: isolation you have to opt into is isolation you will forget.
    """
    env_file = tmp_path / ".env"
    env_file.write_text("", encoding="utf-8")
    monkeypatch.setattr(config_mod, "ENV_FILE", env_file)

    for name in config_mod.SECRET_NAMES:
        monkeypatch.delenv(name, raising=False)
    for name in (
        "CAPITAL_INR", "UNIVERSE_TIER", "BENCHMARK", "MAX_POSITION_PCT",
        "MAX_SECTOR_PCT", "MIN_POSITIONS", "REBALANCE_FREQ", "HISTORY_START",
        "LLM_MODE", "MAX_PARTICIPATION_PCT", "LIVE_ENABLED", "DATA_DIR",
        "DHAN_REGISTERED_IP", "FETCH_MIN_INTERVAL_S", "FETCH_MAX_RETRIES",
    ):
        monkeypatch.delenv(name, raising=False)

    # Force config to resolve fresh rather than reuse a cached singleton.
    monkeypatch.setattr(config_mod, "_CACHED", None)
    return env_file


@pytest.fixture
def cfg(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> config_mod.Config:
    """A validated Config rooted entirely inside tmp_path."""
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    conf = config_mod.load_config(repo_root=tmp_path)
    conf.ensure_dirs()
    return conf


@pytest.fixture
def today() -> dt.date:
    return dt.date.today()
