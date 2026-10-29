# Transmission Layer — board brief · 2026-10-29 10:52Z

data as of **2026-10-29** · 97 series · 12 red / 32 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.712, 19d in regime; vol-pct 0.674, breadth-off 0.75, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.36, contra nifty_50 corr20=0.46, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.12, last shift 2026-09-04. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.06, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-10. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.27, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.05, corr60 -0.16, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.5, corr60 0.29, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.68, β -0.4715, p 0.0); driver zc -1.87 → expected 1.278%. Type hit-rate 0.835 (n=1702).
- Track record · residual_reversion: hit-rate **0.502** (n=1122) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.835** (n=1702) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.58] equities · 2 series ↑
- dyn_jef [EQUITIES]: last 47.51, z20 3.75, zc 1.32, resid-z 1.18 [quiet], 1d 2.85%, |z20|=3.75
- dyn_gs [EQUITIES]: last 926.53, z20 3.71, zc 0.87, resid-z 0.99 [quiet], 1d 1.62%, |z20|=3.71
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.355 via dyn_jef, z 0.08, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.833 vs dyn_gs, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.81 vs dyn_gs, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.671 vs dyn_gs, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.625 vs dyn_gs, historically leads by 2d
- Watch next: dxy (inverse) — not yet - watch; rho -0.514 vs dyn_gs, historically leads by 2d
- **India receivers**: dyn_indusindbk_bo (rho 0.355, z 0.08)
- Source: HUL shares rise 3% after Q2 results. Jefferies, Nomura cut target price but forecast 29% upside potential — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-rise-3-after-q2-results-jefferies-nomura-cut-target-price-but-forecast-29-upside-potential/articleshow/135295044.cms
- Source: Jefferies initiates coverage on NSE with ‘Buy’; here’s why it sees fresh growth potential — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-initiates-coverage-on-nse-with-buy-heres-why-it-sees-fresh-growth-potential/articleshow/135293157.cms
- Source: Potential LTCG tax cut could revive FIIs’ India bet, says Jefferies: Which stocks may benefit most? — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/potential-ltcg-tax-cut-could-revive-fiis-india-bet-says-jefferies-which-stocks-may-benefit-most/articleshow/135290083.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.55), 2025-05-16 (d=0.58)

### [RED 5.83] dyn_cartrade_ns ↓
- dyn_cartrade_ns [EQUITIES]: last 2319.90, z20 -3.83, zc -1.33, resid-z -2.02 [unexplained], 1d -5.87%, |z20|=3.83
- **Mechanism**: dyn_cartrade_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3,377. Here’s why — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/cartrade-tech-shares-tank-over-6-after-q2-results-but-nomura-raises-target-price-to-rs-3377-heres-why/articleshow/135290221.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 5.65] cross-asset · 4 series ↓
- tips_10y_real [RATES]: last 2.64, z20 -1.99, zc -0.39, resid-z -1.15 [quiet], 1d -0.75%, |z20|=1.99
- ust_30y [RATES]: last 5.30, z20 -1.85, zc -0.22, resid-z -0.36 [quiet], 1d -0.19%, |z20|=1.85
- ust_10y [RATES]: last 4.99, z20 -1.84, zc -0.19, resid-z -0.57 [quiet], 1d -0.20%, |z20|=1.84
- dyn_schd [EQUITIES]: last 35.08, z20 1.29, zc -0.15, resid-z -0.75 [quiet], 1d -0.13%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.512 vs dyn_schd, historically leads by 4d
- Watch next: kospi (inverse) — not yet - watch; rho -0.566 vs dyn_schd
- Watch next: nikkei_225 (inverse) — not yet - watch; rho -0.554 vs dyn_schd
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.502 vs dyn_schd
- Source: Global Market: Japan bond yields steady ahead of BOJ policy decision — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-bond-yields-steady-ahead-of-boj-policy-decision/articleshow/135298606.cms
- Source: Asian Paints Q2 Results: Net profit rises 7% YoY to Rs 1,068 crore; firm announces Rs 5.75/share dividend — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/earnings/asian-paints-q2-results-net-profit-rises-7-yoy-to-rs-1068-crore-firm-announces-rs-5-75/share-dividend/articleshow/135297927.cms
- Source: HUL vs Nestle India shares compared: Which FMCG stock to buy post Q2 results: Who wins on profit, revenue and dividend? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/hul-vs-nestle-india-q2-results-who-wins-on-profit-revenue-and-dividend-which-fmcg-stock-should-you-buy-11793258197263.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.66), 2025-05-19 (d=1.13)

