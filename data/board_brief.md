# Transmission Layer — board brief · 2026-11-18 12:59Z

data as of **2026-11-18** · 97 series · 15 red / 31 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.795, 3d in regime; vol-pct 0.922, breadth-off 0.667, Markov P(high-vol) 0.054)
- [INVERTED] **safe_haven_gold** — corr20 -0.07, corr60 -0.19, contra nifty_50 corr20=0.36, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.29, corr60 0.17, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.11, corr60 0.06, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.02, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.31, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.003076390423476072)
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.466, β 0.7877, p 0.0); driver zc -1.69 → expected -1.296%. Type hit-rate 0.818 (n=2062).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.433, β 0.2724, p 0.0); driver zc -1.69 → expected -0.448%. Type hit-rate 0.818 (n=2062).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.422, β -0.2551, p 0.0); driver zc -1.69 → expected 0.42%. Type hit-rate 0.818 (n=2062).
- **SETUP** comex_copper → aud_usd: leads 1d (ccf 0.371, β 0.1076, p 0.00078); driver zc -1.94 → expected -0.4%. Type hit-rate 0.818 (n=2062).
- **SETUP** comex_gold → aud_usd: leads 1d (ccf 0.356, β 0.1486, p 0.0); driver zc -1.86 → expected -0.44%. Type hit-rate 0.818 (n=2062).
- Track record · residual_reversion: hit-rate **0.511** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2062) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.29] commodities · 2 series ↓
- wti [COMMODITIES]: last 84.30, z20 -1.46, zc -0.78, resid-z -0.54 [quiet], 1d -1.99%, 1-session move -1.99% ≥ 1.5%
- brent [COMMODITIES]: last 90.38, z20 -1.35, zc -1.15, resid-z -0.49 [quiet], 1d -2.96%, 1-session move -2.96% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.468 via wti, z 1.38, reacted)
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.551 vs wti
- **India receivers**: nifty_fmcg (rho -0.468, z 1.38)
- Source: EU Moves to Fast-Track Renewables as Oil Import Costs Soar — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/EU-Moves-to-Fast-Track-Renewables-as-Oil-Import-Costs-Soar.html
- Source: India bonds rise tracking easing crude oil, US Treasury yields — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/bonds/india-bonds-rise-tracking-easing-crude-oil-us-treasury-yields/articleshow/135952296.cms
- Source: Rupee appreciates for third consecutive day as oil dips — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-appreciates-for-third-consecutive-day-as-oil-dips/article71714723.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.27] cross-asset · 6 series ↓
- dow_jones [INDICES]: last 50759.13, z20 -3.12, zc -1.69, resid-z -2.13 [unexplained], 1d -1.65%, |z20|=3.12
- russell_2000 [INDICES]: last 2703.29, z20 -2.76, zc -1.03, resid-z -0.79 [quiet], 1d -1.45%, |z20|=2.76
- sp500 [INDICES]: last 7340.63, z20 -2.25, zc -0.82, resid-z -0.25 [quiet], 1d -1.02%, |z20|=2.25
- dyn_nvda [EQUITIES]: last 155.47, z20 -1.92, zc -0.12, resid-z -0.50 [quiet], 1d -0.43%, 1y-pct=0
- nasdaq_100 [INDICES]: last 26996.90, z20 -1.61, zc -0.37, resid-z -1.47 [quiet], 1d -0.74%, |z20|=1.61
- vix [INDICES]: last 24.89, z20 1.55, zc -0.22, resid-z n/a [quiet], 1d -2.24%, |z20|=1.55
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.428 via dyn_nvda, z 1.15, reacted)
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.602 vs russell_2000, historically leads by 4d
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.654 vs dow_jones
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.611 vs sp500
- Watch next: dax (co-move) — not yet - watch; rho 0.603 vs dow_jones
- **India receivers**: dyn_bajfinance_ns (rho -0.428, z 1.15)
- Source: Nvidia shares gain 3% in premarket after Q3 results, upbeat forecast top estimates: Is the AI rally back on track? — Mint Markets, 2026-11-18. https://www.livemint.com/market/stock-market-news/nvidia-shares-gain-3-in-premarket-after-q3-results-upbeat-forecast-top-estimates-is-the-ai-rally-back-on-track-11795005376675.html
- Source: Nvidia's Jensen Huang $10.7 bn share transfer: CEO, wife Lory transfers 59 mn stocks to Trust - What SEC filing reveals? — Mint Markets, 2026-11-18. https://www.livemint.com/market/stock-market-news/nvidias-jensen-huang-10-7-bn-share-transfer-ceo-wife-lory-transfers-59-mn-stocks-to-trust-what-sec-filing-reveals-11794980098699.html
- Source: Anthropic IPO: Why Wall Street is betting big on Claude AI maker — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/us-stocks/news/anthropic-ipo-why-wall-street-is-betting-big-on-claude-ai-maker/slideshow/135951884.cms
- Historical analogues: 2026-05-22 (d=0.49), 2025-10-21 (d=0.53), 2025-08-28 (d=0.57)

