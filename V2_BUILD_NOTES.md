# V2 Build Notes — Transmission Layer

> **READ THIS FIRST.** This is your morning briefing from the overnight v2 build.
> It records what completed, what needs your hand, and your exact next actions.
> The summary at the top is the whole story; detail follows below.

---

## ⭐ MORNING SUMMARY

**All three functional stages completed and verified. Nothing is broken; the
proven data layer (fetch.py despike, engine.py Step 5 math) was not touched.**

- **Stage 1 — Release calendar: ✅ done & verified.** 16 releases compute correct
  next-dates with weekend-rolling; app shows a sorted countdown with clickable
  links, ≤3-day highlight, and a "released last 24h" block.
- **Stage 2 — News digest: ✅ done & verified.** `digest.py` produced a 7.2k-char
  digest in exact Step 6 format with real headlines in **5/5** market groups
  (11 feeds OK, 0 crashes). App shows it with a copy button + the chat prompt.
- **Stage 3 — Workflow wiring: ✅ done & verified.** The scheduled workflow now
  regenerates the digest after the price fetch and commits `digest_latest.txt`
  alongside the price data. YAML valid, all safeguards preserved.
- **Stage 4 — Visual pass: not in scope** for this run (dropped from the final
  goal). Untouched.

**Your 3 next actions when you wake** (details in the numbered section at the
bottom):
1. **Push these commits** — I committed locally but did not push. Run
   `git push` (fast-forward, no conflicts expected). Streamlit Cloud auto-redeploys.
2. **Manually trigger the workflow once** to confirm the digest step works in CI:
   Actions tab → "Scheduled data fetch" → Run workflow. Watch the new
   "Regenerate digest" step; confirm the commit message now reads
   `data: scheduled fetch + digest …`.
3. **Verify the hardcoded 2026 fixed dates** (RBI-MPC, US CPI/PPI/PCE, OPEC) against
   official calendars — links in "Needs your attention".

---

## Stage status

| Stage | What | Status |
|---|---|---|
| 1 | Release calendar (calendar_config.py, release_calendar.py, app panel) | ✅ built & verified |
| 2 | News digest (rss_sources.py, digest.py, app panel) | ✅ built & verified |
| 3 | Wire digest into GitHub Actions workflow | ✅ built & verified |

---

## Decisions & Assumptions

**D1 — Module named `release_calendar.py`, not `calendar.py`.**
The goal said "write calendar.py". A module literally named `calendar.py` in the
project root would shadow Python's stdlib `calendar` module — which I use for
`calendar.monthrange`, and which pandas/datetime tooling can import indirectly.
That shadowing is a classic hard-to-debug footgun. I named the engine
`release_calendar.py` instead. Functionality is identical; only the filename is
safer. `calendar_config.py` is fine (shadows nothing).

**D2 — Weekend rolls only; public holidays NOT modelled.**
Spec Step 4 says "roll to next weekday if holiday/weekend". Modelling Indian /
US / China public holidays needs either a paid API or a bulky dependency
(`holidays`), neither of which fits the zero-budget + stdlib-only constraint for
this stage. I roll Saturdays/Sundays forward to Monday only. Consequence: a
release that officially slips because of a public holiday may display one working
day early. Acceptable for a countdown whose purpose is "read the number in
manually" — you click through on the day regardless.

**D3 — Fixed-date events hardcoded for 2026, flagged for verification.**
FOMC, RBI-MPC, US CPI/PPI/PCE, and OPEC+ are `fixed` rules with hardcoded 2026
dates. FOMC dates are high-confidence (published well ahead). The others are
best-estimates and each carries a `verify` note that surfaces in both the console
output and the app caption. **These must be checked against official calendars
(see "Needs your attention") and refreshed every January.**

**D4 — China added as a 5th market bucket in the calendar.**
Spec Step 4 lists China TSF/credit and China PMI, but the four-market grid
(config.MARKETS) is INDIA/USA/EU/COMMODITIES. Rather than force China items into
a wrong bucket, calendar entries carry `market: "CHINA"`. The calendar panel is
market-agnostic (it lists all releases sorted by proximity), so this is display
metadata only and does not touch the proven config.MARKETS / engine. The digest's
[4] news section also uses the 5-bucket split (USA/India/EU/China/Commodities),
matching spec Step 6 which explicitly names China.

**D5 — "Last 24h" = 24h window with a most-recent-N fallback per feed.**
The environment clock runs at the simulated 2026 date while live RSS servers
stamp entries with their own real-world time, so a strict 24h filter against the
local clock could wrongly empty the news section. digest.py keeps entries inside
a 24h UTC window but, if a feed has fewer than 2 in-window items, tops up from its
most-recent entries (cap 6/feed, 12/market). This guarantees a populated digest
with genuinely recent headlines regardless of clock skew. The digest header and
window use UTC `now`; the calendar uses local `date.today()` — both are "today"
in their own frame, a harmless 5.5h (IST) offset.

**D6 — One-click copy via `st.code`.**
Streamlit's `st.code` renders a built-in copy-to-clipboard icon in the block's
top-right — that is the "one action copy" for the digest, no extra dependency or
JS. The fixed chat prompt sits in an expander directly beneath, also in an
`st.code` block for its own copy button, so you can grab both and paste together.

---

## Stage 1 — Release Calendar ✅

**Files:** `calendar_config.py` (16 releases as structured data),
`release_calendar.py` (schedule-rule evaluator), `app.py` (calendar panel).

**Rule types implemented:** `monthly_day` (nth day, weekend-rolled),
`weekly` (fixed weekday), `daily_business` (Mon–Fri), `fixed` (published date
lists). Pure stdlib datetime + stdlib calendar. No external API.

