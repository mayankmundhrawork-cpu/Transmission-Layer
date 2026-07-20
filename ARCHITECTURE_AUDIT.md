# ARCHITECTURE_AUDIT — synthesis-engine rebuild, Stage 0

Audited 2026-07-14 at `5b5904d`. Everything below verified against the tree,
not recalled. **Stops here for sign-off before any build.**

---

## 1 · Full current data flow

```
yfinance ──(no auth; ~86 symbols; batched 10/call, 1s spacing, retry/backoff;
            EOD tails 15d + intraday 15m provisional upsert)──► data/prices.csv (95 cols incl derived)
FRED ─────(FRED_API_KEY env; 9 series; raw REST, retried)─────► prices.csv
t.me/s/DeItaone ─(no auth; HTML scrape, html.parser; app-side
            st.cache ttl=120s + CI persist; UA-polite)────────► data/squawk.json (60 items, 48h roll)
14 RSS feeds ─(feedparser; per-feed try/except; 7d dedup store)► data/headlines.json (1169 items)
                                   └─ squawk items injected into the headline store (feed="DeItaone")
calendar_config.py ─(pure date rules + fixed 2026 dates)──────► release_calendar.build_calendar()
Groq ─────(GROQ_API_KEY env; llama-3.3-70b-versatile via raw
           OpenAI-compatible REST; free tier)─────────────────► data/theses.json
article fetch ─(stdlib html.parser; 20/run; paywall partial)──► data/articles/*.json
```

**Scheduler**: GitHub Actions cron `15 4,6,8,10,12,14,16,18,20 * * 1-5` +
`30 21 * * 1-5` (≈every 2h, weekdays) → pytest gate → universe update →
fetch → **analytics.py** (conditional→factors→assumptions→regime→spreads→
leadlag→scorecard→anomalies) → digest → overnight (relations→bundles→theses)
→ brief → bot commit of `data/*`. Streamlit app is read-only over committed
state, plus one live call (squawk, 120s TTL).

**Current latency**: market data ≤2h stale (+ provisional intraday row at
fetch time); squawk ~2min while app open; theses/packets refresh per 2h run.
⚠ The target spec's "batch every 2–3 minutes" cannot run on Actions free
tier (~2000 min/mo; 2–3min cadence ≈ 9,000+ min/mo). See §8 adaptation.

## 2 · Where the statistics live (actual formulas)

- **Levels z (display + legacy flags)** — `engine.py:39 _z`:
  `z = (s[-1] − mean(s[-w-1:-1])) / std(s[-w-1:-1], ddof=0)` — prior-w window
  excluding today, on LEVELS. `engine.py:50 _percentile`: share of trailing
  ≤252 obs (incl today) strictly below today.
- **Conditional z (gate)** — `conditional.py:52`:
  `sigma2 = r².ewm(alpha=1−0.94, adjust=False).mean().shift(1)`;
  `zc = r_t / sigma_{t|t−1}`; GARCH(1,1) (`arch`, zero-mean, fit excludes last
  return, 45s total budget) refines the latest sigma only.
- **Global residual z** — `factors.py`: RollingOLS(window 60, min 45) of the
  instrument's returns on its `factors.yaml` block; `betas = params.shift(1)`
  (PIT); `resid = y − Σβ·f`; `resid_z = resid / std(prior-60 resids, ddof=0)`;
  reported R²/contributions from a latest-window HC0 OLS.
  ⚠ This is the **global multi-factor residual** the spec says the
  transmission-gap detector must NOT be built on — the pairwise conditional
  residual (target − β_pair·driver) exists nowhere today.
- **Channel-health table** — `assumptions.py`: for each YAML prior,
  20d/60d return corr vs `expected_sign`; CLEAR=|corr|≥0.25; contra check;
  → VALID/WEAK/INVERTED/INSUFFICIENT; change-point via ruptures(PELT,rbf)
  on rolling-60 corr (fallback: largest 20-session jump).