### [RED 7.27] usd_inr ↓
- usd_inr [FX]: last 93.43, z20 -2.27, zc -1.32, resid-z -0.86 [quiet], 1d -0.57%, 20d range extreme; |z20|=2.27; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.443 via usd_inr, z 0.87, quiet); dyn_indianb_ns (rho -0.442 via usd_inr, z 1.41, reacted); nifty_it (rho -0.395 via usd_inr, z -2.4, reacted); dyn_inoxindia_ns (rho -0.353 via usd_inr, z 5.17, reacted)
- **India receivers**: dyn_havells_ns (rho -0.443, z 0.87); dyn_indianb_ns (rho -0.442, z 1.41); nifty_it (rho -0.395, z -2.4); dyn_inoxindia_ns (rho -0.353, z 5.17)
- Source: Rupee rises 7 paise to close at 93.44 against US dollar — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9344-against-us-dollar/article71715511.ece
- Source: Rupee ends flat after hitting seven-month high as firmer dollar offsets inflows — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-ends-flat-after-hitting-seven-month-high-as-firmer-dollar-offsets-inflows/articleshow/135959732.cms
- Source: Rupee appreciates for third consecutive day as oil dips — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-appreciates-for-third-consecutive-day-as-oil-dips/article71714723.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.4] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.00, z20 6.40, zc 3.58, resid-z 3.40 [unexplained], 1d 16.05%, |z20|=6.40
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.402 via dyn_301077_sz, z 5.17, reacted)
- **India receivers**: dyn_inoxindia_ns (rho 0.402, z 5.17)
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 6.23] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3749.90, z20 -2.91, zc -1.86, resid-z 0.30 [priced], 1d -2.96%, |z20|=2.91; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 45.24, z20 -2.54, zc -1.61, resid-z 0.12 [priced], 1d -4.32%, |z20|=2.54; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 82.88, z20 2.14, zc n/a, resid-z n/a [quiet], 1d 1.42%, |z20|=2.14; 1y-pct=100
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.49 via comex_gold, z 0.07, quiet); dyn_karurvysya_ns (rho 0.456 via comex_gold, z 1.46, reacted); dyn_jiofin_bo (rho 0.396 via comex_gold, z 0.61, quiet); nifty_metal (rho 0.395 via comex_gold, z 0.05, quiet)
- **India receivers**: dyn_muthootfin_ns (rho 0.49, z 0.07); dyn_karurvysya_ns (rho 0.456, z 1.46); dyn_jiofin_bo (rho 0.396, z 0.61); nifty_metal (rho 0.395, z 0.05)
- Source: Today’s Gold Rate in India November 18: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-18-2026/article71715011.ece
- Source: Today’s Gold Rate in India November 18: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-18-2026/article71715010.ece
- Source: Gold, silver prices in Indian markets crash to nearly a year’s low — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/gold/gold-silver-prices-in-indian-markets-crash-to-nearly-a-years-low/article71714989.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.49] dxy ↑
- dxy [FX]: last 103.90, z20 2.49, zc 1.11, resid-z 0.14 [quiet], 1d 0.39%, 20d range extreme; |z20|=2.49; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho -0.383 via dxy, z 1.11, reacted)
- **India receivers**: dyn_indusindbk_bo (rho -0.383, z 1.11)
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [AMBER 5.36] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 64018.05, z20 -2.05, zc -0.48, resid-z -0.08 [quiet], 1d -1.35%, |z20|=2.05
- dyn_coin [EQUITIES]: last 115.04, z20 -2.03, zc -0.86, resid-z -0.11 [quiet], 1d -4.00%, |z20|=2.03; 1y-pct=0
- eth_usd [CRYPTO]: last 1793.91, z20 -1.90, zc -0.41, resid-z 0.08 [quiet], 1d -1.59%, |z20|=1.90
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.43).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global money rushes back into Indian stocks at record pace — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/stocks/news/global-money-rushes-back-into-indian-stocks-at-record-pace/articleshow/135950745.cms
- Source: Global Market Today: Asian shares rebound as Nvidia forecast eases AI trade concerns — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-shares-rebound-as-nvidia-forecast-eases-ai-trade-concerns/articleshow/135944698.cms
- Source: GIFT City eyes global commodity trade; finance, liquidity could pose hurdles — Mint Markets, 2026-11-18. https://www.livemint.com/market/gift-city-eyes-global-commodity-trade-finance-liquidity-could-pose-hurdles-11794895899256.html
- Historical analogues: 2026-05-22 (d=0.43), 2025-10-16 (d=0.51), 2025-04-10 (d=0.56)

### [RED 5.17] dyn_inoxindia_ns ↑
- dyn_inoxindia_ns [EQUITIES]: last 2145.00, z20 5.17, zc 2.98, resid-z 2.96 [unexplained], 1d 8.92%, |z20|=5.17
- **Mechanism**: dyn_inoxindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho -0.353 via dyn_inoxindia_ns, z -2.27, reacted)
- **India receivers**: usd_inr (rho -0.353, z -2.27)
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.04), 2025-06-30 (d=0.07)

