# Transmission Layer — board brief · 2026-11-16 12:41Z

data as of **2026-11-16** · 97 series · 13 red / 26 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.631, 4d in regime; vol-pct 0.845, breadth-off 0.417, Markov P(high-vol) 0.035)
- [WEAK] **safe_haven_gold** — corr20 -0.09, corr60 -0.21, contra nifty_50 corr20=0.25, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.12, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.35, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 -0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.37, corr60 0.32, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.476, β 0.2036, p 0.0); driver zc 2.85 → expected 0.759%. Type hit-rate 0.815 (n=2130).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.451, β 0.2339, p 0.0); driver zc 1.91 → expected 0.479%. Type hit-rate 0.815 (n=2130).
- Track record · residual_reversion: hit-rate **0.515** (n=1157) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2130) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.32] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -3.48, zc -1.08, resid-z -1.27 [quiet], 1d -0.33%, |z20|=3.48; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.86, zc -0.89, resid-z -1.13 [quiet], 1d -0.26%, |z20|=2.86; 1y-pct=2
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Boris Vujčić: Risks and resilience in the euro area financial system — ECB press, 2026-11-16. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp261116~db374b56ab.en.html
- Source: Yen steady against euro and dollar after soft Japanese GDP data — Mint Markets, 2026-11-16. https://www.livemint.com/market/yen-steady-against-euro-and-dollar-after-soft-japanese-gdp-data-11794791270301.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 6.2] rates · 2 series ↑
- tips_10y_real [RATES]: last 2.86, z20 2.37, zc 2.64, resid-z 1.60 [unexplained], 1d 2.88%, 1d move +8.0bps ≥ 5bps; |z20|=2.37; 1y-pct=95
- ust_2y [RATES]: last 4.86, z20 1.94, zc 2.85, resid-z 2.05 [unexplained], 1d 2.75%, |z20|=1.94; 1y-pct=98
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.932 vs tips_10y_real, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-05-14 (d=0.45)

### [RED 6.12] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 64044.81, z20 -2.80, zc -0.04, resid-z -1.18 [quiet], 1d -0.13%, |z20|=2.80
- eth_usd [CRYPTO]: last 1792.67, z20 -2.53, zc 0.29, resid-z -0.81 [quiet], 1d 1.33%, |z20|=2.53
- dyn_coin [EQUITIES]: last 127.64, z20 -1.63, zc -0.49, resid-z 0.21 [quiet], 1d -2.32%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.62).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.518 vs btc_usd, historically leads by 2d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.699 vs btc_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.685 vs btc_usd
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.678 vs btc_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.568 vs btc_usd
- Source: U.S. LNG Flows Hit Record High as Global Gas Supply Crisis Deepens — OilPrice, 2026-11-16. https://oilprice.com/Latest-Energy-News/World-News/US-LNG-Flows-Hit-Record-High-as-Global-Gas-Supply-Crisis-Deepens.html
- Source: Morgan Stanley raises global equities to 'maximum overweight' on cheap valuations, earnings strength — ET Markets, 2026-11-16. https://economictimes.indiatimes.com/markets/us-stocks/news/morgan-stanley-raises-global-equities-to-maximum-overweight-on-cheap-valuations-earnings-strength/articleshow/135888237.cms
- Source: Rupee rises, volatility ebbs as equity inflows blunt global headwinds — ET Markets, 2026-11-16. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-volatility-ebbs-as-equity-inflows-blunt-global-headwinds/articleshow/135883543.cms
- Historical analogues: 2026-05-22 (d=0.62), 2025-04-10 (d=0.87), 2025-10-17 (d=0.93)

