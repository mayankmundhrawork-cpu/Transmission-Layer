# Transmission Layer — board brief · 2026-09-16 14:57Z

data as of **2026-09-16** · 97 series · 12 red / 40 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.655, 5d in regime; vol-pct 0.546, breadth-off 0.765, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.55, corr60 -0.32, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.32, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.11, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.84, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.04, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-07-23. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.17, corr60 0.16, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0013742758758317208)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2084) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.35] cross-asset · 9 series ↑
- tips_10y_real [RATES]: last 2.60, z20 2.73, zc 0.00, resid-z -0.81 [quiet], 1d 0.00%, |z20|=2.73; 1y-pct=99
- ust_2y [RATES]: last 4.65, z20 2.64, zc 0.33, resid-z -0.45 [quiet], 1d 0.43%, |z20|=2.64; 1y-pct=100
- ust_10y [RATES]: last 4.97, z20 2.55, zc 0.20, resid-z -0.34 [quiet], 1d 0.20%, |z20|=2.55; 1y-pct=100
- dow_jones [INDICES]: last 52025.07, z20 -2.00, zc -0.16, resid-z -1.44 [quiet], 1d -0.13%, |z20|=2.00
- russell_2000 [INDICES]: last 2878.77, z20 -1.77, zc 0.25, resid-z -0.02 [quiet], 1d 0.30%, |z20|=1.77
- ust_30y [RATES]: last 5.34, z20 1.73, zc -0.24, resid-z -0.58 [quiet], 1d -0.19%, |z20|=1.73; 1y-pct=99
- wti [COMMODITIES]: last 102.77, z20 1.71, zc -0.91, resid-z -0.91 [quiet], 1d -2.89%, 1-session move -2.89% ≥ 1.5%; |z20|=1.71; 1y-pct=95
- brent [COMMODITIES]: last 106.27, z20 1.62, zc -0.78, resid-z -0.71 [quiet], 1d -2.28%, 1-session move -2.28% ≥ 1.5%; |z20|=1.62; co-occur[inr_oil] suppressed: channel WEAK
- dyn_bond [EQUITIES]: last 88.93, z20 -1.53, zc 0.90, resid-z -0.01 [quiet], 1d 0.30%, 1y-pct=1
- **Mechanism**: cross-asset · 9 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.399 via ust_2y, z -1.69, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.565 vs dow_jones, historically leads by 1d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.554 vs russell_2000
- **India receivers**: midcap_largecap_ratio (rho -0.399, z -1.69)
- Source: U.S. Oil Inventories Edge Lower as Fuel Demand Softens — OilPrice, 2026-09-16. https://oilprice.com/Energy/Crude-Oil/US-Oil-Inventories-Edge-Lower-as-Fuel-Demand-Softens.html
- Source: What history says about longer-term bond yields after an initial Fed hike — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/what-history-says-about-longer-term-bond-yields-after-the-first-fed-hike-53eaae9f?mod=mw_rss_topstories
- Source: Gold, silver prices rise on bargain buying, dip in crude oil rates — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/gold/gold-silver-prices-rise-on-bargain-buying-dip-in-crude-oil-rates/article71472584.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.68), 2025-10-06 (d=0.74)

