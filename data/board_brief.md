# Transmission Layer — board brief · 2026-09-07 09:18Z

data as of **2026-09-07** · 98 series · 7 red / 38 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.261, 2d in regime; vol-pct 0.188, breadth-off 0.333, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.46, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.01, corr60 0.34, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.05, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.07, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.16, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.02, corr60 0.23, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.501** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1972) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.26] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 13.88, z20 5.26, zc 2.93, resid-z 4.13 [unexplained], 1d 17.03%, |z20|=5.26; 1y-pct=98
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PC Jeweller share price surges 15% today - jumps 35% in 1 month - rally reason explained — Mint Markets, 2026-09-07. https://www.livemint.com/market/stock-market-news/pc-jeweller-share-price-surges-15-today-jumps-35-in-1-month-rally-reason-explained-11788756711988.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [RED 6.93] usd_jpy ↓
- usd_jpy [FX]: last 154.46, z20 -4.93, zc -0.74, resid-z -5.45 [unexplained], 1d -0.77%, |z20|=4.93
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho -0.391 via usd_jpy, z 5.26, reacted)
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.528 vs usd_jpy
- **India receivers**: dyn_pcjeweller_ns (rho -0.391, z 5.26)
- Source: Japan's foreign reserves drop by a record $80 billion in August following yen intervention — CNBC Economy, 2026-09-07. https://www.cnbc.com/2026/09/07/japan-foreign-reserves-yen-intervention.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 5.26] cross-asset · 4 series ↑
- ust_10y [RATES]: last 4.77, z20 1.59, zc -0.43, resid-z 0.29 [quiet], 1d -0.42%, |z20|=1.59; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.04, z20 -1.49, zc -0.03, resid-z -0.38 [quiet], 1d -0.01%, 1y-pct=1
- ust_2y [RATES]: last 4.34, z20 1.48, zc -0.89, resid-z -0.06 [quiet], 1d -1.14%, 1y-pct=98
- ust_30y [RATES]: last 5.25, z20 0.47, zc -0.48, resid-z -0.10 [quiet], 1d -0.38%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.858 vs ust_10y
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.524 vs ust_10y, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.524 vs dyn_bond, historically leads by 3d
- Watch next: ust_2s10s (inverse) — not yet - watch; rho -0.506 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.506 vs dyn_bond
- Source: Global Market: Japanese bond yields rise as BOJ rate hike bets keep markets on edge — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-rise-as-boj-rate-hike-bets-keep-markets-on-edge/articleshow/133871174.cms
- Source: HDFC Bank shares in focus after AT1 bond redemption announcement — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/hdfc-bank-shares-in-focus-after-at1-bond-redemption-announcement/article71437483.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [AMBER 5.1] cross-asset · 2 series ↓
- dyn_techm_ns [EQUITIES]: last 1557.90, z20 -2.27, zc -1.54, resid-z -0.14 [moved], 1d -2.44%, |z20|=2.27
- nifty_it [INDICES]: last 29919.45, z20 -2.14, zc -1.71, resid-z -1.13 [moved], 1d -2.53%, |z20|=2.14
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.643 via nifty_it, z -2.61, reacted); dyn_tatatech_ns (rho 0.548 via nifty_it, z -1.75, reacted); nifty_50 (rho 0.53 via nifty_it, z -2.38, reacted); dyn_cartrade_ns (rho -0.457 via dyn_techm_ns, z 1.81, reacted)
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.514 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.643, z -2.61); dyn_tatatech_ns (rho 0.548, z -1.75); nifty_50 (rho 0.53, z -2.38); dyn_cartrade_ns (rho -0.457, z 1.81)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Analysis — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-07-sep-2026/liveblog/133862746.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [AMBER 4.87] commodities · 2 series ↑
- wti [COMMODITIES]: last 91.48, z20 2.04, zc 0.08, resid-z -0.12 [quiet], 1d 0.20%, |z20|=2.04
- brent [COMMODITIES]: last 96.28, z20 1.88, zc 0.35, resid-z 0.02 [quiet], 1d 0.80%, |z20|=1.88
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.666 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.517 vs wti
- Source: Global Market: European stocks subdued as oil surge fuels inflation, ECB rate hike bets — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-stocks-subdued-as-oil-surge-fuels-inflation-ecb-rate-hike-bets/articleshow/133872715.cms
- Source: Oil prices hit near seven-week highs, before edging lower, as Iran plans to increase control of Hormuz — MarketWatch Top, 2026-09-07. https://www.marketwatch.com/story/oil-prices-hit-near-seven-week-highs-before-edging-lower-as-iran-plans-to-increase-control-of-hormuz-5070167c?mod=mw_rss_topstories
- Source: India’s oil and gas sector to remain under pressure as crude, LNG costs rise — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/commodities/indias-oil-and-gas-sector-to-remain-under-pressure-as-crude-lng-costs-rise/article71437678.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.81] dyn_havells_ns ↓
- dyn_havells_ns [EQUITIES]: last 1147.90, z20 -2.81, zc -0.36, resid-z -3.11 [unexplained], 1d -0.53%, |z20|=2.81; 1y-pct=1
- **Mechanism**: dyn_havells_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Havells holding out for improvements — BusinessLine Mkts, 2026-09-05. https://www.thehindubusinessline.com/portfolio/stock-fundamental-analysis-india/havells-holding-out-for-improvements/article71423530.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-22 (d=0.01), 2025-06-30 (d=0.02)

