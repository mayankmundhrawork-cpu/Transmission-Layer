# Exposure redesign · Step 0 audit — yfinance fundamentals coverage (STOP-AND-REPORT)

Run 2026-07-23 against live yfinance 1.5.1. Empirical, per name — real field
names and coverage, not assumptions. **No code changed; stopping for review.**

## Verdict

**The fetcher approach is viable.** yfinance carries quarterly fundamentals for
all ten Margin Trap names — revenue, a COGS line, and inventory — enough to
compute `rm_to_sales` and `inventory_days` with vintage. Two caveats that are
findings, not blockers, are in §3–§4. This overturns the §1 claim that RM/Sales
is filing-dependent: it is a computed ratio over a fundamentals feed, and it
belongs in a fetcher, exactly as the redesign brief argues.

## 1 · Coverage per name (measured)

Correction first: **CEAT's ticker is `CEATLTD.NS`, not `CEAT.NS`** (the latter
returns empty / "possibly delisted"). All ten below are the correct symbols.

| name | ticker | qtr income (Q) | qtr balance-sheet (Q) | Total Revenue | Cost Of Revenue | Inventory | fetched CoR/Rev (latest) |
|---|---|---|---|---|---|---|---|
| CEAT | CEATLTD.NS | 5 | 2 | Y | Y | Y | 0.661 |
| Kansai Nerolac | KANSAINER.NS | 5 | 2 | Y | Y | Y | 0.652 |
| MRF | MRF.NS | 6 | 3 | Y | Y | Y | 0.612 |
| Berger Paints | BERGEPAINT.NS | 5 | 2 | Y | Y | Y | 0.558 |
| Asian Paints | ASIANPAINT.NS | 5 | 3 | Y | Y | Y | 0.553 |
| Blue Star | BLUESTARCO.NS | 5 | 2 | Y | Y | Y | 0.785 |
| Polycab | POLYCAB.NS | 6 | 3 | Y | Y | Y | 0.762 |
| Apollo Tyres | APOLLOTYRE.NS | 6 | 3 | Y | Y | Y | 0.530 |
| Voltas | VOLTAS.NS | 6 | 3 | Y | Y | Y | **0.801** |
| Havells | HAVELLS.NS | 5 | 2 | Y | Y | Y | 0.687 |

- **Income statement**: 5–6 quarters per name, uniform schema.
- **Balance sheet**: only **2–3 quarters** per name — materially thinner than
  income. This is the empirical confirmation of the per-field staleness
  asymmetry the brief made a ruling: `rm_to_sales` (P&L) is quarterly-fresh;
  `inventory_days` (balance sheet) is genuinely lower-cadence and can be ~2
  quarters stale. Encode that asymmetry, don't average it away.
