# Transmission Layer — board brief · 2026-10-08 18:50Z

data as of **2026-10-08** · 97 series · 11 red / 40 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.708, 4d in regime; vol-pct 0.711, breadth-off 0.706, Markov P(high-vol) 0.018)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.41, contra nifty_50 corr20=0.07, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.18, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.11, corr60 0.12, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.29, corr60 -0.11, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.33, corr60 -0.27, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.53, corr60 0.19, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1141) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2171) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.83] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 70.02, z20 2.00, zc n/a, resid-z n/a [quiet], 1d 1.28%, GSR<75 (extreme low); |z20|=2.00
- comex_silver [COMMODITIES]: last 59.25, z20 -1.74, zc -0.61, resid-z -0.98 [quiet], 1d -1.08%, |z20|=1.74
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.367 via gold_silver_ratio, z -2.07, reacted)
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.559 vs comex_silver
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.515 vs gold_silver_ratio
- **India receivers**: midcap_largecap_ratio (rho -0.367, z -2.07)
- Source: Gold prices near Rs 1.5 lakh/10 grams; silver rises as dollar eases from multi-month high. What lies ahead? — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-near-rs-1-5-lakh/10-grams-silver-rises-as-dollar-eases-from-multi-month-high-what-lies-ahead/articleshow/134779724.cms
- Source: Gold prices dip Rs 1,500/10 grams; silver down Rs 1,600/kg ahead of Fed minutes. Key levels to track — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-dip-rs-1500/10-grams-silver-down-rs-1600/kg-ahead-of-fed-minutes-key-levels-to-track/articleshow/134755973.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.51] usd_inr ↑
- usd_inr [FX]: last 96.77, z20 2.51, zc 0.80, resid-z 0.61 [quiet], 1d 0.41%, 20d range extreme; |z20|=2.51; 1y-pct=99; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.413 via usd_inr, z -0.44, quiet); dyn_karurvysya_ns (rho -0.378 via usd_inr, z 0.57, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.413, z -0.44); dyn_karurvysya_ns (rho -0.378, z 0.57)
- Source: RBI intervention halts rupee's slide to record low, risks linger — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/forex/rbi-intervention-halts-rupees-slide-to-record-low-risks-linger/articleshow/134788012.cms
- Source: Rupee falls 13 paise to close at 96.88 against US dollar — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/forex/rupee-falls-13-paise-to-close-at-9688-against-us-dollar/article71559337.ece
- Source: INR vs USD: Rupee near 97/dollar; how TCS, Sun Pharma, Tata Steel, SRF may gain from weaker currency? Experts explain — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/inr-vs-usd-rupee-near-97-dollar-how-tcs-sun-pharma-tata-steel-srf-may-gain-from-weaker-currency-experts-explain-11791449213491.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 7.48] cross-asset · 6 series ↑
- ust_30y [RATES]: last 5.64, z20 1.56, zc -0.44, resid-z -0.33 [quiet], 1d -0.35%, |z20|=1.56; 1y-pct=99
- ust_10y [RATES]: last 5.27, z20 1.26, zc -0.72, resid-z -0.60 [quiet], 1d -0.75%, 1y-pct=98
- tips_10y_real [RATES]: last 2.91, z20 1.18, zc -0.69, resid-z -0.53 [quiet], 1d -1.36%, 1y-pct=98
- dyn_bond [EQUITIES]: last 86.89, z20 -0.99, zc 1.03, resid-z 0.02 [quiet], 1d 0.37%, 1y-pct=2
- ust_2y [RATES]: last 4.79, z20 0.41, zc -0.77, resid-z -0.49 [quiet], 1d -1.03%, 1y-pct=96
- brent [COMMODITIES]: last 104.44, z20 0.33, zc 2.33, resid-z 0.63 [priced], 1d 4.23%, 1-session move +4.23% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.51 vs ust_30y, historically leads by 3d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.557 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.551 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.531 vs ust_30y
- Watch next: sp500 (inverse) — not yet - watch; rho -0.509 vs ust_30y
- Source: Wall St turns lower as crude spikes, chip stocks weigh — Mint Markets, 2026-10-08. https://www.livemint.com/market/wall-st-turns-lower-as-crude-spikes-chip-stocks-weigh-11791485275522.html
- Source: Bond yields fell, as the Treasury market passed a crucial test of investor confidence — MarketWatch Top, 2026-10-08. https://www.marketwatch.com/story/the-treasury-market-is-facing-a-crucial-vote-of-investor-confidence-31fa8d41?mod=mw_rss_topstories
- Source: Oil Prices Plunge as Trump Rules Out Iran Strikes Before Midterms — OilPrice, 2026-10-08. https://oilprice.com/Energy/Oil-Prices/Oil-Prices-Plunge-as-Trump-Rules-Out-Iran-Strikes-Before-Midterms.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.35), 2026-05-14 (d=0.69)

