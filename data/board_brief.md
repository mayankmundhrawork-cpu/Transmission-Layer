# Transmission Layer — board brief · 2026-10-29 23:56Z

data as of **2026-10-29** · 97 series · 14 red / 27 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.661, 1d in regime; vol-pct 0.674, breadth-off 0.647, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.36, contra nifty_50 corr20=0.44, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.14, corr60 0.12, last shift 2026-09-04. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.05, corr60 0.07, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-10. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.25, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.08, corr60 -0.14, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.5, corr60 0.29, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0002726380408915041)
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.291, β 0.064, p 0.0); driver zc -2.24 → expected -0.277%. Type hit-rate 0.835 (n=1702).
- **SETUP** dyn_jef → usd_mxn: leads 1d (ccf -0.272, β -0.0587, p 0.0002); driver zc 1.5 → expected -0.203%. Type hit-rate 0.835 (n=1702).
- **SETUP** dyn_jef → aud_usd: leads 1d (ccf 0.252, β 0.0562, p 0.00207); driver zc 1.5 → expected 0.194%. Type hit-rate 0.835 (n=1702).
- Track record · residual_reversion: hit-rate **0.502** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.835** (n=1702) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.76] dyn_jef ↑
- dyn_jef [EQUITIES]: last 49.15, z20 4.76, zc 1.50, resid-z 1.72 [unexplained], 1d 3.45%, |z20|=4.76
- **Mechanism**: dyn_jef ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.395 via dyn_jef, z 0.08, quiet); dyn_bajfinance_ns (rho 0.363 via dyn_jef, z -0.59, quiet)
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.517 vs dyn_jef, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.547 vs dyn_jef
- **India receivers**: dyn_indusindbk_bo (rho 0.395, z 0.08); dyn_bajfinance_ns (rho 0.363, z -0.59)
- Source: HUL shares rise 3% after Q2 results. Jefferies, Nomura cut target price but forecast 29% upside potential — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-rise-3-after-q2-results-jefferies-nomura-cut-target-price-but-forecast-29-upside-potential/articleshow/135295044.cms
- Source: Jefferies initiates coverage on NSE with ‘Buy’; here’s why it sees fresh growth potential — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-initiates-coverage-on-nse-with-buy-heres-why-it-sees-fresh-growth-potential/articleshow/135293157.cms
- Source: Potential LTCG tax cut could revive FIIs’ India bet, says Jefferies: Which stocks may benefit most? — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/potential-ltcg-tax-cut-could-revive-fiis-india-bet-says-jefferies-which-stocks-may-benefit-most/articleshow/135290083.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [RED 5.94] crypto · 2 series ↓
- btc_usd [CRYPTO]: last 77751.01, z20 -3.11, zc -2.24, resid-z -1.95 [unexplained], 1d -4.33%, |z20|=3.11
- eth_usd [CRYPTO]: last 2244.73, z20 -2.06, zc -1.26, resid-z -1.78 [unexplained], 1d -4.79%, |z20|=2.06
- **Mechanism**: crypto · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-11-14 (z-distance 0.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Bitcoin trades near $80,000 after Fed holds rates, signals possibility of further tightening — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-trades-near-80000-after-fed-holds-rates-signals-possibility-of-further-tightening/articleshow/135309957.cms
- Source: BITCOIN FACES SELLING PRESSURE AS LONG-TERM HOLDERS SIT ON LOSSES Long-term Bitcoin holders own approximately 4 million BTC purchased between $85,000 and $118,000, according to Glassnode analysts. With Bitcoin trading near $80,000, more than half of long-term holders' coins were reportedly acquired  — DeItaone, 2026-10-28. https://t.me/walter_bloomberg/37667
- Source: Bitcoin’s Road to $100,000 Is Crowded With Would-Be Sellers — Mint Markets, 2026-10-28. https://www.livemint.com/market/bitcoins-road-to-100-000-is-crowded-with-would-be-sellers-11793145691174.html
- Historical analogues: 2025-11-14 (d=0.08), 2025-02-27 (d=0.16), 2026-01-29 (d=0.38)

### [RED 5.83] dyn_cartrade_ns ↓
- dyn_cartrade_ns [EQUITIES]: last 2319.90, z20 -3.83, zc -1.33, resid-z -1.98 [unexplained], 1d -5.87%, |z20|=3.83
- **Mechanism**: dyn_cartrade_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3,377. Here’s why — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/cartrade-tech-shares-tank-over-6-after-q2-results-but-nomura-raises-target-price-to-rs-3377-heres-why/articleshow/135290221.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 5.75] brent ↑
- brent [COMMODITIES]: last 111.42, z20 0.75, zc -1.58, resid-z -2.41 [unexplained], 1d -3.38%, 1-session move -3.38% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.426 via brent, z -0.5, quiet)
- Watch next: sp500 (inverse) — not yet - watch; rho -0.561 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.56 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.521 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.514 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.426, z -0.5)
- Source: Mexico’s Richest Man Sells $1.15 Billion in Oil Stocks — OilPrice, 2026-10-29. https://oilprice.com/Latest-Energy-News/World-News/Mexicos-Richest-Man-Sells-115-Billion-in-Oil-Stocks.html
- Source: Europe to Release 42 Million Barrels of Oil — OilPrice, 2026-10-29. https://oilprice.com/Latest-Energy-News/World-News/Europe-to-Release-42-Million-Barrels-of-Oil.html
- Source: CVX - CHEVRON EXPANDS GLOBAL OIL EXPLORATION AS PROFITS SURGE Chevron is accelerating oil and gas exploration in Africa, South America and the Mediterranean, supported by soaring energy profits following the Iran war. 🔸 50% of exploration capital now targets undeveloped regions, up from roughly 20%. — DeItaone, 2026-10-29. https://t.me/walter_bloomberg/37754
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.64] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 77.42, z20 2.32, zc n/a, resid-z n/a [quiet], 1d 2.15%, |z20|=2.32
- comex_silver [COMMODITIES]: last 51.94, z20 -2.22, zc -1.25, resid-z -1.12 [quiet], 1d -2.84%, |z20|=2.22; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4021.20, z20 -2.00, zc -0.64, resid-z -0.99 [quiet], 1d -0.75%, |z20|=2.00; 1y-pct=5; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.56 vs comex_silver, historically leads by 5d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.517 vs gold_silver_ratio, historically leads by 5d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.55 vs gold_silver_ratio
- Source: Karwa Chauth today but gold, silver rates not glittering — will prices rebound or pain will continue till Diwali? — Mint Markets, 2026-10-29. https://www.livemint.com/market/commodities/karwa-chauth-today-but-gold-silver-rates-not-glittering-will-prices-rebound-or-pain-will-continue-till-diwali-11793271194604.html
- Source: Today’s Gold Rate in India October 29: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-29-2026/article71639624.ece
- Source: Today’s Gold Rate in India October 29: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-29-2026/article71639623.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.48] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.35, z20 3.48, zc 2.20, resid-z -0.99 [moved], 1d 5.13%, |z20|=3.48; 1y-pct=98
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Suzlon Energy Q2 Results: Profit plunges 69% YoY to Rs 394 crore due to one-time deferred tax — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/earnings/suzlon-energy-q2-results-profit-plunges-69-yoy-to-rs-394-crore-revenue-rises-26/articleshow/135304125.cms
- Source: Diwali 2026: MCX Muhurat Trading - Date is 8 Nov 2026; check time for special, trading, client mode modification session — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/diwali-2026-mcx-muhurat-trading-date-is-8-nov-2026-check-time-for-special-trading-client-mode-modification-session-11793258582748.html
- Source: Sanofi Consumer share price jumps 11% after strong Q3 results | Is it time to book profits? Check target, rationale — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/sanofi-consumer-share-price-jumps-11-after-strong-q3-results-is-it-time-to-book-profits-check-target-rationale-11793249979630.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 4.94] dyn_gs ↑
- dyn_gs [EQUITIES]: last 927.52, z20 2.94, zc 0.14, resid-z 0.69 [quiet], 1d 0.25%, |z20|=2.94
- **Mechanism**: dyn_gs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.828 vs dyn_gs, historically leads by 2d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.823 vs dyn_gs, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.8 vs dyn_gs, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.66 vs dyn_gs, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.603 vs dyn_gs, historically leads by 2d
- Source: GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects just one additional Fed rate hike, compared with three currently priced by markets, suggesting the current tightening cycle could be among the smallest since 1983. Strategist Vickie Chang highlighted historicall — DeItaone, 2026-10-28. https://t.me/walter_bloomberg/37659
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.11), 2025-05-13 (d=0.14)

