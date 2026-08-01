"""Typed configuration for the factor research platform (BUILD_SPEC §0, §4).

Two rules this module exists to enforce:

1. **Config is typed and validated at import.** A bad `UNIVERSE_TIER` or a
   `HISTORY_START` that isn't a date fails loudly here, not three layers deep
   in a backtest that has already burned an hour.
2. **Secrets are never values.** `Secret` holds a *name*, not a credential.
   The credential is read from the environment (or `.env`) at the moment it is
   used and is never cached, never placed in `os.environ` by us, and never
   representable as a string. `repr()` and `str()` both redact, so a secret
   cannot leak through an f-string, a traceback frame, or a log line.

Everything in §0 is overridable by environment variable so the same code runs
in CI, on a desktop install, and on a dev box without edits.
"""
from __future__ import annotations

import datetime as dt
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Final, Literal, get_args

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT: Final[Path] = Path(__file__).resolve().parent.parent
ENV_FILE: Final[Path] = REPO_ROOT / ".env"

UniverseTier = Literal["nifty500", "smallcap_inclusive", "total_market"]
RebalanceFreq = Literal["monthly", "quarterly"]
LLMMode = Literal["stub", "live"]

# Secrets the platform may ask for. ANTHROPIC_API_KEY is only required when
# LLM_MODE=live; the rest only gate *new fetches*, never the research pipeline
# (§5 — "If the daemon fails, the research pipeline must still run").
SECRET_NAMES: Final[tuple[str, ...]] = (
    "DHAN_CLIENT_ID",
    "DHAN_API_KEY",
    "DHAN_API_SECRET",
    "DHAN_TOTP_SEED",
    "ANTHROPIC_API_KEY",
)


# ---------------------------------------------------------------------------
# .env handling
# ---------------------------------------------------------------------------

def _parse_env_file(path: Path) -> dict[str, str]:
    """Minimal KEY=VALUE parser. Deliberately not python-dotenv: we never want
    a library deciding to export these into ``os.environ`` behind our back."""
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        # Strip one layer of matching quotes, the common .env convention.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key:
            out[key] = value
    return out


def _env_lookup(name: str) -> str | None:
    """Process environment wins over `.env` so CI secrets override a local file."""
    val = os.environ.get(name)
    if val is not None and val != "":
        return val
    val = _parse_env_file(ENV_FILE).get(name)
    return val if val else None


class Secret:
    """A named credential that is resolved on demand and never stored.

    The value is read at :meth:`reveal` time and returned to the caller; this
    object keeps no reference to it. Both ``repr`` and ``str`` redact, which is
    what stops a credential from riding along in a log line or a traceback.
    """

    __slots__ = ("_name",)

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def present(self) -> bool:
        """True if the credential is resolvable right now. Does not expose it."""
        return _env_lookup(self._name) is not None

    def reveal(self) -> str:
        """Return the credential. Call this as late as possible and do not
        assign the result to anything longer-lived than the call that needs it."""
        val = _env_lookup(self._name)
        if val is None:
            raise MissingSecret(
                f"{self._name} is not set. Add it to {ENV_FILE.name} "
                f"(see .env.example) or export it in the environment."
            )
        return val

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"<Secret {self._name} [redacted]>"

    __str__ = __repr__

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Secret) and other._name == self._name

    def __hash__(self) -> int:
        return hash(("Secret", self._name))


class MissingSecret(RuntimeError):
    """Raised when a credential is needed but not configured."""


class ConfigError(ValueError):
    """Raised when configuration is present but invalid."""


# ---------------------------------------------------------------------------
# Coercion helpers — each reports the offending key, because a config error at
# import time with no key name is a 20-minute scavenger hunt.
# ---------------------------------------------------------------------------

def _get_str(key: str, default: str) -> str:
    return _env_lookup(key) or default


def _get_float(key: str, default: float) -> float:
    raw = _env_lookup(key)
    if raw is None:
        return default
    try:
        return float(raw)
    except ValueError as exc:
        raise ConfigError(f"{key} must be a number, got {raw!r}") from exc


def _get_int(key: str, default: int) -> int:
    raw = _env_lookup(key)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ConfigError(f"{key} must be an integer, got {raw!r}") from exc


def _get_bool(key: str, default: bool) -> bool:
    raw = _env_lookup(key)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _get_date(key: str, default: str) -> dt.date:
    raw = _env_lookup(key) or default
    try:
        return dt.date.fromisoformat(raw)
    except ValueError as exc:
        raise ConfigError(f"{key} must be ISO date YYYY-MM-DD, got {raw!r}") from exc