### [AMBER 4.38] nifty_50 ↓
- nifty_50 [INDICES]: last 23754.65, z20 -2.38, zc -1.19, resid-z 0.12 [quiet], 1d -0.60%, |z20|=2.38
- **Mechanism**: nifty_50 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.745 via nifty_50, z -1.5, reacted); nifty_midcap_100 (rho 0.647 via nifty_50, z -2.83, reacted); nifty_fmcg (rho 0.627 via nifty_50, z -1.86, reacted); nifty_it (rho 0.53 via nifty_50, z -2.14, reacted); dyn_indusindbk_bo (rho 0.517 via nifty_50, z -0.03, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.741 vs nifty_50
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.599 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.517 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.745, z -1.5); nifty_midcap_100 (rho 0.647, z -2.83); nifty_fmcg (rho 0.627, z -1.86); nifty_it (rho 0.53, z -2.14)
- Source: India in multi quarter growth upcycle, says Morgan Stanley; sees Sensex at 89,000 by June 2027 — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/india-in-multi-quarter-growth-upcycle-says-morgan-stanley-sees-sensex-at-89000-by-june-2027/articleshow/133871432.cms
- Source: Sensex today | Stock Market LIVE: Sensex crashes 480 pts, Nifty slips to 23,750; Infy, TechM lead losers — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-7th-september-2026/article71437259.ece
- Source: Nifty Prediction Today – September 07, 2026: Nifty 50 Futures: Can fall more. Go short — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/portfolio/technical-analysis/nifty-prediction-today-september-07-2026-nifty-50-futures-can-fall-more-go-short/article71437461.ece
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

### [AMBER 4.23] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1507.70, z20 -2.23, zc -0.10, resid-z -0.01 [quiet], 1d -0.15%, |z20|=2.23; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: India’s Rs 1 lakh crore digital-media boom: Two stocks ICICI Securities is betting on — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/indias-rs-1-lakh-crore-digital-media-boom-two-stocks-icici-securities-is-betting-on/articleshow/133872047.cms
- Source: ICICI Bank shares in focus as LIC gets RBI nod to acquire 9.99% stake in private lender — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/icici-bank-shares-in-focus-as-lic-gets-rbi-nod-to-acquire-9-99-stake-in-private-lender/articleshow/133861811.cms
- Source: LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank — BusinessLine Mkts, 2026-09-05. https://www.thehindubusinessline.com/money-and-banking/lic-gets-rbi-approval-to-acquire-up-to-999-stake-in-icici-bank/article71431558.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

