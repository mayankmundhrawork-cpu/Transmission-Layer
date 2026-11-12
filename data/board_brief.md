# Transmission Layer — board brief · 2026-11-12 12:37Z

data as of **2026-11-12** · 97 series · 12 red / 33 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.572, 1d in regime; vol-pct 0.728, breadth-off 0.417, Markov P(high-vol) 0.206)
- [INVERTED] **safe_haven_gold** — corr20 -0.1, corr60 -0.2, contra nifty_50 corr20=0.29, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.12, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.32, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.508** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2147) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.83] cross-asset · 6 series ↑
- dyn_indusindbk_bo [EQUITIES]: last 930.00, z20 2.68, zc 0.94, resid-z 1.73 [unexplained], 1d 2.99%, |z20|=2.68
- dyn_bajfinance_ns [EQUITIES]: last 1115.00, z20 2.55, zc 1.59, resid-z 1.53 [unexplained], 1d 3.36%, |z20|=2.55; 1y-pct=98
- nifty_midcap_100 [INDICES]: last 62037.10, z20 2.22, zc 0.72, resid-z 1.18 [quiet], 1d 0.85%, |z20|=2.22
- nifty_50 [INDICES]: last 25299.35, z20 2.19, zc 0.14, resid-z 2.78 [unexplained], 1d 0.18%, |z20|=2.19
- dyn_muthootfin_ns [EQUITIES]: last 2932.90, z20 2.02, zc 0.36, resid-z 0.27 [quiet], 1d 1.13%, |z20|=2.02
- nifty_metal [INDICES]: last 12771.65, z20 1.89, zc -0.08, resid-z -0.13 [quiet], 1d -0.11%, |z20|=1.89
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 1.27).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.823 via nifty_midcap_100, z 1.79, reacted); dyn_adanient_bo (rho 0.746 via nifty_metal, z 1.24, reacted); nifty_fmcg (rho 0.642 via nifty_midcap_100, z 1.56, reacted); dyn_indianb_ns (rho 0.618 via nifty_midcap_100, z 2.82, reacted); dyn_tatatech_ns (rho 0.556 via dyn_indusindbk_bo, z 0.07, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.51 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.504 vs nifty_50, historically leads by 5d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.556 vs dyn_indusindbk_bo
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.526 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.823, z 1.79); dyn_adanient_bo (rho 0.746, z 1.24); nifty_fmcg (rho 0.642, z 1.56); dyn_indianb_ns (rho 0.618, z 2.82)
- Source: Sensex today | Stock Market Highlights: Markets extend gains for 3rd day; Sensex ends above 81,900 on FII inflows, lower crude oil — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-12-november-2026/article71689385.ece
- Source: Nifty target at 26,200 as BofA tweaks India strategy; upgrades hospitals, telecom, downgrades two-wheelers — Mint Markets, 2026-11-12. https://www.livemint.com/market/stock-market-news/nifty-target-at-26-200-as-bofa-tweaks-india-strategy-upgrades-hospitals-telecom-downgrades-twowheelers-11794474956038.html
- Source: Financial stocks hold Nifty steady at midday; Auto, FMCG drag — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/financial-stocks-hold-nifty-steady-at-midday-auto-fmcg-drag/article71692751.ece
- Historical analogues: 2025-07-18 (d=1.27), 2025-05-30 (d=1.4), 2025-12-19 (d=1.41)

### [RED 6.32] fx · 2 series ↓
- eur_usd [FX]: last 1.11, z20 -3.49, zc -2.10, resid-z -2.42 [unexplained], 1d -0.73%, |z20|=3.49; 1y-pct=0
- gbp_usd [FX]: last 1.33, z20 -1.76, zc -1.77, resid-z -2.17 [unexplained], 1d -0.65%, |z20|=1.76
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Sterling drops against firmer dollar as markets price in a hawkish Fed — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-drops-against-firmer-dollar-as-markets-price-in-a-hawkish-fed/articleshow/135738659.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 6.06] dxy ↑
- dxy [FX]: last 102.92, z20 3.06, zc 0.04, resid-z 2.61 [unexplained], 1d 0.01%, 20d range extreme; |z20|=3.06; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.577 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [AMBER 5.62] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2020.59, z20 -2.30, zc -0.45, resid-z 0.19 [quiet], 1d -1.72%, |z20|=2.30
- btc_usd [CRYPTO]: last 72857.99, z20 -1.90, zc -0.67, resid-z -0.27 [quiet], 1d -1.50%, |z20|=1.90
- dyn_coin [EQUITIES]: last 136.31, z20 -1.33, zc 0.66, resid-z 0.35 [quiet], 1d 3.16%, 1y-pct=1
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.18).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.738 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.536 vs eth_usd, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.695 vs eth_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.664 vs eth_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.58 vs eth_usd
- Source: China Targets Global Gas Turbine Market as AI Power Demand Explodes — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/China-Targets-Global-Gas-Turbine-Market-as-AI-Power-Demand-Explodes.html
- Source: Bitcoin slips below $74,000 mark, experts explain the factors influencing the cryptocurrency this week — Mint Markets, 2026-11-12. https://www.livemint.com/market/cryptocurrency/bitcoin-slips-below-74000-mark-experts-explain-factors-influence-cryptocurrency-markets-week-us-inflation-risk-investors-11794473906813.html
- Source: Global Market Today: Asian stocks mixed as Nvidia turmoil hits AI-linked shares — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-us-stock-futures-fall-as-nvidia-turmoil-deepens/articleshow/135751953.cms
- Historical analogues: 2026-05-22 (d=0.18), 2025-04-10 (d=0.47), 2025-10-16 (d=0.61)