### [AMBER 6.31] cross-asset · 5 series ↓
- nifty_50 [INDICES]: last 22231.80, z20 -2.38, zc -2.29, resid-z -2.36 [unexplained], 1d -1.64%, |z20|=2.38; 1y-pct=0
- nifty_fmcg [INDICES]: last 43898.40, z20 -2.35, zc -2.25, resid-z -0.82 [priced], 1d -2.02%, |z20|=2.35; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 57880.45, z20 -2.34, zc -2.65, resid-z -2.15 [unexplained], 1d -2.52%, |z20|=2.34
- india_vix [INDICES]: last 15.24, z20 2.19, zc 1.64, resid-z n/a [moved], 1d 9.74%, |z20|=2.19
- dyn_policybzr_ns [EQUITIES]: last 996.00, z20 -1.18, zc -1.16, resid-z 0.61 [quiet], 1d -4.23%, 1y-pct=1
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.64 via nifty_midcap_100, z -2.07, reacted); nifty_metal (rho 0.623 via nifty_midcap_100, z -3.61, reacted); dyn_jiofin_bo (rho 0.589 via nifty_50, z -1.94, reacted); dyn_indusindbk_bo (rho 0.546 via nifty_midcap_100, z -1.77, reacted); dyn_bajfinance_ns (rho -0.539 via india_vix, z -1.3, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.64, z -2.07); nifty_metal (rho 0.623, z -3.61); dyn_jiofin_bo (rho 0.589, z -1.94); dyn_indusindbk_bo (rho 0.546, z -1.77)
- Source: Nifty hits 52-week low as crude, FII selling weigh — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-hits-52-week-low-as-crude-fii-selling-weigh/article71559983.ece
- Source: Nifty hits intra-day high on open for the sixth time in 2026 — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-hits-intra-day-high-on-open-for-the-sixth-time-in-2026/article71560509.ece
- Source: Nifty sinks to an 18-month low as rate fears bite — Mint Markets, 2026-10-08. https://www.livemint.com/market/nifty-50-performance-in-2026-fii-fpi-selling-inflation-rbi-nse-crude-oil-11791461972358.html
- Historical analogues: 2025-07-21 (d=0.6), 2025-07-14 (d=0.65), 2025-12-30 (d=1.12)

