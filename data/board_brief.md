# Transmission Layer — board brief · 2026-09-04 14:20Z

data as of **2026-09-04** · 98 series · 8 red / 38 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.213, 2d in regime; vol-pct 0.131, breadth-off 0.294, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.44, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.88, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.08, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.23, corr60 -0.14, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.03, corr60 0.23, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.002977997490474893)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.501** (n=1127) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.831** (n=1953) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.76] usd_jpy ↓
- usd_jpy [FX]: last 156.07, z20 -5.76, zc -3.31, resid-z -4.81 [unexplained], 1d -1.80%, |z20|=5.76
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.537 vs usd_jpy
- Watch next: kospi (inverse) — not yet - watch; rho -0.503 vs usd_jpy
- Source: Global Market: JGB yields extend fall as stronger yen, hawkish BOJ outlook lift sentiment — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-jgb-yields-extend-fall-as-stronger-yen-hawkish-boj-outlook-lift-sentiment/articleshow/133753277.cms
- Source: Yen Rallies as Intervention, BOJ Rate Risk Weigh on Traders — Mint Markets, 2026-09-03. https://www.livemint.com/market/yen-rallies-as-intervention-boj-rate-risk-weigh-on-traders-11788476981657.html
- Source: Yen Rallies as Intervention, BOJ Rate Risk Weigh on Wary Traders — Mint Markets, 2026-09-03. https://www.livemint.com/market/yen-rallies-as-intervention-boj-rate-risk-weigh-on-wary-traders-11788476981201.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 7.21] commodities · 2 series ↑
- wti [COMMODITIES]: last 89.31, z20 1.38, zc -0.90, resid-z -0.83 [quiet], 1d -2.18%, 1-session move -2.18% ≥ 1.5%
- brent [COMMODITIES]: last 93.88, z20 1.10, zc -0.75, resid-z -0.76 [quiet], 1d -1.72%, 1-session move -1.72% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho -0.383 via wti, z -0.82, quiet)
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.644 vs wti
- **India receivers**: dyn_adanient_bo (rho -0.383, z -0.82)
- Source: Elevated crack spreads and crude oil prices contribute to higher prices at the pump — EIA Today in Energy, 2026-09-04. https://www.eia.gov/todayinenergy/detail.php?id=68104
- Source: Iran Says It's Found Ways to Dodge U.S. Oil Blockade — OilPrice, 2026-09-04. https://oilprice.com/Latest-Energy-News/World-News/Iran-Says-Its-Found-Ways-to-Dodge-US-Oil-Blockade.html
- Source: The Iran War Has Put Venezuela’s Oil Back in the Spotlight — OilPrice, 2026-09-04. https://oilprice.com/Energy/Energy-General/The-Iran-War-Has-Put-Venezuelas-Oil-Back-in-the-Spotlight.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.59] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.39, z20 2.66, zc 0.00, resid-z 0.16 [quiet], 1d 0.00%, |z20|=2.66; 1y-pct=99
- ust_10y [RATES]: last 4.79, z20 2.37, zc 0.00, resid-z 0.12 [quiet], 1d 0.00%, |z20|=2.37; 1y-pct=99
- tips_10y_real [RATES]: last 2.45, z20 1.41, zc 0.24, resid-z 0.43 [quiet], 1d 0.41%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.09, z20 -1.33, zc 0.14, resid-z 0.94 [quiet], 1d 0.05%, 1y-pct=1
- ust_30y [RATES]: last 5.27, z20 1.11, zc 0.00, resid-z 0.06 [quiet], 1d 0.00%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.382 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.502 vs dyn_bond
- Source: Is the stock market open on Labor Day? What about bond trading? Will the post office deliver mail? — MarketWatch Top, 2026-09-04. https://www.marketwatch.com/story/is-the-stock-market-open-on-labor-day-does-the-post-office-deliver-mail-6d58fd77?mod=mw_rss_topstories
- Source: Global Market: German bond yields set for fourth weekly rise as investors bet on further ECB tightening — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-german-bond-yields-set-for-fourth-weekly-rise-as-investors-bet-on-further-ecb-tightening/articleshow/133760410.cms
- Source: Sensex today | Stock Market Live: Sensex rises 530 pts, Nifty up 65 pts on easing US Treasury yields; SBI Life, HDFC Life top gainers — BusinessLine Mkts, 2026-09-04. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-4th-september-2026/article71425360.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 5.2] cross-asset · 3 series ↑
- vix [INDICES]: last 14.04, z20 -1.88, zc -0.24, resid-z n/a [quiet], 1d -1.96%, |z20|=1.88; 1y-pct=1
- dyn_vt [EQUITIES]: last 161.63, z20 0.88, zc -0.10, resid-z -0.03 [quiet], 1d -0.08%, 1y-pct=98
- sp500 [INDICES]: last 7726.91, z20 0.35, zc -0.34, resid-z -0.24 [quiet], 1d -0.27%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-27 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.649 vs vix, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.64 vs dyn_vt, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.645 vs vix
- Watch next: dax (co-move) — not yet - watch; rho 0.523 vs dyn_vt
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.505 vs dyn_vt
- Source: Wall Street mixed after stronger-than-expected jobs data — Mint Markets, 2026-09-04. https://www.livemint.com/market/wall-street-mixed-after-stronger-than-expected-jobs-data-11788529451652.html
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks subdued after jobs report fuels rate-hike bets — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-waller-earnings-forecast-lululemon-adobe-stock-price-news-4th-september-2026/liveblog/133762584.cms
- Source: How does the world's largest crypto exchange, Binance, keep doing business in Europe without a license? Explained — Mint Markets, 2026-09-04. https://www.livemint.com/market/cryptocurrency/how-does-the-worlds-largest-crypto-exchange-binance-keep-doing-business-in-europe-without-a-license-explained-11788518577281.html
- Historical analogues: 2025-08-27 (d=0.14), 2025-10-23 (d=0.17), 2025-10-31 (d=0.17)

