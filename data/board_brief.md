# Transmission Layer — board brief · 2026-10-15 14:59Z

data as of **2026-10-15** · 97 series · 12 red / 30 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.703, 9d in regime; vol-pct 0.64, breadth-off 0.765, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.34, corr60 -0.42, contra nifty_50 corr20=0.36, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.21, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 0.14, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.03, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.27, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.71, corr60 0.22, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0010018738275714423)
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.261, β 0.3681, p 2e-05); driver zc 2.62 → expected 0.329%. Type hit-rate 0.824 (n=2185).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.26, β 0.2666, p 0.02643); driver zc 1.53 → expected 0.279%. Type hit-rate 0.824 (n=2185).
- Track record · residual_reversion: hit-rate **0.496** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2185) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.32] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 73.04, z20 2.49, zc n/a, resid-z n/a [quiet], 1d -1.23%, GSR<75 (extreme low); |z20|=2.49
- comex_silver [COMMODITIES]: last 57.18, z20 -1.64, zc 1.01, resid-z 0.59 [quiet], 1d 2.93%, |z20|=1.64
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.824 vs comex_silver, historically leads by 4d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.512 vs gold_silver_ratio, historically leads by 3d
- Source: Silver futures rise to ₹2.08 lakh per kg — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/gold/silver-futures-rise-to-208-lakh-per-kg/article71586939.ece
- Source: Silver futures plunge 4% on MCX ahead of US CPI; rising oil adds pressure — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/commodities/silver-futures-plunge-4-on-mcx-ahead-of-us-cpi-rising-oil-adds-pressure/articleshow/134946048.cms
- Source: SPOT SILVER FALLS NEARLY 3% TO $57.58/OZ — DeItaone, 2026-10-14. https://t.me/walter_bloomberg/37071
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.9] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1650.00, z20 4.59, zc 2.75, resid-z 1.78 [unexplained], 1d 4.75%, |z20|=4.59
- dyn_tataelxsi_ns [EQUITIES]: last 3700.00, z20 3.51, zc 0.85, resid-z -0.11 [quiet], 1d 2.12%, |z20|=3.51
- nifty_it [INDICES]: last 30719.80, z20 3.38, zc 1.08, resid-z -0.14 [quiet], 1d 1.82%, |z20|=3.38
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.502 via nifty_it, z 1.06, reacted); nifty_fmcg (rho 0.5 via dyn_tataelxsi_ns, z -0.45, quiet); nifty_50 (rho 0.491 via dyn_techm_ns, z 0.37, quiet); dyn_tatatech_ns (rho 0.479 via nifty_it, z 1.53, reacted); midcap_largecap_ratio (rho -0.418 via dyn_techm_ns, z -3.43, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.5 vs dyn_tataelxsi_ns
- **India receivers**: dyn_justdial_bo (rho 0.502, z 1.06); nifty_fmcg (rho 0.5, z -0.45); nifty_50 (rho 0.491, z 0.37); dyn_tatatech_ns (rho 0.479, z 1.53)
- Source: Q2 Results Highlights, 15 Oct: Wipro PAT rises 9% year-on-year; Tech Mahindra profit jumps 32.7%; Nestlé shares tank after Q2 results; IIFL Finance, IRFC, Polycab, KVB and HDFC AMC report higher PAT; Heritage Foods posts decline — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/q2-results-highlights-wipro-nestle-india-tech-mahindra-jio-financial-persistent-systems-irfc-polycab-hdfc-amc-tata-communication-results-groww-tata-tech-leela-emmvee-15-october-2026/article71586591.ece
- Source: Q2 results: Tech Mahindra dividend, bonus shares - Double delight for 7 lakh investors | Payout, ratio, record date — Mint Markets, 2026-10-15. https://www.livemint.com/market/stock-market-news/q2-results-tech-mahindra-dividend-bonus-shares-double-delight-for-7-lakh-investors-payout-ratio-record-date-11792060760425.html
- Source: Tech Mahindra announces 1:1 bonus issue, Rs 15 interim dividend; check record date — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/stocks/earnings/tech-mahindra-announces-11-bonus-issue-rs-15-interim-dividend-check-record-date/articleshow/134968892.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 7.65] usd_inr ↓
- usd_inr [FX]: last 95.04, z20 -2.65, zc -0.53, resid-z -0.28 [quiet], 1d -0.25%, 20d range extreme; |z20|=2.65
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.369 via usd_inr, z 2.27, reacted); dyn_idbi_ns (rho -0.358 via usd_inr, z -0.4, quiet)
- **India receivers**: dyn_karurvysya_ns (rho -0.369, z 2.27); dyn_idbi_ns (rho -0.358, z -0.4)
- Source: Rupee extends winning streak as dollar, oil ease and stocks rally — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/forex/rupee-extends-winning-streak-as-dollar-oil-ease-and-stocks-rally/articleshow/134965552.cms
- Source: Sensex today | Stock Market Highlights: Sensex jumps over 1,500 points, Nifty nears 23,000; rupee extends gains — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/sensex-nifty50-stock-market-highlights-15-october-2026/article71583334.ece
- Source: Rupee extends winning streak for 4th straight session as US dollar, oil ease and stocks rally — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-extends-winning-streak-for-4th-straight-session-as-us-dollar-oil-ease-and-stocks-rally/article71587583.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.43] midcap_largecap_ratio ↓
- midcap_largecap_ratio [DERIVED]: last 2.57, z20 -3.43, zc n/a, resid-z n/a [quiet], 1d -1.97%, break below 100-DMA; |z20|=3.43
- **Mechanism**: midcap_largecap_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.523 via midcap_largecap_ratio, z -0.72, quiet); dyn_techm_ns (rho -0.418 via midcap_largecap_ratio, z 4.59, reacted); dyn_cartrade_ns (rho 0.375 via midcap_largecap_ratio, z -0.01, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.523 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.523, z -0.72); dyn_techm_ns (rho -0.418, z 4.59); dyn_cartrade_ns (rho 0.375, z -0.01)
- Historical analogues: 2025-12-31 (d=0.0), 2025-07-03 (d=0.11), 2025-07-23 (d=0.2)

