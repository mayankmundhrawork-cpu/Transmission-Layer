# Transmission Layer — board brief · 2026-11-18 03:00Z

data as of **2026-11-18** · 97 series · 11 red / 34 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.833, 3d in regime; vol-pct None, breadth-off 0.833, Markov P(high-vol) 0.054)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.22, contra nifty_50 corr20=0.33, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.14, corr60 0.1, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.21, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.21, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0008684598407633359)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.596, β 0.4907, p 0.0); driver zc -1.69 → expected -0.807%. Type hit-rate 0.818 (n=2062).
- **SETUP** dyn_schd → asx_200: leads 1d (ccf 0.495, β 0.4311, p 0.0); driver zc -1.82 → expected -0.649%. Type hit-rate 0.818 (n=2062).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.468, β 0.7911, p 0.0); driver zc -1.69 → expected -1.302%. Type hit-rate 0.818 (n=2062).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.434, β 0.2727, p 0.0); driver zc -1.69 → expected -0.449%. Type hit-rate 0.818 (n=2062).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.418, β -0.2525, p 0.0); driver zc -1.69 → expected 0.415%. Type hit-rate 0.818 (n=2062).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.27, β 0.2741, p 0.02178); driver zc -2.83 → expected -0.464%. Type hit-rate 0.818 (n=2062).
- Track record · residual_reversion: hit-rate **0.511** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2062) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.75] cross-asset · 9 series ↓
- dow_jones [INDICES]: last 50759.13, z20 -3.12, zc -1.69, resid-z -2.02 [unexplained], 1d -1.65%, |z20|=3.12
- russell_2000 [INDICES]: last 2703.29, z20 -2.76, zc -1.03, resid-z -0.71 [quiet], 1d -1.45%, |z20|=2.76
- sp500 [INDICES]: last 7340.63, z20 -2.25, zc -0.82, resid-z -0.25 [quiet], 1d -1.02%, |z20|=2.25
- dyn_coin [EQUITIES]: last 115.04, z20 -2.03, zc -0.86, resid-z -0.11 [quiet], 1d -4.00%, |z20|=2.03; 1y-pct=0
- vix [INDICES]: last 25.45, z20 1.99, zc 1.38, resid-z n/a [quiet], 1d 11.09%, |z20|=1.99
- btc_usd [CRYPTO]: last 64245.93, z20 -1.98, zc -0.06, resid-z -0.28 [quiet], 1d -0.17%, |z20|=1.98
- dyn_nvda [EQUITIES]: last 155.46, z20 -1.92, zc -0.12, resid-z -0.50 [quiet], 1d -0.44%, 1y-pct=0
- eth_usd [CRYPTO]: last 1801.68, z20 -1.83, zc -0.02, resid-z -0.09 [quiet], 1d -0.08%, |z20|=1.83
- nasdaq_100 [INDICES]: last 26996.90, z20 -1.61, zc -0.37, resid-z -1.47 [quiet], 1d -0.74%, |z20|=1.61
- **Mechanism**: cross-asset · 9 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.48).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.43 via dyn_nvda, z 1.69, reacted)
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.602 vs russell_2000, historically leads by 4d
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.654 vs dow_jones
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.611 vs sp500
- Watch next: dax (co-move) — not yet - watch; rho 0.596 vs dow_jones
- **India receivers**: dyn_bajfinance_ns (rho -0.43, z 1.69)
- Source: CoreWeave’s stock pops — even as Nvidia talks up a ‘disciplined’ approach to financing — MarketWatch Top, 2026-11-18. https://www.marketwatch.com/story/coreweaves-stock-pops-even-as-nvidia-talks-up-a-disciplined-approach-to-financing-e7f00876?mod=mw_rss_topstories
- Source: Nvidia’s stock rises as blowout numbers help ease CEO transition fears — MarketWatch Top, 2026-11-18. https://www.marketwatch.com/story/nvidias-stock-rises-as-blowout-numbers-help-ease-ceo-transition-fears-2f20d38a?mod=mw_rss_topstories
- Source: Stock market outlook today,18 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-18. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-18-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11794962131039.html
- Historical analogues: 2026-05-22 (d=0.48), 2025-10-21 (d=0.65), 2025-08-19 (d=1.07)

