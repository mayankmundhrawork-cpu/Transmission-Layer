# Transmission Layer — board brief · 2026-10-14 00:26Z

data as of **2026-10-14** · 97 series · 6 red / 34 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 8d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.4, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.27, corr60 0.23, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.01, corr60 0.14, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.05, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.27, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.61, corr60 0.15, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2098) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 5.59] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 29830.10, z20 2.76, zc 3.54, resid-z 2.57 [unexplained], 1d 5.22%, |z20|=2.76
- dyn_tataelxsi_ns [EQUITIES]: last 3426.70, z20 2.07, zc 2.62, resid-z 2.08 [unexplained], 1d 5.21%, |z20|=2.07
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-31 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho 0.859 via nifty_it, z 0.42, quiet); nifty_50 (rho 0.592 via dyn_tataelxsi_ns, z -0.5, quiet); dyn_justdial_bo (rho 0.534 via nifty_it, z 0.7, quiet); nifty_fmcg (rho 0.532 via dyn_tataelxsi_ns, z -0.54, quiet); dyn_tatatech_ns (rho 0.491 via nifty_it, z 1.48, reacted)
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.859 vs nifty_it, historically leads by 3d
- Watch next: dyn_justdial_bo (co-move) — not yet - watch; rho 0.534 vs nifty_it, historically leads by 4d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.592 vs dyn_tataelxsi_ns
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.532 vs dyn_tataelxsi_ns
- **India receivers**: dyn_techm_ns (rho 0.859, z 0.42); nifty_50 (rho 0.592, z -0.5); dyn_justdial_bo (rho 0.534, z 0.7); nifty_fmcg (rho 0.532, z -0.54)
- Source: Q2 Results Today Highlights: Q2 Results Today Live: Tata Elxsi, ICICI Pru Life, Hero Motors shares trade mixed; PNB Gilts jumps 8% — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/q2-results-today-highlights-hero-motors-icici-pru-tata-elxsi-ss-retail-anand-rathi-share-company-results-13-october-2026/article71577900.ece
- Source: Tata Elxsi Q2 Results: Profit rises 10% YoY to Rs 170 crore; revenue grows 15% — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/stocks/earnings/tata-elxsi-q2-results-profit-rises-10-yoy-to-rs-170-crore-revenue-grows-15/articleshow/134918419.cms
- Source: Q2 Results Today Live: Q2 Results Today Live: Tata Elxsi, ICICI Pru Life, Hero Motors shares trade mixed; PNB Gilts jumps 8% — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-hero-motors-icici-pru-tata-elxsi-ss-retail-anand-rathi-share-company-results-13-october-2026/article71577900.ece
- Historical analogues: 2025-07-31 (d=0.34), 2025-01-30 (d=0.36), 2025-07-09 (d=0.4)

