# Transmission Layer — board brief · 2026-11-06 19:19Z

data as of **2026-11-06** · 97 series · 17 red / 35 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.787, 2d in regime; vol-pct 0.927, breadth-off 0.647, Markov P(high-vol) 0.63)
- [INVERTED] **safe_haven_gold** — corr20 -0.15, corr60 -0.22, contra nifty_50 corr20=0.3, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.13, last shift 2026-09-16. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.06, corr60 0.05, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-18. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.12, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.34, corr60 0.29, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **17 of 89** scanned series survive multiplicity control (effective p ≤ 0.017788085260673547)
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.636, β 0.889, p 0.0); driver zc 2.39 → expected 0.629%. Type hit-rate 0.827 (n=2068).
- **SETUP** dxy → usd_mxn: leads 1d (ccf 0.441, β 0.6457, p 0.0); driver zc 2.39 → expected 0.457%. Type hit-rate 0.827 (n=2068).
- **SETUP** dax → usd_mxn: leads 1d (ccf -0.252, β -0.1398, p 0.00196); driver zc -1.79 → expected 0.282%. Type hit-rate 0.827 (n=2068).
- Track record · residual_reversion: hit-rate **0.509** (n=1131) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2068) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.98] cross-asset · 6 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1087.75, z20 3.83, zc 0.74, resid-z -0.71 [quiet], 1d 1.66%, |z20|=3.83
- nifty_50 [INDICES]: last 25030.35, z20 3.71, zc 1.80, resid-z 2.78 [unexplained], 1d 2.01%, |z20|=3.71
- nifty_metal [INDICES]: last 12690.25, z20 2.85, zc 0.52, resid-z -1.42 [quiet], 1d 0.76%, |z20|=2.85
- dyn_jiofin_bo [EQUITIES]: last 230.40, z20 2.77, zc 0.21, resid-z -1.33 [quiet], 1d 0.39%, |z20|=2.77
- nifty_fmcg [INDICES]: last 46785.50, z20 2.40, zc 0.49, resid-z -1.64 [unexplained], 1d 0.67%, |z20|=2.40
- nifty_midcap_100 [INDICES]: last 60618.90, z20 2.06, zc 0.00, resid-z -2.94 [unexplained], 1d 0.01%, |z20|=2.06
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.678 via nifty_metal, z 1.54, reacted); dyn_muthootfin_ns (rho 0.643 via nifty_midcap_100, z 2.81, reacted); dyn_indusindbk_bo (rho 0.627 via nifty_midcap_100, z 2.8, reacted); dyn_indianb_ns (rho 0.603 via nifty_midcap_100, z 2.94, reacted); dyn_policybzr_ns (rho 0.528 via nifty_midcap_100, z -1.11, reacted)
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.503 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.678, z 1.54); dyn_muthootfin_ns (rho 0.643, z 2.81); dyn_indusindbk_bo (rho 0.627, z 2.8); dyn_indianb_ns (rho 0.603, z 2.94)
- Source: Dhanteras special: Gold beats stocks or Nifty takes the lead? Gold vs Nifty 50 returns in Samvat 2082 compared — Mint Markets, 2026-11-06. https://www.livemint.com/market/stock-market-news/dhanteras-diwali-gold-beats-stocks-or-nifty-takes-the-lead-gold-vs-nifty-50-returns-in-samvat-2082-compared-11793983947279.html
- Source: Nifty reclaims 25,000, Sensex crosses 81,000 as India shrugs off global tech rout — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/nifty-reclaims-25000-sensex-crosses-81000-as-india-shrugs-off-global-tech-rout/article71674840.ece
- Source: Pulse of the Street: Dalal Street shines before Diwali. Can the rally last? — Mint Markets, 2026-11-06. https://www.livemint.com/market/pulse-of-the-street-dalal-street-shines-before-diwali-can-the-rally-last-11793965614339.html
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-14 (d=1.45), 2025-12-23 (d=1.47)

