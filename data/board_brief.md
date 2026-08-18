# Transmission Layer — board brief · 2026-08-18 07:02Z

data as of **2026-08-18** · 98 series · 5 red / 37 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.206, 2d in regime; vol-pct 0.287, breadth-off 0.125, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.36, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.14, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.02, corr60 0.22, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.432460096293056e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2338) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 8.44] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4453.70, z20 1.75, zc 0.66, resid-z -0.31 [quiet], 1d 0.81%, |z20|=1.75
- russell_2000 [INDICES]: last 3057.58, z20 1.50, zc -0.30, resid-z 0.45 [quiet], 1d -0.35%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 225.05, z20 1.37, zc -0.02, resid-z 0.09 [quiet], 1d -0.05%, 1y-pct=98
- dyn_vt [EQUITIES]: last 161.83, z20 1.26, zc -0.34, resid-z 0.26 [quiet], 1d -0.26%, 1y-pct=99
- stoxx_50 [INDICES]: last 6538.73, z20 1.16, zc -0.02, resid-z 0.43 [quiet], 1d -0.01%, 1y-pct=98
- dax [INDICES]: last 26370.39, z20 1.12, zc -0.36, resid-z -0.05 [quiet], 1d -0.26%, 1y-pct=99
- sp500 [INDICES]: last 7746.14, z20 1.02, zc -0.66, resid-z -0.50 [quiet], 1d -0.51%, 1y-pct=98
- comex_copper [COMMODITIES]: last 6.58, z20 0.58, zc -0.16, resid-z 0.33 [quiet], 1d -0.36%, 1y-pct=95
- gold_silver_ratio [DERIVED]: last 68.10, z20 -0.57, zc n/a, resid-z n/a [quiet], 1d 1.92%, GSR<75 (extreme low)
- dow_jones [INDICES]: last 53466.68, z20 0.51, zc -0.70, resid-z -0.12 [quiet], 1d -0.49%, 1y-pct=96
- cac_40 [INDICES]: last 8585.62, z20 0.30, zc -0.82, resid-z -0.44 [quiet], 1d -0.59%, 1y-pct=95
- **Mechanism**: cross-asset · 11 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.97).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.493 via dax, z 0.72, quiet); nifty_50 (rho 0.485 via cac_40, z -0.4, quiet); nifty_metal (rho 0.459 via comex_gold, z 0.75, quiet); dyn_stylebaaza_ns (rho -0.378 via gold_silver_ratio, z 2.65, reacted)
- Watch next: brent (inverse) — not yet - watch; rho -0.658 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.634 vs dow_jones, historically leads by 2d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.604 vs russell_2000, historically leads by 1d
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.577 vs russell_2000, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.741 vs russell_2000
- **India receivers**: nifty_midcap_100 (rho 0.493, z 0.72); nifty_50 (rho 0.485, z -0.4); nifty_metal (rho 0.459, z 0.75); dyn_stylebaaza_ns (rho -0.378, z 2.65)
- Source: Gold Rate Today, Aug 18: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-18-2026/article71359087.ece
- Source: Hindustan Copper, Vedanta, other metal stocks slip up to 2% after sharp gains. Should you buy the dip or avoid? — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-copper-vedanta-other-metal-stocks-slip-up-to-2-after-sharp-gains-should-you-buy-the-dip-or-avoid/articleshow/133313559.cms
- Source: Gold slips below Rs 1.55 lakh/10 gm on MCX, but global prices extend gains. What’s next? — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/commodities/news/gold-slips-below-rs-1-55-lakh/10-gm-on-mcx-but-global-prices-extend-gains-whats-next/articleshow/133311524.cms
- Historical analogues: 2024-11-26 (d=0.97), 2025-10-31 (d=1.09), 2024-10-04 (d=1.16)

