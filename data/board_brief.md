# Transmission Layer — board brief · 2026-10-19 09:52Z

data as of **2026-10-19** · 97 series · 14 red / 27 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.811, 11d in regime; vol-pct 0.714, breadth-off 0.909, Markov P(high-vol) 0.048)
- [INVERTED] **safe_haven_gold** — corr20 -0.31, corr60 -0.38, contra nifty_50 corr20=0.36, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.2, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.12, corr60 0.11, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.07, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.15, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.55, corr60 0.23, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 2.3584464330372867e-06)
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.558, β 0.6401, p 0.0); driver zc -2.18 → expected -1.597%. Type hit-rate 0.812 (n=2051).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.553, β 0.637, p 0.0); driver zc -2.18 → expected -1.589%. Type hit-rate 0.812 (n=2051).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.439, β 0.1923, p 0.0); driver zc -2.18 → expected -0.48%. Type hit-rate 0.812 (n=2051).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.422, β -0.2384, p 0.0); driver zc -2.18 → expected 0.595%. Type hit-rate 0.812 (n=2051).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.409, β 0.7089, p 0.0); driver zc -2.18 → expected -1.769%. Type hit-rate 0.812 (n=2051).
- Track record · residual_reversion: hit-rate **0.502** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.812** (n=2051) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.57] commodities · 2 series ↑
- brent [COMMODITIES]: last 108.45, z20 1.77, zc -0.57, resid-z -0.33 [quiet], 1d -1.28%, |z20|=1.77
- wti [COMMODITIES]: last 98.30, z20 1.74, zc -1.22, resid-z -0.26 [quiet], 1d -3.07%, 1-session move -3.07% ≥ 1.5%; |z20|=1.74
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.613 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.574 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.564 vs brent
- Source: India's Crude Oil Import Bill Soars 46% as Middle East Crisis Drives Up Prices — OilPrice, 2026-10-19. https://oilprice.com/Latest-Energy-News/World-News/Indias-Crude-Oil-Import-Bill-Soars-46-as-Middle-East-Crisis-Drives-Up-Prices.html
- Source: Oil Prices Slip as Trump-Putin Diesel Deal Raises Supply Hopes — OilPrice, 2026-10-19. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Slip-as-Trump-Putin-Diesel-Deal-Raises-Supply-Hopes.html
- Source: India bonds to decline on elevated oil, hawkish RBI — BusinessLine Mkts, 2026-10-19. https://www.thehindubusinessline.com/markets/india-bonds-to-decline-on-elevated-oil-hawkish-rbi/article71602027.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.13] cross-asset · 4 series ↓
- nasdaq_100 [INDICES]: last 29188.64, z20 -3.46, zc -2.18, resid-z -0.68 [priced], 1d -2.50%, |z20|=3.46
- russell_2000 [INDICES]: last 2721.87, z20 -2.61, zc -1.29, resid-z -0.87 [quiet], 1d -1.64%, |z20|=2.61
- vix [INDICES]: last 18.66, z20 2.49, zc -0.55, resid-z n/a [quiet], 1d -6.65%, |z20|=2.49
- dyn_vt [EQUITIES]: last 156.81, z20 -2.46, zc -1.16, resid-z -0.35 [quiet], 1d -0.95%, |z20|=2.46
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-05-06 (z-distance 0.18).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.54 vs russell_2000, historically leads by 1d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.522 vs russell_2000, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.623 vs dyn_vt
- Source: Stock market outlook today, 19 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-16-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11792370660030.html
- Historical analogues: 2025-05-06 (d=0.18), 2025-08-18 (d=0.25), 2025-04-29 (d=0.26)