### [RED 7.2] usd_inr ↓
- usd_inr [FX]: last 93.46, z20 -2.20, zc -1.24, resid-z -0.28 [quiet], 1d -0.54%, 20d range extreme; |z20|=2.20
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.511 via usd_inr, z 1.55, reacted); dyn_indianb_ns (rho -0.45 via usd_inr, z 1.56, reacted); nifty_it (rho -0.433 via usd_inr, z -1.48, reacted); dyn_bajfinance_ns (rho -0.384 via usd_inr, z 1.69, reacted); dyn_tataelxsi_ns (rho -0.373 via usd_inr, z -1.49, reacted)
- **India receivers**: dyn_havells_ns (rho -0.511, z 1.55); dyn_indianb_ns (rho -0.45, z 1.56); nifty_it (rho -0.433, z -1.48); dyn_bajfinance_ns (rho -0.384, z 1.69)
- Source: Rupee hits 7-month high on FPI inflows, softer oil prices — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/forex/rupee-hits-7-month-high-on-fpi-inflows-softer-oil-prices/article71712359.ece
- Source: Rupee rises 43 paise to close at 93.51 (provisional) against US dollar — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/forex/rupee-rises-43-paise-to-close-at-9351-provisional-against-us-dollar/article71711397.ece
- Source: Robust inflows, pullback in shorts lift rupee to seven-month peak — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/forex/forex-news/robust-inflows-pullback-in-shorts-lift-rupee-to-seven-month-peak/articleshow/135921416.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.82] cross-asset · 4 series ↓
- comex_gold [COMMODITIES]: last 3798.80, z20 -2.16, zc 0.02, resid-z 0.30 [quiet], 1d 0.03%, |z20|=2.16; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 5.92, z20 -2.15, zc 0.02, resid-z -0.34 [quiet], 1d 0.04%, |z20|=2.15
- comex_silver [COMMODITIES]: last 46.01, z20 -2.10, zc 0.04, resid-z 0.72 [quiet], 1d 0.12%, |z20|=2.10; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 82.56, z20 1.92, zc n/a, resid-z n/a [quiet], 1d -0.09%, |z20|=1.92; 1y-pct=99
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.456 via comex_gold, z 0.65, quiet); dyn_karurvysya_ns (rho 0.427 via comex_gold, z 2.14, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.456, z 0.65); dyn_karurvysya_ns (rho 0.427, z 2.14)
- Source: Gold hits over one-year low ahead of Fed minutes — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/commodities/news/gold-hits-over-one-year-low-ahead-of-fed-minutes/articleshow/135945512.cms
- Source: Gold struggles to rebound from one-year low as US dollar, yields advance — Mint Markets, 2026-11-17. https://www.livemint.com/market/gold-struggles-to-rebound-from-one-year-low-as-us-dollar-yields-advance-11794942964000.html
- Source: Call for efforts to drive sustainable growth in gold-loan sector — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/gold/call-for-efforts-to-drive-sustainable-growth-in-gold-loan-sector/article71712201.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 5.61] dyn_kaynes_ns ↓
- dyn_kaynes_ns [EQUITIES]: last 2858.00, z20 -3.61, zc -1.50, resid-z -1.61 [unexplained], 1d -4.09%, |z20|=3.61; 1y-pct=0
- **Mechanism**: dyn_kaynes_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-23 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.367 via dyn_kaynes_ns, z 1.58, reacted); nifty_metal (rho 0.359 via dyn_kaynes_ns, z 0.84, quiet); dyn_tatatech_ns (rho 0.359 via dyn_kaynes_ns, z -0.55, quiet); dyn_jiofin_bo (rho 0.352 via dyn_kaynes_ns, z 1.21, reacted)
- **India receivers**: nifty_fmcg (rho 0.367, z 1.58); nifty_metal (rho 0.359, z 0.84); dyn_tatatech_ns (rho 0.359, z -0.55); dyn_jiofin_bo (rho 0.352, z 1.21)
- Source: Kaynes Technology stock in pain as Street falls out of love — Mint Markets, 2026-11-17. https://www.livemint.com/market/mark-to-market/kaynes-technology-stock-q2-results-smart-meter-sales-crash-11794899402071.html
- Source: Kaynes Technology shares extend losses, fall another 4%; should investors worry about its Q2 performance? — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/kaynes-technology-shares-extend-losses-fall-another-4-should-investors-worry-about-its-q2-performance-11794900682488.html
- Source: Amber Enterprises shares resume losing run, tank over 8% after weak Q2 from peer Kaynes Technology. Is more fall ahead? — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/amber-enterprises-shares-resume-losing-run-tank-over-8-after-weak-q2-from-peer-kaynes-technology-is-more-fall-ahead-11794813833370.html
- Historical analogues: 2026-01-23 (d=0.0), 2025-01-23 (d=0.01), 2026-01-06 (d=0.02)

