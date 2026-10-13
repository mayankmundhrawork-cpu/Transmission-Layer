# Transmission Layer — board brief · 2026-10-13 19:14Z

data as of **2026-10-13** · 97 series · 7 red / 34 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.678, 7d in regime; vol-pct 0.649, breadth-off 0.706, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.34, corr60 -0.4, contra nifty_50 corr20=0.21, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.27, corr60 0.23, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.03, corr60 0.14, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.08, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.29, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.62, corr60 0.15, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.493** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2126) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.52] usd_inr ↓
- usd_inr [FX]: last 95.27, z20 -2.52, zc -1.00, resid-z -0.97 [quiet], 1d -0.51%, 20d range extreme; |z20|=2.52
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.407 via usd_inr, z -0.63, quiet); dyn_karurvysya_ns (rho -0.375 via usd_inr, z 3.6, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.407, z -0.63); dyn_karurvysya_ns (rho -0.375, z 3.6)
- Source: Rupee gains 145 paise in two trading sessions, but disquiet sets in forex market — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/money-and-banking/rupee-gains-145-paise-in-two-trading-sessions-but-disquiet-sets-in-forex-market/article71579835.ece
- Source: Sitharaman’s LTCG, STT remarks lift market sentiment; rupee gains for third straight session — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/sitharamans-ltcg-stt-remarks-lift-market-sentiment-rupee-gains-for-third-straight-session/article71579794.ece
- Source: Weekly Rupee View: Recovery might be short-lived — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/portfolio/technical-analysis/weekly-rupee-viewrecovery-might-be-short-lived/article71579313.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.59] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 29830.10, z20 2.76, zc 3.54, resid-z 2.49 [unexplained], 1d 5.22%, |z20|=2.76
- dyn_tataelxsi_ns [EQUITIES]: last 3426.70, z20 2.07, zc 2.62, resid-z 2.03 [unexplained], 1d 5.21%, |z20|=2.07
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-31 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho 0.878 via nifty_it, z 0.42, quiet); nifty_50 (rho 0.591 via dyn_tataelxsi_ns, z -0.5, quiet); dyn_justdial_bo (rho 0.525 via nifty_it, z 0.7, quiet); dyn_tatatech_ns (rho 0.522 via nifty_it, z 1.48, reacted); nifty_fmcg (rho 0.508 via dyn_tataelxsi_ns, z -0.54, quiet)
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.878 vs nifty_it, historically leads by 3d
- Watch next: dyn_justdial_bo (co-move) — not yet - watch; rho 0.525 vs nifty_it, historically leads by 4d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.591 vs dyn_tataelxsi_ns
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.508 vs dyn_tataelxsi_ns
- **India receivers**: dyn_techm_ns (rho 0.878, z 0.42); nifty_50 (rho 0.591, z -0.5); dyn_justdial_bo (rho 0.525, z 0.7); dyn_tatatech_ns (rho 0.522, z 1.48)
- Source: Q2 Results Today Highlights: Q2 Results Today Live: Tata Elxsi, ICICI Pru Life, Hero Motors shares trade mixed; PNB Gilts jumps 8% — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/q2-results-today-highlights-hero-motors-icici-pru-tata-elxsi-ss-retail-anand-rathi-share-company-results-13-october-2026/article71577900.ece
- Source: Tata Elxsi Q2 Results: Profit rises 10% YoY to Rs 170 crore; revenue grows 15% — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/stocks/earnings/tata-elxsi-q2-results-profit-rises-10-yoy-to-rs-170-crore-revenue-grows-15/articleshow/134918419.cms
- Source: Q2 Results Today Live: Q2 Results Today Live: Tata Elxsi, ICICI Pru Life, Hero Motors shares trade mixed; PNB Gilts jumps 8% — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-hero-motors-icici-pru-tata-elxsi-ss-retail-anand-rathi-share-company-results-13-october-2026/article71577900.ece
- Historical analogues: 2025-07-31 (d=0.34), 2025-01-30 (d=0.36), 2025-07-09 (d=0.4)

### [RED 4.83] kospi ↓
- kospi [INDICES]: last 6005.98, z20 -4.83, zc -3.10, resid-z -0.87 [moved], 1d -5.92%, |z20|=4.83
- **Mechanism**: kospi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.479 via kospi, z 2.76, reacted); dyn_bajfinance_ns (rho 0.467 via kospi, z -0.09, quiet); dyn_techm_ns (rho -0.412 via kospi, z 0.42, quiet)
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.943 vs kospi, historically leads by 2d
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.841 vs kospi, historically leads by 2d
- **India receivers**: nifty_it (rho -0.479, z 2.76); dyn_bajfinance_ns (rho 0.467, z -0.09); dyn_techm_ns (rho -0.412, z 0.42)
- Historical analogues: 2026-07-10 (d=0.0), 2026-04-02 (d=0.01), 2025-04-01 (d=0.04)

