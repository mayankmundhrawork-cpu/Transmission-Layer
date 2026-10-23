# Transmission Layer — board brief · 2026-10-23 15:02Z

data as of **2026-10-23** · 97 series · 21 red / 37 amber · 8 events surfaced (37 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.833, 15d in regime; vol-pct 0.791, breadth-off 0.875, Markov P(high-vol) 0.023)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.37, contra nifty_50 corr20=0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.01, corr60 0.13, last shift 2026-08-28. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.23, corr60 0.06, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-02. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.25, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.001632704625657233)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.5** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=1960) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.18] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4015.30, z20 -3.26, zc -0.81, resid-z -0.07 [quiet], 1d -1.11%, |z20|=3.26; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 53.95, z20 -2.36, zc -0.55, resid-z 0.24 [quiet], 1d -1.49%, |z20|=2.36; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 74.43, z20 1.86, zc n/a, resid-z n/a [quiet], 1d 0.38%, GSR<75 (extreme low); |z20|=1.86
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.505 vs comex_silver, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.516 vs comex_gold
- Source: Silver crashes  ₹56000/kg from August peak; gold slides 23000/10 grams. What’s driving the selloff in precious metals — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/silver-crashes-rs-56000-kg-from-august-peak-gold-slides-23000-10-grams-what-s-driving-the-selloff-in-precious-metals-11792763090890.html
- Source: From mercury to gold? This San Francisco startup claims it can produce yellow metal at will — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/stocks/news/from-mercury-to-gold-this-san-francisco-startup-claims-it-can-produce-yellow-metal-at-will/articleshow/135140759.cms
- Source: Silver prices slide below Rs 2 lakh/kg, down nearly 55% from Jan peak. What’s behind the rapid selloff? — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/commodities/news/silver-prices-slide-below-rs-2-lakh/kg-down-nearly-55-from-jan-peak-whats-behind-the-rapid-selloff/articleshow/135139949.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.67] commodities · 2 series ↑
- wti [COMMODITIES]: last 102.39, z20 1.84, zc 1.06, resid-z 0.84 [quiet], 1d 2.94%, 1-session move +2.94% ≥ 1.5%; |z20|=1.84
- brent [COMMODITIES]: last 111.39, z20 1.80, zc -0.67, resid-z -1.08 [quiet], 1d -1.57%, 1-session move -1.57% ≥ 1.5%; |z20|=1.80; 1y-pct=96
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.351 via wti, z -2.99, reacted)
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.54 vs brent, historically leads by 5d
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.395 vs wti, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho -0.351, z -2.99)
- Source: Oil India Strikes Natural Gas in Shallow Offshore Basin — OilPrice, 2026-10-23. https://oilprice.com/Latest-Energy-News/World-News/Oil-India-Strikes-Natural-Gas-in-Shallow-Offshore-Basin.html
- Source: The Hidden $40-Per-Barrel Cost Driving Oil Prices Higher — OilPrice, 2026-10-23. https://oilprice.com/Energy/Energy-General/The-Hidden-40-Per-Barrel-Cost-Driving-Oil-Prices-Higher.html
- Source: U.S. Partner in Venezuela Oil Deal Looks to Hike Crude Production — OilPrice, 2026-10-23. https://oilprice.com/Latest-Energy-News/World-News/US-Partner-in-Venezuela-Oil-Deal-Looks-to-Hike-Crude-Production.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.44] cross-asset · 7 series ↓
- dyn_swiggy_ns [EQUITIES]: last 176.00, z20 -3.10, zc -7.31, resid-z -6.71 [unexplained], 1d -16.75%, |z20|=3.10; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 55799.90, z20 -2.99, zc -2.14, resid-z -3.15 [unexplained], 1d -2.21%, |z20|=2.99
- india_vix [INDICES]: last 16.81, z20 2.26, zc 1.13, resid-z n/a [quiet], 1d 6.68%, |z20|=2.26
- dyn_jiofin_bo [EQUITIES]: last 205.00, z20 -2.17, zc -1.93, resid-z -1.50 [unexplained], 1d -2.84%, |z20|=2.17; 1y-pct=0
- nifty_metal [INDICES]: last 11473.35, z20 -1.97, zc -1.99, resid-z -2.04 [unexplained], 1d -2.75%, |z20|=1.97
- dyn_policybzr_ns [EQUITIES]: last 1015.00, z20 -0.66, zc -0.66, resid-z -0.12 [quiet], 1d -2.21%, 1y-pct=2
- nifty_50 [INDICES]: last 22600.00, z20 -0.54, zc -0.40, resid-z -0.18 [quiet], 1d -0.39%, 1y-pct=3
- **Mechanism**: cross-asset · 7 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.642 via nifty_50, z -2.61, reacted); dyn_bajfinance_ns (rho -0.621 via india_vix, z -2.14, reacted); dyn_adanient_bo (rho 0.6 via nifty_metal, z -2.07, reacted); midcap_largecap_ratio (rho 0.587 via nifty_midcap_100, z -3.53, reacted); dyn_indusindbk_bo (rho -0.568 via india_vix, z -1.83, reacted)
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.558 vs nifty_midcap_100, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.524 vs nifty_50, historically leads by 2d
- **India receivers**: nifty_fmcg (rho 0.642, z -2.61); dyn_bajfinance_ns (rho -0.621, z -2.14); dyn_adanient_bo (rho 0.6, z -2.07); midcap_largecap_ratio (rho 0.587, z -3.53)
- Source: Bharat Electronics among 4 Sensex stocks to hit 52-week lows; shares fall up to 9% in a month — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/stocks/news/bharat-electronics-among-4-sensex-stocks-to-hit-52-week-lows-shares-fall-up-to-9-in-a-month/slideshow/135147674.cms
- Source: Market wrap: Eternal, Apollo Hospital, Shriram Finance, Adani Enterprises among top gainers and losers on Nifty and Sensex on Friday — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-apollo-hospital-shriram-finance-adani-enterprises-among-top-gainers-and-losers-on-nifty-and-sensex-on-friday/articleshow/135144888.cms
- Source: Sensex today | Stock Market Highlights: Sensex, Nifty extend losses as crude surges to $114, all sectors close in red — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-23rd-october-2026/article71611889.ece
- Historical analogues: 2025-07-21 (d=1.08), 2025-12-19 (d=1.16), 2025-07-14 (d=1.31)

