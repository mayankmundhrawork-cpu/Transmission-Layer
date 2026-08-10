# Transmission Layer — board brief · 2026-08-10 13:41Z

data as of **2026-08-10** · 98 series · 7 red / 39 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.318, 1d in regime; vol-pct 0.448, breadth-off 0.188, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.39, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.37, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.06, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.23, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.12, corr60 0.17, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.00019147977053779464)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1129) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2362) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.37] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4396.30, z20 3.47, zc 0.64, resid-z 0.24 [quiet], 1d 1.28%, |z20|=3.47; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.21, z20 2.95, zc 0.51, resid-z -0.29 [quiet], 1d 1.39%, |z20|=2.95; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3034.49, z20 2.30, zc 0.88, resid-z 0.88 [quiet], 1d 1.10%, |z20|=2.30; 1y-pct=99
- stoxx_50 [INDICES]: last 6540.79, z20 2.19, zc 0.31, resid-z 0.57 [quiet], 1d 0.26%, |z20|=2.19; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.91, z20 1.91, zc -0.25, resid-z 1.02 [quiet], 1d -0.24%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 222.65, z20 1.89, zc -0.23, resid-z -0.17 [quiet], 1d -0.58%, 1y-pct=97
- cac_40 [INDICES]: last 8709.25, z20 1.87, zc -0.09, resid-z 0.33 [quiet], 1d -0.07%, |z20|=1.87; 1y-pct=99
- dax [INDICES]: last 26328.85, z20 1.85, zc 0.04, resid-z 0.29 [quiet], 1d 0.04%, |z20|=1.85; 1y-pct=100
- sp500 [INDICES]: last 7749.70, z20 1.85, zc -0.11, resid-z -0.45 [quiet], 1d -0.10%, |z20|=1.85; 1y-pct=99
- dow_jones [INDICES]: last 53954.19, z20 1.62, zc -0.17, resid-z 0.15 [quiet], 1d -0.15%, |z20|=1.62; 1y-pct=98
- comex_copper [COMMODITIES]: last 6.61, z20 1.39, zc 0.27, resid-z 0.53 [quiet], 1d 0.60%, 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.46, z20 -1.39, zc n/a, resid-z n/a [quiet], 1d -0.11%, GSR<75 (extreme low)
- **Mechanism**: The recent move in COMEX gold and silver, along with other commodities and indices, is largely priced in, with small resid_z values indicating that the move is largely explained by factor exposures. The VALID gold_silver_comove channel suggests that monetary metals are co-moving, and the metal_copper_channel indicates that global copper is leading Indian metal equities.
- **Gap**: No gap: The move in COMEX gold and silver is largely priced in, with small resid_z values, and the Indian transmission candidates have already reacted to the move.
- **India take**: The Indian instruments such as nifty_metal, nifty_50, and nifty_midcap_100 have already reacted to the move in COMEX silver, CAC 40, and DAX, respectively. The nifty_fmcg is still quiet and has not reacted yet.
- Watch next: nifty_metal (up) — already moved; Reacted to comex_silver move
- Watch next: nifty_50 (up) — already moved; Reacted to cac_40 move
- Watch next: nifty_midcap_100 (up) — already moved; Reacted to dax move
- **India receivers**: nifty_50 (rho 0.537, z 1.22); nifty_fmcg (rho -0.534, z 0.49); nifty_midcap_100 (rho 0.515, z 1.92); nifty_metal (rho 0.483, z 2.06)
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: S&P 500, Nasdaq futures edge higher as traders monitor Hormuz developments — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-deal-crude-oil-fed-warsh-rate-hike-intel-spacex-amd-chip-stock-price-news-10th-august-2026/liveblog/133105183.cms
- Source: Sky Gold shares jump over 8% after Q1 profit — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/sky-gold-shares-jump-to-fresh-52-week-high-after-q1-profit/article71327003.ece
- Source: Q1 Results Today Live: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco Industries Q1 PAT up, Hindustan Copper PAT down q-o-q, AstraZeneca, Info Edge & Astra Microwave profit dip, Vi, Bosch, Lloyds Metals, Gland Pharma, Zee Entertainment, KEC International to announce Q1 results — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [AMBER 6.33] commodities · 2 series ↓
- wti [COMMODITIES]: last 79.66, z20 -0.50, zc 0.60, resid-z 0.58 [quiet], 1d 1.89%, 1-session move +1.89% ≥ 1.5%
- brent [COMMODITIES]: last 85.25, z20 -0.40, zc 0.61, resid-z 0.61 [quiet], 1d 2.03%, 1-session move +2.03% ≥ 1.5%
- **Mechanism**: The recent rise in crude oil prices, led by WTI and Brent, has been largely priced in by the market, with both commodities showing small resid_z values. However, the correlated instrument dyn_bond has not moved, suggesting a potential transmission channel. The historical analogues for WTI and Brent show a mixed outcome, but the aftermath of similar events has often led to a decline in oil prices.
- **Gap**: No gap: The move in WTI and Brent is largely priced, with small resid_z values and a clear motivation from rising crude oil prices and West Asia uncertainty.
- **India take**: The Indian instrument nifty_midcap_100 has already reacted to the move in WTI, while dyn_bharatcoal_ns has also reacted. However, midcap_largecap_ratio and dyn_hdbfs_bo remain quiet.
- Watch next: dyn_bond (down) — not yet - watch; Correlated instrument with WTI
- **India receivers**: nifty_midcap_100 (rho -0.462, z 1.92); midcap_largecap_ratio (rho -0.402, z 0.53); dyn_bharatcoal_ns (rho -0.392, z -1.01); dyn_hdbfs_bo (rho -0.38, z -0.91)
- Source: Benchmarks flatline for third day as crude keeps bulls at bay — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/benchmarks-flatline-for-third-day-as-crude-keeps-bulls-at-bay/article71328131.ece
- Source: Kazakhstan Weighs New Routes as Drone Strikes Squeeze Black Sea Oil Exports — OilPrice, 2026-08-10. https://oilprice.com/Latest-Energy-News/World-News/Kazakhstan-Weighs-New-Routes-as-Drone-Strikes-Squeeze-Black-Sea-Oil-Exports.html
- Source: Indian bonds steady as soft US data offsets oil rise — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/bonds/indian-bonds-steady-as-soft-us-data-offsets-oil-rise/articleshow/133099683.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.56] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 881.40, z20 3.56, zc 0.29, resid-z 0.15 [quiet], 1d 0.99%, |z20|=3.56; 1y-pct=100
- **Mechanism**: The recent surge in Tata Technologies' stock price can be attributed to the company's strong Q1FY27 results and positive outlook from analysts, which has also been reflected in the Indian market through transmission candidates such as Tata Elxsi and Nifty IT. The VALID metal_copper_channel and gold_silver_comove channels suggest a broader risk-on sentiment, which is further supported by the RISK_ON regime. However, the INVERTED safe_haven_gold channel indicates a potential risk-off sentiment, which may limit the upside.
- **Gap**: No gap: the big raw move in dyn_tatatech_ns with small resid_z=0.13 suggests that the move is largely priced in, leaving no significant event-to-price gap.
- **India take**: The Indian market has already reacted to the surge in Tata Technologies' stock price through transmission candidates such as Tata Elxsi and Nifty IT, which have also moved up. The broader risk-on sentiment in the Indian market is further supported by the VALID metal_copper_channel and gold_silver_comove channels.
- Watch next: dyn_tataelxsi_ns (up) — already moved; reacted to dyn_tatatech_ns
- Watch next: nifty_it (up) — already moved; reacted to dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.471, z 1.54); nifty_it (rho 0.465, z 1.43)
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Source: How Rakesh Jhunjhunwala's old Tata bet created Rs 80,000 crore wealth after two years of flat returns — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/how-rakesh-jhunjhunwalas-old-tata-bet-created-rs-80000-crore-wealth-after-two-years-of-flat-returns/articleshow/133079774.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.45] dyn_heromotoco_ns ↑
- dyn_heromotoco_ns [EQUITIES]: last 5860.00, z20 2.45, zc 1.25, resid-z 1.46 [quiet], 1d 2.36%, |z20|=2.45
- **Mechanism**: The recent surge in Hero MotoCorp's stock price can be attributed to its Q1 earnings beating street estimates, driven by strong sales of premium bikes and EVs. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The global copper market often leads Indian metal equities, and a rise in Hero MotoCorp's stock could be a precursor to a broader move in the metal sector.
- **Gap**: No gap: the move in Hero MotoCorp's stock is largely priced in, given the strong earnings report and the current market regime of RISK_ON
- **India take**: The Indian instrument that expresses this move is dyn_havells_ns, which has already reacted with a rho of 0.447 via dyn_heromotoco_ns. The Nifty Midcap 100 index has also reacted, with a rho of 0.387 via dyn_heromotoco_ns.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to dyn_heromotoco_ns
- **India receivers**: dyn_havells_ns (rho 0.456, z 1.3); nifty_midcap_100 (rho 0.381, z 1.92)
- Source: Hero MotoCorp gains speed as premium bikes, EVs fuel Q1 — Mint Markets, 2026-08-10. https://www.livemint.com/market/mark-to-market/hero-motocorp-q1fy27-earnings-stock-margin-ev-growth-11786338356204.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [AMBER 4.28] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 264.45, z20 2.28, zc 0.22, resid-z 0.05 [quiet], 1d 0.89%, |z20|=2.28; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- **India receivers**: nifty_midcap_100 (rho 0.357, z 1.92)
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [RED 4.01] fx · 3 series ↑
- usd_mxn [FX]: last 17.15, z20 -2.69, zc -0.79, resid-z -0.68 [quiet], 1d -0.33%, |z20|=2.69; 1y-pct=1
- aud_usd [FX]: last 0.71, z20 1.82, zc 0.67, resid-z 0.74 [quiet], 1d 0.34%, |z20|=1.82
- eur_usd [FX]: last 1.16, z20 1.72, zc 0.66, resid-z 0.88 [quiet], 1d 0.24%, |z20|=1.72
- **Mechanism**: The recent move in FX markets, particularly in usd_mxn, aud_usd, and eur_usd, is largely priced in, with resid_z values indicating that the moves are mostly explained by factor exposures. However, the correlated instruments that have not moved, such as usd_brl and taiwan_weighted, may be due for a move. The historical analogues suggest a potential for a decline in these currencies over the next 20 days.
- **Gap**: No gap: the recent FX moves are largely priced in, with small resid_z values indicating that the moves are mostly explained by factor exposures.
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_mxn, with a rho of -0.572. However, other Indian instruments that are correlated with the FX markets, such as metal equities, may be due for a move via the metal_copper_channel.
- Watch next: usd_brl (down) — not yet - watch; historically leads usd_mxn by 3d
- **India receivers**: dyn_muthootfin_ns (rho -0.572, z -1.25)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 3.61] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.29, z20 1.61, zc -0.00, resid-z -0.46 [quiet], 1d -0.01%, 1y-pct=99
- **Mechanism**: The recent move in dyn_tech is priced, with a small resid_z of -0.46, indicating that the move is largely explained by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that equity markets are currently driven by risk appetite. The gathering of experts in chips, defence, and deep-sea drilling in Beijing's summer retreat may indicate China's tech priorities, but its impact on dyn_tech is already reflected in the price.
- **Gap**: No gap: the small resid_z of -0.46 indicates that the move in dyn_tech is largely explained by factor exposures
- **India take**: The Indian instrument dyn_inoxindia_ns, which has a rho of -0.403 with dyn_tech, may react negatively to the move in dyn_tech, but has not yet done so. The metal_copper_channel, which is VALID, may also influence Indian metal equities.
- Watch next: dyn_inoxindia_ns (down) — not yet - watch; rho=-0.403 via dyn_tech
- **India receivers**: dyn_inoxindia_ns (rho -0.403, z 0.46)
- Source: How the guest list for Beijing’s summer retreat reveals its tech priorities — SCMP Economy, 2026-08-10. https://www.scmp.com/news/china/politics/article/3363523/how-guest-list-beijings-summer-retreat-reveals-its-tech-priorities?utm_source=rss_feed
- Source: Global Market: Shanghai, Hong Kong stocks rise as consumer gains offset tech weakness — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-shanghai-hong-kong-stocks-rise-as-consumer-gains-offset-tech-weakness/articleshow/133090625.cms
- Source: Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results, Sky Gold, Dynamatic Tech, Quality Power, Anant Raj shares gain after Q1, Kaynes Tech, Ola, Oswal Pumps, Jamna Auto, Apollo Micro shares in red — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.33] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.22, z20 1.40, zc 1.21, resid-z 1.02 [quiet], 1d 0.97%, 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.03, zc 1.32, resid-z 0.90 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.43, z20 1.00, zc 0.51, resid-z -0.28 [quiet], 1d 0.83%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.59, z20 -0.88, zc -0.69, resid-z 0.28 [quiet], 1d -0.21%, 1y-pct=2
- ust_2y [RATES]: last 4.25, z20 0.25, zc 1.33, resid-z 0.95 [quiet], 1d 1.67%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_lth (co-move) — not yet - watch; rho 0.551 vs dyn_bond, historically leads by 2d
- Watch next: brent (co-move) — not yet - watch; rho 0.533 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.506 vs ust_10y, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

