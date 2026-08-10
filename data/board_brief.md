# Transmission Layer — board brief · 2026-08-10 05:43Z

data as of **2026-08-10** · 98 series · 7 red / 33 amber · 6 events surfaced (16 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.435, 5d in regime; vol-pct 0.496, breadth-off 0.375, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.41, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.38, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.06, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.23, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.18, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.568, β -0.4371, p 0.0); driver zc -1.61 → expected 0.77%. Type hit-rate 0.827 (n=2362).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2378, p 0.0); driver zc -1.61 → expected -0.419%. Type hit-rate 0.827 (n=2362).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.366, β -0.2217, p 0.0); driver zc -1.61 → expected 0.39%. Type hit-rate 0.827 (n=2362).
- Track record · residual_reversion: hit-rate **0.495** (n=1152) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2362) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.19] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4396.00, z20 3.46, zc 0.64, resid-z 0.24 [quiet], 1d 1.27%, |z20|=3.46; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 63.97, z20 2.83, zc 0.37, resid-z -0.39 [quiet], 1d 1.02%, |z20|=2.83; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6528.94, z20 2.46, zc 0.47, resid-z 0.05 [quiet], 1d 0.41%, |z20|=2.46; 1y-pct=100
- dyn_vt [EQUITIES]: last 161.29, z20 2.41, zc 0.86, resid-z 1.02 [quiet], 1d 0.86%, |z20|=2.41; 1y-pct=100
- dyn_nvda [EQUITIES]: last 223.98, z20 2.37, zc 0.88, resid-z -0.17 [quiet], 1d 2.28%, |z20|=2.37; 1y-pct=98
- cac_40 [INDICES]: last 8724.97, z20 2.33, zc 0.38, resid-z 0.12 [quiet], 1d 0.29%, |z20|=2.33; 1y-pct=100
- russell_2000 [INDICES]: last 3033.98, z20 2.28, zc 0.86, resid-z 0.90 [quiet], 1d 1.08%, |z20|=2.28; 1y-pct=99
- dax [INDICES]: last 26354.06, z20 2.22, zc 1.05, resid-z 0.50 [quiet], 1d 0.82%, |z20|=2.22; 1y-pct=100
- sp500 [INDICES]: last 7755.61, z20 2.18, zc 0.61, resid-z -0.45 [quiet], 1d 0.59%, |z20|=2.18; 1y-pct=100
- dow_jones [INDICES]: last 54029.50, z20 1.96, zc 0.27, resid-z -0.16 [quiet], 1d 0.27%, |z20|=1.96; 1y-pct=99
- vix [INDICES]: last 14.89, z20 -1.58, zc -0.21, resid-z n/a [quiet], 1d -1.72%, |z20|=1.58
- comex_copper [COMMODITIES]: last 6.61, z20 1.40, zc 0.27, resid-z -2.12 [unexplained], 1d 0.62%, 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.71, z20 -1.11, zc n/a, resid-z n/a [quiet], 1d 0.26%, GSR<75 (extreme low)
- **Mechanism**: The recent move in gold and silver prices is largely priced in, with small resid_z values indicating that factor exposures explain most of the move. However, the VALID gold_silver_comove channel suggests that the co-movement between gold and silver will continue, potentially driving further price action in these metals.
- **Gap**: No gap: the small resid_z values for gold and silver indicate that the recent price moves are largely explained by factor exposures, leaving little room for a significant event-to-price gap
- **India take**: Indian metal equities, such as those in the nifty_metal index, have already reacted to the move in global metal prices, with a rho of 0.485 with comex_silver. Further moves in gold and silver prices may continue to drive price action in these Indian equities.
- Watch next: comex_gold (down) — already moved; resid_z is small, indicating the move is largely priced in
- Watch next: comex_silver (down) — already moved; resid_z is negative, indicating the move may be overextended
- Watch next: nifty_metal (down) — already moved; rho with comex_silver is 0.485, suggesting transmission of metal price moves to Indian metal equities
- **India receivers**: nifty_fmcg (rho -0.542, z 0.31); nifty_50 (rho 0.542, z 1.25); nifty_midcap_100 (rho 0.521, z 1.96); nifty_metal (rho 0.485, z 2.25)
- Source: Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results, Sky Gold, Dynamatic Tech, Quality Power, Anant Raj shares gain after Q1, Kaynes Tech, Ola, Oswal Pumps, Jamna Auto, Apollo Micro shares in red — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Source: Gold eases from seven-week peak, US inflation data looms — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/gold/gold-eases-from-seven-week-peak-us-inflation-data-looms/article71327016.ece
- Source: Silver futures rise 1.09% to ₹2.33 lakh per kg — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/gold/silver-futures-rise-109-to-233-lakh-per-kg/article71327075.ece
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [AMBER 4.09] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 261.19, z20 2.09, zc -0.09, resid-z -0.17 [quiet], 1d -0.36%, |z20|=2.09; 1y-pct=99
- **Mechanism**: The recent Q1 results of Cupid, with a threefold rise in profit and 159% surge in revenue, have not been fully priced in by the market, as indicated by the quiet move label and low resid_z of -0.17. This suggests that the market has not fully reacted to the positive earnings surprise. The valid metal_copper_channel may play a role in transmitting this move to Indian metal equities.
- **Gap**: No gap: the event has been largely priced in, as evidenced by the low resid_z and quiet move label
- **India take**: Indian metal equities, such as those in the Nifty Metal index, may react positively to Cupid's strong Q1 results, although the response has not yet materialized. The metal_copper_channel may facilitate this transmission.
- Watch next: nifty_metal (up) — not yet - watch; Cupid's strong Q1 results may positively impact the broader metal sector
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [RED 4.0] fx · 3 series ↑
- usd_mxn [FX]: last 17.15, z20 -2.68, zc -0.78, resid-z -0.36 [quiet], 1d -0.32%, |z20|=2.68; 1y-pct=1
- aud_usd [FX]: last 0.71, z20 2.11, zc 0.94, resid-z -0.47 [quiet], 1d 0.49%, |z20|=2.11
- eur_usd [FX]: last 1.16, z20 1.76, zc 0.72, resid-z -1.06 [quiet], 1d 0.27%, |z20|=1.76
- **Mechanism**: The recent surge in FX markets, particularly in usd_mxn, aud_usd, and eur_usd, is driven by a combination of factors, but the small resid_z values indicate that the moves are largely priced in. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly contribute to the current FX move. Instead, the transmission setups, like bovespa -> aud_usd and bovespa -> usd_mxn, suggest a lead-lag relationship between the Brazilian stock market and FX pairs.
- **Gap**: No gap: the small resid_z values and the already moved status of the FX pairs indicate that the current prices reflect the available information
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the usd_mxn move, given its negative correlation. Further transmission effects may be seen in other Indian instruments, such as those related to metal equities, via the metal_copper_channel.
- Watch next: usd_mxn (down) — already moved; historical analogue suggests a potential decline
- Watch next: aud_usd (down) — already moved; historical analogue suggests a potential decline
- Watch next: eur_usd (down) — already moved; historical analogue suggests a potential decline
- **India receivers**: dyn_muthootfin_ns (rho -0.575, z -1.01)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 3.81] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.29, z20 1.81, zc 0.23, resid-z -0.46 [quiet], 1d 0.55%, 1y-pct=100
- **Mechanism**: The recent move in dyn_tech is largely priced, with a small resid_z of -0.46, indicating that the move is mostly explained by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly influence the Indian equity market's reaction to dyn_tech. However, the vix_equity_inverse channel suggests that a vol spike could lead to an equity drawdown, which may impact the Indian market.
- **Gap**: No gap: the move in dyn_tech is largely priced, with a small resid_z, and the Indian transmission candidate, dyn_inoxindia_ns, has not yet reacted significantly
- **India take**: The Indian instrument that expresses this move is dyn_inoxindia_ns, which has a negative correlation with dyn_tech, but it has not yet reacted significantly. The Nifty 50 and Sensex are also expected to be impacted by the global market trends, including the US inflation data.
- Watch next: dyn_inoxindia_ns (down) — not yet - watch; Negative correlation with dyn_tech
- **India receivers**: dyn_inoxindia_ns (rho -0.406, z 0.3)
- Source: Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results, Sky Gold, Dynamatic Tech, Quality Power, Anant Raj shares gain after Q1, Kaynes Tech, Ola, Oswal Pumps, Jamna Auto, Apollo Micro shares in red — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Source: Nifty opens flat as Titan, Tech Mahindra lead gains; markets eye US inflation data — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/nifty-opens-flat-as-titan-tech-mahindra-lead-gains-markets-eye-us-inflation-data/article71326945.ece
- Source: Kaynes Tech shares crash 8% after weak Q1 results: What are Nomura and Motilal Oswal saying — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/kaynes-tech-shares-crash-8-after-weak-q1-results-what-are-nomura-and-motilal-oswal-saying/articleshow/133081372.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.33] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.22, z20 1.40, zc 1.21, resid-z 1.02 [quiet], 1d 0.97%, 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.03, zc 1.32, resid-z 0.90 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.43, z20 1.00, zc 0.51, resid-z -0.28 [quiet], 1d 0.83%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.76, z20 -0.40, zc 0.74, resid-z 0.28 [quiet], 1d 0.23%, 1y-pct=3
- ust_2y [RATES]: last 4.25, z20 0.25, zc 1.33, resid-z 0.95 [quiet], 1d 1.67%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_lth (co-move) — not yet - watch; rho 0.546 vs dyn_bond, historically leads by 2d
- Watch next: brent (co-move) — not yet - watch; rho 0.535 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.508 vs ust_10y, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 3.3] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 172.00, z20 3.30, zc 2.03, resid-z 0.09 [moved], 1d 10.31%, |z20|=3.30
- **Mechanism**: dyn_pltr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho 0.4 via dyn_pltr, z 2.07, reacted)
- **India receivers**: dyn_atherenerg_ns (rho 0.4, z 2.07)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

