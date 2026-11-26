# Transmission Layer — board brief · 2026-11-26 13:50Z

data as of **2026-11-26** · 97 series · 10 red / 33 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.861, 9d in regime; vol-pct 0.952, breadth-off 0.769, Markov P(high-vol) 0.211)
- [WEAK] **safe_haven_gold** — corr20 -0.18, corr60 -0.27, contra nifty_50 corr20=0.1, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.89, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.39, corr60 0.23, last shift 2026-09-23. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.09, corr60 0.06, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.0, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.18, corr60 -0.01, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.3, corr60 0.36, last shift 2026-10-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 88** scanned series survive multiplicity control (effective p ≤ 0.000779424725164013)
- **SETUP** dyn_hdb → nifty_50: leads 1d (ccf 0.283, β 0.1525, p 1e-05); driver zc 1.55 → expected 0.431%. Type hit-rate 0.821 (n=2168).
- Track record · residual_reversion: hit-rate **0.508** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2168) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.05] natgas ↑
- natgas [COMMODITIES]: last 3.68, z20 3.05, zc 3.27, resid-z -0.58 [moved], 1d 12.57%, 1-session move +12.57% ≥ 5.0%; |z20|=3.05
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Iran Says LNG Carrier Exploded After Hitting a Mine in Hormuz — OilPrice, 2026-11-26. https://oilprice.com/Latest-Energy-News/World-News/Iran-Says-LNG-Carrier-Exploded-After-Hitting-a-Mine-in-Hormuz.html
- Source: Global LNG Supply Crunch Set to Spill Into 2027 — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Global-LNG-Supply-Crunch-Set-to-Spill-Into-2027.html
- Source: Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Sachs-Sees-US-Natural-Gas-Demand-Surging-on-Data-Center-Boom.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 7.85] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 86.03, z20 1.53, zc n/a, resid-z n/a [quiet], 1d -2.55%, GSR>85 (extreme high); |z20|=1.53; 1y-pct=99
- comex_silver [COMMODITIES]: last 42.08, z20 -1.44, zc 1.28, resid-z 1.15 [quiet], 1d 5.08%, 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3620.40, z20 -1.32, zc 1.00, resid-z -2.50 [unexplained], 1d 2.39%, 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.588 via comex_gold, z -0.57, quiet); dyn_jiofin_bo (rho 0.455 via comex_gold, z 0.61, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.569 vs comex_silver, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.588, z -0.57); dyn_jiofin_bo (rho 0.455, z 0.61)
- Source: Gold price today in India  ₹58,500 away from record high; right time to buy amid rebound from 14-month low? — Mint Markets, 2026-11-26. https://www.livemint.com/market/commodities/gold-price-today-in-india-rs-58-500-away-from-record-high-right-time-to-buy-amid-rebound-from-14-month-low-11795679635348.html
- Source: Gold rate today in Chennai, Hyderabad, Bangalore: Check 26 November MCX yellow metal prices details — Mint Markets, 2026-11-26. https://www.livemint.com/market/commodities/gold-rate-today-in-chennai-hyderabad-bangalore-check-26-november-mcx-yellow-metal-prices-details-11795681144857.html
- Source: Gold prices crash  ₹22,000 in a month: Is this the right time to buy to make profits when prices go up? Experts' advice — Mint Markets, 2026-11-26. https://www.livemint.com/market/commodities/gold-prices-crash-rs-22-000-in-a-month-is-this-the-right-time-to-buy-to-make-profits-when-prices-go-up-experts-advice-11795679163869.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.99] usd_inr ↓
- usd_inr [FX]: last 92.54, z20 -1.99, zc -0.70, resid-z -0.33 [quiet], 1d -0.29%, 20d range extreme; |z20|=1.99; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.451 via usd_inr, z 2.56, reacted); dyn_indianb_ns (rho -0.445 via usd_inr, z 0.73, quiet); dyn_havells_ns (rho -0.417 via usd_inr, z 0.89, quiet); dyn_techm_ns (rho -0.391 via usd_inr, z 2.89, reacted); dyn_tataelxsi_ns (rho -0.376 via usd_inr, z 0.99, quiet)
- **India receivers**: nifty_it (rho -0.451, z 2.56); dyn_indianb_ns (rho -0.445, z 0.73); dyn_havells_ns (rho -0.417, z 0.89); dyn_techm_ns (rho -0.391, z 2.89)
- Source: IT stocks surge 3.6% as Nifty edges up; rupee slips to 92.44 — BusinessLine Mkts, 2026-11-26. https://www.thehindubusinessline.com/markets/it-stocks-surge-36-as-nifty-edges-up-rupee-slips-to-9244/article71746454.ece
- Source: Indian banks seek RBI intervention as dollar surplus pushes up rupee forward premiums — BusinessLine Mkts, 2026-11-26. https://www.thehindubusinessline.com/markets/forex/indian-banks-seek-rbi-intervention-as-dollar-surplus-pushes-up-rupee-forward-premiums/article71746228.ece
- Source: Rupee weakens 24 paise to settle at 92.44 against US dollar — BusinessLine Mkts, 2026-11-26. https://www.thehindubusinessline.com/markets/forex/rupee-weakens-24-paise-to-settle-at-9244-against-us-dollar/article71746093.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 5.76] brent ↓
- brent [COMMODITIES]: last 91.17, z20 -0.76, zc -1.49, resid-z 1.07 [quiet], 1d -3.64%, 1-session move -3.64% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.757 vs brent, historically leads by 5d
- Watch next: vix (co-move) — not yet - watch; rho 0.521 vs brent, historically leads by 1d
- Source: India bonds tumble as Brent tops $95 per barrel, RBI flags food inflation risks — ET Markets, 2026-11-26. https://economictimes.indiatimes.com/markets/bonds/india-bonds-tumble-as-brent-tops-95-per-barrel-rbi-flags-food-inflation-risks/articleshow/136193320.cms
- Source: Oil Prices Rebound as Middle East Supply Fears Return — OilPrice, 2026-11-26. https://oilprice.com/Energy/Energy-General/Oil-Prices-Rebound-as-Middle-East-Supply-Fears-Return.html
- Source: Spike in oil prices partly reverses rupee rally, forward premiums surge — ET Markets, 2026-11-26. https://economictimes.indiatimes.com/markets/forex/forex-news/spike-in-oil-prices-partly-reverses-rupee-rally-forward-premiums-surge/articleshow/136188127.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [AMBER 5.47] cross-asset · 3 series ↓
- dyn_ms [EQUITIES]: last 167.53, z20 -2.15, zc -0.29, resid-z -1.14 [quiet], 1d -0.75%, |z20|=2.15
- dyn_gs [EQUITIES]: last 800.45, z20 -2.12, zc -0.25, resid-z -1.23 [quiet], 1d -0.69%, |z20|=2.12; 1y-pct=5
- vix [INDICES]: last 26.93, z20 0.79, zc -0.51, resid-z n/a [quiet], 1d -4.81%, 1y-pct=95
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-14 (z-distance 0.4).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.808 vs dyn_gs, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.76 vs dyn_gs
- Source: CRWV - COREWEAVE BANKS PREPARE $4.5 BILLION LOAN SALE AS DEFAULT FEARS SURGE Morgan Stanley and MUFG are preparing to sell $4.5 billion in CoreWeave-linked debt as soon as next week, Bloomberg reports. The loan, backed by GPUs supporting a Meta data center project, is expected to carry investment-gr — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39209
- Source: SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Christian Mueller-Glissmann warns that markets remain fragile as investors question AI investment returns and elevated borrowing costs. Goldman's risk appetite indicator has not reached levels typically associated — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39170
- Source: CBOE VOLATILITY INDEX UP 4.54 POINTS AT 30.88 — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39169
- Historical analogues: 2025-08-14 (d=0.4), 2026-05-20 (d=0.44), 2026-05-13 (d=0.53)

