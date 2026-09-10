# Transmission Layer — board brief · 2026-09-10 08:56Z

data as of **2026-09-10** · 98 series · 16 red / 37 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.548, 2d in regime; vol-pct 0.345, breadth-off 0.75, Markov P(high-vol) 0.018)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.32, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.27, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.23, corr60 0.12, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.81, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.04, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.17, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.08, corr60 0.04, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1122) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2037) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.22] cross-asset · 6 series ↑
- dow_jones [INDICES]: last 52391.48, z20 -3.07, zc -0.91, resid-z -0.43 [quiet], 1d -0.75%, |z20|=3.07
- brent [COMMODITIES]: last 102.13, z20 2.52, zc 0.40, resid-z 0.78 [quiet], 1d 0.91%, |z20|=2.52
- wti [COMMODITIES]: last 96.98, z20 2.34, zc 0.43, resid-z 0.76 [quiet], 1d 0.97%, |z20|=2.34
- russell_2000 [INDICES]: last 2921.10, z20 -2.09, zc -1.12, resid-z -1.19 [quiet], 1d -1.32%, |z20|=2.09
- vix [INDICES]: last 16.45, z20 1.91, zc -0.01, resid-z n/a [quiet], 1d -0.06%, |z20|=1.91
- sp500 [INDICES]: last 7637.70, z20 -1.50, zc -0.61, resid-z -0.56 [quiet], 1d -0.47%, |z20|=1.50
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-21 (z-distance 0.47).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.667 vs dow_jones, historically leads by 5d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.557 vs brent, historically leads by 4d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.557 vs sp500, historically leads by 1d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.531 vs brent, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.547 vs dow_jones
- Source: Sensex today | Stock Market Live: Sensex, Nifty trades weak as crude oil surge, geopolitical tensions weigh on sentiment — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-10th-september-2026/article71448206.ece
- Source: Sensex, Nifty trade firm in mid-session; crude prices, geopolitical tensions keep risk appetite subdued — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/sensex-nifty-trade-firm-in-mid-session-crude-prices-geopolitical-tensions-keep-risk-appetite-subdued/article71450674.ece
- Source: Global Market: Japan Nikkei falls as oil tops $100, BOJ rate hike bets rise — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-nikkei-falls-as-oil-tops-100-boj-rate-hike-bets-rise/articleshow/133996320.cms
- Historical analogues: 2025-10-21 (d=0.47), 2024-10-18 (d=0.48), 2026-05-22 (d=0.49)

