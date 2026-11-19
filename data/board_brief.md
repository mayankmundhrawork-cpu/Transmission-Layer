# Transmission Layer — board brief · 2026-11-19 12:57Z

data as of **2026-11-19** · 97 series · 12 red / 40 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.771, 4d in regime; vol-pct 0.875, breadth-off 0.667, Markov P(high-vol) 0.024)
- [INVERTED] **safe_haven_gold** — corr20 -0.06, corr60 -0.17, contra nifty_50 corr20=0.36, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-18. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.15, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.15, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.15, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.31, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0032821224683141637)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.51** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2012) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.438** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.36] cross-asset · 5 series ↓
- dow_jones [INDICES]: last 50193.03, z20 -3.43, zc -1.01, resid-z -1.69 [unexplained], 1d -1.12%, |z20|=3.43
- dyn_schd [EQUITIES]: last 34.69, z20 -2.22, zc -1.86, resid-z -2.35 [unexplained], 1d -1.76%, |z20|=2.22
- sp500 [INDICES]: last 7322.28, z20 -2.07, zc -0.21, resid-z -0.77 [quiet], 1d -0.25%, |z20|=2.07
- russell_2000 [INDICES]: last 2714.66, z20 -2.01, zc 0.34, resid-z 1.17 [quiet], 1d 0.47%, |z20|=2.01
- dyn_nvda [EQUITIES]: last 150.87, z20 -1.89, zc -0.89, resid-z 1.01 [quiet], 1d -2.95%, 1y-pct=0
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.755 vs dow_jones, historically leads by 1d
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.593 vs russell_2000, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.609 vs dow_jones
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.555 vs dyn_schd
- Source: Can Anthropic’s IPO do for the stock market what Nvidia’s earnings couldn’t? — MarketWatch Top, 2026-11-19. https://www.marketwatch.com/story/can-anthropics-ipo-do-for-the-stock-market-what-nvidias-earnings-couldnt-be67a434?mod=mw_rss_topstories
- Source: S&P 500 index 2027 target: 8200 mark expected by UBS - here's why; but AI-related uncertainties may limit further upside — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/sp-500-index-2027-target-8200-mark-expected-by-ubs-heres-why-but-ai-related-uncertainties-may-limit-further-up-11795066877862.html
- Source: Dividend record date, Nov 19: Last day to buy today to qualify- Oil India, Ashok Leyland, more - Who pays the highest? — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/dividend-record-date-nov-19-last-day-to-buy-today-to-qualify-oil-india-ashok-leyland-more-who-pays-the-highest-11795056567542.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-22 (d=0.91), 2025-05-16 (d=1.21)

