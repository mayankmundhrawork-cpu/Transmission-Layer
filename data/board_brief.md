# Transmission Layer — board brief · 2026-08-18 04:49Z

data as of **2026-08-18** · 98 series · 5 red / 35 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.199, 2d in regime; vol-pct 0.274, breadth-off 0.125, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.36, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.02, corr60 0.22, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.432460096293056e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2424) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 5.99] cross-asset · 8 series ↑
- russell_2000 [INDICES]: last 3057.58, z20 1.50, zc -0.30, resid-z 0.45 [quiet], 1d -0.35%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 225.05, z20 1.37, zc -0.02, resid-z 0.09 [quiet], 1d -0.05%, 1y-pct=98
- dyn_vt [EQUITIES]: last 161.83, z20 1.26, zc -0.34, resid-z 0.26 [quiet], 1d -0.26%, 1y-pct=99
- stoxx_50 [INDICES]: last 6538.73, z20 1.16, zc -0.02, resid-z 0.43 [quiet], 1d -0.01%, 1y-pct=98
- dax [INDICES]: last 26370.39, z20 1.12, zc -0.36, resid-z -0.05 [quiet], 1d -0.26%, 1y-pct=99
- sp500 [INDICES]: last 7746.14, z20 1.02, zc -0.66, resid-z -0.50 [quiet], 1d -0.51%, 1y-pct=98
- dow_jones [INDICES]: last 53466.68, z20 0.51, zc -0.70, resid-z -0.12 [quiet], 1d -0.49%, 1y-pct=96
- cac_40 [INDICES]: last 8585.62, z20 0.30, zc -0.82, resid-z -0.44 [quiet], 1d -0.59%, 1y-pct=95
- **Mechanism**: cross-asset · 8 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-22 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.492 via dax, z 0.54, quiet); nifty_50 (rho 0.485 via cac_40, z -0.41, quiet)
- Watch next: brent (inverse) — not yet - watch; rho -0.658 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.634 vs dow_jones, historically leads by 2d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.604 vs russell_2000, historically leads by 1d
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.577 vs russell_2000, historically leads by 5d
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.545 vs stoxx_50, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.492, z 0.54); nifty_50 (rho 0.485, z -0.41)
- Source: The number of ‘negative-beta’ stocks in the S&P 500 just hit a new record high. What that means for investors. — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/the-number-of-negative-beta-stocks-in-the-s-p-500-just-hit-a-new-record-high-what-that-means-for-investors-992ca307?mod=mw_rss_topstories
- Source: RUSSIA'S LAVROV SAYS RUSSIA AND DPRK ARE FIGHTING TO ESTABLISH NEW AND RIGHTEOUS WORLD ORDER - KCNA — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34821
- Source: SpaceX’s stock is rising, and that’s a good sign for Nvidia and Google — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/spacexs-stock-is-rising-and-thats-a-good-sign-for-nvidia-and-google-913ce9de?mod=mw_rss_topstories
- Historical analogues: 2024-11-22 (d=0.59), 2024-11-11 (d=0.88), 2024-10-15 (d=0.9)