### [AMBER 5.27] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -2.44, zc -0.11, resid-z -0.92 [quiet], 1d -0.04%, |z20|=2.44; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.01, zc 0.31, resid-z -1.03 [quiet], 1d 0.12%, |z20|=2.01; 1y-pct=3
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.049 vs eur_usd, historically leads by 1d
- Source: Boris Vujčić: Risks and resilience in the euro area financial system — ECB press, 2026-11-16. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp261116~db374b56ab.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 5.17] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 39727.13, z20 -1.86, zc -0.39, resid-z -0.97 [quiet], 1d -0.91%, |z20|=1.86
- kospi [INDICES]: last 4986.62, z20 -1.64, zc 0.11, resid-z -0.44 [quiet], 1d 0.37%, |z20|=1.64
- nikkei_225 [INDICES]: last 58696.54, z20 -1.56, zc -0.14, resid-z -0.49 [quiet], 1d -0.28%, |z20|=1.56
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.572 via kospi, z -1.35, reacted); nifty_50 (rho -0.505 via kospi, z 1.56, reacted); nifty_it (rho -0.492 via kospi, z -1.48, reacted); nifty_midcap_100 (rho 0.452 via nikkei_225, z 1.43, reacted); dyn_idbi_ns (rho 0.451 via nikkei_225, z -0.23, quiet)
- **India receivers**: midcap_largecap_ratio (rho 0.572, z -1.35); nifty_50 (rho -0.505, z 1.56); nifty_it (rho -0.492, z -1.48); nifty_midcap_100 (rho 0.452, z 1.43)
- Source: Stock market outlook today,18 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-18. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-18-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11794962131039.html
- Source: Stock market outlook today,17 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-17-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cue-11794875550779.html

