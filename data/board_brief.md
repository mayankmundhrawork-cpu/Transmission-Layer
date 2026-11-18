# Transmission Layer — board brief · 2026-11-18 21:54Z

data as of **2026-11-18** · 97 series · 18 red / 31 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.844, 3d in regime; vol-pct 0.922, breadth-off 0.765, Markov P(high-vol) 0.024)
- [INVERTED] **safe_haven_gold** — corr20 -0.05, corr60 -0.18, contra nifty_50 corr20=0.37, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.34, corr60 0.2, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.06, corr60 0.07, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.15, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.31, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0002155994669548189)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.511** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2042) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.4] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.00, z20 6.40, zc 3.58, resid-z 0.95 [moved], 1d 16.05%, |z20|=6.40
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.402 via dyn_301077_sz, z 5.17, reacted)
- **India receivers**: dyn_inoxindia_ns (rho 0.402, z 5.17)
- Source: China Secures Major Gas Deal as Its Influence Grows Across Central Asia — OilPrice, 2026-11-18. https://oilprice.com/Energy/Energy-General/China-Secures-Major-Gas-Deal-as-Its-Influence-Grows-Across-Central-Asia.html
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 7.62] commodities · 2 series ↓
- wti [COMMODITIES]: last 82.08, z20 -1.79, zc -1.80, resid-z -1.95 [unexplained], 1d -4.57%, 1-session move -4.57% ≥ 1.5%; |z20|=1.79
- brent [COMMODITIES]: last 88.82, z20 -1.51, zc -1.80, resid-z -2.16 [unexplained], 1d -4.64%, 1-session move -4.64% ≥ 1.5%; |z20|=1.51; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.454 via wti, z 1.38, reacted)
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.505 vs wti
- **India receivers**: nifty_fmcg (rho -0.454, z 1.38)
- Source: US Oil Inventories On the Rise — OilPrice, 2026-11-18. https://oilprice.com/Energy/Crude-Oil/US-Oil-Inventories-On-the-Rise.html
- Source: WALLER: ROUGHLY 70% OF ITEMS IN CORE SERVICES BASKET ARE OVER 3%, THAT IS NOT RELATED TO OIL — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38730
- Source: EU Moves to Fast-Track Renewables as Oil Import Costs Soar — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/EU-Moves-to-Fast-Track-Renewables-as-Oil-Import-Costs-Soar.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.36] cross-asset · 5 series ↓
- dow_jones [INDICES]: last 50193.03, z20 -3.43, zc -1.01, resid-z -2.11 [unexplained], 1d -1.12%, |z20|=3.43
- dyn_schd [EQUITIES]: last 34.69, z20 -2.22, zc -1.86, resid-z -2.35 [unexplained], 1d -1.76%, |z20|=2.22
- sp500 [INDICES]: last 7322.28, z20 -2.07, zc -0.21, resid-z -0.77 [quiet], 1d -0.25%, |z20|=2.07
- russell_2000 [INDICES]: last 2714.66, z20 -2.01, zc 0.34, resid-z 1.05 [quiet], 1d 0.47%, |z20|=2.01
- dyn_nvda [EQUITIES]: last 150.87, z20 -1.89, zc -0.90, resid-z 1.01 [quiet], 1d -2.95%, 1y-pct=0
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.597 vs russell_2000, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.608 vs dow_jones
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.555 vs dyn_schd
- Source: Wall Street Sees More Mega Debt Deals Using Paramount Blueprint — Mint Markets, 2026-11-18. https://www.livemint.com/market/wall-street-sees-more-mega-debt-deals-using-paramount-blueprint-11795027290809.html
- Source: Nasdaq gains in choppy trade as Nvidia outlook lifts AI mood; Anthropic pricing awaited — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/sp-500-nasdaq-open-higher-as-nvidia-forecast-eases-ai-jitters/articleshow/135966195.cms
- Source: Dow slumps over 1% at close as hawkish Fed minutes outweigh Nvidia optimism; Anthropic reveals IPO price: Stock Market Highlights — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-nasdaq-sp-500-nvidia-forecast-anthropic-ipo-coreweave-nebius-fed-rate-fed-rate-hike-treasury-yield-news-18th-november-2026/liveblog/135964782.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-22 (d=0.91), 2025-05-16 (d=1.21)