### [RED 4.77] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 70.36, z20 1.77, zc n/a, resid-z n/a [quiet], 1d 0.97%, GSR<75 (extreme low); |z20|=1.77
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.376 via gold_silver_ratio, z -0.95, quiet)
- **India receivers**: midcap_largecap_ratio (rho -0.376, z -0.95)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [AMBER 4.62] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.60, z20 0.95, zc -1.74, resid-z -2.34 [unexplained], 1d -1.23%, 1y-pct=97
- tips_10y_real [RATES]: last 2.87, z20 0.73, zc -0.90, resid-z -1.52 [unexplained], 1d -1.71%, 1y-pct=96
- ust_10y [RATES]: last 5.22, z20 0.72, zc -1.12, resid-z -1.95 [unexplained], 1d -1.14%, 1y-pct=96
- dyn_bond [EQUITIES]: last 87.10, z20 -0.52, zc 0.44, resid-z 0.58 [quiet], 1d 0.16%, 1y-pct=4
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.651 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 1d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.51 vs ust_10y, historically leads by 4d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.54 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.523 vs ust_10y
- Source: India's benchmark bond breaks 4-day falling streak as value investors return — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/bonds/indias-benchmark-bond-breaks-4-day-falling-streak-as-value-investors-return/articleshow/134918791.cms
- Source: JPMorgan posts rare profit miss as dealmaking, bond trading lose momentum — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/us-stocks/news/jpmorgan-posts-rare-profit-miss-as-dealmaking-bond-trading-lose-momentum/articleshow/134918192.cms
- Source: FED'S WALLER: SURGING U.S. BOND YIELDS DRIVEN BY GROWTH, NOT INFLATION Fed Governor Christopher Waller says strong economic growth and AI investment are pushing Treasury yields higher, while inflation expectations remain anchored. He warns that weaker safe-haven demand for U.S. debt could be adding  — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/36975
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 4.28] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -4.28, zc -1.44, resid-z -1.99 [unexplained], 1d -0.15%, |z20|=4.28; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.366 via usd_cny, z -0.69, quiet); dyn_bajfinance_ns (rho -0.354 via usd_cny, z -0.09, quiet)
- **India receivers**: dyn_policybzr_ns (rho -0.366, z -0.69); dyn_bajfinance_ns (rho -0.354, z -0.09)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.1] natgas ↑
- natgas [COMMODITIES]: last 3.31, z20 2.10, zc 1.40, resid-z 1.89 [unexplained], 1d 4.52%, |z20|=2.10
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.1 vs natgas, historically leads by 4d
- Source: China’s $3 Billion Qatar LNG Deal Raises an Awkward Question — OilPrice, 2026-10-13. https://oilprice.com/Energy/Natural-Gas/Chinas-3-Billion-Qatar-LNG-Deal-Raises-an-Awkward-Question.html
- Source: Super El Niño Could Ease Asia’s LNG Supply Concerns — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Super-El-Nio-Could-Ease-Asias-LNG-Supply-Concerns.html
- Source: Pakistan Faces $1 Billion LNG Bill This Winter — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Pakistan-Faces-1-Billion-LNG-Bill-This-Winter.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 3.91] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 6720.00, z20 1.91, zc 0.09, resid-z 2.45 [unexplained], 1d 1.05%, 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top stocks to buy for long term: Bharti Airtel, Kotak Bank, Eternal among 9 shares experts suggest - Check target price — Mint Markets, 2026-10-13. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-long-term-bharti-airtel-kotak-bank-eternal-among-9-stocks-experts-suggest-check-target-price-11791890055735.html
- Source: Park Medi World shares: Hospital stock dips 15% in a month — Will the stock rebound? Experts show road map to investors — Mint Markets, 2026-10-13. https://www.livemint.com/market/stock-market-news/park-medi-world-shares-hospital-stock-dips-15-in-a-month-will-the-stock-rebound-experts-show-road-map-to-investors-11791884861855.html
- Source: Up 75% in 6 months! India Glycols shares surge 14% today - Should you buy? Experts decode — Mint Markets, 2026-10-13. https://www.livemint.com/market/stock-market-news/up-75-in-6-months-india-glycols-shares-surge-14-today-should-you-buy-experts-decode-11791880814133.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
shanghai_comp ↓ (3.71), dyn_karurvysya_ns ↑ (3.6), dyn_rs ↑ (3.53), dyn_meta ↑ (3.5), indices · 2 series ↓ (3.37), sp500 ↑ (3.27), dyn_policybzr_ns ↓ (2.69), commodities · 2 series ↓ (2.61), dyn_cartrade_ns ↑ (2.61), dyn_jiofin_bo ↓ (2.58), dyn_tech ↑ (2.46), indices · 2 series ↓ (2.4)