### [RED 6.61] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 60879.15, z20 -2.95, zc 0.01, resid-z -0.76 [quiet], 1d 0.01%, |z20|=2.95
- india_vix [INDICES]: last 13.14, z20 2.79, zc -0.38, resid-z n/a [quiet], 1d -2.16%, |z20|=2.79
- dyn_jiofin_bo [EQUITIES]: last 225.00, z20 -2.40, zc -0.32, resid-z -1.09 [quiet], 1d -0.44%, |z20|=2.40; 1y-pct=0
- nifty_50 [INDICES]: last 23217.60, z20 -2.11, zc 0.78, resid-z 0.50 [quiet], 1d 0.43%, |z20|=2.11
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.617 via nifty_50, z -0.92, quiet); dyn_indianb_ns (rho 0.559 via nifty_midcap_100, z -2.16, reacted); nifty_it (rho 0.53 via nifty_50, z -1.64, reacted); dyn_techm_ns (rho 0.516 via nifty_50, z -0.8, quiet); midcap_largecap_ratio (rho -0.437 via nifty_50, z -1.69, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.617 vs nifty_50, historically leads by 3d
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.516 vs nifty_50, historically leads by 3d
- **India receivers**: nifty_fmcg (rho 0.617, z -0.92); dyn_indianb_ns (rho 0.559, z -2.16); nifty_it (rho 0.53, z -1.64); dyn_techm_ns (rho 0.516, z -0.8)
- Source: Fed watch freezes Dalal Street; Nifty ekes out modest gains after brutal sell-off — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/fed-watch-freezes-dalal-street-nifty-ekes-out-modest-gains-after-brutal-sell-off/article71472309.ece
- Source: Market wrap: SBI, HDFC Life, TCS, Infosys top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-sbi-hdfc-life-tcs-infosys-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134286572.cms
- Source: Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FMCG, PSU banks outperform — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-16th-september-2026/article71468722.ece
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [AMBER 6.35] usd_inr ↑
- usd_inr [FX]: last 95.94, z20 1.35, zc 0.19, resid-z 0.27 [quiet], 1d 0.11%, 20d range extreme; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Rupee languishes at six-week low ahead of Fed outcome, RBI limits losses — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/forex/rupee-languishes-at-six-week-low-ahead-of-fed-outcome-rbi-limits-losses/articleshow/134284941.cms
- Source: Rupee falls 3 paise to 95.91 against US dollar in early trade — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/forex/rupee-falls-3-paise-to-9591-against-us-dollar-in-early-trade/article71471039.ece
- Source: Rupee expected to stay under pressure with likely Fed rate hike adding to strain from high oil prices — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/forex/rupee-expected-to-stay-under-pressure-with-likely-fed-rate-hike-adding-to-strain-from-high-oil-prices/article71470982.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 5.27] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5430.00, z20 3.27, zc 0.52, resid-z 3.20 [unexplained], 1d 2.45%, |z20|=3.27; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Borosil Renewables' entry into the solar rooftop sector a significant positive, shares may see an upswing, say experts — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/borosil-renewables-entry-into-the-solar-rooftop-sector-a-significant-positive-shares-may-see-an-upswing-say-experts-11789552595550.html
- Source: Zee Entertainment shares surge 8% after 4-day losses; can it rise more? Experts decode — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/zee-entertainment-shares-surge-8-after-4-day-losses-can-it-rise-more-experts-decode-11789540738234.html
- Source: ITC shares edge higher after rise in select cigarette brands, experts see 10% rally in short term | Target, outlook — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/itc-shares-edge-higher-after-rise-in-select-cigarette-brands-experts-see-10-rally-in-short-term-target-outlook-11789536356887.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 5.23] dyn_bac ↓
- dyn_bac [EQUITIES]: last 58.69, z20 -3.23, zc -0.78, resid-z -4.20 [unexplained], 1d -1.40%, |z20|=3.23
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho 0.371 via dyn_bac, z 0.32, quiet)
- **India receivers**: eur_inr (rho 0.371, z 0.32)
- Source: 5% Treasury yields mean America’s debt bill just got a lot bigger — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/5-treasury-yields-mean-americas-debt-bill-just-got-a-lot-bigger-8a5702b0?mod=mw_rss_topstories
- Source: WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expects the Federal Reserve to raise rates in September, according to a WSJ survey. Most forecast 50 basis points of total tightening in 2026, while Bank of America, Deutsche Bank and RBC see 75bps. Market angle: exp — DeItaone, 2026-09-15. https://t.me/walter_bloomberg/35811
- Source: The 10 most overvalued housing markets in America — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-10-most-overvalued-housing-markets-in-america-6d28efdf?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.37] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 748.40, z20 -2.37, zc -0.73, resid-z -0.78 [quiet], 1d -1.44%, |z20|=2.37
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.565 via dyn_tatatech_ns, z -1.64, reacted); dyn_tataelxsi_ns (rho 0.47 via dyn_tatatech_ns, z -1.73, reacted); dyn_techm_ns (rho 0.457 via dyn_tatatech_ns, z -0.8, quiet)
- **India receivers**: nifty_it (rho 0.565, z -1.64); dyn_tataelxsi_ns (rho 0.47, z -1.73); dyn_techm_ns (rho 0.457, z -0.8)
- Source: Tata Group stocks fall up to 7% after Tuesday’s IPO-buzz rally. Which stocks led the losses? — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/tata-group-stocks-fall-up-to-7-after-tuesdays-ipo-buzz-rally-which-stocks-led-the-losses/articleshow/134281314.cms
- Source: RIL, HUL, Nestle, Tata Consumer, Hyundai shares on the rise today | Key things to know — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/ril-hul-nestle-tata-consumer-muthoot-hyundai-shares-on-the-rise-today-key-things-to-know-11789539484574.html
- Source: Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, Blue Star, Allen Blenders, Tata Communications, Mazagon Dock — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/buzzing-stocks-for-sept-16-bharat-forge-titagarh-rail-bhel-cochin-shipyard-thermax-blue-star-allen-blenders-tata-communications-mazagon-dock/article71470888.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.15] dyn_jef ↓
- dyn_jef [EQUITIES]: last 49.42, z20 -2.15, zc 0.44, resid-z -1.05 [quiet], 1d 1.20%, |z20|=2.15
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Solar Industries’ defence share may fall to 22-25% by FY30 after Omnia deal: Jefferies — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-defence-share-may-fall-to-22-25-by-fy30-after-omnia-deal-jefferies/articleshow/134280191.cms
- Source: Solar Industries shares plunge 17% in 2 days. Why Jefferies, Nuvama still see up to 46% upside — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-shares-plunge-17-in-2-days-why-jefferies-nuvama-still-see-up-to-46-upside/articleshow/134279133.cms
- Source: Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estimates after new UPI charges — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-jump-7-as-jefferies-other-brokerages-raise-target-prices-and-earnings-estimates-after-new-upi-charges/articleshow/134278132.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [AMBER 4.13] dyn_stylebaaza_ns ↓
- dyn_stylebaaza_ns [EQUITIES]: last 372.30, z20 -2.13, zc -0.31, resid-z -0.53 [quiet], 1d -1.00%, |z20|=2.13
- **Mechanism**: dyn_stylebaaza_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Retail sales surged toward the end of summer. The U.S. economy has plenty of momentum. — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/retail-sales-surged-toward-the-end-of-summer-economy-still-has-plenty-of-momentum-cdf667b2?mod=mw_rss_topstories
- Source: Jindal Supreme IPO subscribed 7.53 times on Day 1 led by retail investors — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/jindal-supreme-ipo-subscribed-753-times-on-day-1-led-by-retail-investors/article71472574.ece
- Source: IPO GMP Today Live Updates | Hero Motors IPO sails through on Day 1; retail portion subscribed 1.7 times — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/live-blog/ipo-gmp-today-live-updates-hero-motors-ss-retails-nse-ipo-gmp-subscription-price-band-nse-bse-listing-date/liveblog/134277831.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
hy_oas ↑ (4.05), dyn_icicigi_bo ↓ (3.7), nikkei_225 ↓ (3.57), dyn_indusindbk_bo ↓ (3.45), usd_cny ↓ (3.35), fx · 2 series ↓ (3.12), usd_mxn ↑ (3.01), gold_silver_ratio ↑ (3.01), dyn_hdb ↓ (2.74), commodities · 2 series ↑ (2.47), dyn_lenskart_ns ↑ (2.4), nifty_metal ↓ (2.36)