### [RED 5.85] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2595.00, z20 -3.85, zc -2.05, resid-z -1.99 [unexplained], 1d -5.43%, |z20|=3.85
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.539 via dyn_adanient_bo, z -3.61, reacted); nifty_midcap_100 (rho 0.387 via dyn_adanient_bo, z -2.34, reacted); nifty_50 (rho 0.374 via dyn_adanient_bo, z -2.38, reacted)
- **India receivers**: nifty_metal (rho 0.539, z -3.61); nifty_midcap_100 (rho 0.387, z -2.34); nifty_50 (rho 0.374, z -2.38)
- Source: Adani Group's Group CFO Jugeshinder Robbie Singh on recent market volatility: 'Mood is ephemeral; stone is eternal' — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/adani-groups-group-cfo-jugeshinder-robbie-singh-on-recent-market-volatility-mood-is-ephemeral-stone-is-eternal-11791471088722.html
- Source: Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-infosys-tech-mahindra-adani-ent-itc-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134788835.cms
- Source: Adani Group stocks tumble as market rout deepens; Adani Green, Adani Ent, others tank up to 10% — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/stocks/news/adani-group-stocks-tumble-as-market-rout-deepens-adani-green-adani-ent-others-tank-up-to-10/articleshow/134786010.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 5.72] wti ↓
- wti [COMMODITIES]: last 91.55, z20 -0.72, zc 1.58, resid-z 0.58 [priced], 1d 3.70%, 1-session move +3.70% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.909 vs wti
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.594 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.586 vs wti
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.534 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.533 vs wti
- Source: Wall St turns lower as crude spikes, chip stocks weigh — Mint Markets, 2026-10-08. https://www.livemint.com/market/wall-st-turns-lower-as-crude-spikes-chip-stocks-weigh-11791485275522.html
- Source: Oil Prices Plunge as Trump Rules Out Iran Strikes Before Midterms — OilPrice, 2026-10-08. https://oilprice.com/Energy/Oil-Prices/Oil-Prices-Plunge-as-Trump-Rules-Out-Iran-Strikes-Before-Midterms.html
- Source: Nifty hits 52-week low as crude, FII selling weigh — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-hits-52-week-low-as-crude-fii-selling-weigh/article71559983.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.44] dyn_muthootfin_ns ↓
- dyn_muthootfin_ns [EQUITIES]: last 2559.60, z20 -3.44, zc -2.07, resid-z -1.06 [moved], 1d -3.57%, |z20|=3.44; 1y-pct=0
- **Mechanism**: dyn_muthootfin_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.478 via dyn_muthootfin_ns, z -2.34, reacted); nifty_50 (rho 0.448 via dyn_muthootfin_ns, z -2.38, reacted); nifty_metal (rho 0.437 via dyn_muthootfin_ns, z -3.61, reacted); dyn_bajfinance_ns (rho 0.386 via dyn_muthootfin_ns, z -1.3, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.478, z -2.34); nifty_50 (rho 0.448, z -2.38); nifty_metal (rho 0.437, z -3.61); dyn_bajfinance_ns (rho 0.386, z -1.3)
- Source: Muthoot Microfin AUM crosses ₹15,300 crore, cost of funds enters single digits — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/stock-markets/muthoot-microfin-aum-crosses-15300-crore-cost-of-funds-enters-single-digits/article71559184.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 5.07] midcap_largecap_ratio ↓
- midcap_largecap_ratio [DERIVED]: last 2.60, z20 -2.07, zc n/a, resid-z n/a [quiet], 1d -0.89%, break below 100-DMA; |z20|=2.07
- **Mechanism**: midcap_largecap_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.64 via midcap_largecap_ratio, z -2.34, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.64, z -2.34)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
indices · 4 series ↓ (4.84), dyn_ohi ↓ (4.33), shanghai_comp ↓ (4.31), dyn_4417_t ↑ (4.3), cross-asset · 3 series ↑ (4.29), dyn_coalindia_ns ↓ (4.23), dyn_techm_ns ↓ (4.13), dyn_jiofin_bo ↓ (3.94), eur_usd ↓ (3.72), nifty_metal ↓ (3.61), dyn_hdb ↓ (3.29), dyn_justdial_bo ↓ (2.97)