### [RED 6.31] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 23424.45, z20 -2.64, zc -0.05, resid-z -1.01 [quiet], 1d -0.03%, |z20|=2.64
- nifty_midcap_100 [INDICES]: last 62336.30, z20 -2.53, zc -0.60, resid-z -0.90 [quiet], 1d -0.41%, |z20|=2.53
- india_vix [INDICES]: last 11.85, z20 1.95, zc -0.10, resid-z n/a [quiet], 1d -0.55%, |z20|=1.95
- dyn_jiofin_bo [EQUITIES]: last 230.40, z20 -1.86, zc -0.18, resid-z -0.13 [quiet], 1d -0.26%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.627 via nifty_50, z -1.73, reacted); dyn_indianb_ns (rho 0.558 via nifty_midcap_100, z -2.38, reacted); nifty_it (rho 0.513 via nifty_50, z -2.98, reacted); dyn_techm_ns (rho 0.48 via nifty_50, z -2.52, reacted); dyn_indusindbk_bo (rho 0.465 via nifty_50, z -1.02, reacted)
- **India receivers**: nifty_fmcg (rho 0.627, z -1.73); dyn_indianb_ns (rho 0.558, z -2.38); nifty_it (rho 0.513, z -2.98); dyn_techm_ns (rho 0.48, z -2.52)
- Source: Sensex today | Stock Market Live: Sensex, Nifty trades weak as crude oil surge, geopolitical tensions weigh on sentiment — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-10th-september-2026/article71448206.ece
- Source: Sensex, Nifty trade firm in mid-session; crude prices, geopolitical tensions keep risk appetite subdued — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/sensex-nifty-trade-firm-in-mid-session-crude-prices-geopolitical-tensions-keep-risk-appetite-subdued/article71450674.ece
- Source: Is Zerodha down? Brokerage flags BSE F&O issue on Sensex expiry day — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/is-zerodha-down-brokerage-flags-bse-f-o-issue-on-sensex-expiry-day-11789024911548.html
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 6.3] cross-asset · 3 series ↓
- nifty_it [INDICES]: last 28825.95, z20 -2.98, zc -0.19, resid-z -0.12 [quiet], 1d -0.30%, |z20|=2.98
- dyn_techm_ns [EQUITIES]: last 1516.60, z20 -2.52, zc 0.34, resid-z 0.24 [quiet], 1d 0.57%, |z20|=2.52
- dyn_tataelxsi_ns [EQUITIES]: last 3406.30, z20 -2.36, zc 0.38, resid-z 0.75 [quiet], 1d 0.69%, |z20|=2.36; 1y-pct=1
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.587 via nifty_it, z -1.44, reacted); nifty_50 (rho 0.513 via nifty_it, z -2.64, reacted)
- Watch next: shanghai_comp (inverse) — not yet - watch; rho -0.508 vs dyn_techm_ns, historically leads by 5d
- **India receivers**: dyn_tatatech_ns (rho 0.587, z -1.44); nifty_50 (rho 0.513, z -2.64)
- Source: IT stocks crash as Coforge, Infy, Tech Mahindra, HCL, TCS slide on H-1B visa fee hike — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide-h1-b-visa-in-focus/article71445708.ece
- Source: IT stocks crash as Coforge leads selloff; Infosys, Tech Mahindra, HCL Tech, TCS slide — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide/article71445708.ece
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-09-sep-2026/liveblog/133950510.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [AMBER 5.7] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 89.73, z20 -2.04, zc -0.90, resid-z 0.59 [quiet], 1d -0.29%, |z20|=2.04; 1y-pct=0
- ust_10y [RATES]: last 4.80, z20 1.88, zc 0.22, resid-z -0.18 [quiet], 1d 0.42%, |z20|=1.88; 1y-pct=100
- ust_2y [RATES]: last 4.39, z20 1.80, zc 0.54, resid-z 0.16 [quiet], 1d 0.46%, |z20|=1.80; 1y-pct=99
- ust_30y [RATES]: last 5.25, z20 0.37, zc -0.25, resid-z -0.54 [quiet], 1d 0.19%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.357 via ust_2y, z 1.42, reacted)
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.78 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.357, z 1.42)
- Source: US Treasury yields hit highest level since 2023 as buyback disappoints — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-hit-highest-level-since-2023-as-buyback-disappoints/articleshow/133996569.cms
- Source: Global Market: Japanese bond yields rise as oil surge, hawkish BOJ remarks lift rate hike bets — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japanese-bond-yields-rise-as-oil-surge-hawkish-boj-remarks-lift-rate-hike-bets/articleshow/133994320.cms
- Source: US Treasury triples bond buyback to $6 billion: Why markets saw the move as a disappointment — Mint Markets, 2026-09-09. https://www.livemint.com/market/stock-market-news/us-treasury-triples-bond-buyback-to-6-billion-why-markets-saw-the-move-as-a-disappointment-11788973032057.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 5.48] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 22.08, z20 -3.48, zc -1.25, resid-z -0.32 [quiet], 1d -1.78%, |z20|=3.48; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.621 via dyn_hdb, z -2.64, reacted); nifty_it (rho 0.535 via dyn_hdb, z -2.98, reacted); dyn_techm_ns (rho 0.461 via dyn_hdb, z -2.52, reacted); dyn_jiofin_bo (rho 0.398 via dyn_hdb, z -1.86, reacted); dyn_tataelxsi_ns (rho 0.388 via dyn_hdb, z -2.36, reacted)
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.51 vs dyn_hdb, historically leads by 3d
- **India receivers**: nifty_50 (rho 0.621, z -2.64); nifty_it (rho 0.535, z -2.98); dyn_techm_ns (rho 0.461, z -2.52); dyn_jiofin_bo (rho 0.398, z -1.86)
- Source: HDFC Bank shares rebound from fresh 52-week low: What is driving the stock? — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-hit-fresh-52-week-low-for-second-straight-day-what-is-driving-the-stock/article71450256.ece
- Source: HDFC Bank shares fall 2% to fresh 52-week low; here’s why — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-2-to-fresh-52-week-low-heres-why/article71446043.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 5.46] dyn_meta ↑
- dyn_meta [EQUITIES]: last 653.41, z20 3.46, zc 2.85, resid-z 0.39 [moved], 1d 6.51%, |z20|=3.46
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.372 via dyn_meta, z -2.53, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.372, z -2.53)
- Source: US stocks fall as oil surges past $100 on deepening Middle East tensions, Meta jumps 5.5%, AMD gains 3.49% — Mint Markets, 2026-09-09. https://www.livemint.com/market/us-stocks-fall-as-oil-surges-past-100-on-deepening-middle-east-tensions-11788961419384.html
- Source: Meta’s stock jumps as new personal AI agent Muse addresses a major investor concern — MarketWatch Top, 2026-09-09. https://www.marketwatch.com/story/meta-stock-jumps-as-new-personal-ai-agent-muse-addresses-a-major-investor-concern-5ad0a373?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [RED 4.98] dyn_qcom ↑
- dyn_qcom [EQUITIES]: last 176.42, z20 2.98, zc 0.65, resid-z 0.37 [quiet], 1d 1.34%, |z20|=2.98
- **Mechanism**: dyn_qcom ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.503 vs dyn_qcom, historically leads by 2d
- Source: Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/us-stocks/news/qualcomm-amazon-ai-deal-why-the-chipmakers-stock-surged/slideshow/133955258.cms
- Source: Qualcomm stock jumps 9% on AI chip deal with Amazon, hits 2-month high — Mint Markets, 2026-09-08. https://www.livemint.com/market/stock-market-news/qualcomm-stock-jumps-9-on-ai-chip-deal-with-amazon-hits-2-month-high-11788882415437.html
- Source: Qualcomm’s stock climbs as Amazon chip deal offers investors much-needed good news — MarketWatch Top, 2026-09-08. https://www.marketwatch.com/story/qualcomms-stock-climbs-as-amazon-chip-deal-offers-investors-some-much-needed-good-news-5b6a95ca?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.02), 2026-05-04 (d=0.1)

