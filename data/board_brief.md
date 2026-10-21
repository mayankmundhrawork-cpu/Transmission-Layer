# Transmission Layer — board brief · 2026-10-21 09:20Z

data as of **2026-10-21** · 97 series · 9 red / 39 amber · 8 events surfaced (34 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.826, 13d in regime; vol-pct 0.736, breadth-off 0.917, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.2, corr60 -0.37, contra nifty_50 corr20=0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.82, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.13, corr60 0.1, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.02, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.2, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.49, corr60 0.22, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0004481066939820977)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.501** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=1985) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.11] commodities · 2 series ↑
- brent [COMMODITIES]: last 110.10, z20 1.96, zc 0.61, resid-z -0.41 [quiet], 1d 1.20%, |z20|=1.96; 1y-pct=96
- wti [COMMODITIES]: last 99.11, z20 1.27, zc -1.09, resid-z -0.92 [quiet], 1d -2.63%, 1-session move -2.63% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.588 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.592 vs brent
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.57 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.547 vs brent
- Source: Indian Oil to trim West Asia oil imports under annual deals amid Iran war — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/markets/commodities/indian-oil-to-trim-west-asia-oil-imports-under-annual-deals-amid-iran-war/article71606857.ece
- Source: Rubio’s India visit puts energy security in focus as crude costs rise amid global disruptions: Kotak Neo’s Banerjee — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/markets/commodities/rubios-india-visit-puts-energy-security-in-focus-as-crude-costs-rise-amid-global-disruptions-kotak-neos-banerjee/article71606543.ece
- Source: G-sec yield hits over 3-year high of 7.44% as oil back to $110 a barrel — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/markets/g-sec-yields-hits-over-3-year-high-of-744-as-oil-back-to-110-a-barrel/article71606338.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 5.8] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 57151.25, z20 -2.13, zc -1.05, resid-z -0.66 [quiet], 1d -2.28%, |z20|=2.13
- india_vix [INDICES]: last 15.92, z20 1.73, zc 0.85, resid-z n/a [quiet], 1d 7.79%, |z20|=1.73
- dyn_policybzr_ns [EQUITIES]: last 1008.90, z20 -0.52, zc -1.55, resid-z 0.14 [moved], 1d -2.52%, 1y-pct=2
- nifty_50 [INDICES]: last 22660.55, z20 -0.46, zc -1.12, resid-z -1.28 [quiet], 1d -1.00%, 1y-pct=4
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.64 via nifty_50, z -2.23, reacted); dyn_jiofin_bo (rho 0.628 via nifty_midcap_100, z -1.33, reacted); dyn_bajfinance_ns (rho -0.627 via india_vix, z -2.27, reacted); nifty_metal (rho 0.624 via nifty_midcap_100, z -1.61, reacted); dyn_indusindbk_bo (rho -0.551 via india_vix, z -1.63, reacted)
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.509 vs nifty_50, historically leads by 2d
- **India receivers**: nifty_fmcg (rho 0.64, z -2.23); dyn_jiofin_bo (rho 0.628, z -1.33); dyn_bajfinance_ns (rho -0.627, z -2.27); nifty_metal (rho 0.624, z -1.61)
- Source: Sensex today | Stock Market Live: Sensex down 550 pts, Nifty below 22,700; Eternal, Bajaj Fin lead losers — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-21st-october-2026/article71604730.ece
- Source: Gap-up gone: Nifty reverses early gains, 322 stocks hit 52-week lows — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/markets/gap-up-gone-nifty-reverses-early-gains-322-stocks-hit-52-week-lows/article71606718.ece
- Source: Wibbly wobbly Wednesday for stock market! Sensex, Nifty first soars, and then crashes from day's high - Fall reasons? — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/wibbly-wobbly-wednesday-for-stock-market-sensex-nifty-first-soars-and-then-crashes-from-days-high-fall-reasons-11792566806183.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 5.69] gbp_usd ↑
- gbp_usd [FX]: last 1.34, z20 3.69, zc 1.79, resid-z 2.03 [unexplained], 1d 0.64%, |z20|=3.69
- **Mechanism**: gbp_usd ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.817 vs gbp_usd
- Source: Sterling hits 17-month high against euro — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-hits-17-month-high-against-euro/articleshow/135048275.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-03 (d=0.02), 2025-09-15 (d=0.02)

