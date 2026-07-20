# SESSION_HANDOFF — resume context for the next Claude session

Written 2026-07-20 at local commit `024c450`. **Read this first, then
ARCHITECTURE_AUDIT.md, then the S1 files.** The active task is mid-flight.

---

## 1 · What this project is

"The Transmission Layer" — a zero-budget macro anomaly board for an Indian
market practitioner (Substack author). Streamlit Cloud app + GitHub Actions
pipeline (repo `mayankmundhrawork-cpu/Transmission-Layer`, branch `main`).
Everything runs free: yfinance + FRED + RSS + a t.me/s/DeItaone squawk
scrape + Groq free tier (llama-3.3-70b). All state lives in committed
`data/*` files; the app only reads. Built across v1→v7 in prior sessions:
self-assembling news-driven universe (~95 series), events/theses/research
bundles, terminal UI, measured-transmission engine (conditional zc, factor
residuals, assumption ledger, regime, lead-lag P5, FDR P7, hit-rate ledger
P9 — see MIGRATION.md).

## 2 · ACTIVE TASK — "Rebuild the synthesis engine" (SYNTH_V2)

Owner's spec: replace "z-score → one mega-prompt narration" with a 7-stage
pipeline — (1) normalized event bus, (2) deterministic anomaly detectors
with adaptive thresholds & nothing hardcoded, (3) evidence packets, (4)
setup-conditional base rates, (5) decomposed small-LLM calls (Classify →
Articulate, temp ≤0.2, strict JSON, escape hatches), (6) AMIFT critic gate,
(7) ranked output + copy-packet. Prime directive: **intelligence lives in
the scaffold, not the model** — code computes, the LLM phrases. Build behind
`SYNTH_V2` flags; current dashboard keeps running until acceptance passes.

**Stage 0 audit: done + signed off** (`ARCHITECTURE_AUDIT.md`, commit
`da51657`). Key audit finding the owner called "the single most important":
the pairwise conditional residual (target − β_pair·driver) exists nowhere —
today's resid_z is global multi-factor — which is *why* the board always
says "priced".

### Owner rulings (binding, from two sign-off messages)

1. **Cadence**: 2h CI batch stays the durable truth; a 3-min in-app tick
   must produce the FULL deterministic packet (Stages 1–4, not just flags).
   LLM is **event-triggered** (fire one Groq call when a new candidate
   crosses the gate that wasn't in the prior tick — runs app-side, zero
   Actions minutes). In-app live prices: reuse `fetch_yf_batch_live()`
   under `st.cache_data(ttl=180)`; on failure fall back to committed prices
   with an explicit `prices_stale: true` flag (this answer was accepted).
2. **Embeddings**: curated alias map first (done); MiniLM upgrade only on
   evidence from the join-miss log ("no news" flags that had news).
3. **Assumptions table**: retired as inventory; kept ONLY as a naming
   overlay for discovered channels. Gold contra-check must be annotation
   only or generalized per-pair — no hardcoded special case doing detection.
