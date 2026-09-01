# Transmission Layer — board brief · 2026-09-01 19:23Z

data as of **2026-09-01** · 96 series · 16 red / 28 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.352, 1d in regime; vol-pct 0.292, breadth-off 0.412, Markov P(high-vol) 0.022)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.4, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.12, corr60 0.0, last shift 2026-07-16. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.39, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.24, corr60 -0.15, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.12, corr60 0.21, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 88** scanned series survive multiplicity control (effective p ≤ 0.0015243893761345273)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.49, β 0.2162, p 0.0); driver zc 2.79 → expected 0.721%. Type hit-rate 0.828 (n=1964).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2342, p 0.0); driver zc 1.61 → expected 0.392%. Type hit-rate 0.828 (n=1964).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.351, β -0.1179, p 0.0); driver zc 2.79 → expected -0.393%. Type hit-rate 0.828 (n=1964).
- Track record · residual_reversion: hit-rate **0.499** (n=1090) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1964) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.17] cross-asset · 11 series ↓
- russell_2000 [INDICES]: last 2920.26, z20 -3.65, zc -1.02, resid-z -0.54 [quiet], 1d -1.22%, |z20|=3.65
- stoxx_50 [INDICES]: last 6364.29, z20 -2.86, zc -1.02, resid-z -0.38 [quiet], 1d -0.87%, |z20|=2.86
- dow_jones [INDICES]: last 52773.35, z20 -2.43, zc -1.11, resid-z 0.30 [quiet], 1d -0.78%, |z20|=2.43
- wti [COMMODITIES]: last 90.42, z20 2.29, zc 2.62, resid-z 1.47 [moved], 1d 5.43%, 1-session move +5.43% ≥ 1.5%; |z20|=2.29
- dyn_vt [EQUITIES]: last 159.29, z20 -2.27, zc -1.13, resid-z 0.35 [quiet], 1d -0.78%, |z20|=2.27
- dax [INDICES]: last 25957.69, z20 -2.17, zc -1.47, resid-z -0.73 [quiet], 1d -1.14%, |z20|=2.17
- sp500 [INDICES]: last 7630.34, z20 -2.11, zc -1.03, resid-z -0.32 [quiet], 1d -0.73%, |z20|=2.11
- cac_40 [INDICES]: last 8291.73, z20 -2.02, zc -0.52, resid-z 0.35 [quiet], 1d -0.51%, |z20|=2.02
- vix [INDICES]: last 16.33, z20 1.96, zc 1.25, resid-z n/a [quiet], 1d 9.45%, |z20|=1.96
- nasdaq_100 [INDICES]: last 29067.75, z20 -1.67, zc -1.22, resid-z -0.39 [quiet], 1d -1.32%, |z20|=1.67
- brent [COMMODITIES]: last 95.00, z20 1.65, zc 2.34, resid-z 1.35 [moved], 1d 4.98%, 1-session move +4.98% ≥ 1.5%; |z20|=1.65
- **Mechanism**: cross-asset · 11 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.54).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.471 via dax, z -2.55, reacted); nifty_midcap_100 (rho 0.443 via dax, z -1.77, reacted); dyn_indusindbk_bo (rho 0.42 via cac_40, z -1.16, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.632 vs stoxx_50, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.581 vs dax, historically leads by 4d
- Watch next: kospi (co-move) — not yet - watch; rho 0.427 vs nasdaq_100, historically leads by 1d
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.418 vs dyn_vt, historically leads by 1d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.597 vs dyn_vt
- **India receivers**: dyn_adanient_bo (rho 0.471, z -2.55); nifty_midcap_100 (rho 0.443, z -1.77); dyn_indusindbk_bo (rho 0.42, z -1.16)
- Source: Wall Street dips as higher yields, rising oil prices mark shaky start to September — Mint Markets, 2026-09-01. https://www.livemint.com/market/wall-street-dips-as-higher-yields-rising-oil-prices-mark-shaky-start-to-september-11788287811841.html
- Source: Global oil prices surge above $94  a barrel after the U.S. strikes Iranian targets — MarketWatch Top, 2026-09-01. https://www.marketwatch.com/story/global-oil-prices-extend-move-over-90-after-report-of-two-tankers-struck-in-hormuz-0effd708?mod=mw_rss_topstories
- Source: U.S.-Iran Strikes Put $100 Oil Back in Focus — OilPrice, 2026-09-01. https://oilprice.com/Energy/Crude-Oil/US-Iran-Strikes-Put-100-Oil-Back-in-Focus.html
- Historical analogues: 2024-11-26 (d=0.54), 2024-10-21 (d=0.71), 2024-11-14 (d=0.75)

### [RED 8.0] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 89.75, z20 -4.33, zc -2.37, resid-z 0.00 [priced], 1d -0.74%, |z20|=4.33; 1y-pct=0
- ust_2y [RATES]: last 4.34, z20 4.03, zc 2.79, resid-z 2.28 [unexplained], 1d 3.33%, |z20|=4.03; 1y-pct=99
- ust_10y [RATES]: last 4.73, z20 1.35, zc 1.32, resid-z 0.99 [quiet], 1d 1.28%, 1y-pct=99
- tips_10y_real [RATES]: last 2.42, z20 0.58, zc 2.13, resid-z 1.76 [unexplained], 1d 3.42%, 1d move +8.0bps ≥ 5bps; 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.818 vs dyn_bond
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.338 vs ust_2y, historically leads by 1d
- Source: Gold falls to two-week low as rising Treasury yields, dollar weigh — Mint Markets, 2026-09-01. https://www.livemint.com/market/gold-falls-to-two-week-low-as-rising-treasury-yields-dollar-weigh-11788288241495.html
- Source: This could be the 10-year Treasury’s tipping point into the danger zone — MarketWatch Top, 2026-09-01. https://www.marketwatch.com/story/this-could-be-the-10-year-treasurys-tipping-point-into-the-danger-zone-891cd45d?mod=mw_rss_topstories
- Source: US Treasury bond yields ease from highs after data as Iran war escalation fans inflation concerns — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/news/us-treasury-bond-yields-ease-from-highs-after-data-as-iran-war-escalation-fans-inflation-concerns/articleshow/133686615.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.31), 2025-05-23 (d=0.52)

