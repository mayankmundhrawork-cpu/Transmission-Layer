# Transmission Layer — board brief · 2026-09-28 19:40Z

data as of **2026-09-28** · 97 series · 13 red / 32 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.669, 1d in regime; vol-pct 0.651, breadth-off 0.688, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.54, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.24, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.02, corr60 0.11, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.05, corr60 -0.1, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.11, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.5035700777074084e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2358) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.65] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.47, z20 3.04, zc 1.60, resid-z 1.52 [unexplained], 1d 1.30%, |z20|=3.04; 1y-pct=100
- tips_10y_real [RATES]: last 2.85, z20 2.72, zc 1.50, resid-z 1.81 [unexplained], 1d 3.26%, 1d move +9.0bps ≥ 5bps; |z20|=2.72; 1y-pct=100
- ust_10y [RATES]: last 5.18, z20 2.46, zc 1.29, resid-z 1.20 [quiet], 1d 1.37%, |z20|=2.46; 1y-pct=100
- dyn_bond [EQUITIES]: last 87.24, z20 -2.32, zc 0.33, resid-z -1.69 [unexplained], 1d -0.51%, |z20|=2.32; 1y-pct=0
- ust_2y [RATES]: last 4.87, z20 1.78, zc 0.30, resid-z -0.10 [quiet], 1d 0.41%, |z20|=1.78; 1y-pct=100
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.673 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.524 vs ust_30y, historically leads by 3d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.503 vs ust_10y, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.548 vs dyn_bond
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.538 vs ust_10y
- Source: US Treasury yields rise with Middle East, rate hike bets in focus — Mint Markets, 2026-09-28. https://www.livemint.com/market/us-treasury-yields-rise-with-middle-east-rate-hike-bets-in-focus-11790623392198.html
- Source: Wall St declines as oil prices, Treasury yields remain elevated — Mint Markets, 2026-09-28. https://www.livemint.com/market/wall-st-declines-as-oil-prices-treasury-yields-remain-elevated-11790621422930.html
- Source: Paramount rolls out $44 billion bond sale to fund Warner Bros. takeover — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/paramount-rolls-out-44-billion-bond-sale-to-fund-warner-bros-takeover/articleshow/134547217.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.6] hy_oas ↑
- hy_oas [RATES]: last 2.93, z20 5.60, zc 2.51, resid-z 4.08 [unexplained], 1d 4.64%, |z20|=5.60
- **Mechanism**: hy_oas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-25 (d=0.0), 2025-07-31 (d=0.01)

