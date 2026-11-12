# Transmission Layer — board brief · 2026-11-12 21:28Z

data as of **2026-11-12** · 96 series · 12 red / 32 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.629, 2d in regime; vol-pct 0.728, breadth-off 0.529, Markov P(high-vol) 0.075)
- [INVERTED] **safe_haven_gold** — corr20 -0.11, corr60 -0.21, contra nifty_50 corr20=0.28, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.12, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.26, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.2, corr60 -0.0, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.17, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 88** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.507** (n=1141) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2148) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.3] fx · 2 series ↓
- eur_usd [FX]: last 1.11, z20 -4.46, zc -2.89, resid-z -3.17 [unexplained], 1d -1.00%, |z20|=4.46; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.19, zc -2.30, resid-z -2.54 [unexplained], 1d -0.84%, |z20|=2.19
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.046 vs eur_usd, historically leads by 1d
- Source: Sterling drops against firmer dollar as markets price in a hawkish Fed — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-drops-against-firmer-dollar-as-markets-price-in-a-hawkish-fed/articleshow/135738659.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 7.11] commodities · 2 series ↓
- wti [COMMODITIES]: last 88.92, z20 -1.28, zc 0.95, resid-z 0.77 [quiet], 1d 2.76%, 1-session move +2.76% ≥ 1.5%
- brent [COMMODITIES]: last 96.05, z20 -1.19, zc 1.19, resid-z 1.03 [quiet], 1d 3.55%, 1-session move +3.55% ≥ 1.5%; co-occur[inr_oil] suppressed: channel INVERTED
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.486 via wti, z 2.02, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.55 vs brent, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.602 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.597 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.549 vs brent
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.54 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.486, z 2.02)
- Source: $7 Billion in Oil Debt Has Nigerian Banks Holding Back Lending — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/7-Billion-in-Oil-Debt-Has-Nigerian-Banks-Holding-Back-Lending.html
- Source: EIA Data Shows Builds in Crude, Gasoline and Distillates — OilPrice, 2026-11-12. https://oilprice.com/Energy/Crude-Oil/EIA-Data-Shows-Builds-in-Crude-Gasoline-and-Distillates.html
- Source: Brent Briefly Hits $96 After Trump Says U.S. Has No Need for Iran Deal — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/Brent-Briefly-Hits-94-After-Trump-Says-US-Has-No-Need-for-Iran-Deal.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.86] dxy ↑
- dxy [FX]: last 103.18, z20 3.86, zc 0.71, resid-z 0.95 [quiet], 1d 0.26%, 20d range extreme; |z20|=3.86; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.504 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 6.83] cross-asset · 6 series ↑
- dyn_indusindbk_bo [EQUITIES]: last 930.00, z20 2.68, zc 0.94, resid-z 1.88 [unexplained], 1d 2.99%, |z20|=2.68
- dyn_bajfinance_ns [EQUITIES]: last 1115.00, z20 2.55, zc 1.59, resid-z 1.41 [moved], 1d 3.36%, |z20|=2.55; 1y-pct=98
- nifty_midcap_100 [INDICES]: last 62037.10, z20 2.22, zc 0.72, resid-z 1.23 [quiet], 1d 0.85%, |z20|=2.22
- nifty_50 [INDICES]: last 25299.35, z20 2.19, zc 0.14, resid-z 0.19 [quiet], 1d 0.18%, |z20|=2.19
- dyn_muthootfin_ns [EQUITIES]: last 2932.90, z20 2.02, zc 0.36, resid-z 0.76 [quiet], 1d 1.13%, |z20|=2.02
- nifty_metal [INDICES]: last 12771.65, z20 1.89, zc -0.08, resid-z -0.09 [quiet], 1d -0.11%, |z20|=1.89
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 1.27).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.823 via nifty_midcap_100, z 1.79, reacted); dyn_adanient_bo (rho 0.746 via nifty_metal, z 1.24, reacted); nifty_fmcg (rho 0.642 via nifty_midcap_100, z 1.56, reacted); dyn_indianb_ns (rho 0.618 via nifty_midcap_100, z 2.82, reacted); dyn_tatatech_ns (rho 0.556 via dyn_indusindbk_bo, z 0.07, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.51 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.504 vs nifty_50, historically leads by 5d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.556 vs dyn_indusindbk_bo
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.526 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.823, z 1.79); dyn_adanient_bo (rho 0.746, z 1.24); nifty_fmcg (rho 0.642, z 1.56); dyn_indianb_ns (rho 0.618, z 2.82)
- Source: Muthoot FinCorp diversifies funding to trim borrowing cost — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/muthoot-fincorp-diversifies-funding-to-trim-borrowing-cost/article71695055.ece
- Source: Sensex, Nifty pause for breath; Realty surges as rupee slips on dollar buying — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty-today-markets-pause-for-breath-realty-surges-as-rupee-slips-on-dollar-buying/article71693764.ece
- Source: Sensex today | Stock Market Highlights: Markets extend gains for 3rd day; Sensex ends above 81,900 on FII inflows, lower crude oil — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-12-november-2026/article71689385.ece
- Historical analogues: 2025-07-18 (d=1.27), 2025-05-30 (d=1.4), 2025-12-19 (d=1.41)