### [AMBER 5.58] cross-asset · 3 series ↓
- vix [INDICES]: last 19.47, z20 2.26, zc 0.23, resid-z n/a [quiet], 1d 2.31%, |z20|=2.26
- dyn_vt [EQUITIES]: last 156.10, z20 -2.23, zc -0.31, resid-z -0.15 [quiet], 1d -0.27%, |z20|=2.23
- nasdaq_100 [INDICES]: last 29115.95, z20 -1.87, zc 0.34, resid-z 0.40 [quiet], 1d 0.54%, |z20|=1.87
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.12).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.684 vs vix, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.616 vs dyn_vt
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.594 vs vix
- Source: Nasdaq CEO flags IPO slowdown amid market volatility — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/news/nasdaq-ceo-flags-ipo-slowdown-amid-market-volatility/articleshow/135139313.cms
- Source: Stock market outlook today, 23 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-23-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11792716174246.html
- Source: US stocks today: Nasdaq slumps 2.5%, S&P 1% as revived AI doubts ignite tech selloff — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-slumps-2-5-sp-1-as-revived-ai-doubts-ignite-tech-selloff/articleshow/135127224.cms
- Historical analogues: 2025-10-23 (d=0.12), 2025-05-21 (d=0.17), 2025-04-28 (d=0.17)