- **Pairwise substrate** — `relations.py` → `data/relations.json`:
  89 series, **825 pairs** `{a, b, rho60, rho252, leader, follower,
  lead_lag(1..5), lead_rho}` + per-series top-12 neighbours. Method: z-scored
  return matrices (NaN→0 shrinkage approximation), `C = Zᵀ Z / n`; lead-lag =
  `corr(a_{t−k}, b_t)` best |k|≤5 over 252d. Recomputed each run (~1s).
- **Lead-lag verification (P5)** — `leadlag.py`: best-CCF lag k, lagged OLS
  with HAC(maxlags=k), gates: `p<0.05 AND |ccf|≥0.25 AND n≥150` → BH-FDR
  q=0.1 across the scanned pairs → emit only if driver |zc|≥1.5 AND target
  response <60% of β-implied. Granger = caveated evidence only.
  ⚠ Thresholds (0.25, 1.5, 0.6) are **fixed constants**, not adaptive
  percentiles — spec violation to fix in Stage 2.
- **Base rates (partial)** — `scorecard.py`: split-sample
  `transmission_follow 0.815 (n=1968)`, episode-level
  `residual_reversion 0.489 (n=1020)`, `spread_reversion 0.579 (n=19)`.
  ⚠ TYPE-level base rates only — no per-setup conditional distribution
  ("driver ≥Xσ & gap ≥Yσ & channel active → closed Z% within K sessions"),
  no labeled-outcome store. Stage 4 builds this.

## 3 · The hardcoded lists and their readers

| Artifact | Contents | Read by |
|---|---|---|
| `assumptions.yaml` (9 priors) | driver/target/sign/contra/channel text | `assumptions.py` (scorer) → state consumed by `engine.py` (co-occurrence gating via `group_status`), `thesis.py` (prompt block), `digest.py` [0], `brief.py`, `app.py` (panel), `anomalies_json.py` (degraded list) |
| `backbone.py LINKED_GROUPS` (4 pairs) | co-occurrence escalation groups | `engine.py` composites (ledger-gated); re-exported by `registry.py` |
| `backbone.py NEWS_ALIASES` (~30 series → keyword lists) | headline↔series matching | `events.py` news attach; `india.py` |
| `factors.yaml` | factor blocks per class | `factors.py` |
| Fixed thresholds sprinkled | AMBER_Z 1.5/RED_Z 2.5 (engine), EVENT_CORR 0.65/floor 3.2 (events), MIN_CORR 0.25/DRIVER_ZC 1.5 (leadlag), CLEAR 0.25 (assumptions) | respective modules |

**To retire per spec**: `assumptions.yaml` as the channel *inventory* (its
scoring machinery generalizes into Stage-2 channel discovery over all 825
pairs), `LINKED_GROUPS`, fixed z/corr constants → adaptive percentiles.

## 4 · How the LLM is called today

`thesis.py` — **one mega-prompt per event** (the exact anti-pattern the spec
targets):
- Endpoint: Groq `chat/completions`, model `llama-3.3-70b-versatile`;
  **temperature 0.4** (spec: ≤0.2), `max_tokens 900`, no JSON mode, no seed.
- System prompt: analyst persona + "No gap is a valid output" + priced-vs-
  unexplained doctrine + WEAK/INVERTED channel prohibition.
- User prompt (assembled in `_compose_prompt`): event members w/ z20/zc/
  resid_z/r2/move-label; laggards; analogues + aftermath; regime; full
  9-channel status table; verified setups + type hit-rates; article excerpts.
- Output contract: one JSON blob `{mechanism, responders[], gap, confidence,
  one_liner, india_take}` parsed by `text.find("{") .. text.rfind("}")` +
  `json.loads`. Failure → rule-based skeleton (escape hatch exists).
- Caching: key = members + z quantized to 0.5 + news titles → unchanged
  events never re-call; ≤8 calls/run.
- **Observed failure mode confirmed** (recent `theses.json`): outputs
  gravitate to generic "No gap: … already priced/reacted" — the model is
  asked to discover+classify+narrate at once from a wide dump.