## Watchlist (below surfacing floor)
dyn_coin ↓ (3.01), dyn_hdb ↓ (2.72), dyn_pltr ↑ (2.66), dyn_lth ↓ (2.5), dyn_indianb_ns ↑ (2.44), dyn_icicigi_bo ↓ (2.28), dyn_idbi_ns ↓ (2.18), dyn_indusindbk_bo ↑ (2.16), usd_cny ↓ (2.14), nifty_metal ↑ (2.06), shanghai_comp ↑ (1.99), nifty_midcap_100 ↑ (1.92)

## India macro
- nifty_50: 24583.8008 (1d 0.05%, z20 1.22, flag none)
- nifty_midcap_100: 63848.3516 (1d 0.61%, z20 1.92, flag amber)
- usd_inr: 95.2900 (1d -0.02%, z20 -1.18, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5972 (1d 0.55%, z20 0.53, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.4 — "Indian bonds steady as soft US data offsets oil rise"
- COALINDIA.NS (COAL INDIA LTD) score 79.6 — "Indian bonds steady as soft US data offsets oil rise"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.3 — "Indian bonds steady as soft US data offsets oil rise"
- INDIANB.NS (INDIAN BANK) score 60.9 — "Indian bonds steady as soft US data offsets oil rise"
- BAC (Bank of America Corporation) score 48.0 — "Are target date funds aggressive enough to give Americans retirement savings that last the"
- COIN (Coinbase Global, Inc.) score 45.1 — "Global Market |Bank of Japan signals vigilance on Yen weakness, keeps door open for rate h"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.9 — "How the guest list for Beijing’s summer retreat reveals its tech priorities"
- HDB (HDFC Bank Limited) score 44.5 — "Heat Waves Could Cost the EU 1% of GDP, Dutch Bank Says"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.6 — "How the guest list for Beijing’s summer retreat reveals its tech priorities"
- TECH (Bio-Techne Corp) score 42.0 — "How the guest list for Beijing’s summer retreat reveals its tech priorities"
- IDBI.NS (IDBI BANK LIMITED) score 41.8 — "Heat Waves Could Cost the EU 1% of GDP, Dutch Bank Says"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.8 — "Heat Waves Could Cost the EU 1% of GDP, Dutch Bank Says"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.3 — "Heat Waves Could Cost the EU 1% of GDP, Dutch Bank Says"
- OHI (Omega Healthcare Investors, In) score 37.7 — "SPCX - SPACEX RETAIL INVESTORS TURN NET SELLERS Retail investors sold a net $4.5 million o"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.1 — "Top Gainers & Losers on 10 August: Hitachi Energy, Paytm, Titian, BSE, BEML, Lenskart amon"
- LTH (Life Time Group Holdings, Inc.) score 28.3 — "TRUMP’S MONDAY CALENDAR — AUGUST 10 🔸 8:00 AM — Executive Time 🔸 9:30 AM — Pre-Tape Interv"
- CHKP (Check Point Software Technolog) score 28.3 — "AAPL : downgraded to Underperform by Jefferies; PT cut to $263.66 from $285.56 Jefferies d"
- 301077.SZ (CHINASTARS) score 24.4 — "U.S. Bets $400 Million on Australian Scandium Miner to Break China's Grip"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.0 — "Indian bonds steady as soft US data offsets oil rise"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.7 — "Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.3 — "Bharat Forge shares plunge 9% after firm posts Rs 90 crore Q1 net loss on exceptional item"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.0 — "Market wrap: Titan Company, Bajaj Finance, SBI among top gainers and losers on Nifty and S"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.7 — "‘I want her to choose the best strategy’: My wife’s Social Security is just $900. Should s"
- JIOFIN.BO (Jio Financial Services Limited) score 9.2 — "SBI shares slip post Q1 beat; what Jefferies, JM Financial say"
- MS (Morgan Stanley) score 8.9 — "J.P. Morgan raises S&P 500 year-end target to 8,000 on AI and earnings optimism"
- META (Meta) score 8.7 — "META - META TO RESUME OPEN-SOURCE AI MODEL RELEASES Meta CEO Mark Zuckerberg says the comp"
- VT (Vanguard Total World Stock Ind) score 8.0 — "Elon Musk vs Michael Burry: World's richest man says AI internet traffic will outpace huma"
- AAPL (Apple Inc.) score 7.9 — "AAPL : downgraded to Underperform by Jefferies; PT cut to $263.66 from $285.56 Jefferies d"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.8 — "SBI shares slip post Q1 beat; what Jefferies, JM Financial say"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.8 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.6 — "How Adani’s $125 billion capex boom is creating new winners on Dalal Street"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 4.8 — "Bharat Forge shares plunge 9% after firm posts Rs 90 crore Q1 net loss on exceptional item"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.6 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 4.4 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- PLTR (Palantir Technologies Inc.) score 3.9 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- NVDA (NVIDIA Corporation) score 3.6 — "Two reasons why Nvidia’s stock saw its biggest weekly surge in more than a year"
- AMZN (Amazon.com, Inc.) score 2.8 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 2.8 — "Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results?"
- CUPID.NS (CUPID LIMITED) score 2.5 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.9 — "Hero MotoCorp gains speed as premium bikes, EVs fuel Q1"

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