### [RED 4.99] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 11.99, z20 2.99, zc 4.07, resid-z 4.28 [unexplained], 1d 13.97%, |z20|=2.99
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PC Jeweller clears debt to one more bank, nears debt-free status — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/gold/pc-jeweller-clears-debt-to-one-more-bank-nears-debt-free-status/article71423219.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [RED 4.61] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1510.00, z20 -2.61, zc -0.18, resid-z -0.06 [quiet], 1d -0.26%, |z20|=2.61; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Eternal, ICICI Bank, 5 other largecap stocks with upside potential of up to 40%. Do you own any? — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/stocks/news/eternal-icici-bank-5-other-largecap-stocks-with-upside-potential-of-up-to-40-do-you-own-any/slideshow/133751438.cms
- Source: Explained: What $127 billion FCNR(B) inflows mean for ICICI Bank, HDFC Bank, other bank stocks — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/explained-what-127-billion-fcnrb-inflows-mean-for-icici-bank-hdfc-bank-other-bank-stocks/articleshow/133725930.cms
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 4.59] dyn_nvda ↑
- dyn_nvda [EQUITIES]: last 234.21, z20 2.59, zc 0.79, resid-z 0.94 [quiet], 1d 2.52%, |z20|=2.59; 1y-pct=99
- **Mechanism**: dyn_nvda ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.39 via dyn_nvda, z 2.51, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.627 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.587 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.584 vs dyn_nvda, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.39, z 2.51)
- Source: Nvidia takes back control of the AI trade as Big Tech nears record highs — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/nvidia-takes-back-control-of-the-ai-trade-as-big-tech-nears-record-highs-c0dfed9d?mod=mw_rss_topstories
- Source: US stocks rise as Fed Governor signals possible rate pause; Nvidia, Snowflake rally — Mint Markets, 2026-09-03. https://www.livemint.com/market/stock-market-news/us-stocks-climb-after-fed-governor-s-comments-on-holding-rates-steady-11788443392991.html
- Source: Here’s what Nvidia’s $13 billion Hugging Face deal means for the world of AI — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/heres-what-nvidias-13-billion-hugging-face-deal-means-for-the-world-of-ai-360e9fd1?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