### [RED 6.07] cross-asset · 4 series ↓
- comex_copper [COMMODITIES]: last 6.03, z20 -2.40, zc -0.78, resid-z -0.93 [quiet], 1d -0.89%, |z20|=2.40
- comex_silver [COMMODITIES]: last 47.56, z20 -2.04, zc -0.64, resid-z -1.40 [quiet], 1d -3.00%, |z20|=2.04; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 81.50, z20 2.00, zc n/a, resid-z n/a [quiet], 1d 2.82%, |z20|=2.00; 1y-pct=99
- comex_gold [COMMODITIES]: last 3876.10, z20 -1.92, zc 0.01, resid-z -1.00 [quiet], 1d -0.26%, |z20|=1.92; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.47 via comex_gold, z 0.85, quiet); dyn_karurvysya_ns (rho 0.425 via comex_gold, z 2.27, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.575 vs comex_copper, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.505 vs comex_copper, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.47, z 0.85); dyn_karurvysya_ns (rho 0.425, z 2.27)
- Source: Today’s Gold Rate in India November 16: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-16-2026/article71707185.ece
- Source: Today’s Gold Rate in India November 16: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-16-2026/article71707186.ece
- Source: MCX gold, silver prices drop: What led to rates slide; multi-month lows ahead of wedding season - Details for investors — Mint Markets, 2026-11-16. https://www.livemint.com/market/commodities/mcx-gold-silver-prices-drop-what-led-to-rates-slide-multi-month-lows-ahead-of-wedding-season-details-for-investors-11794801621038.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 5.66] dxy ↑
- dxy [FX]: last 103.45, z20 2.66, zc 0.63, resid-z 0.95 [quiet], 1d 0.04%, 20d range extreme; |z20|=2.66; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 5.23] dyn_kaynes_ns ↓
- dyn_kaynes_ns [EQUITIES]: last 2980.00, z20 -3.23, zc -0.54, resid-z -0.48 [quiet], 1d -13.12%, |z20|=3.23; 1y-pct=0
- **Mechanism**: dyn_kaynes_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-23 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.408 via dyn_kaynes_ns, z 0.98, quiet); nifty_metal (rho 0.381 via dyn_kaynes_ns, z 0.72, quiet); nifty_midcap_100 (rho 0.374 via dyn_kaynes_ns, z 1.48, reacted); dyn_tatatech_ns (rho 0.374 via dyn_kaynes_ns, z -0.39, quiet); nifty_fmcg (rho 0.35 via dyn_kaynes_ns, z 1.85, reacted)
- **India receivers**: dyn_jiofin_bo (rho 0.408, z 0.98); nifty_metal (rho 0.381, z 0.72); nifty_midcap_100 (rho 0.374, z 1.48); dyn_tatatech_ns (rho 0.374, z -0.39)
- Source: Amber Enterprises shares resume losing run, tank over 8% after weak Q2 from peer Kaynes Technology. Is more fall ahead? — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/amber-enterprises-shares-resume-losing-run-tank-over-8-after-weak-q2-from-peer-kaynes-technology-is-more-fall-ahead-11794813833370.html
- Source: Why Kaynes Technology shares crashed 20% to 52-week low? stock down 54% in a year | What stock market experts say — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/why-kaynes-technology-shares-crashed-20-to-52-week-low-stock-down-54-in-a-year-what-stock-market-experts-say-11794807033272.html
- Source: Kaynes Technology shares crash 12%, hit fresh 52-week low after weak Q2 results — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/stock-markets/kaynes-technology-shares-crash-12-hit-fresh-52-week-low-after-weak-q2-results/article71706984.ece
- Historical analogues: 2026-01-23 (d=0.0), 2025-01-23 (d=0.01), 2026-01-06 (d=0.02)

