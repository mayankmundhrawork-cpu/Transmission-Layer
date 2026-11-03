# Transmission Layer — board brief · 2026-11-03 19:28Z

data as of **2026-11-03** · 97 series · 6 red / 38 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.804, 3d in regime; vol-pct 0.859, breadth-off 0.75, Markov P(high-vol) 0.091)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.45, contra nifty_50 corr20=0.24, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.16, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 0.07, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.74, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.32, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.13, corr60 -0.11, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.56, corr60 0.37, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 88** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.259, β 0.2639, p 0.02836); driver zc -1.94 → expected -0.271%. Type hit-rate 0.827 (n=1677).
- Track record · residual_reversion: hit-rate **0.505** (n=1108) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=1677) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.78] indices · 2 series ↑
- nifty_50 [INDICES]: last 23810.85, z20 3.95, zc 1.91, resid-z 2.20 [unexplained], 1d 1.58%, |z20|=3.95
- nifty_fmcg [INDICES]: last 45580.05, z20 1.95, zc 3.29, resid-z 3.07 [unexplained], 1d 3.65%, |z20|=1.95
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.701 via nifty_50, z 0.37, quiet); dyn_jiofin_bo (rho 0.637 via nifty_50, z 0.41, quiet); dyn_bajfinance_ns (rho 0.612 via nifty_50, z 0.99, quiet); dyn_indusindbk_bo (rho 0.551 via nifty_50, z -0.04, quiet); nifty_metal (rho 0.547 via nifty_50, z 0.61, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.701 vs nifty_50, historically leads by 3d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.637 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.701 vs nifty_50
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.612 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.551 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.701, z 0.37); dyn_jiofin_bo (rho 0.637, z 0.41); dyn_bajfinance_ns (rho 0.612, z 0.99); dyn_indusindbk_bo (rho 0.551, z -0.04)
- Source: US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nifty, global markets, US bonds? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-date-today-what-trumps-loss-mean-for-gold-sensex-nifty-global-markets-us-bonds-11793715305962.html
- Source: Market wrap:  BSE, Nestle India, Power Grid, SBI top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-bse-nestle-india-power-grid-sbi-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/135495602.cms
- Source: Nifty crosses 23,800 for first time since August on falling crude prices, earnings boost — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/nifty-crosses-23800-for-first-time-since-august-on-falling-crude-prices-earnings-boost/article71660642.ece
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [RED 6.72] cross-asset · 4 series ↓
- ust_2y [RATES]: last 4.56, z20 -3.06, zc -0.84, resid-z -0.81 [quiet], 1d -1.08%, |z20|=3.06
- ust_10y [RATES]: last 4.94, z20 -1.79, zc -0.75, resid-z -1.16 [quiet], 1d -0.80%, |z20|=1.79
- tips_10y_real [RATES]: last 2.60, z20 -1.76, zc -0.63, resid-z -0.61 [quiet], 1d -1.14%, |z20|=1.76
- dyn_schd [EQUITIES]: last 35.58, z20 1.17, zc -1.02, resid-z -0.68 [quiet], 1d -0.88%, 1y-pct=98
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.521 vs dyn_schd, historically leads by 4d
- Watch next: dyn_tgt (co-move) — not yet - watch; rho 0.602 vs dyn_schd
- Watch next: kospi (inverse) — not yet - watch; rho -0.546 vs dyn_schd
- Source: Small-cap stock under  ₹50 jumps 5% after announcement of Q2 Results 2026, dividend | Up 65% in 6 months; do you own? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/smallcap-stock-under-rs-50-jumps-5-after-announcement-of-q2-results-2026-dividend-up-65-in-6-months-do-you-own-11793700056652.html
- Source: German bond yields rise as oil climbs ahead of US Midterm elections — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/news/german-bond-yields-rise-as-oil-climbs-ahead-of-us-midterm-elections/articleshow/135490769.cms
- Source: Asian Paints surges 2.7% as investors rush ahead of dividend ex-date — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/stock-markets/asian-paints-surges-27-as-investors-rush-ahead-of-dividend-ex-date/article71659864.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.57), 2025-05-19 (d=1.16)