### [AMBER 5.51] cross-asset · 3 series ↓
- dyn_nvda [EQUITIES]: last 217.07, z20 -2.19, zc -0.85, resid-z -0.92 [quiet], 1d -1.91%, |z20|=2.19
- russell_2000 [INDICES]: last 2752.92, z20 -1.90, zc 0.54, resid-z 1.64 [unexplained], 1d 0.86%, |z20|=1.90
- nasdaq_100 [INDICES]: last 29744.24, z20 -1.76, zc -0.57, resid-z -0.76 [quiet], 1d -0.69%, |z20|=1.76
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.595 vs dyn_nvda, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.56 vs nasdaq_100, historically leads by 2d
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.54 vs russell_2000, historically leads by 1d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.563 vs nasdaq_100
- Watch next: dax (co-move) — not yet - watch; rho 0.526 vs russell_2000
- Source: US stocks: Nasdaq nears one-month low as AI stocks slide on debt concerns — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-nasdaq-nears-one-month-low-as-ai-stocks-slide-on-debt-concerns/articleshow/134969761.cms
- Source: Micron, Nvidia and other chip stocks face renewed pressure as AI fears swell — MarketWatch Top, 2026-10-15. https://www.marketwatch.com/story/micron-nvidia-and-other-chip-stocks-face-renewed-pressure-as-ai-fears-swell-4e0dc989?mod=mw_rss_topstories
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq nears one-month low as debt worries deepen AI stock selloff — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-rate-yield-earnings-season-anthropic-coreweave-oracle-rocket-lab-ai-chip-stock-price-news-15th-october-2026/liveblog/134967916.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.22), 2025-04-29 (d=0.35)

