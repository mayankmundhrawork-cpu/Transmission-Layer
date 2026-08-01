"""Archive backfill CLI (§17 CP2).

    python -m src.archive.backfill --source bhavcopy --start 2022-04-01 --end 2025-03-31

Resumable by construction: every document already archived is a cache hit, so
re-running after an interruption costs SQLite lookups rather than requests. A
block halts the run immediately and reports how far it got — the right response
to a block is to wait, not to try harder.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys

from src.archive.fetchers.base import ArchiveFetcher, FetchSummary
from src.archive.fetchers.nse import (
    NseAsmGsmFetcher, NseBhavcopyFetcher, NseCorporateActionsFetcher,
    NseDelistedFetcher, NseFnoBanFetcher, NseIndexConstituentsFetcher,
    candidate_trading_days,
)
from src.archive.http import PoliteSession
from src.archive.store import open_archive
from src.config import get_config

#: Index slugs whose current constituent lists we archive. Historical membership
#: is reconstructed from circulars (§5) — see src/master/universe.py.
INDEX_SLUGS = ("nifty500", "niftysmallcap250", "niftymidcap150", "nifty50", "niftytotalmarket")


def _daily_keys(start: dt.date, end: dt.date) -> list[str]:
    return candidate_trading_days(start, end)


def _quarter_ranges(start: dt.date, end: dt.date) -> list[str]:
    """Corporate actions are served as date ranges, not per-day files."""
    keys, cursor = [], start
    while cursor <= end:
        nxt = min(cursor + dt.timedelta(days=90), end)
        keys.append(f"{cursor.isoformat()}_{nxt.isoformat()}")
        cursor = nxt + dt.timedelta(days=1)
    return keys


def build_plan(source: str, start: dt.date, end: dt.date) -> tuple[type[ArchiveFetcher], list[str]]:
    plans: dict[str, tuple[type[ArchiveFetcher], list[str]]] = {
        "bhavcopy": (NseBhavcopyFetcher, _daily_keys(start, end)),
        "fno_ban": (NseFnoBanFetcher, _daily_keys(start, end)),
        "corp_actions": (NseCorporateActionsFetcher, _quarter_ranges(start, end)),
        "delisted": (NseDelistedFetcher, ["delisted", "suspended"]),
        "indices": (NseIndexConstituentsFetcher, list(INDEX_SLUGS)),
        "surveillance": (
            NseAsmGsmFetcher,
            [f"{k}_{d}" for d in _daily_keys(start, end) for k in ("asm", "gsm")],
        ),
    }
    if source not in plans:
        raise SystemExit(f"unknown source {source!r}; expected one of {sorted(plans)}")
    return plans[source]


def run(source: str, start: dt.date, end: dt.date, *, force: bool = False,
        quiet: bool = False) -> FetchSummary:
    cfg = get_config()
    cfg.ensure_dirs()
    fetcher_cls, keys = build_plan(source, start, end)

    with open_archive() as archive:
        session = PoliteSession(
            min_interval_s=cfg.fetch_min_interval_s, max_retries=cfg.fetch_max_retries
        )
        fetcher = fetcher_cls(archive, session=session)

        pending = [k for k in keys if force or not fetcher.is_cached(k)]
        if not quiet:
            print(
                f"{source}: {len(keys)} documents in range, {len(pending)} to fetch "
                f"({len(keys) - len(pending)} already archived). "
                f"At {cfg.fetch_min_interval_s:.0f}s/request this is roughly "
                f"{len(pending) * cfg.fetch_min_interval_s / 60:.0f} minutes.",
                file=sys.stderr,
            )

        def progress(key: str, summary: FetchSummary) -> None:
            if not quiet and summary.attempted % 25 == 0:
                print(f"  … {key}: {summary}", file=sys.stderr)

        summary = fetcher.fetch_many(keys, force=force, on_progress=progress)
        if not quiet:
            print(summary, file=sys.stderr)
            if summary.blocked:
                print(
                    "Halted on a block. Everything fetched so far is archived; "
                    "wait a few hours and re-run — it resumes from the cache.",
                    file=sys.stderr,
                )
        return summary


def main(argv: list[str] | None = None) -> int:
    cfg = get_config()
    parser = argparse.ArgumentParser(
        prog="python -m src.archive.backfill",
        description="Fetch source documents into the append-only archive.",
    )
    parser.add_argument("--source", default="bhavcopy",
                        help="bhavcopy | corp_actions | delisted | indices | "
                             "surveillance | fno_ban")
    parser.add_argument("--start", default=cfg.history_start.isoformat())
    parser.add_argument("--end", default=dt.date.today().isoformat())
    parser.add_argument("--force", action="store_true",
                        help="re-fetch documents already archived (creates new entries)")
    parser.add_argument("--stats", action="store_true",
                        help="print archive statistics and exit")
    parser.add_argument("--verify", action="store_true",
                        help="re-hash every blob and report corruption")
    args = parser.parse_args(argv)

    if args.stats:
        with open_archive() as archive:
            print(json.dumps(archive.stats(), indent=2))
        return 0

    if args.verify:
        with open_archive() as archive:
            problems = archive.verify()
        print(json.dumps({"ok": not problems, "problems": problems}, indent=2))
        return 1 if problems else 0

    summary = run(
        args.source, dt.date.fromisoformat(args.start), dt.date.fromisoformat(args.end),
        force=args.force,
    )
    return 2 if summary.blocked else (1 if summary.failed else 0)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
