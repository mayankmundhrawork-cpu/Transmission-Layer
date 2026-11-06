# Transmission Layer — board brief · 2026-11-06 12:03Z

data as of **2026-11-06** · 97 series · 21 red / 31 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.731, 2d in regime; vol-pct 0.962, breadth-off 0.5, Markov P(high-vol) 1.0)
- [INVERTED] **safe_haven_gold** — corr20 -0.16, corr60 -0.23, contra nifty_50 corr20=0.29, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.13, last shift 2026-09-16. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.05, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.9, last shift 2026-09-18. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.17, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.12, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.33, corr60 0.29, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **18 of 89** scanned series survive multiplicity control (effective p ≤ 0.018773411069677115)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.592, β 0.4896, p 0.0); driver zc -2.6 → expected -1.681%. Type hit-rate 0.826 (n=2070).
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.56, β 0.335, p 0.0); driver zc -3.69 → expected -1.498%. Type hit-rate 0.826 (n=2070).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.558, β 0.4282, p 0.0); driver zc -4.23 → expected -1.848%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.558, β 0.4395, p 0.0); driver zc -3.95 → expected -1.795%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_demz → asx_200: leads 1d (ccf 0.53, β 0.4, p 0.0); driver zc -3.22 → expected -1.388%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.525, β -0.3089, p 0.0); driver zc -3.95 → expected 1.261%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_schd → asx_200: leads 1d (ccf 0.493, β 0.4305, p 0.0); driver zc -2.16 → expected -0.951%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.476, β 0.1904, p 0.0); driver zc -3.06 → expected -1.226%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.473, β 0.2389, p 0.0); driver zc -2.01 → expected -0.856%. Type hit-rate 0.826 (n=2070).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.453, β -0.2592, p 0.0); driver zc -4.23 → expected 1.119%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.446, β -0.3856, p 0.0); driver zc -3.95 → expected 1.575%. Type hit-rate 0.826 (n=2070).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.43, β -0.1791, p 0.0); driver zc -4.02 → expected 1.127%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.345, β 0.528, p 1e-05); driver zc -3.95 → expected -2.156%. Type hit-rate 0.826 (n=2070).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.314, β 0.3517, p 3e-05); driver zc -3.69 → expected -1.573%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.302, β 0.3604, p 0.0); driver zc -3.95 → expected -1.472%. Type hit-rate 0.826 (n=2070).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.289, β 0.2515, p 0.0); driver zc -3.69 → expected -1.125%. Type hit-rate 0.826 (n=2070).
- **SETUP** dyn_demz → nifty_midcap_100: leads 1d (ccf 0.276, β 0.302, p 0.0); driver zc -3.22 → expected -1.048%. Type hit-rate 0.826 (n=2070).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.274, β 0.3215, p 0.0); driver zc -4.23 → expected -1.388%. Type hit-rate 0.826 (n=2070).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.257, β 0.2148, p 2e-05); driver zc -4.02 → expected -1.351%. Type hit-rate 0.826 (n=2070).
- **SETUP** russell_2000 → nifty_50: leads 1d (ccf 0.254, β 0.1651, p 5e-05); driver zc -3.69 → expected -0.738%. Type hit-rate 0.826 (n=2070).
- Track record · residual_reversion: hit-rate **0.51** (n=1128) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2070) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.04] cross-asset · 8 series ↓
- sp500 [INDICES]: last 7356.73, z20 -4.54, zc -4.23, resid-z -0.47 [priced], 1d -4.32%, |z20|=4.54
- dyn_vt [EQUITIES]: last 151.37, z20 -4.37, zc -3.95, resid-z -0.03 [priced], 1d -4.08%, |z20|=4.37
- nasdaq_100 [INDICES]: last 26647.86, z20 -3.44, zc -4.02, resid-z -3.34 [unexplained], 1d -6.29%, |z20|=3.44
- vix [INDICES]: last 26.53, z20 2.87, zc -0.13, resid-z n/a [quiet], 1d -5.86%, |z20|=2.87; 1y-pct=96
- dyn_demz [EQUITIES]: last 46.87, z20 -2.56, zc -3.22, resid-z 1.51 [unexplained], 1d -3.47%, |z20|=2.56
- dyn_coin [EQUITIES]: last 136.84, z20 -2.26, zc -2.06, resid-z -0.20 [priced], 1d -9.68%, |z20|=2.26; 1y-pct=0
- btc_usd [CRYPTO]: last 76014.42, z20 -1.85, zc 0.03, resid-z -0.66 [quiet], 1d 0.10%, |z20|=1.85
- russell_2000 [INDICES]: last 2729.20, z20 -1.70, zc -3.69, resid-z 0.22 [priced], 1d -4.47%, |z20|=1.70
- **Mechanism**: cross-asset · 8 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.43).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.515 vs btc_usd, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.527 vs dyn_coin
- Source: Sensex reclaims 80,000 after March; Nifty tops 24,700 despite global tech rout — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/sensex-reclaims-80000-after-march-nifty-tops-24700-despite-global-tech-rout/article71673442.ece
- Source: The Global Oil Glut Returns as High Prices Crush Demand — OilPrice, 2026-11-06. https://oilprice.com/Latest-Energy-News/World-News/The-Global-Oil-Glut-Returns-as-High-Prices-Crush-Demand.html
- Source: The new anti-corruption law arming Beijing with wide global enforcement powers — SCMP Economy, 2026-11-06. https://www.scmp.com/news/china/politics/article/3373519/new-anti-corruption-law-arms-beijing-expansive-global-enforcement-powers
- Historical analogues: 2026-05-22 (d=0.43), 2025-10-23 (d=0.73), 2025-08-28 (d=0.93)