## Watchlist (below surfacing floor)
dyn_blln ↓ (4.65), dyn_kaynes_ns ↓ (4.52), dyn_coalindia_ns ↓ (4.02), rates · 3 series ↑ (3.9), fx · 2 series ↓ (3.67), dyn_eternal_ns ↑ (3.08), comex_copper ↓ (3.07), eur_inr ↓ (3.01), dyn_lth ↑ (2.84), dyn_4417_t ↑ (2.8), dyn_crwv ↓ (2.54), nifty_it ↓ (2.4)

## India macro
- nifty_50: 25227.9492 (1d -0.63%, z20 1.25, flag none)
- nifty_midcap_100: 60974.4492 (1d -1.22%, z20 0.93, flag none)
- usd_inr: 93.4300 (1d -0.57%, z20 -2.27, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4169 (1d -0.60%, z20 -1.66, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 83.1 — "Fairfax to exit Indian shadow lender IIFL in $370 million sale"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.9 — "Fairfax to exit Indian shadow lender IIFL in $370 million sale"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.4 — "Fairfax to exit Indian shadow lender IIFL in $370 million sale"
- NVDA (NVIDIA Corporation) score 63.8 — "Flat opening as Nvidia earnings beat softens Wall Street’s blow; Bank Nifty holds near rec"
- INDIANB.NS (INDIAN BANK) score 59.7 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- BAC (Bank of America Corporation) score 51.5 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- HDB (HDFC Bank Limited) score 46.3 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.8 — "TCS share price down 26% in 2026: Is this a buying opportunity? What do technical charts s"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.4 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 43.4 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.4 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.8 — "TCS share price down 26% in 2026: Is this a buying opportunity? What do technical charts s"
- TECH (Bio-Techne Corp) score 42.8 — "TCS share price down 26% in 2026: Is this a buying opportunity? What do technical charts s"
- TGT (Target Corporation) score 35.0 — "Netweb Technologies shares up 42% from 52-week low, is there more steam left in the AI sto"
- OHI (Omega Healthcare Investors, In) score 33.9 — "Why Ashok Leyland’s investors are wary despite robust demand"
- COIN (Coinbase Global, Inc.) score 25.7 — "Global money rushes back into Indian stocks at record pace"
- CHKP (Check Point Software Technolog) score 22.0 — "Netweb Technologies shares up 42% from 52-week low, is there more steam left in the AI sto"
- 301077.SZ (CHINASTARS) score 21.9 — "China’s local officials feel financial stick long before seeing carrot"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "Cuba’s Energy Crisis Turns Into a Goldmine for U.S. Fuel Exporters"
- LTH (Life Time Group Holdings, Inc.) score 19.7 — "ADNOC Ship Attacked in Hormuz as Maritime Security Risks Rise"
- BLLN (BillionToOne, Inc.) score 18.1 — "NVDA - NVIDIA STOPS DISCLOSING SINGAPORE SALES AS REVENUE SURGES TO $104 BILLION Nvidia st"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.4 — "Bajaj Auto Share Price Highlights: Bajaj Auto Stock Price History"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.9 — "Tata Motors among 5 stocks closing above 200-DMA"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.9 — "Tata Motors among 5 stocks closing above 200-DMA"
- JIOFIN.BO (Jio Financial Services Limited) score 15.6 — "China’s local officials feel financial stick long before seeing carrot"
- BOND (PIMCO Active Bond Exchange-Tra) score 15.4 — "India bonds rise tracking easing crude oil, US Treasury yields"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.6 — "Indoco Remedies share price jumps 13%; pharma stock up over 16% in 2 weeks: Can the rally "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.3 — "IIFL Finance share price: NBFC stock jumps 6% after  ₹3,454 cr block deal: Why is Fairfax "
- BZ=F (Brent Crude Oil Last Day Finan) score 8.1 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- MS (Morgan Stanley) score 8.1 — "JPMORGAN WARNS LEVERAGED-LOAN DEFAULTS COULD MORE THAN DOUBLE IN 2027 JPMorgan forecasts U"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.0 — "Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant"
- META (Meta) score 6.8 — "Profit-booking drags Nifty below 25,200; Pharma holds firm as metals, durables bleed"
- SCHD (Schwab US Dividend Equity ETF) score 6.1 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.7 — "Stock Market Live Updates | Opening Bell: Sensex gains over 200 pts, Nifty above 25,300; I"
- GS (Goldman Sachs Group, Inc. (The) score 4.0 — "GOLDMAN SACHS CUTS OIL PRICE FORECASTS FOR 2026 AND 2027 Goldman Sachs has lowered its Bre"
- RS (Reliance, Inc.) score 3.8 — "Reliance, UltraTech, Hyundai Motor shares: Top 3 stocks to buy; check ratings, target pric"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 3.5 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- CRWV (CoreWeave, Inc.) score 3.3 — "CoreWeave’s stock pops — even as Nvidia talks up a ‘disciplined’ approach to financing"
- ETERNAL.NS (ETERNAL LIMITED) score 2.1 — "Eternal among 5 stocks hitting 52-week highs; stock rallies up to 15% in a month"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.0 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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