def _get_literal(key: str, default: str, allowed: tuple[str, ...]) -> str:
    val = _env_lookup(key) or default
    if val not in allowed:
        raise ConfigError(f"{key} must be one of {allowed}, got {val!r}")
    return val


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Config:
    """Resolved platform configuration. Frozen: nothing mutates config at runtime."""

    # --- §0 fill-ins -------------------------------------------------------
    capital_inr: float
    universe_tier: UniverseTier
    benchmark: str
    max_position_pct: float
    max_sector_pct: float
    min_positions: int
    rebalance_freq: RebalanceFreq
    history_start: dt.date
    llm_mode: LLMMode

    # --- §9 liquidity ------------------------------------------------------
    max_participation_pct: float  # of trailing median daily traded value

    # --- §14 execution safety ---------------------------------------------
    live_enabled: bool
    registered_static_ip: str | None

    # --- paths -------------------------------------------------------------
    repo_root: Path
    archive_dir: Path
    db_dir: Path
    prereg_dir: Path
    reports_dir: Path

    # --- fetch politeness (§5) --------------------------------------------
    fetch_min_interval_s: float
    fetch_max_retries: int

    secrets: dict[str, Secret] = field(default_factory=dict, repr=False)

    # -- derived ------------------------------------------------------------
    @property
    def max_position_inr(self) -> float:
        return self.capital_inr * self.max_position_pct / 100.0

    @property
    def is_smallcap_tier(self) -> bool:
        return self.universe_tier in ("smallcap_inclusive", "total_market")

    def secret(self, name: str) -> Secret:
        try:
            return self.secrets[name]
        except KeyError as exc:
            raise ConfigError(
                f"Unknown secret {name!r}; known: {sorted(self.secrets)}"
            ) from exc

    def validate(self) -> None:
        """Loud, structural checks. Called at construction — §3 says invariants
        are assertions that fail, not comments that hope."""
        if self.capital_inr <= 0:
            raise ConfigError("CAPITAL_INR must be positive")
        if not 0 < self.max_position_pct <= 100:
            raise ConfigError("MAX_POSITION_PCT must be in (0, 100]")
        if not 0 < self.max_sector_pct <= 100:
            raise ConfigError("MAX_SECTOR_PCT must be in (0, 100]")
        if self.min_positions < 1:
            raise ConfigError("MIN_POSITIONS must be >= 1")
        if not 0 < self.max_participation_pct <= 100:
            raise ConfigError("MAX_PARTICIPATION_PCT must be in (0, 100]")
        # A position cap below 1/N makes the minimum-position floor unreachable.
        if self.max_position_pct * self.min_positions < 100.0:
            raise ConfigError(
                f"MAX_POSITION_PCT ({self.max_position_pct}) x MIN_POSITIONS "
                f"({self.min_positions}) = {self.max_position_pct * self.min_positions:.1f}%"
                " < 100%: the constraints cannot both be satisfied."
            )
        if self.history_start >= dt.date.today():
            raise ConfigError("HISTORY_START must be in the past")
        if self.llm_mode == "live" and not self.secrets["ANTHROPIC_API_KEY"].present():
            raise ConfigError(
                "LLM_MODE=live requires ANTHROPIC_API_KEY. Set it in .env, "
                "or use LLM_MODE=stub (the default) to run without an API key."
            )

    def ensure_dirs(self) -> None:
        for path in (self.archive_dir, self.db_dir, self.reports_dir):
            path.mkdir(parents=True, exist_ok=True)


def load_config(repo_root: Path | None = None) -> Config:
    """Build a :class:`Config` from environment + `.env`, applying §0 defaults."""
    root = Path(repo_root) if repo_root else REPO_ROOT
    data_dir = Path(_get_str("DATA_DIR", str(root / "data")))

    cfg = Config(
        # CAPITAL_INR default is the deployable book this platform was
        # commissioned for (₹10,00,000). Override in .env; never commit a real
        # number you'd rather not publish.
        capital_inr=_get_float("CAPITAL_INR", 1_000_000.0),
        universe_tier=_get_literal(
            "UNIVERSE_TIER", "smallcap_inclusive", get_args(UniverseTier)
        ),  # type: ignore[arg-type]
        benchmark=_get_str("BENCHMARK", "NIFTY_500_TRI"),
        max_position_pct=_get_float("MAX_POSITION_PCT", 4.0),
        max_sector_pct=_get_float("MAX_SECTOR_PCT", 25.0),
        min_positions=_get_int("MIN_POSITIONS", 25),
        rebalance_freq=_get_literal(
            "REBALANCE_FREQ", "quarterly", get_args(RebalanceFreq)
        ),  # type: ignore[arg-type]
        history_start=_get_date("HISTORY_START", "2010-04-01"),
        llm_mode=_get_literal("LLM_MODE", "stub", get_args(LLMMode)),  # type: ignore[arg-type]
        max_participation_pct=_get_float("MAX_PARTICIPATION_PCT", 5.0),
        # §14: live trading is off unless explicitly, deliberately enabled.
        live_enabled=_get_bool("LIVE_ENABLED", False),
        registered_static_ip=_env_lookup("DHAN_REGISTERED_IP"),
        repo_root=root,
        archive_dir=data_dir / "archive",
        db_dir=data_dir / "db",
        prereg_dir=root / "prereg",
        reports_dir=data_dir / "reports",
        fetch_min_interval_s=_get_float("FETCH_MIN_INTERVAL_S", 2.0),
        fetch_max_retries=_get_int("FETCH_MAX_RETRIES", 4),
        secrets={name: Secret(name) for name in SECRET_NAMES},
    )
    cfg.validate()
    return cfg


_CACHED: Config | None = None


def get_config(refresh: bool = False) -> Config:
    """Process-wide config singleton. `refresh=True` re-reads the environment."""
    global _CACHED
    if _CACHED is None or refresh:
        _CACHED = load_config()
    return _CACHED