### [RED 5.38] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3934.40, z20 -2.06, zc -0.49, resid-z -2.77 [unexplained], 1d -0.89%, |z20|=2.06; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 79.22, z20 2.00, zc n/a, resid-z n/a [quiet], 1d 1.22%, |z20|=2.00
- comex_silver [COMMODITIES]: last 49.67, z20 -1.98, zc -0.68, resid-z -0.50 [quiet], 1d -2.08%, |z20|=1.98; 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.524 vs comex_gold
- Source: US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nifty, global markets, US bonds? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-date-today-what-trumps-loss-mean-for-gold-sensex-nifty-global-markets-us-bonds-11793715305962.html
- Source: Indian gold demand down 30% in September quarter as high prices hurt jewellery sales — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/gold/gold-demand-down-30-in-september-quarter-as-high-prices-hurt-jewellery-sales/article71660046.ece
- Source: Gold demand down 30% in September quarter as high prices hurt jewellery sales — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/gold/gold-demand-down-30-in-september-quarter-as-high-prices-hurt-jewellery-sales/article71660046.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.18] indices · 3 series ↓
- vix [INDICES]: last 20.67, z20 1.86, zc -0.24, resid-z n/a [quiet], 1d -2.27%, |z20|=1.86
- sp500 [INDICES]: last 7578.49, z20 -1.85, zc 0.51, resid-z -2.23 [unexplained], 1d 0.49%, |z20|=1.85
- nasdaq_100 [INDICES]: last 28211.01, z20 -1.81, zc 0.44, resid-z -0.35 [quiet], 1d 0.79%, |z20|=1.81
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-20 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.687 vs vix
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.609 vs vix
- Source: Shopify’s stock slides after earnings. This is what’s worrying Wall Street. — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/shopifys-stock-slides-after-earnings-this-is-whats-worrying-wall-street-e2e8d52b?mod=mw_rss_topstories
- Source: US stocks today: Technology stocks lift S&P 500 as US midterm vote keeps investors on edge — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-sp-500-nasdaq-open-higher-as-oil-prices-extend-declines-midterms-on-tap/articleshow/135503356.cms
- Source: US Stock Market Live Updates: S&P 500, Nasdaq rise ahead of midterm results; Apple falls — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/stock-market-live-updates-dow-jones-nasdaq-sp-500-apple-palantir-nvidia-midterm-elections-us-iran-war-crude-oil-prices-ai-stocks-treasury-yields-earnings-news-3rd-november-2026/liveblog/135501430.cms
- Historical analogues: 2026-05-20 (d=0.14), 2025-08-18 (d=0.18), 2025-10-23 (d=0.18)

### [RED 4.73] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 928.00, z20 -2.73, zc -0.12, resid-z -1.16 [quiet], 1d -0.32%, |z20|=2.73; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.578 via dyn_policybzr_ns, z 0.99, quiet); nifty_midcap_100 (rho 0.52 via dyn_policybzr_ns, z 0.37, quiet); nifty_50 (rho 0.482 via dyn_policybzr_ns, z 3.95, reacted); dyn_indusindbk_bo (rho 0.45 via dyn_policybzr_ns, z -0.04, quiet); nifty_metal (rho 0.367 via dyn_policybzr_ns, z 0.61, quiet)
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.578 vs dyn_policybzr_ns, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.723 vs dyn_policybzr_ns
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.52 vs dyn_policybzr_ns
- **India receivers**: dyn_bajfinance_ns (rho 0.578, z 0.99); nifty_midcap_100 (rho 0.52, z 0.37); nifty_50 (rho 0.482, z 3.95); dyn_indusindbk_bo (rho 0.45, z -0.04)
- Source: Broker’s call: PB Fintech (Buy) — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/brokers-call-pb-fintech-buy/article71656563.ece
- Source: MobiKwik shares zoom 10% as fintech firm posts record Rs 12 crore profit in Q2 — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/mobikwik-shares-zoom-10-as-fintech-firm-posts-record-rs-12-crore-profit-in-q2/articleshow/135452378.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [AMBER 4.71] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 146.09, z20 -1.88, zc 1.28, resid-z -1.49 [quiet], 1d 5.99%, 1y-pct=2
- btc_usd [CRYPTO]: last 77528.82, z20 -1.68, zc 0.52, resid-z 0.18 [quiet], 1d 1.11%, |z20|=1.68
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.04).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: IEA Warns Global Gas Crunch Could Last Well into 2027 — OilPrice, 2026-11-03. https://oilprice.com/Latest-Energy-News/World-News/IEA-Warns-Global-Gas-Crunch-Could-Last-Well-into-2027.html
- Source: US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nifty, global markets, US bonds? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-date-today-what-trumps-loss-mean-for-gold-sensex-nifty-global-markets-us-bonds-11793715305962.html
- Source: Global refinery inputs fell sharply in the second quarter of 2026 before modest recovery — EIA Today in Energy, 2026-11-03. https://www.eia.gov/todayinenergy/detail.php?id=68404
- Historical analogues: 2026-05-22 (d=0.04), 2026-04-02 (d=0.19), 2025-10-22 (d=0.35)