### [RED 7.4] cross-asset · 10 series ↓
- dyn_vt [EQUITIES]: last 152.10, z20 -2.64, zc 0.25, resid-z -0.03 [quiet], 1d 0.48%, |z20|=2.64
- sp500 [INDICES]: last 7404.23, z20 -2.62, zc 0.35, resid-z -0.47 [quiet], 1d 0.69%, |z20|=2.62
- nasdaq_100 [INDICES]: last 27076.53, z20 -2.24, zc 0.59, resid-z -3.34 [unexplained], 1d 1.68%, |z20|=2.24
- vix [INDICES]: last 24.45, z20 2.15, zc -0.29, resid-z n/a [quiet], 1d -13.24%, |z20|=2.15
- dyn_coin [EQUITIES]: last 133.72, z20 -2.13, zc -0.48, resid-z -0.20 [quiet], 1d -2.27%, |z20|=2.13; 1y-pct=0
- btc_usd [CRYPTO]: last 75609.29, z20 -2.03, zc -0.15, resid-z -0.21 [quiet], 1d -0.44%, |z20|=2.03
- hy_oas [RATES]: last 3.48, z20 2.00, zc 1.63, resid-z -3.82 [unexplained], 1d 4.82%, |z20|=2.00; 1y-pct=100
- eth_usd [CRYPTO]: last 2225.15, z20 -1.64, zc -0.09, resid-z 0.19 [quiet], 1d -0.42%, |z20|=1.64
- ig_oas [RATES]: last 0.93, z20 1.47, zc 0.82, resid-z -2.86 [unexplained], 1d 2.20%, 1y-pct=97
- dyn_rs [EQUITIES]: last 421.16, z20 -0.05, zc 1.05, resid-z -0.73 [quiet], 1d 1.72%, 1y-pct=96
- **Mechanism**: cross-asset · 10 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-21 (z-distance 0.71).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.49 via ig_oas, z -1.99, reacted); nifty_it (rho 0.397 via ig_oas, z 1.13, reacted); nifty_midcap_100 (rho -0.385 via ig_oas, z 2.06, reacted); dyn_policybzr_ns (rho -0.359 via ig_oas, z -1.11, reacted)
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.862 vs dyn_vt, historically leads by 1d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.518 vs btc_usd, historically leads by 1d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.588 vs dyn_vt
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.528 vs hy_oas
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.52 vs dyn_coin
- **India receivers**: midcap_largecap_ratio (rho -0.49, z -1.99); nifty_it (rho 0.397, z 1.13); nifty_midcap_100 (rho -0.385, z 2.06); dyn_policybzr_ns (rho -0.359, z -1.11)
- Source: The S&P 500 could be dangerously exposed to AI. Here are some simple alternatives. — MarketWatch Top, 2026-11-06. https://www.marketwatch.com/story/the-s-p-500-has-become-a-big-ai-bet-here-are-some-simple-alternatives-3c7574a4?mod=mw_rss_topstories
- Source: Nifty reclaims 25,000, Sensex crosses 81,000 as India shrugs off global tech rout — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/nifty-reclaims-25000-sensex-crosses-81000-as-india-shrugs-off-global-tech-rout/article71674840.ece
- Source: US stocks today: Nasdaq rebounds as chip stocks recover from steep losses, rate fears persist — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-opens-higher-as-chips-pare-losses-rate-hike-fears-linger/articleshow/135611515.cms
- Historical analogues: 2025-10-21 (d=0.71), 2025-10-31 (d=0.74), 2025-08-29 (d=0.98)

