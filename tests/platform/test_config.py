"""Config layer tests (§0, §4).

The tests that matter here are the redaction ones. Everything else is
coercion plumbing; a secret that can be str()'d into a log line is the kind of
bug you find in someone else's incident report.
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from src import config as config_mod
from src.config import ConfigError, MissingSecret, Secret, load_config


# --- defaults ---------------------------------------------------------------

def test_defaults_match_build_spec(cfg):
    assert cfg.capital_inr == 1_000_000.0
    assert cfg.universe_tier == "smallcap_inclusive"
    assert cfg.benchmark == "NIFTY_500_TRI"
    assert cfg.max_position_pct == 4.0
    assert cfg.max_sector_pct == 25.0
    assert cfg.min_positions == 25
    assert cfg.rebalance_freq == "quarterly"
    assert cfg.history_start == dt.date(2010, 4, 1)
    assert cfg.llm_mode == "stub", "stub is the default: the system runs with no API key"
    assert cfg.max_participation_pct == 5.0


def test_live_execution_is_off_by_default(cfg):
    """§14: LIVE_ENABLED defaults False. This is a safety default, not a preference."""
    assert cfg.live_enabled is False


def test_derived_position_cap(cfg):
    assert cfg.max_position_inr == pytest.approx(40_000.0)  # 4% of ₹10L


def test_env_overrides_defaults(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CAPITAL_INR", "2500000")
    monkeypatch.setenv("UNIVERSE_TIER", "nifty500")
    monkeypatch.setenv("REBALANCE_FREQ", "monthly")
    cfg = load_config(repo_root=tmp_path)
    assert cfg.capital_inr == 2_500_000.0
    assert cfg.universe_tier == "nifty500"
    assert cfg.rebalance_freq == "monthly"


def test_dotenv_file_is_read(tmp_path, monkeypatch, isolated_env):
    isolated_env.write_text(
        '# a comment\nCAPITAL_INR=750000\nBENCHMARK="NIFTY_SMALLCAP_250_TRI"\n\n',
        encoding="utf-8",
    )
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    cfg = load_config(repo_root=tmp_path)
    assert cfg.capital_inr == 750_000.0
    assert cfg.benchmark == "NIFTY_SMALLCAP_250_TRI", "quotes should be stripped"


def test_process_env_wins_over_dotenv(tmp_path, monkeypatch, isolated_env):
    isolated_env.write_text("CAPITAL_INR=111\n", encoding="utf-8")
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CAPITAL_INR", "222")
    assert load_config(repo_root=tmp_path).capital_inr == 222.0


# --- validation -------------------------------------------------------------

@pytest.mark.parametrize(
    "key,bad",
    [
        ("UNIVERSE_TIER", "largecap"),
        ("REBALANCE_FREQ", "daily"),
        ("LLM_MODE", "yolo"),
        ("HISTORY_START", "01-04-2010"),
        ("CAPITAL_INR", "lots"),
        ("MIN_POSITIONS", "twenty"),
    ],
)
def test_invalid_config_fails_loudly(tmp_path, monkeypatch, key, bad):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv(key, bad)
    with pytest.raises(ConfigError) as exc:
        load_config(repo_root=tmp_path)
    assert key in str(exc.value), "the error must name the offending key"


def test_negative_capital_rejected(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CAPITAL_INR", "-1")
    with pytest.raises(ConfigError, match="CAPITAL_INR"):
        load_config(repo_root=tmp_path)


def test_unsatisfiable_position_constraints_rejected(tmp_path, monkeypatch):
    """2% cap x 25 positions can only fill 50% of the book — that is a
    contradiction, and it should surface at config load, not at rebalance."""
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("MAX_POSITION_PCT", "2.0")
    monkeypatch.setenv("MIN_POSITIONS", "25")
    with pytest.raises(ConfigError, match="cannot both be satisfied"):
        load_config(repo_root=tmp_path)


def test_future_history_start_rejected(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("HISTORY_START", str(dt.date.today() + dt.timedelta(days=1)))
    with pytest.raises(ConfigError, match="HISTORY_START"):
        load_config(repo_root=tmp_path)


def test_live_llm_without_key_rejected(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("LLM_MODE", "live")
    with pytest.raises(ConfigError, match="ANTHROPIC_API_KEY"):
        load_config(repo_root=tmp_path)


# --- secrets ----------------------------------------------------------------

def test_secret_never_reveals_itself_in_repr_or_str(monkeypatch):
    monkeypatch.setenv("DHAN_API_SECRET", "super-secret-value")
    s = Secret("DHAN_API_SECRET")

    assert "super-secret-value" not in repr(s)
    assert "super-secret-value" not in str(s)
    assert "super-secret-value" not in f"{s}"
    assert "super-secret-value" not in "{}".format(s)
    assert "super-secret-value" not in f"{s!r}"
    assert "redacted" in repr(s)
    # ...but it is retrievable when explicitly asked for.
    assert s.reveal() == "super-secret-value"


def test_secret_holds_no_value_attribute(monkeypatch):
    """__slots__ is the enforcement: there is nowhere to stash the credential."""
    monkeypatch.setenv("DHAN_API_SECRET", "super-secret-value")
    s = Secret("DHAN_API_SECRET")
    s.reveal()
    assert not hasattr(s, "__dict__")
    assert set(Secret.__slots__) == {"_name"}
    for slot in Secret.__slots__:
        assert getattr(s, slot) == "DHAN_API_SECRET"


def test_secret_reads_at_call_time_not_construction(monkeypatch):
    s = Secret("DHAN_API_KEY")
    assert s.present() is False
    monkeypatch.setenv("DHAN_API_KEY", "later")
    assert s.present() is True
    assert s.reveal() == "later"


def test_missing_secret_raises_with_guidance():
    s = Secret("DHAN_TOTP_SEED")
    with pytest.raises(MissingSecret, match=r"\.env\.example"):
        s.reveal()


def test_config_repr_excludes_secrets(cfg, monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-do-not-print-me")
    text = repr(cfg)
    assert "sk-ant-do-not-print-me" not in text
    assert "secrets" not in text, "the secrets dict is repr=False"


def test_all_spec_secrets_are_registered(cfg):
    assert set(cfg.secrets) == {
        "DHAN_CLIENT_ID", "DHAN_API_KEY", "DHAN_API_SECRET",
        "DHAN_TOTP_SEED", "ANTHROPIC_API_KEY",
    }
    assert all(isinstance(v, Secret) for v in cfg.secrets.values())


def test_unknown_secret_name_rejected(cfg):
    with pytest.raises(ConfigError, match="Unknown secret"):
        cfg.secret("AWS_SECRET_ACCESS_KEY")


# --- repo hygiene -----------------------------------------------------------

def test_env_is_gitignored():
    """§0: `.env` in .gitignore in the first commit. Assert it, don't trust it."""
    ignored = (Path(__file__).resolve().parents[2] / ".gitignore").read_text()
    assert ".env" in ignored


def test_env_example_exists_and_has_no_values():
    """The example file must be a template, not a leak."""
    example = Path(__file__).resolve().parents[2] / ".env.example"
    assert example.exists()
    for line in example.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        if key.strip() in config_mod.SECRET_NAMES:
            assert value.strip() == "", f"{key} must be empty in .env.example"


def test_directories_are_created(cfg):
    assert cfg.archive_dir.is_dir()
    assert cfg.db_dir.is_dir()
    assert cfg.reports_dir.is_dir()