### [RED 5.42] usd_jpy ↑
- usd_jpy [FX]: last 159.70, z20 3.42, zc 1.25, resid-z 1.20 [quiet], 1d 0.63%, |z20|=3.42
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.411 via usd_jpy, z 0.1, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.411, z 0.1)
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [AMBER 4.62] commodities · 2 series ↓
- wti [COMMODITIES]: last 85.80, z20 -1.78, zc -0.29, resid-z 1.09 [quiet], 1d -0.84%, |z20|=1.78
- brent [COMMODITIES]: last 92.16, z20 -1.64, zc -0.22, resid-z 1.43 [quiet], 1d -0.65%, |z20|=1.64; co-occur[inr_oil] suppressed: channel INVERTED
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.505 via wti, z 2.02, reacted); nifty_midcap_100 (rho -0.467 via wti, z 2.22, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.545 vs brent, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.609 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.559 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.501 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.505, z 2.02); nifty_midcap_100 (rho -0.467, z 2.22)
- Source: Nigeria Hits OPEC Oil Production Quota for Sixth Straight Month — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/Nigeria-Hits-OPEC-Oil-Production-Quota-for-Sixth-Straight-Month.html
- Source: India Boosts Gulf Oil Imports as Russian Crude Loses Its Price Advantage — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/India-Boosts-Gulf-Oil-Imports-as-Russian-Crude-Loses-Its-Price-Advantage.html
- Source: Sensex today | Stock Market Highlights: Markets extend gains for 3rd day; Sensex ends above 81,900 on FII inflows, lower crude oil — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-12-november-2026/article71689385.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 4.44] indices · 4 series ↑
- stoxx_50 [INDICES]: last 6407.81, z20 2.77, zc 0.23, resid-z 1.01 [quiet], 1d 0.23%, |z20|=2.77
- dax [INDICES]: last 26854.54, z20 2.50, zc 0.63, resid-z 1.77 [unexplained], 1d 0.72%, |z20|=2.50; 1y-pct=100
- cac_40 [INDICES]: last 8384.65, z20 2.34, zc 0.73, resid-z 1.28 [quiet], 1d 0.62%, |z20|=2.34
- ftse_100 [INDICES]: last 10873.20, z20 2.00, zc 0.47, resid-z 2.03 [unexplained], 1d 0.35%, |z20|=2.00; 1y-pct=96
- **Mechanism**: indices · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.507 via cac_40, z 2.02, reacted); nifty_midcap_100 (rho 0.506 via dax, z 2.22, reacted); nifty_fmcg (rho 0.481 via cac_40, z 1.56, reacted); dyn_jiofin_bo (rho 0.45 via cac_40, z 1.79, reacted); dyn_tataelxsi_ns (rho 0.445 via ftse_100, z 0.87, quiet)
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.524 vs stoxx_50, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.514 vs stoxx_50, historically leads by 2d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.507 vs dax, historically leads by 1d
- **India receivers**: dyn_muthootfin_ns (rho 0.507, z 2.02); nifty_midcap_100 (rho 0.506, z 2.22); nifty_fmcg (rho 0.481, z 1.56); dyn_jiofin_bo (rho 0.45, z 1.79)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2026-03-31 (d=0.71)

