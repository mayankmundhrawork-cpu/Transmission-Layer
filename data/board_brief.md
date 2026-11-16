# Transmission Layer — board brief · 2026-11-16 23:23Z

data as of **2026-11-16** · 97 series · 13 red / 33 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.74, 1d in regime; vol-pct 0.892, breadth-off 0.588, Markov P(high-vol) 0.034)
- [WEAK] **safe_haven_gold** — corr20 -0.09, corr60 -0.21, contra nifty_50 corr20=0.25, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.12, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.35, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 -0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.37, corr60 0.32, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006738585313537104)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.515** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2130) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.62] rates · 4 series ↑
- tips_10y_real [RATES]: last 2.91, z20 2.95, zc 0.88, resid-z 0.62 [quiet], 1d 1.75%, 1d move +5.0bps ≥ 5bps; |z20|=2.95; 1y-pct=97
- ust_2y [RATES]: last 4.88, z20 2.05, zc 0.30, resid-z -0.11 [quiet], 1d 0.41%, |z20|=2.05; 1y-pct=98
- ust_30y [RATES]: last 5.47, z20 1.88, zc 0.83, resid-z 0.51 [quiet], 1d 0.74%, |z20|=1.88
- ust_10y [RATES]: last 5.15, z20 1.66, zc 0.88, resid-z 0.55 [quiet], 1d 0.98%, |z20|=1.66
- **Mechanism**: rates · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_tgt (inverse) — not yet - watch; rho -0.565 vs ust_30y
- Watch next: dyn_schd (inverse) — not yet - watch; rho -0.519 vs tips_10y_real
- Source: Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/forex/rupee-likely-to-open-flat-as-dollar-strength-us-bond-yields-weigh-on-sentiment/article71706648.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [RED 8.73] cross-asset · 8 series ↓
- btc_usd [CRYPTO]: last 65173.55, z20 -2.54, zc 0.45, resid-z -1.19 [quiet], 1d 1.63%, |z20|=2.54
- eth_usd [CRYPTO]: last 1823.26, z20 -2.34, zc 0.67, resid-z -0.81 [quiet], 1d 3.06%, |z20|=2.34
- dyn_nvda [EQUITIES]: last 156.16, z20 -2.20, zc -0.49, resid-z -0.50 [quiet], 1d -4.11%, |z20|=2.20; 1y-pct=0
- dyn_coin [EQUITIES]: last 119.84, z20 -1.98, zc -0.49, resid-z -0.11 [quiet], 1d -6.12%, 1y-pct=0
- sp500 [INDICES]: last 7420.19, z20 -1.78, zc -0.30, resid-z -0.25 [quiet], 1d -1.87%, |z20|=1.78
- russell_2000 [INDICES]: last 2743.39, z20 -1.55, zc -0.21, resid-z 0.30 [quiet], 1d -1.69%, |z20|=1.55
- nasdaq_100 [INDICES]: last 27204.77, z20 -1.55, zc -0.57, resid-z -1.47 [quiet], 1d -2.64%, |z20|=1.55
- vix [INDICES]: last 22.88, z20 1.23, zc 0.34, resid-z n/a [quiet], 1d 18.55%, 1-session move +18.55% ≥ 15.0%
- **Mechanism**: cross-asset · 8 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.417 via dyn_nvda, z 1.74, reacted)
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.606 vs russell_2000, historically leads by 4d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.693 vs btc_usd
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.521 vs dyn_nvda
- **India receivers**: dyn_bajfinance_ns (rho -0.417, z 1.74)
- Source: Nvidia’s stock extends decline following harsh words from the U.S. government — MarketWatch Top, 2026-11-16. https://www.marketwatch.com/story/nvidias-stock-extends-declines-following-harsh-words-from-the-u-s-government-d721188e?mod=mw_rss_topstories
- Source: Wall Street update: Why Walmart, Home Depot, Target, Lowe's stocks are in focus this week | Q3 earnings latest news — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/wall-street-update-why-walmart-home-depot-target-lowes-stocks-are-in-focus-this-week-q3-earnings-latest-news-11794849291449.html
- Source: Meganet Technologies Global files draft papers for ₹740-crore IPO — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/meganet-technologies-global-files-draft-papers-for-740-crore-ipo/article71709227.ece
- Historical analogues: 2026-05-22 (d=0.52), 2025-10-21 (d=0.8), 2026-04-02 (d=1.11)