### [AMBER 5.52] brent ↑
- brent [COMMODITIES]: last 110.24, z20 0.52, zc -2.06, resid-z 0.57 [priced], 1d -4.41%, 1-session move -4.41% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.431 via brent, z -0.5, quiet)
- Watch next: sp500 (inverse) — not yet - watch; rho -0.576 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.567 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.562 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.515 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.431, z -0.5)
- Source: Oil and gas stocks to buy: ONGC vs Oil India shares - Kotak Securities raises FY27 forecast to $100; know preferred pick — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/oil-and-gas-stocks-to-buy-ongc-vs-oil-india-shares-kotak-securities-raises-fy27-forecast-to-100-know-preferred-pick-11793259081354.html
- Source: Best Vedanta stock to buy after Q2 results 2026: Vedanta Iron and Steel, Vedanta Oil and Gas, others — Which is better? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/best-vedanta-stock-to-buy-after-q2-results-2026-vedanta-iron-and-steel-vedanta-oil-and-gas-others-which-is-better-11793255299161.html
- Source: Indian bonds track US Treasuries higher amid oil-price relief — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/bonds/indian-bonds-track-us-treasuries-higher-amid-oil-price-relief/articleshow/135294873.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.23] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 76.44, z20 1.91, zc n/a, resid-z n/a [quiet], 1d 0.85%, |z20|=1.91
- comex_silver [COMMODITIES]: last 52.82, z20 -1.88, zc -0.53, resid-z -0.35 [quiet], 1d -1.19%, |z20|=1.88; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4037.30, z20 -1.72, zc -0.30, resid-z 1.08 [quiet], 1d -0.35%, |z20|=1.72; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.503 vs gold_silver_ratio, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.565 vs comex_silver
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.544 vs gold_silver_ratio
- Source: Today’s Gold Rate in India October 29: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-29-2026/article71639624.ece
- Source: Today’s Gold Rate in India October 29: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-29-2026/article71639623.ece
- Source: Silver futures decline to ₹1.93 lakh/kg — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/markets/commodities/silver-futures-decline-to-193-lakhkg/article71639207.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.18] natgas ↑
- natgas [COMMODITIES]: last 3.04, z20 0.18, zc 2.02, resid-z 1.59 [unexplained], 1d 8.06%, 1-session move +8.06% ≥ 5.0%
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: U.S. Natural Gas Production Hits New Records as Demand Surges — OilPrice, 2026-10-28. https://oilprice.com/Energy/Natural-Gas/US-Natural-Gas-Production-Hits-New-Records-as-Demand-Surges.html
- Source: India’s Record LNG Buying Meets Record-High Prices — OilPrice, 2026-10-28. https://oilprice.com/Energy/Natural-Gas/Indias-Record-LNG-Buying-Meets-Record-High-Prices.html
- Source: QatarEnergy Extends LNG Force Majeure to End of 2026 — OilPrice, 2026-10-28. https://oilprice.com/Latest-Energy-News/World-News/QatarEnergy-Extends-LNG-Force-Majeure-to-End-of-2026.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 4.72] dyn_sepn ↑
- dyn_sepn [EQUITIES]: last 44.23, z20 2.72, zc 0.05, resid-z 1.23 [quiet], 1d 0.20%, |z20|=2.72; 1y-pct=98
- **Mechanism**: dyn_sepn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US OCT CONSUMER CONFIDENCE INDEX 91.7 (CONSENSUS 81.0) VS SEPT REVISED 84.2 (PREVIOUS 81.9) - CONFERENCE BOARD — DeItaone, 2026-10-27. https://t.me/walter_bloomberg/37609
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [RED 4.61] dyn_rs ↑
- dyn_rs [EQUITIES]: last 437.03, z20 2.61, zc 0.61, resid-z 1.53 [unexplained], 1d 0.98%, |z20|=2.61; 1y-pct=100
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Reliance Jio Platforms shares vs Bharti Airtel vs Vodafone Idea: Top telecom stock to buy? What experts suggest — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/reliance-jio-platforms-shares-vs-bharti-airtel-vs-vodafone-idea-top-telecom-stock-to-buy-what-experts-suggest-11793262195751.html
- Source: Reliance Jio Platforms shares: After 26.68% IPO debut gains, jump 5% more - What should investors do? Buy more or exit? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/reliance-jio-platforms-shares-after-26-68-ipo-debut-gains-jump-5-more-what-should-investors-do-buy-more-or-exit-11793248224964.html
- Source: Jio Platforms shares: After 27% jump on IPO listing day, will Reliance group stock rise more today? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/jio-platforms-shares-after-27-jump-on-ipo-listing-day-will-reliance-group-stock-rise-more-today-11793239306452.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

## Watchlist (below surfacing floor)
dyn_meta ↓ (4.4), dyn_tech ↑ (4.1), sofr ↑ (3.87), dyn_hdb ↓ (3.69), shanghai_comp ↓ (3.55), indices · 2 series ↑ (3.51), dyn_jiofin_bo ↓ (3.38), dyn_4417_t ↑ (3.33), dyn_techm_ns ↑ (2.95), commodities · 2 series ↓ (2.81), bovespa ↓ (2.62), usd_cny ↓ (2.52)

