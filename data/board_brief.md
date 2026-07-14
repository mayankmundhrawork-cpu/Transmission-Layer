# Transmission Layer — board brief · 2026-07-14 08:26Z

data as of **2026-07-14** · 92 series · 8 red / 31 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.419, 5d in regime; vol-pct 0.602, breadth-off 0.235, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.27, corr60 -0.45, contra nifty_50 corr20=0.42, last shift 2026-05-19. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.44, corr60 0.37, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 -0.03, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.19, corr60 0.25, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 76** scanned series survive multiplicity control (effective p ≤ 0.001422727937290702)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.4, β 0.2428, p 0.0); driver zc 3.11 → expected 0.694%. Type hit-rate 0.815 (n=1968).
- Track record · residual_reversion: hit-rate **0.489** (n=1020) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=1968) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.579** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 5.7] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 480.20, z20 5.70, zc 0.90, resid-z 1.63 [unexplained], 1d 8.40%, |z20|=5.70
- **Mechanism**: dyn_kalyankjil_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-07 (z-distance 1.99).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.58 via dyn_kalyankjil_ns, z 1.59, reacted); dyn_indianb_ns (rho 0.515 via dyn_kalyankjil_ns, z 1.35, reacted); dyn_pcjeweller_ns (rho 0.439 via dyn_kalyankjil_ns, z 1.89, reacted); nifty_50 (rho 0.408 via dyn_kalyankjil_ns, z 0.82, quiet); dyn_indusindbk_bo (rho 0.378 via dyn_kalyankjil_ns, z 1.98, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.58, z 1.59); dyn_indianb_ns (rho 0.515, z 1.35); dyn_pcjeweller_ns (rho 0.439, z 1.89); nifty_50 (rho 0.408, z 0.82)
- Historical analogues: 2026-01-07 (d=1.99), 2026-06-15 (d=2.01), 2025-07-02 (d=3.07)

### [RED 5.4] commodities · 3 series ↑
- wheat [COMMODITIES]: last 639.25, z20 4.08, zc 2.97, resid-z 2.34 [unexplained], 1d 4.58%, |z20|=4.08; 1y-pct=96
- corn [COMMODITIES]: last 460.25, z20 3.97, zc 6.11, resid-z 5.41 [unexplained], 1d 7.60%, |z20|=3.97
- soybeans [COMMODITIES]: last 1189.50, z20 1.97, zc 0.81, resid-z 0.89 [quiet], 1d 0.83%, |z20|=1.97
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho -0.375 via soybeans, z 1.25, reacted)
- **India receivers**: dyn_adanient_bo (rho -0.375, z 1.25)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.64] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.60, z20 1.64, zc n/a, resid-z n/a [quiet], 1d 0.25%, 52-wk extreme (pct=97); |z20|=1.64; 1y-pct=97
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z-score of 1.64, indicating a potential mean reversion. This ratio is derived from the relative performance of midcap and largecap stocks, and its extreme value may signal a reversal in the market trend. The historical analogues suggest a mixed outcome for various assets, with the S&P 500 showing a positive median return, while the high-yield OAS shows a negative median return.
- **Gap**: No gap: the nifty_midcap_100 has already reacted to the extreme midcap_largecap_ratio, with a z-score of 1.59, indicating that the Indian market has likely priced in the event
- **India take**: The Nifty Midcap 100 index, with a correlation of 0.516 with the midcap_largecap_ratio, has likely expressed this move and may be due for a correction. The Indian market may see a pullback in midcap stocks, as indicated by the high z-score of the nifty_midcap_100
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.54, z 2.03); dyn_kalyankjil_ns (rho 0.384, z 4.87); dyn_indianb_ns (rho 0.361, z 0.37); dyn_swiggy_ns (rho 0.359, z 1.23)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 3.9] bovespa ↑
- bovespa [INDICES]: last 177680.62, z20 3.90, zc 3.11, resid-z 3.19 [unexplained], 1d 2.86%, |z20|=3.90
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-08-13 (z-distance 0.73).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.548 vs bovespa, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.543 vs bovespa, historically leads by 2d
- Historical analogues: 2024-08-13 (d=0.73), 2025-08-12 (d=0.92), 2025-01-30 (d=0.96)