### [RED 5.28] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 745.00, z20 3.28, zc 0.82, resid-z 1.21 [quiet], 1d 1.70%, |z20|=3.28
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.513 via dyn_justdial_bo, z 2.7, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.21, reacted); nifty_50 (rho 0.454 via dyn_justdial_bo, z -0.46, quiet); dyn_tataelxsi_ns (rho 0.396 via dyn_justdial_bo, z 2.16, reacted); nifty_midcap_100 (rho 0.351 via dyn_justdial_bo, z -2.13, reacted)
- **India receivers**: nifty_it (rho 0.513, z 2.7); dyn_techm_ns (rho 0.505, z 3.21); nifty_50 (rho 0.454, z -0.46); dyn_tataelxsi_ns (rho 0.396, z 2.16)
- Source: Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss by Anand Rathi's expert — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-short-term-just-dial-bse-orient-hotels-target-price-stop-loss-by-anand-rathis-expert-11792400725179.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [RED 5.15] dyn_wit ↑
- dyn_wit [EQUITIES]: last 2.06, z20 3.15, zc 1.69, resid-z -0.06 [moved], 1d 6.48%, |z20|=3.15
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: IT stocks on fire, rally up to 15% today; check performance of TCS, L&T Technology, Wipro, Infosys | Jefferies bullish — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/it-stocks-on-fire-rally-up-to-15-today-check-performance-of-tcs-l-t-technology-wipro-infosys-jefferies-bulli-11792559488325.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [RED 4.81] dow_jones ↑
- dow_jones [INDICES]: last 52500.12, z20 2.81, zc 1.38, resid-z 1.85 [unexplained], 1d 1.03%, |z20|=2.81
- **Mechanism**: dow_jones ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.901 vs dow_jones
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.688 vs dow_jones, historically leads by 1d
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.586 vs dow_jones, historically leads by 1d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.779 vs dow_jones
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.553 vs dow_jones, historically leads by 2d
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks open lower as AI stocks decline, oil prices rise — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: S&P 500 Healthcare hits record high, Dow soars over 500 points — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Dow leads Wall Street higher, investors focus on healthcare stocks — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-28 (d=0.1), 2025-08-22 (d=0.11)