## India macro
- nifty_50: 22936.7500 (1d 1.05%, z20 1.29, flag none)
- nifty_midcap_100: 57836.8008 (1d 0.99%, z20 -0.50, flag none)
- usd_inr: 95.2500 (1d 0.08%, z20 -0.40, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5216 (1d -0.06%, z20 -1.02, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 103.2 — "Gift Nifty indicates negative opening for Indian stocks"
- COALINDIA.NS (COAL INDIA LTD) score 103.0 — "Gift Nifty indicates negative opening for Indian stocks"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 101.1 — "Gift Nifty indicates negative opening for Indian stocks"
- INDIANB.NS (INDIAN BANK) score 69.8 — "Gift Nifty indicates negative opening for Indian stocks"
- TGT (Target Corporation) score 62.3 — "Top stock to buy today: Jefferies India sees 29% upside in NSE share price in upside scena"
- BAC (Bank of America Corporation) score 60.4 — "City Union Bank shares rally 7% after Q2 net profit grows 27% YoY to Rs 416 Crore"
- COIN (Coinbase Global, Inc.) score 57.5 — "Global Market: Japan's Nikkei rises on Advantest forecast; Samsung slump caps gains"
- OHI (Omega Healthcare Investors, In) score 55.6 — "Alphabet Inc. shares: Google parent stock price falls 10% post Q3 earnings | What should i"
- HDB (HDFC Bank Limited) score 52.5 — "City Union Bank shares rally 7% after Q2 net profit grows 27% YoY to Rs 416 Crore"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.1 — "City Union Bank shares rally 7% after Q2 net profit grows 27% YoY to Rs 416 Crore"
- IDBI.NS (IDBI BANK LIMITED) score 51.8 — "City Union Bank shares rally 7% after Q2 net profit grows 27% YoY to Rs 416 Crore"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 51.8 — "City Union Bank shares rally 7% after Q2 net profit grows 27% YoY to Rs 416 Crore"
- CHKP (Check Point Software Technolog) score 45.3 — "IPO GMP comparison: BLS Polymers vs SFC Environmental vs M.K. Sons vs Bombay Coated - Chec"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.2 — "CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.4 — "CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3"
- TECH (Bio-Techne Corp) score 40.4 — "CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.8 — "EU Scrambles to Contain Energy Price Crisis Ahead of Winter"
- LTH (Life Time Group Holdings, Inc.) score 27.6 — "BLS Polymers IPO Day 3: Issue subscribed 42.47 times with GMP at 34%. Check key details"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 27.0 — "Paras Healthcare shares: After IPO listing gains, check what's happening with stock - Buy,"
- RS (Reliance, Inc.) score 25.7 — "Jio Platforms shares: After 27% jump on IPO listing day, will Reliance group stock rise mo"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.5 — "Indian bonds track US Treasuries higher amid oil-price relief"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.6 — "Diwali stocks 2026: Tata Steel, MCX, IHCL and 8 more to add sparkle to shares portfolio in"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.6 — "Diwali stocks 2026: Tata Steel, MCX, IHCL and 8 more to add sparkle to shares portfolio in"
- 301077.SZ (CHINASTARS) score 22.8 — "Global Market: China’s yuan hits four-year high against dollar after Fed holds rates"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.1 — "Stocks to Watch, Oct 29: TVS Motor, Fortis Healthcare, Dr Reddy’s, Bajaj Electricals, Zagg"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.0 — "Best Adani stock to buy after Q2 results 2026? Adani Power vs Adani Ports vs Adani Enterpr"
- JIOFIN.BO (Jio Financial Services Limited) score 15.7 — "ALPHABET ($GOOGL) Q3 2026 EARNINGS Revenue: $127.58B vs. $127.93B est. — MISS EPS: $2.12 v"
- JEF (Jefferies Financial Group Inc.) score 15.0 — "Top stock to buy today: Jefferies India sees 29% upside in NSE share price in upside scena"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.6 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.0 — "EU Rules Out New Climate Finance Pledges at COP31"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "YIELD ON 10-YEAR TREASURY NOTE LAST UP 4.11 BASIS POINTS AT 5.034%"
- SEPN (Septerna, Inc.) score 11.2 — "Vedanta Aluminium reports 41% revenue growth to Rs 22,066 crore in September quarter"
- SCHD (Schwab US Dividend Equity ETF) score 11.2 — "HUL vs Nestle India shares compared: Which FMCG stock to buy post Q2 results: Who wins on "
- META (Meta) score 9.0 — "AMD $META - AMD AND META ADVANCE STRATEGIC PARTNERSHIP TO POWER META’S SUPERINTELLIGENCE I"
- VT (Vanguard Total World Stock Ind) score 7.7 — "Bahri Profit Hits $1.36 Billion as the World Scrambles for Tankers"
- INFY (Infosys Limited) score 6.8 — "Infosys, TechM, TCS, other IT stocks plunge up to 5%, extend losses as global AI trade reb"
- GS (Goldman Sachs Group, Inc. (The) score 6.6 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- SWIGGY.NS (SWIGGY LIMITED) score 2.7 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.8 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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