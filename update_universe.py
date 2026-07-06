"""Scheduled-run orchestrator: headlines → extraction → universe update.

Run:  python update_universe.py
(placed before fetch.py in the workflow so newly-admitted symbols are
backfilled in the same run)
"""
from __future__ import annotations

import sys

from headlines import pull_and_update
from universe import update_universe


def main() -> int:
    print("-- headlines --")
    hrep = pull_and_update()
    print(f"  +{hrep['new_items']} new · {hrep['total_items']} in window · "
          f"feeds ok {len(hrep['ok'])} / failed {len(hrep['failed'])} / "
          f"empty {len(hrep['empty'])}")

    print("-- universe --")
    urep = update_universe()
    print(f"  new headlines processed : {urep['new_headlines']}")
    print(f"  member mentions counted : {urep['member_mentions']}")
    print(f"  members (dynamic layer) : {urep['members']}")
    print(f"  candidates pending      : {urep['candidates']}")
    print(f"  lookup budget remaining : {urep['lookup_budget_left']}")
    for tag, key in (("ADMIT", "admitted"), ("REJECT", "rejected"),
                     ("DEFER", "deferred"), ("EVICT", "evicted")):
        for entry in urep[key]:
            print(f"  {tag:6} {entry}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
