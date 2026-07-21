# SYNTH_V2 · S4 base-rate reconstruction — methodology (FOR APPROVAL)

Written 2026-07-21. **No hit rate is computed until this matching rule is
signed off** (owner demand). A base rate is only as honest as the rule that
decides what counts as "the same setup." This doc fixes that rule; the
numbers come after.

Scope: the flagship `transmission_gap` detector only. `news_no_move` and
`channel_shift` base rates are deferred (different outcome semantics; noted
in §7).

---

## 1 · The matching rule — "the same setup" IS the detector predicate

The setup is not a hand-crafted similarity ("driver moved a lot, target
didn't"). The setup is **the exact live detector predicate, evaluated at a
historical session t on strictly-prior data**. A historical trigger counts as
the same setup if and only if the same function that fires live returns true
at t. This is the only definition that can't drift from what the board
actually shows — there is no second implementation to disagree with.

For every ordered discovered channel `(driver → target)` and every session
`t` in the 530-day matrix with enough PIT history, recompute — using only
data with index `≤ t`, all estimators `shift(1)` / strictly-prior:

1. **Driver market event at t** — `synth_events._move_event` on the driver's
   own `|zc|` series at position t: clears the adaptive bar (q98 of history
   before t), with the min-history floor / fixed-bar band / staleness guard
   already built. *Same function as live.*
2. **Channel admissible at t** — rolling-60d `|rho|` in the upper tail of the
   pair's own history up to t (state `active`/`turning_on`); passes the
   **strength floor computed cross-sectionally over the channels live at t**
   (not today's floor); class-admissible (static, registry-derived).
3. **Signed shortfall clears the gap bar at t** — `expected = beta_pair(t) ·
   driver_ret(t)`; `actual` = target cum return over `h = lead_lag+1`;
   `shortfall = -residual · sign(expected) / (sigma_target(t)·√h)` clears the
   pair's own adaptive gap bar (q90 of its shortfall history before t).
4. **Not a counter-move at t** — the ruling-6 exclusions (daily counter-zc
   beyond the target's own event bar; cumulative window move against the
   implied direction beyond the target's own q50 window move).

The set of `(channel, t)` that pass ALL four is the reconstructed population
of the setup. Implementation reuses `market_events_backfill` +
`detect_transmission_gaps` unchanged, walked across t — so the reconstruction
literally calls the live detector. If the detector changes, the population
changes with it (and the base-rate store is invalidated — §6).

**No forward leakage.** Everything in 1–4 is a feature of data ≤ t. The only
forward-looking quantity is the outcome (§2), which is never an input to the
trigger.

---

## 2 · The outcome — "did the gap close?" (needs your ruling)

A trigger at t carries an implied direction `sign(expected)` and a residual
(how far short the target is). The gap "closes" if the target subsequently
moves in the implied direction enough to absorb the shortfall. Over a
resolution window `t+1 … t+K`:

- Let `remaining` = the implied move not yet realised at t (expected − actual,
  in the implied direction, σ units).
- Track the target's cumulative return from t forward, projected onto the
  implied direction, in σ units → `caught(k)`.

**Proposed outcome states:**
- **CLOSED** — `caught(k) ≥ CLOSE_FRAC · remaining` for some k ≤ K (the
  target catches a material fraction of the outstanding implied move).
- **FADED** — window ends with `caught(K) < CLOSE_FRAC · remaining` (never
  caught up), OR the target moved further against the implied direction.
- The hit rate = P(CLOSED | triggered).

**Rulings (owner sign-off 2026-07-21):**

| knob | RULED | note |
|---|---|---|
| `K` (resolution horizon) | **`clamp(lead_lag, 5, 15)`** | floor a week, CAP at 15 sessions (3 weeks). Past the cap a "resolution" is drift contaminated by everything else, not transmission attributable to the pulse. |
| `CLOSE_FRAC` | **compute BOTH 0.5 and 1.0**; surface 0.5 as headline, 1.0 alongside | the gap between them is signal: 0.5-often/1.0-rarely = a partial-convergence pattern the practitioner must see when sizing. Cheap to store both. |
| first-touch vs endpoint | **first-touch** | matches how the trade is taken; endpoint-only would fail a setup that converged day 3 and reversed by day 10. |
| time-to-touch | **store the distribution, not just the boolean** | first-touch-day-2 and first-touch-day-14 are both "hits" but very different trades; a median TTT of 11 on a 15-cap is drift sneaking under the cap. |
| against-direction | a material against-move (`caught ≤ −0.5·gap`) tags `FADED_AGAINST` vs `FADED_FLAT` | keeps "moved the wrong way" distinct from "never came" |

`CLOSED` = target catches ≥ `CLOSE_FRAC · outstanding_gap` in the implied
direction at some k ≤ K (first-touch). Outstanding gap = `expected − realized`
at the trigger day. Both fracs and the time-to-touch are stored per trigger.

---

## 3 · Pooling hierarchy (per-pair N is tiny)

A single channel fires a handful of times in 530 days — per-pair N is too
small to base-rate alone. Proposed back-off, reported explicitly per
candidate so the reader sees which level answered:

1. **pair-specific** `(driver → target)` — use if `N ≥ N_MIN` (propose 8,
   matching the S6 AMIFT gate).
2. **class-pair** — pool by `(driver_class → target_class)` bucket
   (INDICES→INDICES, INDICES→COMMODITIES, …) + lead-lag bucket. This is the
   natural generalisation and mirrors how the detector already reasons about
   admissibility by class.
3. **global transmission** — all reconstructed gap triggers pooled (the
   analogue of the existing `scorecard.transmission_follow` 0.815 / n=1968).

Each candidate's base rate cites the tightest level that clears `N_MIN`, its N,
and a Wilson 95% CI — never a bare point estimate.

**Ruled additions:**
- **Disclose the pooling level in the surfaced output**, not just internally.
  "72%" means something different at pair-level N=40 than global-level N=600;
  the level IS part of the number (ties to the editorial standard — a
  proprietary metric without its disclosed basis is uncitable).
- **Hard floor:** if even the global pool is below `N_MIN`, return
  `INSUFFICIENT` — never a computed rate on n<8. S6 already consumes
  `INSUFFICIENT`.

---

## 4 · Independence / clustering (honest N, not inflated N)

Two contamination sources, both handled by clustering rather than pretending
independence:

- **Overlapping windows** — a channel firing on consecutive days produces
  overlapping `t … t+K` windows → correlated outcomes. Dedupe to
  non-overlapping triggers per channel (keep the first; skip triggers whose
  window overlaps a kept one), OR keep all and cluster the CI by channel.
- **Fan-out correlation** — one driver-date firing across many targets gives
  correlated outcomes (same driver pulse). Cluster the CI by `driver-date`.
  The point estimate can pool; the CI must not treat six Goldman-day targets
  as six independent draws.

Proposed: report the clustered (conservative) N alongside the raw N so the
discount is visible.

**Ruled tightening — cluster count IS the effective N for the floor.** The
clustering is not only a CI-width correction, it is a sample-adequacy
correction. If a pair's N=8 is really 8 target-legs from 2 driver-dates, the
effective N is ~2 and it must FAIL `N_MIN` despite the raw count clearing it.
So `N_MIN` is evaluated against the **cluster count** (independent
driver-date × channel episodes), never the row count — otherwise fan-out
inflates the sample past the floor and the gate leaks back in through the
denominator.

---

## 5 · Market-only vs news-conditional (ruling 8)

Two base rates, never conflated:

- **Market-conditional (primary)** — trigger = §1 (driver move + channel +
  shortfall + not-counter-move). Sampled over the FULL 530-day matrix. Large
  N, the honest denominator. This is the base rate that ships.
- **News-conditional (refinement)** — additionally require a driver news
  join in the bus at t. The bus only exists back to the git archive window
  (~2h commits since Jul 3), so this sample is **archive-limited and
  small-N** — reported as a flagged refinement, never as the primary number,
  and never back-filled with fabricated history.

---

## 6 · Reproducibility / params binding

The reconstructed population depends on every threshold (`MOVE_QUANTILE 0.98`,
`GAP_QUANTILE 0.90`, `COUNTER_QUANTILE 0.50`, `CHANNEL_STRENGTH_PCTILE 0.25`,
`K`, `CLOSE_FRAC`). The base-rate store records a **params hash**; if any knob
changes, the store is stale and must be recomputed. The golden fixture's four
tripwires already guard the trigger-side knobs; S4 adds `K`/`CLOSE_FRAC` to
the hashed set. Output: `data/synth/base_rates.json`.

---

## A · Point-in-time channel state — no survivorship (owner-added, binding)

The reconstruction re-runs the detector on data ≤ t, and **the channel used at
historical t is the channel as it would have been measured at t** — rolling
correlation, `beta_pair`, the pair's own active-percentile, and every adaptive
bar recomputed on the trailing window ending at t. A pair that is an active
channel today may have been dormant in 2024; grading a 2024 trigger with
today's `beta_pair` or today's `rho` is lookahead and is forbidden.

Concretely, the reconstruction rebuilds channels PIT at each t via
`synth_channels.build_channels(prices.loc[:t])` and feeds THAT into
`detect_transmission_gaps` — it never reads `data/synth/channels.json` (which
is today's state). The cross-sectional strength floor is likewise the p25 of
the trailing-window `|rho|` across the channel universe AT t, not today's
0.385. This is the leak that is easiest to introduce accidentally and
impossible to see in the output, so it is stated explicitly and guarded by a
test (a trigger's `beta_pair` must equal the PIT trailing-window beta at t,
never the golden channels.json beta).

## B · The base rate describes the reference class, not the instance

The reconstruction grades CLOSED historical windows; the live board surfaces
OPEN ones (the golden table's two bovespa legs). So a base rate attached to a
live candidate is a claim about a population the candidate **has not joined
yet**. The surfaced copy must therefore read "setups of this type historically
resolved X%," never "this setup is X% likely to resolve." It is the same
priced-vs-gap honesty one layer up: the number describes the reference class,
not the instance. This is enforced in the packet/copy schema (S5/S7) and noted
in the base-rate record as `frame: "reference_class"`.

## 7 · Deferred

- `news_no_move` / `channel_shift` outcome semantics (what does a
  news-no-move "resolve" to? a subsequent catch-up move? a vol expansion?)
  — separate methodology note, after the gap base rate is validated.
- The cross-sectional/dispersion detector stays deferred (S1–S2 ruling 9).

---

## Status — all rulings received (2026-07-21)

Five knobs accepted with modifications (K-cap 15, dual CLOSE_FRAC,
time-to-touch distribution, pooling-level disclosure + INSUFFICIENT floor,
cluster-count-as-effective-N), plus binding additions A (PIT channel state)
and B (reference-class framing). Next deliverable: the **reconstruction
audit** — trigger population + resolved outcomes on a few pairs, showing a
couple of genuine closes, one first-touch near the cap, and one the
counter-move logic correctly refuses to score — BEFORE any headline hit rate,
so the outcome definition can be checked for honesty on the rows themselves.