### [RED 4.52] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1826.00, z20 3.21, zc -0.20, resid-z 0.71 [quiet], 1d 2.64%, |z20|=3.21; 1y-pct=100
- nifty_it [INDICES]: last 32219.15, z20 2.70, zc -0.63, resid-z 0.27 [quiet], 1d 2.23%, |z20|=2.70
- dyn_tataelxsi_ns [EQUITIES]: last 3818.60, z20 2.16, zc -0.61, resid-z 0.38 [quiet], 1d 0.75%, |z20|=2.16
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.521 via dyn_tataelxsi_ns, z -0.46, quiet); dyn_justdial_bo (rho 0.513 via nifty_it, z 3.28, reacted); nifty_fmcg (rho 0.489 via dyn_tataelxsi_ns, z -2.23, reacted); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -3.41, reacted); dyn_tatatech_ns (rho 0.403 via nifty_it, z -1.27, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.514 vs nifty_it
- **India receivers**: nifty_50 (rho 0.521, z -0.46); dyn_justdial_bo (rho 0.513, z 3.28); nifty_fmcg (rho 0.489, z -2.23); midcap_largecap_ratio (rho -0.439, z -3.41)
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [AMBER 4.31] dyn_meta ↓
- dyn_meta [EQUITIES]: last 694.44, z20 -2.31, zc -0.62, resid-z -0.37 [quiet], 1d -1.56%, |z20|=2.31
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta's AI spending, Muse assistant adoption in focus for quarterly results — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/metas-ai-spending-muse-assistant-adoption-in-focus-for-quarterly-results/articleshow/135068976.cms
- Source: Meta’s AI spending and Muse adoption set to test Zuckerberg’s strategy — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/metas-ai-spending-muse-assistant-adoption-in-focus-for-quarterly-results/articleshow/135068976.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

## Watchlist (below surfacing floor)
dyn_bajfinance_ns ↓ (4.27), dyn_4417_t ↑ (4.1), dyn_rs ↑ (4.1), gold_silver_ratio ↑ (4.08), usd_inr ↓ (4.06), dyn_dell ↓ (4.05), nasdaq_100 ↓ (3.98), natgas ↓ (3.9), commodities · 3 series ↓ (3.81), dyn_tech ↑ (3.43), midcap_largecap_ratio ↓ (3.41), tips_10y_real ↓ (3.36)

## India macro
- nifty_50: 22660.5508 (1d -1.00%, z20 -0.46, flag amber)
- nifty_midcap_100: 57151.2500 (1d -2.28%, z20 -2.13, flag amber)
- usd_inr: 94.6000 (1d -0.41%, z20 -2.06, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5221 (1d -1.29%, z20 -3.41, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 89.8 — "Indian stock markets likely to open marginally positive on global cues"
- INDIANB.NS (INDIAN BANK) score 85.2 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.1 — "Indian stock markets likely to open marginally positive on global cues"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.7 — "Indian stock markets likely to open marginally positive on global cues"
- BAC (Bank of America Corporation) score 73.6 — "How Bad Would It Get If China Blocks Rare Earths to America?"
- HDB (HDFC Bank Limited) score 68.0 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- IDBI.NS (IDBI BANK LIMITED) score 65.4 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.4 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 65.4 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.7 — "Car buyers are demanding lower prices and better tech. Automakers must deliver both"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 56.1 — "Car buyers are demanding lower prices and better tech. Automakers must deliver both"
- TECH (Bio-Techne Corp) score 56.1 — "Car buyers are demanding lower prices and better tech. Automakers must deliver both"
- OHI (Omega Healthcare Investors, In) score 51.2 — "ETMarkets Smart Talk | Investors want more than trading apps; they want a partner in their"
- COIN (Coinbase Global, Inc.) score 50.2 — "Indian stock markets likely to open marginally positive on global cues"
- CHKP (Check Point Software Technolog) score 41.4 — "Paras Healthcare IPO opens for subscription: Check GMP, price band and key details"
- TGT (Target Corporation) score 35.9 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- BOND (PIMCO Active Bond Exchange-Tra) score 34.3 — "Indian bonds sell off on oil shock ahead of RBI policy minutes"
- RS (Reliance, Inc.) score 29.1 — "Top stocks to watch today: Eternal, Reliance Industries, IREDA, RailTel shares in focus on"
- 301077.SZ (CHINASTARS) score 23.5 — "How Bad Would It Get If China Blocks Rare Earths to America?"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.8 — "ETMarkets Smart Talk| India’s next wealth creators may be hidden in specialised manufactur"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 22.6 — "Top stocks to buy: Experts bet on SBI, Bank of Baroda, Meesho, CG Power, and 2 others - Ta"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.6 — "Bajaj Auto Share Price Live Updates: Bajaj Auto's Price Movement Signals Concern"
- LTH (Life Time Group Holdings, Inc.) score 17.5 — "Jio Platforms IPO Day 1 Live Updates: Issue subscribed 1.27 times, QIB portion 3.86 times"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.4 — "Bajaj Finance shares fall 3% after Q2 results. What Jefferies, Nomura, other brokerages no"
- JIOFIN.BO (Jio Financial Services Limited) score 14.2 — "L&T Tech Services shares surge 15% after Q2 2026 results - Should investors buy, sell, or "
- BZ=F (Brent Crude Oil Last Day Finan) score 13.6 — "Paras Healthcare IPO: Can higher occupancy deliver lasting profit?"
- SEPN (Septerna, Inc.) score 13.0 — "GOLDMAN SACHS: U.S. GDP HOLDS STRONG DESPITE HOUSING SLUMP U.S. housing starts plunged 5.2"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.0 — "RIL's stock climbs 2% as Jio Platforms IPO achieves full subscription in just 100 minutes"
- GS (Goldman Sachs Group, Inc. (The) score 11.6 — "Copper supply crunch deepens as new mines take over 16 years to develop: Goldman Sachs"
- META (Meta) score 10.7 — "Hindustan Zinc’s Q2 earnings glow on lower costs, higher metal prices"
- JEF (Jefferies Financial Group Inc.) score 9.6 — "UltraTech Cement shares jump 3% as brokerages revise target prices after Q2 results. What "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.4 — "Tata Steel Share Price Live Updates: Tata Steel's Stock Performance"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.4 — "Tata Steel Share Price Live Updates: Tata Steel's Stock Performance"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.6 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Trading Status"
- VT (Vanguard Total World Stock Ind) score 6.5 — "In charts: How one of the world's biggest economies got trapped by debt"
- NVDA (NVIDIA Corporation) score 4.8 — "DEEPSEEK AND HUAWEI ARE COLLABORATING ON NEW AI CHIP DESIGNS TO CHALLENGE NVIDIA - THE IN "
- WIT (Wipro Limited) score 3.7 — "IT stocks on fire, rally up to 15% today; check performance of TCS, L&T Technology, Wipro,"
- DELL (Dell Technologies Inc.) score 1.7 — "Super Micro’s stock soars after surprise update — with Dell and HPE shares joining the ral"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.6 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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