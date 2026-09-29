# Transmission Layer — board brief · 2026-09-29 10:39Z

data as of **2026-09-29** · 97 series · 14 red / 31 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.707, 4d in regime; vol-pct 0.581, breadth-off 0.833, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.57, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.05, corr60 0.14, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.1, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.06, corr60 -0.1, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.15, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.44, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0013742758758317208)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.5** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2378) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.6] hy_oas ↑
- hy_oas [RATES]: last 2.93, z20 5.60, zc 2.51, resid-z 4.08 [unexplained], 1d 4.64%, |z20|=5.60
- **Mechanism**: hy_oas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S. high-yield debt issuance is straining investor demand, pushing junk-bond spreads to their widest since April. September issuance has reached $38.5 billion, while CCC spreads have surged to their highest since — DeItaone, 2026-09-28. https://t.me/walter_bloomberg/36264
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-25 (d=0.0), 2025-07-31 (d=0.01)

### [RED 7.41] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4180.20, z20 -2.62, zc 0.69, resid-z -0.30 [quiet], 1d 0.71%, |z20|=2.62; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.13, z20 -2.52, zc -0.07, resid-z -0.97 [quiet], 1d -0.15%, |z20|=2.52; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.38, z20 1.10, zc n/a, resid-z n/a [quiet], 1d 0.86%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.597 vs comex_silver, historically leads by 1d
- Source: Gold traders to protest on Oct 15 against MDR on UPI dealings — BusinessLine Mkts, 2026-09-29. https://www.thehindubusinessline.com/markets/gold/gold-traders-to-protest-on-oct-15-against-mdr-on-upi-dealings/article71523296.ece
- Source: Gold edges up from 7-week low; all eyes on West Asia, US economic data — BusinessLine Mkts, 2026-09-29. https://www.thehindubusinessline.com/markets/gold/gold-edges-up-from-7-week-low-all-eyes-on-west-asia-us-economic-data/article71522988.ece
- Source: Today’s Gold Rate, September 29: Check Gold Rates in Delhi, Mumbai, Chennai — BusinessLine Mkts, 2026-09-29. https://www.thehindubusinessline.com/markets/gold/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-september-29-2026/article71523070.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.75] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.49, z20 2.82, zc 0.44, resid-z 0.60 [quiet], 1d 0.37%, |z20|=2.82; 1y-pct=100
- dyn_bond [EQUITIES]: last 87.27, z20 -2.28, zc 0.33, resid-z 0.13 [quiet], 1d -0.48%, |z20|=2.28; 1y-pct=0
- tips_10y_real [RATES]: last 2.83, z20 2.13, zc -0.31, resid-z -0.18 [quiet], 1d -0.70%, |z20|=2.13; 1y-pct=99
- ust_10y [RATES]: last 5.17, z20 2.05, zc -0.18, resid-z -0.02 [quiet], 1d -0.19%, |z20|=2.05; 1y-pct=99
- ust_2y [RATES]: last 4.81, z20 1.31, zc -0.92, resid-z -0.78 [quiet], 1d -1.23%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.517 vs ust_30y, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.6 vs dyn_bond
- Watch next: sp500 (co-move) — not yet - watch; rho 0.548 vs dyn_bond
- Source: US bond yields hit 19-year high! What's driving the surge and why Nifty, Sensex are feeling the heat? Experts decode — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/us-bond-yields-hit-19-year-high-whats-driving-the-surge-and-why-nifty-sensex-are-feeling-the-heat-experts-decode-11790673444471.html
- Source: US bond market: Why AI blowout holds key for the Indian stock market? — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/us-bond-market-why-is-ai-blowout-holds-key-for-the-indian-stock-market-11790669210878.html
- Source: Nifty logs weakest expiry since March amid surging bond yields — Mint Markets, 2026-09-29. https://www.livemint.com/market/nifty-expiry-us-bond-yields-crude-oil-prices-11790662749575.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.42] cross-asset · 4 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1081.00, z20 -2.76, zc -0.35, resid-z -1.28 [quiet], 1d -6.11%, |z20|=2.76; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 59321.25, z20 -2.74, zc -1.00, resid-z -1.53 [unexplained], 1d -0.99%, |z20|=2.74
- nifty_50 [INDICES]: last 22716.20, z20 -2.21, zc -0.41, resid-z 0.36 [quiet], 1d -0.28%, |z20|=2.21; 1y-pct=2
- india_vix [INDICES]: last 13.34, z20 1.76, zc -0.37, resid-z n/a [quiet], 1d -2.22%, |z20|=1.76
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.605 via nifty_midcap_100, z -2.58, reacted); dyn_jiofin_bo (rho 0.583 via nifty_50, z -2.82, reacted); nifty_fmcg (rho 0.557 via nifty_50, z -2.17, reacted); dyn_techm_ns (rho 0.494 via nifty_50, z -1.65, reacted); dyn_indusindbk_bo (rho 0.482 via nifty_midcap_100, z -2.77, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.605, z -2.58); dyn_jiofin_bo (rho 0.583, z -2.82); nifty_fmcg (rho 0.557, z -2.17); dyn_techm_ns (rho 0.494, z -1.65)
- Source: PB Fintech shares extend losses for fourth straight session; loses 41% in four days — what investors should do? — Mint Markets, 2026-09-29. https://www.livemint.com/market/pb-fintech-shares-extend-losses-for-fourth-straight-session-loses-41-in-four-days-what-investors-should-do-11790654948645.html
- Source: Stock market prediction for tomorrow: Sensex, Nifty outlook for Wednesday | Kospi, Taiwan cues to watch | 30 Sept 2026 — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/stock-market-prediction-for-tomorrow-sensex-nifty-outlook-for-wednesday-kospi-taiwan-cues-to-watch-30-sept-2026-11790675991769.html
- Source: Nifty 50 is breaking long-held supports as selloff deepens — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/nifty-50-is-breaking-long-held-supports-as-selloff-deepens-11790674933256.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 6.01] brent ↓
- brent [COMMODITIES]: last 97.50, z20 -1.01, zc -2.70, resid-z -0.77 [priced], 1d -7.39%, 1-session move -7.39% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.883 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.58 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.538 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.601 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.55 vs brent
- Source: The road ahead: How to invest amid macro uncertainty as oil on boil, Indian economy under heat of weak monsoon too? — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/the-road-ahead-how-to-invest-amid-macro-uncertainty-as-oil-on-boil-indian-economy-under-heat-of-weak-monsoon-too-11790597800951.html
- Source: Crude oil shock and higher yields: Why Indian stock markets may remain volatile in near term - where should you invest? — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/crude-oil-shock-and-higher-yields-why-indian-stock-markets-may-remain-volatile-in-near-term-where-should-you-invest-11790665625517.html
- Source: Sensex, Nifty rebound from near six-month lows amid crude shock — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/sensex-nifty-stock-market-today-crude-oil-price-11790661886513.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [RED 4.88] dxy ↑
- dxy [FX]: last 101.43, z20 1.88, zc 0.66, resid-z -0.82 [quiet], 1d 0.22%, 20d range extreme; |z20|=1.88; 1y-pct=98
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [RED 4.84] fx · 4 series ↓
- usd_mxn [FX]: last 17.96, z20 3.18, zc 1.64, resid-z 2.56 [unexplained], 1d 1.21%, |z20|=3.18
- aud_usd [FX]: last 0.70, z20 -2.26, zc -0.37, resid-z -0.67 [quiet], 1d -0.23%, |z20|=2.26
- eur_usd [FX]: last 1.13, z20 -2.12, zc -0.90, resid-z -0.69 [quiet], 1d -0.30%, |z20|=2.12; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -1.85, zc 0.06, resid-z 0.12 [quiet], 1d 0.02%, |z20|=1.85
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.502 via usd_mxn, z -2.76, reacted); dyn_icicigi_bo (rho -0.483 via gbp_usd, z 0.23, quiet); dyn_muthootfin_ns (rho 0.463 via aud_usd, z -1.75, reacted); dyn_inoxindia_ns (rho 0.411 via aud_usd, z -0.81, quiet); nifty_midcap_100 (rho -0.389 via usd_mxn, z -2.74, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.55 vs aud_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.354 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_policybzr_ns (rho -0.502, z -2.76); dyn_icicigi_bo (rho -0.483, z 0.23); dyn_muthootfin_ns (rho 0.463, z -1.75); dyn_inoxindia_ns (rho 0.411, z -0.81)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 4.82] dyn_jiofin_bo ↓
- dyn_jiofin_bo [EQUITIES]: last 217.90, z20 -2.82, zc -0.81, resid-z -0.17 [quiet], 1d -1.07%, |z20|=2.82; 1y-pct=0
- **Mechanism**: dyn_jiofin_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.583 via dyn_jiofin_bo, z -2.21, reacted); nifty_midcap_100 (rho 0.431 via dyn_jiofin_bo, z -2.74, reacted)
- **India receivers**: nifty_50 (rho 0.583, z -2.21); nifty_midcap_100 (rho 0.431, z -2.74)
- Source: 26% dip in YTD! Jio Financial Services shares hit 52-week low — will trend reverse? Target price, support, resistance — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/26-dip-in-ytd-jio-financial-services-shares-hit-52-week-low-will-trend-reverse-target-price-support-resistance-11790658322060.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-14 (d=0.01), 2025-08-06 (d=0.03)