### [AMBER 5.12] rates · 2 series ↑
- hy_oas [RATES]: last 3.72, z20 2.29, zc 0.71, resid-z 0.43 [quiet], 1d 2.48%, |z20|=2.29; 1y-pct=99
- ig_oas [RATES]: last 0.98, z20 2.17, zc 0.45, resid-z 0.00 [quiet], 1d 1.03%, |z20|=2.17; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.491 via ig_oas, z -1.73, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.572 vs hy_oas, historically leads by 5d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.527 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.491, z -1.73)
- Source: U.S. $44 BILLION 7-YEAR TREASURY AUCTION TAILS AS DEMAND DISAPPOINTS The U.S. Treasury sold $44 billion in 7-year notes at a high yield of 4.708%, above the 4.698% when-issued yield before the auction. That represents a 1-basis-point tail, signaling weaker-than-expected demand. 🔸 Bid-to-cover ratio: — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39202
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [RED 4.68] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 163.83, z20 2.68, zc 1.04, resid-z 0.00 [quiet], 1d 2.82%, |z20|=2.68
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Swami Ramdev fame company announces 2nd interim dividend; check amount, record date, history — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/swami-ramdev-fame-company-patanjali-foods-announces-2nd-interim-dividend-check-amount-record-date-history-11795691413030.html
- Source: Check Nifty target, Top Stocks to Buy: PL Capital adds HUL, Astral, Grindwell to high-conviction list | Full List — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/check-nifty-target-top-stocks-to-buy-pl-capital-adds-hul-astral-grindwell-to-high-conviction-list-full-list-11795685183310.html
- Source: US stock market open or closed today Thursday, 26 Nov? Check NYSE and Nasdaq trading schedule, holiday calendar — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/us-stock-market-open-or-closed-today-thursday-26-nov-check-nyse-and-nasdaq-trading-schedule-holiday-calendar-11795689325619.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 4.33] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 103.71, z20 -1.50, zc 0.28, resid-z -1.54 [unexplained], 1d 1.33%, 1y-pct=1
- btc_usd [CRYPTO]: last 60852.24, z20 -1.07, zc 0.32, resid-z 0.24 [quiet], 1d 0.79%, 1y-pct=4
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-03-31 (z-distance 0.13).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.528 vs dyn_coin, historically leads by 1d
- Watch next: brent (inverse) — not yet - watch; rho -0.527 vs btc_usd, historically leads by 3d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.528 vs btc_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.523 vs btc_usd
- Source: India’s steel output rises 3.6% in October, but global production dips — BusinessLine Mkts, 2026-11-26. https://www.thehindubusinessline.com/markets/commodities/indias-steel-output-rises-36-in-october-but-global-production-dips/article71746170.ece
- Source: Can Nifty cross 26,000 today? FPI buying, global cues hold the key — BusinessLine Mkts, 2026-11-26. https://www.thehindubusinessline.com/markets/will-nifty-cross-26000-today-fpi-inflows-global-cues-in-focus/article71745061.ece
- Source: Oil Rallies as Hormuz Mine Strikes Rattle Global Markets — OilPrice, 2026-11-26. https://oilprice.com/Latest-Energy-News/World-News/Oil-Rallies-as-Hormuz-Mine-Strikes-Rattle-Global-Markets.html
- Historical analogues: 2025-03-31 (d=0.13), 2026-04-01 (d=0.15), 2025-10-30 (d=0.19)