## Watchlist (below surfacing floor)
dyn_indianb_ns ↑ (2.87), dyn_icicigi_bo ↓ (2.56), dyn_lth ↑ (2.41), nifty_metal ↑ (2.25), usd_cny ↓ (2.15), dyn_indusindbk_bo ↑ (2.13), bovespa ↓ (2.09), dyn_atherenerg_ns ↑ (2.07), nifty_midcap_100 ↑ (1.96), corn ↑ (1.93), asx_200 ↑ (1.79), nifty_it ↑ (1.6)

## India macro
- nifty_50: 24591.2500 (1d 0.08%, z20 1.25, flag none)
- nifty_midcap_100: 63872.1016 (1d 0.65%, z20 1.96, flag amber)
- usd_inr: 95.2150 (1d -0.10%, z20 -1.31, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5974 (1d 0.56%, z20 0.55, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.3 — "From infrastructure to energy storage: The expanding role of zinc in India’s development j"
- COALINDIA.NS (COAL INDIA LTD) score 77.5 — "From infrastructure to energy storage: The expanding role of zinc in India’s development j"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.2 — "From infrastructure to energy storage: The expanding role of zinc in India’s development j"
- INDIANB.NS (INDIAN BANK) score 53.2 — "Foreign flows into Indian bonds may remain muted despite tax relief: SBI Funds"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.4 — "Technocraft Ventures IPO Day 2 LIVE: GMP jumps! Subscription status, review, other details"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.9 — "Technocraft Ventures IPO Day 2 LIVE: GMP jumps! Subscription status, review, other details"
- TECH (Bio-Techne Corp) score 41.3 — "Technocraft Ventures IPO Day 2 LIVE: GMP jumps! Subscription status, review, other details"
- BAC (Bank of America Corporation) score 40.3 — "Mcap of four of top-10 most valued firms jumps ₹1.43 lakh crore; State Bank biggest winner"
- COIN (Coinbase Global, Inc.) score 39.4 — "India's gas demand returns to pre-disruption levels, but global LNG competition rises: Equ"
- OHI (Omega Healthcare Investors, In) score 36.4 — "Molbio Diagnostics raises ₹281 cr from anchor investors ahead of IPO"
- HDB (HDFC Bank Limited) score 35.6 — "Mcap of four of top-10 most valued firms jumps ₹1.43 lakh crore; State Bank biggest winner"
- IDBI.NS (IDBI BANK LIMITED) score 34.7 — "Mcap of four of top-10 most valued firms jumps ₹1.43 lakh crore; State Bank biggest winner"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.7 — "Mcap of four of top-10 most valued firms jumps ₹1.43 lakh crore; State Bank biggest winner"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.2 — "Mcap of four of top-10 most valued firms jumps ₹1.43 lakh crore; State Bank biggest winner"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.7 — "EU Locks In Plan To Triple Energy Storage Capacity By 2030"
- CHKP (Check Point Software Technolog) score 27.4 — "Crude Check: Uncertainty remains"
- LTH (Life Time Group Holdings, Inc.) score 24.3 — "Australian Wheat Crop Rebounds at Crucial Time for Global Supply"
- 301077.SZ (CHINASTARS) score 21.1 — "Is China’s party newspaper carrying more stories highlighting women’s role as mothers?"
- BOND (PIMCO Active Bond Exchange-Tra) score 19.4 — "Foreign flows into Indian bonds may remain muted despite tax relief: SBI Funds"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.7 — "Tata Consumer Share Price Live Updates: Tata Consumer's Performance Overview"
- JIOFIN.BO (Jio Financial Services Limited) score 8.9 — "RIL Share Price Live Updates: RIL's Financial Snapshot"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.7 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Current Trading Status"
- MS (Morgan Stanley) score 8.6 — "SBI shares rise nearly 2% after Q1 beat. Here's what Nomura, Morgan Stanley and other top "
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.3 — "SpaceX’s stock just had one of its best days ever — with the first lockup expiration now b"
- VT (Vanguard Total World Stock Ind) score 7.5 — "HASSETT: TAKE OUT GOVT WORKERS, WORLD CUP, JOBS ROSE 100,000"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.9 — "Q1 results 2026: Vodafone Idea to Bharat Forge among companies to declare Q1 results today"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.3 — "RIL Share Price Live Updates: RIL's Financial Snapshot"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.3 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.1 — "How Adani’s $125 billion capex boom is creating new winners on Dalal Street"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.9 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- PLTR (Palantir Technologies Inc.) score 4.2 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- META (Meta) score 4.1 — "Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Ze"
- NVDA (NVIDIA Corporation) score 3.9 — "Two reasons why Nvidia’s stock saw its biggest weekly surge in more than a year"
- AAPL (Apple Inc.) score 3.3 — "U.S. stock futures flat as investors await inflation data, grapple with more Iran uncertai"
- AMZN (Amazon.com, Inc.) score 3.0 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 2.7 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"
- GOOGL (Alphabet) score 2.7 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- MSFT (Microsoft Corporation) score 2.5 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- SNDK (Sandisk Corporation) score 2.2 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
- INFY (Infosys Limited) score 2.0 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"

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