## Watchlist (below surfacing floor)
dyn_chkp ↓ (4.3), shanghai_comp ↓ (4.21), dyn_havells_ns ↓ (4.02), dyn_nvda ↑ (3.3), dyn_4417_t ↑ (3.16), dyn_tech ↑ (3.1), dyn_hdb ↓ (3.04), commodities · 2 series ↓ (2.98), dyn_indusindbk_bo ↓ (2.77), dyn_indianb_ns ↓ (2.72), dyn_atherenerg_ns ↓ (2.65), usd_brl ↑ (2.59)

## India macro
- nifty_50: 22716.1992 (1d -0.28%, z20 -2.21, flag amber)
- nifty_midcap_100: 59321.2500 (1d -0.99%, z20 -2.74, flag red)
- usd_inr: 95.9800 (1d 0.20%, z20 1.03, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6114 (1d -0.71%, z20 -2.58, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 76.0 — "SRIT India, Shah Investor’s Home IPO Day 2: Check GMP, subscription status and key details"
- INOXINDIA.NS (INOX INDIA LIMITED) score 74.7 — "SRIT India, Shah Investor’s Home IPO Day 2: Check GMP, subscription status and key details"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.5 — "SRIT India, Shah Investor’s Home IPO Day 2: Check GMP, subscription status and key details"
- INDIANB.NS (INDIAN BANK) score 49.4 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- COIN (Coinbase Global, Inc.) score 49.1 — "Global Market: South Korean stocks under pressure ahead of trade data, Micron results"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.1 — "Global Market: RoboTechnik slides below IPO price in weak Hong Kong debut"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.1 — "Global Market: RoboTechnik slides below IPO price in weak Hong Kong debut"
- TECH (Bio-Techne Corp) score 39.1 — "Global Market: RoboTechnik slides below IPO price in weak Hong Kong debut"
- OHI (Omega Healthcare Investors, In) score 38.5 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- CHKP (Check Point Software Technolog) score 36.6 — "SRIT India, Shah Investor’s Home IPO Day 2: Check GMP, subscription status and key details"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.6 — "Global Market: Nikkei falls as oil surge, global bond selloff rattle markets"
- HDB (HDFC Bank Limited) score 33.0 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- BAC (Bank of America Corporation) score 31.3 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- IDBI.NS (IDBI BANK LIMITED) score 28.6 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.6 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.6 — "Nifty SIP return fails to beat even bank FD over 5 years: Is this the warning sign investo"
- SEPN (Septerna, Inc.) score 27.0 — "Stocks to Watch, Sept 29: Tata Group, Ola Electric, Anupam Rasayan, HCL Software, IRFC, NC"
- 301077.SZ (CHINASTARS) score 26.9 — "Global Market: China stocks edge up as policy support pledge lifts property shares"
- LTH (Life Time Group Holdings, Inc.) score 25.7 — "Orient Cables IPO Day 3: GMP at 27%; subscription crosses 8 times. key details inside"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.5 — "Energy security measures could offset up to 70% of Hormuz oil flows in future disruption: "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.0 — "SEBI rejects charge of minimum public shareholding violation by Adani Group companies"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.8 — "Stocks to Watch, Sept 29: Tata Group, Ola Electric, Anupam Rasayan, HCL Software, IRFC, NC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.8 — "Stocks to Watch, Sept 29: Tata Group, Ola Electric, Anupam Rasayan, HCL Software, IRFC, NC"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.5 — "Orient Cables, German Green Steel IPOs draw strong demand on last day, AceVector, Runwal f"
- POLICYBZR.NS (PB FINTECH LIMITED) score 12.3 — "PB Fintech shares suffer Rs 37,000 crore shock in 4 days but Jefferies, Bernstein see up t"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "Stocks to buy: JM Financial expects soft Q2 season for IT majors; check target prices for "
- META (Meta) score 9.9 — "Nifty Metal slips 5% in September post 29% 1 yr rally, October comeback ahead? Hindustan Z"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.8 — "Bitcoin near $83,900, Ethereum around $2,680 as crypto markets consolidate: Here is what e"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.6 — "Auto stocks: Festive demand gets a low-base boost; can earnings justify valuations?"
- GS (Goldman Sachs Group, Inc. (The) score 7.2 — "Goldman Sachs identifies 42 Indian stocks riding AI build-out"
- VT (Vanguard Total World Stock Ind) score 6.9 — "From SpaceX to Saudi Aramco: World's biggest IPOs as Anthropic's blockbuster listing looms"
- TGT (Target Corporation) score 6.5 — "Stocks to buy: JM Financial expects soft Q2 season for IT majors; check target prices for "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.8 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- NVDA (NVIDIA Corporation) score 5.4 — "Nvidia $150 billion share buyback: Should you participate post-record date announcement?"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.9 — "JAPANESE, US FINANCE CHIEFS DISCUSS YEN DEPRECIATION: KYODO"
- MS (Morgan Stanley) score 4.8 — "A month ago, this JPMorgan team urged caution on stocks. Now it’s going all in on tech."
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.8 — "ETMarkets Smart Talk| F&O STT, UPI charges and trading costs: Sandeep Neema on the hidden "
- MU (Micron Technology, Inc.) score 3.1 — "Global Market: South Korean stocks under pressure ahead of trade data, Micron results"
- VOLTAS.NS (VOLTAS LTD) score 0.6 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.4 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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