### [RED 6.73] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1774.00, z20 3.41, zc -0.30, resid-z 0.47 [quiet], 1d -0.89%, |z20|=3.41; 1y-pct=99
- nifty_it [INDICES]: last 31426.70, z20 2.50, zc -0.77, resid-z 0.07 [quiet], 1d -1.56%, |z20|=2.50
- dyn_tataelxsi_ns [EQUITIES]: last 3787.00, z20 2.42, zc -0.64, resid-z 0.24 [quiet], 1d -1.64%, |z20|=2.42
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.522 via dyn_tataelxsi_ns, z 0.09, quiet); dyn_justdial_bo (rho 0.502 via nifty_it, z 3.82, reacted); nifty_fmcg (rho 0.49 via dyn_tataelxsi_ns, z -1.52, reacted); midcap_largecap_ratio (rho -0.436 via dyn_techm_ns, z -2.75, reacted); dyn_tatatech_ns (rho 0.406 via nifty_it, z -0.49, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.518 vs nifty_it
- **India receivers**: nifty_50 (rho 0.522, z 0.09); dyn_justdial_bo (rho 0.502, z 3.82); nifty_fmcg (rho 0.49, z -1.52); midcap_largecap_ratio (rho -0.436, z -2.75)
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Source: How to trade Tech Mahindra shares after 22% rally in 4 days? Technical expert weighs in — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/stocks/news/how-to-trade-tech-mahindra-shares-after-22-rally-in-4-days-technical-expert-weighs-in/articleshow/135041900.cms
- Source: Veteran SIP investors not deterred by stagnant market: Kotak Mahindra's's Harsha Upadhyaya — Mint Markets, 2026-10-19. https://www.livemint.com/market/veteran-sip-investors-not-deterred-by-stagnant-market-kotak-mahindrass-harsha-upadhyaya-11792308340457.html
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 5.82] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 734.90, z20 3.82, zc 0.92, resid-z 1.33 [quiet], 1d 3.15%, |z20|=3.82
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.502 via dyn_justdial_bo, z 2.5, reacted); dyn_techm_ns (rho 0.496 via dyn_justdial_bo, z 3.41, reacted); nifty_50 (rho 0.443 via dyn_justdial_bo, z 0.09, quiet); dyn_tataelxsi_ns (rho 0.391 via dyn_justdial_bo, z 2.42, reacted)
- **India receivers**: nifty_it (rho 0.502, z 2.5); dyn_techm_ns (rho 0.496, z 3.41); nifty_50 (rho 0.443, z 0.09); dyn_tataelxsi_ns (rho 0.391, z 2.42)
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [RED 4.75] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7530.00, z20 2.75, zc 0.37, resid-z -0.92 [quiet], 1d 2.03%, |z20|=2.75; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Source: Tanla Platforms shares crash 6% - Experts decode future of 'long-term downtrend' | What lies ahead for CPaaS stock? — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tanla-platforms-shares-crash-6-before-trimming-losses-time-to-buy-experts-decode-11792391852511.html
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.66] dyn_wit ↑
- dyn_wit [EQUITIES]: last 1.95, z20 2.66, zc 1.11, resid-z 0.73 [quiet], 1d 4.28%, |z20|=2.66
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [RED 4.6] usd_cny ↓
- usd_cny [FX]: last 6.67, z20 -4.60, zc -3.19, resid-z -4.72 [unexplained], 1d -0.32%, |z20|=4.60; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [RED 4.56] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 72.62, z20 1.56, zc n/a, resid-z n/a [quiet], 1d -1.00%, GSR<75 (extreme low); |z20|=1.56
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.53 vs gold_silver_ratio, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
dyn_hdb ↑ (4.45), dyn_301077_sz ↓ (4.17), dyn_bac ↓ (4.08), dyn_rs ↑ (3.96), usd_inr ↓ (3.94), dyn_karurvysya_ns ↑ (3.87), dyn_dell ↓ (3.86), tips_10y_real ↓ (3.39), dyn_tech ↑ (3.22), eur_usd ↓ (2.85), midcap_largecap_ratio ↓ (2.75), dyn_nvda ↓ (2.63)

