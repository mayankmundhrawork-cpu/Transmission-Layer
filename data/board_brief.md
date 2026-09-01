# Transmission Layer — board brief · 2026-09-01 14:51Z

data as of **2026-09-01** · 96 series · 15 red / 28 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.258, 2d in regime; vol-pct 0.223, breadth-off 0.294, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.39, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.01, last shift 2026-07-16. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.31, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.15, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.21, corr60 0.21, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 88** scanned series survive multiplicity control (effective p ≤ 0.0005014137825609666)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.49, β 0.2162, p 0.0); driver zc 2.79 → expected 0.721%. Type hit-rate 0.828 (n=1992).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2342, p 0.0); driver zc 1.89 → expected 0.46%. Type hit-rate 0.828 (n=1992).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.351, β -0.1179, p 0.0); driver zc 2.79 → expected -0.393%. Type hit-rate 0.828 (n=1992).
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.302, β 0.4336, p 0.0); driver zc -1.76 → expected -0.237%. Type hit-rate 0.828 (n=1992).
- Track record · residual_reversion: hit-rate **0.499** (n=1090) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1992) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.47] cross-asset · 5 series ↓
- russell_2000 [INDICES]: last 2942.70, z20 -2.82, zc -0.39, resid-z -0.03 [quiet], 1d -0.47%, |z20|=2.82
- dow_jones [INDICES]: last 53013.53, z20 -1.74, zc -0.46, resid-z 0.19 [quiet], 1d -0.32%, |z20|=1.74
- wti [COMMODITIES]: last 87.85, z20 1.54, zc 1.17, resid-z 0.62 [quiet], 1d 2.44%, 1-session move +2.44% ≥ 1.5%; |z20|=1.54
- sp500 [INDICES]: last 7654.15, z20 -1.53, zc -0.59, resid-z -0.32 [quiet], 1d -0.42%, |z20|=1.53
- brent [COMMODITIES]: last 92.28, z20 0.98, zc 0.93, resid-z 0.46 [quiet], 1d 1.98%, 1-session move +1.98% ≥ 1.5%
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.563 vs dow_jones, historically leads by 5d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.504 vs sp500, historically leads by 5d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.503 vs dow_jones, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.618 vs russell_2000
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.606 vs sp500
- Source: Oil up more than 2% as renewed US-Iran strikes stoke supply fears — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/news/oil-up-more-than-2-as-renewed-us-iran-strikes-stoke-supply-fears/articleshow/133684457.cms
- Source: Oil tops $90 as inflation fears push US 10-year yield to highest since January 2025 — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/oil-tops-90-as-inflation-fears-push-us-10-year-yield-to-highest-since-january-2025-11788270385773.html
- Source: India’s economic growth fails to boost market performance amid rising crude prices — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/indias-economic-growth-fails-to-boost-market-performance-amid-rising-crude-prices/article71415170.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.47), 2024-10-18 (d=0.52)

### [RED 7.69] cross-asset · 4 series ↑
- ust_2y [RATES]: last 4.34, z20 4.03, zc 2.79, resid-z 2.28 [unexplained], 1d 3.33%, |z20|=4.03; 1y-pct=99
- dyn_bond [EQUITIES]: last 89.93, z20 -3.54, zc -1.76, resid-z 0.00 [priced], 1d -0.55%, |z20|=3.54; 1y-pct=0
- ust_10y [RATES]: last 4.73, z20 1.35, zc 1.32, resid-z 0.99 [quiet], 1d 1.28%, 1y-pct=99
- tips_10y_real [RATES]: last 2.42, z20 0.58, zc 2.13, resid-z 1.76 [unexplained], 1d 3.42%, 1d move +8.0bps ≥ 5bps; 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.839 vs dyn_bond
- Watch next: brent (inverse) — not yet - watch; rho -0.551 vs dyn_bond
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.338 vs ust_2y, historically leads by 1d
- Source: Are rising bond rates really so bad? Maybe not, say these experts. — MarketWatch Top, 2026-09-01. https://www.marketwatch.com/story/are-rising-bond-rates-really-so-bad-maybe-not-say-these-exports-1af9e683?mod=mw_rss_topstories
- Source: US bond yields reflect 'flat to down' inflation expectations, stronger growth, Bessent says — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/news/us-bond-yields-reflect-flat-to-down-inflation-expectations-stronger-growth-bessent-says/articleshow/133684502.cms
- Source: Oil tops $90 as inflation fears push US 10-year yield to highest since January 2025 — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/oil-tops-90-as-inflation-fears-push-us-10-year-yield-to-highest-since-january-2025-11788270385773.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.31), 2025-05-23 (d=0.52)