### [RED 7.42] commodities · 2 series ↓
- wti [COMMODITIES]: last 85.38, z20 -1.59, zc -0.07, resid-z -0.38 [quiet], 1d -3.59%, 1-session move -3.59% ≥ 1.5%; |z20|=1.59
- brent [COMMODITIES]: last 92.10, z20 -1.43, zc 0.01, resid-z -0.39 [quiet], 1d -3.90%, 1-session move -3.90% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.466 via wti, z 0.85, quiet)
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.543 vs wti
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.527 vs brent
- **India receivers**: dyn_muthootfin_ns (rho -0.466, z 0.85)
- Source: Uganda Pushes First Oil to Mid-2027 as Iran War Holds Up Equipment — OilPrice, 2026-11-16. https://oilprice.com/Energy/Crude-Oil/Uganda-Pushes-First-Oil-to-Mid-2027-as-Iran-War-Holds-Up-Equipment.html
- Source: Libya Has Africa's Biggest Oil Reserves, but Western Majors Aren't Biting — OilPrice, 2026-11-16. https://oilprice.com/Energy/Crude-Oil/Libya-Has-Africas-Biggest-Oil-Reserves-but-Western-Majors-Arent-Biting.html
- Source: Venezuela’s Oil Comeback Faces a New Threat From Washington — OilPrice, 2026-11-16. https://oilprice.com/Energy/Energy-General/Venezuelas-Oil-Comeback-Faces-a-New-Threat-From-Washington.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.56] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -3.73, zc -1.08, resid-z -1.27 [quiet], 1d -0.44%, |z20|=3.73; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -3.06, zc -0.89, resid-z -1.13 [quiet], 1d -0.35%, |z20|=3.06; 1y-pct=1
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Boris Vujčić: Risks and resilience in the euro area financial system — ECB press, 2026-11-16. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp261116~db374b56ab.en.html
- Source: Yen steady against euro and dollar after soft Japanese GDP data — Mint Markets, 2026-11-16. https://www.livemint.com/market/yen-steady-against-euro-and-dollar-after-soft-japanese-gdp-data-11794791270301.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 6.29] cross-asset · 4 series ↓
- comex_copper [COMMODITIES]: last 5.99, z20 -2.62, zc -0.78, resid-z -0.94 [quiet], 1d -1.46%, |z20|=2.62
- comex_silver [COMMODITIES]: last 46.94, z20 -2.29, zc -0.64, resid-z -1.40 [quiet], 1d -4.26%, |z20|=2.29; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 82.16, z20 2.27, zc n/a, resid-z n/a [quiet], 1d 3.66%, |z20|=2.27; 1y-pct=100
- comex_gold [COMMODITIES]: last 3856.60, z20 -2.16, zc 0.01, resid-z 0.30 [quiet], 1d -0.76%, |z20|=2.16; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.47 via comex_gold, z 0.85, quiet); dyn_karurvysya_ns (rho 0.425 via comex_gold, z 2.27, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.47, z 0.85); dyn_karurvysya_ns (rho 0.425, z 2.27)
- Source: Goldman Forecasts Gold to Take Two Years to Recapture All-Time Highs — Mint Markets, 2026-11-16. https://www.livemint.com/market/goldman-forecasts-gold-to-take-two-years-to-recapture-all-time-highs-11794862583269.html
- Source: Gold below $4,000/oz attracts ETF inflows, led by US — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/gold/gold-below-4000oz-attracts-etf-inflows-led-by-us/article71708410.ece
- Source: SILVER COULD HIT $75 AN OUNCE IN 2027, BANK OF AMERICA SAYS Bank of America (BofA) says silver could climb to $75 an ounce next year as macroeconomic headwinds ease. Silver closed Friday at $48.74, down 6.1% for the week, pressured by a stronger dollar, higher oil prices and Fed rate-hike expectatio — DeItaone, 2026-11-16. https://t.me/walter_bloomberg/38553
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 5.92] dxy ↑
- dxy [FX]: last 103.59, z20 2.92, zc 0.63, resid-z 0.14 [quiet], 1d 0.17%, 20d range extreme; |z20|=2.92; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 5.47] dyn_blln ↓
- dyn_blln [EQUITIES]: last 96.10, z20 -3.47, zc -1.53, resid-z -0.57 [moved], 1d -8.61%, |z20|=3.47
- **Mechanism**: dyn_blln ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Diamondback to Buy Double Eagle’s Midland Stake for $5 Billion — OilPrice, 2026-11-16. https://oilprice.com/Latest-Energy-News/World-News/Diamondback-to-Buy-Double-Eagles-Midland-Stake-for-5-Billion.html
- Source: Trump Media faces possible $1 billion debt repayment as stock nears record lows — ET Markets, 2026-11-16. https://economictimes.indiatimes.com/markets/us-stocks/news/trump-media-faces-possible-1-billion-debt-repayment-as-stock-nears-record-lows/articleshow/135898089.cms
- Source: $51 billion capex, 23% earnings growth: Adani Ports, Adani Green to Energy; Jefferies sees up to 44% upside in 6 stocks — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/51-billion-capex-23-earnings-growth-adani-ports-adani-green-to-energy-jefferies-sees-up-to-44-upside-in-6-stocks-11794842210030.html

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

## Watchlist (below surfacing floor)
cross-asset · 2 series ↑ (4.57), usd_jpy ↑ (3.76), indices · 3 series ↑ (3.47), dyn_atherenerg_ns ↑ (3.46), dyn_tech ↑ (3.24), aud_usd ↓ (3.08), eur_inr ↓ (3.03), dyn_4417_t ↑ (2.95), dyn_schd ↑ (2.82), dyn_lth ↑ (2.71), indices · 2 series ↓ (2.58), dyn_karurvysya_ns ↑ (2.27)