4. **Acceptance**: pin a FROZEN golden snapshot with hand-labeled expected
   anomalies as the fixture; "latest" is for smoke tests only.
   (Env note: local clock said 2026-07-14 during the audit while the owner
   says today is the 20th — env clock drifts; don't trust it for dating.)
5. **(A) Min-history floor**: no market events on <N sessions of |zc|
   history (use N=180-ish); below floor use a conservative fixed bar
   (|zc|≥3.0) and tag `low_history: true`.
6. **(B) Directionality**: the pairwise conditional residual must carry
   sign through β_pair; a gap = target short of the IMPLIED direction.
   Driver up + target hard-down is NOT a gap. Add an acceptance test for it.
7. **(C)**: develop S2 against a bus containing live market events — DONE
   (fresh fetch pulled, bus has a market event).
8. **(A, base rates)**: primary sample = reconstruct detector triggers
   historically across the full 530-day price matrix (would it have fired;
   did target close the gap in K sessions). Git archive (~2h commits since
   Jul 3) is for point-in-time integrity only, NOT sample size.
   News-conditional refinements limited to the archive window → flag small N.
9. **(B, dispersion)**: the cross-sectional/exposure detector is DEFERRED —
   explicitly out of S1–S2 scope; do not block on it.
10. **Process**: the first S2 output the owner wants to see is the
    **decomposed candidate table** (driver, target, driver-percentile,
    β_pair, conditional-residual-in-σ, channel-state, score components) on
    the frozen snapshot — BEFORE any LLM work. Send it up for eyeball.
11. Basket rulings APPLIED in `synth_aliases.py`: monsoon → +nifty_50 @
    weight 0.5; tariffs → +nifty_it, +nifty_metal; semis→nifty_it kept with
    `watch: True` (S2 audit must surface candidates whose news-join came via
    watch entries so its hit rate is visible; cut if noise).

### Stage status

- **S1 event bus: DONE + APPROVED** (`synth_events.py`, `synth_aliases.py`,
  commits `56da695` + `024c450`). Schema: Event{id sha1-12, ts, source
  market|squawk|rss|release, kind, entities, topics, payload, salience}.
  Market adapter fires on ADAPTIVE bar (|zc| ≥ q98 of own history,
  MOVE_MIN_HISTORY=120 — note: ruling 5's floor/fallback still needs to be
  implemented ON TOP of this). 3-layer lexicon: L1 auto universe, L2
  backbone NEWS_ALIASES, L3 curated topics with weights + watch. Join-miss
  log at `data/synth/join_misses.json` (rolling 400) — already caught the
  IRANIAN≠iran morphology miss (fixed with a Gulf-escalation entry carrying
  brent/wti/gold/vix). Bus state `data/synth/events.json` (7d roll).
  Latest local build: 242 events (market 1 = dyn_justdial_bo, squawk 20,
  rss 219, release 2), miss rate 0.27; squawk live pull failed once with a
  transient local network error (WinError 10053) — retry, it's flaky-safe.
- **S2: NOT STARTED — the next work.** Plan agreed:
  a. Freeze golden snapshot: copy prices.csv, headlines.json, squawk.json,
     universe.json, relations.json, synth/events.json into
     `data/synth/golden_<date>/`; hand-label expected anomalies with owner
     later.
  b. `synth_channels.py` — channel discovery over ALL relations pairs (825):
     current rolling-60d corr vs its OWN historical distribution percentile
     → states active / turning_on / breaking (+ sign-flip), change-point
     dating (reuse assumptions.py machinery: ruptures PELT/rbf w/ fallback);
     assumptions.yaml names as display overlay only. Persist
     `data/synth/channels.json`.
  c. `synth_detect.py` — detectors over bus+prices+channels:
     transmission_gap (flagship: ordered lead pairs, driver market-event
     with direction, expected = rolling β_pair × driver_ret computed PIT,
     conditional residual SIGNED, gap in target-σ units, adaptive gap bar =
     high percentile of that pair's own residual history, channel must be
     active); news_move_divergence (big news/no move AND big move/no news,
     using entity joins + join-miss trust + entity weights); channel
     turning_on/breaking as candidates. Decomposed scores, no opaque
     composites. Output `data/synth/candidates.json` ranked.
  d. STOP and show the candidate table (ruling 10).
- **S4 → S3 → S5/S6 → S7** then per the approved build order (S4 before S3
  per owner's original spec order adaptation: base-rate store powers the
  packet). S5 prompts go in versioned files (e.g. `prompts/` dir), temp
  ≤0.2, Call A classify {GAP|PRICED|UNEXPLAINED|INSUFFICIENT}, Call B
  articulate with falsifier-or-drop; S6 AMIFT gate (code-first: null-hyp
  check, cross-asset corroboration computed, steelman, base-rate PASS needs
  N≥8 & hit≥60%, positioning honest-N/A). Acceptance tests incl.: no
  hardcoded pairs (grep), every thesis cites news id + base rate N,
  LLM-off still useful, small-vs-frontier packet convergence, direction
  false-positive test (ruling 6).

## 3 · Git / repo state

- Local `main` at `024c450`; **local-only commits: `da51657` (audit),
  `56da695` (S1), `024c450` (S2 prep)** — origin/main last seen at bot
  commit `d34014d` (2026-07-14; CI has NOT run since — worth checking why:
  possibly Actions billing/pause or schedule idle; run
  `gh`-less check via git credential token + API, see §5).
- **Do NOT push mid-build without asking** (owner pushes or asks; a push
  auto-redeploys Streamlit). When pushing after bot commits: `git rebase
  origin/main -X theirs` (my regenerated data wins; next CI refreshes).
- **NEVER `git add -A`**: the folder contains the owner's separate untracked
  projects (screener/ [gitignored], swing_classifier/, swing_strategy/,
  delivery_study*/, symptom_study/, tests/test_swing_*.py,
  tests/test_delivery_*.py). Stage files explicitly.

## 4 · Cheat sheet (hard-won environment facts)

- Local Python 3.14: `ruptures` has no wheel (guarded import w/ fallback
  exists); CI is 3.12 and has it. `arch`, `statsmodels` installed locally.
- Windows console is cp1252: run scripts with `python -X utf8`, keep ASCII
  in print statements (── and → have crashed runs before).
- OneDrive sometimes locks `.git` (rebase-abort once failed; `rm -rf
  .git/rebase-merge` fixed it).
- `gh` CLI not installed. GitHub API access works via:
  `TOKEN=$(printf "protocol=https\nhost=github.com\n\n" | git credential
  fill | grep '^password=' | cut -d= -f2)` → curl with Bearer token
  (workflow dispatch, run logs). Used repeatedly; owner approved this loop.
- Streamlit Cloud: source-only pushes can soft-sync and leave stale modules
  in the running process → ImportError. Fix: bump the `rev:` comment in
  requirements.txt to force a container rebuild (currently v7).
- Secrets: FRED_API_KEY (repo+app), GROQ_API_KEY (repo). No paid LLM
  anywhere — hard owner constraint ("0 budget"). Groq temp for new calls
  ≤0.2 per spec (old thesis.py uses 0.4 — that path is being replaced).
- CI workflow `.github/workflows/fetch.yml`: pytest gate → universe →
  fetch → analytics.py → digest → overnight.py → brief.py → bot-commits
  data/. Cron ~2h weekdays. ~2000 free min/mo is the binding budget.
- Key formulas/locations: levels z `engine.py:39`; zc EWMA λ=.94
  `conditional.py` (`shift(1)`, PIT); global resid `factors.py`
  (RollingOLS 60, betas shift(1)); pairs+lead-lag `relations.py` →
  `data/relations.json` (825 pairs); channel scoring machinery to
  generalize: `assumptions.py`; P5 gates `leadlag.py`; base-rate types
  `scorecard.py` (transmission_follow 0.815 n=1968 split-sample).
- The app (`app.py`) is the terminal UI (design tokens in UI_NOTES.md);
  don't touch its zones for SYNTH_V2 until S7.
- User guide: USER_GUIDE.md + published artifact. Board brief for LLM
  feeding: `brief.py` → `data/board_brief.md` (methodology appendix must be
  extended when SYNTH_V2 ships).

## 5 · Immediate next actions for the resuming session

1. `git log origin/main..HEAD` sanity + check why CI idle since Jul 14
   (dispatch a run via the token loop if wanted).
2. Retry squawk pull (transient failure), rebuild bus.
3. Freeze the golden snapshot dir.
4. Implement ruling 5's min-history floor in `synth_events.market_events`.
5. Build `synth_channels.py`, then `synth_detect.py` (S2), with the
   directionality acceptance test in `tests/test_analytics.py` style.
6. **Show the owner the decomposed candidate table and STOP for eyeball**
   before S4+.