### [AMBER 4.46] dyn_dell ↑
- dyn_dell [EQUITIES]: last 521.34, z20 2.46, zc 0.13, resid-z 2.36 [unexplained], 1d 0.96%, |z20|=2.46; 1y-pct=100
- **Mechanism**: dyn_dell ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho 0.463 via dyn_dell, z 1.41, reacted); nifty_it (rho -0.439 via dyn_dell, z -0.58, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.542 vs dyn_dell, historically leads by 5d
- **India receivers**: dyn_coalindia_ns (rho 0.463, z 1.41); nifty_it (rho -0.439, z -0.58)
- Source: Dell’s AI Boom: $95 billion backlog reshapes growth outlook — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/dells-ai-boom-95-billion-backlog-reshapes-growth-outlook/slideshow/133726366.cms
- Source: HPE follows in Dell’s footsteps as it rides the AI server boom to a big earnings beat — MarketWatch Top, 2026-09-02. https://www.marketwatch.com/story/hpe-follows-in-dells-footsteps-as-it-rides-the-ai-server-boom-to-a-big-earnings-beat-ec46eaea?mod=mw_rss_topstories
- Source: Dell stock price news: Shares jump 14% on record Q2 results as AI server demand surges — data details — Mint Markets, 2026-09-02. https://www.livemint.com/market/stock-market-news/dell-stock-price-news-shares-jump-14-on-record-q2-results-as-ai-server-demand-surges-data-details-11788356963938.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

## Watchlist (below surfacing floor)
nifty_50 ↓ (3.78), natgas ↑ (3.73), usd_inr ↓ (3.65), dyn_havells_ns ↓ (3.49), midcap_largecap_ratio ↑ (3.47), gold_silver_ratio ↓ (3.05), dyn_tech ↑ (3.05), usd_cny ↓ (2.93), fx · 2 series ↑ (2.64), dyn_atherenerg_ns ↑ (2.56), dyn_inoxindia_ns ↑ (2.51), dyn_heromotoco_ns ↓ (2.22)

## India macro
- nifty_50: 23897.6992 (1d 0.10%, z20 -1.78, flag amber)
- nifty_midcap_100: 63081.2500 (1d -0.24%, z20 -2.06, flag amber)
- usd_inr: 94.4750 (1d -0.01%, z20 -1.65, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6396 (1d -0.35%, z20 0.47, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.6 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- COALINDIA.NS (COAL INDIA LTD) score 83.1 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.7 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- INDIANB.NS (INDIAN BANK) score 79.6 — "Philip R. Lane: Diversity at the European Central Bank"
- BAC (Bank of America Corporation) score 68.8 — "Philip R. Lane: Diversity at the European Central Bank"
- COIN (Coinbase Global, Inc.) score 62.4 — "Global Market: European shares edge lower as investors await US jobs data"
- HDB (HDFC Bank Limited) score 62.0 — "Philip R. Lane: Diversity at the European Central Bank"
- IDBI.NS (IDBI BANK LIMITED) score 59.3 — "Philip R. Lane: Diversity at the European Central Bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.3 — "Philip R. Lane: Diversity at the European Central Bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 59.3 — "Philip R. Lane: Diversity at the European Central Bank"
- BOND (PIMCO Active Bond Exchange-Tra) score 57.0 — "Global Market: German bond yields set for fourth weekly rise as investors bet on further E"
- CHKP (Check Point Software Technolog) score 46.9 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- OHI (Omega Healthcare Investors, In) score 43.0 — "US Market: Coinbase seeks US nod to bring equity perpetuals to investors"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.3 — "Can Big Tech’s $1-trillion AI bet pay off? Jefferies explains why it remains bullish"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.0 — "Can Big Tech’s $1-trillion AI bet pay off? Jefferies explains why it remains bullish"
- TECH (Bio-Techne Corp) score 41.0 — "Can Big Tech’s $1-trillion AI bet pay off? Jefferies explains why it remains bullish"
- LTH (Life Time Group Holdings, Inc.) score 33.9 — "UBL slips as analysts stay divided on margin timeline"
- 301077.SZ (CHINASTARS) score 25.1 — "U.S.-Venezuela Oil Deal Threatens China’s Oil-Backed Loans"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.3 — "Penny stock under 10 rupees: Upper circuit — Leather share jumps 74% in 4 sessions | Back-"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.4 — "Priority Jewels IPO listing today: Will the jewellery maker deliver gains? Here's what GMP"
- NVDA (NVIDIA Corporation) score 15.0 — "Nvidia takes back control of the AI trade as Big Tech nears record highs"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.7 — "Retail investors raise stakes in 10 stocks for two straight quarters; shares rally up to 8"
- JIOFIN.BO (Jio Financial Services Limited) score 14.6 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.4 — "SEBI goes after Hindenburg, others in Adani case"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.1 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.9 — "Market wrap:  RIL,Tata Steel, Bharti Airtel, HCL Tech top gainers and losers on Nifty and "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.8 — "Market wrap:  RIL,Tata Steel, Bharti Airtel, HCL Tech top gainers and losers on Nifty and "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.2 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.7 — "TRUMP: I JUST WANT THE WAR ENDED IN UKRAINE"
- VT (Vanguard Total World Stock Ind) score 7.8 — "How does the world's largest crypto exchange, Binance, keep doing business in Europe witho"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.8 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- MS (Morgan Stanley) score 7.6 — "Cipla slips after Qilu Pembrolizumab deal; Morgan Stanley flags crowded field"
- META (Meta) score 6.2 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.9 — "Eternal, ICICI Bank, 5 other largecap stocks with upside potential of up to 40%. Do you ow"
- DELL (Dell Technologies Inc.) score 4.0 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.2 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.8 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 0.6 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.5 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas reported strong growth in June quarter, but failed to impress"

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