### [RED 5.73] usd_jpy ↑
- usd_jpy [FX]: last 159.87, z20 3.73, zc 1.45, resid-z 1.73 [unexplained], 1d 0.73%, |z20|=3.73
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.412 via usd_jpy, z 0.1, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.412, z 0.1)
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [AMBER 5.65] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 71545.93, z20 -2.33, zc -1.47, resid-z -1.28 [quiet], 1d -3.27%, |z20|=2.33
- eth_usd [CRYPTO]: last 2018.85, z20 -2.32, zc -0.47, resid-z -0.20 [quiet], 1d -1.80%, |z20|=2.32
- dyn_coin [EQUITIES]: last 130.62, z20 -1.56, zc -0.88, resid-z 0.21 [quiet], 1d -4.15%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.38).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.546 vs btc_usd, historically leads by 2d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.735 vs btc_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.727 vs btc_usd
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.713 vs btc_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.616 vs btc_usd
- Source: UK Vows Global Climate Leadership as PM Doubles Down on Net Zero — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/UK-Vows-Global-Climate-Leadership-as-PM-Doubles-Down-on-Net-Zero.html
- Source: Standard Chartered launches four global investment funds from GIFT City — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/standard-chartered-launches-four-global-investment-funds-from-gift-city/article71693748.ece
- Source: China Targets Global Gas Turbine Market as AI Power Demand Explodes — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/China-Targets-Global-Gas-Turbine-Market-as-AI-Power-Demand-Explodes.html
- Historical analogues: 2026-05-22 (d=0.38), 2025-04-10 (d=0.63), 2025-10-16 (d=0.7)

### [RED 5.29] commodities · 2 series ↓
- comex_gold [COMMODITIES]: last 3878.00, z20 -2.46, zc -1.82, resid-z -1.00 [moved], 1d -3.06%, |z20|=2.46; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 49.92, z20 -1.39, zc -1.34, resid-z 0.97 [quiet], 1d -3.77%, 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.474 via comex_gold, z 2.02, reacted); dyn_karurvysya_ns (rho 0.424 via comex_gold, z 2.15, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.513 vs comex_gold
- **India receivers**: dyn_muthootfin_ns (rho 0.474, z 2.02); dyn_karurvysya_ns (rho 0.424, z 2.15)
- Source: Gold drops to over one-year low as fading Middle East peace hopes fan inflation fears — Mint Markets, 2026-11-12. https://www.livemint.com/market/gold-drops-to-over-one-year-low-as-fading-middle-east-peace-hopes-fan-inflation-fears-11794511222562.html
- Source: Today’s Gold Rate in India November 12: Gold prices down in Delhi, Mumbai, Kolkata, Chennai and Bengaluru — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-12-2026/article71692844.ece
- Source: What's gold price future in India? Will it touch  ₹1.50 lakh per 10 grams again by December 2026? Experts' view — Mint Markets, 2026-11-12. https://www.livemint.com/market/commodities/whats-gold-price-future-in-india-will-it-touch-1-50-lakh-per-10-grams-again-by-december-2026-experts-view-11794468408702.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-15 (d=0.09), 2026-05-15 (d=0.16)

### [RED 4.46] indices · 4 series ↑
- stoxx_50 [INDICES]: last 6409.74, z20 2.80, zc 0.26, resid-z 0.84 [quiet], 1d 0.26%, |z20|=2.80
- dax [INDICES]: last 26816.59, z20 2.41, zc 0.51, resid-z 1.33 [quiet], 1d 0.58%, |z20|=2.41; 1y-pct=100
- cac_40 [INDICES]: last 8372.71, z20 2.26, zc 0.56, resid-z 1.17 [quiet], 1d 0.48%, |z20|=2.26
- ftse_100 [INDICES]: last 10867.29, z20 1.91, zc 0.40, resid-z 0.98 [quiet], 1d 0.29%, |z20|=1.91
- **Mechanism**: indices · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.506 via cac_40, z 2.02, reacted); nifty_midcap_100 (rho 0.504 via dax, z 2.22, reacted); nifty_fmcg (rho 0.485 via cac_40, z 1.56, reacted); dyn_jiofin_bo (rho 0.45 via cac_40, z 1.79, reacted); dyn_tataelxsi_ns (rho 0.445 via ftse_100, z 0.87, quiet)
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.596 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.516 vs stoxx_50, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.514 vs stoxx_50, historically leads by 2d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.504 vs dax, historically leads by 1d
- **India receivers**: dyn_muthootfin_ns (rho 0.506, z 2.02); nifty_midcap_100 (rho 0.504, z 2.22); nifty_fmcg (rho 0.485, z 1.56); dyn_jiofin_bo (rho 0.45, z 1.79)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2026-03-31 (d=0.71)

