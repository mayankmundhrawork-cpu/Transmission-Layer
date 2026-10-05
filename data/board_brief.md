# Transmission Layer — board brief · 2026-10-05 11:25Z

data as of **2026-10-05** · 97 series · 7 red / 35 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.75, 1d in regime; vol-pct 0.7, breadth-off 0.8, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.42, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.19, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.03, corr60 0.12, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.25, corr60 -0.09, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.587, β -0.4304, p 0.0); driver zc 2.44 → expected -1.058%. Type hit-rate 0.816 (n=2364).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.384, β 0.2222, p 0.0); driver zc 2.44 → expected 0.546%. Type hit-rate 0.816 (n=2364).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.37, β -0.2069, p 0.0); driver zc 2.44 → expected -0.508%. Type hit-rate 0.816 (n=2364).
- Track record · residual_reversion: hit-rate **0.497** (n=1127) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2364) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 8.34] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.61, z20 2.06, zc -0.65, resid-z -1.26 [quiet], 1d -0.53%, |z20|=2.06; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.54, z20 -1.99, zc -0.59, resid-z -4.75 [unexplained], 1d -0.22%, 1y-pct=0
- ust_10y [RATES]: last 5.24, z20 1.51, zc -0.89, resid-z -2.10 [unexplained], 1d -0.95%, |z20|=1.51; 1y-pct=98
- tips_10y_real [RATES]: last 2.88, z20 1.41, zc -0.84, resid-z -2.58 [unexplained], 1d -1.71%, 1d move -5.0bps ≥ 5bps; 1y-pct=98
- ust_2y [RATES]: last 4.78, z20 0.62, zc -1.55, resid-z -3.54 [unexplained], 1d -2.05%, 1y-pct=97
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.701 vs ust_30y, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.558 vs dyn_bond
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.531 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.517 vs ust_30y
- Source: What Bessent is now saying after bond yields didn’t stop rising on ‘I am the house’ remark — MarketWatch Top, 2026-10-05. https://www.marketwatch.com/story/what-bessent-is-now-saying-after-bond-yields-didnt-stop-rising-on-i-am-the-house-remark-0ab359f8?mod=mw_rss_topstories
- Source: India’s BPCL plans $3 billion bond sale to fund Brazil oil bet — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/bonds/indias-bpcl-plans-3-billion-bond-sale-to-fund-brazil-oil-bet/articleshow/134699704.cms
- Source: The bond selloff is opening up rare opportunities for investors. Here is where to look, says major bank. — MarketWatch Top, 2026-10-05. https://www.marketwatch.com/story/bond-selloff-is-opening-up-rare-opportunities-for-investors-here-is-where-to-look-says-major-bank-463447c7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 6.24] usd_inr ↑
- usd_inr [FX]: last 96.29, z20 1.24, zc 0.58, resid-z 0.31 [quiet], 1d 0.07%, 20d range extreme; 1y-pct=95
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.396 via usd_inr, z 0.96, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.396, z 0.96)
- Source: Rupee ends flat, anchored by RBI intervention in face of global strains — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-ends-flat-anchored-by-rbi-intervention-in-face-of-global-strains/articleshow/134700361.cms
- Source: Gap-Up fades as IT and HDFC Bank drag Nifty to near-flat; crude, Rupee weigh — BusinessLine Mkts, 2026-10-05. https://www.thehindubusinessline.com/markets/gap-up-fades-as-it-and-hdfc-bank-drag-nifty-to-near-flat-crude-rupee-weigh/article71546207.ece
- Source: RBI likely intervenes to support rupee, traders say — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/forex/rbi-likely-intervenes-to-support-rupee-traders-say/articleshow/134686004.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.03] indices · 2 series ↑
- nikkei_225 [INDICES]: last 69928.05, z20 3.20, zc -0.47, resid-z -0.82 [quiet], 1d 2.37%, |z20|=3.20; 1y-pct=97
- taiwan_weighted [INDICES]: last 49666.41, z20 2.84, zc 0.23, resid-z -0.28 [quiet], 1d 2.46%, |z20|=2.84; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.544 via taiwan_weighted, z -1.41, reacted); nifty_it (rho -0.374 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.842 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.544, z -1.41); nifty_it (rho -0.374, z -0.73)
- Source: Global Market: Japan’s Nikkei jumps 2.5% to 3-month high as AI stocks rally — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-jumps-2-5-to-3-month-high-as-ai-stocks-rally/articleshow/134685851.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [AMBER 5.96] cross-asset · 4 series ↓
- india_vix [INDICES]: last 14.71, z20 2.30, zc 1.21, resid-z n/a [quiet], 1d 1.73%, |z20|=2.30
- dyn_policybzr_ns [EQUITIES]: last 976.20, z20 -1.92, zc -1.18, resid-z -0.96 [quiet], 1d -0.39%, 1y-pct=0
- nifty_50 [INDICES]: last 22555.75, z20 -1.82, zc -1.36, resid-z -1.34 [quiet], 1d 0.60%, |z20|=1.82; 1y-pct=1
- nifty_midcap_100 [INDICES]: last 59127.45, z20 -1.81, zc -1.06, resid-z -0.70 [quiet], 1d 0.67%, |z20|=1.81
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.634 via nifty_midcap_100, z -1.32, reacted); nifty_fmcg (rho 0.573 via nifty_50, z -1.43, reacted); dyn_bajfinance_ns (rho -0.572 via india_vix, z -1.41, reacted); dyn_jiofin_bo (rho 0.537 via nifty_50, z -2.5, reacted); nifty_metal (rho 0.521 via nifty_midcap_100, z -2.21, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.634, z -1.32); nifty_fmcg (rho 0.573, z -1.43); dyn_bajfinance_ns (rho -0.572, z -1.41); dyn_jiofin_bo (rho 0.537, z -2.5)
- Source: Small-cap stock under  ₹100 jumps 4% following relief rally on Dalal Street | Do you own? — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/smallcap-stock-under-rs-100-jumps-4-following-relief-rally-on-dalal-street-do-you-own-11791197541177.html
- Source: Sensex today | Stock Market Live: Sensex rises 472 pts to end at 72,382, Nifty settles at 22,555; ITC, Eternal lead gainers — BusinessLine Mkts, 2026-10-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-5th-october-2026/article71544056.ece
- Source: Stock market prediction for tomorrow: Sensex, Nifty outlook for Tuesday | Kospi, Taiwan cues to watch | 6 Oct 2026 — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/stock-market-prediction-for-tomorrow-sensex-nifty-outlook-for-tuesday-kospi-taiwan-cues-to-watch-6-oct-2026-11791193571147.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 4.84] dxy ↑
- dxy [FX]: last 102.25, z20 1.84, zc -0.47, resid-z 2.77 [unexplained], 1d 0.32%, 20d range extreme; |z20|=1.84; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [RED 4.5] dyn_jiofin_bo ↓
- dyn_jiofin_bo [EQUITIES]: last 211.15, z20 -2.50, zc -1.66, resid-z -0.41 [priced], 1d -0.40%, |z20|=2.50; 1y-pct=0
- **Mechanism**: dyn_jiofin_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.537 via dyn_jiofin_bo, z -2.53, reacted); nifty_midcap_100 (rho 0.496 via dyn_jiofin_bo, z -2.52, reacted); nifty_metal (rho 0.395 via dyn_jiofin_bo, z -2.96, reacted); dyn_muthootfin_ns (rho 0.362 via dyn_jiofin_bo, z -2.12, reacted)
- **India receivers**: nifty_50 (rho 0.537, z -1.82); dyn_bajfinance_ns (rho 0.513, z -1.41); nifty_midcap_100 (rho 0.496, z -1.81); nifty_metal (rho 0.395, z -2.21)