## India macro
- nifty_50: 23217.5996 (1d 0.43%, z20 -2.11, flag amber)
- nifty_midcap_100: 60879.1484 (1d 0.01%, z20 -2.95, flag red)
- usd_inr: 95.9450 (1d 0.11%, z20 1.35, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6221 (1d -0.42%, z20 -1.69, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 65.0 — "Expert view: What a booming IPO market means for Indian investors"
- COALINDIA.NS (COAL INDIA LTD) score 64.6 — "Expert view: What a booming IPO market means for Indian investors"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 63.7 — "Expert view: What a booming IPO market means for Indian investors"
- INDIANB.NS (INDIAN BANK) score 63.3 — "Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FM"
- COIN (Coinbase Global, Inc.) score 56.0 — "Global Market: European shares recover as oil rally pauses ahead of Fed decision"
- BAC (Bank of America Corporation) score 49.9 — "Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FM"
- HDB (HDFC Bank Limited) score 44.5 — "Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FM"
- OHI (Omega Healthcare Investors, In) score 44.4 — "Expert view: What a booming IPO market means for Indian investors"
- BOND (PIMCO Active Bond Exchange-Tra) score 43.7 — "Indian bonds rise on short covering before Fed decision"
- IDBI.NS (IDBI BANK LIMITED) score 40.7 — "Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FM"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.7 — "Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FM"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.7 — "Sensex today | Stock Market Highlights: Sensex gains 333 points, Nifty rises 99 points; FM"
- CHKP (Check Point Software Technolog) score 38.8 — "Fortis Healthcare shares outlook by Nomura: Rating neutral and target price remains  ₹1030"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.8 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.8 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- TECH (Bio-Techne Corp) score 32.8 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- 301077.SZ (CHINASTARS) score 26.8 — "China Could Curb Fuel Exports as Diesel and Gasoline Stocks Sink"
- SEPN (Septerna, Inc.) score 24.2 — "NSE IPO GMP slips ahead of launch tomorrow, 17 September: Should you subscribe at IPO pric"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.9 — "TTF Gas Hits $92.95 as Gulf Tensions Weigh on Energy Markets"
- LTH (Life Time Group Holdings, Inc.) score 23.6 — "Hero Motors IPO Day 1: Issue subscribed 1.18 times so far"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.3 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.3 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.2 — "Jindal Supreme IPO subscribed 7.53 times on Day 1 led by retail investors"
- JIOFIN.BO (Jio Financial Services Limited) score 9.9 — "JM Financial sees up to 28% upside in Dr Reddy’s and Aurobindo Pharma. Should you buy?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.4 — "5% Treasury yields mean America’s debt bill just got a lot bigger"
- NVDA (NVIDIA Corporation) score 8.9 — "BESSENT: TRUMP COMPLETELY ALIGNED WITH NVIDIA'S JENSEN HUANG"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.9 — "SIP returns in last 3 yrs  remain lacklustre even as inflows hit new high"
- JEF (Jefferies Financial Group Inc.) score 7.8 — "Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estim"
- VT (Vanguard Total World Stock Ind) score 7.6 — "Quote of the day by Edward Thorp: "I think that we only get estimates of the distributions"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.4 — "GRT Jewellers launches ₹431 crore open offer for remaining TBZ stake"
- MS (Morgan Stanley) score 7.3 — "Yes Bank shares jump 4% as Citi, Morgan Stanley see lender as key beneficiary of new UPI c"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 6.8 — "Borosil Renewables' entry into the solar rooftop sector a significant positive, shares may"
- META (Meta) score 6.3 — "Ahead of US Fed rate hike impact on gold rates prediction: How FOMC outcome will effect ye"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.3 — "Indonesia's new finance minister faces an uphill battle on fiscal credibility"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "Suzlon Energy, Adani Power share prices fall: Check 1-week, 1-year and 5-year returns"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.8 — "ICICI Prudential MF, Kotak MF top buyers in SS Retail's Rs 146 crore anchor round before I"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.0 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.6 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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