### [RED 5.42] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 154.84, z20 3.42, zc 0.83, resid-z 0.74 [quiet], 1d 1.88%, |z20|=3.42
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.39 via dyn_chkp, z -1.83, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.39, z -1.83)
- Source: NBFC stock crashes 25% in month, but ICICI Securities sees a potential 50% rally - Do you own it? Check target price — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/nbfc-stock-crashes-25-in-month-but-icici-securities-sees-a-potential-50-rally-do-you-own-it-check-target-price-11792757924909.html
- Source: FMCG stocks to buy: Anand Rathi names Marico, GCPL, Asian Paints, Mrs Bector Food - check ratings and target prices — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/fmcg-stocks-to-buy-now-anand-rathi-names-marico-gcpl-asian-paints-mrs-bector-food-check-ratings-and-target-prices-11792751055004.html
- Source: Infosys Q2 results, dividend 2026 amount announced:  ₹26 per share payout, profit jumps 6.23% YoY - Check record date — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/infosys-q2-results-dividend-2026-amount-announced-rs-25-per-share-payout-profit-jumps-6-23-yoy-check-record-date-11792754002819.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 5.38] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 46041.43, z20 -2.06, zc -1.26, resid-z 0.02 [quiet], 1d -1.81%, |z20|=2.06
- nikkei_225 [INDICES]: last 62726.83, z20 -1.89, zc -0.15, resid-z 0.13 [quiet], 1d -0.29%, |z20|=1.89
- kospi [INDICES]: last 5524.45, z20 -1.51, zc -0.05, resid-z 0.32 [quiet], 1d -0.17%, |z20|=1.51
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.446 via kospi, z -1.28, reacted); dyn_idbi_ns (rho 0.429 via nikkei_225, z -3.07, reacted)
- **India receivers**: dyn_cartrade_ns (rho 0.446, z -1.28); dyn_idbi_ns (rho 0.429, z -3.07)
- Source: Japan’s Nikkei falls over 1% as Wall Street tech selloff rattles markets — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-falls-over-1-as-wall-street-tech-selloff-rattles-markets/articleshow/135133891.cms
- Source: Stock market outlook today, 23 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-23-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11792716174246.html
- Source: Global Market: Japan’s Nikkei falls as chip stocks retreat on AI spending concerns — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-as-chip-stocks-retreat-on-ai-spending-concerns/articleshow/135106795.cms

### [RED 5.36] usd_jpy ↓
- usd_jpy [FX]: last 156.75, z20 -3.36, zc -1.91, resid-z -1.72 [unexplained], 1d -0.88%, |z20|=3.36
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Yen jumps as oil, AI and France worries rattle markets — Mint Markets, 2026-10-22. https://www.livemint.com/market/yen-jumps-as-oil-ai-and-france-worries-rattle-markets-11792694662480.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [AMBER 5.28] natgas ↓
- natgas [COMMODITIES]: last 3.04, z20 -0.28, zc 2.43, resid-z 3.46 [unexplained], 1d 8.83%, 1-session move +8.83% ≥ 5.0%
- **Mechanism**: natgas ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho -0.352 via natgas, z 0.82, quiet)
- **India receivers**: dyn_justdial_bo (rho -0.352, z 0.82)
- Source: Oil India Strikes Natural Gas in Shallow Offshore Basin — OilPrice, 2026-10-23. https://oilprice.com/Latest-Energy-News/World-News/Oil-India-Strikes-Natural-Gas-in-Shallow-Offshore-Basin.html
- Source: European Natural Gas Prices Surge to Highest Level Since 2022 — OilPrice, 2026-10-23. https://oilprice.com/Latest-Energy-News/World-News/European-Natural-Gas-Prices-Surge-to-Highest-Level-Since-2022.html
- Source: Adani Total Gas cites higher LNG cost, domestic supply cut for ₹4.45 per kg CNG prices hike — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/markets/commodities/adani-total-gas-cites-higher-lng-cost-domestic-supply-cut-for-445-per-kg-cng-prices-hike/article71615330.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
dyn_meta ↓ (5.15), dyn_tatatech_ns ↓ (5.02), dyn_coalindia_ns ↓ (4.62), cross-asset · 2 series ↑ (4.57), dyn_lth ↑ (4.34), dyn_rs ↑ (4.19), dyn_bajfinance_ns ↓ (4.14), dyn_bond ↑ (4.14), dyn_sepn ↑ (4.11), dyn_atherenerg_ns ↓ (4.08), dyn_adanient_bo ↓ (4.07), hy_oas ↑ (4.04)

