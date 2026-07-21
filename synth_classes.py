"""SYNTH_V2 · asset-class taxonomy + causation-of-direction prior.

Not a hardcoded channel — a prior on the asset-class GRAPH, read straight
from the registry's `market` field (INDICES / FX / RATES / COMMODITIES /
CRYPTO / DERIVED / EQUITIES). The transmission premise itself assumes a
direction of causation across classes; this encodes the one rule that
follows from it:

    a single-name equity is not a driver of a macro series.

Macro (indices, rates, FX, commodities, vol-as-index, cross-asset spreads)
transmits DOWN to single names and across macro; a single stock's
idiosyncratic move fanning out onto crude, Bunds or silver is a correlation
artifact, never a mechanism. Single names may be TARGETS of macro drivers and
may drive other single names; only single-name -> macro is inadmissible.

Because the rule is stated over classes and the classes come from the
registry, no series id appears here as a literal — adding a stock to the
universe classifies it automatically.
"""
from __future__ import annotations

from functools import lru_cache

MACRO_MARKETS = frozenset(
    {"INDICES", "FX", "RATES", "COMMODITIES", "CRYPTO", "DERIVED"})
SINGLE_NAME_MARKETS = frozenset({"EQUITIES"})


@lru_cache(maxsize=1)
def _market_map() -> dict[str, str]:
    from registry import load_registry
    return {s["id"]: s.get("market") for s in load_registry()}


def market_of(sid: str) -> str | None:
    return _market_map().get(sid)


def is_macro(sid: str) -> bool:
    return market_of(sid) in MACRO_MARKETS


def is_single_name(sid: str) -> bool:
    return market_of(sid) in SINGLE_NAME_MARKETS


def driver_admissible(driver: str, target: str) -> tuple[bool, str | None]:
    """(admissible, reason_if_not). Only macro may drive macro. This FAILS
    CLOSED: any driver that is not positively classified macro is inadmissible
    for a macro target — a single-name equity OR an unclassified series (a
    registry gap must never silently admit a stock as a driver of the S&P).
    Non-macro targets are unconstrained (macro can drive single names; single
    names can drive single names)."""
    if is_macro(target) and not is_macro(driver):
        reason = ("single_name_drives_macro" if is_single_name(driver)
                  else "unclassified_drives_macro")
        return False, reason
    return True, None
