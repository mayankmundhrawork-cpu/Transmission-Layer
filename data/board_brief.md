# Transmission Layer — board brief · 2026-10-16 09:00Z

data as of **2026-10-16** · 97 series · 10 red / 28 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.732, 10d in regime; vol-pct 0.632, breadth-off 0.833, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.44, corr60 -0.44, contra nifty_50 corr20=0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.29, corr60 0.22, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.07, corr60 0.15, last shift 2026-08-26. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.02, last shift 2026-08-12. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.24, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.77, corr60 0.26, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 7.122317359220531e-06)
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.358, β -0.0895, p 0.0); driver zc 2.49 → expected -0.352%. Type hit-rate 0.824 (n=2165).
- Track record · residual_reversion: hit-rate **0.501** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2165) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.05] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1779.10, z20 6.73, zc 4.08, resid-z 4.49 [unexplained], 1d 7.82%, |z20|=6.73; 1y-pct=100
- nifty_it [INDICES]: last 31717.05, z20 3.88, zc 1.92, resid-z 2.07 [unexplained], 1d 3.25%, |z20|=3.88
- dyn_tataelxsi_ns [EQUITIES]: last 3826.00, z20 3.48, zc 1.39, resid-z 1.46 [quiet], 1d 3.41%, |z20|=3.48
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.539 via nifty_it, z 2.65, reacted); nifty_50 (rho 0.499 via dyn_tataelxsi_ns, z 0.64, quiet); nifty_fmcg (rho 0.463 via dyn_tataelxsi_ns, z -0.84, quiet); dyn_tatatech_ns (rho 0.423 via nifty_it, z 1.0, reacted); midcap_largecap_ratio (rho -0.398 via dyn_techm_ns, z -3.18, reacted)
- **India receivers**: dyn_justdial_bo (rho 0.539, z 2.65); nifty_50 (rho 0.499, z 0.64); nifty_fmcg (rho 0.463, z -0.84); dyn_tatatech_ns (rho 0.423, z 1.0)
- Source: Tech Mahindra shares jump 9% after Q2 results, Jefferies upgrades stock — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/markets/tech-mahindra-shares-jump-76-after-q2-results-jefferies-upgrades-stock/article71591220.ece
- Source: TCS vs HCL Tech vs Tech Mahindra vs Wipro: Which IT stock won Q2 results 2026? AI revenue, deal wins compared — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/tcs-vs-hcl-tech-vs-tech-mahindra-vs-wipro-which-it-stock-won-q2-results-2026-ai-revenue-deal-wins-compared-11792130967795.html
- Source: Tech Mahindra up 7% after Q2 results, dividend, bonus shares announced- Buy, sell or hold? Check target prices, ratings — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/tech-mahindra-up-5-after-q2-results-dividend-bonus-shares-announced-buy-sell-or-hold-check-target-prices-ratings-11792123783188.html
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 7.43] usd_inr ↓
- usd_inr [FX]: last 94.96, z20 -2.43, zc -0.37, resid-z -0.11 [quiet], 1d -0.20%, 20d range extreme; |z20|=2.43; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.37 via usd_inr, z -0.24, quiet); dyn_karurvysya_ns (rho -0.365 via usd_inr, z 2.95, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.37, z -0.24); dyn_karurvysya_ns (rho -0.365, z 2.95)
- Source: Gold, Silver rebound on softer Dollar and falling yields; domestic gains capped by Rupee strength — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/markets/gold/gold-silver-rebound-on-softer-dollar-and-falling-yields-domestic-gains-capped-by-rupee-strength/article71591618.ece
- Source: Rupee relief comes with disruptions in financial markets — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/forex/rupee-relief-comes-with-disruptions-in-financial-markets/articleshow/134985296.cms
- Source: Rupee rises 20 paise to 94.79 against US dollar in early trade — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-20-paise-to-94-79-against-us-dollar-in-early-trade/articleshow/134982864.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 5.88] wti ↑
- wti [COMMODITIES]: last 95.47, z20 0.88, zc -1.10, resid-z 0.87 [quiet], 1d -2.55%, 1-session move -2.55% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.861 vs wti
- Source: Global Fuel Oil Shortage Deepens as Middle East and Russia Supplies Collapse — OilPrice, 2026-10-16. https://oilprice.com/Latest-Energy-News/World-News/Global-Fuel-Oil-Shortage-Deepens-as-Middle-East-and-Russia-Supplies-Collapse.html
- Source: Oil Prices Head for Weekly Gain as Hormuz Attacks Rattle Markets — OilPrice, 2026-10-16. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Head-for-Weekly-Gain-as-Hormuz-Attacks-Rattle-Markets.html
- Source: Crude oil price falls as IEA agrees to complete remaining oil releases — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-fall-as-iea-agrees-to-complete-remaining-oil-releases/article71591091.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 5.39] brent ↓
- brent [COMMODITIES]: last 102.50, z20 -0.39, zc -1.80, resid-z -0.43 [priced], 1d -3.23%, 1-session move -3.23% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.861 vs brent, historically leads by 5d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.623 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.581 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.576 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.542 vs brent
- Source: Global Fuel Oil Shortage Deepens as Middle East and Russia Supplies Collapse — OilPrice, 2026-10-16. https://oilprice.com/Latest-Energy-News/World-News/Global-Fuel-Oil-Shortage-Deepens-as-Middle-East-and-Russia-Supplies-Collapse.html
- Source: Oil Prices Head for Weekly Gain as Hormuz Attacks Rattle Markets — OilPrice, 2026-10-16. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Head-for-Weekly-Gain-as-Hormuz-Attacks-Rattle-Markets.html
- Source: Crude oil price falls as IEA agrees to complete remaining oil releases — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-fall-as-iea-agrees-to-complete-remaining-oil-releases/article71591091.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.01] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7380.00, z20 3.01, zc 4.54, resid-z -1.04 [moved], 1d 15.67%, |z20|=3.01; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho -0.358 via dyn_4417_t, z -0.24, quiet)
- **India receivers**: dyn_coalindia_ns (rho -0.358, z -0.24)
- Source: Welspun Corp shares surge 230% YTD: Should investors buy this multibagger stock ahead of Q2 results? Experts suggestion — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/welspun-corp-shares-surge-230-ytd-should-investors-buy-this-multibagger-stock-ahead-of-q2-results-experts-suggestion-11792135856784.html
- Source: Q2 Preview: ICICI, Axis, YES, HDFC Bank - 4 banking stocks to declare results 2026 on Oct 17 - Expectations by experts — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/q2-preview-icici-axis-yes-hdfc-bank-4-banking-stocks-to-declare-results-2026-on-oct-17-expectations-by-experts-11792137099601.html
- Source: Reliance Jio IPO: Should investors chase listing gains or focus on long-term value? Experts weigh in — Mint Markets, 2026-10-16. https://www.livemint.com/market/ipo/reliance-jio-ipo-should-investors-chase-listing-gains-or-focus-on-long-term-value-experts-weigh-in-11792064886682.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.95] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 355.35, z20 2.95, zc 1.45, resid-z 1.02 [quiet], 1d 2.81%, |z20|=2.95; 1y-pct=100
- **Mechanism**: dyn_karurvysya_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho 0.46 via dyn_karurvysya_ns, z 2.0, reacted); dyn_muthootfin_ns (rho 0.395 via dyn_karurvysya_ns, z -1.19, reacted); usd_inr (rho -0.365 via dyn_karurvysya_ns, z -2.43, reacted); nifty_50 (rho 0.363 via dyn_karurvysya_ns, z 0.64, quiet)
- **India receivers**: dyn_indianb_ns (rho 0.46, z 2.0); dyn_muthootfin_ns (rho 0.395, z -1.19); usd_inr (rho -0.365, z -2.43); nifty_50 (rho 0.363, z 0.64)
- Source: Karur Vysya Bank shares jump 6% to hit a 52-week high after Q2 results - Should you buy? Rationale, target price — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/karur-vysya-bank-shares-jump-6-to-hit-a-52-week-high-after-q2-results-should-you-buy-rationale-target-price-11792125152481.html
- Source: Karur Vysya Bank shares rally 6% after Q2 profit jumps 37% YoY — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/karur-vysya-bank-shares-rally-6-after-q2-profit-jumps-37-yoy/articleshow/134982900.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 4.81] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 72.58, z20 1.81, zc n/a, resid-z n/a [quiet], 1d -1.07%, GSR<75 (extreme low); |z20|=1.81
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.534 vs gold_silver_ratio, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [AMBER 4.3] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3713.15, z20 -2.30, zc 0.19, resid-z -1.20 [quiet], 1d 0.15%, |z20|=2.30; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.395 via shanghai_comp, z -2.02, reacted)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.649 vs shanghai_comp, historically leads by 2d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.505 vs shanghai_comp, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.395, z -2.02)
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