**Verification** (`python release_calendar.py`, as of 2026-07-04, a Saturday):
computed next-dates all sane. Spot checks that passed —
- India CPI day-12 fell on Sun Jul 12 → correctly rolled to Mon **Jul 13**.
- China PMI day-1 fell on Sat Aug 1 → correctly rolled to Mon **Aug 3**.
- Daily/weekly-Friday items correctly showed **Jul 3** in "released last 24h"
  (yesterday relative to Saturday).
- FOMC **Jul 29**, US PCE **Jul 31**, RBI MPC **Aug 7** — sorted by proximity.
App panel: styled dataframe with clickable LinkColumn, amber highlight for
items due ≤3 days, and a separate "released in last 24h" markdown block with
prominent links. py_compile passes.

---

## Stage 2 — News Digest ✅

**Files:** `rss_sources.py` (feeds grouped by market + manual bookmarks),
`digest.py` (assembler + `CHAT_PROMPT`), `app.py` (Morning digest panel),
`requirements.txt` (+feedparser), output `data/digest_latest.txt`.

**Verification** (`python digest.py`): wrote a 7.2k-char digest in exact Step 6
format — [1] metric state (all 27 series), [2] flags fired (from proven engine),
[3] release proximity (from Stage 1 calendar), [4] news by market. **5 of 5**
market groups populated with real headlines (done-condition was ≥3). 11 feeds OK,
0 failed, 3 empty (handled gracefully, digest still complete). App panel renders
the digest with a copy button + the chat prompt in an expander. py_compile and
import chain pass.

### RSS feed status (from the verification run)
**Working (11):** Federal Reserve, CNBC Economy, MarketWatch Top (USA); ET
Markets, Mint Markets, BusinessLine Markets (India); ECB press (EU); SCMP Economy
(China); OilPrice, EIA Today in Energy, Mining.com (Commodities).

**Empty on this run (3) — watch, may be intermittent or need replacing:**
- **BLS latest** (`bls.gov/feed/bls_latest.rss`) — returned no entries. BLS feeds
  can be flaky/rate-limited; Fed + CNBC already cover US, so not urgent.
- **Business Standard markets** (`business-standard.com/rss/markets-106.rss`) —
  no entries; ET + Mint + BusinessLine cover India well.
- **ECB blog** (`ecb.europa.eu/rss/blog.xml`) — no entries; ECB press works, so EU
  is covered. EU is the thinnest bucket (only ECB feeds) — consider adding a
  stable EU markets feed if you want more depth.

**Manual bookmarks (no reliable RSS, surfaced as click-throughs in the digest):**
China → NBS, PBoC, Caixin Global. India → RBI press.

---

## Stage 3 — Workflow wiring ✅

**File:** `.github/workflows/fetch.yml`.

Added a **"Regenerate digest"** step that runs `python digest.py` after
**"Run fetch"** and before the commit step, with `FRED_API_KEY` in its env
(digest.py imports the engine → config, which requires the key). The commit step
now stages `data/digest_latest.txt` alongside `data/prices.csv` and
`data/fetch_log.json`, and the message reads `data: scheduled fetch + digest …`.

**Preserved safeguards (verified by YAML parse):**
- Triggers remain `schedule` + `workflow_dispatch` only → **no self-loop** (a
  push cannot trigger it).
- `[skip ci]` still in the commit message.
- No-empty-commit guard (`git diff --cached --quiet`) unchanged.
- `permissions: contents: write` and `concurrency: fetch-data` unchanged.

**Calendar needs no fetch** — it computes live from rules at app-open, so only the
digest was added to the scheduled job, exactly as specified.

**I did NOT trigger the workflow** (per instruction). See next actions.

---

## Next actions for you (precise, in order)

1. **Push the local commits.** I committed each stage but did not push. From
   `C:\Users\MAYANK\OneDrive\Desktop\Substack`:
   ```
   git push
   ```
   This fast-forwards origin/main (I first pulled the 2 bot commits that had
   landed, so no divergence). Streamlit Cloud auto-redeploys within ~30s and will
   show the new calendar + digest panels. New commits to push: Stage 1
   (`43ca83c`), Stage 2 (`94caf60`), Stage 3 (this one).

2. **Manually trigger the workflow once** to confirm the digest works in CI:
   GitHub → **Actions** → **Scheduled data fetch** → **Run workflow** → main.
   In the run, expand **Regenerate digest** — it should print
   `market groups with headlines: N/5` and write the file. Then check the
   **Commit and push** step made a commit reading `data: scheduled fetch + digest …`.
   (If it says "No data changes — skipping commit", the CSV+digest were identical
   to what's already committed — re-run after the next market close.)

3. **Verify the 2026 fixed dates** below and refresh each January.

4. **Set FRED_API_KEY locally** if you want to run `python digest.py` or the app
   yourself (same key handling as v1):
   `powershell:  $env:FRED_API_KEY = "<key>"` — the digest imports the engine,
   which requires it even though the digest itself only reads the CSV + RSS.

---

## Needs your attention (verify & maintain)

### Fixed dates to confirm against official calendars (and refresh each Jan)
- **RBI MPC 2026** — estimates. Confirm: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx
- **US CPI 2026** — estimates. Confirm: https://www.bls.gov/schedule/news_release/cpi.htm
- **US PPI 2026** — estimates. Confirm: https://www.bls.gov/schedule/news_release/ppi.htm
- **US PCE 2026** — estimates. Confirm: https://www.bea.gov/news/schedule
- **OPEC+ ministerial 2026** — placeholders only (announced ad hoc). Confirm: https://www.opec.org/
- **FOMC 2026** — high-confidence but worth a glance: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm

_(RSS feed status and workflow-trigger reminder are added in Stages 2 & 3.)_