## India macro
- nifty_50: 22721.9492 (1d 1.60%, z20 -0.50, flag amber)
- nifty_midcap_100: 59458.4492 (1d 1.04%, z20 -0.65, flag none)
- usd_inr: 95.2700 (1d -0.51%, z20 -2.52, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6168 (1d -0.56%, z20 -0.95, flag none)
- Next India prints: NSDL FPI flows T-0d · India WPI T-1d · India trade / CAD data T-2d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 81.6 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.8 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.1 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- INDIANB.NS (INDIAN BANK) score 71.2 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- BAC (Bank of America Corporation) score 64.6 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- HDB (HDFC Bank Limited) score 58.6 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- IDBI.NS (IDBI BANK LIMITED) score 56.9 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.9 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.9 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.1 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- TECH (Bio-Techne Corp) score 54.1 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- COIN (Coinbase Global, Inc.) score 50.9 — "Global Market: European shares rise as lower oil prices lift sentiment; tech stocks slide"
- OHI (Omega Healthcare Investors, In) score 46.1 — "BOFA: U.S. TREASURY YIELDS MAY NEED TO HIT 6% TO DERAIL STOCK RALLY Bank of America's late"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.9 — "BOFA: U.S. TREASURY YIELDS MAY NEED TO HIT 6% TO DERAIL STOCK RALLY Bank of America's late"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.9 — "Trump Defends Russian Diesel Deal as Energy Ceasefire Claims Unravel"
- TGT (Target Corporation) score 31.4 — "Top stocks to buy in F&O segment: M&M, Shree Cements, Cholamandalam Investment by Jay Thak"
- LTH (Life Time Group Holdings, Inc.) score 29.0 — "Global Market: European shares rise as lower oil prices lift sentiment; tech stocks slide"
- CHKP (Check Point Software Technolog) score 28.0 — "Top stocks to buy in F&O segment: M&M, Shree Cements, Cholamandalam Investment by Jay Thak"
- 301077.SZ (CHINASTARS) score 21.1 — "China sentences 3 more Myanmar crime bosses to death in scam centre crackdown"
- SEPN (Septerna, Inc.) score 19.0 — "Minutes of the Board's discount rate meetings on August 17, September 9, and September 16,"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.9 — "RBL Bank share price crashes 8% after Q2 results - Should investors buy, sell, or hold the"
- JIOFIN.BO (Jio Financial Services Limited) score 14.1 — "70% women control portfolios, but none received structured financial training, study finds"
- VT (Vanguard Total World Stock Ind) score 10.9 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.0 — "Tata Elxsi Q2 Results: Profit rises 10% YoY to Rs 170 crore; revenue grows 15%"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.0 — "Tata Elxsi Q2 Results: Profit rises 10% YoY to Rs 170 crore; revenue grows 15%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.8 — "Stocks to Watch, Oct 12: Lenskart, Everyday Ind, SJS, Authum, Adani enterprise, M&M"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "My wife says we can’t afford to retire. We have $4 million. Do I just keep working?"
- BZ=F (Brent Crude Oil Last Day Finan) score 8.8 — "Dividend, rights issue record date: Last chance to buy today - Shivam Autotech, Shraddha P"
- GS (Goldman Sachs Group, Inc. (The) score 8.7 — "GOLDMAN SACHS ($GS ) Q3 EARNINGS BEAT ESTIMATES Results * EPS: $17.01 vs. $13.02 est. (+30"
- JEF (Jefferies Financial Group Inc.) score 8.6 — "ICICI Prudential AMC shares rise 2% as Jefferies, other brokerages revise target prices af"
- RS (Reliance, Inc.) score 8.0 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.3 — "RBI to curb rupee volatility amid external pressures, says Finance Minister Sitharaman"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 7.1 — "RBI to curb rupee volatility amid external pressures, says Finance Minister Sitharaman"
- NVDA (NVIDIA Corporation) score 6.3 — "Nvidia’s share of China AI chip market falls to 34% as Huawei gains ground"
- META (Meta) score 5.0 — "Meta is back on the AI leaderboard with its new family of Wonder models"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.6 — "CKK Retail Mart to issue 5:1 bonus, enhance share capital"
- POLICYBZR.NS (PB FINTECH LIMITED) score 3.7 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.3 — "Piero Cipollone: Interview with Corriere della Sera"
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