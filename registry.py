"""The live series registry: backbone (Layer 0) + news-admitted universe (Layer 1).

Everything that iterates "all tracked series" (fetch, engine, app, digest)
reads from here instead of a hardcoded list. The dynamic layer comes from
data/universe.json, written by universe.py during the scheduled run — this
module only READS state, so the Streamlit app stays fetch-free at open.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from backbone import BACKBONE, CLASSES, LINKED_GROUPS, NEWS_ALIASES  # re-export

DATA_DIR = Path(__file__).parent / "data"
UNIVERSE_JSON = DATA_DIR / "universe.json"

_BACKBONE_IDS = {s["id"] for s in BACKBONE}
_BACKBONE_SYMBOLS = {s.get("symbol") for s in BACKBONE if s.get("symbol")}


def symbol_to_id(symbol: str) -> str:
    """Stable, filesystem/CSV-safe series id for a dynamic symbol."""
    sid = symbol.lower()
    sid = re.sub(r"[^a-z0-9]+", "_", sid).strip("_")
    return f"dyn_{sid}"


def load_universe() -> dict:
    """Raw universe state ({} if the file doesn't exist yet)."""
    if not UNIVERSE_JSON.exists():
        return {"updated": None, "members": {}, "candidates": {}}
    try:
        return json.loads(UNIVERSE_JSON.read_text(encoding="utf-8"))
    except Exception:
        # A corrupt state file must not sink the board; start fresh.
        return {"updated": None, "members": {}, "candidates": {}}


def dynamic_specs() -> list[dict]:
    """Engine-compatible specs for the active news-admitted members."""
    uni = load_universe()
    specs = []
    for sym, m in sorted(uni.get("members", {}).items()):
        if m.get("status") != "active":
            continue
        if sym in _BACKBONE_SYMBOLS:
            continue  # already covered by the backbone
        specs.append({
            "id": symbol_to_id(sym),
            "market": m.get("cls", "EQUITIES"),
            "source": "yfinance",
            "symbol": sym,
            "freq": "eod",
            "framework": {},
            # class-aware selectivity: news-admitted names need a bigger move
            # to go amber than the macro backbone (see V3 notes · D-selectivity)
            "amber_z": m.get("amber_z"),  # None → engine default per settings
            "dynamic": True,
            "name": m.get("name", sym),
        })
    return specs


def load_registry() -> list[dict]:
    """Full iteration order: backbone first, then dynamic members."""
    return list(BACKBONE) + dynamic_specs()


def registry_index() -> dict[str, dict]:
    return {s["id"]: s for s in load_registry()}


__all__ = [
    "BACKBONE", "CLASSES", "LINKED_GROUPS", "NEWS_ALIASES",
    "load_registry", "load_universe", "dynamic_specs", "registry_index",
    "symbol_to_id",
]