### [RED 4.52] dyn_rs ↑
- dyn_rs [EQUITIES]: last 439.74, z20 2.52, zc 0.36, resid-z 0.66 [quiet], 1d 0.59%, |z20|=2.52; 1y-pct=100
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Jio Platforms first Q2 results after bumper listing: check date; Reliance firm’s earnings in focus; key numbers to watch — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/jio-platforms-first-q2-results-after-bumper-listing-check-date-reliance-firm-s-earnings-in-focus-key-numbers-to-watch-11793290112398.html
- Source: Reliance Power shares on fire! Anil Ambani’s stock jumps 9.22%, but remains down 59% in a year - should you buy? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/reliance-power-shares-on-fire-anil-ambani-s-stock-jumps-9-22-but-remains-down-59-in-a-year-should-you-buy-11793273904768.html
- Source: Reliance Jio Platforms shares vs Bharti Airtel vs Vodafone Idea: Top telecom stock to buy? What experts suggest — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/reliance-jio-platforms-shares-vs-bharti-airtel-vs-vodafone-idea-top-telecom-stock-to-buy-what-experts-suggest-11793262195751.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

## Watchlist (below surfacing floor)
indices · 2 series ↑ (4.15), dyn_ohi ↑ (4.01), dyn_tech ↑ (3.92), dyn_schd ↑ (3.73), shanghai_comp ↓ (3.55), dyn_jiofin_bo ↓ (3.38), dyn_4417_t ↑ (3.33), usd_cny ↓ (3.31), asx_200 ↑ (3.25), dyn_hdb ↓ (3.11), dyn_techm_ns ↑ (2.95), eur_usd ↓ (2.77)