- All values are absolute rupees, so `rm_to_sales = CoR / Revenue` is a computed
  0–1 ratio (range guard applies), and `inventory_days = Inventory / (CoR/days)`
  needs both feeds (so it inherits the balance sheet's thinner cadence).
- The fetched ratios span 0.530–0.801, all inside (0,1) — the range guard is
  well-calibrated and would catch a percentage slip.

## 2 · The one comparison point we have — and it matches

The only published RM/Sales value provided so far is **Voltas 0.803**. Fetched
`Cost Of Revenue / Total Revenue` (latest quarter) = **0.801** — a **0.002**
match. That is strong evidence the aggregator the published screen used computes
RM-cost the same way yfinance's "Cost Of Revenue" does. **But it is one name.**
The other nine need your published RM/Sales values to confirm the feed reproduces
the screen across the basket — I will not assume nine matches from one.

## 3 · The RM-cost definition mapping (the important caveat)

yfinance exposes **`Cost Of Revenue`** — a COGS *aggregate*. There is **no
materials-specific row**: the full quarterly income statement (Asian Paints,
inspected in full) carries `Total Revenue`, `Cost Of Revenue`,
`Reconciled Cost Of Revenue`, `Operating Expense`, `Total Expenses`, `Gross
Profit` — and no "cost of materials consumed", "purchases of stock-in-trade", or
"inventory adjustments" line. So the feed **collapses the three RM-cost
definitions the published screen's limitations section named into one aggregate**
and cannot distinguish them.

- The label is **consistent across all ten names** (all use `Cost Of Revenue`),
  so the mapping is at least uniform — no per-name definitional drift within the
  feed.
- But "consistent aggregate" ≠ "cost of materials consumed". The fetched
  `rm_to_sales` is `quality: derived` with a documented definition variance, and
  the Voltas match suggests the variance is small — for that name.
- **Consequence for fixture 4b (pre-authorised as a finding, not a bug):** if
  fetched CoR/Rev does not reproduce the published RM/Sales for some names, that
  is real information about the published screen's provenance, recorded here — it
  does NOT license tuning the fetcher to hit the published numbers.
- One open design choice the audit surfaces: **period/aggregation** — latest
  quarter vs TTM vs annual. Voltas matched on latest-quarter; the fetcher must
  pick and document this, and it affects reproduction.

## 4 · What the feed does NOT carry (stays manual — FxCapture tier)

Confirmed absent from yfinance fundamentals, unchanged from §1:
- **billing-currency mix** — only geography is disclosed anywhere; yfinance
  carries neither. Permanent `proxy`.
- **hedge notional / maturity** — a notes-to-accounts item; not in the feed.
- **currency-specific onsite cost base** — not disclosed anywhere.

These are the `FxCapture` metric's inputs and stay in the manual tier, uncurated
until the owner supplies them — the interface gets implemented, the fields stay
failing, never faked.

## 5 · WPI base note (carried from the WPI confirmation)

WPI rebased 2011-12 → 2022-23 effective June 2026 — a discontinuity the vintage
store already tracks (`fetch_wpi.same_base`). Relevant because the shock leg for
non-matrix inputs (rubber) rides WPI and its vintages straddle the base change.

## 6 · Reusable pieces (no rebuild needed)

- **`fetch_wpi.py`** — the vintage discipline to mirror exactly: `(series,
  publish_date)` keying, never-overwrite, `wpi_asof` no-lookahead. The
  fundamentals adapter is the same pattern keyed on `(ticker, metric, period_end,
  fetched_at)`.
- **`fetch_yf_batch_live` / `fetch_yf_batch_tails`** (fetch.py) — the yfinance
  batching / retry / per-symbol-fallback precedent; the fundamentals fetch
  should reuse the retry + pacing (this audit hit one transient empty on CEAT
  before the ticker fix, so retry matters).
- **`synth_exposure.py`** — the fail-closed provenance machinery + the 0–1 range
  guard STAY. The redesign changes where values come from (fetched-with-vintage),
  not the guards on them.

## 7 · Reproduction across conventions (all ten, measured) — the provenance finding

Owner supplied the published RM/Sales table; fetched `Cost Of Revenue /
Total Revenue` computed three ways. Best-fit Δ = smallest gap to published over
the three conventions.

| name | published | latest-Q | ttm-4Q | annual | best Δ |
|---|---:|---:|---:|---:|---|
| CEAT | 0.610 | 0.661 | 0.624 | 0.622 | annual 0.012 |
| Kansai Nerolac | 0.571 | 0.652 | 0.647 | 0.653 | **ttm 0.076** |
| MRF | 0.607 | 0.612 | 0.627 | 0.652 | latestQ 0.005 |
| Berger | 0.581 | 0.558 | 0.572 | 0.581 | annual 0.000 |
| Asian Paints | 0.482 | 0.553 | 0.563 | 0.566 | **latestQ 0.071** |
| Blue Star | 0.778 | 0.785 | 0.774 | 0.769 | ttm 0.004 |
| Polycab | 0.755 | 0.762 | 0.764 | 0.784 | latestQ 0.007 |
| Apollo | 0.551 | 0.530 | 0.546 | 0.557 | ttm 0.005 |
| Voltas | 0.803 | 0.801 | 0.784 | 0.785 | latestQ 0.002 |
| Havells | 0.669 | 0.687 | 0.678 | 0.702 | ttm 0.009 |

**Findings:**
1. **8 of 10 reproduce to ≤ 0.012 on their best-fit convention.** The feed does
   carry the aggregator's number for most of the basket.
2. **Two names diverge ~7 points on EVERY convention: Asian Paints (0.071) and
   Kansai Nerolac (0.076) — both paints, both fetched HIGH.** Published is *below*
   fetched COGS/Rev, which is the signature of the aggregate-vs-materials gap:
   yfinance `Cost Of Revenue` ≥ cost-of-materials-consumed, and the surplus
   (processing, solvents, packaging) is largest for paints. Voltas (traded goods,
   COGS≈materials) matches to 0.002. The divergence is **definitional, not
   period** — no convention closes it.
3. **No single convention reproduces the whole basket** (best-fit splits across
   latest-Q / ttm / annual). This is decisive for the design choice: pick
   **trailing-4Q on principle** (seasonality smoothing), NOT to maximise matches —
   matching is a definitional problem a period choice cannot fix.
4. **Consequence, pre-authorised:** fixture 4b (fetched) will NOT reproduce 4a
   (published) for the two paints names; their GM-at-Risk will differ. That is
   recorded provenance about the published screen, not a fetcher bug, and the
   fetcher will NOT be tuned to close it.

**Rulings folded (2026-07-26):** production default **trailing-4Q**, store all
three; `inventory_days` = latest available (balance sheet is 2–3 Q only) with the
longer staleness tolerance, disclosed in the packet; **CEATLTD.NS** goes in a
ticker-mapping config, not inline; provenance strings name the actual fields
(`CostOfRevenue/TotalRevenue`) so the reader sees it is an aggregate.

## Stop — questions before Step 1

1. **Confirm the other nine published RM/Sales values** (or point me at them) so
   4a can be written and 4b's reproduction can be judged. Voltas matches; I need
   the rest to know whether the feed reproduces the screen or diverges (either is
   a valid, recordable outcome).
2. **Period/aggregation choice** for the fetched ratio: latest-quarter (matched
   Voltas), trailing-4Q, or annual? This is a fetcher design decision with a
   reproduction consequence — your call, documented either way.
3. Proceed to Step 1 (`fetch_fundamentals.py`, vintage + no-lookahead + per-field
   staleness) on this coverage? The data supports it.