## Watchlist (below surfacing floor)
equities · 2 series ↓ (4.14), fx · 2 series ↓ (4.04), dyn_tgt ↑ (3.8), cross-asset · 2 series ↑ (3.73), dyn_301077_sz ↓ (3.73), usd_mxn ↑ (3.37), dyn_lth ↑ (3.06), dyn_eternal_ns ↑ (2.83), dyn_2545_tw ↓ (2.82), shanghai_comp ↓ (2.59), dyn_4417_t ↑ (2.54), corn ↑ (2.31)

## India macro
- nifty_50: 25884.5000 (1d 0.25%, z20 1.26, flag none)
- nifty_midcap_100: 61782.5000 (1d 0.32%, z20 0.89, flag none)
- usd_inr: 92.5400 (1d -0.29%, z20 -1.99, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.3869 (1d 0.07%, z20 -1.73, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.2 — "Indian bonds tumble as Brent tops $95 per barrel, RBI flags food inflation risks"
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.4 — "Indian bonds tumble as Brent tops $95 per barrel, RBI flags food inflation risks"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.2 — "Indian bonds tumble as Brent tops $95 per barrel, RBI flags food inflation risks"
- NVDA (NVIDIA Corporation) score 63.8 — "NVDA - U.S. INTELLIGENCE FINDS NO EVIDENCE CHINA ORCHESTRATED JENSEN HUANG AFFAIR — WSJ U."
- INDIANB.NS (INDIAN BANK) score 58.7 — "Indian bonds tumble as Brent tops $95 per barrel, RBI flags food inflation risks"
- BAC (Bank of America Corporation) score 44.1 — "HDFC Bank shares rise 2.5% as board approves key Director re-appointment"
- HDB (HDFC Bank Limited) score 40.7 — "BSE shares jump 48% in 2026 so far: HDFC Securities upgrades to BUY, hikes target; sees 18"
- TGT (Target Corporation) score 38.6 — "Gold, Silver rates today LIVE: UBS keeps  ₹1.50 lakh/10 gm target for gold in 2027 despite"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.4 — "HDFC Bank shares rise 2.5% as board approves key Director re-appointment"
- IDBI.NS (IDBI BANK LIMITED) score 36.4 — "HDFC Bank shares rise 2.5% as board approves key Director re-appointment"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.4 — "HDFC Bank shares rise 2.5% as board approves key Director re-appointment"
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.2 — "TCS, Wipro, Infosys to HCL Tech shares: Why are Indian IT stocks skyrocketing despite Trum"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.1 — "TCS, Wipro, Infosys to HCL Tech shares: Why are Indian IT stocks skyrocketing despite Trum"
- TECH (Bio-Techne Corp) score 32.1 — "TCS, Wipro, Infosys to HCL Tech shares: Why are Indian IT stocks skyrocketing despite Trum"
- OHI (Omega Healthcare Investors, In) score 32.1 — "Volatility-weary US investors side swiped as tariff mayhem adds to tech pain"
- BLLN (BillionToOne, Inc.) score 30.0 — "Enbridge Eyes $1 Billion Pipeline Deal With Indigenous Communities"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 28.3 — "NVDA - U.S. INTELLIGENCE FINDS NO EVIDENCE CHINA ORCHESTRATED JENSEN HUANG AFFAIR — WSJ U."
- 301077.SZ (CHINASTARS) score 26.2 — "From AI models to football: how China plans to expand defence education by 2030"
- CHKP (Check Point Software Technolog) score 23.2 — "1:1 bonus share by famous IT company with 25% returns in 6 months: Check last day to buy, "
- COIN (Coinbase Global, Inc.) score 21.5 — "Oil Rallies as Hormuz Mine Strikes Rattle Global Markets"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.4 — "India’s kharif foodgrains estimate 5% lower on weather woes"
- LTH (Life Time Group Holdings, Inc.) score 19.2 — "Gold prices crash  ₹22,000 in a month: Is this the right time to buy to make profits when "
- BOND (PIMCO Active Bond Exchange-Tra) score 17.0 — "Adani firms plan public bond sale to raise at least Rs 2,000 crore"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.9 — "Multibagger stock to buy: SG Mart shares rise 4% despite 5800% rally in 5 years | Buy, sel"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.3 — "Stocks to watch, Nov 26: LG Electronics, Tata Steel, APL Apollo Tubes, Fino Payments, PNB,"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.3 — "Stocks to watch, Nov 26: LG Electronics, Tata Steel, APL Apollo Tubes, Fino Payments, PNB,"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.6 — "1:1 bonus share by famous IT company with 25% returns in 6 months: Check last day to buy, "
- META (Meta) score 10.6 — "Gold rate today in Chennai, Hyderabad, Bangalore: Check 26 November MCX yellow metal price"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.2 — "Bajaj Finserv Share Price Highlights: Bajaj Finserv Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 8.1 — "Jio Financial Services vs Reliance vs Jio Platforms shares: Which Mukesh Ambani's stock to"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.7 — "ANT - ANTHROPIC RISKS LOSING $1 TRILLION MARKET VALUATION JUST DAYS AFTER IPO Anthropic is"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.3 — "Eternal, Adani Enterprises among 10 stocks with highest FII buying in Q2. How many do you "
- CRWV (CoreWeave, Inc.) score 6.7 — "CRWV - COREWEAVE BONDS PLUNGE AS 2031 YIELD SURGES TO 17.91% CoreWeave's debt is coming un"
- TATASTEEL.BO (TATA STEEL LTD.) score 6.3 — "Stocks to watch, Nov 26: LG Electronics, Tata Steel, APL Apollo Tubes, Fino Payments, PNB,"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.3 — "Climate Finance Dispute Derails COP31 Negotiations"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Chr"
- MS (Morgan Stanley) score 4.7 — "CRWV - COREWEAVE BANKS PREPARE $4.5 BILLION LOAN SALE AS DEFAULT FEARS SURGE Morgan Stanle"
- ETERNAL.NS (ETERNAL LIMITED) score 3.5 — "Eternal, Adani Enterprises among 10 stocks with highest FII buying in Q2. How many do you "
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.0 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.7 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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