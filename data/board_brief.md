# Transmission Layer — board brief · 2026-08-26 04:54Z

data as of **2026-08-26** · 98 series · 6 red / 36 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.267, 2d in regime; vol-pct 0.159, breadth-off 0.375, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.28, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.87, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.02, corr60 -0.08, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.26, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.33, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.3, β 0.4321, p 0.0); driver zc 1.69 → expected 0.222%. Type hit-rate 0.816 (n=2368).
- Track record · residual_reversion: hit-rate **0.496** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2368) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.34] cross-asset · 4 series ↑
- brent [COMMODITIES]: last 85.25, z20 -0.68, zc -1.46, resid-z -1.09 [quiet], 1d -3.76%, 1-session move -3.76% ≥ 1.5%
- wti [COMMODITIES]: last 80.31, z20 -0.62, zc -1.02, resid-z -0.76 [quiet], 1d -2.49%, 1-session move -2.49% ≥ 1.5%
- dyn_vt [EQUITIES]: last 160.99, z20 0.57, zc 0.75, resid-z -0.42 [quiet], 1d 0.56%, 1y-pct=98
- dow_jones [INDICES]: last 53572.91, z20 0.30, zc 0.35, resid-z -0.77 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.959 vs dyn_vt, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.944 vs dyn_vt, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.835 vs dyn_vt
- Watch next: vix (inverse) — not yet - watch; rho -0.804 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.597 vs dyn_vt, historically leads by 5d
- Source: Crude oil price drop as Iran-Oman talks raise Hormuz hopes — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/commodities/crude-oil-price-futures-fall-as-iran-oman-discuss-maritime-corridor-in-strait-of-hormuz/article71391402.ece
- Source: Sensex, Nifty rise on crude slump, Iran ceasefire hopes; ICICI Bank leads early gains — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/sensex-nifty-rise-on-crude-slump-iran-ceasefire-hopes-icici-bank-leads-early-gains/article71391362.ece
- Source: Sensex rises over 300 points; Nifty above 24,350 as oil prices slide. What lies ahead? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/sensex-rises-over-200-points-nifty-nears-24350-as-oil-prices-slide-what-lies-ahead/articleshow/133528847.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 6.59] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 158.87, z20 2.93, zc 1.12, resid-z -0.68 [quiet], 1d 14.39%, |z20|=2.93; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.19, z20 2.66, zc 0.81, resid-z -0.65 [quiet], 1d 4.30%, |z20|=2.66
- btc_usd [CRYPTO]: last 78891.04, z20 2.20, zc 0.11, resid-z -0.35 [quiet], 1d 0.38%, |z20|=2.20
- eth_usd [CRYPTO]: last 2460.99, z20 1.94, zc 0.20, resid-z -0.72 [quiet], 1d 0.83%, |z20|=1.94
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 1.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.446 via btc_usd, z 1.54, reacted)
- **India receivers**: nifty_metal (rho 0.446, z 1.54)
- Source: Global Market: Japan stocks rise ahead of Nvidia earnings, US inflation data — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-rise-ahead-of-nvidia-earnings-us-inflation-data/articleshow/133529314.cms
- Source: Global Market: KOSPI rises as investors await Nvidia results for AI trade cues — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-kospi-rises-as-investors-await-nvidia-results-for-ai-trade-cues/articleshow/133529158.cms
- Source: Indian stocks set for strong opening as crude oil falls, global cues improve — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/indian-stocks-set-for-strong-opening-as-crude-oil-falls-global-cues-improve/article71391257.ece
- Historical analogues: 2025-08-11 (d=1.0), 2026-05-05 (d=1.19), 2024-10-31 (d=1.2)

