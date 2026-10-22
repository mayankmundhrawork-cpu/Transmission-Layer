# Transmission Layer — board brief · 2026-10-22 00:04Z

data as of **2026-10-22** · 97 series · 13 red / 31 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.716, 13d in regime; vol-pct 0.727, breadth-off 0.706, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.21, corr60 -0.37, contra nifty_50 corr20=0.41, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.82, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-27. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.13, corr60 0.09, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.2, corr60 -0.26, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.49, corr60 0.22, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 88** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.256, β 0.1946, p 0.00958); driver zc 1.59 → expected 0.258%. Type hit-rate 0.819 (n=1918).
- **SETUP** dax → asx_200: leads 1d (ccf 0.253, β 0.1833, p 0.00599); driver zc 1.52 → expected 0.248%. Type hit-rate 0.819 (n=1918).
- Track record · residual_reversion: hit-rate **0.495** (n=1104) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=1918) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.31] natgas ↓
- natgas [COMMODITIES]: last 2.78, z20 -3.31, zc -1.88, resid-z -2.60 [unexplained], 1d -6.28%, 1-session move -6.28% ≥ 5.0%; |z20|=3.31
- **Mechanism**: natgas ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.075 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.073 vs natgas, historically leads by 4d
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.04 vs natgas, historically leads by 4d
- Source: Asian LNG Prices Surge Past $30 as Middle East Shipping Risks Escalate — OilPrice, 2026-10-20. https://oilprice.com/Latest-Energy-News/World-News/Asian-LNG-Prices-Surge-Past-30-as-Middle-East-Shipping-Risks-Escalate.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 7.3] usd_inr ↓
- usd_inr [FX]: last 94.45, z20 -2.30, zc -1.08, resid-z -1.37 [quiet], 1d -0.57%, 20d range extreme; |z20|=2.30
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.382 via usd_inr, z -1.98, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.382, z -1.98)
- Source: Rupee rises 46 paise to 94.45 on India-US trade deal hopes; oil prices cap gains — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-46-paise-to-94-45-on-india-us-trade-deal-hopes-oil-prices-cap-gains/articleshow/135092741.cms
- Source: Jio Platforms' IPO-linked inflows boost rupee; elevated oil prices spur caution — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/forex/forex-news/jio-platforms-ipo-linked-inflows-boost-rupee-elevated-oil-prices-spur-caution/articleshow/135089592.cms
- Source: IMF advises India to let rupee move as first defence amid oil shock — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/economy/imf-advises-india-to-let-rupee-move-as-first-defence-amid-oil-shock/article71607130.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.85] commodities · 2 series ↑
- brent [COMMODITIES]: last 110.06, z20 1.95, zc 0.59, resid-z 0.76 [quiet], 1d 1.17%, |z20|=1.95; 1y-pct=96
- wti [COMMODITIES]: last 98.04, z20 1.02, zc -1.52, resid-z -1.20 [moved], 1d -3.68%, 1-session move -3.68% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.552 vs brent, historically leads by 5d
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.382 vs wti, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.523 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.51 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.504 vs brent
- Source: Big Oil Eyes Record Profits but Keeps Spending in Check — OilPrice, 2026-10-21. https://oilprice.com/Energy/Energy-General/Big-Oil-Eyes-Record-Profits-but-Keeps-Spending-in-Check.html
- Source: Oil is now flowing out of the Persian Gulf like before the Iran war. Why prices may still not come down anytime soon. — MarketWatch Top, 2026-10-21. https://www.marketwatch.com/story/oil-is-now-flowing-out-of-the-persian-gulf-like-before-the-iran-war-why-prices-may-still-not-come-down-anytime-soon-56df2f48?mod=mw_rss_topstories
- Source: Treasuries Slide After Middle East Strife Report Spurs Oil Gains — Mint Markets, 2026-10-21. https://www.livemint.com/market/treasuries-slide-after-middle-east-strife-report-spurs-oil-gains-11792613769755.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.63] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1834.70, z20 3.31, zc -0.20, resid-z 0.71 [quiet], 1d 3.13%, |z20|=3.31; 1y-pct=100
- nifty_it [INDICES]: last 32422.50, z20 2.87, zc -0.63, resid-z 0.27 [quiet], 1d 2.88%, |z20|=2.87
- dyn_tataelxsi_ns [EQUITIES]: last 3848.60, z20 2.28, zc -0.61, resid-z 0.38 [quiet], 1d 1.55%, |z20|=2.28
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.52 via dyn_tataelxsi_ns, z -0.02, quiet); dyn_justdial_bo (rho 0.511 via nifty_it, z 4.18, reacted); nifty_fmcg (rho 0.488 via dyn_tataelxsi_ns, z -1.74, reacted); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -3.36, reacted); dyn_tatatech_ns (rho 0.404 via nifty_it, z -1.22, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.51 vs nifty_it
- **India receivers**: nifty_50 (rho 0.52, z -0.02); dyn_justdial_bo (rho 0.511, z 4.18); nifty_fmcg (rho 0.488, z -1.74); midcap_largecap_ratio (rho -0.439, z -3.36)
- Source: Mahindra Finance Q2 net profit surges 55% to Rs 882 crore on volumes, lower credit cost — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-finance-q2-net-profit-surges-55-to-rs-882-crore-on-volumes-lower-credit-cost/articleshow/135094556.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 6.18] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 765.15, z20 4.18, zc 0.82, resid-z 1.21 [quiet], 1d 4.45%, |z20|=4.18
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.511 via dyn_justdial_bo, z 2.87, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.31, reacted); nifty_50 (rho 0.45 via dyn_justdial_bo, z -0.02, quiet); dyn_tataelxsi_ns (rho 0.395 via dyn_justdial_bo, z 2.28, reacted)
- **India receivers**: nifty_it (rho 0.511, z 2.87); dyn_techm_ns (rho 0.505, z 3.31); nifty_50 (rho 0.45, z -0.02); dyn_tataelxsi_ns (rho 0.395, z 2.28)
- Source: Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss by Anand Rathi's expert — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-short-term-just-dial-bse-orient-hotels-target-price-stop-loss-by-anand-rathis-expert-11792400725179.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [AMBER 5.45] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 57568.75, z20 -1.79, zc -1.05, resid-z -0.66 [quiet], 1d -1.56%, |z20|=1.79
- india_vix [INDICES]: last 15.71, z20 1.58, zc 0.85, resid-z n/a [quiet], 1d 6.38%, |z20|=1.58
- dyn_jiofin_bo [EQUITIES]: last 211.50, z20 -1.21, zc -0.77, resid-z 0.39 [quiet], 1d -1.03%, 1y-pct=0
- dyn_policybzr_ns [EQUITIES]: last 1008.00, z20 -0.53, zc -1.55, resid-z 0.14 [moved], 1d -2.61%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-07 (z-distance 0.4).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.755 via india_vix, z -0.02, quiet); nifty_metal (rho 0.632 via nifty_midcap_100, z -1.42, reacted); dyn_bajfinance_ns (rho -0.629 via india_vix, z -2.1, reacted); nifty_fmcg (rho 0.591 via nifty_midcap_100, z -1.74, reacted); dyn_indusindbk_bo (rho -0.558 via india_vix, z -1.44, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.71 vs nifty_midcap_100
- **India receivers**: nifty_50 (rho -0.755, z -0.02); nifty_metal (rho 0.632, z -1.42); dyn_bajfinance_ns (rho -0.629, z -2.1); nifty_fmcg (rho 0.591, z -1.74)
- Source: L&T Tech Services shares surge 15% after Q2 2026 results - Should investors buy, sell, or hold stock? Experts suggestion — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/lt-tech-services-shares-surge-15-after-q2-results-should-investors-buy-sell-or-hold-the-stock-experts-suggest-11792556660824.html
- Source: US Stocks: GE Aerospace raises 2026 profit forecast as services strength drives growth — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-ge-aerospace-raises-2026-profit-forecast-as-services-strength-drives-growth/articleshow/135068763.cms
- Historical analogues: 2025-07-07 (d=0.4), 2025-07-16 (d=0.44), 2025-12-31 (d=0.7)

### [RED 5.33] dyn_wit ↑
- dyn_wit [EQUITIES]: last 2.15, z20 3.33, zc 1.25, resid-z -0.06 [quiet], 1d 4.88%, |z20|=3.33
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who leads the Q2 results 2026 race? — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/it-mid-caps-vs-large-caps-tcs-infosys-wipro-vs-persistent-coforge-tata-tech-who-leads-the-q2-results-2026-race-11792600156200.html
- Source: Market Trading Guide: Wipro among 5 stock recommendations for Thursday — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-wipro-among-5-stock-recommendations-for-thursday/slideshow/135095527.cms
- Source: Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - Check stop loss, targets — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/top-2-stocks-to-buy-or-sell-for-short-term-wipro-dixon-technologies-by-nagaraj-shetti-check-stop-loss-targets-11792580012562.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [RED 5.23] dow_jones ↑
- dow_jones [INDICES]: last 52851.78, z20 3.23, zc 0.83, resid-z 0.74 [quiet], 1d 0.68%, |z20|=3.23
- **Mechanism**: dow_jones ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.717 vs dow_jones, historically leads by 1d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.879 vs dow_jones
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.65 vs dow_jones, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.591 vs dow_jones, historically leads by 4d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.579 vs dow_jones, historically leads by 5d
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq surges at open as SpaceX, SuperMicro results lift AI stocks — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-ai-stocks-spacex-super-micro-tesla-netflix-fed-rate-hike-treasury-yields-stock-price-news-21st-september-2026/liveblog/135092299.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq surges 1% as SpaceX, AI stocks rise while Netflix slips — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-ai-stocks-spacex-super-micro-tesla-netflix-fed-rate-hike-treasury-yields-stock-price-news-21st-september-2026/liveblog/135092299.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: Nasdaq leads Wall Street higher as SpaceX, Super Micro lift AI sentiment — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-ai-stocks-spacex-super-micro-tesla-netflix-fed-rate-hike-treasury-yields-stock-price-news-21st-september-2026/liveblog/135092299.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-28 (d=0.1), 2025-08-22 (d=0.11)

## Watchlist (below surfacing floor)
commodities · 3 series ↓ (4.41), dyn_chkp ↑ (4.32), dyn_rs ↑ (4.28), dyn_4417_t ↑ (4.1), dyn_bajfinance_ns ↓ (4.1), dyn_tech ↑ (4.06), gold_silver_ratio ↑ (3.94), usd_cny ↓ (3.82), gbp_usd ↑ (3.4), tips_10y_real ↓ (3.36), midcap_largecap_ratio ↓ (3.36), dyn_inoxindia_ns ↓ (3.08)

## India macro
- nifty_50: 22811.3496 (1d -0.34%, z20 -0.02, flag none)
- nifty_midcap_100: 57568.7500 (1d -1.56%, z20 -1.79, flag amber)
- usd_inr: 94.4500 (1d -0.57%, z20 -2.30, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5237 (1d -1.23%, z20 -3.36, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.5 — "India’s Top State Refiner to Reduce Middle East Term Oil Purchases"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.3 — "India’s Top State Refiner to Reduce Middle East Term Oil Purchases"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.1 — "India’s Top State Refiner to Reduce Middle East Term Oil Purchases"
- INDIANB.NS (INDIAN BANK) score 77.6 — "SPCX - JPMORGAN DOUBLES SPACEX PRICE TARGET TO $500 JPMorgan raised its SpaceX price targe"
- BAC (Bank of America Corporation) score 68.6 — "SPCX - JPMORGAN DOUBLES SPACEX PRICE TARGET TO $500 JPMorgan raised its SpaceX price targe"
- HDB (HDFC Bank Limited) score 61.8 — "SPCX - JPMORGAN DOUBLES SPACEX PRICE TARGET TO $500 JPMorgan raised its SpaceX price targe"
- IDBI.NS (IDBI BANK LIMITED) score 59.5 — "SPCX - JPMORGAN DOUBLES SPACEX PRICE TARGET TO $500 JPMorgan raised its SpaceX price targe"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.5 — "SPCX - JPMORGAN DOUBLES SPACEX PRICE TARGET TO $500 JPMorgan raised its SpaceX price targe"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 59.5 — "SPCX - JPMORGAN DOUBLES SPACEX PRICE TARGET TO $500 JPMorgan raised its SpaceX price targe"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.7 — "IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who lea"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.4 — "IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who lea"
- TECH (Bio-Techne Corp) score 52.4 — "IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who lea"
- OHI (Omega Healthcare Investors, In) score 52.1 — "Tesla’s stock falls as Elon Musk leaves investors wanting more"
- COIN (Coinbase Global, Inc.) score 50.1 — "S&P Global Warns Hormuz Energy Shock Could Become a Global Food Crisis"
- CHKP (Check Point Software Technolog) score 40.6 — "Big Oil Eyes Record Profits but Keeps Spending in Check"
- TGT (Target Corporation) score 37.7 — "SpaceX’s massive AI targets will test the limits of reality"
- RS (Reliance, Inc.) score 31.7 — "IPO GMP race: Reliance Jio Platforms IPO vs Paras Healthcare IPO - Check grey market winne"
- BOND (PIMCO Active Bond Exchange-Tra) score 31.7 — "YIELD ON 20-YR U.S. TREASURY BOND PARES DECLINE AFTER $13 BLN AUCTION, LAST DOWN 1.25 BASI"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.3 — "S&P Global Warns Hormuz Energy Shock Could Become a Global Food Crisis"
- LTH (Life Time Group Holdings, Inc.) score 24.7 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: Nasdaq leads Wall Street"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 23.4 — "Trump says data centers should generate their own electricity — but experts say only state"
- 301077.SZ (CHINASTARS) score 22.4 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.7 — "Market wrap: Infosys, HCL Tech, Bajaj Finance, BSE top gainers and losers on Nifty and Sen"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.0 — "Market wrap: Infosys, HCL Tech, Bajaj Finance, BSE top gainers and losers on Nifty and Sen"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.7 — "YIELD ON 20-YR U.S. TREASURY BOND PARES DECLINE AFTER $13 BLN AUCTION, LAST DOWN 1.25 BASI"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.2 — "TSLA - TESLA BEATS EARNINGS AS CASH FLOW SMASHES EXPECTATIONS Tesla delivered a mixed Q3, "
- META (Meta) score 14.2 — "META - META MUST PAY $25 BILLION IN PENALTIES, NEW MEXICO JUDGE RULES AFTER JURY FOUND COM"
- JIOFIN.BO (Jio Financial Services Limited) score 14.1 — "Jio IPO strengthens Reliance’s financial flexibility; capex funding remains key: Moody’s"
- SEPN (Septerna, Inc.) score 12.2 — "Global Market: UK inflation rises to 3.5% in September, boosting rate hike bets"
- GS (Goldman Sachs Group, Inc. (The) score 11.0 — "Goldman Sachs Warns of New Oil Price Shock as Tanker Rates Soar"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.0 — "IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who lea"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.0 — "IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who lea"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.5 — "Adani Green Q2 Results: Profit rises 15% YoY to Rs 673 crore; revenue jumps 39%"
- JEF (Jefferies Financial Group Inc.) score 8.3 — "UltraTech Cement shares jump 3% as brokerages revise target prices after Q2 results. What "
- VT (Vanguard Total World Stock Ind) score 7.6 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- NVDA (NVIDIA Corporation) score 7.1 — "NVIDIA MAY ALSO BE A BIDDER FOR AMBARELLA ( $AMBA ) - BETAVILLE"
- WIT (Wipro Limited) score 6.1 — "Market Trading Guide: Wipro among 5 stock recommendations for Thursday"
- GOLDCASE.BO (Zerodha Mutual Fund) score 2.7 — "Zerodha launches US stock investing: How to invest in Tesla, Amazon, SpaceX, Meta, Micron,"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.6 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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