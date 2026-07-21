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

**Open choices I need you to rule on:**

| knob | proposal | alternative |
|---|---|---|
| `K` (resolution horizon) | `K = max(lead_lag, 5)` — tie it to the pair's own lead-lag, floored at a week | fixed `K=10` for all pairs (simpler, comparable across pairs) |
| `CLOSE_FRAC` | `0.5` — catch half the outstanding gap | `1.0` (full convergence) — stricter, lower hit rate |
| direction of "against" | any close beyond `−0.5σ` against = not a fade, still open | strict: any against-move ends it as FADED |
| first-touch vs end-of-window | CLOSED on first k that clears (path-based) | evaluate only at t+K (endpoint) |

My recommendation: `K = max(lead_lag, 5)`, `CLOSE_FRAC = 0.5`, first-touch,
because a practitioner acts on partial convergence within the lead-lag
horizon, not full mean-reversion at a fixed endpoint. But this is the single
most consequential definitional choice in S4 — it decides what "worked"
means — so it's yours.

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

## 7 · Deferred

- `news_no_move` / `channel_shift` outcome semantics (what does a
  news-no-move "resolve" to? a subsequent catch-up move? a vol expansion?)
  — separate methodology note, after the gap base rate is validated.
- The cross-sectional/dispersion detector stays deferred (S1–S2 ruling 9).

---

## What I need from you before writing a line of S4 code

1. The §2 outcome knobs — `K`, `CLOSE_FRAC`, first-touch vs endpoint,
   against-direction strictness. **This is the ruling that matters most.**
2. Confirm the §3 pooling back-off (pair → class-pair → global) and `N_MIN=8`.
3. Confirm §4 clustering by channel + driver-date for the CI.

Then I build the reconstruction, show you the trigger population and the
resolved outcomes on a few pairs (the reconstruction audit) — still before
any headline hit-rate — so you can sanity-check that "CLOSED" is being called
correctly, exactly as this S2 table let you sanity-check the detector.
