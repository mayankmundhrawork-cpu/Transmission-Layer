# Build Notes

---

# V6 — Squawk, India lens, hypotheses & journal (newest)

## Built (all live-verified)

- **Squawk (`squawk.py`)**: DeItaone via its public Telegram mirror
  `t.me/s/walter_bloomberg` (X has no free lane; the mirror needs no auth).
  App panel pulls live with a **120s cache** (your accepted ~2-min lag),
  falling back to the persisted store when the mirror is down; the scheduled
  job persists 48h history to `data/squawk.json` and injects items into the
  headline store (feed `DeItaone`) so extraction/universe/event-matching see
  them. Suffix noise + emoji stripped at ingest. **[VERIFY]** occasionally
  that the mirror stays alive; alternates can be added to
  `squawk.CHANNEL_URLS`.
- **India transmission lens (`india.py`)**: for every event, ranked Indian
  receivers (correlation/lead vs event members + reacted/quiet state) —
  pure math over relations. Rendered as a "→ india" line under every event
  card, fed to theses as INDIA TRANSMISSION CANDIDATES, and the thesis JSON
  gained a mandatory **india_take** field (thesis cache key salted v2 to
  force one-time regeneration). New India strip under the headline strip:
  nifty/inr/GoI/CPI prints + next India releases countdown. Backbone gained
  `india_cpi_yoy` (FRED `CPALTT01INM659N` **[VERIFY]** first CI fetch).
- **Hypotheses & journal (`journal.py`)**: jot hypotheses on the board;
  optional free-LLM evaluation (verdict / mechanism check / what confirms /
  what refutes / expressing instruments / sharpened restatement) —
  one user-clicked call each, EVAL_PROMPT system voice. Trade-intent journal
  (instrument/side/level/rationale, linked to the motivating event) with
  open/close lifecycle and markdown export. **No broker/demat API by
  design** — the schema records intent now so fills can attach later.
- **Bug pass**: HTML entities unescaped at headline/digest ingest (kills the
  `S&amp;P` artifacts everywhere downstream); squawk text cleaned of channel
  suffixes; calendar computed once per render.

## Cloud caveat (same as scratchpad)
Journal/hypotheses state lives in `data/journal.json` — durable locally,
ephemeral across Streamlit Cloud redeploys. **Export before closing** on
cloud. (The workflow does not commit journal/scratchpad — they're personal
working state, not pipeline data.)

## Costs
Unchanged: $0.00/run. Squawk = one HTML GET per 2 min while the app is open.
Hypothesis evaluations are user-clicked free-LLM calls.

---

# V5 — Research Accelerator (newest section)

> Five capabilities that compress the gap between "opening the board" and
> "writing the first paragraph": per-event theses, deep-link research bundles,
> correlation/lead-lag substrate, evidence-pinning scratchpad, historical
> pattern replay. **Zero-budget constraint honoured throughout: no paid LLM
> integration exists anywhere in this codebase.**

## What was built (all verified live)

| Feature | Module | State file | Verified |
|---|---|---|---|
| 3 · correlations + lead-lag | `relations.py` | `data/relations.json` | 462 pairs/61 series; sp500↔vix −0.79, brent↔wti 0.955; laggards for the indices event = gold/USTs/HY-OAS |
| 5 · pattern search + replay | `patterns.py` | `data/pattern_cache.json` | "ust_10y 1d≥2%" → 14 episodes, gold +2.41% median +20d (0.77 hit); analogues per event |
| 2 · research bundles | `research.py` (+`headlines.py` link field) | `data/research_bundles.json`, `data/articles/` | 13 articles fetched w/ clean excerpts; FRED/Yahoo/CFTC primary links; zero refetches on second run |
| 1 · theses | `thesis.py` | `data/theses.json` | 8 skeleton theses keyless; free-endpoint routing in place |
| 4 · scratchpad | `scratchpad.py` | `data/scratchpad.json` | pin→note→export loop; citations + ?-notes → open questions |
| orchestrator | `overnight.py` | — | full pass end-to-end at $0.00 |

