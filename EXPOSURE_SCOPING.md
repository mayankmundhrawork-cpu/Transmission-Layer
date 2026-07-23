# SYNTH_V2 · Exposure / cross-sectional detector — §1 data-feed answer (FOR REVIEW)

Written 2026-07-23. This is **only §1** of the scoping brief: the per-field
obtainability answer. Per build-order step 1, no store schema and no detector
code until this is signed off. If the honest answer were "not obtainable at
acceptable cost", this doc would say that. It does not — but it also does not
accept the brief's "already have it" at face value where that is optimistic.

---

## Viability verdict (lead)

**Viable at zero budget — but ONLY as manual curation of a small universe, and
only if two fields stay permanently flagged as proxies.** The build is not
"acquire an exposure feed"; there is no free structured exposure feed for Indian
names and there will not be one. The build is: a small, hand-curated,
quality-tagged exposure store, joined to the shock and pricing legs that already
exist. The automation ceiling is the **shock + pricing** (recomputed on the
tick); **exposure is irreducibly results-day manual entry.** This is the
"semi-automated by nature" framing, confirmed by the data, not assumed.

One correction to the brief before anything else: the shock leg is **not** fully
"already have it" (see §1.3). It is ~70% in the price matrix and has a real gap
that needs one small monthly fetcher. Flagging so the plan is built on the true
state, not the optimistic one.

---

## 1.1 · The three legs, honestly

| leg | status | what's true |
|---|---|---|
| **Pricing** (relative return vs basket) | **LIVE** | fully in the price matrix; nothing to build |
| **Shock** (input-cost / FX / rate moves) | **PARTIAL** | commodity + FX + rate moves are in the matrix; non-matrix inputs (natural rubber, TiO2, specific chemicals) are NOT — need MOSPI WPI sub-indices, one monthly fetcher |
| **Exposure** (RM/sales, inventory, currency mix, hedge, segment) | **MANUAL** | public in filings, none as a structured free feed, quarterly-at-most cadence |

Two of three legs are effectively live; the third is manual. That ratio is what
makes this viable at all.

## 1.2 · Exposure — per-field verdicts

Source basis: SEBI LODR quarterly results (limited review) + annual report notes
to accounts (Ind AS), filed free on NSE/BSE. **Curation = a human reading the
filing, not scraping** — which also sidesteps screener.in-style ToS questions.

| field | disclosed? | cadence | quality tier | verdict |
|---|---|---|---|---|
| **Cost of materials / revenue (RM/sales)** | Yes, P&L line | **quarterly** | `disclosed` | Best field. Quarterly results carry "cost of materials consumed". Manual entry from the results PDF/XBRL. |
| **Inventory / inventory-days** | Yes, balance sheet | **half-yearly / FY** | `disclosed` (level) + `derived` (days) | Lower cadence — full BS is H1 + FY under LODR, not every quarter. Days = inv ÷ (materials/period), derived. |
| **Segment / geography revenue** | Yes, Ind AS 108 | quarterly (segment) / **annual** (geography) | `disclosed` | Segment revenue quarterly; geographical split annual. Fine for exposure that moves slowly. |
| **Revenue *currency* mix** | **No** — only geography | — | `proxy` | Billing currency is never disclosed; geography is the proxy. This was the FX-capture lesson — it must stay flagged, never dressed as disclosed. |
| **Hedge cover / derivative notional** | Notional yes (notes) | **annual**, some H1 | `disclosed` (notional) + `derived` (cover %) | Outstanding-forward notional is in the financial-instruments note. Cover % (hedged ÷ exposure) is derived; some IT names give it on the concall. Maturity at weekly granularity is NOT obtainable → proxy. |
| **Input-cost basket composition** | Partial (commentary) | ad hoc | `proxy` / `derived` | Which RMs and their weights are rarely quantified; mostly hand-built from industry knowledge. The least-disclosed field, and the one most likely to be `proxy`. |

**Net:** 3 fields are honestly `disclosed` (RM/sales, inventory level, segment/
geography), 3 are structurally `derived`/`proxy` (currency mix, hedge maturity,
input composition). A basket is therefore never all-`disclosed`; the store's job
is to make that visible per field, not to hide it.

## 1.3 · The shock gap (correcting "already have it")

- **In the matrix already:** wti, brent, natgas, comex_copper/silver/gold, wheat/
  corn/soybeans, DXY + the FX crosses, the rate series. Any basket whose input is
  one of these (tyres↔crude/rubber-proxy, some metals) gets its shock free, daily.
- **NOT in the matrix:** natural rubber, TiO2/paints chemistry, specific steel/
  aluminium grades, packaging. For these the shock must come from **MOSPI WPI
  sub-indices** (eaindustry.nic.in, free, monthly, ~2-week lag). That is one small
  fetcher on the pattern of `fetch_fred` — not a large build, but real, and it
  belongs in the plan.
- **Cadence consequence:** the daily tick recomputes the *matrix-sourced* shock
  and the pricing; the *WPI-sourced* shock updates monthly; exposure updates on
  results days. Three different clocks, none of them 3-minute — the tick must not
  pretend exposure or WPI is intraday.

## 1.4 · What is NOT obtainable at any price here (permanent proxies)

Stated so no future session tries to "fix" these by hunting a feed:
- **Billing-currency splits** — only geography is disclosed. Permanent proxy.
- **Currency-specific onsite cost bases** — not disclosed. Proxy.
- **Hedge maturity at weekly granularity** — only outstanding notional, annually.
  Proxy.