### [RED 5.09] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 23.17, z20 5.09, zc 2.68, resid-z 3.40 [unexplained], 1d 12.04%, |z20|=5.09
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [AMBER 5.03] cross-asset · 3 series ↑
- dyn_eternal_ns [EQUITIES]: last 375.05, z20 1.71, zc 0.50, resid-z 0.33 [quiet], 1d 1.06%, 1y-pct=100
- dyn_bajfinance_ns [EQUITIES]: last 1121.10, z20 1.69, zc 0.50, resid-z -0.04 [quiet], 1d 1.00%, 1y-pct=98
- nifty_50 [INDICES]: last 25387.40, z20 1.56, zc 0.34, resid-z -0.00 [quiet], 1d 0.38%, |z20|=1.56
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-02-19 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.699 via nifty_50, z 1.43, reacted); dyn_jiofin_bo (rho 0.662 via nifty_50, z 1.21, reacted); nifty_fmcg (rho 0.641 via nifty_50, z 1.58, reacted); dyn_indusindbk_bo (rho 0.626 via dyn_bajfinance_ns, z 1.86, reacted); dyn_muthootfin_ns (rho 0.61 via nifty_50, z 0.65, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.506 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.577 vs nifty_50
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.552 vs dyn_bajfinance_ns
- **India receivers**: nifty_midcap_100 (rho 0.699, z 1.43); dyn_jiofin_bo (rho 0.662, z 1.21); nifty_fmcg (rho 0.641, z 1.58); dyn_indusindbk_bo (rho 0.626, z 1.86)
- Source: Sensex today | Stock Market Live Updates: Stock to buy today: Cemindia Projects (₹1,353) – BUY — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-18-november-2026/article71711870.ece
- Source: Gift Nifty signals weak opening for domestic markets — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/gift-nifty-signals-weak-opening-for-domestic-markets/article71714370.ece
- Source: Stock Market Live Updates: GIFT Nifty signals a negative start; Asian shares trade higher — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/stocks/live-blog/bse-sensex-today-nifty50-stock-market-live-updates-gift-nifty-hcl-tech-airtel-share-price-18-november-2026/liveblog/135945558.cms
- Historical analogues: 2025-02-19 (d=0.49), 2025-07-21 (d=0.84), 2025-07-11 (d=1.03)

## Watchlist (below surfacing floor)
dxy ↑ (5.0), dyn_blln ↓ (4.65), rates · 3 series ↑ (3.9), dyn_atherenerg_ns ↑ (3.14), dyn_lth ↑ (2.84), dyn_4417_t ↑ (2.82), eur_inr ↓ (2.67), dyn_crwv ↓ (2.54), shanghai_comp ↓ (2.38), aud_usd ↓ (2.26), dyn_karurvysya_ns ↑ (2.14), usd_mxn ↓ (1.82)

## India macro
- nifty_50: 25387.4004 (1d 0.38%, z20 1.56, flag amber)
- nifty_midcap_100: 61728.4492 (1d 0.25%, z20 1.43, flag none)
- usd_inr: 93.4600 (1d -0.54%, z20 -2.20, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4315 (1d -0.13%, z20 -1.35, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 78.3 — "Stock recommendations for 18 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.8 — "Stock recommendations for 18 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.2 — "Stock recommendations for 18 November from MarketSmith India"
- NVDA (NVIDIA Corporation) score 66.9 — "NVDA - NVIDIA STOPPED DISCLOSING SINGAPORE SALES AS REVENUES HIT $104BN US chipmaker chang"
- INDIANB.NS (INDIAN BANK) score 55.8 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- BAC (Bank of America Corporation) score 51.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- HDB (HDFC Bank Limited) score 45.5 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.9 — "US DNI CLAYTON ON TECH OUTAGES: NOT SEEING THIS AS A CYBER ATTACK INCIDENT"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.7 — "US DNI CLAYTON ON TECH OUTAGES: NOT SEEING THIS AS A CYBER ATTACK INCIDENT"
- TECH (Bio-Techne Corp) score 42.7 — "US DNI CLAYTON ON TECH OUTAGES: NOT SEEING THIS AS A CYBER ATTACK INCIDENT"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- IDBI.NS (IDBI BANK LIMITED) score 42.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- TGT (Target Corporation) score 34.1 — "Reliance, UltraTech, Hyundai Motor shares: Top 3 stocks to buy; check ratings, target pric"
- OHI (Omega Healthcare Investors, In) score 30.7 — "BTC $ANT - BITCOIN LOSSES MOUNT AS INVESTORS SHIFT ATTENTION TO ANTHROPIC IPO Bitcoin has "
- COIN (Coinbase Global, Inc.) score 27.2 — "GIFT City eyes global commodity trade; finance, liquidity could pose hurdles"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.8 — "Cuba’s Energy Crisis Turns Into a Goldmine for U.S. Fuel Exporters"
- 301077.SZ (CHINASTARS) score 21.9 — "In 45 Days Defense Giants Must Prove Their Magnets Are China-Free"
- LTH (Life Time Group Holdings, Inc.) score 20.5 — "NVDA - NVIDIA STOPS DISCLOSING SINGAPORE SALES AS REVENUE SURGES TO $104 BILLION Nvidia st"
- BLLN (BillionToOne, Inc.) score 20.0 — "NVDA - NVIDIA STOPS DISCLOSING SINGAPORE SALES AS REVENUE SURGES TO $104 BILLION Nvidia st"
- CHKP (Check Point Software Technolog) score 19.8 — "Reliance, UltraTech, Hyundai Motor shares: Top 3 stocks to buy; check ratings, target pric"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 15.9 — "‘It’s downright dirty’: My brother took over our ailing mother’s life and finances. What c"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.4 — "Tata Chemicals share price jumps 9%: Volume surge, Tata Sons listing buzz behind the Tata "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.4 — "Tata Chemicals share price jumps 9%: Volume surge, Tata Sons listing buzz behind the Tata "
- BOND (PIMCO Active Bond Exchange-Tra) score 14.8 — "BP launches offer to buy back up to $6 billion of bonds"
- JIOFIN.BO (Jio Financial Services Limited) score 13.8 — "NVDA - NVIDIA STOPS DISCLOSING SINGAPORE SALES AS REVENUE SURGES TO $104 BILLION Nvidia st"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.7 — "Why Silver rates crashed from record high of  ₹4 lakh per kg price to below  ₹1.75 lakh? E"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.3 — "‘It’s downright dirty’: My brother took over our ailing mother’s life and finances. What c"
- BZ=F (Brent Crude Oil Last Day Finan) score 8.9 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- MS (Morgan Stanley) score 8.9 — "JPMORGAN WARNS LEVERAGED-LOAN DEFAULTS COULD MORE THAN DOUBLE IN 2027 JPMorgan forecasts U"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.7 — "Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant"
- SCHD (Schwab US Dividend Equity ETF) score 6.7 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.2 — "Stock Market Live Updates | Opening Bell: Sensex gains over 200 pts, Nifty above 25,300; I"
- GS (Goldman Sachs Group, Inc. (The) score 4.4 — "GOLDMAN SACHS CUTS OIL PRICE FORECASTS FOR 2026 AND 2027 Goldman Sachs has lowered its Bre"
- META (Meta) score 4.2 — "Metal stock jumps 17%, inches close to 52-week high after this CAPEX update; will the rall"
- RS (Reliance, Inc.) score 4.1 — "Reliance, UltraTech, Hyundai Motor shares: Top 3 stocks to buy; check ratings, target pric"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 3.8 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- CRWV (CoreWeave, Inc.) score 3.6 — "CoreWeave’s stock pops — even as Nvidia talks up a ‘disciplined’ approach to financing"
- ETERNAL.NS (ETERNAL LIMITED) score 2.3 — "Eternal among 5 stocks hitting 52-week highs; stock rallies up to 15% in a month"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.1 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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