### [RED 7.2] usd_inr ↓
- usd_inr [FX]: last 93.46, z20 -2.20, zc -1.24, resid-z -0.71 [quiet], 1d -0.54%, 20d range extreme; |z20|=2.20; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.447 via usd_inr, z 0.87, quiet); dyn_indianb_ns (rho -0.444 via usd_inr, z 1.41, reacted); nifty_it (rho -0.398 via usd_inr, z -2.4, reacted); dyn_tataelxsi_ns (rho -0.351 via usd_inr, z -1.96, reacted)
- **India receivers**: dyn_havells_ns (rho -0.447, z 0.87); dyn_indianb_ns (rho -0.444, z 1.41); nifty_it (rho -0.398, z -2.4); dyn_tataelxsi_ns (rho -0.351, z -1.96)
- Source: Rupee rises 7 paise to close at 93.44 against US dollar — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9344-against-us-dollar/article71715511.ece
- Source: Rupee ends flat after hitting seven-month high as firmer dollar offsets inflows — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-ends-flat-after-hitting-seven-month-high-as-firmer-dollar-offsets-inflows/articleshow/135959732.cms
- Source: Rupee appreciates for third consecutive day as oil dips — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-appreciates-for-third-consecutive-day-as-oil-dips/article71714723.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.9] natgas ↑
- natgas [COMMODITIES]: last 3.39, z20 1.90, zc 1.61, resid-z 1.65 [unexplained], 1d 5.58%, 1-session move +5.58% ≥ 5.0%; |z20|=1.90
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Mozambique Approves Exxon’s Redesigned $30 Billion Rovuma LNG Plan — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/Mozambique-Approves-Exxons-Redesigned-30-Billion-Rovuma-LNG-Plan.html
- Source: China Gas Upsizes Long-Term LNG Supply with U.S. Venture Global — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/China-Gas-Upsizes-Long-Term-LNG-Supply-with-US-Venture-Global.html
- Source: U.S. natural gas inventories end injection season above normal levels — EIA Today in Energy, 2026-11-18. https://www.eia.gov/todayinenergy/detail.php?id=68484
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 6.49] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3726.90, z20 -3.17, zc -2.24, resid-z 0.21 [priced], 1d -3.55%, |z20|=3.17; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 44.99, z20 -2.64, zc -1.81, resid-z 0.39 [priced], 1d -4.87%, |z20|=2.64; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 82.85, z20 2.12, zc n/a, resid-z n/a [quiet], 1d 1.38%, |z20|=2.12; 1y-pct=100
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.497 via comex_gold, z 0.07, quiet); dyn_karurvysya_ns (rho 0.457 via comex_gold, z 1.46, reacted); nifty_metal (rho 0.404 via comex_gold, z 0.05, quiet); dyn_jiofin_bo (rho 0.403 via comex_gold, z 0.61, quiet)
- **India receivers**: dyn_muthootfin_ns (rho 0.497, z 0.07); dyn_karurvysya_ns (rho 0.457, z 1.46); nifty_metal (rho 0.404, z 0.05); dyn_jiofin_bo (rho 0.403, z 0.61)
- Source: Gold Slumps 3% to Lowest in Over a Year on Hawkish Fed Signals — Mint Markets, 2026-11-18. https://www.livemint.com/market/gold-slumps-3-to-lowest-in-over-a-year-on-hawkish-fed-signals-11795036212650.html
- Source: Gold drops to 14-month low as dollar, yields rise on hawkish Fed rhetoric — Mint Markets, 2026-11-18. https://www.livemint.com/market/gold-drops-to-14-month-low-as-dollar-yields-rise-on-hawkish-fed-rhetoric-11795032242167.html
- Source: Gold, silver imports worth $715 million at Indian Customs, says bullion industry body — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/gold/gold-silver-imports-worth-715-million-at-indian-customs-says-bullion-industry-body/article71716461.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.71] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 62231.71, z20 -2.39, zc -1.47, resid-z -1.70 [unexplained], 1d -4.10%, |z20|=2.39; 1y-pct=4
- eth_usd [CRYPTO]: last 1761.70, z20 -2.07, zc -0.86, resid-z -0.91 [quiet], 1d -3.36%, |z20|=2.07
- dyn_coin [EQUITIES]: last 110.54, z20 -2.06, zc -0.84, resid-z -0.27 [quiet], 1d -3.90%, |z20|=2.06; 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.48).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: China Gas Upsizes Long-Term LNG Supply with U.S. Venture Global — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/China-Gas-Upsizes-Long-Term-LNG-Supply-with-US-Venture-Global.html
- Source: SPCX $APO - SPACEX PLANS $40 BILLION OFF-BALANCE-SHEET AI CHIP FINANCING SpaceX is preparing a $40 billion financing deal arranged by Apollo Global Management to fund AI chips without adding the debt directly to its balance sheet. The financing will use a special-purpose vehicle (SPV), allowing Spac — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38740
- Source: Global money rushes back into Indian stocks at record pace — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/stocks/news/global-money-rushes-back-into-indian-stocks-at-record-pace/articleshow/135950745.cms
- Historical analogues: 2026-05-22 (d=0.48), 2025-10-16 (d=0.65), 2025-04-10 (d=0.67)

### [RED 5.51] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -2.68, zc -0.52, resid-z -0.75 [quiet], 1d -0.19%, |z20|=2.68; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.65, zc -0.69, resid-z -1.10 [quiet], 1d -0.26%, |z20|=2.65; 1y-pct=0
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.049 vs eur_usd, historically leads by 1d

## Watchlist (below surfacing floor)
comex_copper ↓ (5.48), dyn_blln ↓ (5.44), dxy ↑ (5.34), dyn_inoxindia_ns ↑ (5.17), dyn_bac ↓ (4.53), dyn_kaynes_ns ↓ (4.52), dyn_coalindia_ns ↓ (4.02), dyn_tgt ↑ (3.75), dyn_lth ↑ (3.41), dyn_eternal_ns ↑ (3.08), ftse_100 ↓ (2.84), eur_inr ↓ (2.84)