### [RED 7.98] cross-asset · 6 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1087.75, z20 3.83, zc 0.74, resid-z -0.82 [quiet], 1d 1.66%, |z20|=3.83
- nifty_50 [INDICES]: last 25030.35, z20 3.71, zc 1.80, resid-z 3.39 [unexplained], 1d 2.01%, |z20|=3.71
- nifty_metal [INDICES]: last 12690.25, z20 2.85, zc 0.52, resid-z -1.29 [quiet], 1d 0.76%, |z20|=2.85
- dyn_jiofin_bo [EQUITIES]: last 230.40, z20 2.77, zc 0.21, resid-z -1.28 [quiet], 1d 0.39%, |z20|=2.77
- nifty_fmcg [INDICES]: last 46785.50, z20 2.40, zc 0.49, resid-z -1.51 [unexplained], 1d 0.67%, |z20|=2.40
- nifty_midcap_100 [INDICES]: last 60618.90, z20 2.06, zc 0.00, resid-z -2.78 [unexplained], 1d 0.01%, |z20|=2.06
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.678 via nifty_metal, z 1.54, reacted); dyn_muthootfin_ns (rho 0.643 via nifty_midcap_100, z 2.81, reacted); dyn_indusindbk_bo (rho 0.627 via nifty_midcap_100, z 2.8, reacted); dyn_indianb_ns (rho 0.603 via nifty_midcap_100, z 2.94, reacted); dyn_policybzr_ns (rho 0.528 via nifty_midcap_100, z -1.11, reacted)
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.503 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.678, z 1.54); dyn_muthootfin_ns (rho 0.643, z 2.81); dyn_indusindbk_bo (rho 0.627, z 2.8); dyn_indianb_ns (rho 0.603, z 2.94)
- Source: Sensex reclaims 80,000 after March; Nifty tops 24,700 despite global tech rout — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/sensex-reclaims-80000-after-march-nifty-tops-24700-despite-global-tech-rout/article71673442.ece
- Source: Sensex today | Stock Market Live: Sensex settled at 81,028.02 on Friday; Nifty 50 rises to 25,030.35 — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-6-november-2026/article71669668.ece
- Source: Diwali 2026: Is Samvat 2083 the start of Dalal Street’s next big rally? — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/stocks/diwali-2026-is-samvat-2083-the-start-of-dalal-streets-next-big-rally/videoshow/135603351.cms
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-14 (d=1.45), 2025-12-23 (d=1.47)