## India macro
- nifty_50: 22936.7500 (1d 1.05%, z20 1.29, flag none)
- nifty_midcap_100: 57836.8008 (1d 0.99%, z20 -0.50, flag none)
- usd_inr: 95.2100 (1d 0.03%, z20 -0.45, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5216 (1d -0.06%, z20 -1.02, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 98.6 — "MSCI Rejig: LIC, Meesho likely to enter India Standard Index; OFSS, Siemens Energy may be "
- COALINDIA.NS (COAL INDIA LTD) score 98.4 — "MSCI Rejig: LIC, Meesho likely to enter India Standard Index; OFSS, Siemens Energy may be "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 96.7 — "MSCI Rejig: LIC, Meesho likely to enter India Standard Index; OFSS, Siemens Energy may be "
- INDIANB.NS (INDIAN BANK) score 73.9 — "Federal Reserve Board announces approval of application by The Bank of Nova Scotia"
- BAC (Bank of America Corporation) score 65.7 — "CVX - CHEVRON EXPANDS GLOBAL OIL EXPLORATION AS PROFITS SURGE Chevron is accelerating oil "
- OHI (Omega Healthcare Investors, In) score 57.7 — "US MORTGAGE RATES FALL FOR SECOND STRAIGHT WEEK The average 30-year fixed mortgage rate dr"
- TGT (Target Corporation) score 56.9 — "CVX - CHEVRON EXPANDS GLOBAL OIL EXPLORATION AS PROFITS SURGE Chevron is accelerating oil "
- HDB (HDFC Bank Limited) score 56.8 — "Federal Reserve Board announces approval of application by The Bank of Nova Scotia"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.4 — "Federal Reserve Board announces approval of application by The Bank of Nova Scotia"
- IDBI.NS (IDBI BANK LIMITED) score 56.2 — "Federal Reserve Board announces approval of application by The Bank of Nova Scotia"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.2 — "Federal Reserve Board announces approval of application by The Bank of Nova Scotia"
- COIN (Coinbase Global, Inc.) score 52.7 — "CVX - CHEVRON EXPANDS GLOBAL OIL EXPLORATION AS PROFITS SURGE Chevron is accelerating oil "
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.6 — "US MORTGAGE RATES FALL FOR SECOND STRAIGHT WEEK The average 30-year fixed mortgage rate dr"
- CHKP (Check Point Software Technolog) score 42.8 — "Top 3 stocks to buy tomorrow: Kotak Mahindra Bank, Nykaa, Eternal by market expert; check "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.4 — "US MORTGAGE RATES FALL FOR SECOND STRAIGHT WEEK The average 30-year fixed mortgage rate dr"
- TECH (Bio-Techne Corp) score 40.4 — "US MORTGAGE RATES FALL FOR SECOND STRAIGHT WEEK The average 30-year fixed mortgage rate dr"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 36.6 — "ECB OFFICIALS EXPECT DECEMBER RATE HIKE, THEN PAUSE ECB policymakers expect a 25-basis-poi"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.3 — "MICROSOFT EXPECTS TO RAISE ABOUT $25 BILLION IN US BOND SALE - SOURCE"
- LTH (Life Time Group Holdings, Inc.) score 27.2 — "Trump's approval rating on economy hits all-time low as midterm looms: CNBC survey"
- RS (Reliance, Inc.) score 24.6 — "Reliance Power shares on fire! Anil Ambani’s stock jumps 9.22%, but remains down 59% in a "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 23.8 — "Paras Healthcare shares: After IPO listing gains, check what's happening with stock - Buy,"
- 301077.SZ (CHINASTARS) score 22.1 — "BYD Earnings Miss Estimates as China's EV Price War Takes Its Toll"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 21.8 — "Tata Power, JSW Energy, Torrent Power: Ambit sees buying opportunity in power stocks after"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 21.8 — "Tata Power, JSW Energy, Torrent Power: Ambit sees buying opportunity in power stocks after"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 21.4 — "ESAF Small Finance Bank posts Rs 160 crore Q2 profit as asset quality improves"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 16.9 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- JIOFIN.BO (Jio Financial Services Limited) score 15.7 — "Piero Cipollone: Next-day securities settlement, tokenisation and the transformation of Eu"
- SCHD (Schwab US Dividend Equity ETF) score 13.6 — "Godrej Consumer Q2 Results: Profit rises 14% YoY to Rs 523 crore, revenue jumps 19%; co de"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.3 — "ESAF Small Finance Bank posts Rs 160 crore Q2 profit as asset quality improves"
- JEF (Jefferies Financial Group Inc.) score 13.3 — "Top stock to buy today: Jefferies India sees 29% upside in NSE share price in upside scena"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.8 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- SEPN (Septerna, Inc.) score 12.8 — "DALLAS FED'S TRIMMED MEAN PCE PRICE INDEX +2.8% ANNUALIZED IN SEPTEMBER VS AUGUST +2.0%"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.4 — "US MORTGAGE RATES FALL FOR SECOND STRAIGHT WEEK The average 30-year fixed mortgage rate dr"
- META (Meta) score 9.0 — "Shanghai Exchange Halts Duty-Free Metal Delivery Against Futures"
- INFY (Infosys Limited) score 7.9 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- VT (Vanguard Total World Stock Ind) score 7.8 — "World's First Permanent Nuclear Waste Site Wins License in Finland"
- GS (Goldman Sachs Group, Inc. (The) score 5.8 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- SWIGGY.NS (SWIGGY LIMITED) score 2.3 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.7 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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