### [RED 5.08] dyn_301077_sz ↓
- dyn_301077_sz [EQUITIES]: last 19.80, z20 -3.08, zc -0.97, resid-z -0.36 [quiet], 1d -2.80%, |z20|=3.08; 1y-pct=5
- **Mechanism**: dyn_301077_sz ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [AMBER 4.98] crypto · 2 series ↓
- eth_usd [CRYPTO]: last 2396.00, z20 -2.15, zc -0.23, resid-z -0.94 [quiet], 1d -0.92%, |z20|=2.15
- btc_usd [CRYPTO]: last 81816.18, z20 -1.55, zc 0.15, resid-z -0.39 [quiet], 1d 0.31%, |z20|=1.55
- **Mechanism**: crypto · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-04-10 (z-distance 0.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.564 vs eth_usd, historically leads by 1d
- Source: Bitcoin Slides as Wall Street Risk Pullback Tests Bullish Turn — Mint Markets, 2026-10-14. https://www.livemint.com/market/bitcoin-slides-as-wall-street-risk-pullback-tests-bullish-turn-11792003663551.html
- Source: Bitcoin hovers near $83K as Asian stock sell-off triggers over $800 million in crypto liquidations — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-hovers-near-83k-as-asian-stock-sell-off-triggers-over-800-million-in-crypto-liquidations/articleshow/134939967.cms
- Source: MICHAEL SAYLOR PREDICTS BITCOIN WILL SURGE BACK ABOVE $100,000 Strategy ($MSTR ) Chairman Michael Saylor says Bitcoin's bear market is over, predicting a return above $100,000. Key takeaways: * Bitcoin: Trading near $83,000. * Bottom: Saylor believes BTC bottomed just below $60,000. * Forecast: Expe — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37031
- Historical analogues: 2025-04-10 (d=0.08), 2025-11-05 (d=0.09), 2025-06-20 (d=0.19)

### [RED 4.92] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3706.48, z20 -2.92, zc -2.24, resid-z -1.00 [moved], 1d -1.61%, |z20|=2.92; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.391 via shanghai_comp, z -1.48, reacted)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.638 vs shanghai_comp, historically leads by 2d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.509 vs shanghai_comp, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.391, z -1.48)
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

## Watchlist (below surfacing floor)
dyn_dell ↓ (4.4), kospi ↓ (4.32), rates · 4 series ↑ (4.29), dyn_bac ↓ (4.18), dow_jones ↑ (3.7), usd_cny ↓ (3.63), soybeans ↓ (3.59), natgas ↑ (3.58), dyn_rs ↑ (3.53), eur_usd ↓ (3.09), dyn_4417_t ↑ (3.01), dyn_tech ↑ (2.98)

## India macro
- nifty_50: 22997.3496 (1d 1.66%, z20 0.37, flag none)
- nifty_midcap_100: 59192.0000 (1d -0.35%, z20 -0.72, flag none)
- usd_inr: 95.0450 (1d -0.25%, z20 -2.65, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5739 (1d -1.97%, z20 -3.43, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 107.1 — "Jio Platforms to Reliance Power: India’s 10 biggest IPOs ranked"
- INOXINDIA.NS (INOX INDIA LIMITED) score 102.7 — "Jio Platforms to Reliance Power: India’s 10 biggest IPOs ranked"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 101.5 — "Jio Platforms to Reliance Power: India’s 10 biggest IPOs ranked"
- INDIANB.NS (INDIAN BANK) score 96.0 — "JAPAN’S NIKKEI PLUNGES 3.5% AS FED RATE HIKE FEARS GROW Japanese stocks tumbled after hott"
- BAC (Bank of America Corporation) score 90.8 — "JAPAN’S NIKKEI PLUNGES 3.5% AS FED RATE HIKE FEARS GROW Japanese stocks tumbled after hott"
- HDB (HDFC Bank Limited) score 83.7 — "JAPAN’S NIKKEI PLUNGES 3.5% AS FED RATE HIKE FEARS GROW Japanese stocks tumbled after hott"
- IDBI.NS (IDBI BANK LIMITED) score 79.8 — "JAPAN’S NIKKEI PLUNGES 3.5% AS FED RATE HIKE FEARS GROW Japanese stocks tumbled after hott"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 79.8 — "JAPAN’S NIKKEI PLUNGES 3.5% AS FED RATE HIKE FEARS GROW Japanese stocks tumbled after hott"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 79.8 — "JAPAN’S NIKKEI PLUNGES 3.5% AS FED RATE HIKE FEARS GROW Japanese stocks tumbled after hott"
- TECHM.NS (TECH MAHINDRA LIMITED) score 72.8 — "Q2 Results Live Updates: Tech Mahindra posts 33% YoY profit jump. Rs 15/share dividend dec"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 71.4 — "Q2 Results Live Updates: Tech Mahindra posts 33% YoY profit jump. Rs 15/share dividend dec"
- TECH (Bio-Techne Corp) score 71.4 — "Q2 Results Live Updates: Tech Mahindra posts 33% YoY profit jump. Rs 15/share dividend dec"
- OHI (Omega Healthcare Investors, In) score 58.5 — "Reliance-backed Jio Platforms IPO RHP: 10 key risks investors can't afford to miss out bef"
- COIN (Coinbase Global, Inc.) score 58.3 — "Global Market: European shares fall as global tech selloff, rate fears weigh on sentiment"
- TGT (Target Corporation) score 42.8 — "70% YTD returns! Axis Capital sees 30% more upside in this renewable power stock; do you o"
- CHKP (Check Point Software Technolog) score 41.6 — "Newly listed stock has 30% upside potential! JM Financial issues buy call; Check target pr"
- BOND (PIMCO Active Bond Exchange-Tra) score 37.3 — "Sharp and immediate fall! Yes Bank share price crash 10% after SC ruling on  ₹8,415 crore "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.0 — "Ukraine to Resume Russian Oil Refinery Strikes After Failed Energy Ceasefire"
- SEPN (Septerna, Inc.) score 28.4 — "India’s ethanol receipts hit 987 crore litres by September, maize leads supply"
- RS (Reliance, Inc.) score 27.8 — "Big surge! Early Diwali for Sensex, Nifty as stock market skyrockets on Reliance Jio IPO, "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.8 — "ICICI Bank, HDFC Bank, SBI, Axis Bank: Which banking stock to buy ahead of Q2 results - Wh"
- LTH (Life Time Group Holdings, Inc.) score 24.8 — "Global Market: European shares fall as global tech selloff, rate fears weigh on sentiment"
- 301077.SZ (CHINASTARS) score 23.1 — "China indicates rare earths will keep flowing to EU, regardless of U.S. trade deal expirat"
- JIOFIN.BO (Jio Financial Services Limited) score 21.6 — "Newly listed stock has 30% upside potential! JM Financial issues buy call; Check target pr"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.3 — "Tata Elxsi vs Tata Tech: Which Tata Group's stock wins Q2 results report card? Profit, rev"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 20.3 — "Tata Elxsi vs Tata Tech: Which Tata Group's stock wins Q2 results report card? Profit, rev"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.6 — "Bonus shares, stock split, dividend: Last day to buy as these shares trade ex-date today |"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 13.2 — "Q2 Results Highlights, 15 Oct: Wipro PAT rises 9% year-on-year; Tech Mahindra profit jumps"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.3 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Performance"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.0 — "Q2 Results Highlights, 15 Oct: Wipro PAT rises 9% year-on-year; Tech Mahindra profit jumps"
- VT (Vanguard Total World Stock Ind) score 10.9 — "U.S. Wants World Bank to Drop Ban on Upstream Oil and Gas Funding"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.4 — "Sensex on fire! 1,500-point rally puts bulls back in the driver’s seat. What just happened"
- GS (Goldman Sachs Group, Inc. (The) score 7.5 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- NVDA (NVIDIA Corporation) score 6.6 — "Micron, Nvidia and other chip stocks face renewed pressure as AI fears swell"
- JEF (Jefferies Financial Group Inc.) score 6.4 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- META (Meta) score 5.9 — "IT stocks lift Nifty as Adani, Metal stocks slide amid global sellof"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.6 — "Bajaj Broking rolls out algorithm trading platform for retail investors"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.2 — "Piero Cipollone: Interview with Corriere della Sera"
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