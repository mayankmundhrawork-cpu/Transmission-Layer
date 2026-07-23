"""Central settings & secrets access.

Keys are read lazily so that modules which don't need a secret never require it:
- the Streamlit app only reads committed data files → needs NO keys;
- fetch.py needs FRED_API_KEY at fetch time;
- extract.py uses ANTHROPIC_API_KEY only if present (optional LLM tier).
"""
from __future__ import annotations

import os


def get_fred_key() -> str:
    key = (os.environ.get("FRED_API_KEY") or "").strip()
    if not key:
        raise RuntimeError(
            "FRED_API_KEY is not set. Export it before running the fetch, e.g.:\n"
            "  PowerShell:  $env:FRED_API_KEY = '<your-key>'\n"
            "  bash/zsh:    export FRED_API_KEY='<your-key>'\n"
            "In CI it is injected from the FRED_API_KEY repository secret."
        )
    return key


def get_anthropic_key() -> str | None:
    """Optional. When absent the LLM extraction tier is silently skipped."""
    key = (os.environ.get("ANTHROPIC_API_KEY") or "").strip()
    return key or None


# ── universe tunables (see V3_BUILD_NOTES.md · Decisions) ──────────────
UNIVERSE_CAP = 40            # max dynamic (news-admitted) members
ADMIT_SCORE = 2.0            # EWMA mention score needed for admission
ADMIT_MIN_FEEDS = 2          # distinct feeds that must have mentioned it
DECAY_HALF_LIFE_DAYS = 3.0   # mention-score half-life
EVICT_SCORE = 0.3            # below this AND quiet → evicted
EVICT_QUIET_DAYS = 10        # days without a mention before eviction allowed
MAX_LOOKUPS_PER_RUN = 12     # yfinance Search budget per scheduled run
MAX_BACKFILL_PER_RUN = 12    # full-history backfills per run (new symbols)
HEADLINE_WINDOW_DAYS = 7     # rolling headline store window

# ── selectivity tunables ───────────────────────────────────────────────
DYNAMIC_AMBER_Z = 2.0        # stricter amber bar for news-admitted equities
EVENT_CORR_THRESHOLD = 0.65  # |60d return corr| to cluster flagged series
SURFACE_FLOOR = 3.2          # min event score to earn a card on the board
MAX_EVENT_CARDS = 8

# ── research accelerator (v5) ──────────────────────────────────────────
CORR_WINDOW = 60             # primary rolling-correlation window (sessions)
CORR_CONTEXT = 252           # long-window context correlation
MIN_CORR = 0.35              # persist pairs at/above this |rho|
MAX_LAG = 5                  # lead-lag search depth (sessions)
LAGGARD_MIN_CORR = 0.50      # neighbour correlation to qualify as a laggard
LAGGARD_MAX_Z = 1.0          # neighbour |z20| below this = "hasn't moved yet"

ARTICLE_FETCH_MAX_PER_RUN = 20
ARTICLE_TIMEOUT = 10         # seconds per article fetch
ARTICLE_MAX_CHARS = 6000     # excerpt cap stored per article

THESIS_MAX_PER_RUN = 8       # hard ceiling on LLM thesis generations per run
THESIS_MAX_TOKENS = 900

PATTERN_MIN_GAP = 5          # sessions between distinct historical matches
PATTERN_HORIZONS = (5, 20)   # aftermath windows
ANALOGUE_TOP = 5             # nearest historical analogues per event


SYNTH_V2 = (os.environ.get("SYNTH_V2", "1").strip() not in ("0", "", "false"))
SYNTH_LIVE_TTL = 180         # in-app live-price cache (owner ruling 1: 3-min tick)


def get_llm_backend() -> dict | None:
    """Zero-budget LLM routing: free OpenAI-compatible endpoints only.
    Priority: Groq free tier, then OpenRouter :free models. No key -> None,
    and thesis.py renders its rule-based skeleton instead. NO PAID PLANS."""
    groq = (os.environ.get("GROQ_API_KEY") or "").strip()
    if groq:
        return {"name": "groq", "key": groq,
                "url": "https://api.groq.com/openai/v1/chat/completions",
                "model": "llama-3.3-70b-versatile"}
    orouter = (os.environ.get("OPENROUTER_API_KEY") or "").strip()
    if orouter:
        return {"name": "openrouter", "key": orouter,
                "url": "https://openrouter.ai/api/v1/chat/completions",
                "model": "meta-llama/llama-3.3-70b-instruct:free"}
    return None