### [AMBER 4.89] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.91, z20 0.95, zc 0.74, resid-z 0.80 [quiet], 1d 1.39%, 1y-pct=97
- ust_30y [RATES]: last 5.60, z20 0.87, zc 0.00, resid-z 0.11 [quiet], 1d 0.00%, 1y-pct=97
- ust_10y [RATES]: last 5.24, z20 0.79, zc 0.38, resid-z 0.49 [quiet], 1d 0.38%, 1y-pct=96
- dyn_bond [EQUITIES]: last 87.08, z20 -0.54, zc 0.38, resid-z 1.21 [quiet], 1d 0.13%, 1y-pct=4
- ust_2y [RATES]: last 4.80, z20 0.26, zc 0.81, resid-z 0.85 [quiet], 1d 1.05%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.527 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.504 vs ust_30y
- Source: U.S. TREASURY YIELDS FALL FOLLOWING FED'S WILLIAMS COMMENTS U.S. Treasury yields moved lower after New York Fed President John Williams signaled one more rate hike in 2026 may be sufficient, with no further increases currently anticipated in 2027. 30-year yield: 5.565% (-3.42 bps) 10-year yield: 5.2 — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37025
- Source: BOND EXPERT WARNS OF $110 BILLION SELLING SHOCK IF TREASURY YIELDS HIT 6% Veteran bond strategist Harley Bassman warns of a “nightmare scenario” in U.S. Treasuries. If the 20-year Treasury yield rises above 6%, futures-related hedging could trigger selling pressure equivalent to $110 billion in bond — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37018
- Source: India's benchmark bond breaks 4-day falling streak as value investors return — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/bonds/indias-benchmark-bond-breaks-4-day-falling-streak-as-value-investors-return/articleshow/134918791.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 4.66] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 70.47, z20 1.66, zc n/a, resid-z n/a [quiet], 1d 0.01%, GSR<75 (extreme low); |z20|=1.66
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.396 via gold_silver_ratio, z -0.95, quiet)
- **India receivers**: midcap_largecap_ratio (rho -0.396, z -0.95)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 4.28] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -4.28, zc -1.44, resid-z -1.96 [unexplained], 1d -0.15%, |z20|=4.28; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.361 via usd_cny, z -0.69, quiet); dyn_bajfinance_ns (rho -0.356 via usd_cny, z -0.09, quiet)
- **India receivers**: dyn_policybzr_ns (rho -0.361, z -0.69); dyn_bajfinance_ns (rho -0.356, z -0.09)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.06] indices · 2 series ↑
- sp500 [INDICES]: last 7805.59, z20 1.23, zc -0.03, resid-z 0.73 [quiet], 1d -0.02%, 1y-pct=98
- nasdaq_100 [INDICES]: last 30568.69, z20 0.28, zc -0.30, resid-z -0.76 [quiet], 1d -0.31%, 1y-pct=95
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.953 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.724 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.873 vs sp500
- Watch next: wti (inverse) — not yet - watch; rho -0.605 vs nasdaq_100, historically leads by 2d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.633 vs sp500
- Source: Wall Street Sees Inflation Easing Even With Oil Above $90 — OilPrice, 2026-10-14. https://oilprice.com/Energy/Energy-General/Wall-Street-Sees-Inflation-Easing-Even-With-Oil-Above-90.html
- Source: US stocks: Nasdaq ends down as chipmakers fall and bank earnings roll in — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-nasdaq-ends-down-as-chipmakers-fall-and-bank-earnings-roll-in/articleshow/134926328.cms
- Source: U.S. CORE INFLATION FORECAST ALIGNS WITH WALL STREET EXPECTATIONS The Cleveland Fed's inflation nowcast points to core CPI rising 0.20% month-over-month, nearly matching analysts' median forecast of 0.21%. Key figures: * Headline CPI: +0.53% MoM, below analysts' forecast range of 0.55%–0.62%. * Core — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37032
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [AMBER 3.89] natgas ↑
- natgas [COMMODITIES]: last 3.32, z20 1.89, zc -0.01, resid-z 1.99 [unexplained], 1d -0.03%, |z20|=1.89
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.138 vs natgas, historically leads by 4d
- Source: Stranded Middle East LNG Supply Upends Gas Markets — OilPrice, 2026-10-13. https://oilprice.com/Energy/Natural-Gas/Stranded-Middle-East-LNG-Supply-Upends-Gas-Markets.html
- Source: China’s $3 Billion Qatar LNG Deal Raises an Awkward Question — OilPrice, 2026-10-13. https://oilprice.com/Energy/Natural-Gas/Chinas-3-Billion-Qatar-LNG-Deal-Raises-an-Awkward-Question.html
- Source: Super El Niño Could Ease Asia’s LNG Supply Concerns — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Super-El-Nio-Could-Ease-Asias-LNG-Supply-Concerns.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 3.71] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3799.50, z20 -1.71, zc 0.08, resid-z 0.72 [quiet], 1d 0.06%, |z20|=1.71; 1y-pct=1
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.373 via shanghai_comp, z 0.04, quiet)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.547 vs shanghai_comp, historically leads by 2d
- **India receivers**: dyn_inoxindia_ns (rho 0.373, z 0.04)
- Source: Global Market: China stocks fall as global yields, geopolitical tensions weigh on sentiment — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-global-yields-geopolitical-tensions-weigh-on-sentiment/articleshow/134884757.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [RED 3.6] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 349.20, z20 3.60, zc 1.03, resid-z -0.25 [quiet], 1d 2.02%, |z20|=3.60; 1y-pct=99
- **Mechanism**: dyn_karurvysya_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho 0.487 via dyn_karurvysya_ns, z 1.13, reacted); usd_inr (rho -0.413 via dyn_karurvysya_ns, z -1.0, reacted); dyn_muthootfin_ns (rho 0.383 via dyn_karurvysya_ns, z -1.39, reacted)
- **India receivers**: dyn_indianb_ns (rho 0.487, z 1.13); usd_inr (rho -0.413, z -1.0); dyn_muthootfin_ns (rho 0.383, z -1.39)
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

## Watchlist (below surfacing floor)
dyn_rs ↑ (3.48), dyn_meta ↑ (3.38), indices · 2 series ↓ (3.37), dyn_4417_t ↑ (3.31), comex_copper ↑ (3.3), kospi ↓ (2.89), dyn_policybzr_ns ↓ (2.69), dyn_cartrade_ns ↑ (2.61), dyn_jiofin_bo ↓ (2.58), indices · 2 series ↓ (2.4), dyn_tech ↑ (2.4), dyn_nvda ↑ (2.15)