## LLM posture (the zero-budget design)

- `settings.get_llm_backend()` routes to **free endpoints only**: Groq free
  tier (`llama-3.3-70b-versatile`) first, then OpenRouter `:free` models.
  Plain `requests`, OpenAI-compatible; no SDK, no paid path, `cost_usd` is
  0.0 by construction and logged per run in `data/theses.json → ledger`.
- **No key → skeleton theses**: laggards ("watch next") and nearest
  analogues render from pure math; mechanism/gap say "unassessed (LLM off)"
  honestly. The board is fully functional keyless.
- **To turn prose theses on for free**: create a free Groq account, add
  `GROQ_API_KEY` as a repo secret. Caps: 8 theses/run, 900 tokens each,
  cache-keyed so unchanged events never re-call.

## Decisions & compromises

- **Correlation windows**: 60d primary (matches the events layer) + 252d
  context; lead-lag searched at 1–5 sessions over the 252d window. NaN→0
  standardisation slightly shrinks ragged-column correlations (accepted,
  documented in `relations.py`).
- **Analogue similarity** uses each member's *last valid* z (holiday gaps:
  CBOT closed while NY trades) — ≤2-session skew accepted.
- **Article extraction** is stdlib-only (`html.parser`, ¶-density ≥40 chars).
  Paywalls: pre-wall text is kept (`status=partial`) per your instruction;
  hard walls (401/402/403) are negative-cached as `skipped`. No external
  reader services, no new dependencies.
- **Scratchpad persistence**: disk state, perfect locally; on Streamlit
  Cloud the FS is ephemeral across redeploys — **the exported brief is the
  durable artifact; export before you close.** "clear pad" is two-step and
  auto-snapshots to `data/scratchpad_backup.json`. True cloud persistence
  via GitHub-API commits (needs a PAT secret) is a documented later toggle.
- **Streamlit DOM automation is jittery** (a parallel session fired a stray
  pin during testing) — the pad logic itself verified clean programmatically.

## Costs per run

$0.00. Article fetches ≤20/run (13 on first live run, 0 after cache).
Free-LLM calls ≤8/run when a key exists; Groq free tier is rate-limited but
comfortably covers 8 calls × ~11 runs/day.

## Tune after a week

- `LAGGARD_MIN_CORR` (0.50) / `LAGGARD_MAX_Z` (1.0) — laggard list too
  long/short.
- `ANALOGUE_TOP` (5) and `PATTERN_MIN_GAP` (5 sessions).
- Whether skeleton theses are enough, or the free Groq key earns its place.
- `ARTICLE_FETCH_MAX_PER_RUN` if bundles feel thin on multi-headline days.

---

# V3/V4 — The Self-Assembling Universe

> **The board no longer has a hardcoded universe.** It
> assembles what it tracks from the news, on top of a 56-series macro backbone.

---

## ⭐ MORNING SUMMARY

**All six stages completed and verified against live data.** The pipeline
headlines → entities → symbols → tracked series → clustered events works end
to end on this machine, today, with real feeds and real prices:

- **Universe**: 56-series backbone (global indices, FX, rates+credit,
  commodities, crypto, proven derived ratios) + **5 news-admitted members on
  the first live run** — HDFC Bank (HDB), IndusInd Bank (INDUSINDBK.BO),
  Micron (MU), TeraWulf (WULF), Ather Energy (ATHERENERG.NS) — each carrying
  the exact headlines that admitted it. 61 tracked series total, cap 40 dynamic.
- **Selectivity**: 25 raw engine flags → **7 event cards** (European indices
  fused into one event; sub-floor flags collapsed to a watchlist line).
  A calm day produces zero cards by design.
- **News ties**: every event card shows the motivating headlines (feed + age);
  the TeraWulf card carries its Anthropic-deal story, IndusInd its bank-rally
  coverage. The universe panel answers "why is this tracked?" for every member.