### [RED 4.65] indices · 4 series ↑
- ftse_100 [INDICES]: last 10946.98, z20 2.99, zc 0.57, resid-z 0.83 [quiet], 1d 0.41%, |z20|=2.99; 1y-pct=100
- cac_40 [INDICES]: last 8387.49, z20 1.76, zc 0.11, resid-z 0.28 [quiet], 1d 0.22%, |z20|=1.76
- stoxx_50 [INDICES]: last 6372.96, z20 1.64, zc -0.21, resid-z 0.00 [quiet], 1d -0.22%, |z20|=1.64
- dax [INDICES]: last 26724.80, z20 1.62, zc -0.08, resid-z 0.15 [quiet], 1d -0.09%, |z20|=1.62; 1y-pct=99
- **Mechanism**: indices · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.51 via cac_40, z 1.85, reacted); nifty_midcap_100 (rho 0.502 via dax, z 1.48, reacted); dyn_muthootfin_ns (rho 0.491 via cac_40, z 0.85, quiet); dyn_jiofin_bo (rho 0.447 via cac_40, z 0.98, quiet); dyn_tataelxsi_ns (rho 0.435 via ftse_100, z -0.78, quiet)
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.599 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.531 vs ftse_100, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.511 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_fmcg (rho 0.51, z 1.85); nifty_midcap_100 (rho 0.502, z 1.48); dyn_muthootfin_ns (rho 0.491, z 0.85); dyn_jiofin_bo (rho 0.447, z 0.98)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2026-03-31 (d=0.71)

### [AMBER 4.57] cross-asset · 2 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1110.00, z20 1.74, zc 0.08, resid-z 0.62 [quiet], 1d -0.63%, 1y-pct=97
- nifty_50 [INDICES]: last 25291.10, z20 1.66, zc -0.53, resid-z -0.92 [quiet], 1d 0.58%, |z20|=1.66
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.06).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.693 via nifty_50, z 1.48, reacted); dyn_jiofin_bo (rho 0.651 via nifty_50, z 0.98, quiet); nifty_fmcg (rho 0.636 via nifty_50, z 1.85, reacted); dyn_indusindbk_bo (rho 0.62 via dyn_bajfinance_ns, z 1.38, reacted); dyn_muthootfin_ns (rho 0.595 via nifty_50, z 0.85, quiet)
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.557 vs dyn_bajfinance_ns, historically leads by 4d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.522 vs nifty_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.507 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.573 vs nifty_50
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.554 vs dyn_bajfinance_ns
- **India receivers**: nifty_midcap_100 (rho 0.693, z 1.48); dyn_jiofin_bo (rho 0.651, z 0.98); nifty_fmcg (rho 0.636, z 1.85); dyn_indusindbk_bo (rho 0.62, z 1.38)
- Source: Morgan Stanley sees Sensex at 1.05 lakh in bull case by December 2027; base target at 95,000 — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/morgan-stanley-sees-sensex-at-105-lakh-in-bull-case-by-december-2027-base-target-at-95000/article71707830.ece
- Source: Nifty rises 147 points despite Asian sell-off; Banks, FMCG support Sensex — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/nifty-rises-147-points-despite-asian-sell-off-banks-fmcg-support-sensex/article71707780.ece
- Source: Bajaj Life Insurance launches innovation-focused equity fund under ULIP wrapper — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/bajaj-life-insurance-launches-innovation-focused-equity-fund-under-ulip-wrapper/article71707562.ece
- Historical analogues: 2025-07-18 (d=0.06), 2025-02-25 (d=0.19), 2025-02-14 (d=0.36)

## Watchlist (below surfacing floor)
dyn_nvda ↓ (4.16), usd_jpy ↑ (3.75), dyn_atherenerg_ns ↑ (3.46), dyn_schd ↑ (3.38), dyn_tech ↑ (3.15), dyn_4417_t ↑ (2.95), dyn_lth ↑ (2.88), eur_inr ↓ (2.86), ust_2s10s ↓ (2.85), aud_usd ↓ (2.83), indices · 2 series ↓ (2.58), dyn_karurvysya_ns ↑ (2.27)

