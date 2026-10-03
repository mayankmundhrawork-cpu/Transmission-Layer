# Transmission Layer — board brief · 2026-10-03 00:35Z

data as of **2026-10-03** · 97 series · 13 red / 39 amber · 8 events surfaced (34 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.367, 1d in regime; vol-pct 0.162, breadth-off 0.571, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.42, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.75, corr60 0.85, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.19, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.12, last shift 2026-08-20. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.1, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.24, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.46, corr60 0.2, last shift 2026-07-28. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006262113571624539)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.586, β -0.4303, p 0.0); driver zc 2.44 → expected -1.057%. Type hit-rate 0.824 (n=2347).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.383, β 0.2224, p 0.0); driver zc 2.44 → expected 0.546%. Type hit-rate 0.824 (n=2347).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.373, β -0.2076, p 0.0); driver zc 2.44 → expected -0.51%. Type hit-rate 0.824 (n=2347).
- Track record · residual_reversion: hit-rate **0.501** (n=1131) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2347) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 8.34] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.61, z20 2.06, zc -0.65, resid-z -1.26 [quiet], 1d -0.53%, |z20|=2.06; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.54, z20 -1.99, zc -0.60, resid-z -4.75 [unexplained], 1d -0.22%, 1y-pct=0
- ust_10y [RATES]: last 5.24, z20 1.51, zc -0.91, resid-z -2.10 [unexplained], 1d -0.95%, |z20|=1.51; 1y-pct=98
- tips_10y_real [RATES]: last 2.88, z20 1.41, zc -0.84, resid-z -2.58 [unexplained], 1d -1.71%, 1d move -5.0bps ≥ 5bps; 1y-pct=98
- ust_2y [RATES]: last 4.78, z20 0.62, zc -1.58, resid-z -3.54 [unexplained], 1d -2.05%, 1y-pct=97
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.701 vs ust_30y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.531 vs ust_30y, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.558 vs dyn_bond
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.517 vs ust_30y
- Source: How much higher can bond yields rise — and what does it mean for stocks? — MarketWatch Top, 2026-10-02. https://www.marketwatch.com/story/how-much-higher-can-bond-yields-rise-and-what-does-it-mean-for-stocks-12883d6c?mod=mw_rss_topstories
- Source: Why bond investors quickly lost their enthusiasm for weak jobs figures — MarketWatch Top, 2026-10-02. https://www.marketwatch.com/story/why-bond-investors-quickly-lost-their-enthusiasm-for-weak-labor-figures-7a9727da?mod=mw_rss_topstories
- Source: Nabard subsidiary Nabkisan lists India’s first WASH social bond; raises ₹180 crore — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/markets/nabard-subsidiary-nabkisan-lists-indias-first-wash-social-bond-raises-180-crore/article71536956.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.31] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4172.10, z20 -1.86, zc -0.81, resid-z 1.11 [quiet], 1d -0.72%, |z20|=1.86; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 60.71, z20 -1.65, zc -0.01, resid-z 0.90 [quiet], 1d -0.02%, |z20|=1.65; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.72, z20 1.00, zc n/a, resid-z n/a [quiet], 1d -0.69%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.364 via gold_silver_ratio, z -1.56, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.582 vs comex_silver, historically leads by 1d
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.579 vs comex_gold
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.573 vs comex_gold
- **India receivers**: midcap_largecap_ratio (rho -0.364, z -1.56)
- Source: SPOT GOLD FALLS NEARLY 1% TO $4,137.85/OZ — DeItaone, 2026-10-02. https://t.me/walter_bloomberg/36571
- Source: Today’s Gold Rate: Latest gold prices in Coimbatore, Nagpur, Jaipur & other cities — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-2-2026/article71536292.ece
- Source: Today’s Gold Rate, Aug 26: Check gold rates in Delhi, Mumbai, Chennai — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-2-2026/article71536291.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 6.33] usd_inr ↑
- usd_inr [FX]: last 96.30, z20 1.33, zc 0.73, resid-z 0.43 [quiet], 1d 0.39%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.396 via usd_inr, z 0.81, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.396, z 0.81)
- Source: ETMarkets Smart Talk: Rupee under pressure, inflation sticky: Will RBI be forced to rethink rates? Ankita Pathak, Ionic Asset — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/expert-view/etmarkets-smart-talk-rupee-under-pressure-inflation-sticky-will-rbi-be-forced-to-rethink-rates-ankita-pathak-ionic-asset/articleshow/134634188.cms
- Source: FCNR inflows cushion rupee, BoP; FII flows crucial for sustained external stability: Report — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/markets/fcnr-inflows-cushion-rupee-bop-fii-flows-crucial-for-sustained-external-stability-report/article71535966.ece
- Source: Rupee sinks to 96.31, logs biggest fall in over 2 months — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-sinks-to-96-31-logs-biggest-fall-in-over-2-months/articleshow/134630728.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.19] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 22421.95, z20 -2.53, zc -1.36, resid-z -1.34 [quiet], 1d -0.88%, |z20|=2.53; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 58732.00, z20 -2.52, zc -1.06, resid-z -0.70 [quiet], 1d -0.99%, |z20|=2.52
- india_vix [INDICES]: last 14.46, z20 2.49, zc 1.22, resid-z n/a [quiet], 1d 7.19%, |z20|=2.49
- dyn_policybzr_ns [EQUITIES]: last 980.00, z20 -2.24, zc -1.16, resid-z -0.96 [quiet], 1d -7.89%, |z20|=2.24; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.634 via nifty_midcap_100, z -1.56, reacted); nifty_fmcg (rho 0.573 via nifty_50, z -3.7, reacted); dyn_jiofin_bo (rho 0.537 via nifty_50, z -2.93, reacted); nifty_metal (rho 0.521 via nifty_midcap_100, z -2.96, reacted); dyn_indusindbk_bo (rho 0.509 via nifty_midcap_100, z -2.15, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.634, z -1.56); nifty_fmcg (rho 0.573, z -3.7); dyn_jiofin_bo (rho 0.537, z -2.93); nifty_metal (rho 0.521, z -2.96)
- Source: Sumeet Bagadia's top 3 stocks to buy: HDFC Life, Cummins India, CG Power | Target, stoploss, Nifty, Bank Nifty outlook — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/sumeet-bagadias-top-3-stocks-to-buy-hdfc-life-cummins-india-cg-power-target-stoploss-nifty-bank-nifty-outlook-11790949673699.html
- Source: Experts' view: Why would bears cheer Nifty's breakdown below 22,000? — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/experts-view-why-would-bears-cheer-niftys-breakdown-below-22000-11790938909647.html
- Source: Investors worried over bloodbath as Nifty 50 sees longest weekly losing streak in 25 yrs - Outlook for H2 from experts — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/investors-worried-over-bloodbath-as-nifty-50-sees-longest-weekly-losing-streak-in-25-yrs-outlook-for-h2-from-experts-11790922247662.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 6.03] wti ↓
- wti [COMMODITIES]: last 91.26, z20 -1.03, zc -0.64, resid-z -0.29 [quiet], 1d -1.73%, 1-session move -1.73% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.906 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.564 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.507 vs wti
- Source: Trump Says South Korea Deal Includes $8.4 Billion U.S. Oil Project — OilPrice, 2026-10-02. https://oilprice.com/Latest-Energy-News/World-News/Trump-Says-South-Korea-Deal-Includes-84-Billion-US-Oil-Project.html
- Source: Iranian Oil Starts Flowing to Tajikistan Despite U.S. Sanctions Risk — OilPrice, 2026-10-02. https://oilprice.com/Energy/Energy-General/Iranian-Oil-Starts-Flowing-to-Tajikistan-Despite-US-Sanctions-Risk.html
- Source: U.S. Oil Drilling Inches Up As Prices Fall — OilPrice, 2026-10-02. https://oilprice.com/Energy/Crude-Oil/US-Oil-Drilling-Inches-Up-As-Prices-Fall.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 5.13] indices · 2 series ↑
- nikkei_225 [INDICES]: last 68190.14, z20 2.30, zc -0.56, resid-z -0.94 [quiet], 1d -1.11%, |z20|=2.30
- taiwan_weighted [INDICES]: last 48483.91, z20 1.73, zc 0.25, resid-z -0.32 [quiet], 1d 0.27%, |z20|=1.73; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.374 via taiwan_weighted, z -0.79, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.841 vs nikkei_225
- **India receivers**: nifty_it (rho -0.374, z -0.79)
- Source: Global Markets | Japan's Nikkei retreats from 6-week high as investors lock in gains — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-retreats-from-6-week-high-as-investors-lock-in-gains/articleshow/134633243.cms
- Source: Global Market: Japan’s Nikkei hits six-week high as chip stocks rally on AI optimism — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-hits-six-week-high-as-chip-stocks-rally-on-ai-optimism/articleshow/134609469.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 4.93] dyn_jiofin_bo ↓
- dyn_jiofin_bo [EQUITIES]: last 212.00, z20 -2.93, zc -1.66, resid-z -0.41 [priced], 1d -2.12%, |z20|=2.93; 1y-pct=0
- **Mechanism**: dyn_jiofin_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.537 via dyn_jiofin_bo, z -2.53, reacted); nifty_midcap_100 (rho 0.496 via dyn_jiofin_bo, z -2.52, reacted); nifty_metal (rho 0.395 via dyn_jiofin_bo, z -2.96, reacted); dyn_muthootfin_ns (rho 0.362 via dyn_jiofin_bo, z -2.12, reacted)
- **India receivers**: nifty_50 (rho 0.537, z -2.53); nifty_midcap_100 (rho 0.496, z -2.52); nifty_metal (rho 0.395, z -2.96); dyn_muthootfin_ns (rho 0.362, z -2.12)
- Source: AI BOOM MAY REQUIRE U.S. SPENDING EQUAL TO 9% OF GDP America may need to spend roughly $3.5 trillion annually on AI services by 2032 — 8.8% of GDP — to justify today’s massive data-center investment, according to Columbia professor Stijn Van Nieuwerburgh. The risk is that expanding compute capacity  — DeItaone, 2026-10-02. https://t.me/walter_bloomberg/36524
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-14 (d=0.01), 2025-08-06 (d=0.03)