## India macro
- nifty_50: 22721.9492 (1d 1.60%, z20 -0.50, flag amber)
- nifty_midcap_100: 59458.4492 (1d 1.04%, z20 -0.65, flag none)
- usd_inr: 95.7759 (1d -1.03%, z20 -1.00, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6168 (1d -0.56%, z20 -0.95, flag none)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-1d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.6 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.0 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 73.3 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- INDIANB.NS (INDIAN BANK) score 69.7 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq ends lower as chip stocks extend "
- BAC (Bank of America Corporation) score 64.4 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq ends lower as chip stocks extend "
- HDB (HDFC Bank Limited) score 57.7 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq ends lower as chip stocks extend "
- IDBI.NS (IDBI BANK LIMITED) score 56.1 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq ends lower as chip stocks extend "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.1 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq ends lower as chip stocks extend "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.1 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq ends lower as chip stocks extend "
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.5 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- TECH (Bio-Techne Corp) score 51.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- COIN (Coinbase Global, Inc.) score 48.4 — "Global Market: European shares rise as lower oil prices lift sentiment; tech stocks slide"
- OHI (Omega Healthcare Investors, In) score 43.8 — "BOFA: U.S. TREASURY YIELDS MAY NEED TO HIT 6% TO DERAIL STOCK RALLY Bank of America's late"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.1 — "BOND EXPERT WARNS OF $110 BILLION SELLING SHOCK IF TREASURY YIELDS HIT 6% Veteran bond str"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.3 — "U.S. DIESEL FUTURES SURGE 4.5% DESPITE TRUMP'S RUSSIAN FUEL DEAL U.S. diesel futures jumpe"
- TGT (Target Corporation) score 30.8 — "FED'S WILLIAMS SEES ONE MORE RATE HIKE IN 2026, NONE IN 2027 New York Fed President John W"
- LTH (Life Time Group Holdings, Inc.) score 29.6 — "FED'S WILLIAMS SEES NO NEED FOR RATE HIKE IN 2027 AT THIS TIME"
- CHKP (Check Point Software Technolog) score 26.7 — "Top stocks to buy in F&O segment: M&M, Shree Cements, Cholamandalam Investment by Jay Thak"
- 301077.SZ (CHINASTARS) score 21.1 — "Micron’s stock extends declines as China competition heats up"
- SEPN (Septerna, Inc.) score 18.1 — "Minutes of the Board's discount rate meetings on August 17, September 9, and September 16,"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.0 — "RBL Bank share price crashes 8% after Q2 results - Should investors buy, sell, or hold the"
- JIOFIN.BO (Jio Financial Services Limited) score 13.4 — "70% women control portfolios, but none received structured financial training, study finds"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.4 — "STOCKS OF CRUDE OIL IN THE US STRATEGIC PETROLEUM RESERVE WERE UNCHANGED AT 283 MLN BARREL"
- VT (Vanguard Total World Stock Ind) score 10.4 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.0 — "MICHAEL SAYLOR PREDICTS BITCOIN WILL SURGE BACK ABOVE $100,000 Strategy ($MSTR ) Chairman "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Elxsi Q2 Results: Profit rises 10% YoY to Rs 170 crore; revenue grows 15%"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Tata Elxsi Q2 Results: Profit rises 10% YoY to Rs 170 crore; revenue grows 15%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.3 — "Stocks to Watch, Oct 12: Lenskart, Everyday Ind, SJS, Authum, Adani enterprise, M&M"
- GS (Goldman Sachs Group, Inc. (The) score 8.2 — "GOLDMAN SACHS ($GS ) Q3 EARNINGS BEAT ESTIMATES Results * EPS: $17.01 vs. $13.02 est. (+30"
- JEF (Jefferies Financial Group Inc.) score 8.2 — "ICICI Prudential AMC shares rise 2% as Jefferies, other brokerages revise target prices af"
- RS (Reliance, Inc.) score 7.6 — "Strong buzz! Reliance Jio said to see over $20 billion bids as investors line up for India"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.0 — "RBI to curb rupee volatility amid external pressures, says Finance Minister Sitharaman"
- NVDA (NVIDIA Corporation) score 6.9 — "NVDA - NVIDIA TO ANNOUNCE $2 BILLION IN NEW EUROPEAN AI INVESTMENTS Nvidia CEO Jensen Huan"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 6.7 — "RBI to curb rupee volatility amid external pressures, says Finance Minister Sitharaman"
- META (Meta) score 4.7 — "Meta is back on the AI leaderboard with its new family of Wonder models"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.4 — "CKK Retail Mart to issue 5:1 bonus, enhance share capital"
- POLICYBZR.NS (PB FINTECH LIMITED) score 3.5 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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