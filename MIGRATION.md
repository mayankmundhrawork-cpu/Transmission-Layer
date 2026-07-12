# MIGRATION — from asserted transmission to measured transmission

> **STATUS (end of first run):** Phases 1–4 implemented, tested and wired;
> 5–9 stubbed with contracts. 8/8 known-answer tests green.
> **Acceptance case live on real data**: digest [0] now opens with
> `[INVERTED] safe_haven_gold: corr20=-0.28, contra nifty_50 corr20=+0.43,
> shifted 2025-07-14` — and the inr_oil linked group (measured corr ≈ 0) no
> longer escalates. New per-run state: conditional.json, factor_state.json,
> assumptions_state.json, regime_state.json, spreads_state.json,
> anomalies.json. CI: pytest gate + analytics step. Deferred honestly:
> NSE FII/DII/delivery% (CI IP-block reality — enrichment lane, P5-era);
> ruptures has no local py3.14 wheel (CI py3.12 fine; rolling-jump fallback
> in place). Remaining: P5 lead-lag emit gate, P6 pairs/Hurst, P7 FDR wiring
> (BH implemented+tested), P9 hit-rate ledger — contracts in
> leadlag.py / spreads.py / fdr.py / scorecard.py.

Phase 0 audit of the Transmission Layer (rev v6.2, 2026-07-12) and the
implementation plan for the empirically-grounded anomaly engine.

---

## 1 · Current state (what exists, verified in code)

**Pipeline** (per 2-hourly CI run): `update_universe` (RSS+squawk → entity
extraction → symbol resolution → universe state) → `fetch` (yfinance/FRED,
incremental tails + budgeted backfills + intraday provisional upsert,
despike) → `digest` → `overnight` (relations → analogues/laggards/India
receivers → research bundles → free-LLM theses) → `brief` → commit
`data/*`. App is read-only over committed state.

**Descriptors today**: `z20`/`z60` on LEVELS vs prior-N window (ddof=0,
today excluded); trailing ≤252-obs percentile; 1d/5d %; framework move
rules; co-occurrence escalation; event clustering by 60d return corr
(|ρ|≥0.65, direction-consistent) with score floor.

**Already-measured substrate (genuine head start)**: `relations.py`
computes pairwise 60d/252d return correlations AND directional lead-lag
(1–5 sessions) every run; `india.py` receivers and `thesis.py` laggards are
read from it live, not asserted. Phases 4–5 build on this rather than from
zero.

## 2 · The gaps (audit findings)

| # | Finding | Where | Severity |
|---|---|---|---|
| G1 | **Standing priors hardcoded as constants**: 4 linked groups (`metal_copper`, `inr_oil`, `gold_silver`, `goi_ust`) escalate co-occurrence regardless of whether the relationship is currently alive | `backbone.py:95` → `engine.py` composites | HIGH — the "gold safe-haven" class of bug |
| G2 | **Economic semantics in string literals**: GSR>85 labelled "monetary stress", <75 "industrial" — narrative shipped untested | `engine.py:109-111` | HIGH |
| G3 | **LLM theses narrate channels with no measured channel status in the prompt** — the model can assert "safe-haven bid" freely; laggards are measured but channel *validity* is not fed | `thesis.py` prompt pack | HIGH |
| G4 | **Anomaly = raw move**: z on levels vs a 20-obs window; no vol conditioning (a 2σ-in-quiet-regime move drowns), no factor residualisation (priced vs unexplained is guessed by the LLM, not computed) | `engine.py` | HIGH |
| G5 | **No regime layer**: percentiles and correlations are unconditional; decouplings (gold leaving safe-haven) are invisible until they rot a thesis | — | HIGH |
| G6 | **Spread stats are z-only**: `gold_silver_ratio` at z 2.3 says nothing about reversion horizon | `engine.py` | MED |
| G7 | **No multiplicity control**: ~90 series × thresholds each run; amber floods on broad days are partially absorbed by event clustering but no FDR notion exists | `events.py` | MED |
| G8 | **No hit-rate memory**: signal types carry no realised precision | — | MED |
| G9 | India-specific edges absent: FII/DII flows, delivery %, India VIX | data layer | MED |