### [RED 6.92] usd_inr ↓
- usd_inr [FX]: last 93.90, z20 -1.92, zc -1.39, resid-z -1.38 [quiet], 1d -0.65%, 20d range extreme; |z20|=1.92; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.368 via usd_inr, z 1.96, reacted); dyn_idbi_ns (rho -0.357 via usd_inr, z -0.38, quiet)
- **India receivers**: dyn_havells_ns (rho -0.368, z 1.96); dyn_idbi_ns (rho -0.357, z -0.38)
- Source: Rupee surges 52 points to close at 93.89 against US dollar — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/forex/rupee-surges-52-points-to-close-at-9389-against-us-dollar/article71673987.ece
- Source: Indian rupee strengthens past 94/$ as oil slides, foreign inflows return — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/forex/indian-rupee-strengthens-past-94/-as-oil-slides-foreign-inflows-return/articleshow/135604040.cms
- Source: Rupee falls 9 paise to 94.50 against US dollar in early trade — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/forex/rupee-falls-9-paise-to-94-50-against-us-dollar-in-early-trade/articleshow/135597848.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.45] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 39717.22, z20 -3.13, zc -1.91, resid-z 1.35 [moved], 1d -4.47%, |z20|=3.13
- nikkei_225 [INDICES]: last 57410.91, z20 -2.95, zc -3.58, resid-z 1.00 [moved], 1d -6.00%, |z20|=2.95
- kospi [INDICES]: last 5101.44, z20 -2.28, zc -1.40, resid-z 0.84 [quiet], 1d -5.24%, |z20|=2.28
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.552 via nikkei_225, z -1.99, reacted); nifty_50 (rho -0.53 via taiwan_weighted, z 3.71, reacted); nifty_it (rho -0.475 via kospi, z 1.13, reacted); dyn_idbi_ns (rho 0.404 via nikkei_225, z -0.38, quiet); dyn_inoxindia_ns (rho 0.365 via nikkei_225, z -1.14, reacted)
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.542 vs taiwan_weighted
- **India receivers**: midcap_largecap_ratio (rho 0.552, z -1.99); nifty_50 (rho -0.53, z 3.71); nifty_it (rho -0.475, z 1.13); dyn_idbi_ns (rho 0.404, z -0.38)
- Source: How US Midterm Election Results, AI sell-off impacted US stock market, Nikkei 225, Kospi, Taiwan and China; data details — Mint Markets, 2026-11-06. https://www.livemint.com/market/stock-market-news/how-us-midterm-election-results-ai-sell-off-impacted-us-stock-market-nikkei-225-kospi-taiwan-and-china-data-details-11793943446082.html
- Source: Japan’s Nikkei plunges 5.7%, South Korea’s Kospi falls 7.4% amid AI stock rout — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/stock-markets/japans-nikkei-plunges-57-south-koreas-kospi-falls-74-amid-ai-stock-rout/article71672730.ece
- Source: Stock market outlook today, 6 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11793925396840.html

### [AMBER 5.06] cross-asset · 3 series ↓
- ust_2y [RATES]: last 4.58, z20 -1.75, zc -0.51, resid-z -0.66 [quiet], 1d -0.65%, |z20|=1.75
- ust_10y [RATES]: last 4.90, z20 -1.63, zc -0.93, resid-z -1.10 [quiet], 1d -1.01%, |z20|=1.63
- dyn_schd [EQUITIES]: last 35.41, z20 0.75, zc -2.16, resid-z 2.43 [unexplained], 1d -2.21%, 1y-pct=98
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.843 vs ust_2y
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.014 vs ust_2y, historically leads by 1d
- Source: 56% returns in 6 months! TAAL Tech dividend record date ahead- Check eligibility, dividend amount, payment timeline — Mint Markets, 2026-11-06. https://www.livemint.com/market/stock-market-news/56-returns-in-6-months-taal-tech-dividend-record-date-ahead-check-eligibility-dividend-amount-payment-timeline-11793962758960.html
- Source: India bonds emerge as top Asian performers as oil, Treasury yields decline — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/bonds/india-bonds-emerge-as-top-asian-performers-as-oil-treasury-yields-decline/articleshow/135597789.cms
- Source: Govt bonds emerge as top Asian performers as oil, Treasury yields decline — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/govt-bonds-emerge-as-top-asian-performers-as-oil-treasury-yields-decline/article71673151.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.46), 2025-05-19 (d=1.07)