### [RED 7.21] usd_inr ↓
- usd_inr [FX]: last 93.29, z20 -2.21, zc -0.46, resid-z -0.39 [quiet], 1d -0.20%, 20d range extreme; |z20|=2.21; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.445 via usd_inr, z 1.79, reacted); dyn_indianb_ns (rho -0.439 via usd_inr, z 1.51, reacted); nifty_it (rho -0.414 via usd_inr, z -3.05, reacted); dyn_tataelxsi_ns (rho -0.377 via usd_inr, z -0.93, quiet); dyn_bajfinance_ns (rho -0.35 via usd_inr, z 1.03, reacted)
- **India receivers**: dyn_havells_ns (rho -0.445, z 1.79); dyn_indianb_ns (rho -0.439, z 1.51); nifty_it (rho -0.414, z -3.05); dyn_tataelxsi_ns (rho -0.377, z -0.93)
- Source: Rupee extends rally to close 5 paise higher at 93.36 against US dollar — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/forex/rupee-extends-rally-to-close-5-paise-higher-at-9336-against-us-dollar/article71719784.ece
- Source: Stock rally keeps rupee upbeat, traders eye exporters for fresh fuel — ET Markets, 2026-11-19. https://economictimes.indiatimes.com/markets/forex/forex-news/india-rupee-stock-rally-keeps-rupee-upbeat-traders-eye-exporters-for-fresh-fuel/articleshow/135986825.cms
- Source: Rupee slides 8 paise to 93.49 against US dollar in early trade — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/forex/rupee-slides-8-paise-to-9349-against-us-dollar-in-early-trade/article71718647.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.26] brent ↓
- brent [COMMODITIES]: last 90.12, z20 -1.26, zc -0.82, resid-z -0.78 [quiet], 1d -1.99%, 1-session move -1.99% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (co-move) — not yet - watch; rho 0.559 vs brent, historically leads by 1d
- Source: India’s Oil Imports Hit Record High as Saudi Shipments Surge — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/Indias-Oil-Imports-Hit-Record-High-as-Saudi-Shipments-Surge.html
- Source: India’s crude oil demand to grow at 3% annually till 2035: IEA — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/commodities/indias-crude-oil-demand-to-grow-at-3-annually-till-2035-iea/article71719490.ece
- Source: The Middle East War Has Wiped 2.8 Billion Barrels Off Global Oil Supply — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/The-Middle-East-War-Has-Wiped-28-Billion-Barrels-Off-Global-Oil-Supply.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 6.04] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3716.80, z20 -2.72, zc -0.33, resid-z 0.21 [quiet], 1d -0.67%, |z20|=2.72; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 44.99, z20 -2.35, zc -0.00, resid-z 0.79 [quiet], 1d -0.01%, |z20|=2.35; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 82.60, z20 1.83, zc n/a, resid-z n/a [quiet], 1d -0.66%, |z20|=1.83; 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.532 via comex_gold, z -0.06, quiet); dyn_karurvysya_ns (rho 0.47 via comex_gold, z 1.19, reacted); nifty_metal (rho 0.437 via comex_silver, z 0.22, quiet); dyn_jiofin_bo (rho 0.402 via comex_gold, z 0.8, quiet); nifty_midcap_100 (rho 0.379 via comex_gold, z 1.16, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.532 vs comex_gold, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.532, z -0.06); dyn_karurvysya_ns (rho 0.47, z 1.19); nifty_metal (rho 0.437, z 0.22); dyn_jiofin_bo (rho 0.402, z 0.8)
- Source: 15% fall in gold prices could trigger panic, warn lenders — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/gold/15-fall-in-gold-prices-could-trigger-panic-warn-lenders/article71719017.ece
- Source: Today’s Gold Rate in India, November 19: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-19-2026/article71719289.ece
- Source: Today’s Gold Rate in India November 19: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-19-2026/article71719290.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.88] cross-asset · 2 series ↓
- nifty_it [INDICES]: last 30919.45, z20 -3.05, zc -0.74, resid-z -1.34 [quiet], 1d -1.10%, |z20|=3.05
- dyn_techm_ns [EQUITIES]: last 1723.00, z20 -2.91, zc -0.98, resid-z -1.28 [quiet], 1d -1.54%, |z20|=2.91
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.674 via nifty_it, z -0.93, quiet); nifty_50 (rho 0.494 via nifty_it, z 1.38, reacted); dyn_justdial_bo (rho 0.444 via dyn_techm_ns, z -0.91, quiet); dyn_indianb_ns (rho 0.443 via nifty_it, z 1.51, reacted); usd_inr (rho -0.414 via nifty_it, z -2.21, reacted)
- Watch next: dyn_tataelxsi_ns (co-move) — not yet - watch; rho 0.674 vs nifty_it, historically leads by 1d
- **India receivers**: dyn_tataelxsi_ns (rho 0.674, z -0.93); nifty_50 (rho 0.494, z 1.38); dyn_justdial_bo (rho 0.444, z -0.91); dyn_indianb_ns (rho 0.443, z 1.51)
- Source: SML Mahindra offers shares at 37% discount as M&M steps up CV expansion — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/sml-mahindra-offers-shares-at-36-discount-as-mm-steps-up-cv-expansion/article71714724.ece
- Source: SML Mahindra offers shares at 36% discount as M&M steps up CV expansion — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/sml-mahindra-offers-shares-at-36-discount-as-mm-steps-up-cv-expansion/article71714724.ece
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.44] dyn_blln ↓
- dyn_blln [EQUITIES]: last 91.61, z20 -3.44, zc -1.80, resid-z 0.27 [moved], 1d -6.04%, |z20|=3.44
- **Mechanism**: dyn_blln ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Tata Tech shares jump 10% as company targets $1.3 billion revenue by FY30, bets on aerospace, industrial machinery — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/tata-tech-shares-jump-10-as-company-targets-1-3-billion-revenue-by-fy30-bets-on-aerospace-industrial-machinery-11795077108823.html
- Source: The Middle East War Has Wiped 2.8 Billion Barrels Off Global Oil Supply — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/The-Middle-East-War-Has-Wiped-28-Billion-Barrels-Off-Global-Oil-Supply.html
- Source: Anthropic IPO breaks all records, even SpaceX! What $81.3 billion means for India's IT and AI stocks? Experts decode — Mint Markets, 2026-11-19. https://www.livemint.com/market/ipo/anthropic-ipo-breaks-all-records-even-spacex-what-81-3-billion-means-for-indias-it-and-ai-stocks-experts-decode-11795075165072.html