### [RED 6.11] commodities · 3 series ↑
- soybeans [COMMODITIES]: last 1318.50, z20 2.79, zc 3.31, resid-z 3.17 [unexplained], 1d 3.39%, |z20|=2.79; 1y-pct=100
- corn [COMMODITIES]: last 545.50, z20 2.68, zc 4.64, resid-z 3.84 [unexplained], 1d 5.92%, |z20|=2.68; 1y-pct=100
- wheat [COMMODITIES]: last 781.00, z20 2.56, zc 1.47, resid-z 1.51 [unexplained], 1d 3.24%, |z20|=2.56; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Australia Raises Wheat Crop Forecast as Export Demand Picks Up — Mint Markets, 2026-08-31. https://www.livemint.com/market/australia-raises-wheat-crop-forecast-as-export-demand-picks-up-11788215862266.html
- Source: Chicago wheat falls on selling pressure after recent highs — Mint Markets, 2026-08-31. https://www.livemint.com/market/chicago-wheat-falls-on-selling-pressure-after-recent-highs-11788203489599.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.4] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1725.60, z20 3.40, zc 0.14, resid-z -0.22 [quiet], 1d 0.46%, |z20|=3.40; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy surges 130% in 2026, outpacing Tesla, BYD — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/ather-energy-surges-130-in-2026-outpacing-tesla-byd/article71414201.ece
- Source: Ather Energy’s 130% stock surge leaves Tesla and BYD behind in 2026 — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/stocks/news/ather-energys-130-stock-surge-leaves-tesla-and-byd-behind-in-2026/articleshow/133672575.cms
- Source: Ather Energy share price hits lifetime high | Delivers 423% returns from IPO price — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-hits-lifetime-high-delivers-423-returns-from-ipo-price-11788162211726.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 4.66] dyn_lth ↓
- dyn_lth [EQUITIES]: last 41.82, z20 -2.66, zc -0.20, resid-z -0.94 [quiet], 1d -0.48%, |z20|=2.66
- **Mechanism**: dyn_lth ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: Japan bond yields hit 3% for first time in 30 years amid inflation, fiscal risks — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-bond-yields-hit-3-for-first-time-in-30-years-amid-inflation-fiscal-risks/articleshow/133671709.cms
- Source: Stocks to watch and why on September 1: PVR INOX, E2E Networks, NCC, Brigade Enterprises, Time Technoplast and more — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/stocks-to-watch-and-why-on-september-1-pvr-inox-e2e-networks-ncc-brigade-enterprises-indegene-and-more-11788197253602.html
- Source: BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent defended his U.S. bond-market intervention after criticism from Stanley Druckenmiller. Bessent suggested the veteran investor “lost money” around the time he submitted his critical op-ed. He also defended Treasur — DeItaone, 2026-08-31. https://t.me/walter_bloomberg/35250
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 4.55] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2863.25, z20 -2.55, zc -1.06, resid-z -0.77 [quiet], 1d -1.98%, |z20|=2.55
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.524 via dyn_adanient_bo, z -1.77, reacted); nifty_50 (rho 0.505 via dyn_adanient_bo, z -1.52, reacted); dyn_indusindbk_bo (rho 0.389 via dyn_adanient_bo, z -1.16, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.524, z -1.77); nifty_50 (rho 0.505, z -1.52); dyn_indusindbk_bo (rho 0.389, z -1.16)
- Source: Adani Power leads group rally as buying bets lift sentiment — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/adani-power-leads-group-rally-as-buying-bets-lift-sentiment/article71414084.ece
- Source: How Adani Group stocks are performing today after share prices plunged yesterday | Top gainers and losers — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/adani-green-to-adani-power-how-adani-group-stocks-are-performing-today-after-share-prices-plunged-yesterday-11788241077630.html
- Source: Adani group stocks face heavy selling pressure; Adani Enterprises tumbles nearly 8% — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/adani-group-stocks-face-heavy-selling-pressure-adani-enterprises-tumbles-nearly-8/articleshow/133657152.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.14] natgas ↑
- natgas [COMMODITIES]: last 2.94, z20 2.14, zc 0.03, resid-z 0.24 [quiet], 1d 0.10%, |z20|=2.14
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.045 vs natgas, historically leads by 4d
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.004 vs natgas, historically leads by 4d
- Source: Asia Spot LNG Prices Hit 5-Month High as Hormuz Blockage Drags On — OilPrice, 2026-09-01. https://oilprice.com/Latest-Energy-News/World-News/Asia-Spot-LNG-Prices-Hit-5-Month-High-as-Hormuz-Blockage-Drags-On.html
- Source: U.S. LNG exports rose 23% in the first half of 2026 because of higher capacity — EIA Today in Energy, 2026-09-01. https://www.eia.gov/todayinenergy/detail.php?id=
- Source: Russia Doubles Dark Fleet to Ship LNG to Asia — OilPrice, 2026-09-01. https://oilprice.com/Latest-Energy-News/World-News/Russia-Doubles-Dark-Fleet-to-Ship-LNG-to-Asia.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.01] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1567.00, z20 -2.01, zc 0.31, resid-z 0.46 [quiet], 1d 0.46%, |z20|=2.01; 1y-pct=1
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Narayanan of ICICI Pru AMC — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/expert-view-favour-value-over-growth-it-not-an-outright-contra-bet-says-chockalingam-narayanan-of-icici-pru-amc-11788256314458.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