### [RED 3.82] dyn_meta ↑
- dyn_meta [EQUITIES]: last 669.31, z20 3.82, zc 2.00, resid-z 1.39 [moved], 1d 5.99%, |z20|=3.82
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho 0.413 via dyn_meta, z 1.35, reacted); dyn_swiggy_ns (rho 0.393 via dyn_meta, z 2.06, reacted); nifty_midcap_100 (rho 0.391 via dyn_meta, z 1.59, reacted)
- **India receivers**: dyn_indianb_ns (rho 0.413, z 1.35); dyn_swiggy_ns (rho 0.393, z 2.06); nifty_midcap_100 (rho 0.391, z 1.59)
- Source: Meta’s stock roars back to life as it notches its best week in years — MarketWatch Top, 2026-07-10. https://www.marketwatch.com/story/metas-stock-roars-back-to-life-as-it-heads-for-its-best-week-in-years-0ff0fa7d?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [AMBER 3.81] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 68.47, z20 0.81, zc n/a, resid-z n/a [quiet], 1d 0.09%, GSR<75 (extreme low)
- **Mechanism**: The gold-silver ratio has increased, which may propagate through the commodities market, affecting prices of correlated instruments such as COMEX copper, silver, and gold. This move could be driven by changes in industrial demand or investor sentiment. The historically leading relationships between these instruments and the gold-silver ratio suggest potential follow-through moves.
- **Gap**: No gap: The correlated instruments have not moved significantly yet, and the historical analogues do not show a consistent pattern of price movement after a similar increase in the gold-silver ratio.
- **India take**: Indian investors can express this view through instruments such as MCX Copper, MCX Silver, and MCX Gold, which are likely to be affected by the movement in COMEX copper, silver, and gold. However, these instruments have not reacted significantly yet.
- Watch next: comex_copper (down) — not yet - watch; Historical lead of 3 days
- Watch next: comex_silver (down) — not yet - watch; High negative correlation
- Watch next: comex_gold (down) — not yet - watch; Historical lead of 4 days
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 3.64] sofr ↓
- sofr [RATES]: last 3.53, z20 -3.64, zc -1.15, resid-z -2.14 [unexplained], 1d -1.40%, |z20|=3.64; 1y-pct=1
- **Mechanism**: sofr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-06 (d=0.0), 2025-04-17 (d=0.0)

### [AMBER 3.49] rates · 4 series ↑
- tips_10y_real [RATES]: last 2.31, z20 1.83, zc 0.00, resid-z 0.32 [quiet], 1d 0.00%, |z20|=1.83; 1y-pct=99
- ust_30y [RATES]: last 5.05, z20 1.68, zc -0.26, resid-z -0.05 [quiet], 1d -0.20%, |z20|=1.68; 1y-pct=96
- ust_10y [RATES]: last 4.54, z20 1.29, zc -0.43, resid-z -0.16 [quiet], 1d -0.44%, 1y-pct=95
- ust_2y [RATES]: last 4.16, z20 0.50, zc -0.91, resid-z -0.90 [quiet], 1d -1.19%, 1y-pct=96
- **Mechanism**: The recent rise in US Treasury yields has been driven by a sharp selloff, but a strong auction of 30-year government bonds and stable economic data have led to a rebound in bond prices, causing yields to ease. This move is likely to propagate through the fixed income markets. The Indian government bond market has already reacted, with the 10-year bond yield falling 3.8 basis points to 6.7139% on Friday.
- **Gap**: No gap: the Indian 10-year bond yield has already fallen in response to the easing of US Treasury yields, indicating that the market has priced in the event.
- **India take**: The Indian 10-year bond yield, as represented by the 6.94% 2036 bond, has reacted to the easing of US Treasury yields, falling 3.8 basis points to 6.7139%. The India 10-year government bond yield, as a transmission candidate, is likely to track this move.
- Watch next: tips_10y_real (down) — already moved; 10-year real yield has fallen

## Watchlist (below surfacing floor)
natgas ↓ (3.48), cross-asset · 4 series ↑ (3.35), cross-asset · 2 series ↑ (2.82), brent_wti_spread ↑ (2.3), dyn_qessf ↓ (2.09), dyn_swiggy_ns ↑ (2.06), dyn_atherenerg_ns ↑ (1.89), dyn_cupid_ns ↑ (1.67), dyn_adanient_bo ↑ (1.25), dyn_inoxindia_ns ↑ (1.23), usd_cny ↓ (1.06), eur_usd ↓ (0.42)