## 3 · Point-in-time audit (explicitly requested)

**Clean** — verified line-by-line:
- `engine._z`: window is the N obs strictly before today (`tail(window+1)`,
  stats on `iloc[-window-1:-1]`) — no lookahead.
- `engine._percentile`, `patterns.metric_frame` (`shift(1).rolling`),
  `patterns` pctile (`rolling(...).rank`), `relations` (trailing tails),
  100-DMA rule (`tail(101).iloc[:-1]`) — all trailing-only.
- `patterns.aftermath` uses forward returns BY DESIGN (historical
  evaluation, not signal input).

**Wrinkles to carry into the design (not bugs, but must stay true):**
- **W1 — despike uses t+1**: an interior bad print is corrected using its
  next neighbour. The LAST observation is never touched (interior-only), so
  no live-signal lookahead; but historical rows are hygiene-adjusted with
  one day of hindsight. Acceptable; documented; new modules must not despike
  the live point.
- **W2 — intraday provisional row**: a digest generated mid-session uses a
  provisional last price later overwritten by the official close.
  Reproducibility contract: every run commits its exact inputs, so a digest
  is reproducible from its data commit SHA. New modules must read only the
  committed frame (they do — everything reads `data/prices.csv`).
- **W3 — z on levels** (not returns): not lookahead, but the naive-z
  weakness Phase 2 replaces. Levels-z is RETAINED for display continuity;
  the anomaly gates move to vol-conditional return z.

## 4 · Library verdicts (PyPI checked 2026-07-12, versions pinned in Phase 1)

| Library | Version / last release | Verdict |
|---|---|---|
| `arch` | 8.0.0 · 2025-10-21 | ✓ EWMA/GARCH(1,1) — Phase 2 |
| `statsmodels` | 0.14.6 · 2025-12-05 | ✓ RollingOLS, MarkovRegression, ADF/KPSS, coint, HAC — Phases 3/4/6 |
| `ruptures` | 1.1.10 · 2025-09-10 | ✓ change-points on key correlations — Phase 4 |
| `pykalman` | 0.11.2 · 2026-01-31 | ✓ (revived fork) — OPTIONAL dynamic betas; RollingOLS is primary |
| `filterpy` | 1.4.5 · 2018-10-10 | ✗ dead — rejected |
| `jugaad-data` | 0.33.1 · 2026-03-16 | ✓ most-maintained NSE lib — bhavcopy/FII-DII best-effort |
| `nsepython` | 2.97 · 2025-05-26 | ~ fallback only |
| `nsetools` | 2.0.1 · 2025-03-18 | ~ not needed if jugaad works |
| `nsepy` | 0.8 · 2020-03-07 | ✗ dead, as suspected — rejected |
| `fredapi` | 0.5.2 · 2024-05-05 | not needed — existing raw FRED client works and is thinner |
| `pandas-datareader` | 0.11.1 · 2026-06-24 | ✓ stooq fallback lane |

**NSE-from-CI reality check**: NSE blocks datacenter IPs; jugaad/nsepython
calls from GitHub runners frequently 403. Design consequence: India-edge
data is **best-effort with graceful degradation + parquet point-in-time
cache** (a local/seeded pull survives CI outages), and **India VIX comes
from yfinance `^INDIAVIX`** (verified working: 22 rows, last 12.25) — no
NSE dependency for the highest-value series.

## 5 · Implementation order (Phases 1–4 this run; 5–9 stubbed)

Order chosen so each stage feeds the next and the gold fix lands complete:

1. **P2 first — `conditional.py`**: EWMA-vol (RiskMetrics λ=0.94) and
   GARCH(1,1) (`arch`, seeded, fit budgeted) standardised RETURN z per
   series; regime-conditional percentile hook (consumes P4's label).
   Emitted alongside raw z: `z20`, `zc` (vol-conditional), both in grid,
   brief, digest [1].
2. **P3 — `factors.py`**: per-instrument factor sets from
   `factors.yaml` (default: broad index, sector index where known,
   USDINR/DXY, Brent, GSec/UST rate, VIX). `RollingOLS` (60d, HAC SEs) →
   predicted return → **residual, residual-z, R², top contributors**.
   PIT: betas from window ending t−1 applied to day-t factor returns.
3. **P4 — `assumptions.yaml` + `assumptions.py` + `regime.py`**: the ledger
   (initial 8 priors incl. `safe_haven_gold`, the four linked groups, VIX↔
   equity, DXY↔EM-FX, oil↔INR), scored live each run → VALID / WEAK /
   INVERTED / INSUFFICIENT_DATA with the measured numbers attached;
   rules-based risk-on/off regime (India VIX + VIX percentile, equity-bond
   corr sign, breadth) with `MarkovRegression` as secondary label;
   `ruptures` change-point dating on the ledger's key correlations.
   **Consumers**: engine co-occurrence escalation gated on ledger status;
   thesis prompt receives channel statuses; digest + brief gain an
   "Assumptions & regime health" header. Gold case must render as:
   *safe-haven channel INVERTED, gold–nifty 20d corr = +0.xx (dated by
   change-point), long-gold-on-risk anomaly suppressed*.
4. **P1 hardening — data layer**: parquet PIT cache (`data/parquet/`),
   retry/backoff decorator on all fetchers, `^INDIAVIX` into backbone,
   jugaad-data FII/DII + delivery% as best-effort daily pulls with
   holiday-aware (exchange_calendars or weekday+existing roll logic)
   handling; stooq fallback for yfinance outages. Corporate-action note:
   yfinance auto_adjust stays OFF for continuity; dynamic single names get
   split detection via despike-adjacent sanity check (flagged, not silently
   fixed).
5. **P5–P9 stubs** — `leadlag.py`, `spreads.py` (ADF/KPSS/OU half-life/
   Hurst interfaces), `fdr.py` (Benjamini-Hochberg over the scan),
   `scorecard.py` (hit-rate ledger), `anomalies_json.py` (output contract)
   — interfaces + TODO notes; `spreads.py` gets the OU half-life
   implemented early if time allows since G6 is cheap to fix.

**Testing**: fixtures with known answers for _z/zc (synthetic series with
planted vol regimes), RollingOLS residuals (constructed factor data),
assumption scorer (synthetic corr flips), OU half-life (simulated OU
process), BH-FDR (textbook p-value vector). `tests/` + plain `pytest`,
run in CI before the fetch step.

**Runtime budget**: GARCH fits ~90 series × <0.3s (budgeted, EWMA fallback
on failure/timeout); RollingOLS trivial; Markov switching on 1–2 proxies;
ruptures on ~8 ledger series. Fits inside the existing ~3-min CI run.

**Config-driven**: `factors.yaml` + `assumptions.yaml` next to
`calendar_config.py`; no economics in Python beyond generic scoring math.

## 6 · Digest/brief contract changes (extend, never replace)

- Digest `[1]` rows gain `zc` and `resid-z`; `[2]` flags annotated
  `priced | unexplained | assumption-invalidated`.
- New digest header block + brief section: regime label, ledger table with
  measured numbers, active change-points.
- `data/anomalies.json` (P8 stub → fills as P5–7 land): one record per
  candidate with all gate evidence + falsifiers.

## 7 · Risks & honest limits

- **NSE flows/delivery from CI may simply not work** (IP blocks) — the
  design treats them as enrichment, never gate inputs.
- **2y of daily history** bounds everything: Markov regimes will be coarse
  (2-state only), cointegration tests are weak at n≈500, and FDR operates
  on modest samples. Stated in output, not hidden.
- **GARCH on monthly FRED series is meaningless** — conditional stats apply
  to daily series only; monthly series keep levels-z with the sparse guard.
- The LLM can still over-narrate — mitigated by feeding it ledger statuses
  and instructing "cite channel status; do not assert unmeasured channels",
  but the hard gate is that suppressed anomalies never reach it.