### [AMBER 5.38] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 110.54, z20 -2.06, zc -0.84, resid-z -0.27 [quiet], 1d -3.90%, |z20|=2.06; 1y-pct=0
- btc_usd [CRYPTO]: last 63804.60, z20 -1.78, zc 0.46, resid-z -1.12 [quiet], 1d 1.30%, |z20|=1.78
- eth_usd [CRYPTO]: last 1802.90, z20 -1.60, zc 0.41, resid-z -0.59 [quiet], 1d 1.59%, |z20|=1.60
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.504 vs dyn_coin, historically leads by 2d
- Source: Global Cooling Demand Overtakes Heating for the First Time — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/Global-Cooling-Demand-Overtakes-Heating-for-the-First-Time.html
- Source: The Middle East War Has Wiped 2.8 Billion Barrels Off Global Oil Supply — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/The-Middle-East-War-Has-Wiped-28-Billion-Barrels-Off-Global-Oil-Supply.html
- Source: Goldman Sachs sees global equities rallying in 2027, forecasts up to 24% returns — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/goldman-sachs-sees-global-equities-rallying-in-2027-forecasts-up-to-24-returns/article71718728.ece
- Historical analogues: 2025-10-22 (d=0.34), 2025-03-31 (d=0.47), 2025-10-30 (d=0.52)

### [RED 5.14] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 704.00, z20 3.14, zc 3.79, resid-z 2.94 [unexplained], 1d 7.20%, |z20|=3.14
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.533 via dyn_tatatech_ns, z 0.8, quiet); dyn_indusindbk_bo (rho 0.516 via dyn_tatatech_ns, z 1.33, reacted); nifty_midcap_100 (rho 0.491 via dyn_tatatech_ns, z 1.16, reacted); dyn_tataelxsi_ns (rho 0.467 via dyn_tatatech_ns, z -0.93, quiet); dyn_indianb_ns (rho 0.452 via dyn_tatatech_ns, z 1.51, reacted)
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.533 vs dyn_tatatech_ns, historically leads by 1d
- **India receivers**: dyn_jiofin_bo (rho 0.533, z 0.8); dyn_indusindbk_bo (rho 0.516, z 1.33); nifty_midcap_100 (rho 0.491, z 1.16); dyn_tataelxsi_ns (rho 0.467, z -0.93)
- Source: Tata Tech shares jump 10% as company targets $1.3 billion revenue by FY30, bets on aerospace, industrial machinery — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/tata-tech-shares-jump-10-as-company-targets-1-3-billion-revenue-by-fy30-bets-on-aerospace-industrial-machinery-11795077108823.html
- Source: Tata Chemicals among 4 stocks that show RSI Trending Up — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/stocks/news/tata-chemicals-among-4-stocks-that-show-rsi-trending-up/slideshow/135948695.cms
- Source: Tata Motors among 5 stocks closing above 200-DMA — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/stocks/news/tata-motors-among-5-stocks-closing-above-200-dma/slideshow/135947686.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
fx · 2 series ↓ (5.08), comex_copper ↓ (4.73), dyn_301077_sz ↑ (4.41), dyn_tgt ↑ (3.75), hang_seng ↓ (3.43), dyn_lth ↑ (3.41), dyn_inoxindia_ns ↑ (3.36), dyn_eternal_ns ↑ (3.02), ftse_100 ↓ (2.81), dyn_4417_t ↑ (2.73), rates · 2 series ↑ (2.69), dyn_crwv ↓ (2.66)