### [AMBER 4.4] dyn_jef ↑
- dyn_jef [EQUITIES]: last 48.75, z20 2.40, zc 0.29, resid-z -3.25 [unexplained], 1d 0.99%, |z20|=2.40
- **Mechanism**: dyn_jef ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.47 via dyn_jef, z -0.04, quiet)
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.73 vs dyn_jef
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.573 vs dyn_jef
- **India receivers**: dyn_indusindbk_bo (rho 0.47, z -0.04)
- Source: ITC shares rise 2% after Q2 results. What are Jefferies, Nuvama and others saying? — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/stocks/news/itc-shares-rise-2-after-q2-results-what-are-jefferies-nuvama-and-others-saying/articleshow/135481293.cms
- Source: Delhivery shares soar 6% after Q2 results; JPMorgan, Jefferies, Kotak, Citi maintain buy calls — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/delhivery-shares-jump-95-after-q2-results-jpmorgan-jefferies-kotak-citi-maintain-buy-calls/article71655384.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [AMBER 4.37] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1795.00, z20 2.37, zc 0.35, resid-z -0.37 [quiet], 1d 1.15%, |z20|=2.37; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.374 via dyn_atherenerg_ns, z 0.37, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.374, z 0.37)
- Source: Best EV stock to buy: Ather Energy vs Ola Electric Mobility; which is better profit-making deal? Investors guide, target — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/best-ev-stock-to-buy-ather-energy-vs-ola-electric-mobility-which-is-better-profit-making-deal-investors-guide-target-11793608999266.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.11), shanghai_comp ↓ (3.77), dyn_lth ↑ (3.76), dyn_4417_t ↑ (3.65), corn ↓ (3.54), dyn_sepn ↑ (3.32), dyn_tech ↑ (3.29), rates · 2 series ↑ (3.25), indices · 2 series ↑ (2.91), taiwan_weighted ↓ (2.89), dyn_techm_ns ↑ (2.82), usd_brl ↑ (2.36)