## Watchlist (below surfacing floor)
usd_jpy ↑ (3.88), nifty_50 ↓ (3.52), midcap_largecap_ratio ↑ (3.43), dyn_lenskart_ns ↑ (3.36), ust_2s10s ↓ (3.35), dyn_hdb ↓ (3.18), gold_silver_ratio ↑ (3.04), sofr ↑ (2.83), dyn_inoxindia_ns ↑ (2.55), dyn_havells_ns ↓ (2.54), bovespa ↑ (2.15), taiwan_weighted ↑ (2.11)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.4 — "Brigade Group opens PVR INOX Cinemas at Whitefield township; stock slips 2.2%"
- COALINDIA.NS (COAL INDIA LTD) score 75.9 — "Indian govt tightens sugar stock limit, cuts traders’ limit by half"
- INDIANB.NS (INDIAN BANK) score 74.8 — "BESSENT ON IRAN, SANCTIONS: PROBABLY GOING TO ANNOUNCE BANK SANCTION THIS WEEK AND NEXT WE"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 73.3 — "Indian govt tightens sugar stock limit, cuts traders’ limit by half"
- BAC (Bank of America Corporation) score 67.1 — "BESSENT ON IRAN, SANCTIONS: PROBABLY GOING TO ANNOUNCE BANK SANCTION THIS WEEK AND NEXT WE"
- HDB (HDFC Bank Limited) score 58.8 — "BESSENT ON IRAN, SANCTIONS: PROBABLY GOING TO ANNOUNCE BANK SANCTION THIS WEEK AND NEXT WE"
- IDBI.NS (IDBI BANK LIMITED) score 56.7 — "BESSENT ON IRAN, SANCTIONS: PROBABLY GOING TO ANNOUNCE BANK SANCTION THIS WEEK AND NEXT WE"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.7 — "BESSENT ON IRAN, SANCTIONS: PROBABLY GOING TO ANNOUNCE BANK SANCTION THIS WEEK AND NEXT WE"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.7 — "BESSENT ON IRAN, SANCTIONS: PROBABLY GOING TO ANNOUNCE BANK SANCTION THIS WEEK AND NEXT WE"
- COIN (Coinbase Global, Inc.) score 49.8 — "MUSK SAYS SEEING SIGNIFICANT PRODUCTIVITY GAINS FROM AI MUSK SAYS AI TO INCREASE GLOBAL EC"
- BOND (PIMCO Active Bond Exchange-Tra) score 45.4 — "30-YEAR TREASURY YIELD ERASES INTERVENTION DROP The 30-year Treasury yield surged as high "
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.7 — "Hy-Tech Engineers hits upper circuit after strong debut; Symbiotec, Skyways end above list"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.2 — "Hy-Tech Engineers hits upper circuit after strong debut; Symbiotec, Skyways end above list"
- TECH (Bio-Techne Corp) score 35.1 — "Hy-Tech Engineers hits upper circuit after strong debut; Symbiotec, Skyways end above list"
- OHI (Omega Healthcare Investors, In) score 32.3 — "Why Japan's 30-year high bond yields should worry Indian stock market investors"
- 301077.SZ (CHINASTARS) score 31.1 — "BESSENT ON TRADE: WE DO NOT WANT TO PULL APART FROM CHINA BESSENT ON TRADE: WE HAVE TO DER"
- LTH (Life Time Group Holdings, Inc.) score 30.6 — "BANK OF AMERICA VP KILLED IN TIMES SQUARE ATTACK Bank of America Vice President Erin Piace"
- CHKP (Check Point Software Technolog) score 27.6 — "Gold, Silver Price Outlook: Can gold prices hit  ₹1,70,000 per 10 grams after Jackson Hole"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.5 — "BESSENT: IRAN PROBABLY HAS WORLD'S 3RD-GREATEST ENERGY RESOURCE"
- NVDA (NVIDIA Corporation) score 18.4 — "SB Energy heads for IPO after Nvidia backs $105 billion OpenAI data-centre project"
- PCJEWELLER.NS (PC JEWELLER LTD) score 15.8 — "Tata CliQ Luxury becomes exclusive online platform for Manish Malhotra’s fine jewellery"
- JIOFIN.BO (Jio Financial Services Limited) score 14.8 — "SAT dismisses Omaxe appeal against SEBI order over financial statement irregularities"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.6 — "Food Inflation Jumps as Higher Energy Costs Hit UK Retailers"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.1 — "Muthoot Finance approves Muthoot Money merger to create larger gold loan business"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.2 — "How Adani Group stocks are performing today after share prices plunged yesterday | Top gai"
- MS (Morgan Stanley) score 9.3 — "JPMORGAN: RISING YIELDS WON’T KILL STOCK RALLY JPMorgan remains bullish on global equities"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.0 — "Mahanadi Coalfields IPO: Coal India to sell 10% stake"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.9 — "Tata CliQ Luxury becomes exclusive online platform for Manish Malhotra’s fine jewellery"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.9 — "Tata CliQ Luxury becomes exclusive online platform for Manish Malhotra’s fine jewellery"
- META (Meta) score 8.3 — "Battle of metals: Gold or silver? What should investors choose as Warsh stokes rate hike f"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "upGrad completes Unacademy acquisition at just over $200 million, marking steep valuation "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.8 — "SAT dismisses Omaxe appeal against SEBI order over financial statement irregularities"
- VT (Vanguard Total World Stock Ind) score 7.3 — "BESSENT: IRAN PROBABLY HAS WORLD'S 3RD-GREATEST ENERGY RESOURCE"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.1 — "Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Na"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.2 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- DKS (Dick's Sporting Goods Inc) score 1.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.9 — "Can Wolfe’s upgrade push Moderna stock higher?"
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