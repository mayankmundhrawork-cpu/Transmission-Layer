"""Release-calendar engine — computes next occurrence + days-until per release.

Named `release_calendar` (not `calendar`) so it does not shadow Python's stdlib
`calendar` module, which is used below for monthrange and may be imported
indirectly by pandas. See V2_BUILD_NOTES.md Decisions & Assumptions.

Pure stdlib datetime + the calendar registry. No fetching, no external API.
The Streamlit app calls build_calendar() at open; nothing is persisted.

Holiday handling: weekend rolls only (Sat/Sun → next Monday). Public holidays
are NOT modelled (no free stdlib holiday calendar); a release that officially
slips for a holiday may show a date one working day early. Logged as an
assumption in V2_BUILD_NOTES.md.
"""
from __future__ import annotations

import calendar as _cal  # stdlib
from datetime import date, timedelta
from typing import Any

from calendar_config import RELEASES

RECENT_WINDOW_DAYS = 1   # "released in last 24h" window
SOON_DAYS = 3            # highlight threshold


def _roll_to_weekday(d: date) -> date:
    """Push Sat/Sun forward to the next Monday; weekdays unchanged."""
    while d.weekday() >= 5:  # 5=Sat, 6=Sun
        d += timedelta(days=1)
    return d


def _monthly_day_on(year: int, month: int, day: int) -> date:
    """The rolled nth-day-of-month date, clamped to the month's length."""
    last = _cal.monthrange(year, month)[1]
    d = date(year, month, min(day, last))
    return _roll_to_weekday(d)


def _add_month(year: int, month: int) -> tuple[int, int]:
    return (year + 1, 1) if month == 12 else (year, month + 1)


def _sub_month(year: int, month: int) -> tuple[int, int]:
    return (year - 1, 12) if month == 1 else (year, month - 1)


def _next_prev_monthly_day(today: date, day: int) -> tuple[date, date | None]:
    """Next occurrence on/after today and the most recent one strictly before."""
    this = _monthly_day_on(today.year, today.month, day)
    if this >= today:
        nxt = this
        py, pm = _sub_month(today.year, today.month)
        prev = _monthly_day_on(py, pm, day)
    else:
        ny, nm = _add_month(today.year, today.month)
        nxt = _monthly_day_on(ny, nm, day)
        prev = this
    return nxt, prev


def _next_prev_weekly(today: date, weekday: int) -> tuple[date, date]:
    ahead = (weekday - today.weekday()) % 7
    nxt = today + timedelta(days=ahead)          # today if it matches
    prev = nxt - timedelta(days=7) if nxt > today else nxt - timedelta(days=7)
    # most recent strictly-before occurrence
    back = (today.weekday() - weekday) % 7
    prev = today - timedelta(days=back if back != 0 else 7)
    return nxt, prev


def _next_prev_business(today: date) -> tuple[date, date]:
    nxt = _roll_to_weekday(today)                 # today if a weekday
    prev = today - timedelta(days=1)
    while prev.weekday() >= 5:
        prev -= timedelta(days=1)
    return nxt, prev


def _next_prev_fixed(today: date, dates: list[str]) -> tuple[date | None, date | None]:
    parsed = sorted(date.fromisoformat(s) for s in dates)
    nxt = next((d for d in parsed if d >= today), None)
    prev = next((d for d in reversed(parsed) if d < today), None)
    return nxt, prev


def _occurrences(today: date, rule: dict) -> tuple[date | None, date | None]:
    t = rule["type"]
    if t == "monthly_day":
        return _next_prev_monthly_day(today, rule["day"])
    if t == "weekly":
        return _next_prev_weekly(today, rule["weekday"])
    if t == "daily_business":
        return _next_prev_business(today)
    if t == "fixed":
        return _next_prev_fixed(today, rule["dates"])
    raise ValueError(f"unknown rule type: {t}")


def build_calendar(today: date | None = None) -> dict[str, Any]:
    """Return {'upcoming': [...], 'recent': [...], 'today': iso}.

    upcoming: every release with a computable next date, sorted by days_until.
    recent:   releases whose previous occurrence fell within the last 24h.
    """
    today = today or date.today()
    upcoming: list[dict[str, Any]] = []
    recent: list[dict[str, Any]] = []

    for rel in RELEASES:
        try:
            nxt, prev = _occurrences(today, rel["rule"])
        except Exception as e:  # a malformed rule must not sink the whole panel
            nxt, prev = None, None
            note = f"rule error: {e}"
        else:
            note = rel.get("verify", "")

        if nxt is not None:
            upcoming.append({
                "name": rel["name"],
                "market": rel["market"],
                "next_date": nxt.isoformat(),
                "days_until": (nxt - today).days,
                "threshold": rel["threshold"],
                "url": rel["url"],
                "soon": (nxt - today).days <= SOON_DAYS,
                "verify": note,
            })

        if prev is not None and 0 <= (today - prev).days <= RECENT_WINDOW_DAYS:
            recent.append({
                "name": rel["name"],
                "market": rel["market"],
                "released_date": prev.isoformat(),
                "threshold": rel["threshold"],
                "url": rel["url"],
            })

    upcoming.sort(key=lambda r: r["days_until"])
    recent.sort(key=lambda r: r["released_date"], reverse=True)
    return {"today": today.isoformat(), "upcoming": upcoming, "recent": recent}


if __name__ == "__main__":
    cal = build_calendar()
    print(f"=== RELEASE CALENDAR as of {cal['today']} ===\n")
    print("UPCOMING (sorted by proximity):")
    for r in cal["upcoming"]:
        mark = " <== SOON" if r["soon"] else ""
        v = f"  [VERIFY: {r['verify']}]" if r["verify"] else ""
        print(f"  {r['days_until']:>4}d  {r['next_date']}  {r['name']:38} "
              f"({r['market']}){mark}{v}")
    print("\nRELEASED IN LAST 24h:")
    if not cal["recent"]:
        print("  (none)")
    for r in cal["recent"]:
        print(f"  {r['released_date']}  {r['name']:38} ({r['market']})  {r['url']}")