## India macro
- nifty_50: 24208.5996 (1d 0.01%, z20 0.86, flag none)
- nifty_midcap_100: 63062.3516 (1d 0.04%, z20 2.03, flag amber)
- usd_inr: 95.3250 (1d -0.07%, z20 0.73, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6035 (1d 0.25%, z20 1.64, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-1d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 34.2 — "Broker’s call: Indian Bank (Buy)"
- COIN (Coinbase Global, Inc.) score 28.2 — "Global Emissions Hit Another Record High Despite Clean Energy Boom"
- HDB (HDFC Bank Limited) score 24.7 — "Broker’s call: Indian Bank (Buy)"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 23.6 — "Broker’s call: Indian Bank (Buy)"
- INDIANB.NS (INDIAN BANK) score 19.4 — "Broker’s call: Indian Bank (Buy)"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 13.1 — "Global Emissions Hit Another Record High Despite Clean Energy Boom"
- SKHYV (SK hynix Inc. American Deposit) score 12.5 — "SK HYNIX VOLATILITY GOES BOTH WAYS SK Hynix plunged a record 15%, dragging the Kospi down "
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 8.1 — "47% rally in 4 days! Kalyan Jewellers shares rise another 10%. Should you book profit?"
- CHKP (Check Point Software Technolog) score 7.8 — "Kusumgar IPO allotment to be finalised today. Here's GMP, how to check status"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.7 — "Q1 surprise sends jewellery stocks shining 40% in a month. Will the surge last in next qua"
- BOND (PIMCO Active Bond Exchange-Tra) score 7.5 — "India bonds fall as oil spike, Treasury rout weigh"
- VT (Vanguard Total World Stock Ind) score 5.8 — "Masdar Secures $5.1 Billion for World’s Largest Solar-and-Battery Project"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 5.6 — "HCL Tech Q1 Results 2026: PAT jumps 20%, revenue rises 14%; board declares  ₹12 interim di"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.1 — "FRANCE'S MACRON: UKRAINE HAS AGREED TO BUY SAMP-T AIR DEFENCE SYSTEM"
- META (Meta) score 4.4 — "Meta and Amazon are leading a trillion-dollar Big Tech spending spree"
- MU (Micron Technology, Inc.) score 3.9 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- SWIGGY.NS (SWIGGY LIMITED) score 3.8 — "Swiggy shares slide over 2% after FSSAI issues 9 notices over consumer complaints"
- MS (Morgan Stanley) score 3.5 — "MORGAN STANLEY EXPECTS US HYPERSCALER CAPEX TO REACH $1.2 TRLN BY 2027 MORGAN STANLEY EXPE"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 3.1 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 2.9 — "Vedanta Aluminium, Adani Power, 4 other stocks with up to 24% upside. Do you own any?"
- CUPID.NS (CUPID LIMITED) score 2.7 — "Cupid shares fall 2% after 131% rally in 3 months; Stock reclassified to BSE Group ‘A’"
- JEF (Jefferies Financial Group Inc.) score 2.6 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.5 — "GE Vernova, Atlanta Electricals among top beneficiaries of India's transmission expansion"
- GS (Goldman Sachs Group, Inc. (The) score 2.3 — "Goldman Sachs pegs Nifty target at 26,500 by June 2027; lists 15 stocks from key themes"
- MCAP (MCAP Inc.) score 2.3 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- JUSTDIAL.BO (JUST DIAL LTD.) score 1.8 — "Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.7 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- BLK (BlackRock, Inc.) score 1.4 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.4 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 0.9 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 0.9 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 0.8 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.7 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
- WULF (TeraWulf Inc.) score 0.6 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"

---
## Appendix — how every statistic in this brief is computed

**z20 (primary z-score).** For a series with daily observations x:
`z20 = (x_today − mean(x_prev20)) / std(x_prev20)`
where `x_prev20` is the 20 most recent observations STRICTLY BEFORE today
(the window excludes today, so today's move is measured against yesterday's
baseline) and std is the population standard deviation (ddof=0). Computed on
LEVELS, not returns. `z60` is identical with a 60-observation window.
A series needs the full prior window; otherwise z is n/a.

**1-year percentile (pct_1y).** Over the trailing window of up to 252
observations INCLUDING today (n = actual observations available, min 20):
`pct_1y = 100 × (count of window values strictly below today) / n`.
0 = lowest of the year, 100 = highest. (The Patterns query engine uses a
rank-based variant that treats ties by average rank — equivalent in
practice.)

**1d% / 5d%.** Simple percent change vs the observation 1 (resp. 5) trading
observations ago: `100 × (x_today/x_prev − 1)`. Reported as n/a when the
prior value is ~0 (zero-crossing spreads like 2s10s).

**Flag thresholds.**
- amber: |z20| ≥ 1.5 (backbone) or ≥ 2.0 (news-admitted names), OR pct_1y ≤5
  or ≥95, OR a named framework trigger (e.g. WTI/Brent 1-session ≥1.5%,
  TIPS 1-day ≥5bp, VIX 1-session ≥15%, gold/silver ratio >85 or <75).
- red: |z20| ≥ 2.5, OR framework trigger with |z20| above the amber bar.
- Series with <30 observations never flag (sparse guard).
- Data hygiene: an isolated print deviating >15% from BOTH neighbours in the
  same direction (spike-and-revert) is replaced by the neighbour mean before
  any statistic is computed (VIX exempt — that pattern is its signal).

**Events.** Flagged series are clustered when their 60-day daily-return
correlation satisfies |ρ| ≥ 0.65 AND today's moves are consistent with ρ's
sign. Event score = (strongest member's engine score, i.e. |z20| + 3 if a
framework trigger fired) + 1.2·ln(n_members) + 2 if corroborating news is
attached. Events surface only above a floor of 3.2, max 8 cards; the rest
are suppressed to the watchlist.

**Correlations / lead-lag (rho in "India receivers" and "watch next").**
Pearson correlation of daily percent-change returns over trailing 60d
(rho60) and 252d (rho252) windows; pairs kept at |ρ| ≥ 0.35. "Leads by k
days" means corr(return_A at t−k, return_B at t) over the 252d window is
the strongest lagged relationship, k ∈ 1..5. A "receiver/laggard" is a
correlated instrument whose own |z20| < 1.0 (it has not yet moved).

**Historical analogues.** Nearest past dates by Euclidean distance between
today's member z20 vector and every historical date's vector (last 10
sessions excluded, episodes ≥5 sessions apart). Aftermath stats are the
median/hit-rate of forward percent changes +5 and +20 observations after
each analogue date.

**zc (vol-conditional return z).** `zc = r_today / sigma_EWMA(t|t-1)` where
sigma is the RiskMetrics EWMA (lambda 0.94) of squared returns strictly
before today; GARCH(1,1) refines the latest sigma when the fit converges.
This is the "unusual" gate: it sees a 2-sigma move in a quiet regime that
the 20-day levels-z drowns. Daily series only.

**resid_z (unexplained z).** Rolling 60d OLS of the instrument's returns on
its configured factor block (betas from the window ending t-1 applied to
today's factor returns). `resid = actual − predicted`; resid_z = resid vs
the std of the prior 60 residuals. Large raw move + small resid_z = PRICED
(factors explain it); large resid_z = genuinely unexplained. Move labels:
priced / unexplained / moved / quiet per these thresholds (1.5/1.0, r2>=.25).

**Assumption statuses.** Each standing prior (safe-haven gold, oil->INR,
etc.) is scored live: VALID = 20d AND 60d return corr clear (|corr|>=0.25)
in the expected sign; INVERTED = clearly wrong sign on 20d or the contra
check fires (e.g. gold trading WITH nifty); WEAK = neither clear;
INSUFFICIENT_DATA = too few paired observations. Change-point dates mark
the last shift of the 60d rolling correlation (PELT/rbf). Co-occurrence
escalation and thesis mechanisms are gated on these statuses.

**Regime.** Rules-based risk-on/off score = mean(vol 1y-percentile,
share of equity indices below 50DMA, sign-scaled 20d equity-rates corr);
RISK_OFF >= 0.6, RISK_ON <= 0.35. Markov 2-state switching-variance
P(high-vol) reported as corroborating evidence, never as a gate.

**Data.** Daily closes: yfinance (indices/FX/commodities/equities/crypto)
and FRED (rates/credit/India macro), ~2 years of history, refreshed every
2h on weekdays with an intraday provisional last price that the official
close later overwrites. All statistics use this daily series — intraday
prints enter as today's provisional observation.

---
## How to use this brief (instruction to the assistant)
You are helping draft a macro article for an audience of Indian market
practitioners. Work ONLY from the data above — never invent numbers.
Priorities: (1) the event-to-price gap — what the news implies that price
has not yet reflected; (2) the transmission chain into Indian instruments,
using the INDIA lines and laggards; (3) historical precedent where given.
A sceptical 'no gap here' is a valid conclusion. Cite specifics (levels,
z-scores, dates) from the brief. The owner's hypotheses and journal intents
show what they are already thinking — engage with them directly.