"""Build the derived store from the archive (§5-§7).

    python -m src.store.build            # incremental
    python -m src.store.build --rebuild  # from scratch

The derived store is disposable by design: `--rebuild` drops it and replays
every archived document. If that loses something, it means data was written
here that should have been in the archive.
"""
from __future__ import annotations

import argparse
import json
import sys

from src.archive.store import open_archive
from src.config import get_config
from src.store.schema import open_store_db, rebuild as rebuild_db

STAGES = ("bhavcopy", "delisted", "corp_actions", "indices", "surveillance",
          "fundamentals", "screener")


def main(argv: list[str] | None = None) -> int:
    cfg = get_config()
    parser = argparse.ArgumentParser(
        prog="python -m src.store.build",
        description="Replay the archive into the derived store.")
    parser.add_argument("--rebuild", action="store_true",
                        help="drop the store and rebuild from scratch")
    parser.add_argument("--stages", default=",".join(STAGES),
                        help=f"comma-separated subset of {','.join(STAGES)}")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    cfg.ensure_dirs()
    db_path = cfg.db_dir / "platform.sqlite"
    conn = rebuild_db(db_path) if args.rebuild else open_store_db(db_path)

    from src.store.ingest import Ingestor

    stages = [s.strip() for s in args.stages.split(",") if s.strip()]
    reports = {}
    with open_archive() as archive:
        ingestor = Ingestor(archive, conn)
        runners = {
            "bhavcopy": ingestor.ingest_bhavcopy,
            "delisted": ingestor.ingest_delisted,
            "corp_actions": ingestor.ingest_corporate_actions,
            "indices": ingestor.ingest_index_constituents,
            "surveillance": ingestor.ingest_surveillance,
            "fundamentals": ingestor.ingest_fundamentals,
            "screener": ingestor.ingest_screener_prototype,
        }
        for stage in stages:
            if stage not in runners:
                print(f"unknown stage {stage!r}", file=sys.stderr)
                return 2
            report = runners[stage]()
            reports[stage] = {
                "documents": report.documents, "rows": report.rows_written,
                "unresolved_symbols": report.unresolved_symbols,
                "errors": len(report.errors),
            }
            if not args.json:
                print(report, file=sys.stderr)

    # Fill listing windows from observed trading where no delisting notice exists.
    ingestor.master.close_listing_windows()
    conn.close()

    if args.json:
        print(json.dumps(reports, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
