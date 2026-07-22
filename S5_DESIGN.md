# SYNTH_V2 · S5 — the investigation-assembler (FOR APPROVAL, no Groq yet)

Written 2026-07-22. **No prompt is written until this design is signed off.**

S4 changed what S5 is. We built S4 expecting it to *validate* setups with a
hit rate. On two years it does the opposite: the flagship transmission-gap
family is `NO_RELIABLE_EDGE` (within-class ~a coin flip whose misses skew
against; cross-asset unratable). So S5 is **not** "narrate the setup." It is:

> assemble the investigation packet for a divergence the engine already knows
> is historically unreliable, so a human can decide whether THIS instance has a
> mechanism the base rate doesn't capture.

That is exactly the CEAT-margin / FX-capture judgment made by hand: a
divergence is a question, not an answer. S5 hands over the question, fully
worked, and is structurally forbidden from answering it.

---

## 1 · The reframe (display contract) — divergence, not setup

A transmission gap is relabelled everywhere reader-facing:

- `kind: transmission_gap` → disposition **`LEAD` / "divergence to investigate"**,
  never "setup", never "signal".
- The packet headline is the **reference-class verdict**, not the rate:
  "No reliable edge in this reference class (INDICES→INDICES): half-close 0.56
  [0.33–0.77], full-close 0.31, misses 6:1 against. Treat as a lead."
- The rate/interval/miss-skew appear only as **evidence beneath** the verdict
  (already built: `base_rate_record` is verdict-primary).

A candidate can only be dispositioned **`OBSERVATION` / actionable** when its
reference-class verdict is `PROVISIONAL_EDGE` or better AND it clears the S6
gate. On today's data no transmission-gap family qualifies, so every gap ships
as a LEAD. That is the honest posture, enforced, not a tone.

## 2 · Re-rank the surface (three trust tiers)

The single ranked list becomes three explicit tiers; within a tier, the
existing surface_score orders:

1. **Observation — news-corroborated mechanism.** `news_no_move` with a live
   cluster (the golden-day wti/brent energy cluster). A catalyst-grounded
   mispricing, not a transmission bet — S4's coin-flip finding does not touch
   it. Highest trust.
2. **Observation — exposure divergence** *(reserved; the deferred
   cross-sectional detector — §6).* Empty today, ranked here when built.
3. **Lead — transmission divergence.** Every driver_pulse. Explicitly marked
   "lead: reference class shows no reliable edge," sits below tiers 1–2, and
   its base-rate verdict rides on the card. A bare gap can never outrank a
   news-corroborated observation, regardless of score.

This is the S2 news-privilege rule hardened into tiers: the news-join is the
mechanism, and mechanism outranks correlation whose base rate just came back a
coin flip.

## 3 · The S6 cap contract (what S5 hands S6, what S6 may not do)

`verdict` is a **hard confidence cap**, code-enforced before any LLM output is
shown:

| reference-class verdict | max disposition S6 may assign |
|---|---|
| `PROVISIONAL_EDGE` | OBSERVATION (actionable, still hedged by interval) |
| `NO_DEMONSTRATED_EDGE` | LEAD |
| `NO_RELIABLE_EDGE` | LEAD (and the against-skew is surfaced as risk) |
| `INSUFFICIENT` | LEAD, tagged "reference class too rare to rate" |

S6 (the AMIFT critic) can only ever *lower* the disposition (kill a lead), never
raise it. No LLM phrasing can promote a `NO_RELIABLE_EDGE` divergence to a
thesis — the cap is applied to the record, not requested of the model.

## 4 · The packet (deterministic; the LLM never sees a blank page)

Assembled entirely in code from existing stages — useful with the LLM OFF:

```
InvestigationPacket {
  instance        driver -> target, date
  disposition     LEAD | OBSERVATION            (from the cap, code-set)
  divergence      {driver_zc, driver_class, beta_pair, expected_pct,
                   actual_pct, residual_sigma SIGNED, shortfall_sigma,
                   channel_state, channel_stability, window_open}
  reference_class {verdict, adequacy, evidence:{clusters, ratio,
                   rate_05, rate_10, miss_split}, basis}   # S4, verdict-first
  corroboration   {cross_asset co-movers computed PIT, news_join or null,
                   join_trust}                              # code, not LLM
  the_question    the ONE thing a human must resolve — templated from the
                  verdict: e.g. "INDICES->INDICES rarely transmits and misses
                  skew against; does THIS driver move implicate <target>
                  through a mechanism the reference class omits (shared
                  catalyst, exposure, positioning)? If not, it is noise."
  falsifier       the observation that would kill the lead (code-derived:
                  the against-move threshold, the window expiry)
  prices_stale    bool
}
```

## 5 · The LLM's job (decomposed, capped, escape-hatched) — spec only

Two small calls, temp ≤ 0.2, strict JSON, versioned in `prompts/`. Neither can
assert an edge; both operate strictly below the cap.

- **Call A — Classify** `{INVESTIGATE | DISMISS | INSUFFICIENT_CONTEXT}`.
  Given the packet, does a plausible instance-specific mechanism exist that the
  reference class would miss? DISMISS drops the lead (noise). Escape hatch:
  `INSUFFICIENT_CONTEXT` when the packet lacks what's needed — never a guess.
- **Call B — Articulate** (only if INVESTIGATE): phrase *the question and the
  falsifier* for the reader, cite the news id and the base-rate verdict
  verbatim, and state what would confirm/kill it. **Falsifier-or-drop**: no
  falsifier, no card. Call B may not output a probability, a "should," or the
  word "setup"; it describes a lead to investigate.

LLM-off fallback: the deterministic packet + templated `the_question` is
already a usable investigation card. The LLM only sharpens phrasing and prunes
noise — it never manufactures confidence.

## 6 · What this says about where the edge lives (not S5, but it frames S5)

S4 quantitatively confirmed the transmission-gap family is the weaker signal
and the **news-corroborated** and (deferred) **exposure-divergence** families
are where real edge should live — those are catalyst/exposure mispricings with
a mechanism, not transmission bets. Recommendation carried into the roadmap:
prioritise the deferred exposure-feed / cross-sectional detector next, because
the data now says the engine's most reliable output is the one it can't yet
compute. (Out of S5 scope; flagged so S5's tier-2 slot is reserved, not
forgotten.)

## 7 · Acceptance tests S5 must ship with

- no card asserts a rate as headline (verdict-primary enforced);
- every LEAD cites its reference-class verdict + basis;
- the cap holds: no packet with `NO_RELIABLE_EDGE`/`INSUFFICIENT` can carry
  disposition OBSERVATION, in code, regardless of LLM output;
- LLM-off produces a usable packet;
- Call B with no falsifier yields no card;
- news-corroborated observation always ranks above every transmission LEAD.

---

## Sign-off requested

1. The reframe (§1) + three-tier re-rank (§2) — these are the display-contract
   pieces I held rather than blind-commit. Approve and I wire them into
   `synth_detect`'s surface + a `synth_packet.py` assembler.
2. The S6 cap table (§3).
3. The Call A/B decomposition (§5), specifically that Call A's classes are
   `{INVESTIGATE | DISMISS | INSUFFICIENT_CONTEXT}` (investigation framing),
   not the original `{GAP | PRICED | UNEXPLAINED | INSUFFICIENT}` (thesis
   framing) — the reframe changes the classifier's job.

Then I build the deterministic assembler + tests first (LLM-off), show you a
packet on the golden snapshot, and only after that eyeball do I write the two
prompts.