- **Statistical core**: despike byte-identical; z/percentile/framework/
  co-occurrence math unchanged (three additive changes listed below).
- **Cost**: $0/run without an Anthropic key; ≈ $0.01–0.03/run with one.

---

## Stage status

| Stage | What | Verified how |
|---|---|---|
| 1 | settings / backbone / registry / headline store | live pull: 11 feeds, 227 headlines |
| 2 | extract / resolve / universe state machine | 5 members self-admitted w/ evidence; junk negative-cached; 2-feed rule held back 1-feed repeats |
| 3 | incremental rate-safe fetch | 61/61 series OK across 3 runs; backfill budget deferred exactly 12/run |
| 4 | events selectivity layer | 25 flags → 7 cards; correlation clusters correct; news ties genuine after word-boundary fix |
| 5 | terminal UI (events, universe panel, search, class tabs) | live preview: 7 cards render w/ news, universe table, 74 sparklines, no errors |
| 6 | workflow wiring + this file | YAML valid; digest runs over 61 series with all 4 sections |

---

## Decisions & Assumptions (the ones that matter)

**D1 — Backbone is static by design, not a regression.** The brief allows "a
stable macro backbone you decide the board needs." 56 series in `backbone.py`:
21 global equity indices, 10 FX, 9 rates/credit (added **HY & IG OAS** — credit
stress gauges the board lacked), 9 commodities, BTC/ETH, 5 derived (proven four
+ new `ust_2s10s` curve). Single-name equities are **never** hardcoded — they
only enter via news.

**D2 — Admission is deliberately hard; eviction is deliberately slow.**
Score ≥2.0 (EWMA, 3-day half-life) across **≥2 distinct feeds** to get in;
eviction needs decayed score <0.3 AND 10 quiet days AND not currently flagged.
Cap 40. This is the anti-churn design: one viral headline doesn't admit, one
quiet week doesn't evict, and the board never drops something it's flagging.

**D3 — LLM tier is optional and capped.** One Haiku call per run
(≤150 headlines, ≤1500 output tokens) **only if `ANTHROPIC_API_KEY` exists**.
Heuristic tier (capitalized-span mining + stop-lists + $TICKER) carries the
system alone otherwise — it admitted all 5 members today without the LLM.
LLM outputs go through the same resolver validation as everything else.

**D4 — Resolution is the junk gate, and it remembers.** Gazetteer (commodity
words → futures, theme words → liquid ETFs, shorthands like "Xbox"→MSFT,
hard negatives for private cos: OpenAI/Anthropic/SpaceX/TikTok) → persistent
cache (positive AND negative) → yf.Search (≤12 lookups/run) with quoteType
whitelist + name-similarity + primary-exchange preference. Junk dies once and
is never re-queried. Network errors are NOT negative-cached.

**D5 — Selectivity = events, not per-series flags.** Flag math is untouched;
the *board* shows clusters: flags join an event when 60d return correlation
|ρ|≥0.65 AND today's moves are consistent with that correlation's sign. Score
= strongest member (engine score) + 1.2·ln(breadth) + 2·news-corroboration;
floor 3.2, max 8 cards. Dynamic names carry a stricter amber bar (|z|≥2.0 vs
1.5 backbone). Verified live: 25 flags → 7 cards.