## India macro
- nifty_50: 22600.0000 (1d -0.39%, z20 -0.54, flag amber)
- nifty_midcap_100: 55799.8984 (1d -2.21%, z20 -2.99, flag red)
- usd_inr: 94.9300 (1d 0.65%, z20 -1.11, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4690 (1d -1.83%, z20 -3.53, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 103.8 — "Jio Plaforms IPO is most subscribed in India's history as bids total $77.1 billion"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.4 — "Jio Plaforms IPO is most subscribed in India's history as bids total $77.1 billion"
- INOXINDIA.NS (INOX INDIA LIMITED) score 101.7 — "Jio Plaforms IPO is most subscribed in India's history as bids total $77.1 billion"
- INDIANB.NS (INDIAN BANK) score 81.6 — "Jubilant Pharmova eyes $150 million through rupee debt sale, bankers say"
- BAC (Bank of America Corporation) score 72.4 — "Jubilant Pharmova eyes $150 million through rupee debt sale, bankers say"
- HDB (HDFC Bank Limited) score 64.1 — "Jubilant Pharmova eyes $150 million through rupee debt sale, bankers say"
- OHI (Omega Healthcare Investors, In) score 62.9 — "Angel One rolls out US stock investing for investors"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 62.5 — "Jubilant Pharmova eyes $150 million through rupee debt sale, bankers say"
- IDBI.NS (IDBI BANK LIMITED) score 61.6 — "Jubilant Pharmova eyes $150 million through rupee debt sale, bankers say"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 61.6 — "Jubilant Pharmova eyes $150 million through rupee debt sale, bankers say"
- COIN (Coinbase Global, Inc.) score 60.3 — "Global Market: French bond selloff raises debt concerns across Europe amid social unrest"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.3 — "Broker’s Call: Mahindra Lifespace Developers (Buy)"
- TGT (Target Corporation) score 48.6 — "Top telecom shares to buy: Bharti Airtel, Vodafone Idea, Indus Towers by Ambit Capital wit"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.2 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- TECH (Bio-Techne Corp) score 48.2 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- CHKP (Check Point Software Technolog) score 45.8 — "Infosys dividend alert! IT major announces Rs 26 per share dividend. Check record date"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.3 — "Global Market: French bond selloff raises debt concerns across Europe amid social unrest"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.4 — "Ather Energy, TVS Motor, Bajaj Auto, Tata Motors PV shares: Can Delhi’s pollution curbs ch"
- LTH (Life Time Group Holdings, Inc.) score 31.1 — "Bitcoin Falls Below $83,000 as AI Jitters Weigh on Sentiment"
- RS (Reliance, Inc.) score 29.7 — "Reliance Jio IPO overall subscription status, GMP: Day 1, 2, 3 details; allotment, listing"
- 301077.SZ (CHINASTARS) score 26.6 — "China AI Model Stocks’ $150 Billion Drop Shows No Sign of Easing"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.6 — "Reliance Jio IPO oversubscribed | Should investors apply or avoid or buy shares after list"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.4 — "Ather Energy, TVS Motor, Bajaj Auto, Tata Motors PV shares: Can Delhi’s pollution curbs ch"
- JIOFIN.BO (Jio Financial Services Limited) score 20.0 — "Smart financial advisers are dropping ROI, NAV and QCD for plain English when talking to c"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 18.9 — "Adani Power Q2 Results: Profit zooms 134% YoY to Rs 6,919 crore; revenue jumps 45%"
- META (Meta) score 18.3 — "From mercury to gold? This San Francisco startup claims it can produce yellow metal at wil"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.7 — "Ather Energy, TVS Motor, Bajaj Auto, Tata Motors PV shares: Can Delhi’s pollution curbs ch"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.7 — "Ather Energy, TVS Motor, Bajaj Auto, Tata Motors PV shares: Can Delhi’s pollution curbs ch"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.9 — "Market wrap: Eternal, Apollo Hospital, Shriram Finance, Adani Enterprises among top gainer"
- BZ=F (Brent Crude Oil Last Day Finan) score 16.9 — "IPO GMP comparison: Reliance Jio Platforms IPO vs Paras Healthcare - Last day to apply tod"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.6 — "This hot AI-fueled stock has been in a rut. It just beat earnings expectations by 36%."
- SEPN (Septerna, Inc.) score 15.2 — "India's September crude oil imports jump over 16% month-on-month"
- JEF (Jefferies Financial Group Inc.) score 11.7 — "Swiggy vs Eternal shares compared: Which is better stock to buy post Q2 results? Jefferies"
- GS (Goldman Sachs Group, Inc. (The) score 9.3 — "Ola Electric shares dip 5% after Goldman Sachs downgrades stock to Sell. Here’s why"
- SWIGGY.NS (SWIGGY LIMITED) score 6.4 — "Swiggy vs Eternal shares compared: Which is better stock to buy post Q2 results? Jefferies"
- VT (Vanguard Total World Stock Ind) score 6.2 — "Reliance Jio IPO Global Record: Another feather in cap! History created - 1st IPO worldwid"
- WIT (Wipro Limited) score 5.9 — "Top stocks to buy: IT stocks soar! TCS, Infosys, HCL Tech, Wipro - Nifty IT up over 3% tod"
- NVDA (NVIDIA Corporation) score 5.8 — "Christopher Wood swapped Nvidia for a Greek infrastructure stock. The bet is paying off"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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