### [RED 7.25] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4167.20, z20 -3.93, zc 0.51, resid-z -0.40 [quiet], 1d -3.56%, |z20|=3.93; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.47, z20 -2.95, zc 0.60, resid-z 0.50 [quiet], 1d -4.32%, |z20|=2.95; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.79, z20 0.38, zc n/a, resid-z n/a [quiet], 1d 0.79%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.6 vs comex_silver, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.588 vs comex_gold
- Source: Gold tumbles 4% to seven-week low as oil, dollar and yields climb — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-tumbles-4-to-seven-week-low-as-oil-dollar-and-yields-climb/articleshow/134549139.cms
- Source: Inflows into gold ETFs continue to be positive for 10th week in a row — BusinessLine Mkts, 2026-09-28. https://www.thehindubusinessline.com/markets/gold/inflows-into-gold-etfs-continue-to-be-positive-for-10th-week-in-a-row/article71520688.ece
- Source: Gold, silver plunge up to 3% as oil surge, rate-hike bets trigger sell-off. What lies ahead? — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/stocks/news/gold-silver-plunge-up-to-3-as-oil-surge-rate-hike-bets-trigger-sell-off-what-lies-ahead/articleshow/134542705.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.78] cross-asset · 4 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1151.30, z20 -3.12, zc -0.11, resid-z -1.03 [quiet], 1d -1.26%, |z20|=3.12; 1y-pct=0
- india_vix [INDICES]: last 13.74, z20 2.62, zc -0.55, resid-z n/a [quiet], 1d 13.03%, |z20|=2.62
- nifty_midcap_100 [INDICES]: last 59913.20, z20 -2.51, zc -0.14, resid-z -1.03 [quiet], 1d -1.62%, |z20|=2.51
- nifty_50 [INDICES]: last 22780.25, z20 -2.29, zc 0.48, resid-z 0.36 [quiet], 1d -1.56%, |z20|=2.29; 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.586 via nifty_midcap_100, z -1.36, reacted); dyn_jiofin_bo (rho 0.582 via nifty_50, z -2.84, reacted); nifty_fmcg (rho 0.558 via nifty_50, z -1.07, reacted); nifty_metal (rho 0.51 via nifty_midcap_100, z -1.26, reacted); dyn_techm_ns (rho 0.495 via nifty_50, z -0.69, quiet)
- **India receivers**: midcap_largecap_ratio (rho 0.586, z -1.36); dyn_jiofin_bo (rho 0.582, z -2.84); nifty_fmcg (rho 0.558, z -1.07); nifty_metal (rho 0.51, z -1.26)
- Source: Nifty 50 breaks below 23K! Monthly expiry may keep volatility elevated | Support, resistance, outlook for Sep 29 — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/nifty-50-breaks-below-23k-monthly-expiry-may-keep-volatility-elevated-support-resistance-outlook-for-sep-29-11790611758900.html
- Source: Nifty slides to six-month low as US-Iran deal hopes fade, oil tops $100 a barrel — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/crude-oil-impact-india-stock-market-nifty-today-11790598428016.html
- Source: Market wrap: Infosys, Dr Reddy's Labs, Tata Motors PV, Power Grid top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-infosys-dr-reddys-labs-tata-motors-pv-power-grid-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/134543014.cms
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.59] brent ↓
- brent [COMMODITIES]: last 98.27, z20 -0.59, zc -0.75, resid-z -0.77 [quiet], 1d -5.80%, 1-session move -5.80% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.931 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.568 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.536 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.638 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.585 vs brent
- Source: Oil prices settle slightly higher on supply worries as Trump rejects Iran proposal — Mint Markets, 2026-09-28. https://www.livemint.com/market/oil-prices-settle-slightly-higher-on-supply-worries-as-trump-rejects-iran-proposal-11790623271537.html
- Source: Wall St declines as oil prices, Treasury yields remain elevated — Mint Markets, 2026-09-28. https://www.livemint.com/market/wall-st-declines-as-oil-prices-treasury-yields-remain-elevated-11790621422930.html
- Source: Gold tumbles 4% to seven-week low as oil, dollar and yields climb — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-tumbles-4-to-seven-week-low-as-oil-dollar-and-yields-climb/articleshow/134549139.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [RED 5.5] fx · 4 series ↓
- usd_mxn [FX]: last 17.94, z20 3.84, zc 1.72, resid-z 2.44 [unexplained], 1d 1.16%, |z20|=3.84
- aud_usd [FX]: last 0.70, z20 -2.16, zc -0.44, resid-z -0.69 [quiet], 1d 0.21%, |z20|=2.16
- eur_usd [FX]: last 1.14, z20 -2.08, zc -0.19, resid-z -0.19 [quiet], 1d -0.02%, |z20|=2.08; 1y-pct=1
- gbp_usd [FX]: last 1.33, z20 -1.92, zc -0.54, resid-z -0.67 [quiet], 1d 0.35%, |z20|=1.92
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.49 via usd_mxn, z -3.12, reacted); dyn_icicigi_bo (rho -0.485 via gbp_usd, z 0.91, quiet); dyn_muthootfin_ns (rho 0.459 via aud_usd, z -1.43, reacted); dyn_inoxindia_ns (rho 0.415 via aud_usd, z -1.1, reacted); nifty_50 (rho 0.374 via eur_usd, z -2.29, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.552 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_policybzr_ns (rho -0.49, z -3.12); dyn_icicigi_bo (rho -0.485, z 0.91); dyn_muthootfin_ns (rho 0.459, z -1.43); dyn_inoxindia_ns (rho 0.415, z -1.1)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.27] dyn_chkp ↓
- dyn_chkp [EQUITIES]: last 129.27, z20 -2.27, zc -1.60, resid-z -1.26 [moved], 1d -1.50%, |z20|=2.27
- **Mechanism**: dyn_chkp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.351 via dyn_chkp, z -1.56, reacted)
- **India receivers**: dyn_tatatech_ns (rho 0.351, z -1.56)
- Source: 4 Adani group companies settle public shareholding violations case with Sebi. Check details — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/stocks/news/4-adani-group-companies-settle-public-shareholding-violations-case-with-sebi-check-details/articleshow/134547647.cms
- Source: Top 2 stocks to buy or sell tomorrow: Laurus Labs, Indus Towers by Chandan Taparia - Check stop-loss, targets — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/top-2-stocks-to-buy-or-sell-tomorrow-laurus-labs-indus-towers-by-chandan-taparia-check-stop-loss-targets-11790594465913.html
- Source: BSE stock falls 2.3% as SEBI mulls self-listing rules revamp, days after NSE IPO listing - Check details — Mint Markets, 2026-09-28. https://www.livemint.com/market/bse-stock-falls-2-3-as-sebi-mulls-self-listing-rules-revamp-days-after-nse-ipo-listing-check-details-11790585815691.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 3.82] natgas ↑
- natgas [COMMODITIES]: last 3.15, z20 1.82, zc -0.62, resid-z -1.20 [quiet], 1d -1.35%, |z20|=1.82
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.432 via natgas, z -3.12, reacted)
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.124 vs natgas, historically leads by 4d
- **India receivers**: dyn_policybzr_ns (rho -0.432, z -3.12)
- Source: High Freight Costs Push More U.S. LNG Toward Europe — OilPrice, 2026-09-28. https://oilprice.com/Latest-Energy-News/World-News/High-Freight-Costs-Push-More-US-LNG-Toward-Europe.html
- Source: Qatar Extends LNG Force Majeure as Hormuz Crisis Drags On — OilPrice, 2026-09-28. https://oilprice.com/Latest-Energy-News/World-News/Qatar-Extends-LNG-Force-Majeure-as-Hormuz-Crisis-Drags-On.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
dyn_nvda ↑ (3.22), dyn_4417_t ↑ (3.17), dyn_tech ↑ (3.17), shanghai_comp ↓ (3.13), dyn_havells_ns ↓ (3.0), dyn_hdb ↓ (2.91), dyn_jiofin_bo ↓ (2.84), usd_brl ↑ (2.75), dyn_indianb_ns ↓ (2.7), dyn_indusindbk_bo ↓ (2.41), dyn_atherenerg_ns ↓ (2.2), dyn_ms ↓ (2.06)