## India macro
- nifty_50: 22231.8008 (1d -1.64%, z20 -2.38, flag amber)
- nifty_midcap_100: 57880.4492 (1d -2.52%, z20 -2.34, flag amber)
- usd_inr: 96.7700 (1d 0.41%, z20 2.51, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6035 (1d -0.89%, z20 -2.07, flag red)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 90.1 — "India at an inflection point in private credit space: What is creating the opportunity?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.0 — "India at an inflection point in private credit space: What is creating the opportunity?"
- INDIANB.NS (INDIAN BANK) score 89.3 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.2 — "India at an inflection point in private credit space: What is creating the opportunity?"
- BAC (Bank of America Corporation) score 74.9 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- HDB (HDFC Bank Limited) score 71.4 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- IDBI.NS (IDBI BANK LIMITED) score 68.3 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 68.3 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 68.3 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- COIN (Coinbase Global, Inc.) score 60.7 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- OHI (Omega Healthcare Investors, In) score 47.4 — "Power demand cycle shifting to value; Anand Rathi suggests what investors should do with C"
- BOND (PIMCO Active Bond Exchange-Tra) score 46.9 — "Bond yields fell, as the Treasury market passed a crucial test of investor confidence"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.0 — "Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Se"
- TGT (Target Corporation) score 40.1 — "Alakh Pandey-led Physicswallah shares up 42% in 6 months; Motilal Oswal sees further upsid"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.2 — "Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Se"
- TECH (Bio-Techne Corp) score 39.2 — "Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Se"
- CHKP (Check Point Software Technolog) score 33.4 — "TCS dividend payout decoded: Check 3-year dividends, yield and stock returns of IT bellwet"
- LTH (Life Time Group Holdings, Inc.) score 28.4 — "Why a longtime skeptic of Palantir’s stock is finally saying it’s time to buy"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.4 — "AMFI Rejig: Lenskart, LG Electronics, Siemens Energy among 6 stocks set for largecap upgra"
- SEPN (Septerna, Inc.) score 24.9 — "Meeting of 9-10 September 2026"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 23.9 — "Nifty falls 15% YTD: Top experts reveal stock market outlook, their preferred sectors now"
- 301077.SZ (CHINASTARS) score 19.1 — "CHINA STEPS UP ECONOMIC TALKS WITH UK AND EU Chinese Vice Premier He Lifeng called for str"
- JIOFIN.BO (Jio Financial Services Limited) score 15.3 — "CHINA STEPS UP ECONOMIC TALKS WITH UK AND EU Chinese Vice Premier He Lifeng called for str"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.8 — "TCS share price expectations for tomorrow: How Q2 results 2026 will impact Tata stock on F"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.8 — "TCS share price expectations for tomorrow: How Q2 results 2026 will impact Tata stock on F"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.8 — "Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Se"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.3 — "FRENCH DEFAULT RISK REMAINS NEAR MULTI-YEAR HIGHS The cost of insuring French government d"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.6 — "FRENCH DEFAULT RISK REMAINS NEAR MULTI-YEAR HIGHS The cost of insuring French government d"
- JEF (Jefferies Financial Group Inc.) score 12.2 — "RBI rate hike done. Now what’s ahead for bank stocks? Jefferies, other brokerages weigh in"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.0 — "CHINA STEPS UP ECONOMIC TALKS WITH UK AND EU Chinese Vice Premier He Lifeng called for str"
- META (Meta) score 9.6 — "US President Donald Trump buys $1 million-plus stakes in Meta, Microsoft, McDonald’s; adds"
- VT (Vanguard Total World Stock Ind) score 8.5 — "TRUMP: WE SHOULD HAVE THE LOWEST INTEREST RATE IN THE WORLD"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.5 — "CHINA STEPS UP ECONOMIC TALKS WITH UK AND EU Chinese Vice Premier He Lifeng called for str"
- NVDA (NVIDIA Corporation) score 7.1 — "Microsoft and Nvidia are teaming up on a supercharged AI laptop"
- RS (Reliance, Inc.) score 6.1 — "Reliance Drives India’s Venezuelan Oil Imports to Seven-Year High"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.8 — "UK Retailers Push to Cut Green Levies as Power Bills Top £440 Million"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "Goldman Sachs sees 26% return for Asian equities, bets big on tech earnings surge"
- POLICYBZR.NS (PB FINTECH LIMITED) score 4.1 — "Pine Labs, CAMS, Moneyview, other fintech stocks rally up to 11% after RBI MPC move. Here’"
- DELL (Dell Technologies Inc.) score 1.0 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"

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