### [RED 4.34] commodities · 2 series ↓
- comex_gold [COMMODITIES]: last 3949.70, z20 -1.51, zc -0.76, resid-z 0.26 [quiet], 1d -1.27%, |z20|=1.51; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 50.99, z20 -0.97, zc -0.61, resid-z 0.44 [quiet], 1d -1.71%, 1y-pct=4; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.514 via comex_gold, z 2.02, reacted); dyn_karurvysya_ns (rho 0.422 via comex_gold, z 2.15, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.526 vs comex_gold
- **India receivers**: dyn_muthootfin_ns (rho 0.514, z 2.02); dyn_karurvysya_ns (rho 0.422, z 2.15)
- Source: Today’s Gold Rate in India November 12: Gold prices down in Delhi, Mumbai, Kolkata, Chennai and Bengaluru — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-12-2026/article71692844.ece
- Source: What's gold price future in India? Will it touch  ₹1.50 lakh per 10 grams again by December 2026? Experts' view — Mint Markets, 2026-11-12. https://www.livemint.com/market/commodities/whats-gold-price-future-in-india-will-it-touch-1-50-lakh-per-10-grams-again-by-december-2026-experts-view-11794468408702.html
- Source: How are ITC shares performing after Gold Flake Regular price hike by  ₹10 per pack? Should you buy stock? Experts views — Mint Markets, 2026-11-12. https://www.livemint.com/market/stock-market-news/how-are-itc-shares-performing-after-gold-flake-regular-price-hike-by-rs-10-per-pack-should-you-buy-stock-experts-views-11794458280381.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-15 (d=0.09), 2026-05-15 (d=0.16)

## Watchlist (below surfacing floor)
dyn_nvda ↓ (4.15), dyn_hdb ↑ (4.09), comex_copper ↓ (3.78), natgas ↑ (3.77), usd_inr ↓ (3.61), dyn_tech ↑ (3.48), dyn_lth ↑ (3.46), dyn_schd ↑ (3.31), eur_inr ↓ (3.1), dyn_4417_t ↑ (2.93), dyn_indianb_ns ↑ (2.82), aud_usd ↓ (2.53)

## India macro
- nifty_50: 25299.3496 (1d 0.18%, z20 2.19, flag amber)
- nifty_midcap_100: 62037.1016 (1d 0.85%, z20 2.22, flag amber)
- usd_inr: 94.0400 (1d 0.12%, z20 -1.61, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4521 (1d 0.67%, z20 -0.99, flag none)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.2 — "Flattish opening seen for Indian stocks; markets eye release of inflation data"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.9 — "Flattish opening seen for Indian stocks; markets eye release of inflation data"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 82.7 — "Flattish opening seen for Indian stocks; markets eye release of inflation data"
- NVDA (NVIDIA Corporation) score 58.3 — "Nvidia shares plummet 10% in after-hours trade as investors consider a future without Huan"
- INDIANB.NS (INDIAN BANK) score 57.8 — "Flattish opening seen for Indian stocks; markets eye release of inflation data"
- BAC (Bank of America Corporation) score 48.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Market Performance"
- TGT (Target Corporation) score 45.4 — "Tata Power shares rise 2% after Q2 results. Why brokerages are bullish despite target pric"
- HDB (HDFC Bank Limited) score 42.3 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Market Performance"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.9 — "HCL Tech Share Price Live Updates: HCL Tech's stock price settles at Rs 1380.8 today"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Market Performance"
- IDBI.NS (IDBI BANK LIMITED) score 38.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Market Performance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Market Performance"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.4 — "HCL Tech Share Price Live Updates: HCL Tech's stock price settles at Rs 1380.8 today"
- TECH (Bio-Techne Corp) score 38.4 — "HCL Tech Share Price Live Updates: HCL Tech's stock price settles at Rs 1380.8 today"
- 301077.SZ (CHINASTARS) score 33.7 — "China Targets Global Gas Turbine Market as AI Power Demand Explodes"
- CHKP (Check Point Software Technolog) score 31.1 — "Sensex Expiry Today Prediction 12 November Thursday: What should be your trading strategy?"
- OHI (Omega Healthcare Investors, In) score 29.5 — "Nvidia shares plummet 10% in after-hours trade as investors consider a future without Huan"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 24.7 — "Bajaj Auto Share Price Live Updates: Bajaj Auto's Current Trading Status"
- COIN (Coinbase Global, Inc.) score 23.4 — "China Targets Global Gas Turbine Market as AI Power Demand Explodes"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.5 — "Clean Max Enviro Energy shares jump 7%; stock trades 27% above IPO price — What’s driving "
- LTH (Life Time Group Holdings, Inc.) score 21.1 — "Maritime PSU face-off: SCI vs GRSE - Which PSU stock to buy after Q2 results? Profit, divi"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.0 — "India bonds to stay hemmed in by oil, Treasury moves ahead of inflation data"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.8 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Stock Details"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.1 — "Tata Consumer Share Price Live Updates: Tata Consumer Market Movement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.1 — "Tata Consumer Share Price Live Updates: Tata Consumer Market Movement"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.5 — "How are ITC shares performing after Gold Flake Regular price hike by  ₹10 per pack? Should"
- SCHD (Schwab US Dividend Equity ETF) score 13.4 — "Maritime PSU face-off: SCI vs GRSE - Which PSU stock to buy after Q2 results? Profit, divi"
- JIOFIN.BO (Jio Financial Services Limited) score 11.3 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Market Performance"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.2 — "Up in 8 of last 10 sessions, HDFC Bank share price jumps 22% in this period - Why should y"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.2 — "Buzzing stocks: Bajaj Finance, Tata Power, Adani Enterprises, Sandur Manganese, Alivus Lif"
- CRWV (CoreWeave, Inc.) score 9.5 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.3 — "Nuvama Wealth share price: Brokerage stock up over 6% today, just 5% away from peak on str"
- RS (Reliance, Inc.) score 5.5 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- JEF (Jefferies Financial Group Inc.) score 5.5 — "FIIs are back! Jefferies lists 11 stocks that can be the biggest beneficiaries"
- META (Meta) score 5.4 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- DEMZ (Democratic Large Cap Core ETF) score 5.1 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- GS (Goldman Sachs Group, Inc. (The) score 4.2 — "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast"
- SEPN (Septerna, Inc.) score 3.0 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.1 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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