## India macro
- nifty_50: 25227.9492 (1d -0.63%, z20 1.25, flag none)
- nifty_midcap_100: 60974.4492 (1d -1.22%, z20 0.93, flag none)
- usd_inr: 93.4600 (1d -0.54%, z20 -2.20, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4169 (1d -0.60%, z20 -1.66, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 80.3 — "Goldman Sachs upgrades India to overweight, sets Nifty target of 28,500"
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.4 — "Goldman Sachs upgrades India to overweight, sets Nifty target of 28,500"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.1 — "Goldman Sachs upgrades India to overweight, sets Nifty target of 28,500"
- NVDA (NVIDIA Corporation) score 60.5 — "Dow slumps over 1% at close as hawkish Fed minutes outweigh Nvidia optimism; Anthropic rev"
- INDIANB.NS (INDIAN BANK) score 59.8 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- BAC (Bank of America Corporation) score 51.2 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- HDB (HDFC Bank Limited) score 46.5 — "HDFC Life Share Price Highlights: HDFC Life Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.0 — "SML Mahindra offers shares at 37% discount as M&M steps up CV expansion"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.8 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- IDBI.NS (IDBI BANK LIMITED) score 42.8 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.8 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.3 — "After 156% surge in a day, this American firm stock rises another 5%. What's driving the b"
- TECH (Bio-Techne Corp) score 40.3 — "After 156% surge in a day, this American firm stock rises another 5%. What's driving the b"
- TGT (Target Corporation) score 34.1 — "Goldman Sachs upgrades India to overweight, sets Nifty target of 28,500"
- OHI (Omega Healthcare Investors, In) score 32.1 — "US Stock Market: Nasdaq preparing to roll out 23-hour-a-day trading from this date – Key f"
- COIN (Coinbase Global, Inc.) score 25.6 — "SPCX $APO - SPACEX PLANS $40 BILLION OFF-BALANCE-SHEET AI CHIP FINANCING SpaceX is prepari"
- 301077.SZ (CHINASTARS) score 24.1 — "RUSSIA AND CHINA HAVE MOVED TO A NEW LEVEL OF DEFENCE INDUSTRY COOPERATION, SENIOR RUSSIAN"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.0 — "FED'S WALLER CALLS FOR 50-BASIS-POINT RATE HIKE IN DECEMBER Federal Reserve Governor Chris"
- BLLN (BillionToOne, Inc.) score 20.7 — "ECB WEIGHS DOUBLING BANK RESERVE REQUIREMENTS TO 2%, SAVING €4.4 BILLION ANNUALLY The Euro"
- CHKP (Check Point Software Technolog) score 20.2 — "Netweb Technologies shares up 42% from 52-week low, is there more steam left in the AI sto"
- LTH (Life Time Group Holdings, Inc.) score 18.0 — "ADNOC Ship Attacked in Hormuz as Maritime Security Risks Rise"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.0 — "FINANCES WORSEN FOR 37% OF GERMAN CONSUMERS, SURVEY SHOWS 37% of German consumers say thei"
- JIOFIN.BO (Jio Financial Services Limited) score 16.3 — "FINANCES WORSEN FOR 37% OF GERMAN CONSUMERS, SURVEY SHOWS 37% of German consumers say thei"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.6 — "Tata Motors among 5 stocks closing above 200-DMA"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.6 — "Tata Motors among 5 stocks closing above 200-DMA"
- BOND (PIMCO Active Bond Exchange-Tra) score 14.2 — "India bonds rise tracking easing crude oil, US Treasury yields"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.4 — "Indoco Remedies share price jumps 13%; pharma stock up over 16% in 2 weeks: Can the rally "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.2 — "FINANCES WORSEN FOR 37% OF GERMAN CONSUMERS, SURVEY SHOWS 37% of German consumers say thei"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.5 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- MS (Morgan Stanley) score 7.4 — "JPMORGAN WARNS LEVERAGED-LOAN DEFAULTS COULD MORE THAN DOUBLE IN 2027 JPMorgan forecasts U"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.4 — "Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant"
- META (Meta) score 6.3 — "Profit-booking drags Nifty below 25,200; Pharma holds firm as metals, durables bleed"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.2 — "Adani Ent Share Price Highlights: Adani Ent. Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 5.6 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- GS (Goldman Sachs Group, Inc. (The) score 4.7 — "Goldman Sachs upgrades India to overweight, sets Nifty target of 28,500"
- RS (Reliance, Inc.) score 3.4 — "Reliance, UltraTech, Hyundai Motor shares: Top 3 stocks to buy; check ratings, target pric"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 3.2 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- CRWV (CoreWeave, Inc.) score 3.0 — "CoreWeave’s stock pops — even as Nvidia talks up a ‘disciplined’ approach to financing"
- ETERNAL.NS (ETERNAL LIMITED) score 1.9 — "Eternal among 5 stocks hitting 52-week highs; stock rallies up to 15% in a month"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.9 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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