"""SYNTH_V2 · MOSPI WPI sub-index fetch + VINTAGE store.

The one genuinely-new automatable shock input (EXPOSURE_SCOPING.md §1.3): the
non-matrix input costs (natural rubber, coarse chemicals) come from MOSPI WPI
sub-indices — monthly, ~2-week publication lag, free from eaindustry.nic.in.

The store is BY VINTAGE, as-published, NEVER overwritten on revision. WPI prints
provisional and is revised; grading a pre-registered screen against a later
revised value is lookahead — the same error S4 point A forbids for channel
state. So every value is keyed by (series, publish_date), and
`wpi_asof(series, registration_date)` returns the value that EXISTED at
registration, never today's revision.

Granularity (confirmed against eaindustry / MOSPI, 2026-07-23):
  * rubber IS a WPI commodity group with item-level indices — obtainable.
  * a specific pigment (TiO2) is NOT a line; it sits under the coarse "chemicals
    & chemical products" group. A coarse bucket is a `quality: proxy` fact,
    tagged, never passed off as the input. The published Margin Trap piece used
    a coarse sector input-basket and held up.
  * WPI rebased 2011-12 -> 2022-23 effective June 2026. A base change is a
    discontinuity: a % move that straddles the base boundary is NOT valid, so
    each vintage stores its `base` and cross-base comparisons are flagged.

WPI staleness is first-class (monthly + lag => a shock can be ~6 weeks old);
`wpi_staleness` surfaces it for the packet's data-quality header.

NOTE: the eaindustry release is an Excel/HTML table, not a clean API. The
VINTAGE STORE below is complete and tested; `fetch_and_store` leaves the file
PARSE as a marked interface to wire once the current release format is confirmed
against the live download — it never guesses values.
"""
from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

WPI_DIR = Path(__file__).parent / "data" / "wpi"
VINTAGES_JSON = WPI_DIR / "vintages.json"
CURRENT_BASE = "2022-23"        # effective June 2026

# Which sub-indices we track, with an HONEST granularity/quality tag. `mospi_item`
# is left None until confirmed against the live release — the fetch is not wired
# on a guessed code.
WPI_SERIES = {
    "wpi_rubber": {"desc": "rubber & rubber products (commodity group)",
                   "granularity": "group", "quality": "derived",
                   "mospi_item": None},
    "wpi_chemicals": {"desc": "chemicals & chemical products (coarse)",
                      "granularity": "coarse", "quality": "proxy",
                      "mospi_item": None},
    "wpi_basic_metals": {"desc": "basic metals (coarse)",
                         "granularity": "coarse", "quality": "proxy",
                         "mospi_item": None},
}


def load_vintages() -> dict:
    if VINTAGES_JSON.exists():
        try:
            return json.loads(VINTAGES_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"series": {}}


def store_vintage(series: str, publish_date: str, period: str, value: float,
                  base: str = CURRENT_BASE) -> bool:
    """Store one as-published value. Returns False (no-op) if this (series,
    publish_date) already exists — a revision NEVER overwrites the original
    vintage; a later revision is a NEW publish_date, stored alongside."""
    WPI_DIR.mkdir(parents=True, exist_ok=True)
    v = load_vintages()
    s = v["series"].setdefault(series, {})
    if publish_date in s:
        return False                                   # never overwrite a vintage
    s[publish_date] = {"period": period, "value": float(value), "base": base}
    VINTAGES_JSON.write_text(json.dumps(v, indent=2), encoding="utf-8")
    return True


def _d(x) -> date | None:
    try:
        return datetime.fromisoformat(str(x)).date()
    except Exception:
        return None


def wpi_asof(series: str, registration_date: str, vintages: dict | None = None) -> dict | None:
    """The value as it EXISTED at registration_date — the latest vintage whose
    publish_date <= registration_date. No lookahead: a revision published after
    registration is invisible here."""
    v = vintages or load_vintages()
    s = v.get("series", {}).get(series, {})
    reg = _d(registration_date)
    if reg is None or not s:
        return None
    eligible = [(pd, rec) for pd, rec in s.items()
                if _d(pd) is not None and _d(pd) <= reg]
    if not eligible:
        return None
    pd_best, rec = max(eligible, key=lambda kv: _d(kv[0]))
    return {"series": series, "publish_date": pd_best, **rec}


def wpi_staleness(rec: dict, asof_date: str, max_age_days: int = 45) -> dict:
    """Age of the WPI reading's PERIOD vs asof — monthly + lag means a shock can
    be weeks old. `stale` when older than max_age_days (first-class, for the
    packet header)."""
    per = _d((rec or {}).get("period") + "-01") if rec and rec.get("period") \
        else None
    a = _d(asof_date)
    if per is None or a is None:
        return {"stale": True, "age_days": None, "reason": "no period/asof"}
    age = (a - per).days
    return {"stale": age > max_age_days, "age_days": age}


def same_base(a: dict, b: dict) -> bool:
    """Two vintages are comparable (a valid % move) only within the same base."""
    return bool(a and b and a.get("base") == b.get("base"))


def fetch_and_store(publish_date: str | None = None) -> dict:
    """Fetch the latest WPI release and store each tracked series as a vintage.

    INTERFACE ONLY — the eaindustry release is an Excel/HTML table whose exact
    columns for the 2022-23 base must be confirmed against the live download
    before parsing. Wiring the parser here without the real file would be
    guessing values, which the store forbids. Returns a status dict.
    """
    raise NotImplementedError(
        "confirm the eaindustry.nic.in 2022-23-base release format (item codes "
        "for WPI_SERIES, publish-date column) against the live download, then "
        "wire the parser to call store_vintage per series. The vintage store, "
        "wpi_asof and staleness are complete and tested; only the source parse "
        "is pending confirmation.")


if __name__ == "__main__":
    print("WPI series tracked (granularity/quality honest):")
    for k, m in WPI_SERIES.items():
        print(f"  {k:18} {m['granularity']:7} quality={m['quality']:9} {m['desc']}")
    print(f"current base: {CURRENT_BASE} | vintages file: {VINTAGES_JSON}")