### [RED 6.54] commodities · 2 series ↑
- corn [COMMODITIES]: last 527.50, z20 3.71, zc 4.23, resid-z 1.17 [moved], 1d 5.39%, |z20|=3.71; 1y-pct=100
- wheat [COMMODITIES]: last 712.25, z20 2.91, zc 2.55, resid-z 0.20 [moved], 1d 3.90%, |z20|=2.91; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [AMBER 5.97] cross-asset · 2 series ↑
- comex_copper [COMMODITIES]: last 6.76, z20 1.93, zc 0.31, resid-z 0.99 [quiet], 1d 0.68%, |z20|=1.93; 1y-pct=100; co-occur[metal_copper] suppressed: channel WEAK
- gold_silver_ratio [DERIVED]: last 67.95, z20 -0.13, zc n/a, resid-z n/a [quiet], 1d 0.56%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho -0.427 via gold_silver_ratio, z 1.54, reacted); dyn_stylebaaza_ns (rho -0.416 via gold_silver_ratio, z 0.95, quiet); nifty_midcap_100 (rho -0.369 via gold_silver_ratio, z 1.86, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.543 vs comex_copper, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.704 vs comex_copper
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.5 vs comex_copper, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.568 vs comex_copper
- Watch next: sp500 (co-move) — not yet - watch; rho 0.5 vs comex_copper
- **India receivers**: nifty_metal (rho -0.427, z 1.54); dyn_stylebaaza_ns (rho -0.416, z 0.95); nifty_midcap_100 (rho -0.369, z 1.86)
- Source: Hindustan Copper share price in focus as OFS opens for retail investors today. Should you apply? — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/hindustan-copper-share-price-in-focus-as-ofs-opens-for-retail-investors-today-should-you-apply-11787713785032.html
- Source: Hindustan Copper shares in focus as OFS opens for retail investors. Here are all the details — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-copper-shares-in-focus-as-ofs-opens-for-retail-investors-here-are-all-the-details/articleshow/133528239.cms
- Source: Hindustan Copper OFS opens for retail investors today. Should you apply in the metals major's offer? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-copper-ofs-opens-for-retail-investors-today-should-you-apply-in-the-metals-majors-offer/articleshow/133527323.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.14), 2026-05-15 (d=0.24)

### [RED 5.52] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3135.10, z20 3.52, zc 0.35, resid-z 1.77 [unexplained], 1d 0.92%, |z20|=3.52
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.485 via dyn_adanient_bo, z -0.52, quiet); nifty_midcap_100 (rho 0.465 via dyn_adanient_bo, z 1.86, reacted); dyn_indusindbk_bo (rho 0.445 via dyn_adanient_bo, z -0.23, quiet)
- **India receivers**: nifty_50 (rho 0.485, z -0.52); nifty_midcap_100 (rho 0.465, z 1.86); dyn_indusindbk_bo (rho 0.445, z -0.23)
- Source: Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharashtra | shares rise — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/gautam-adanis-adani-energy-solutions-wins-rs-4-700-crore-transmission-project-in-maharashtra-shares-rise-11787717367517.html
- Source: Market Trading Guide: Adani Enterprises, Dixon Tech among 4 stock recommendations for Wednesday — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-adani-enterprises-dixontechamong-4-stock-recommendations-for-wednesday/slideshow/133515517.cms
- Source: Market wrap: Adani Enterprise, InterGlobe, HDFC Life, HCL Tech, top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprise-interglobe-hdfc-life-hcl-tech-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/133509563.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 4.67] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.65, z20 1.67, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=100); |z20|=1.67; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.453 via midcap_largecap_ratio, z 1.86, reacted); nifty_fmcg (rho -0.367 via midcap_largecap_ratio, z -1.34, reacted); dyn_fincables_ns (rho 0.358 via midcap_largecap_ratio, z 0.88, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.453, z 1.86); nifty_fmcg (rho -0.367, z -1.34); dyn_fincables_ns (rho 0.358, z 0.88)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.49] natgas ↑
- natgas [COMMODITIES]: last 2.86, z20 2.49, zc 1.06, resid-z -0.15 [quiet], 1d 3.29%, |z20|=2.49
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hormuz Crisis Boosts Appeal of $42-Billion Tanzania LNG — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/Hormuz-Crisis-Boosts-Appeal-of-42-Billion-Tanzania-LNG.html
- Source: JPMorgan and Santander Lead $15 Billion Financing Push for Argentina LNG — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/JPMorgan-and-Santander-Lead-15-Billion-Financing-Push-for-Argentina-LNG.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.33] dyn_bond ↑
- dyn_bond [EQUITIES]: last 91.12, z20 2.33, zc 1.69, resid-z -0.49 [priced], 1d 0.51%, |z20|=2.33
- **Mechanism**: dyn_bond ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.927 vs dyn_bond, historically leads by 1d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.736 vs dyn_bond, historically leads by 1d
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.852 vs dyn_bond
- Watch next: wti (inverse) — not yet - watch; rho -0.569 vs dyn_bond, historically leads by 3d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.515 vs dyn_bond, historically leads by 3d
- Source: Yes, Federal, RBL put dollar bond plans on hold — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/bonds/yes-federal-rbl-put-dollar-bond-plans-on-hold/articleshow/133527256.cms
- Source: JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock and bond settlements using blockchain technology, according to Nikkei. The FSA, Finance Ministry, Bank of Japan and financial institutions will launch a study group this summer. A — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35047
- Source: Japanese bond funds see record inflows as rising yields attract global investors — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/japanese-bond-funds-see-record-inflows-as-rising-yields-attract-global-investors/articleshow/133518488.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-11 (d=0.01), 2026-05-06 (d=0.01)