- **Realised pass-through vs list price** — never disclosed; hand-estimated in the
  Margin Trap piece. Proxy.

These four were proxied by hand in the published pieces and must carry
`quality: proxy` forever.

## 1.5 · Curation burden (honest numbers)

Most fields update **annually** (inventory, geography, hedge notional, input
composition); only RM/sales is genuinely quarterly. Realistic annual load per
10-name basket:

- RM/sales: 10 names × 4 quarters = 40 entries
- the 5 slower fields: 10 names × ~1 update = ~50 entries
- ≈ **90 field-entries/year per basket**, concentrated on results days, plus a
  one-time historical backfill for the fixtures.

Scope the initial universe to **one basket (~10 names), the Margin Trap paints/
tyres/electricals set**, since it is already assembled and is the first golden
fixture. Do **not** attempt the 95-series universe or a second basket until the
first proves the loop.

## 1.6 · One verification step before curation (intellectual honesty)

The cadence/quality table above is reasoned from Ind AS / SEBI LODR norms, not
from re-reading every filing. Before curating, **spot-check the exact
availability against 2–3 actual filings** in the Margin Trap universe (one tyre,
one paint, one electrical) — specifically whether "cost of materials consumed"
appears in *their* quarterly results and whether inventory is in their Q1 filing
or only H1. If a name buries a field, that name's field is `derived` from the
nearest disclosure, not `disclosed`. Cheap to check; expensive to assume.

---

## Recommendation & STOP

The exposure detector **is viable at zero budget** as a manually-curated,
quality-tagged store over one small basket, joined to the live pricing leg and a
mostly-live shock leg (plus one small monthly WPI fetcher). It is **not** viable
as an automated feed, and it **cannot be back-rated** (§4 of the brief stands —
launch `UNRATED`, accrue the rate forward via a pre-registration log).

Per build-order step 1, **stopping here for review.** On sign-off, the next unit
is §2 (store schema + completeness/staleness tests) and the WPI fetcher — still
no detector predicate until the store exists and the Margin Trap universe is
curated.

Two questions for you before I proceed past §1:
1. **WPI fetcher now or later?** It's the one genuinely-new automatable piece.
   Build it alongside the store (so the shock leg is whole for the first basket),
   or defer and let the first basket run on matrix-only shock where its inputs
   allow? My lean: build it with the store — the Margin Trap basket needs rubber,
   which is WPI-only.
2. **Curation authorship.** The store is your domain knowledge (you built both
   published screens by hand). I can build the schema, the tests, the fetcher,
   and pre-fill the *structure* per name, but the `value`/`source`/`quality`
   judgments on each field are yours to enter or confirm — I will not invent
   exposure numbers. Confirm that division of labour so the store is never seeded
   with guessed values.

---

## Sign-off (2026-07-23) — answers folded, binding for §2+

1. **WPI fetcher: NOW, with the store.** It is a blocker, not a nicety —
   acceptance test #1 (reproduce the Margin Trap ranking) needs rubber, which is
   WPI-only. Two conditions, both binding:
   - **Vintage storage, as-published, never overwritten on revision.** WPI prints
     provisional and is revised; grading a pre-registered screen against a later
     revised value is lookahead — the same error as S4 point A (PIT channel
     state). The store keys every value by `(series, publish_date)` and
     `wpi_asof(series, registration_date)` returns the value that existed AT
     registration, never today's revision.
   - **Confirm granularity before wiring, and tag coarseness as `proxy`.** Rubber
     is plausible as a WPI line; a specific pigment (TiO2) almost certainly is
     not — WPI carries "chemicals & chemical products" far coarser than a pigment.
     Where only a coarse bucket exists, that coarseness is a `quality: proxy`
     fact, tagged, never passed off as the input. Precedent: the published Margin
     Trap piece used a **sector input-basket WPI shock** (coarse) and held up — so
     coarse is workable *if labelled coarse*.
   - **WPI staleness is first-class**, like exposure staleness: monthly with a
     publication lag → a WPI-driven shock can be ~6 weeks old at worst. That goes
     in the packet's data-quality header, not discovered by the reader.
2. **Curation authorship: confirmed AND structural (fail-closed).** I build
   schema/tests/fetcher and pre-fill the skeleton structure; owner supplies
   `value`/`source`/`quality`; I never invent a number. Enforced, not agreed: a
   row with a `value` but null `source` or null `quality` FAILS the completeness
   test, and the skeleton ships with sentinels that fail until curated —
   fail-closed exactly like `driver_admissible`. The division survives a tired
   evening because the store literally cannot hold an unprovenanced value.
3. **Spot-check priority: inventory cadence FIRST**, then RM/sales. Inventory-days
   is the Margin Trap lag dampener; if it is genuinely H1/FY rather than
   quarterly, the dampener runs on up-to-two-quarters-stale data and the whole
   screen's staleness profile changes. RM/sales second (the load-bearing disclosed
   field).
4. **Margin Trap is the first fixture because its core field is the cleanest.**
   RM/sales is `disclosed`+quarterly — the highest-quality field in the whole
   table — while the FX basket's core (currency mix) is structurally `proxy` and
   its hedge maturity is unobtainable. The first fixture must test the MACHINERY,
   not the proxy assumptions; the messy basket stresses it second.

§2 proceeds: exposure store schema + completeness/staleness tests (fail-closed) +
WPI fetcher with vintage storage. **No detector predicate until the store exists
and the Margin Trap basket is curated by the owner.**