**D6 — Three additive changes to proven statistical code** (flagged per your
instruction, none alter existing series' math):
1. `engine._pct_change`: returns NaN instead of ±inf when the prior value is ~0
   (zero-crossing spreads like 2s10s; display-safety only).
2. `engine._flag_level`: optional per-series `amber_z` parameter (default 1.5
   = exact old behavior; only dynamic members pass 2.0).
3. `fetch.py`: per-spec `no_despike` exemption, applied ONLY to VIX — the
   despike filter's bad-tick signature (isolated 15% spike-and-revert) is
   precisely VIX's genuine signal. VIX history was re-backfilled clean after
   the first run "corrected" 6 real spikes. The despike function itself is
   byte-identical.

**D7 — Fetch is incremental now.** Known symbols get a 15-day tail merge
(fresh values win on overlap); only new symbols get the full 2-year backfill,
budgeted 12/run (queue carries over). Request volume dropped ~10× per run vs
v1 despite 2.3× the symbols. Legacy columns (dabur/britannia/bpcl) keep their
history in prices.csv but are no longer fetched.

**D8 — FRED key access is lazy.** Only `fetch.py` requires it now. The
Streamlit app needs NO secrets (it only reads committed files) — the
`FRED_API_KEY` Streamlit-Cloud secret is harmless but no longer necessary.

**D9 — usd_cnh → usd_cny.** `CNH=X` returns nothing on Yahoo; `CNY=X`
(onshore) verified with 515 rows. **[VERIFY]** if you specifically want
offshore CNH, find a working symbol and swap it in `backbone.py`.

**D10 — Digest format preserved.** Section [2] still lists engine flags (spec
Step 6 unchanged); the events layer is a board concept. [1] now has 61 lines.
`CHAT_PROMPT` untouched.

---

## Tunables you may want to adjust (all in `settings.py`)

| Knob | Default | Effect of raising it |
|---|---|---|
| `UNIVERSE_CAP` | 40 | more concurrent news-tracked names |
| `ADMIT_SCORE` / `ADMIT_MIN_FEEDS` | 2.0 / 2 | harder admission, quieter universe |
| `SURFACE_FLOOR` | 3.2 | fewer event cards (quieter board) |
| `DYNAMIC_AMBER_Z` | 2.0 | stricter flagging for news names |
| `EVENT_CORR_THRESHOLD` | 0.65 | looser clustering → more separate cards |

The three I most expect you'll touch: **SURFACE_FLOOR** (if the board still
feels busy after a week, raise to ~4), **ADMIT_SCORE** (raise to 3 if too many
marginal names get in), **UNIVERSE_CAP**.

---

## Estimated / hardcoded — needs your eye

- **2026 fixed dates** in `calendar_config.py` (FOMC/RBI-MPC/US CPI·PPI·PCE/
  OPEC) — unchanged from v2, still estimates, still need annual refresh.
- **usd_cny** stand-in for CNH (D9).
- **Stop-lists** in `extract.py` — grown from live-data iteration today;
  they'll need occasional additions (new politicians, new boilerplate).
  Junk that slips through still dies at resolution or admission.
- **Gazetteer** in `resolve.py` (~45 entries) — extend as you notice news
  language that should map to a specific instrument.
- **`data/resolution_cache.json`** — negative entries are permanent; if a
  private company IPOs (e.g. OpenAI), delete its cache line + gazetteer entry.

---

## Next actions (in order)

1. **Add the optional secret** (GitHub → Settings → Secrets → Actions):
   `ANTHROPIC_API_KEY` — skip this entirely and the system runs free on
   heuristics. `FRED_API_KEY` already exists and is still used by fetch.
2. **Push** `main` (12 local commits, `522b7be`…). Streamlit Cloud will
   redeploy (~3 min; requirements adds `anthropic`).
3. **Verify the live app**: events section renders with news ties; universe
   panel shows the 5 members; grid tabs + filter work; drill-down loads.
4. **Trigger the workflow manually** (Actions → Scheduled data fetch → Run
   workflow) and check the log: `Update universe from news` step prints the
   headline/universe report; fetch shows tail-refresh + any backfills; commit
   message `data: scheduled fetch + digest … [skip ci]` includes
   universe.json/headlines.json/resolution_cache.json.
5. **Live with it a week, tune to quiet** (same philosophy as v1): watch
   which names get admitted and how many cards a normal day produces, then
   adjust the three knobs above.
6. **Curate occasionally**: skim `data/universe.json` members + the app's
   candidates line; add stop-list/gazetteer entries for anything dumb.

## What to push
Everything on `main` — 12 commits from `v4 stage 1` through this file, all
local. No force-push needed; the branch is ahead of origin only.