## Watchlist (below surfacing floor)
dyn_muthootfin_ns ↑ (4.32), comex_gold ↑ (3.89), rates · 2 series ↑ (3.39), dyn_lenskart_ns ↑ (3.31), fx · 2 series ↑ (2.99), dyn_tech ↑ (2.99), dyn_icicigi_bo ↓ (2.95), indices · 2 series ↑ (2.85), dyn_atherenerg_ns ↑ (2.47), dyn_idbi_ns ↑ (2.33), dyn_cartrade_ns ↑ (2.25), dyn_karurvysya_ns ↑ (2.19)

## India macro
- nifty_50: 24304.5996 (1d -0.12%, z20 -0.52, flag none)
- nifty_midcap_100: 64322.6484 (1d 0.25%, z20 1.86, flag amber)
- usd_inr: 95.4020 (1d -0.34%, z20 -0.36, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6465 (1d 0.37%, z20 1.67, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 82.8 — "Stocks to buy in 2026 for long term: Cummins India, Indian Hotels among 5 stocks that coul"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.5 — "Stock recommendations for 26 August from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 77.3 — "Stock recommendations for 26 August from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.8 — "Stock recommendations for 26 August from MarketSmith India"
- BAC (Bank of America Corporation) score 75.2 — "Sensex Today | Nifty 50 | Stock Market LIVE Updates: Sensex jumps over 250 pts, Nifty abov"
- HDB (HDFC Bank Limited) score 69.0 — "Sensex Today | Nifty 50 | Stock Market LIVE Updates: Sensex jumps over 250 pts, Nifty abov"
- IDBI.NS (IDBI BANK LIMITED) score 64.1 — "Sensex Today | Nifty 50 | Stock Market LIVE Updates: Sensex jumps over 250 pts, Nifty abov"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 64.1 — "Sensex Today | Nifty 50 | Stock Market LIVE Updates: Sensex jumps over 250 pts, Nifty abov"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 64.1 — "Sensex Today | Nifty 50 | Stock Market LIVE Updates: Sensex jumps over 250 pts, Nifty abov"
- BOND (PIMCO Active Bond Exchange-Tra) score 64.1 — "Yes, Federal, RBL put dollar bond plans on hold"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Daily Performance"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Daily Performance"
- TECH (Bio-Techne Corp) score 52.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Daily Performance"
- COIN (Coinbase Global, Inc.) score 49.6 — "Indian stocks set for strong opening as crude oil falls, global cues improve"
- OHI (Omega Healthcare Investors, In) score 46.8 — "Hindustan Copper OFS opens for retail investors today. Should you apply in the metals majo"
- LTH (Life Time Group Holdings, Inc.) score 33.7 — "RUBIO HAS TOLD SEVERAL OF HIS FOREIGN COUNTERPARTS IN RECENT DAYS THAT "FOR TIME BEING" U."
- CHKP (Check Point Software Technolog) score 30.5 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- 301077.SZ (CHINASTARS) score 24.0 — "China Defies U.S. Economic D-Day against Iran"
- NVDA (NVIDIA Corporation) score 21.7 — "Global Market: KOSPI rises as investors await Nvidia results for AI trade cues"
- JIOFIN.BO (Jio Financial Services Limited) score 20.5 — "ONGC Share Price Live Updates: ONGC's Financial Snapshot"
- MS (Morgan Stanley) score 17.1 — "Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.8 — "Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharasht"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.3 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.0 — "Indus Towers to AU Small Finance Bank - Jay Thakkar suggests 3 stocks to buy or sell for s"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 15.9 — "Hindustan Copper OFS opens for retail investors today. Should you apply in the metals majo"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.2 — "ONGC Share Price Live Updates: ONGC's Financial Snapshot"
- META (Meta) score 10.2 — "Hindustan Copper OFS opens for retail investors today. Should you apply in the metals majo"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.4 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Sees Positive Movement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.1 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Sees Positive Movement"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.6 — "Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharasht"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.2 — "ICICI Bank Share Price Live Updates: ICICI Bank Shows Strong Market Performance"
- VT (Vanguard Total World Stock Ind) score 7.0 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.6 — "U.S. HOME PRICES BEAT EXPECTATIONS IN JUNE U.S. 20-city home prices rose 0.2% month-over-m"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 5.9 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- JEF (Jefferies Financial Group Inc.) score 4.7 — "Jefferies picks 4 NBFCs with up to 20% upside that may continue outperforming Nifty, bank "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.5 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 3.2 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 0.7 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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