## India macro
- nifty_50: 25291.0996 (1d 0.58%, z20 1.66, flag amber)
- nifty_midcap_100: 61575.5508 (1d -0.50%, z20 1.48, flag none)
- usd_inr: 93.9120 (1d -0.13%, z20 -1.47, flag none)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4347 (1d -1.07%, z20 -1.34, flag none)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 70.7 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.5 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 66.6 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- NVDA (NVIDIA Corporation) score 55.8 — "MUSK: JENSEN DROVE SUPPLY CHAIN BRILLIANTLY AT NVIDIA, BUT MANY OF THOSE DEALS WERE A HAND"
- INDIANB.NS (INDIAN BANK) score 43.7 — "SILVER COULD HIT $75 AN OUNCE IN 2027, BANK OF AMERICA SAYS Bank of America (BofA) says si"
- BAC (Bank of America Corporation) score 40.0 — "US AVIATION CHAOS: OVER 22,000 FLIGHTS CANCELED OR DELAYED America’s air travel system is "
- HDB (HDFC Bank Limited) score 34.9 — "SILVER COULD HIT $75 AN OUNCE IN 2027, BANK OF AMERICA SAYS Bank of America (BofA) says si"
- TECHM.NS (TECH MAHINDRA LIMITED) score 34.7 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.9 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- TECH (Bio-Techne Corp) score 32.9 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 31.8 — "SILVER COULD HIT $75 AN OUNCE IN 2027, BANK OF AMERICA SAYS Bank of America (BofA) says si"
- IDBI.NS (IDBI BANK LIMITED) score 31.8 — "SILVER COULD HIT $75 AN OUNCE IN 2027, BANK OF AMERICA SAYS Bank of America (BofA) says si"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.8 — "SILVER COULD HIT $75 AN OUNCE IN 2027, BANK OF AMERICA SAYS Bank of America (BofA) says si"
- TGT (Target Corporation) score 30.3 — "SPCX: CITIGROUP RAISES TARGET PRICE TO $280 FROM $240"
- OHI (Omega Healthcare Investors, In) score 24.6 — "DEUTSCHE BANK WARNS MARKETS ARE UNDERESTIMATING RATE HIKE RISKS Deutsche Bank warns invest"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.5 — "RISK OF NUCLEAR ACCIDENT IN UKRAINE INCREASING THIS WINTER, ATOMIC SAFETY REGULATORS REPRE"
- COIN (Coinbase Global, Inc.) score 22.5 — "Morgan Stanley turns bullish on global stocks, targets S&P 500 at 8,700"
- CHKP (Check Point Software Technolog) score 22.3 — "Crystal Crop Protection IPO GMP today: How much listing gain is expected? Check profit cal"
- 301077.SZ (CHINASTARS) score 20.3 — "China’s Coal Power Generation Slumps as Wind and Solar Surge"
- LTH (Life Time Group Holdings, Inc.) score 18.4 — "NVDA - NVIDIA SHARES FALL AS JENSEN HUANG REPORTEDLY CONSIDERS CEO COMEBACK Nvidia shares "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.6 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.6 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- BOND (PIMCO Active Bond Exchange-Tra) score 14.6 — "Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.3 — "Bajaj Finserv Share Price Highlights: Bajaj Finserv Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 12.0 — "NVDA - NVIDIA SHARES FALL AS JENSEN HUANG REPORTEDLY CONSIDERS CEO COMEBACK Nvidia shares "
- BLLN (BillionToOne, Inc.) score 11.8 — "Warren Buffett donates $5.47 billion in Berkshire Hathaway shares to charities, confidence"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.7 — "Nifty may open 75 points higher; experts flag consolidation amid global weakness"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.6 — "NVDA - NVIDIA SHARES EXTEND DECLINES, LAST DOWN 3.6% PREMARKET"
- SCHD (Schwab US Dividend Equity ETF) score 8.7 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.4 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.9 — "MORGAN STANLEY RAISES BRENT OIL FORECASTS FOR 2026 AND 2027 Morgan Stanley has revised its"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "$51 billion capex, 23% earnings growth: Adani Ports, Adani Green to Energy; Jefferies sees"
- GS (Goldman Sachs Group, Inc. (The) score 5.7 — "GOLDMAN SACHS CUTS OIL PRICE FORECASTS FOR 2026 AND 2027 Goldman Sachs has lowered its Bre"
- MS (Morgan Stanley) score 4.7 — "Morgan Stanley turns bullish on global stocks, targets S&P 500 at 8,700"
- CRWV (CoreWeave, Inc.) score 3.4 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- META (Meta) score 3.2 — "Nvidia Without Huang: What a Pause in AI Deals Means for Metals"
- RS (Reliance, Inc.) score 2.8 — "Reliance Industries shares rebound 15% in November, add  ₹2.38 lakh crore in market value;"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.7 — "Kaynes Technology shares crash 12%, hit fresh 52-week low after weak Q2 results"
- DEMZ (Democratic Large Cap Core ETF) score 2.2 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.4 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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