### [RED 5.55] commodities · 3 series ↑
- corn [COMMODITIES]: last 491.00, z20 4.23, zc 4.37, resid-z 0.84 [moved], 1d 5.59%, |z20|=4.23; 1y-pct=100
- wheat [COMMODITIES]: last 688.25, z20 1.45, zc 1.10, resid-z -0.15 [quiet], 1d 2.00%, 1y-pct=99
- soybeans [COMMODITIES]: last 1224.50, z20 1.31, zc 1.93, resid-z 2.09 [unexplained], 1d 1.96%, 1y-pct=98
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.422 via wheat, z 2.71, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.422, z 2.71)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 4.71] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 619.95, z20 2.71, zc 1.43, resid-z -0.53 [quiet], 1d 2.03%, |z20|=2.71; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.65] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 402.65, z20 2.65, zc 1.34, resid-z 1.75 [unexplained], 1d 4.99%, |z20|=2.65; 1y-pct=96
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.403 via dyn_stylebaaza_ns, z 0.36, quiet); dyn_adanient_bo (rho 0.384 via dyn_stylebaaza_ns, z -0.17, quiet); dyn_bharatcoal_ns (rho 0.359 via dyn_stylebaaza_ns, z -1.08, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.403, z 0.36); dyn_adanient_bo (rho 0.384, z -0.17); dyn_bharatcoal_ns (rho 0.359, z -1.08)
- Source: US Stock Market: Citadel Securities warns SEC rule change could hurt retail investors, market liquidity — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-citadel-securities-warns-sec-rule-change-could-hurt-retail-investors-market-liquidity/articleshow/133311215.cms
- Source: US stocks: US market slips as oil prices rise, retail results awaited — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-slips-as-oil-prices-rise-retail-results-awaited/articleshow/133306298.cms
- Source: Wall Street indexes slip with Iran, retail results in focus — Mint Markets, 2026-08-17. https://www.livemint.com/market/wall-street-indexes-slip-with-iran-retail-results-in-focus-11786993198786.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [RED 4.62] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.62, zc n/a, resid-z n/a [quiet], 1d -0.13%, 52-wk extreme (pct=99); |z20|=1.62; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.508 via midcap_largecap_ratio, z 0.54, quiet); dyn_bharatcoal_ns (rho 0.374 via midcap_largecap_ratio, z -1.08, reacted); dyn_fincables_ns (rho 0.362 via midcap_largecap_ratio, z 2.08, reacted); dyn_pcjeweller_ns (rho 0.352 via midcap_largecap_ratio, z 0.36, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.508 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.508, z 0.54); dyn_bharatcoal_ns (rho 0.374, z -1.08); dyn_fincables_ns (rho 0.362, z 2.08); dyn_pcjeweller_ns (rho 0.352, z 0.36)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

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

### [AMBER 4.09] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1256.80, z20 -2.09, zc -0.41, resid-z -1.93 [unexplained], 1d -0.81%, |z20|=2.09; 1y-pct=5
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.577 via dyn_voltas_ns, z -1.08, reacted); nifty_midcap_100 (rho 0.517 via dyn_voltas_ns, z 0.54, quiet); nifty_50 (rho 0.39 via dyn_voltas_ns, z -0.41, quiet); dyn_havells_ns (rho 0.373 via dyn_voltas_ns, z 1.27, reacted); dyn_cupid_ns (rho 0.364 via dyn_voltas_ns, z 0.53, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.517 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.577, z -1.08); nifty_midcap_100 (rho 0.517, z 0.54); nifty_50 (rho 0.39, z -0.41); dyn_havells_ns (rho 0.373, z 1.27)
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Source: Voltas shares fall 4% as brokerages differ after Q1 results — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/voltas-shares-fall-over-6-from-intraday-high-as-brokerages-differ-after-q1-results/article71355298.ece
- Source: Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Voltas among top losers — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-17-august-nmdc-steel-lg-electronics-bse-tata-tech-infosys-voltas-among-top-losers-11786961037869.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [AMBER 3.73] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.39, z20 1.73, zc -0.01, resid-z 0.08 [quiet], 1d -0.01%, 1y-pct=99
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.417 via dyn_tech, z -0.06, quiet)
- **India receivers**: dyn_inoxindia_ns (rho -0.417, z -0.06)
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Source: Stanley Druckenmiller ditched these chip plays before the selloff. Here’s how he’s playing the tech sector now. — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/stanley-druckenmiller-ditched-these-chip-plays-before-the-selloff-heres-how-hes-playing-the-tech-sector-now-9115c06f?mod=mw_rss_topstories
- Source: ECB WARNS AI BOOM COULD END IN CORRECTION ECB economists warn stock-market valuations may be heading for a correction as enthusiasm around AI pushes tech valuations toward dot-com bubble levels. Unlike the early 2000s, policymakers have less room to cut rates or deploy fiscal — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34797
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

## Watchlist (below surfacing floor)
comex_gold ↑ (3.7), gold_silver_ratio ↓ (3.5), dyn_lth ↑ (3.24), dyn_bac ↑ (3.09), dyn_icicigi_bo ↓ (3.04), fx · 2 series ↑ (2.92), dyn_tatatech_ns ↑ (2.83), nifty_fmcg ↓ (2.72), dyn_fincables_ns ↑ (2.08), bovespa ↓ (1.85), usd_brl ↑ (1.85), ust_2s10s ↑ (1.77)