## India macro
- nifty_50: 25514.3008 (1d 1.14%, z20 1.38, flag none)
- nifty_midcap_100: 61618.8516 (1d 1.06%, z20 1.16, flag none)
- usd_inr: 93.2900 (1d -0.20%, z20 -2.21, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4151 (1d -0.08%, z20 -1.63, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 99.0 — "Mahanadi Coalfields IPO GMP today at  ₹3 vs  ₹136 price band - Should you apply for Coal I"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.7 — "Mahanadi Coalfields IPO GMP today at  ₹3 vs  ₹136 price band - Should you apply for Coal I"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.6 — "Mahanadi Coalfields IPO GMP today at  ₹3 vs  ₹136 price band - Should you apply for Coal I"
- INDIANB.NS (INDIAN BANK) score 57.6 — "Anthropic’s rise to $1.5 trillion puts Indian companies’ competitiveness in focus: Uday Ko"
- NVDA (NVIDIA Corporation) score 57.0 — "Can Anthropic’s IPO do for the stock market what Nvidia’s earnings couldn’t?"
- BAC (Bank of America Corporation) score 49.2 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- HDB (HDFC Bank Limited) score 44.2 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.0 — "Sterlite Technologies among 3 stocks showing White Marubozu pattern"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.0 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- IDBI.NS (IDBI BANK LIMITED) score 41.0 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.0 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.7 — "Sterlite Technologies among 3 stocks showing White Marubozu pattern"
- TECH (Bio-Techne Corp) score 38.7 — "Sterlite Technologies among 3 stocks showing White Marubozu pattern"
- TGT (Target Corporation) score 37.3 — "S&P 500 index 2027 target: 8200 mark expected by UBS - here's why; but AI-related uncertai"
- OHI (Omega Healthcare Investors, In) score 34.7 — "Mahanadi Coalfields raises ₹2,295 crore from anchor investors ahead of IPO"
- COIN (Coinbase Global, Inc.) score 28.0 — "Goldman Sachs sees global equities rallying in 2027, forecasts up to 24% returns"
- 301077.SZ (CHINASTARS) score 24.6 — "China Coking Coal Hits Three-Month Low as Supply Recovers"
- BLLN (BillionToOne, Inc.) score 22.7 — "Anthropic IPO breaks all records, even SpaceX! What $81.3 billion means for India's IT and"
- CHKP (Check Point Software Technolog) score 22.4 — "Gold Rates Live Updates: Gold prices fall marginally, silver gains on MCX. Check future es"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.0 — "EU Delays Methane Rules by Two Years Amid Energy Supply Fears"
- LTH (Life Time Group Holdings, Inc.) score 21.3 — "Global Cooling Demand Overtakes Heating for the First Time"
- JIOFIN.BO (Jio Financial Services Limited) score 17.8 — "Stocks to watch, Nov 19: Jio Financial, Bharat Forge, LT Foods, National Aluminium, Dalmia"
- BOND (PIMCO Active Bond Exchange-Tra) score 17.2 — "Corporate loan book to slow as companies tap bond markets on higher EBLR rates"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 16.6 — "IIFL Finance shares drop over 3% after Fairfax pared over 13% stake"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.7 — "Tata Tech shares jump 10% as company targets $1.3 billion revenue by FY30, bets on aerospa"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.7 — "Tata Tech shares jump 10% as company targets $1.3 billion revenue by FY30, bets on aerospa"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.8 — "Why gold, silver prices are going down? What experts say about rate fall - More plunge ahe"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.5 — "IIFL Finance shares drop over 3% after Fairfax pared over 13% stake"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "This closely watched investing guru just sold all of his stocks"
- MS (Morgan Stanley) score 8.4 — "Morgan Stanley is ‘overweight’ on these 9 largecap stocks. How many do you own?"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.5 — "Dividend record date, Nov 19: Last day to buy today to qualify- Oil India, Ashok Leyland, "
- META (Meta) score 6.3 — "GOLD, SILVER AND COPPER PLUNGE AS METALS SELLOFF ACCELERATES Precious and industrial metal"
- GS (Goldman Sachs Group, Inc. (The) score 6.0 — "Goldman Sachs sees global equities rallying in 2027, forecasts up to 24% returns"
- SCHD (Schwab US Dividend Equity ETF) score 5.8 — "Dividend record date, Nov 19: Last day to buy today to qualify- Oil India, Ashok Leyland, "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.4 — "Adani Ent Share Price Highlights: Adani Ent. Stock Price History"
- RS (Reliance, Inc.) score 4.0 — "Reliance Industries shares: After 13% surge in 1 month, JPMorgan sees another 23% upside i"
- ETERNAL.NS (ETERNAL LIMITED) score 3.7 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.8 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- CRWV (CoreWeave, Inc.) score 2.6 — "CoreWeave’s stock pops — even as Nvidia talks up a ‘disciplined’ approach to financing"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.8 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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