- No embedding model anywhere; entity matching is alias/word-boundary only
  (`extract.py` stop-lists + `resolve.py` gazetteer + `NEWS_ALIASES`).

## 5 · Persistence inventory

- `data/prices.csv`: **530 rows × 95 series** (2024-07-15 → 2026-07-14, 2y
  rolling window trimmed at fetch; parquet mirror).
- Headlines 7d/1169 items (w/ links); squawk 48h/60 items; articles cache.
- Analytics state (per run, committed): conditional/factor/assumptions/
  regime/spreads/leadlag/scorecard/anomalies JSONs.
- **The git history of data commits is a point-in-time archive** (every ~2h
  since 2026-07-03) — usable to backfill a labeled-outcome store.
- No labeled outcomes, no event-bus archive, no per-candidate outcome ledger.

## 6 · What already maps to the target (reuse, don't rewrite)

| Target stage | Existing asset | Gap |
|---|---|---|
| S1 event bus | headline+squawk stores w/ ts/source/title/link; universe extraction | no unified Event schema; no salience; entity tagging only at universe-admission, not per-item |
| S2 transmission gap | `leadlag.py` three-gate emit | pair scan seeded from `relations` lead-pairs (good) but thresholds fixed; residual is global-factor, not pairwise-conditional |
| S2 channel discovery | `assumptions.py` scoring + change-points | inventory hardcoded at 9; must scan all 825 pairs vs their own corr history |
| S2 news–move divergence | events news-corroboration bonus | no "big news/no move" or "big move/no news" detectors |
| S2 cross-sectional dispersion | nothing | build (approx via rolling factor betas; low-confidence flag) |
| S3 packets | research bundles + brief per event | not per-candidate, not self-contained, no score decomposition |
| S4 base rates | patterns.analogues + scorecard types | not setup-conditional; no N/hit/horizon per candidate |
| S5 decomposed LLM | single mega-prompt | split into Classify/Articulate, temp ≤0.2, packet-grounded |
| S6 critic | none (prompt-level discipline only) | AMIFT gate, code-first |
| S7 output | digest/brief/app | add ranked thesis surface + copy-packet action; retire channel table |

## 7 · Auth/limits summary

yfinance: none (IP throttle; batched+backoff). FRED: key, generous. Telegram
preview: none (blockable; graceful-empty). RSS: none. Groq free tier:
~30 req/min, 14.4k tok/min class limits — decomposed calls fit if ≤~20
candidates/run with caching. GitHub Actions: ~2000 free min/mo (the binding
cadence constraint).

## 8 · Adaptations I propose to the spec (flagging before build)

1. **Cadence**: "every 2–3 min" is impossible on Actions free tier. Proposal:
   keep the 2h CI batch as the committed-state truth AND run the same
   pipeline in-app on a 3-min `st.cache_data(ttl=180)` tick over live squawk
   + provisional prices (compute is ~seconds; LLM stages stay CI-side under
   budget caps). Say if you'd rather pay for a runner instead.
2. **Embeddings**: no embedding model exists. First pass = deterministic
   alias-map + curated topic map (Hormuz-style entries) — free, auditable;
   embedding upgrade (local MiniLM in CI) only if recall proves insufficient.
3. **"Retire the assumptions table"**: I'll retire it as *inventory* (Stage 2
   discovers channels from all pairs) but keep the YAML as optional *named
   overlays* (display names for discovered channels + the contra-check
   config for gold), since "safe_haven_gold INVERTED" needs a human name to
   be readable. The detector logic will not depend on it.
4. **2026-07-18 acceptance snapshot**: that date is 4 days in the future;
   I'll wire acceptance tests to run against "latest committed snapshot" and
   we execute them on the 18th as specified.

---

**Audit complete. Stopping for sign-off per Step 0.** Build order on
approval: S1 bus → S2 detectors (retire hardcoded channels) → S4 base-rate
store → S3 packets → S5/S6 decomposed LLM + critic → S7 output — each behind
`SYNTH_V2` flags so the current board keeps running until acceptance passes.