## India macro
- nifty_50: 24213.8008 (1d -0.30%, z20 -0.41, flag none)
- nifty_midcap_100: 63534.5508 (1d -0.44%, z20 0.54, flag amber)
- usd_inr: 95.6520 (1d 0.21%, z20 -0.09, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6239 (1d -0.13%, z20 1.62, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.1 — "Stock recommendations for 18 August from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.6 — "Stock recommendations for 18 August from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.5 — "Stock recommendations for 18 August from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 59.2 — "Axis Bank expands corporate play beyond loans, shuns price war"
- BAC (Bank of America Corporation) score 43.3 — "Axis Bank expands corporate play beyond loans, shuns price war"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.5 — "Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Hea"
- COIN (Coinbase Global, Inc.) score 41.2 — "Global Market Today: Asian shares advance; oil rises on Middle East concerns"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.2 — "Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Hea"
- TECH (Bio-Techne Corp) score 40.9 — "Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Hea"
- OHI (Omega Healthcare Investors, In) score 39.6 — "Sebi cautions investors against social media live trading tips and unregistered advisory s"
- CHKP (Check Point Software Technolog) score 36.5 — "Shankesh Jewellers IPO opens for subscription. Should you apply? Check GMP, key details"
- HDB (HDFC Bank Limited) score 35.7 — "Axis Bank expands corporate play beyond loans, shuns price war"
- IDBI.NS (IDBI BANK LIMITED) score 33.8 — "Axis Bank expands corporate play beyond loans, shuns price war"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 33.8 — "Axis Bank expands corporate play beyond loans, shuns price war"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 33.7 — "Axis Bank expands corporate play beyond loans, shuns price war"
- LTH (Life Time Group Holdings, Inc.) score 28.9 — "Lupin shares in focus after USFDA nod for drug to treat excessive daytime sleepiness"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.5 — "Why this popular Treasury-bond ETF is trading at its lowest since 2004"
- 301077.SZ (CHINASTARS) score 23.3 — "China’s Xi praises former president Jiang Zemin’s contribution in show of party unity"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.5 — "Tata Steel Share Price Live Updates: Tata Steel's Current Price and Market Performance"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.1 — "TRUMP ON UK PM: HE HAS IMMIGRATION, ENERGY PROBLEMS"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.8 — "Tata Steel Share Price Live Updates: Tata Steel's Current Price and Market Performance"
- JIOFIN.BO (Jio Financial Services Limited) score 15.9 — "Sebi cautions investors against social media live trading tips and unregistered advisory s"
- PCJEWELLER.NS (PC JEWELLER LTD) score 13.6 — "AI catches up with jewellery sector, redefines designs"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.0 — "Coal India Share Price Live Updates: Coal India  Current Trading Status"
- MS (Morgan Stanley) score 10.9 — "Here’s how Amazon’s stock could nearly double by the end of next year, according to Morgan"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.6 — "Jio Financial Services Share Price Live Updates: Jio Financial Services dips below its 20-"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.4 — "The number of ‘negative-beta’ stocks in the S&P 500 just hit a new record high. What that "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.7 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- NVDA (NVIDIA Corporation) score 7.6 — "SpaceX’s stock is rising, and that’s a good sign for Nvidia and Google"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.3 — "US Stock Market: Citadel Securities warns SEC rule change could hurt retail investors, mar"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "Adani flagship eyes India’s Nifty crown after years of turmoil"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 5.6 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- VT (Vanguard Total World Stock Ind) score 5.2 — "RUSSIA'S LAVROV SAYS RUSSIA AND DPRK ARE FIGHTING TO ESTABLISH NEW AND RIGHTEOUS WORLD ORD"
- AAPL (Apple Inc.) score 4.2 — "Apple’s stock could rise 30% if it strikes an Nvidia deal for AI, this analyst says"
- META (Meta) score 4.1 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.7 — "ICICI Bank dollar debt fundraising tops $2 billion in a month: Bankers"
- VOLTAS.NS (VOLTAS LTD) score 3.5 — "Voltas among 4 F&O stocks with a sharp rise in futures open interest"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.0 — "Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Hea"
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