### [RED 4.36] bovespa ↑
- bovespa [INDICES]: last 191797.94, z20 4.36, zc 2.44, resid-z 1.90 [unexplained], 1d 2.46%, |z20|=4.36; 1y-pct=96
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_stylebaaza_ns (rho -0.436 via bovespa, z -1.94, reacted)
- **India receivers**: dyn_stylebaaza_ns (rho -0.436, z -1.94)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

## Watchlist (below surfacing floor)
eur_usd ↓ (4.25), dyn_indusindbk_bo ↓ (4.15), rates · 2 series ↑ (4.13), dyn_nvda ↑ (3.77), dxy ↑ (3.71), nifty_fmcg ↓ (3.7), nasdaq_100 ↑ (3.59), indices · 2 series ↓ (3.47), commodities · 3 series ↓ (3.33), dyn_4417_t ↑ (3.22), hang_seng ↓ (3.01), nifty_metal ↓ (2.96)

## India macro
- nifty_50: 22421.9492 (1d -0.88%, z20 -2.53, flag red)
- nifty_midcap_100: 58732.0000 (1d -0.99%, z20 -2.52, flag red)
- usd_inr: 96.3000 (1d 0.39%, z20 1.33, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6194 (1d -0.12%, z20 -1.56, flag amber)
- Next India prints: NSDL FPI flows T-2d · IMD weekly rainfall T-2d · RBI MPC decision T-4d · AMFI SIP / MF flows T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.4 — "Inox Air Products files draft papers for IPO"
- COALINDIA.NS (COAL INDIA LTD) score 86.6 — "Nabard subsidiary Nabkisan lists India’s first WASH social bond; raises ₹180 crore"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.4 — "Nabard subsidiary Nabkisan lists India’s first WASH social bond; raises ₹180 crore"
- INDIANB.NS (INDIAN BANK) score 66.4 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- BOND (PIMCO Active Bond Exchange-Tra) score 59.8 — "BOFA’S HARTNETT SEES RISK-OFF MOOD PERSISTING BofA’s Michael Hartnett says investors are l"
- COIN (Coinbase Global, Inc.) score 52.8 — "FRENCH 5-YEAR SOVEREIGN CREDIT DEFAULT SWAPS HIT 81BPS, S&P GLOBAL MARKET INTELLIGENCE"
- BAC (Bank of America Corporation) score 50.2 — "America's Canadian import restrictions come into force. Here are the products barred from "
- OHI (Omega Healthcare Investors, In) score 47.7 — "BOFA’S HARTNETT SEES RISK-OFF MOOD PERSISTING BofA’s Michael Hartnett says investors are l"
- HDB (HDFC Bank Limited) score 46.0 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.4 — "ANTHROPIC WARNS THAT GOVERNMENT ATTITUDES TOWARD THE COMPANY, ITS TECHNOLOGY COULD HAVE IM"
- IDBI.NS (IDBI BANK LIMITED) score 42.7 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.7 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.7 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- SEPN (Septerna, Inc.) score 40.5 — "TIMIRAOS: WEAK JOBS REPORT CLEARS PATH FOR FED PAUSE The September jobs report gives the F"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.6 — "ANTHROPIC WARNS THAT GOVERNMENT ATTITUDES TOWARD THE COMPANY, ITS TECHNOLOGY COULD HAVE IM"
- TECH (Bio-Techne Corp) score 38.6 — "ANTHROPIC WARNS THAT GOVERNMENT ATTITUDES TOWARD THE COMPANY, ITS TECHNOLOGY COULD HAVE IM"
- CHKP (Check Point Software Technolog) score 36.4 — "Stock market holiday today: Are NSE, BSE closed for Gandhi Jayanti? Check 2026 holiday lis"
- LTH (Life Time Group Holdings, Inc.) score 34.1 — "HASSETT ON DIESEL: WE HAVE BEEN TALKING WITH EUROPE *HASSETT ON DIESEL: EUROPE RELEASE WOU"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.8 — "TRUMP: SOUTH KOREA DEAL EXPANDS WITH $8.4 BILLION ENERGY PROJECT President Trump says the "
- TGT (Target Corporation) score 30.0 — "MSTR - CITI RAISES STRATEGY TARGET TO $240 ON HIGHER BITCOIN FORECAST Citi raised its Stra"
- 301077.SZ (CHINASTARS) score 23.5 — "‘America is back’, AI ‘conspiracy’, China’s Laos deal: 7 global relations reads"
- BZ=F (Brent Crude Oil Last Day Finan) score 21.9 — "CBOE VOLATILITY INDEX HITS ONE-WEEK LOW, LAST DOWN 0.79 POINTS AT 15.60"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.6 — "RBI MPC may hike repo rate next week: Experts share the equity-debt strategy investors sho"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.9 — "TRUMP: EUROPE HAS JUST AGREED TO RELEASE A MASSIVE AMOUNT OF THEIR HEAVILY STOCKED DIESEL "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.9 — "Adani Group's most valuable company sets new record; shares major business update"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.5 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.5 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- JIOFIN.BO (Jio Financial Services Limited) score 11.4 — "AI BOOM MAY REQUIRE U.S. SPENDING EQUAL TO 9% OF GDP America may need to spend roughly $3."
- POLICYBZR.NS (PB FINTECH LIMITED) score 8.9 — "Where could PB Fintech share price be in the next five years?"
- GS (Goldman Sachs Group, Inc. (The) score 8.7 — "U.S. Diesel Export Ban Would Hit Latin America Hardest: Goldman"
- META (Meta) score 8.3 — "META PARTS WAYS WITH VIRTUE AI - SEMAFOR"
- VT (Vanguard Total World Stock Ind) score 7.3 — "Jio Platforms IPO in final stages after concluding worldwide roadshows"
- NVDA (NVIDIA Corporation) score 7.1 — "NVIDIA SHARES RISE 2.5% TO HIT FIRST RECORD HIGH SINCE MAY"
- JEF (Jefferies Financial Group Inc.) score 6.7 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.2 — "Down 10% in a month; Bajaj Finance approves  ₹11,700 cr QIP,  ₹5,800 cr warrants to Bajaj "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.8 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.6 — "ESDS, Lumino, Purple Style Labs: 18 IPO stocks facing anchor lock-in expiry in October - C"
- MS (Morgan Stanley) score 4.2 — "NVDA - MORGAN STANLEY RENAMES NVIDIA TO TOP PICK"
- VOLTAS.NS (VOLTAS LTD) score 0.3 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.2 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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