### [RED 4.83] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 24.69, z20 2.83, zc 0.76, resid-z 2.55 [unexplained], 1d 1.48%, |z20|=2.83
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: HDFC Bank shares rally 16% in four sessions, cross ₹12-lakh-crore market cap — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-rally-16-in-four-sessions-cross-12-lakh-crore-market-cap/article71673355.ece
- Source: HDFC Bank climbs for third straight session, up 12% from last week’s Low — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-climbs-for-third-straight-session-up-12-from-last-weeks-low/article71668872.ece
- Source: HDFC Bank shares witness strong buying, rise 7% in 1 month. Can new CEO, improving fundamentals drive next leg of rally? — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/hdfc-bank-shares-witness-strong-buying-rise-7-in-1-month-can-new-ceo-improving-fundamentals-drive-next-leg-of-rally-11793861115989.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.81] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 2869.00, z20 2.81, zc 0.28, resid-z -0.85 [quiet], 1d 1.06%, |z20|=2.81
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.643 via dyn_muthootfin_ns, z 2.06, reacted); dyn_jiofin_bo (rho 0.612 via dyn_muthootfin_ns, z 2.77, reacted); nifty_metal (rho 0.587 via dyn_muthootfin_ns, z 2.85, reacted); nifty_50 (rho 0.512 via dyn_muthootfin_ns, z 3.71, reacted); nifty_fmcg (rho 0.473 via dyn_muthootfin_ns, z 2.4, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.643, z 2.06); dyn_jiofin_bo (rho 0.612, z 2.77); nifty_metal (rho 0.587, z 2.85); nifty_50 (rho 0.512, z 3.71)
- Source: Muthoot Microfin posts record disbursements, PAT jumps 3.6x in Q2 FY27 — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/muthoot-microfin-posts-record-disbursements-pat-jumps-36x-in-q2-fy27/article71670335.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 4.8] dyn_indusindbk_bo ↑
- dyn_indusindbk_bo [EQUITIES]: last 911.45, z20 2.80, zc 0.01, resid-z -1.54 [unexplained], 1d 0.05%, |z20|=2.80
- **Mechanism**: dyn_indusindbk_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.627 via dyn_indusindbk_bo, z 2.06, reacted); nifty_50 (rho 0.621 via dyn_indusindbk_bo, z 3.71, reacted); dyn_jiofin_bo (rho 0.579 via dyn_indusindbk_bo, z 2.77, reacted); dyn_bajfinance_ns (rho 0.546 via dyn_indusindbk_bo, z 3.83, reacted); dyn_tatatech_ns (rho 0.472 via dyn_indusindbk_bo, z -0.63, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.627, z 2.06); nifty_50 (rho 0.621, z 3.71); dyn_jiofin_bo (rho 0.579, z 2.77); dyn_bajfinance_ns (rho 0.546, z 3.83)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank  Current Price Update — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-share-price-today-live-06-nov-2026/liveblog/135591674.cms
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank Sees Significant Price Surge — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-live-updates-05-nov-2026/liveblog/135557166.cms
- Source: IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-live-updates-05-nov-2026/liveblog/135557166.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

## Watchlist (below surfacing floor)
dyn_lth ↑ (4.55), commodities · 2 series ↓ (4.52), comex_copper ↓ (4.4), aud_usd ↓ (3.9), equities · 2 series ↑ (3.77), dyn_atherenerg_ns ↑ (3.68), cross-asset · 2 series ↑ (3.42), dyn_4417_t ↑ (3.28), dyn_tech ↑ (2.91), dyn_techm_ns ↑ (2.91), eur_usd ↓ (2.7), ftse_100 ↓ (2.67)