### [RED 5.58] commodities · 3 series ↑
- corn [COMMODITIES]: last 491.25, z20 4.26, zc 4.41, resid-z 0.84 [moved], 1d 5.65%, |z20|=4.26; 1y-pct=100
- wheat [COMMODITIES]: last 689.25, z20 1.50, zc 1.18, resid-z -0.15 [quiet], 1d 2.15%, 1y-pct=99
- soybeans [COMMODITIES]: last 1225.00, z20 1.32, zc 1.97, resid-z 2.09 [unexplained], 1d 2.00%, 1y-pct=98
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.427 via wheat, z 3.08, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.427, z 3.08)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.08] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 626.30, z20 3.08, zc 2.17, resid-z -0.53 [moved], 1d 3.08%, |z20|=3.08; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.92] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.92, zc n/a, resid-z n/a [quiet], 1d 0.07%, 52-wk extreme (pct=100); |z20|=1.92; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.505 via midcap_largecap_ratio, z 0.72, quiet); dyn_bharatcoal_ns (rho 0.376 via midcap_largecap_ratio, z -1.19, reacted); dyn_fincables_ns (rho 0.359 via midcap_largecap_ratio, z 2.12, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.505 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.505, z 0.72); dyn_bharatcoal_ns (rho 0.376, z -1.19); dyn_fincables_ns (rho 0.359, z 2.12)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.65] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 402.65, z20 2.65, zc 1.34, resid-z 1.75 [unexplained], 1d 4.99%, |z20|=2.65; 1y-pct=96
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.4 via dyn_stylebaaza_ns, z 0.26, quiet); dyn_adanient_bo (rho 0.384 via dyn_stylebaaza_ns, z -0.19, quiet); dyn_bharatcoal_ns (rho 0.356 via dyn_stylebaaza_ns, z -1.19, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.4, z 0.26); dyn_adanient_bo (rho 0.384, z -0.19); dyn_bharatcoal_ns (rho 0.356, z -1.19)
- Source: US Stock Market: Citadel Securities warns SEC rule change could hurt retail investors, market liquidity — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-citadel-securities-warns-sec-rule-change-could-hurt-retail-investors-market-liquidity/articleshow/133311215.cms
- Source: US stocks: US market slips as oil prices rise, retail results awaited — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-slips-as-oil-prices-rise-retail-results-awaited/articleshow/133306298.cms
- Source: Wall Street indexes slip with Iran, retail results in focus — Mint Markets, 2026-08-17. https://www.livemint.com/market/wall-street-indexes-slip-with-iran-retail-results-in-focus-11786993198786.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.58] cross-asset · 3 series ↑
- ust_30y [RATES]: last 5.25, z20 1.26, zc 0.98, resid-z 0.73 [quiet], 1d 0.77%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.43, z20 -1.26, zc -0.71, resid-z -0.48 [quiet], 1d -0.22%, 1y-pct=1
- ust_10y [RATES]: last 4.68, z20 0.39, zc 1.08, resid-z 1.15 [quiet], 1d 1.08%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.688 vs ust_30y, historically leads by 1d
- Watch next: brent (co-move) — not yet - watch; rho 0.557 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.529 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.532 vs ust_30y
- Source: Indian lenders’ dollar bond sales hit record near $9 billion — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/indian-lenders-dollar-bond-sales-hit-record-near-9-billion/article71358856.ece
- Source: Global Market: Japan’s 10-year JGB yield hits three-decade high on BOJ rate hike bets — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-jgb-yield-hits-three-decade-high-on-boj-rate-hike-bets/articleshow/133311165.cms
- Source: Global Market: Japan stocks slide as oil spike and rising bond yields weigh on sentiment — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-slide-as-oil-spike-and-rising-bond-yields-weigh-on-sentiment/articleshow/133310581.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.12), 2025-04-23 (d=0.18)

### [AMBER 4.15] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1255.40, z20 -2.15, zc -0.46, resid-z -1.93 [unexplained], 1d -0.92%, |z20|=2.15; 1y-pct=5
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.577 via dyn_voltas_ns, z -1.19, reacted); nifty_midcap_100 (rho 0.516 via dyn_voltas_ns, z 0.72, quiet); nifty_50 (rho 0.39 via dyn_voltas_ns, z -0.4, quiet); dyn_havells_ns (rho 0.374 via dyn_voltas_ns, z 1.19, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.516 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.577, z -1.19); nifty_midcap_100 (rho 0.516, z 0.72); nifty_50 (rho 0.39, z -0.4); dyn_havells_ns (rho 0.374, z 1.19)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Source: Voltas shares fall 4% as brokerages differ after Q1 results — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/voltas-shares-fall-over-6-from-intraday-high-as-brokerages-differ-after-q1-results/article71355298.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [AMBER 3.73] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.39, z20 1.73, zc -0.01, resid-z 0.08 [quiet], 1d -0.01%, 1y-pct=99
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.417 via dyn_tech, z 0.11, quiet)
- **India receivers**: dyn_inoxindia_ns (rho -0.417, z 0.11)
- Source: Sensex today | Stock Market Live: Sensex down 400 pts, Nifty drops below 24,200; Infosys, HCL Tech top losers — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-market-live-sensex-nifty50-today-live-updates-today-18th-august-2026/article71358725.ece
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