## Watchlist (below surfacing floor)
dyn_dell ↓ (4.29), dow_jones ↑ (4.21), dyn_nvda ↓ (4.16), dyn_hdb ↑ (4.06), soybeans ↓ (3.95), rates · 3 series ↑ (3.7), dyn_rs ↑ (3.49), dyn_muthootfin_ns ↓ (3.19), midcap_largecap_ratio ↓ (3.18), indices · 2 series ↑ (2.81), dyn_tech ↑ (2.76), dyn_justdial_bo ↑ (2.65)

## India macro
- nifty_50: 23080.8008 (1d 0.36%, z20 0.64, flag none)
- nifty_midcap_100: 59148.5508 (1d -0.07%, z20 -0.69, flag none)
- usd_inr: 94.9650 (1d -0.20%, z20 -2.43, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5627 (1d -0.43%, z20 -3.18, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 116.0 — "Stock recommendations for 16 October from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 112.3 — "Stock recommendations for 16 October from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 111.4 — "Stock recommendations for 16 October from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 106.9 — "The curious case of IDBI Bank's winner Wednesdays"
- BAC (Bank of America Corporation) score 98.2 — "The curious case of IDBI Bank's winner Wednesdays"
- HDB (HDFC Bank Limited) score 91.2 — "The curious case of IDBI Bank's winner Wednesdays"
- IDBI.NS (IDBI BANK LIMITED) score 86.1 — "The curious case of IDBI Bank's winner Wednesdays"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 86.1 — "The curious case of IDBI Bank's winner Wednesdays"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 86.1 — "The curious case of IDBI Bank's winner Wednesdays"
- TECHM.NS (TECH MAHINDRA LIMITED) score 82.0 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Current Trading Status"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 79.9 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Current Trading Status"
- TECH (Bio-Techne Corp) score 79.9 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Current Trading Status"
- COIN (Coinbase Global, Inc.) score 69.6 — "Global Market: Yuan holds steady, set for third weekly gain on robust Chinese exports"
- OHI (Omega Healthcare Investors, In) score 63.6 — "With inflation rising, will Warsh keep investors guessing?"
- CHKP (Check Point Software Technolog) score 45.9 — "Bonfiglioli Transmissions IPO Day 2: GMP at 24%; Check subscription status. Should you sub"
- TGT (Target Corporation) score 45.7 — "Tech Mahindra up 7% after Q2 results, dividend, bonus shares announced- Buy, sell or hold?"
- BOND (PIMCO Active Bond Exchange-Tra) score 38.8 — "Mint Explainer| How Sebi’s changes to bonds could help NBFCs"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.6 — "BoE's Bailey says energy price pass-through remains limited, rate risks persist"
- RS (Reliance, Inc.) score 30.1 — "Top stocks to watch today: Reliance Industries, Urban Company, Wipro shares in focus on Fr"
- LTH (Life Time Group Holdings, Inc.) score 28.2 — "Goodluck India stock hits a new all-time high: is the stock worth watching?"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 27.8 — "Wipro shares rise 5%, up 15% so far in October - Should you buy this IT stock after Q2 res"
- SEPN (Septerna, Inc.) score 25.7 — "10 stocks held by 100+ MF schemes in September rally up to 205% in CY26; 6 turn multibagge"
- JIOFIN.BO (Jio Financial Services Limited) score 25.6 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Price Update"
- 301077.SZ (CHINASTARS) score 23.1 — "Global Market: China's wealthy rush to unwind offshore trusts as tax deadline looms"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.9 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Details"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.9 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Details"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 18.4 — "Bajaj Auto Share Price Live Updates: Bajaj Auto's Price and Returns Overview"
- BZ=F (Brent Crude Oil Last Day Finan) score 16.7 — "CRWV - COREWEAVE SHARES REVERSE DECLINES, LAST UP 2.7%"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.5 — "Muthoot Microfin AUM crosses ₹15,300 crore, cost of funds enters single digits"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.1 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- NVDA (NVIDIA Corporation) score 10.9 — "GERMANY PLANS MAJOR AI PARTNERSHIP WITH NVIDIA — HANDELSBLATT German Chancellor Friedrich "
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.7 — "Don’t ditch tech stocks just yet. Make these moves to take advantage of the latest AI rese"
- VT (Vanguard Total World Stock Ind) score 9.2 — "U.S. Wants World Bank to Drop Ban on Upstream Oil and Gas Funding"
- GS (Goldman Sachs Group, Inc. (The) score 9.1 — "Wipro shares rise over 2% as Q2 revenue grows 9% YoY. What are Nomura, Goldman Sachs analy"
- META (Meta) score 7.8 — "Jio IPO: Meta, Google sit on nearly ₹1 lakh crore paper profit & neither is selling"
- WIT (Wipro Limited) score 6.7 — "Wipro shares rise 5%, up 15% so far in October - Should you buy this IT stock after Q2 res"
- JEF (Jefferies Financial Group Inc.) score 6.4 — "Tech Mahindra shares jump 9% after Q2 results, Jefferies upgrades stock"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.0 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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