### [AMBER 4.39] dyn_stylebaaza_ns ↓
- dyn_stylebaaza_ns [EQUITIES]: last 361.00, z20 -2.39, zc -1.31, resid-z -1.04 [quiet], 1d -2.00%, |z20|=2.39
- **Mechanism**: dyn_stylebaaza_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: FIIs, retail investors raise stakes in 10 stocks, shares rally up to 35% in 3 months — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/stocks/news/fiis-retail-investors-raise-stakes-in-10-stocks-stocks-rally-up-to-35-in-3-months/slideshow/134695032.cms
- Source: Crash alert! V2 Retail shares plunge 20% on Q2 business update; festive season shift weighs on growth — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/stocks/news/crash-alert-v2-retail-shares-plunge-20-on-q2-business-update-festive-season-shift-weighs-on-growth/articleshow/134685984.cms
- Source: V2 Retail shares plunge 19% after Q2 business update | What lies ahead for investors? — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/v2-retail-shares-plunge-19-after-q2-business-update-what-lies-ahead-for-investors-11791173055240.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [RED 4.36] bovespa ↑
- bovespa [INDICES]: last 191797.94, z20 4.36, zc 2.44, resid-z 1.90 [unexplained], 1d 2.46%, |z20|=4.36; 1y-pct=96
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_stylebaaza_ns (rho -0.436 via bovespa, z -2.39, reacted)
- **India receivers**: dyn_stylebaaza_ns (rho -0.436, z -2.39)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

## Watchlist (below surfacing floor)
eur_usd ↓ (4.35), hang_seng ↓ (4.22), rates · 2 series ↑ (4.13), dyn_nvda ↑ (3.77), dyn_4417_t ↑ (3.63), gold_silver_ratio ↓ (3.44), indices · 2 series ↓ (3.33), dyn_hdb ↓ (2.96), nifty_metal ↓ (2.21), usd_cny ↓ (2.21), dyn_tech ↑ (2.21), dyn_voltas_ns ↓ (2.16)