## Watchlist (below surfacing floor)
dyn_lth ↑ (3.24), dyn_hdb ↓ (3.19), dyn_bac ↑ (3.09), fx · 2 series ↑ (2.97), dyn_icicigi_bo ↓ (2.77), dyn_tatatech_ns ↑ (2.74), nifty_fmcg ↓ (2.7), dyn_fincables_ns ↑ (2.12), dyn_idbi_ns ↓ (2.01), shanghai_comp ↑ (1.96), bovespa ↓ (1.85), ust_2s10s ↑ (1.77)

## India macro
- nifty_50: 24215.9004 (1d -0.30%, z20 -0.40, flag none)
- nifty_midcap_100: 63667.5508 (1d -0.23%, z20 0.72, flag amber)
- usd_inr: 95.6700 (1d 0.23%, z20 -0.06, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6292 (1d 0.07%, z20 1.92, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.3 — "NSE said to seek up to $55 billion valuation in record India IPO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.8 — "NSE said to seek up to $55 billion valuation in record India IPO"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.7 — "NSE said to seek up to $55 billion valuation in record India IPO"
- INDIANB.NS (INDIAN BANK) score 62.0 — "Axis Bank Share Price Live Updates: Axis Bank  Yearly Performance Overview"
- BAC (Bank of America Corporation) score 45.3 — "Axis Bank Share Price Live Updates: Axis Bank  Yearly Performance Overview"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.6 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Market Activity"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.3 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Market Activity"
- TECH (Bio-Techne Corp) score 43.1 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Market Activity"
- COIN (Coinbase Global, Inc.) score 42.4 — "Gold slips below Rs 1.55 lakh/10 gm on MCX, but global prices extend gains. What’s next?"
- HDB (HDFC Bank Limited) score 39.0 — "Axis Bank Share Price Live Updates: Axis Bank  Yearly Performance Overview"
- OHI (Omega Healthcare Investors, In) score 38.8 — "Sebi cautions investors against social media live trading tips and unregistered advisory s"
- IDBI.NS (IDBI BANK LIMITED) score 36.1 — "Axis Bank Share Price Live Updates: Axis Bank  Yearly Performance Overview"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.1 — "Axis Bank Share Price Live Updates: Axis Bank  Yearly Performance Overview"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.0 — "Axis Bank Share Price Live Updates: Axis Bank  Yearly Performance Overview"
- CHKP (Check Point Software Technolog) score 35.8 — "Shankesh Jewellers IPO opens for subscription. Should you apply? Check GMP, key details"
- LTH (Life Time Group Holdings, Inc.) score 28.3 — "Lupin shares in focus after USFDA nod for drug to treat excessive daytime sleepiness"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.9 — "Indian bonds wobble on oil strain, RBI swap pullback"
- 301077.SZ (CHINASTARS) score 22.8 — "China’s Xi praises former president Jiang Zemin’s contribution in show of party unity"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.0 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Market Performance Overview"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.7 — "Global Market: Chinese, Hong Kong stocks slip as AI shares retreat; energy stocks gain"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.4 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Market Performance Overview"
- JIOFIN.BO (Jio Financial Services Limited) score 15.5 — "Sebi cautions investors against social media live trading tips and unregistered advisory s"
- PCJEWELLER.NS (PC JEWELLER LTD) score 14.3 — "Lalithaa Jewellery Mart IPO Day 2 LIVE: GMP, subscription status to review. Apply or not?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.8 — "Coal India Share Price Live Updates: Coal India  Current Trading Status"
- MS (Morgan Stanley) score 10.7 — "Here’s how Amazon’s stock could nearly double by the end of next year, according to Morgan"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.4 — "Jio Financial Services Share Price Live Updates: Jio Financial Services dips below its 20-"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.2 — "The number of ‘negative-beta’ stocks in the S&P 500 just hit a new record high. What that "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.5 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- NVDA (NVIDIA Corporation) score 7.4 — "SpaceX’s stock is rising, and that’s a good sign for Nvidia and Google"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.2 — "US Stock Market: Citadel Securities warns SEC rule change could hurt retail investors, mar"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "Adani flagship eyes India’s Nifty crown after years of turmoil"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 5.4 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- VT (Vanguard Total World Stock Ind) score 5.1 — "RUSSIA'S LAVROV SAYS RUSSIA AND DPRK ARE FIGHTING TO ESTABLISH NEW AND RIGHTEOUS WORLD ORD"
- META (Meta) score 5.0 — "Hindustan Copper, Vedanta, other metal stocks slip up to 2% after sharp gains. Should you "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.7 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Movement"
- VOLTAS.NS (VOLTAS LTD) score 4.4 — "Voltas reported strong growth in June quarter, but failed to impress"
- AAPL (Apple Inc.) score 4.1 — "Apple’s stock could rise 30% if it strikes an Nvidia deal for AI, this analyst says"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.9 — "Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Man"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.8 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.7 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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