### [RED 6.93] usd_inr ↓
- usd_inr [FX]: last 93.89, z20 -1.93, zc -1.40, resid-z -1.56 [unexplained], 1d -0.66%, 20d range extreme; |z20|=1.93; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.368 via usd_inr, z 1.96, reacted); dyn_idbi_ns (rho -0.357 via usd_inr, z -0.38, quiet)
- **India receivers**: dyn_havells_ns (rho -0.368, z 1.96); dyn_idbi_ns (rho -0.357, z -0.38)
- Source: Rupee strengthens to close at a six-and-a-half-month high — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/forex/rupee-strengthens-to-close-at-a-six-and-a-half-month-high/article71675114.ece
- Source: Rupee surges 52 points to close at 93.89 against US dollar — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/forex/rupee-surges-52-points-to-close-at-9389-against-us-dollar/article71673987.ece
- Source: Indian rupee strengthens past 94/$ as oil slides, foreign inflows return — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/forex/indian-rupee-strengthens-past-94/-as-oil-slides-foreign-inflows-return/articleshow/135604040.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.45] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 39717.22, z20 -3.13, zc -1.91, resid-z -3.62 [unexplained], 1d -4.47%, |z20|=3.13
- nikkei_225 [INDICES]: last 57410.91, z20 -2.95, zc -3.58, resid-z -4.31 [unexplained], 1d -6.00%, |z20|=2.95
- kospi [INDICES]: last 5101.44, z20 -2.28, zc -1.40, resid-z -2.12 [unexplained], 1d -5.24%, |z20|=2.28
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
- dyn_schd [EQUITIES]: last 35.27, z20 0.51, zc -0.36, resid-z 2.43 [unexplained], 1d -0.43%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.843 vs ust_2y
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.014 vs ust_2y, historically leads by 1d
- Source: India's 10-year bond posts best week in 7 years, leads emerging Asia as oil slides — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/bonds/indias-10-year-bond-posts-best-week-in-7-years-leads-emerging-asia-as-oil-slides/articleshow/135606792.cms
- Source: 56% returns in 6 months! TAAL Tech dividend record date ahead- Check eligibility, dividend amount, payment timeline — Mint Markets, 2026-11-06. https://www.livemint.com/market/stock-market-news/56-returns-in-6-months-taal-tech-dividend-record-date-ahead-check-eligibility-dividend-amount-payment-timeline-11793962758960.html
- Source: India bonds emerge as top Asian performers as oil, Treasury yields decline — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/bonds/india-bonds-emerge-as-top-asian-performers-as-oil-treasury-yields-decline/articleshow/135597789.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.46), 2025-05-19 (d=1.07)

### [RED 4.83] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 25.16, z20 2.83, zc 0.97, resid-z 2.55 [unexplained], 1d 1.86%, |z20|=2.83
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.379 via dyn_hdb, z 3.71, reacted)
- **India receivers**: nifty_50 (rho 0.379, z 3.71)
- Source: Muhurat Trading 2026: Equirus Prive's 16 Diwali picks include HDFC Bank, M&M, ESFB Voltas; upside seen up to 54% — Mint Markets, 2026-11-06. https://www.livemint.com/market/stock-market-news/muhurat-trading-2026-equirus-prives-16-diwali-picks-include-hdfc-bank-m-m-esfb-voltas-upside-seen-up-to-54-11793974438126.html
- Source: HDFC Bank shares rally 16% in four sessions, cross ₹12-lakh-crore market cap — BusinessLine Mkts, 2026-11-06. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-rally-16-in-four-sessions-cross-12-lakh-crore-market-cap/article71673355.ece
- Source: HDFC Bank climbs for third straight session, up 12% from last week’s Low — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-climbs-for-third-straight-session-up-12-from-last-weeks-low/article71668872.ece
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
- dyn_indusindbk_bo [EQUITIES]: last 911.45, z20 2.80, zc 0.01, resid-z -1.48 [quiet], 1d 0.05%, |z20|=2.80
- **Mechanism**: dyn_indusindbk_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.627 via dyn_indusindbk_bo, z 2.06, reacted); nifty_50 (rho 0.621 via dyn_indusindbk_bo, z 3.71, reacted); dyn_jiofin_bo (rho 0.579 via dyn_indusindbk_bo, z 2.77, reacted); dyn_bajfinance_ns (rho 0.546 via dyn_indusindbk_bo, z 3.83, reacted); dyn_tatatech_ns (rho 0.472 via dyn_indusindbk_bo, z -0.63, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.627, z 2.06); nifty_50 (rho 0.621, z 3.71); dyn_jiofin_bo (rho 0.579, z 2.77); dyn_bajfinance_ns (rho 0.546, z 3.83)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank  Current Price Update — ET Markets, 2026-11-06. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-share-price-today-live-06-nov-2026/liveblog/135591674.cms
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank Sees Significant Price Surge — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-live-updates-05-nov-2026/liveblog/135557166.cms
- Source: IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-live-updates-05-nov-2026/liveblog/135557166.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