## India macro
- nifty_50: 22780.2500 (1d -1.56%, z20 -2.29, flag amber)
- nifty_midcap_100: 59913.1992 (1d -1.62%, z20 -2.51, flag red)
- usd_inr: 95.9730 (1d -0.20%, z20 1.06, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6301 (1d -0.07%, z20 -1.36, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 66.2 — "India’s IPO pipeline surges to ₹3.86 lakh crore as companies tap public markets"
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.6 — "India’s IPO pipeline surges to ₹3.86 lakh crore as companies tap public markets"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 64.4 — "India’s IPO pipeline surges to ₹3.86 lakh crore as companies tap public markets"
- INDIANB.NS (INDIAN BANK) score 43.3 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- COIN (Coinbase Global, Inc.) score 42.9 — "Should you consider global stocks as Nifty struggles to give returns? Key factors behind p"
- OHI (Omega Healthcare Investors, In) score 34.2 — "Top stocks in focus today: Investors must watch HCL Tech, NCC, IRFC, Power Mech shares on "
- CHKP (Check Point Software Technolog) score 34.1 — "Top 2 stocks to buy or sell tomorrow: Laurus Labs, Indus Towers by Chandan Taparia - Check"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.7 — "TRUMP REJECTS AI INTEGRATION WITH CHINA President Trump said the U.S. should not integrate"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.7 — "TRUMP REJECTS AI INTEGRATION WITH CHINA President Trump said the U.S. should not integrate"
- TECH (Bio-Techne Corp) score 32.7 — "TRUMP REJECTS AI INTEGRATION WITH CHINA President Trump said the U.S. should not integrate"
- HDB (HDFC Bank Limited) score 32.3 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- BAC (Bank of America Corporation) score 30.4 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- 301077.SZ (CHINASTARS) score 28.8 — "TRUMP REJECTS AI INTEGRATION WITH CHINA President Trump said the U.S. should not integrate"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.6 — "CleanMax raises ₹2,500 crore via Green Bonds"
- IDBI.NS (IDBI BANK LIMITED) score 27.3 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 27.3 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 27.3 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- LTH (Life Time Group Holdings, Inc.) score 25.0 — "RBI completes 1 trillion rupee net debt sale for first time in a decade"
- SEPN (Septerna, Inc.) score 24.4 — "Stock market prediction for today: Sensex, Nifty outlook for Tuesday | Kospi, Taiwan cues "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.8 — "TRUMP REJECTS AI INTEGRATION WITH CHINA President Trump said the U.S. should not integrate"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.0 — "SAT disposes of appeals by five Adani-linked FPIs after SEBI agrees to share file noting"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.7 — "Market wrap: Infosys, Dr Reddy's Labs, Tata Motors PV, Power Grid top gainers and losers o"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.7 — "Market wrap: Infosys, Dr Reddy's Labs, Tata Motors PV, Power Grid top gainers and losers o"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.1 — "Global Gas Squeeze Could Last Through Next Summer"
- JIOFIN.BO (Jio Financial Services Limited) score 10.5 — "Spending $800 to see my family this Thanksgiving is a financial burden. How can I push for"
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.6 — "PB Fintech: the risk was known. Investors chased the stock anyway"
- META (Meta) score 9.2 — "MongoDB’s stock is down nearly 20% as CEO decamps to Meta"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.7 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 6.7 — "IPO frenzy attracts FPIs, even as stock selling hits  ₹25,682 crore in September: Will tre"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.5 — "The Next Global Energy Crisis Won’t Come From Just One Direction"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.6 — "JAPANESE, US FINANCE CHIEFS DISCUSS YEN DEPRECIATION: KYODO"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.5 — "ETMarkets Smart Talk| F&O STT, UPI charges and trading costs: Sandeep Neema on the hidden "
- GS (Goldman Sachs Group, Inc. (The) score 5.2 — "Clean Max Enviro bulk deal: Augment India divests stakes worth Rs 1,096 crore; Goldman Sac"
- MS (Morgan Stanley) score 4.4 — "‘We were wrong.’ Why Morgan Stanley changed its tune on the U.S. dollar — and what it expe"
- VT (Vanguard Total World Stock Ind) score 3.7 — "Beyond high-profile wars, a worldwide battle for critical minerals"
- NVDA (NVIDIA Corporation) score 3.0 — "Nvidia approves record $150 billion share buyback plan as AI boom powers cash generation"
- MU (Micron Technology, Inc.) score 2.4 — "Micron has a chance to set the record straight with its earnings report"
- MSFT (Microsoft Corporation) score 1.6 — "Wall Street ends higher as investors buy AI stocks; Microsoft rallies"
- VOLTAS.NS (VOLTAS LTD) score 0.7 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.4 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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