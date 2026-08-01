# Point-in-Time Fundamental Factor Research Platform

Research infrastructure for answering whether a factor has out-of-sample
predictive content on NSE/BSE equities — with look-ahead and survivorship bias
made structurally impossible rather than merely avoided.

This lives under `src/` and is **separate from the intraday board** at the repo
root (`app.py`, `digest.py`, …). The two share a repository, not a runtime:
separate dependency file, separate CI workflow, separate entry points.

> This is a research platform, not a trading bot. Live execution is off by
> default and stays off until you deliberately enable it and type a
> per-rebalance confirmation.

---

## Install the desktop program

1. Go to the repo's **Actions → Desktop build (Windows installer)**, open the
   most recent successful run, and download the
   `PITFactorPlatform-<version>-setup` artifact. (Tagged releases also attach
   the installer to the GitHub Release page.)
2. Unzip and run the `.exe`. No Python required.
3. Launch **PIT Factor Research Platform** from the Start menu.

On first launch the store is empty and the dashboard says so. Populate it:

```
python -m src.archive.backfill --source bhavcopy --start 2022-04-01
python -m src.archive.backfill --source delisted
python -m src.archive.backfill --source indices
python -m src.store.build
```

Credentials go in `.env` under `%LOCALAPPDATA%\PITFactorPlatform\` — copy
`.env.example` and fill it in. Nothing in the research pipeline needs
credentials; they gate *new fetches* only.

### Running from source

```
python -m venv .venv && .venv/bin/pip install -r requirements-platform.txt
.venv/bin/python -m pytest tests/platform      # 463 tests
.venv/bin/python -m src.desktop.main           # native window
.venv/bin/python -m src.desktop.main --browser # or open in a browser
```

---

## The four layers

| Layer | What it is | Where |
|---|---|---|
| **Archive** | Immutable, content-addressed store of raw source documents with fetch timestamps. Append-only, enforced by SQLite triggers. | `src/archive/` |
| **Store** | Bitemporal database derived from the archive. Every fact carries the period it describes *and* the timestamp it became public. | `src/store/` |
| **Research** | Factor construction and evaluation against pre-registered hypotheses. Cannot read a live source. | `src/factors/`, `src/eval/` |
| **Deployment** | Portfolio construction and an execution adapter that is OFF by default. | `src/portfolio/`, `src/execution/` |

Nothing in the research layer reads from the network. Every result is
reproducible from a git commit plus an archive snapshot.

---

## The invariants, and how each is enforced

These are the things that make a factor result trustworthy. None of them is a
comment.

**Bitemporality.** `store.as_of(date)` is the only sanctioned read of
fundamentals. The table is named `_fundamental_fact_private`; `latest()` raises
`LookAheadViolation` if *anything in the call stack* belongs to `src.factors` or
`src.eval`; and a static AST check fails CI if either name appears in those
packages. The static check has its own positive control, because an analyser
that matches nothing reports success forever.

**Delisted-inclusive universe.** The candidate pool comes from
`SecurityMaster.listed_on(date)`, which includes securities since delisted,
merged, or suspended. There is deliberately no `currently_listed()` primitive to
reach for.

**ISIN is the key.** Symbols are validity-dated attributes.
`resolve_symbol("OLDNAME", 2023)` correctly returns nothing — which is what
stops a symbol-keyed join from splicing two companies' return series together at
a rename.

**Append-only archive.** Re-fetching a document creates a new entry sharing one
content-addressed blob. `UPDATE` and `DELETE` abort at the database level.

**No costless trades.** Statutory cost alone is strictly positive, so no input
combination yields a free fill. The spread estimator is floored because
Corwin-Schultz returns zero on exactly the illiquid names where the true spread
is widest.

**Pre-registration is read-only to the code.** Specs are hashed on load; the
pipeline cannot write into `prereg/` (runtime guard plus a static check).

---

## What the platform will not do

Per the build spec's exclusions, and enforced by the type system where possible:

- **No multi-agent debate.** No bull/bear/verdict agents.
- **No composite score with hand-chosen weights.** Factor exposures are reported
  as a vector; portfolio weighting defaults to equal.
- **No LLM-generated numbers.** `Objection` and `ReviewResult` have no
  `score`/`confidence`/`severity`/`approved` field, so adversarial review cannot
  become endorsement by drift. The Anthropic adapter strips a forbidden-key set
  from every response.
- **No sentiment scoring** as a factor input.
- **No auto-rebalancing** without an explicit human confirmation step.

The model layer has a veto and a pen. It never has a vote.

---

## Statistical protocol (the part that stops you fooling yourself)

- **Effective N**, from the eigenvalue participation ratio of the exposure
  correlation matrix. 46 correlated names came out as ~13 independent bets in the
  calibration run. Every t-statistic uses effective N.
- **Newey-West** standard errors on the IC series. Overlapping forward windows
  make the naive t-statistic roughly twice too large.
- **Benjamini-Hochberg across the whole persistent trial registry**, not within a
  run. Trials cannot be deleted — a trigger enforces it.
- **Deflated Sharpe** (Bailey & López de Prado). A result is SIGNIFICANT only if
  it clears *both* corrections, and both numbers are always shown.
- **No optional stopping.** The harness refuses any window but the registered
  one unless an extension was declared before results were viewed.
- **Benchmark is the control.** A spec whose primary metric is absolute rather
  than benchmark-relative is rejected at load.

`PREREG-000-noise-control` is a permanent calibration study: a seeded-noise
factor whose desired outcome is a null. If it ever reports SIGNIFICANT, the
harness is broken and every other result it has produced is suspect.

---

## Known gaps — read before trusting a number

- **Statutory cost rates are UNVERIFIED.** §9 requires checking them against
  primary sources; that could not be done in the build environment. Every table
  in `src/costs/rates.yaml` carries `verified: false`, the cost model warns on
  first use, and the dashboard shows a banner. **Verify them before treating any
  net-of-cost result as real.** The rates are data, so verifying one is a YAML
  edit, not a code change.
- **No real data has been fetched.** The build environment had no route to
  nseindia.com or api.dhan.co. Every fetcher and parser is tested offline
  against faithful fixtures; the live backfill runs on your machine.
- **Circuit detection is a heuristic** (zero intraday range at a band-sized
  move) because NSE does not publish per-scrip bands in the bhavcopy. It
  under-detects rather than over-detects.
- **The Dhan automated token flow is the partner-app flow** and may not be
  available on a standard account. `--token-from-stdin` always works.

---

## Command reference

```
python -m src.archive.backfill --source bhavcopy --start 2022-04-01
python -m src.archive.backfill --stats
python -m src.archive.backfill --verify        # re-hash every blob
python -m src.store.build [--rebuild]
python -m src.auth.dhan_token --status
python -m src.auth.dhan_token --token-from-stdin
python -m src.costs.worked_example             # CP5 hand-checked round trip
python -m src.desktop.main [--browser|--no-window]
```

## Build checkpoints (§17)

| CP | Gate | Status |
|---|---|---|
| CP1 | `pytest` runs clean | pass |
| CP2 | Archive + bhavcopy fetcher + token daemon | pass offline; live fetch needs network |
| CP3 | Acceptance tests 2 & 4 (survivorship, index PIT) | pass |
| CP4 | Acceptance tests 1 & 3 (look-ahead, publication lag) | pass |
| CP5 | Cost model reproduces a hand-computed round trip | pass — ₹500.0806, 100.02 bps |
| CP6 | Universe size series, no unexplained discontinuity | pass |
| CP7 | Every factor computes on 10 dates, no `latest()` reachable | pass — 34 factors |
| CP8 | Random factor reports NOT SIGNIFICANT after correction | pass |
| CP9 | Pre-registration system + ledger | pass |
| 10-12 | Portfolio, paper execution, LLM stub, dashboard | pass |

**No real study has been run.** CP1–CP9 pass against a synthetic market seeded
with a delisting, a merger, a rename, an illiquid name, a penny stock, a new
listing, and a bounded ASM window. The first real study is registered
separately, after the cost rates are verified and the archive is populated.