## India macro
- nifty_50: 25030.3496 (1d 2.01%, z20 3.71, flag red)
- nifty_midcap_100: 60618.8984 (1d 0.01%, z20 2.06, flag amber)
- usd_inr: 93.9000 (1d -0.65%, z20 -1.92, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4218 (1d -1.97%, z20 -1.99, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · AMFI SIP / MF flows T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 105.2 — "Indian stocks set for pullback after sharp rally on oil slide, foreign inflows"
- INOXINDIA.NS (INOX INDIA LIMITED) score 104.5 — "Indian stocks set for pullback after sharp rally on oil slide, foreign inflows"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 103.8 — "Indian stocks set for pullback after sharp rally on oil slide, foreign inflows"
- INDIANB.NS (INDIAN BANK) score 67.3 — "Indian stocks set for pullback after sharp rally on oil slide, foreign inflows"
- TECHM.NS (TECH MAHINDRA LIMITED) score 60.4 — "Tech Mahindra Share Price Live Updates: Tech Mahindra finishes trading at Rs 1824.0"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 58.5 — "Tech Mahindra Share Price Live Updates: Tech Mahindra finishes trading at Rs 1824.0"
- TECH (Bio-Techne Corp) score 58.5 — "Tech Mahindra Share Price Live Updates: Tech Mahindra finishes trading at Rs 1824.0"
- OHI (Omega Healthcare Investors, In) score 53.0 — "Will AI backlash delay Anthropic IPO? Investors raise doubts"
- BAC (Bank of America Corporation) score 47.9 — "America’s Rare Earth Reckoning Is Less Than 60 Days Away"
- HDB (HDFC Bank Limited) score 46.3 — "Kotak Bank Share Price Live Updates: Kotak Bank's Performance Highlights"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.3 — "Kotak Bank Share Price Live Updates: Kotak Bank's Performance Highlights"
- IDBI.NS (IDBI BANK LIMITED) score 42.3 — "Kotak Bank Share Price Live Updates: Kotak Bank's Performance Highlights"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.3 — "Kotak Bank Share Price Live Updates: Kotak Bank's Performance Highlights"
- TGT (Target Corporation) score 34.9 — "Titan shines 3% on Dhanteras 2026 after 2x profit; Noel Tata's exit news from board adds t"
- COIN (Coinbase Global, Inc.) score 31.5 — "JAPAN’S PRIME MINISTER WARNS OF GLOBAL MARKET VOLATILITY Japanese Prime Minister Sanae Tak"
- CHKP (Check Point Software Technolog) score 28.7 — "Gold, Silver Price Live updates: Gold rates dip on Dhanteras as silver, yellow metal fall "
- BOND (PIMCO Active Bond Exchange-Tra) score 28.2 — "CHINA'S 10-YEAR BOND YIELD FALLS TO A RECORD LOW"
- 301077.SZ (CHINASTARS) score 27.9 — "CHINA'S 10-YEAR BOND YIELD FALLS TO A RECORD LOW"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 27.5 — "Oil Rebounds Toward $100 as Democrats’ Sweep Rattles Energy Stocks"
- LTH (Life Time Group Holdings, Inc.) score 21.6 — "56% returns in 6 months! TAAL Tech dividend record date ahead- Check eligibility, dividend"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 21.3 — "Bajaj Auto Share Price Live Updates: Bajaj Auto's Stock Update"
- JIOFIN.BO (Jio Financial Services Limited) score 19.3 — "Thermax shares fall 20% to 52-week low on weak Q2, JM Financial maintains sell"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.3 — "Dhanteras 2026 today: Buy gold at current rates or avoid? Shopping guide - 20% price down "
- RS (Reliance, Inc.) score 17.1 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- SCHD (Schwab US Dividend Equity ETF) score 15.0 — "56% returns in 6 months! TAAL Tech dividend record date ahead- Check eligibility, dividend"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.1 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Market Performance Snapshot"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.5 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Movement Today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.5 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Movement Today"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.8 — "IPO multibaggers: 13 stocks that delivered up to 193% returns since last Dhanteras"
- META (Meta) score 12.1 — "Gold, Silver Price Live updates: Gold rates dip on Dhanteras as silver, yellow metal fall "
- DEMZ (Democratic Large Cap Core ETF) score 10.8 — "NASDAQ ERASES $2.5 TRILLION AS DEMOCRATIC SWEEP SPARKS AI SELLOFF The Nasdaq 100 plunged 6"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.3 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Market Performance"
- SEPN (Septerna, Inc.) score 9.4 — "DEMOCRATS SWEEP CONGRESS. FED HIKE BETS RETREAT. Following the midterm results, December F"
- VT (Vanguard Total World Stock Ind) score 6.0 — "Gold prices may be nearing bottom as World Gold Council sees recovery signals"
- JEF (Jefferies Financial Group Inc.) score 5.5 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.4 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have just $500 in sa"
- GS (Goldman Sachs Group, Inc. (The) score 4.3 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 4.2 — "Infosys Share Price Live Updates: Infosys Price Update and Trends"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.0 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.4 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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