### [RED 4.92] dyn_coalindia_ns ↑
- dyn_coalindia_ns [EQUITIES]: last 433.65, z20 2.92, zc 0.46, resid-z 0.39 [quiet], 1d 0.61%, |z20|=2.92
- **Mechanism**: dyn_coalindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on Thu, 10 Sept | Triggers — Mint Markets, 2026-09-09. https://www.livemint.com/market/top-stocks-in-focus-tomorrow-investors-must-watch-coal-india-shakti-pumps-wipro-shares-on-thu-10-sept-triggers-11788964212253.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

## Watchlist (below surfacing floor)
hang_seng ↓ (4.7), gold_silver_ratio ↓ (4.67), comex_copper ↑ (4.55), usd_jpy ↓ (4.49), midcap_largecap_ratio ↑ (4.42), commodities · 2 series ↑ (4.41), indices · 4 series ↓ (4.39), dyn_indianb_ns ↓ (4.38), dyn_icicigi_bo ↓ (4.17), dyn_pcjeweller_ns ↑ (4.11), dyn_lth ↓ (4.1), dyn_lenskart_ns ↑ (3.5)

## India macro
- nifty_50: 23424.4492 (1d -0.03%, z20 -2.64, flag red)
- nifty_midcap_100: 62336.3008 (1d -0.41%, z20 -2.53, flag red)
- usd_inr: 95.4050 (1d 0.61%, z20 0.43, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6612 (1d -0.38%, z20 1.42, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · India CPI T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.4 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.5 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- COALINDIA.NS (COAL INDIA LTD) score 81.4 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- INDIANB.NS (INDIAN BANK) score 57.4 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- COIN (Coinbase Global, Inc.) score 54.0 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- BAC (Bank of America Corporation) score 50.7 — "Stocks to Watch Today: Indian Bank, Hindustan Zinc, Wipro, Shakti Pumps and more"
- OHI (Omega Healthcare Investors, In) score 46.2 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- HDB (HDFC Bank Limited) score 45.3 — "Stocks to Watch Today: Indian Bank, Hindustan Zinc, Wipro, Shakti Pumps and more"
- CHKP (Check Point Software Technolog) score 45.0 — "Veegaland Developers IPO GMP jumps 17% on Day 1; should you apply? Check key dates, review"
- IDBI.NS (IDBI BANK LIMITED) score 41.1 — "Stocks to Watch Today: Indian Bank, Hindustan Zinc, Wipro, Shakti Pumps and more"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.1 — "Stocks to Watch Today: Indian Bank, Hindustan Zinc, Wipro, Shakti Pumps and more"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.1 — "Stocks to Watch Today: Indian Bank, Hindustan Zinc, Wipro, Shakti Pumps and more"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.5 — "HFCL shares hit lower circuit after 240% rally in 2026. What technical charts now indicate"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "HFCL shares hit lower circuit after 240% rally in 2026. What technical charts now indicate"
- TECH (Bio-Techne Corp) score 39.4 — "HFCL shares hit lower circuit after 240% rally in 2026. What technical charts now indicate"
- BOND (PIMCO Active Bond Exchange-Tra) score 38.2 — "Commodity Talk| Equities, bonds... and commodities? Why investors may need a third pillar "
- 301077.SZ (CHINASTARS) score 29.0 — "China’s Communist Party quietly signals social stability push with new high-level body"
- LTH (Life Time Group Holdings, Inc.) score 26.7 — "Glass Wall Systems IPO Day 3: Issue subscribed 8.22 times so far. GMP signals 36% listing "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.2 — "Ather Energy shares rise 3% as Nomura raises target price; stock up nearly 200% in 1 year"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.5 — "Hunter Biden memecoin $LAPTOP loses 95% of market value just hours after launch"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.1 — "Adani Power among 3 stocks showing White Marubozu Pattern"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.7 — "PC Jeweller share price shines for second session | What's behind the rally?"
- MS (Morgan Stanley) score 11.2 — "JPMorgan, Jane Street probes show India scrutinizing traders"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "This Tata Group stock surges 10% today amid a spurt in volume despite a weak stock market "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "This Tata Group stock surges 10% today amid a spurt in volume despite a weak stock market "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.2 — "Running the numbers on Trump’s $5,000 dividend proposal, from its cost to the impact on av"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.9 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- META (Meta) score 7.2 — "COPPER HITS RECORD AS GLOBAL SUPPLIES TIGHTEN Copper hit a fresh record of $14,802.50 a to"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.9 — "ICICI Prudential AMC gets RBI approval to buy up to 9.95% stake in Kotak and 3 other banks"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.5 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- JIOFIN.BO (Jio Financial Services Limited) score 6.3 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Shows Slight Growt"
- VT (Vanguard Total World Stock Ind) score 5.5 — "NSE slashes IPO ambitions as world’s biggest options boom fades"
- NVDA (NVIDIA Corporation) score 5.5 — "Global investing is no longer optional for Indian investors—but diversification is more th"
- JEF (Jefferies Financial Group Inc.) score 5.0 — "Vodafone Idea shares price in focus as Jefferies initiates coverage with Buy rating. Why a"
- IFCI.NS (IFCI LTD) score 3.8 — "IFCI share price down today- drops 14% in 2 days- Why is the stock falling?"
- QCOM (QUALCOMM Incorporated) score 2.9 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.2 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 1.0 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- DKS (Dick's Sporting Goods Inc) score 0.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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