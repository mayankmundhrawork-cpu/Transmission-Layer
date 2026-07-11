# The Transmission Layer — User Guide

A macro anomaly board that assembles its own tracked universe from the news,
flags genuine dislocations, drafts the first pass of your analysis, and feeds
your writing workflow — built for an Indian market practitioner watching how
global signals transmit into Indian securities. Runs unattended on GitHub
Actions, serves from Streamlit Cloud, costs ₹0/month.

---

## 1 · The morning loop (60 seconds to oriented)

1. Open the board. Everything expensive was computed overnight — theses,
   research bundles, correlations, analogues.
2. **Status bar**: how many series, how many red/amber, how many events,
   which desks are open. If events = 0, that's a valid answer — calm day.
3. **Squawk box**: last few hours of @DeItaone wire headlines (~2-min lag).
4. **Event cards**: each dislocation with its thesis, the instruments that
   should move next, the India transmission line, and the motivating news.
5. Pin what matters → add a note → **export brief** → open your editor
   already holding cited numbers, precedents and a draft mechanism.

---

## 2 · Reading the board, zone by zone

### Status bar
`TRANSMISSION LAYER │ AS OF … │ 78 SERIES (57+21/40) │ ●3 RED ●21 AMBER │ 8 EVENTS (13 SUPPR) │ FETCH …Z │ IST CLSD · LDN CLSD · NY OPEN`

- **57+21/40** = 57 backbone series + 21 news-admitted members of a 40 cap.
- **SUPPR** = flags absorbed below the event floor — the board is being
  selective, not blind.
- Session cluster: the **bright** desk is open right now (DST-aware).

### Squawk · DeItaone
Live wire headlines scraped from the public Telegram mirror of @DeItaone
(no X API needed). Bright rows are <30 min old. Refreshes at most every
120 s while the app is open — the ~2-minute lag you accepted. Squawk lines
also flow into the news pipeline, so they can admit tickers to the universe
and attach as evidence on events.

### Global strip / India strip
Key cross-market gauges (S&P, VIX, 10y, HY OAS, DXY, Brent, gold, BTC, INR,
Nifty), then the home market: Nifty, Midcap, INR, GoI 10y, India CPI YoY —
plus the next India data prints with countdowns. Amber/red text on a cell =
that series is currently flagged.

### Events — the loud layer
Raw per-series flags are clustered by correlation so one real dislocation is
ONE card, ranked by score (strength + breadth + framework + news
corroboration). Each card carries:

- **Members** with flag-tinted sparklines, z-scores, 1-day moves.
- **Thesis block** — mechanism → gap → watch-next responders → an
  **india_take** (which Indian instrument expresses the view). Tag shows the
  model (`llama-3.3-70b-versatile` via free Groq tier) or `skeleton` when no
  key is set — the responders/analogue lines are pure math either way.
- **→ INDIA line** — Indian receivers of this event by correlation/lead-lag,
  with their current z (has it transmitted yet, or is it pending?).
- **Research bundle** (expander) — full articles behind the headlines
  (excerpts, paywall-graceful), primary sources (FRED pages, exchange pages,
  EIA/CFTC/RBI), historical analogue dates, and copy-ready citations.
- **Pin** — sends the whole card (numbers, thesis, citations) to the
  scratchpad.

Below the cards: the **watchlist** line = sub-floor flags, deliberately quiet.

### Drill-down
Any series → price with MA20/50, 20-day mean & range, amber/red z-bands,
historical flag markers, ringed latest point. Zoom/hover on. Defaults to the
top event's strongest member. Screenshot-ready for posts.

### Relations · correlation & lead-lag
Pick an instrument → ranked correlation neighbours (60d & 252d), who
historically leads whom and by how many sessions, each neighbour's current z.
The overlay chart rebases the strongest pair to 100 with the lag applied.
This is the substrate behind every "X moved; Y is next" line.

### Patterns · historical replay
Structured query builder — *series / metric (z20, 1-day %, level, percentile)
/ operator / value* → every historical episode matching, then what happened
to your chosen response series over the next 5 and 20 sessions (median,
hit-rate, range, path sparkline). **Pin precedent** drops the stats into the
scratchpad as citable history. Example that works today:
`ust_10y · d1pct · ≥ · 2.0` → 14 episodes → gold +2.4% median +20d, 77% hit.

### Scratchpad
Everything you pin lands here with its evidence attached. Add a note to any
pin (end it with `?` and it becomes an Open Question in the export).
**Export brief** downloads a structured markdown draft — thesis, numbered
cited evidence, precedents, open questions. **Clear** is two-step and takes
a backup first.

> ⚠ On Streamlit Cloud the filesystem resets on redeploy — **export before
> you close**. Running locally, pins persist indefinitely.