## Watchlist (below surfacing floor)
commodities · 2 series ↓ (4.6), comex_copper ↓ (4.38), aud_usd ↓ (4.08), dyn_lth ↑ (4.01), equities · 2 series ↑ (3.77), dyn_tech ↑ (3.77), cross-asset · 2 series ↑ (3.42), dyn_4417_t ↑ (3.28), dyn_techm_ns ↑ (2.91), eur_inr ↓ (2.72), asx_200 ↑ (2.55), dyn_sepn ↑ (2.35)

## India macro
- nifty_50: 25030.3496 (1d 2.01%, z20 3.71, flag red)
- nifty_midcap_100: 60618.8984 (1d 0.01%, z20 2.06, flag amber)
- usd_inr: 93.8950 (1d -0.66%, z20 -1.93, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4218 (1d -1.97%, z20 -1.99, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · AMFI SIP / MF flows T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 103.1 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- INOXINDIA.NS (INOX INDIA LIMITED) score 102.5 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 101.8 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- INDIANB.NS (INDIAN BANK) score 66.7 — "Kotak Bank Share Price Highlights: Kotak Bank Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 59.3 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 57.5 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- TECH (Bio-Techne Corp) score 57.5 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- OHI (Omega Healthcare Investors, In) score 49.5 — "Will AI backlash delay Anthropic IPO? Investors raise doubts"
- BAC (Bank of America Corporation) score 48.7 — "Kotak Bank Share Price Highlights: Kotak Bank Stock Price History"
- HDB (HDFC Bank Limited) score 47.2 — "Kotak Bank Share Price Highlights: Kotak Bank Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.4 — "Kotak Bank Share Price Highlights: Kotak Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 43.4 — "Kotak Bank Share Price Highlights: Kotak Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.4 — "Kotak Bank Share Price Highlights: Kotak Bank Stock Price History"
- TGT (Target Corporation) score 36.6 — "S&P 500 FUTURES FACE FURTHER DOWNSIDE AS BEARISH SIGNALS INTENSIFY S&P 500 E-mini futures "
- COIN (Coinbase Global, Inc.) score 30.4 — "Nifty reclaims 25,000, Sensex crosses 81,000 as India shrugs off global tech rout"
- CHKP (Check Point Software Technolog) score 28.8 — "Gold, Silver Price Live updates: Check latest gold and silver prices on Dhanteras. Check 2"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 27.6 — "Energy Aspects Slashes Forecast of China’s November Diesel Exports"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.3 — "India's 10-year bond posts best week in 7 years, leads emerging Asia as oil slides"
- 301077.SZ (CHINASTARS) score 27.0 — "Energy Aspects Slashes Forecast of China’s November Diesel Exports"
- LTH (Life Time Group Holdings, Inc.) score 22.1 — "Diwali 2026 stock market holiday: NSE, BSE open on Sunday but closed this day -Muhurat tra"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 21.9 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 19.0 — "STARLINK AND ONEWEB SATELLITE COMMUNICATIONS SERVICES POSE RISKS OF DESTABILISING THE SOCI"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.0 — "Hunting for next defence stock winners? Raymond, PTC, Axiscades, Rossell - Experts decode "
- RS (Reliance, Inc.) score 15.9 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.2 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 14.0 — "56% returns in 6 months! TAAL Tech dividend record date ahead- Check eligibility, dividend"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.6 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.6 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "Pulse of the Street: Dalal Street shines before Diwali. Can the rally last?"
- META (Meta) score 12.3 — "Manaksia Coated Metals raised ₹150 crore through QIP"
- DEMZ (Democratic Large Cap Core ETF) score 11.0 — "Democratic Congress to guard US’ Taiwan policy and press Trump on arms sales"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.6 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- SEPN (Septerna, Inc.) score 8.7 — "DEMOCRATS SWEEP CONGRESS. FED HIKE BETS RETREAT. Following the midterm results, December F"
- VT (Vanguard Total World Stock Ind) score 5.6 — "Gold prices may be nearing bottom as World Gold Council sees recovery signals"
- JEF (Jefferies Financial Group Inc.) score 5.1 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.0 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have just $500 in sa"
- GS (Goldman Sachs Group, Inc. (The) score 4.0 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 3.9 — "Infosys Share Price Live Updates: Infosys Price Update and Trends"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.9 — "Broker’s call: PB Fintech (Buy)"
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