## Watchlist (below surfacing floor)
natgas ↑ (4.03), cross-asset · 2 series ↑ (3.82), usd_inr ↓ (3.51), midcap_largecap_ratio ↑ (3.46), gold_silver_ratio ↓ (3.42), dyn_tech ↑ (3.1), nifty_midcap_100 ↓ (2.83), fx · 2 series ↑ (2.77), taiwan_weighted ↑ (2.64), dyn_tataelxsi_ns ↓ (2.61), dyn_dell ↑ (2.58), dyn_meta ↑ (2.17)

## India macro
- nifty_50: 23754.6504 (1d -0.60%, z20 -2.38, flag amber)
- nifty_midcap_100: 62731.8516 (1d -0.55%, z20 -2.83, flag red)
- usd_inr: 94.4600 (1d -0.04%, z20 -1.51, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6408 (1d 0.04%, z20 0.46, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · AMFI SIP / MF flows T-1d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 62.1 — "India’s critical minerals mission needs institution builders, not mine operators"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 58.6 — "India’s critical minerals mission needs institution builders, not mine operators"
- COALINDIA.NS (COAL INDIA LTD) score 58.4 — "India’s critical minerals mission needs institution builders, not mine operators"
- INDIANB.NS (INDIAN BANK) score 52.0 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- BAC (Bank of America Corporation) score 45.8 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- COIN (Coinbase Global, Inc.) score 44.7 — "Iran War Forces a Rewrite of Global Oil Trade Routes"
- HDB (HDFC Bank Limited) score 40.6 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- IDBI.NS (IDBI BANK LIMITED) score 39.2 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.2 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.2 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.5 — "Green Bonds Hit Record High Despite Persistent Challenges"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.7 — "Former Tata Technologies CEO McGoldrick sells shares worth ₹165 crore"
- CHKP (Check Point Software Technolog) score 32.6 — "Crude Check: Prices could moderate"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.5 — "Former Tata Technologies CEO McGoldrick sells shares worth ₹165 crore"
- TECH (Bio-Techne Corp) score 32.5 — "Former Tata Technologies CEO McGoldrick sells shares worth ₹165 crore"
- OHI (Omega Healthcare Investors, In) score 31.1 — "Pranav Constructions raises ₹84 crore from anchor investors; IPO to open on Sep 7"
- LTH (Life Time Group Holdings, Inc.) score 20.9 — "Anthropic IPO timeline shifts toward mid-October"
- 301077.SZ (CHINASTARS) score 18.8 — "Typhoon Saudel: days of flooding trigger fatal landslide in central China"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.4 — "Oil-Rich Oman Bets Big on Renewable Energy"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.7 — "3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma majors, Adani Enterprises,"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.6 — "PC Jeweller share price surges 15% today - jumps 35% in 1 month - rally reason explained"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.7 — "Former Tata Technologies CEO McGoldrick sells shares worth ₹165 crore"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.7 — "Former Tata Technologies CEO McGoldrick sells shares worth ₹165 crore"
- NVDA (NVIDIA Corporation) score 9.0 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- JIOFIN.BO (Jio Financial Services Limited) score 8.8 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- VT (Vanguard Total World Stock Ind) score 7.7 — "World’s biggest money managers are rebuilding gold positions"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.0 — "3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma majors, Adani Enterprises,"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.8 — "India increases coal rail supplies as 58 power plants face low inventories"
- MS (Morgan Stanley) score 6.5 — "3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma majors, Adani Enterprises,"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.1 — "BSE shares surge 10% in just 3 sessions. What’s driving the rally?"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.1 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.8 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 4.1 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- META (Meta) score 3.3 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- DELL (Dell Technologies Inc.) score 2.1 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.2 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.0 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 0.3 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.3 — "Can Wolfe’s upgrade push Moderna stock higher?"
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