## Watchlist (below surfacing floor)
dyn_nvda ↓ (4.34), natgas ↑ (4.12), tips_10y_real ↑ (4.06), comex_copper ↓ (3.99), dyn_tech ↑ (3.87), eur_inr ↓ (3.85), usd_inr ↓ (3.62), dyn_schd ↑ (3.09), dyn_4417_t ↑ (2.93), ust_2s10s ↓ (2.92), aud_usd ↓ (2.88), dyn_indianb_ns ↑ (2.82)

## India macro
- nifty_50: 25299.3496 (1d 0.18%, z20 2.19, flag amber)
- nifty_midcap_100: 62037.1016 (1d 0.85%, z20 2.22, flag amber)
- usd_inr: 94.0330 (1d 0.11%, z20 -1.62, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4521 (1d 0.67%, z20 -0.99, flag none)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.2 — "India bonds track Treasury weakness ahead of debt supply"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.1 — "India bonds track Treasury weakness ahead of debt supply"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.9 — "India bonds track Treasury weakness ahead of debt supply"
- NVDA (NVIDIA Corporation) score 66.5 — "NVDA - INVESTORS RUSH TO BUY NVIDIA DIP DESPITE CEO CRISIS Nearly 90% of Nvidia trades by "
- INDIANB.NS (INDIAN BANK) score 59.0 — "Punjab National Bank among 4 stocks hitting 52-week highs; rally up to 22% in a month"
- BAC (Bank of America Corporation) score 52.6 — "Punjab National Bank among 4 stocks hitting 52-week highs; rally up to 22% in a month"
- HDB (HDFC Bank Limited) score 44.8 — "Punjab National Bank among 4 stocks hitting 52-week highs; rally up to 22% in a month"
- TGT (Target Corporation) score 41.7 — "Tata Power shares rise 2% after Q2 results. Why brokerages are bullish despite target pric"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.5 — "Punjab National Bank among 4 stocks hitting 52-week highs; rally up to 22% in a month"
- IDBI.NS (IDBI BANK LIMITED) score 41.5 — "Punjab National Bank among 4 stocks hitting 52-week highs; rally up to 22% in a month"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.5 — "Punjab National Bank among 4 stocks hitting 52-week highs; rally up to 22% in a month"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.6 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.3 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- TECH (Bio-Techne Corp) score 36.3 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- 301077.SZ (CHINASTARS) score 31.9 — "Trafigura Is Key Player in LME Aluminum Squeeze With China Trade"
- CHKP (Check Point Software Technolog) score 31.5 — "Oil India dividend, Q2 results 2026: PSU giant announces interim payout as profit more tha"
- OHI (Omega Healthcare Investors, In) score 29.1 — "NVDA - INVESTORS RUSH TO BUY NVIDIA DIP DESPITE CEO CRISIS Nearly 90% of Nvidia trades by "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 23.7 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- COIN (Coinbase Global, Inc.) score 23.5 — "Standard Chartered launches four global investment funds from GIFT City"
- LTH (Life Time Group Holdings, Inc.) score 22.4 — "NVDA - INVESTORS RUSH TO BUY NVIDIA DIP DESPITE CEO CRISIS Nearly 90% of Nvidia trades by "
- BOND (PIMCO Active Bond Exchange-Tra) score 21.2 — "India bonds track Treasury weakness ahead of debt supply"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "Clean Max Enviro Energy pledges Rs 50,000 crore investment in Andhra Pradesh"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 20.2 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.6 — "Tata Consumer Share Price Live Updates: Tata Consumer Market Movement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.6 — "Tata Consumer Share Price Live Updates: Tata Consumer Market Movement"
- SCHD (Schwab US Dividend Equity ETF) score 14.3 — "Oil India dividend, Q2 results 2026: PSU giant announces interim payout as profit more tha"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.4 — "How are ITC shares performing after Gold Flake Regular price hike by  ₹10 per pack? Should"
- JIOFIN.BO (Jio Financial Services Limited) score 11.4 — "Federal Reserve Board announces pricing, effective January 1, 2027, for payment services t"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.6 — "Federal Reserve Board announces pricing, effective January 1, 2027, for payment services t"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.3 — "Up in 8 of last 10 sessions, HDFC Bank share price jumps 22% in this period - Why should y"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.4 — "Buzzing stocks: Bajaj Finance, Tata Power, Adani Enterprises, Sandur Manganese, Alivus Lif"
- CRWV (CoreWeave, Inc.) score 8.7 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- RS (Reliance, Inc.) score 6.1 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- META (Meta) score 6.0 — "India ETFs draw ₹35,120 crore in Q3 as large-cap, precious metals lead inflows"
- JEF (Jefferies Financial Group Inc.) score 5.0 — "FIIs are back! Jefferies lists 11 stocks that can be the biggest beneficiaries"
- DEMZ (Democratic Large Cap Core ETF) score 4.7 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- GS (Goldman Sachs Group, Inc. (The) score 3.8 — "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast"
- SEPN (Septerna, Inc.) score 2.7 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "Broker’s call: PB Fintech (Buy)"

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