### Hypotheses & journal
- **Hypothesis**: jot an idea ("if Brent holds 72, OMCs underperform Nifty
  within 5 sessions") → save → **evaluate** sends it with current board
  state to the free LLM for a structured critique: mechanism check, what
  would confirm/refute, which instruments express it.
- **Journal**: log trade *intents* (instrument, side, level, rationale) tied
  to the board state that motivated them — no broker connection, by design,
  but the record is export-ready for when your trading terminal links up.

### Universe · news-tracked layer
Every news-admitted member with its mention score, age, quiet-time, and the
exact headline that admitted it ("why tracked" is always answerable).
Below: candidates pending admission and what they still need.

### Grid · full universe
All series, class-tabbed (indices / equities / FX / rates / commodities /
crypto / derived), searchable, with sparklines and full statistics. Calm rows
are monochrome — a flagged row is the loudest thing in the table.

### Release calendar & morning digest
India-and-global data releases with countdowns (accent edge = due ≤3 days;
released <24h get prominent links), and the one-click digest + fixed chat
prompt for the event-to-price-gap ritual.

---

## 3 · The flag language

- **z20** — today vs the prior 20 sessions, in standard deviations.
- **Amber** — |z| ≥ 1.5 (backbone) / ≥ 2.0 (news-admitted names), or a 1-year
  percentile extreme (≤5 / ≥95), or a named framework trigger (oil ±1.5%/day,
  TIPS ±5bp/day, GSR bands, VIX +15%/day…).
- **Red** — |z| ≥ 2.5, or framework trigger + elevated z.
- **Events** — flags whose 60-day returns are correlated AND moving
  consistently are fused into one card; score must clear a floor (3.2) to
  surface. Everything else is suppressed into the watchlist.
- **Red/amber appear nowhere else in the UI.** If you see those colours,
  something is flagged. An empty events zone is the correct resting state.

---

## 4 · The self-assembling universe

- **Admission**: an entity must be mentioned in ≥2 distinct feeds with
  enough weight (score ≥2, 3-day half-life decay), then resolve to a real,
  validated Yahoo symbol. Junk names die at resolution and are remembered
  forever (negative cache).
- **Eviction**: only when the score has decayed below 0.3 AND the name has
  been quiet 10+ days AND it isn't currently flagged. Cap: 40 members.
- **Curation** (occasionally): skim the universe panel; if something dumb got
  in, add a stop-word in `extract.py` or a gazetteer/negative entry in
  `resolve.py`. If a private company IPOs, delete its negative-cache line.

---

## 5 · Freshness

| Layer | Cadence |
|---|---|
| Squawk | ~2 min while the app is open (120 s cache) |
| Prices | every 2 h on weekdays (GitHub cron) + intraday last-price upsert, so the board is at most ~2 h behind live |
| Official closes | 21:30 UTC anchor run; provisional intraday prints are overwritten automatically |
| News / universe / theses / bundles | every scheduled run, overnight-complete |

Manual refresh anytime: GitHub → Actions → *Scheduled data fetch* → Run
workflow. The bot commits the new data; Streamlit picks it up.

---

## 6 · Operations

**Secrets** (GitHub → Settings → Secrets → Actions):
- `FRED_API_KEY` — required (rates/credit data).
- `GROQ_API_KEY` — optional, free; upgrades theses and hypothesis evaluation
  from skeleton to prose. No paid LLM exists anywhere in the system.

**Costs**: $0/month. Free data, free LLM tier, ~700 of 2,000 free Actions
minutes.

**Knobs** (in `settings.py`, tune after living with it):
- `SURFACE_FLOOR` 3.2 — raise if the board feels busy.
- `ADMIT_SCORE` 2.0 / `UNIVERSE_CAP` 40 — universe strictness.
- `DYNAMIC_AMBER_Z` 2.0 — flag bar for news names.
- `LAGGARD_MIN_CORR` 0.5 — "watch next" list length.

**Annual chore**: refresh the fixed 2026 dates in `calendar_config.py`
(FOMC / RBI MPC / US CPI·PPI·PCE / OPEC) each January.

---

## 7 · Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Red `Failed to fetch dynamically imported module` boxes | Browser holding a stale frontend bundle after a redeploy | Hard refresh (`Ctrl+F5`); incognito if stubborn |
| `ImportError` on deploy after a code push | Streamlit soft-synced source without rebuilding the container | share.streamlit.io → app → ⋮ → **Reboot**, or bump the `rev:` comment in `requirements.txt` |
| Squawk box empty | Telegram mirror briefly unreachable | It degrades gracefully; check again in a few minutes |
| A feed shows EMPTY in logs | RSS sources are intermittent | Normal; the run continues. Worry only if a whole market group is empty for days |
| Workflow run failed | Check the failing step's log in Actions | Data-dependent issues usually self-heal next run; else read the traceback |
| Pins vanished on the cloud app | Redeploy reset the ephemeral filesystem | Export the brief before closing; run locally for persistent pads |

---

## 8 · File map (for when you want to change something)

| Concern | File |
|---|---|
| What's tracked (backbone) | `backbone.py` |
| Universe rules & stop-words | `universe.py`, `extract.py`, `resolve.py` |
| Flag math (proven, don't touch casually) | `engine.py` |
| Event clustering & news ties | `events.py` |
| Correlations / lead-lag | `relations.py` |
| Pattern queries / analogues | `patterns.py` |
| Theses & LLM routing | `thesis.py`, `settings.py` |
| Research bundles / articles | `research.py` |
| India receivers | `india.py` |
| Squawk | `squawk.py` |
| Scratchpad / journal | `scratchpad.py`, `journal.py` |
| All tunables | `settings.py` |
| The board itself | `app.py` (design tokens in `UI_NOTES.md`) |
| Schedule & CI | `.github/workflows/fetch.yml` |