## India macro
- nifty_50: 25291.0996 (1d 0.58%, z20 1.66, flag amber)
- nifty_midcap_100: 61575.5508 (1d -0.50%, z20 1.48, flag none)
- usd_inr: 93.9225 (1d -0.12%, z20 -1.45, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4347 (1d -1.07%, z20 -1.34, flag none)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 68.4 — "Commodities’ place in the Indian investor’s portfolio"
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.1 — "Commodities’ place in the Indian investor’s portfolio"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 66.0 — "Commodities’ place in the Indian investor’s portfolio"
- NVDA (NVIDIA Corporation) score 51.9 — "Nvidia Without Huang: What a Pause in AI Deals Means for Metals"
- INDIANB.NS (INDIAN BANK) score 40.7 — "Commodities’ place in the Indian investor’s portfolio"
- BAC (Bank of America Corporation) score 36.6 — "America’s Offshore Wind Industry Is Growing Despite Trump’s Crackdown"
- TECHM.NS (TECH MAHINDRA LIMITED) score 34.1 — "Tech Query: Britannia Industries, JSW Energy, Urban Company, Lemon Tree Hotels — What is t"
- HDB (HDFC Bank Limited) score 32.1 — "Retail Crowd Dump Vietnam Stocks for Near 10% Bank-Deposit Rates"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.1 — "Tech Query: Britannia Industries, JSW Energy, Urban Company, Lemon Tree Hotels — What is t"
- TECH (Bio-Techne Corp) score 32.1 — "Tech Query: Britannia Industries, JSW Energy, Urban Company, Lemon Tree Hotels — What is t"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.6 — "Retail Crowd Dump Vietnam Stocks for Near 10% Bank-Deposit Rates"
- IDBI.NS (IDBI BANK LIMITED) score 28.6 — "Retail Crowd Dump Vietnam Stocks for Near 10% Bank-Deposit Rates"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.6 — "Retail Crowd Dump Vietnam Stocks for Near 10% Bank-Deposit Rates"
- TGT (Target Corporation) score 26.9 — "Eicher Motors shares vroom like its Bullet, stock price jumps over 3%; what brokerages say"
- OHI (Omega Healthcare Investors, In) score 26.2 — "Gold edges higher as investors await Warsh remarks for rate signals"
- CHKP (Check Point Software Technolog) score 23.6 — "Today’s Gold Rate, November 14: Check Gold Rates in Delhi, Mumbai, Chennai"
- COIN (Coinbase Global, Inc.) score 22.8 — "Transparent price discovery is the missing link in global bulk commodity trade"
- 301077.SZ (CHINASTARS) score 21.4 — "As Apec looms, China’s Shenzhen wraps up preparations for its toughest stress test ever"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.5 — "US Market Outlook: Bourses get a breather"
- LTH (Life Time Group Holdings, Inc.) score 18.2 — "Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment"
- BOND (PIMCO Active Bond Exchange-Tra) score 16.2 — "Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.1 — "Top stocks to watch today: Tata Motors PV, Eicher Motors, Hindalco shares in focus on Mond"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.1 — "Top stocks to watch today: Tata Motors PV, Eicher Motors, Hindalco shares in focus on Mond"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.8 — "Bajaj Auto Share Price Highlights: Bajaj Auto Bonus"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "Jio Financial Services Share Price Highlights: Jio Financial Services Bonus"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 10.8 — "Nifty may open 75 points higher; experts flag consolidation amid global weakness"
- SCHD (Schwab US Dividend Equity ETF) score 9.7 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.5 — "Govt bonds consolidate after last week’s selloff"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.3 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.5 — "12.5 MILLION AMERICAN GAMERS PLAN TO TAKE TIME OFF FOR GTA 6 An estimated 12.5 million US "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.6 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- BLLN (BillionToOne, Inc.) score 5.3 — "Singapore Makes a $65 Billion Bet on the Future of Gold"
- GS (Goldman Sachs Group, Inc. (The) score 4.2 — "Goldman Sachs Predicts ‘Sizeable Surplus’ for Oil Market in 2027"
- CRWV (CoreWeave, Inc.) score 3.8 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- META (Meta) score 3.6 — "Nvidia Without Huang: What a Pause in AI Deals Means for Metals"
- RS (Reliance, Inc.) score 3.2 — "Reliance Industries shares rebound 15% in November, add  ₹2.38 lakh crore in market value;"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 3.0 — "Kaynes Technology shares crash 12%, hit fresh 52-week low after weak Q2 results"
- MS (Morgan Stanley) score 3.0 — "Why Morgan Stanley says it’s time to go ‘max’ overweight on stocks"
- DEMZ (Democratic Large Cap Core ETF) score 2.5 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.6 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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