### [RED 6.01] commodities · 3 series ↑
- soybeans [COMMODITIES]: last 1314.25, z20 2.69, zc 2.99, resid-z 2.72 [unexplained], 1d 3.06%, |z20|=2.69; 1y-pct=100
- wheat [COMMODITIES]: last 785.00, z20 2.65, zc 1.71, resid-z 1.61 [unexplained], 1d 3.77%, |z20|=2.65; 1y-pct=100
- corn [COMMODITIES]: last 544.50, z20 2.65, zc 4.49, resid-z 3.48 [unexplained], 1d 5.73%, |z20|=2.65; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Australia Raises Wheat Crop Forecast as Export Demand Picks Up — Mint Markets, 2026-08-31. https://www.livemint.com/market/australia-raises-wheat-crop-forecast-as-export-demand-picks-up-11788215862266.html
- Source: Chicago wheat falls on selling pressure after recent highs — Mint Markets, 2026-08-31. https://www.livemint.com/market/chicago-wheat-falls-on-selling-pressure-after-recent-highs-11788203489599.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.4] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1725.60, z20 3.40, zc 0.14, resid-z -0.13 [quiet], 1d 0.46%, |z20|=3.40; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy surges 130% in 2026, outpacing Tesla, BYD — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/ather-energy-surges-130-in-2026-outpacing-tesla-byd/article71414201.ece
- Source: Ather Energy’s 130% stock surge leaves Tesla and BYD behind in 2026 — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/stocks/news/ather-energys-130-stock-surge-leaves-tesla-and-byd-behind-in-2026/articleshow/133672575.cms
- Source: Ather Energy share price hits lifetime high | Delivers 423% returns from IPO price — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-hits-lifetime-high-delivers-423-returns-from-ipo-price-11788162211726.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 4.55] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2863.25, z20 -2.55, zc -1.06, resid-z -1.00 [quiet], 1d -1.98%, |z20|=2.55
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.524 via dyn_adanient_bo, z -1.77, reacted); nifty_50 (rho 0.505 via dyn_adanient_bo, z -1.52, reacted); dyn_indusindbk_bo (rho 0.389 via dyn_adanient_bo, z -1.16, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.524, z -1.77); nifty_50 (rho 0.505, z -1.52); dyn_indusindbk_bo (rho 0.389, z -1.16)
- Source: Adani Power leads group rally as buying bets lift sentiment — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/adani-power-leads-group-rally-as-buying-bets-lift-sentiment/article71414084.ece
- Source: How Adani Group stocks are performing today after share prices plunged yesterday | Top gainers and losers — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/adani-green-to-adani-power-how-adani-group-stocks-are-performing-today-after-share-prices-plunged-yesterday-11788241077630.html
- Source: Adani group stocks face heavy selling pressure; Adani Enterprises tumbles nearly 8% — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/adani-group-stocks-face-heavy-selling-pressure-adani-enterprises-tumbles-nearly-8/articleshow/133657152.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.32] dyn_lth ↓
- dyn_lth [EQUITIES]: last 42.15, z20 -2.32, zc 0.13, resid-z -0.94 [quiet], 1d 0.30%, |z20|=2.32
- **Mechanism**: dyn_lth ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: Japan bond yields hit 3% for first time in 30 years amid inflation, fiscal risks — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-bond-yields-hit-3-for-first-time-in-30-years-amid-inflation-fiscal-risks/articleshow/133671709.cms
- Source: Stocks to watch and why on September 1: PVR INOX, E2E Networks, NCC, Brigade Enterprises, Time Technoplast and more — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/stocks-to-watch-and-why-on-september-1-pvr-inox-e2e-networks-ncc-brigade-enterprises-indegene-and-more-11788197253602.html
- Source: BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent defended his U.S. bond-market intervention after criticism from Stanley Druckenmiller. Bessent suggested the veteran investor “lost money” around the time he submitted his critical op-ed. He also defended Treasur — DeItaone, 2026-08-31. https://t.me/walter_bloomberg/35250
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [AMBER 4.01] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1567.00, z20 -2.01, zc 0.31, resid-z 0.42 [quiet], 1d 0.46%, |z20|=2.01; 1y-pct=1
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Narayanan of ICICI Pru AMC — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/expert-view-favour-value-over-growth-it-not-an-outright-contra-bet-says-chockalingam-narayanan-of-icici-pru-amc-11788256314458.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 3.98] indices · 3 series ↓
- stoxx_50 [INDICES]: last 6372.76, z20 -2.66, zc -0.87, resid-z -0.73 [quiet], 1d -0.74%, |z20|=2.66
- dax [INDICES]: last 25982.47, z20 -1.99, zc -1.35, resid-z -1.00 [quiet], 1d -1.05%, |z20|=1.99
- cac_40 [INDICES]: last 8299.61, z20 -1.96, zc -0.43, resid-z -0.26 [quiet], 1d -0.42%, |z20|=1.96
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.47 via dax, z -2.55, reacted); nifty_midcap_100 (rho 0.439 via dax, z -1.77, reacted); dyn_indusindbk_bo (rho 0.42 via cac_40, z -1.16, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.621 vs stoxx_50, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.583 vs dax, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.533 vs stoxx_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.512 vs cac_40
- **India receivers**: dyn_adanient_bo (rho 0.47, z -2.55); nifty_midcap_100 (rho 0.439, z -1.77); dyn_indusindbk_bo (rho 0.42, z -1.16)
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-14 (d=0.36), 2025-04-16 (d=0.39)

## Watchlist (below surfacing floor)
dyn_hdb ↓ (3.66), usd_jpy ↑ (3.65), nifty_50 ↓ (3.52), midcap_largecap_ratio ↑ (3.43), dyn_lenskart_ns ↑ (3.36), ust_2s10s ↓ (3.35), gold_silver_ratio ↓ (3.14), sofr ↑ (2.83), hy_oas ↓ (2.64), dyn_inoxindia_ns ↑ (2.55), dyn_havells_ns ↓ (2.54), dyn_tech ↑ (2.34)

## India macro
- nifty_50: 24055.8008 (1d -0.10%, z20 -1.52, flag amber)
- nifty_midcap_100: 63333.2500 (1d -1.39%, z20 -1.77, flag amber)
- usd_inr: 94.9400 (1d -0.46%, z20 -0.89, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6328 (1d -1.29%, z20 0.43, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.2 — "Price, Not Politics, Is Driving Most of India’s Oil Buying"
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.7 — "Price, Not Politics, Is Driving Most of India’s Oil Buying"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.4 — "Price, Not Politics, Is Driving Most of India’s Oil Buying"
- INDIANB.NS (INDIAN BANK) score 72.9 — "Market close: Sensex, Nifty end lower as losses in banking, auto drag"
- BAC (Bank of America Corporation) score 63.9 — "Market close: Sensex, Nifty end lower as losses in banking, auto drag"
- HDB (HDFC Bank Limited) score 57.3 — "Market close: Sensex, Nifty end lower as losses in banking, auto drag"
- IDBI.NS (IDBI BANK LIMITED) score 55.0 — "Market close: Sensex, Nifty end lower as losses in banking, auto drag"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 55.0 — "Market close: Sensex, Nifty end lower as losses in banking, auto drag"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 55.0 — "Market close: Sensex, Nifty end lower as losses in banking, auto drag"
- COIN (Coinbase Global, Inc.) score 48.9 — "Global Market: European shares muted as bond yields surge on inflation concerns"
- BOND (PIMCO Active Bond Exchange-Tra) score 44.3 — "Global Market: European shares muted as bond yields surge on inflation concerns"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.3 — "Hy-Tech Engineers hits upper circuit after strong debut; Symbiotec, Skyways end above list"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.7 — "Hy-Tech Engineers hits upper circuit after strong debut; Symbiotec, Skyways end above list"
- TECH (Bio-Techne Corp) score 36.7 — "Hy-Tech Engineers hits upper circuit after strong debut; Symbiotec, Skyways end above list"
- OHI (Omega Healthcare Investors, In) score 33.8 — "Why Japan's 30-year high bond yields should worry Indian stock market investors"
- LTH (Life Time Group Holdings, Inc.) score 30.9 — "Fly-Hi Maritime, Farm Peace IPOs open today: Check price, lot size, GMP and key dates"
- 301077.SZ (CHINASTARS) score 30.4 — "Glacier risk hangs over China-Nepal border as region remembers mudslide victims"
- CHKP (Check Point Software Technolog) score 28.8 — "Gold, Silver Price Outlook: Can gold prices hit  ₹1,70,000 per 10 grams after Jackson Hole"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.5 — "U.S. Energy Storage Capacity Installations Hit Record High in Q2"
- NVDA (NVIDIA Corporation) score 18.2 — "Multibagger AI stock in focus after bagging Rs 1,000 crore term sheet to provide Nvidia Bl"
- PCJEWELLER.NS (PC JEWELLER LTD) score 15.4 — "Deepa Jewellers IPO opens for bidding, GMP at 31%: Should you apply or avoid?"
- JIOFIN.BO (Jio Financial Services Limited) score 14.4 — "Broker’s Call: Medi Assist Healthcare Services (Buy)"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.1 — "FOMO alert: Retail investors sold 1,051 stocks before they soared 36% on average"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.6 — "Muthoot Finance approves Muthoot Money merger to create larger gold loan business"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.7 — "How Adani Group stocks are performing today after share prices plunged yesterday | Top gai"
- META (Meta) score 8.7 — "Battle of metals: Gold or silver? What should investors choose as Warsh stokes rate hike f"
- MS (Morgan Stanley) score 8.7 — "BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent de"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.4 — "Solar Overtakes Coal as China's Largest Power Source"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.3 — "Tata Elxsi, Sarla Aviation sign MoU to build India’s first indigenous eVTOL aircraft"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.2 — "Tata Elxsi, Sarla Aviation sign MoU to build India’s first indigenous eVTOL aircraft"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.3 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.1 — "Milky Mist Q1 Results: After strong IPO debut, profit and revenue surge | What financials "
- VT (Vanguard Total World Stock Ind) score 6.5 — "Refinery to the world: Energy expert Anas Alhajji on India's surprising fuel advantage"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.3 — "Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Na"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.4 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- DKS (Dick's Sporting Goods Inc) score 1.3 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 1.0 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.2 — "Voltas reported strong growth in June quarter, but failed to impress"

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