## India macro
- nifty_50: 22873.5508 (1d -1.18%, z20 0.09, flag none)
- nifty_midcap_100: 58388.1992 (1d -1.26%, z20 -1.20, flag none)
- usd_inr: 94.9050 (1d 0.40%, z20 -1.94, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5527 (1d -0.08%, z20 -2.75, flag red)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 89.0 — "Fresh debt sale set to rattle Indian bonds as rate-hike jitters persist"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.1 — "Fresh debt sale set to rattle Indian bonds as rate-hike jitters persist"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.6 — "Fresh debt sale set to rattle Indian bonds as rate-hike jitters persist"
- INDIANB.NS (INDIAN BANK) score 83.7 — "Fresh debt sale set to rattle Indian bonds as rate-hike jitters persist"
- BAC (Bank of America Corporation) score 73.8 — "Q2 Results Highlights: HDFC Bank, ICICI Bank, Axis Bank, IDBI Bank, Central Bank of India "
- HDB (HDFC Bank Limited) score 70.9 — "Q2 Results Highlights: HDFC Bank, ICICI Bank, Axis Bank, IDBI Bank, Central Bank of India "
- IDBI.NS (IDBI BANK LIMITED) score 66.8 — "Q2 Results Highlights: HDFC Bank, ICICI Bank, Axis Bank, IDBI Bank, Central Bank of India "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 66.8 — "Q2 Results Highlights: HDFC Bank, ICICI Bank, Axis Bank, IDBI Bank, Central Bank of India "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 66.8 — "Q2 Results Highlights: HDFC Bank, ICICI Bank, Axis Bank, IDBI Bank, Central Bank of India "
- TECHM.NS (TECH MAHINDRA LIMITED) score 62.3 — "Tech Query: ICICI Prudential Asset Management Company (AMC), Latent View Analytics, Rashtr"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 59.8 — "Tech Query: ICICI Prudential Asset Management Company (AMC), Latent View Analytics, Rashtr"
- TECH (Bio-Techne Corp) score 59.8 — "Tech Query: ICICI Prudential Asset Management Company (AMC), Latent View Analytics, Rashtr"
- COIN (Coinbase Global, Inc.) score 52.3 — "How commodity volatility is changing the economics of global retail expansion in India"
- OHI (Omega Healthcare Investors, In) score 42.8 — "Veteran SIP investors not deterred by stagnant market: Kotak Mahindra's's Harsha Upadhyaya"
- CHKP (Check Point Software Technolog) score 35.0 — "Today’s Gold Rate, Aug 26: Check gold rates in Delhi, Mumbai, Chennai"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.1 — "Fresh debt sale set to rattle Indian bonds as rate-hike jitters persist"
- TGT (Target Corporation) score 31.9 — "Axis Bank shares fall over 4% despite 38% YoY jump in Q2 net profit. Why brokerages are re"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 21.9 — "Hindustan Zinc share: Q2 results 2026 date today! Dividend, profit growth in focus? Expert"
- 301077.SZ (CHINASTARS) score 20.6 — "Is China’s Shenzhen ready to host Xi, Trump and Putin during Apec summit?"
- LTH (Life Time Group Holdings, Inc.) score 20.2 — "Ixigo shares rally 13% after travel platform reports all-time high profit"
- RS (Reliance, Inc.) score 19.6 — "Jio Platforms IPO GMP today: Reliance-backed  ₹30,213 cr issue - Listing gains expectation"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.3 — "Bolivia’s Energy Crisis Deepens as Natural Gas Reserves Run Dry"
- SEPN (Septerna, Inc.) score 15.4 — "Equity MF gross redemptions rise 19% in September quarter"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.7 — "Bajaj Finserv Share Price Live Updates: Bajaj Finserv's Current Trading Price"
- JIOFIN.BO (Jio Financial Services Limited) score 13.2 — "China's central bank to boost support for global investors in financial markets"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.3 — "India’s finance minister says market liquidity makes it easier for investors to exit"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.0 — "CBOE VOLATILITY INDEX JUMPS TO OVER FOUR-MONTH HIGH, LAST UP 4.97 POINTS AT 21.41"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.9 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Struggles Below Support Level"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.9 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Struggles Below Support Level"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.0 — "PC Jeweller shares soar 26% in just two sessions. Here’s what’s triggering the sharp surge"
- META (Meta) score 7.9 — "US Market: Wall Street’s AI rally faces test as Meta earnings loom"
- JEF (Jefferies Financial Group Inc.) score 7.3 — "ICICI Bank share price target after Q2 results: What are Jefferies, other analysts saying?"
- GS (Goldman Sachs Group, Inc. (The) score 6.5 — "AI debt, municipal bonds offer opportunities amid market volatility: Goldman Sachs"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- VT (Vanguard Total World Stock Ind) score 5.6 — "Imagicaaworld sells hotel, acquires water park stake, eyes indoor entertainment push"
- NVDA (NVIDIA Corporation) score 5.4 — "GERMANY PLANS MAJOR AI PARTNERSHIP WITH NVIDIA — HANDELSBLATT German Chancellor Friedrich "
- WIT (Wipro Limited) score 4.3 — "What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are "
- DELL (Dell Technologies Inc.) score 1.2 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.0 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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