## India macro
- nifty_50: 23810.8496 (1d 1.58%, z20 3.95, flag red)
- nifty_midcap_100: 58598.0508 (1d 1.06%, z20 0.37, flag none)
- usd_inr: 94.7300 (1d -0.18%, z20 -0.88, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4610 (1d -0.51%, z20 -1.68, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · AMFI SIP / MF flows T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 92.3 — "Penny stock under  ₹10 jumps 7.5% after Q2 Results 2026 following Indian stock market rall"
- INOXINDIA.NS (INOX INDIA LIMITED) score 92.3 — "Penny stock under  ₹10 jumps 7.5% after Q2 Results 2026 following Indian stock market rall"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.9 — "Penny stock under  ₹10 jumps 7.5% after Q2 Results 2026 following Indian stock market rall"
- INDIANB.NS (INDIAN BANK) score 63.3 — "US MIDTERMS HISTORICALLY SIGNAL STRONG STOCK MARKET GAINS The S&P 500 has gained an averag"
- OHI (Omega Healthcare Investors, In) score 48.7 — "Wall Street's hidden bargains: 10 US largecap stocks trading at historic discount for inve"
- BAC (Bank of America Corporation) score 43.8 — "US MIDTERMS HISTORICALLY SIGNAL STRONG STOCK MARKET GAINS The S&P 500 has gained an averag"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.6 — "European shares fall as tech stocks slide, Middle East tensions weigh"
- TGT (Target Corporation) score 41.6 — "Marico share price: FMCG stock gains 8% on strong Q2 results, nears 52-week high - Buy or "
- HDB (HDFC Bank Limited) score 41.5 — "US MIDTERMS HISTORICALLY SIGNAL STRONG STOCK MARKET GAINS The S&P 500 has gained an averag"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.6 — "European shares fall as tech stocks slide, Middle East tensions weigh"
- TECH (Bio-Techne Corp) score 39.6 — "European shares fall as tech stocks slide, Middle East tensions weigh"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.2 — "US MIDTERMS HISTORICALLY SIGNAL STRONG STOCK MARKET GAINS The S&P 500 has gained an averag"
- IDBI.NS (IDBI BANK LIMITED) score 39.2 — "US MIDTERMS HISTORICALLY SIGNAL STRONG STOCK MARKET GAINS The S&P 500 has gained an averag"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.2 — "US MIDTERMS HISTORICALLY SIGNAL STRONG STOCK MARKET GAINS The S&P 500 has gained an averag"
- COIN (Coinbase Global, Inc.) score 34.3 — "Global refinery inputs fell sharply in the second quarter of 2026 before modest recovery"
- CHKP (Check Point Software Technolog) score 30.5 — "Nifty Expiry Today Prediction 3 Nov: Bulls back in action! Check support, resistance level"
- RS (Reliance, Inc.) score 29.3 — "Reliance shares see volume breakout: Is a trend reversal around the corner? Here’s what RI"
- 301077.SZ (CHINASTARS) score 26.8 — "‘Speak last’: China’s fifth plenum moves to rein in Communist Party leaders"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.9 — "My father has Alzheimer’s and his caregiver is using his debit card for DoorDash. Should I"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.4 — "US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nift"
- LTH (Life Time Group Holdings, Inc.) score 23.9 — "Dubai Benchmark Slips Into Contango for the First Time Since July"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 15.5 — "Q2 Results Today Live: SBI Q2 profit up 14%; Bajaj Finserv, Pfizer, Solar Ind Q2 earnings "
- JIOFIN.BO (Jio Financial Services Limited) score 15.0 — "Motilal Oswal Financial Services announces leadership rejig; appoints new heads across bus"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.6 — "HDFC Bank share price gains 3% today: Here's why - Is the worst over after a 27% one-year "
- BZ=F (Brent Crude Oil Last Day Finan) score 13.2 — "IEA Warns Global Gas Crunch Could Last Well into 2027"
- SCHD (Schwab US Dividend Equity ETF) score 12.3 — "Asian Paints surges 2.7% as investors rush ahead of dividend ex-date"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.7 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.7 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- SEPN (Septerna, Inc.) score 10.9 — "Indian gold demand down 30% in September quarter as high prices hurt jewellery sales"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.7 — "Utkarsh Small Finance Bank reports sixth consecutive quarterly loss"
- META (Meta) score 9.6 — "Q2 Results Today Live: SBI Q2 profit up 14%; Bajaj Finserv, Pfizer, Solar Ind Q2 earnings "
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.6 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.4 — "Diwali stock picks: Titan, Eternal, BSE to Adani Ports — 10 long-term bets by Motilal Oswa"
- VT (Vanguard Total World Stock Ind) score 8.2 — "ADNOC Chief Says World Has “Eroded Its Supply Buffers”"
- JEF (Jefferies Financial Group Inc.) score 7.9 — "ITC shares rise 2% after Q2 results. What are Jefferies, Nuvama and others saying?"
- GS (Goldman Sachs Group, Inc. (The) score 6.8 — "DEMOCRATIC SWEEP AT 73%. WALL STREET BRACES FOR MIDTERMS. Prediction markets price a 73% c"
- INFY (Infosys Limited) score 4.9 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- BNBA-EUR.PA (21Shares Binance Coin ETP) score 2.1 — "Binance says North Korean hackers stole $6.34 billion funds in a technical breach"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.8 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.8 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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