## India macro
- nifty_50: 22555.7500 (1d 0.60%, z20 -1.82, flag amber)
- nifty_midcap_100: 59127.4492 (1d 0.67%, z20 -1.81, flag amber)
- usd_inr: 96.2925 (1d 0.07%, z20 1.24, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6214 (1d 0.08%, z20 -1.32, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI MPC decision T-2d · AMFI SIP / MF flows T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.9 — "From gold consumer to global powerhouse: How India refines, designs, and dominates"
- COALINDIA.NS (COAL INDIA LTD) score 70.1 — "From gold consumer to global powerhouse: How India refines, designs, and dominates"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 68.9 — "From gold consumer to global powerhouse: How India refines, designs, and dominates"
- INDIANB.NS (INDIAN BANK) score 57.7 — "SoftBank-backed Starfish gets ₹88.3 crore from AceVector IPO exit"
- COIN (Coinbase Global, Inc.) score 45.0 — "From gold consumer to global powerhouse: How India refines, designs, and dominates"
- BOND (PIMCO Active Bond Exchange-Tra) score 42.9 — "Indian markets eye gap-up opening; crude, bond yields and RBI policy remain key"
- BAC (Bank of America Corporation) score 41.5 — "SoftBank-backed Starfish gets ₹88.3 crore from AceVector IPO exit"
- HDB (HDFC Bank Limited) score 39.1 — "SoftBank-backed Starfish gets ₹88.3 crore from AceVector IPO exit"
- OHI (Omega Healthcare Investors, In) score 38.1 — "From a nation of savers to a nation of investors: NSE bets on technology, financialisation"
- IDBI.NS (IDBI BANK LIMITED) score 36.2 — "SoftBank-backed Starfish gets ₹88.3 crore from AceVector IPO exit"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.2 — "SoftBank-backed Starfish gets ₹88.3 crore from AceVector IPO exit"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.2 — "SoftBank-backed Starfish gets ₹88.3 crore from AceVector IPO exit"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.6 — "From a nation of savers to a nation of investors: NSE bets on technology, financialisation"
- CHKP (Check Point Software Technolog) score 30.6 — "Runwal Enterprises shares to list today; check GMP and key details ahead of debut"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 29.9 — "From a nation of savers to a nation of investors: NSE bets on technology, financialisation"
- TECH (Bio-Techne Corp) score 29.9 — "From a nation of savers to a nation of investors: NSE bets on technology, financialisation"
- LTH (Life Time Group Holdings, Inc.) score 27.4 — "China returns to top 100 in gender parity ranking for first time since 2016"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 27.2 — "Nayara Energy hikes petrol by ₹5, diesel by ₹3"
- TGT (Target Corporation) score 25.0 — "OPEC+ agrees in principle to keep oil output targets unchanged in November, delegate says"
- SEPN (Septerna, Inc.) score 23.0 — "TIMIRAOS: WEAK JOBS REPORT CLEARS PATH FOR FED PAUSE The September jobs report gives the F"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 16.7 — "NSE vs BSE: Which is a better exchange stock to buy ahead of Q2 results - What experts sug"
- 301077.SZ (CHINASTARS) score 15.3 — "China returns to top 100 in gender parity ranking for first time since 2016"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.4 — "CBOE VOLATILITY INDEX HITS ONE-WEEK LOW, LAST DOWN 0.79 POINTS AT 15.60"
- JIOFIN.BO (Jio Financial Services Limited) score 10.5 — "Why India’s gold loan boom is becoming a story about financial inclusion"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.5 — "The 2029 tipping point: Western populations are about to start shrinking, piling pressure "
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.3 — "Europe’s Diesel Woes Just Got Even Worse"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.8 — "Adani Energy Solutions share price rally: From  ₹990 to  ₹1,350 in just 6 months: Know why"
- JEF (Jefferies Financial Group Inc.) score 6.8 — "Bajaj Finance shares jump 5% after Q2 business update. Why Jefferies sees 35% upside in it"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 6.5 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 6.5 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.2 — "V2 Retail shares plunge 19% after Q2 business update | What lies ahead for investors?"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.1 — "Where could PB Fintech share price be in the next five years?"
- NVDA (NVIDIA Corporation) score 5.0 — "Nvidia still 'the one' for AI? BNP Paribas raises target to $345, sees up to 47% upside"
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "U.S. Diesel Export Ban Would Hit Latin America Hardest: Goldman"
- META (Meta) score 4.7 — "META PARTS WAYS WITH VIRTUE AI - SEMAFOR"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.3 — "20 Stocks to watch today: HDFC Bank, ICICI life, Wipro, DLF, Ola Electric & Gland Pharma"
- VT (Vanguard Total World Stock Ind) score 4.2 — "Jio Platforms IPO in final stages after concluding worldwide roadshows"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 4.0 — "Bajaj Finance shares jump 5% after Q2 business update. Why Jefferies sees 35% upside in it"
- VOLTAS.NS (VOLTAS LTD) score 0.2 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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