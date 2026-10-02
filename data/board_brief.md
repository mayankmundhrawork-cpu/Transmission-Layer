# Transmission Layer — board brief · 2026-10-02 17:52Z

data as of **2026-10-02** · 97 series · 14 red / 35 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.406, 1d in regime; vol-pct 0.24, breadth-off 0.571, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.43, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.76, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.19, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.03, corr60 0.12, last shift 2026-08-19. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.77, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.1, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.25, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.45, corr60 0.19, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006262113571624539)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.5** (n=1131) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.825** (n=2349) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.45] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4165.30, z20 -1.93, zc -1.00, resid-z 0.22 [quiet], 1d -0.88%, |z20|=1.93; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 60.49, z20 -1.75, zc -0.22, resid-z 0.82 [quiet], 1d -0.40%, |z20|=1.75; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.87, z20 1.13, zc n/a, resid-z n/a [quiet], 1d -0.49%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.352 via gold_silver_ratio, z -1.56, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.579 vs comex_silver, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.564 vs comex_gold
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.564 vs comex_gold
- **India receivers**: midcap_largecap_ratio (rho -0.352, z -1.56)
- Source: Today’s Gold Rate: Latest gold prices in Coimbatore, Nagpur, Jaipur & other cities — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-2-2026/article71536292.ece
- Source: Today’s Gold Rate, Aug 26: Check gold rates in Delhi, Mumbai, Chennai — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-2-2026/article71536291.ece
- Source: Gold steadies before US payrolls data, set for second weekly loss — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/markets/gold/gold-steadies-before-us-payrolls-data-set-for-second-weekly-loss/article71536094.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.81] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.64, z20 2.88, zc 1.10, resid-z 0.74 [quiet], 1d 0.89%, |z20|=2.88; 1y-pct=100
- ust_10y [RATES]: last 5.29, z20 2.09, zc 0.55, resid-z 0.14 [quiet], 1d 0.57%, |z20|=2.09; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.53, z20 -1.99, zc -0.63, resid-z 1.10 [quiet], 1d -0.24%, 1y-pct=0
- tips_10y_real [RATES]: last 2.93, z20 1.96, zc 0.33, resid-z 0.02 [quiet], 1d 0.69%, |z20|=1.96; 1y-pct=100
- ust_2y [RATES]: last 4.88, z20 1.27, zc -0.15, resid-z -0.64 [quiet], 1d -0.20%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.656 vs ust_30y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.518 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.502 vs ust_30y, historically leads by 3d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.539 vs ust_10y
- Watch next: sp500 (co-move) — not yet - watch; rho 0.53 vs dyn_bond
- Source: How much higher can bond yields rise — and what does it mean for stocks? — MarketWatch Top, 2026-10-02. https://www.marketwatch.com/story/how-much-higher-can-bond-yields-rise-and-what-does-it-mean-for-stocks-12883d6c?mod=mw_rss_topstories
- Source: Why bond investors quickly lost their enthusiasm for weak jobs figures — MarketWatch Top, 2026-10-02. https://www.marketwatch.com/story/why-bond-investors-quickly-lost-their-enthusiasm-for-weak-labor-figures-7a9727da?mod=mw_rss_topstories
- Source: Nabard subsidiary Nabkisan lists India’s first WASH social bond; raises ₹180 crore — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/markets/nabard-subsidiary-nabkisan-lists-indias-first-wash-social-bond-raises-180-crore/article71536956.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 6.33] usd_inr ↑
- usd_inr [FX]: last 96.30, z20 1.33, zc 0.73, resid-z 0.56 [quiet], 1d 0.39%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.39 via usd_inr, z 0.81, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.39, z 0.81)
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
- **India take**: midcap_largecap_ratio (rho 0.601 via nifty_midcap_100, z -1.56, reacted); dyn_jiofin_bo (rho 0.589 via nifty_50, z -2.93, reacted); nifty_fmcg (rho 0.588 via nifty_50, z -3.7, reacted); nifty_metal (rho 0.523 via nifty_midcap_100, z -2.96, reacted); dyn_indusindbk_bo (rho 0.492 via nifty_midcap_100, z -2.15, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.601, z -1.56); dyn_jiofin_bo (rho 0.589, z -2.93); nifty_fmcg (rho 0.588, z -3.7); nifty_metal (rho 0.523, z -2.96)
- Source: Sumeet Bagadia's top 3 stocks to buy: HDFC Life, Cummins India, CG Power | Target, stoploss, Nifty, Bank Nifty outlook — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/sumeet-bagadias-top-3-stocks-to-buy-hdfc-life-cummins-india-cg-power-target-stoploss-nifty-bank-nifty-outlook-11790949673699.html
- Source: Experts' view: Why would bears cheer Nifty's breakdown below 22,000? — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/experts-view-why-would-bears-cheer-niftys-breakdown-below-22000-11790938909647.html
- Source: Investors worried over bloodbath as Nifty 50 sees longest weekly losing streak in 25 yrs - Outlook for H2 from experts — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/investors-worried-over-bloodbath-as-nifty-50-sees-longest-weekly-losing-streak-in-25-yrs-outlook-for-h2-from-experts-11790922247662.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.13] indices · 2 series ↑
- nikkei_225 [INDICES]: last 68190.14, z20 2.30, zc -0.56, resid-z -0.90 [quiet], 1d -1.11%, |z20|=2.30
- taiwan_weighted [INDICES]: last 48483.91, z20 1.73, zc 0.25, resid-z -0.14 [quiet], 1d 0.27%, |z20|=1.73; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.425 via taiwan_weighted, z -0.79, quiet); dyn_techm_ns (rho -0.419 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.797 vs nikkei_225
- **India receivers**: nifty_it (rho -0.425, z -0.79); dyn_techm_ns (rho -0.419, z -0.73)
- Source: Global Markets | Japan's Nikkei retreats from 6-week high as investors lock in gains — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-retreats-from-6-week-high-as-investors-lock-in-gains/articleshow/134633243.cms
- Source: Global Market: Japan’s Nikkei hits six-week high as chip stocks rally on AI optimism — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-hits-six-week-high-as-chip-stocks-rally-on-ai-optimism/articleshow/134609469.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 4.93] dyn_jiofin_bo ↓
- dyn_jiofin_bo [EQUITIES]: last 212.00, z20 -2.93, zc -1.66, resid-z -0.41 [priced], 1d -2.12%, |z20|=2.93; 1y-pct=0
- **Mechanism**: dyn_jiofin_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.589 via dyn_jiofin_bo, z -2.53, reacted); nifty_midcap_100 (rho 0.446 via dyn_jiofin_bo, z -2.52, reacted)
- **India receivers**: nifty_50 (rho 0.589, z -2.53); nifty_midcap_100 (rho 0.446, z -2.52)
- Source: AI BOOM MAY REQUIRE U.S. SPENDING EQUAL TO 9% OF GDP America may need to spend roughly $3.5 trillion annually on AI services by 2032 — 8.8% of GDP — to justify today’s massive data-center investment, according to Columbia professor Stijn Van Nieuwerburgh. The risk is that expanding compute capacity  — DeItaone, 2026-10-02. https://t.me/walter_bloomberg/36524
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-14 (d=0.01), 2025-08-06 (d=0.03)

### [AMBER 4.24] eur_usd ↓
- eur_usd [FX]: last 1.13, z20 -2.24, zc -1.89, resid-z -2.16 [unexplained], 1d -0.60%, |z20|=2.24; 1y-pct=0
- **Mechanism**: eur_usd ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.364 via eur_usd, z -2.53, reacted)
- **India receivers**: nifty_50 (rho 0.364, z -2.53)
- Source: EURO EXTENDS LOSES AGAINST US DOLLAR, LAST DOWN 1% AT $1.12165 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36495
- Source: EURO SLIDE CONTINUES; LAST DOWN 0.55% AT $1.127 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36444
- Source: FOREX-Euro slides to 17-month low, hit by rates and inflation cocktail — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/forex-euro-slides-to-17-month-low-hit-by-rates-and-inflation-cocktail/articleshow/134613639.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.02), 2026-06-16 (d=0.04)

### [AMBER 4.15] dyn_indusindbk_bo ↓
- dyn_indusindbk_bo [EQUITIES]: last 880.00, z20 -2.15, zc -0.81, resid-z -0.60 [quiet], 1d -1.97%, |z20|=2.15
- **Mechanism**: dyn_indusindbk_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.492 via dyn_indusindbk_bo, z -2.52, reacted); nifty_50 (rho 0.407 via dyn_indusindbk_bo, z -2.53, reacted); nifty_metal (rho 0.374 via dyn_indusindbk_bo, z -2.96, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.492, z -2.52); nifty_50 (rho 0.407, z -2.53); nifty_metal (rho 0.374, z -2.96)
- Source: With Anup Bagchi as CEO, a deep-dive into how bank stocks fared after top boss changes - Yes, RBL, IndusInd, HDFC Bank — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/as-hdfc-bank-names-anup-bagchi-as-ceo-heres-how-bank-stocks-fared-after-past-ceo-changes-yes-bank-rbl-to-indusind-11790942528070.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

## Watchlist (below surfacing floor)
rates · 2 series ↑ (4.13), dyn_nvda ↑ (3.9), dxy ↑ (3.71), nifty_fmcg ↓ (3.7), nasdaq_100 ↑ (3.59), indices · 2 series ↓ (3.47), dyn_4417_t ↑ (3.22), commodities · 3 series ↓ (3.2), dyn_hdb ↓ (3.05), hang_seng ↓ (3.01), nifty_metal ↓ (2.96), dyn_voltas_ns ↓ (2.95)

## India macro
- nifty_50: 22421.9492 (1d -0.88%, z20 -2.53, flag red)
- nifty_midcap_100: 58732.0000 (1d -0.99%, z20 -2.52, flag red)
- usd_inr: 96.3000 (1d 0.39%, z20 1.33, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6194 (1d -0.12%, z20 -1.56, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 97.5 — "Inox Air Products files draft papers for IPO"
- COALINDIA.NS (COAL INDIA LTD) score 92.4 — "Nabard subsidiary Nabkisan lists India’s first WASH social bond; raises ₹180 crore"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.0 — "Nabard subsidiary Nabkisan lists India’s first WASH social bond; raises ₹180 crore"
- INDIANB.NS (INDIAN BANK) score 70.8 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- BOND (PIMCO Active Bond Exchange-Tra) score 63.8 — "BOFA’S HARTNETT SEES RISK-OFF MOOD PERSISTING BofA’s Michael Hartnett says investors are l"
- COIN (Coinbase Global, Inc.) score 56.4 — "FRENCH 5-YEAR SOVEREIGN CREDIT DEFAULT SWAPS HIT 81BPS, S&P GLOBAL MARKET INTELLIGENCE"
- BAC (Bank of America Corporation) score 53.5 — "America's Canadian import restrictions come into force. Here are the products barred from "
- OHI (Omega Healthcare Investors, In) score 50.9 — "BOFA’S HARTNETT SEES RISK-OFF MOOD PERSISTING BofA’s Michael Hartnett says investors are l"
- HDB (HDFC Bank Limited) score 49.0 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.3 — "ANTHROPIC WARNS THAT GOVERNMENT ATTITUDES TOWARD THE COMPANY, ITS TECHNOLOGY COULD HAVE IM"
- IDBI.NS (IDBI BANK LIMITED) score 45.5 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.5 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.5 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.2 — "ANTHROPIC WARNS THAT GOVERNMENT ATTITUDES TOWARD THE COMPANY, ITS TECHNOLOGY COULD HAVE IM"
- TECH (Bio-Techne Corp) score 41.2 — "ANTHROPIC WARNS THAT GOVERNMENT ATTITUDES TOWARD THE COMPANY, ITS TECHNOLOGY COULD HAVE IM"
- SEPN (Septerna, Inc.) score 40.1 — "Private sector jobs rose by 90,000 in September, better than expected, ADP reports"
- CHKP (Check Point Software Technolog) score 38.8 — "Stock market holiday today: Are NSE, BSE closed for Gandhi Jayanti? Check 2026 holiday lis"
- LTH (Life Time Group Holdings, Inc.) score 34.3 — "PRESIDENT TRUMP — FRIDAY, OCTOBER 2, 2026 🔸 8:00 AM — Executive Time — White House 🔸 9:00 "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.0 — "FRANCE FLOATS 100 MILLION-BARREL ENERGY RESERVE RELEASE France has proposed that EU countr"
- TGT (Target Corporation) score 32.0 — "MSTR - CITI RAISES STRATEGY TARGET TO $240 ON HIGHER BITCOIN FORECAST Citi raised its Stra"
- 301077.SZ (CHINASTARS) score 25.1 — "‘America is back’, AI ‘conspiracy’, China’s Laos deal: 7 global relations reads"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 21.9 — "RBI MPC may hike repo rate next week: Experts share the equity-debt strategy investors sho"
- BZ=F (Brent Crude Oil Last Day Finan) score 19.2 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.7 — "Adani Group's most valuable company sets new record; shares major business update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.7 — "AI BOOM MAY REQUIRE U.S. SPENDING EQUAL TO 9% OF GDP America may need to spend roughly $3."
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.3 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.3 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- JIOFIN.BO (Jio Financial Services Limited) score 12.1 — "AI BOOM MAY REQUIRE U.S. SPENDING EQUAL TO 9% OF GDP America may need to spend roughly $3."
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.5 — "Where could PB Fintech share price be in the next five years?"
- GS (Goldman Sachs Group, Inc. (The) score 9.3 — "U.S. Diesel Export Ban Would Hit Latin America Hardest: Goldman"
- VT (Vanguard Total World Stock Ind) score 7.8 — "Jio Platforms IPO in final stages after concluding worldwide roadshows"
- META (Meta) score 7.8 — "Gold price today: Precious metal slips ahead of US Jobs data; MCX closed for Gandhi Jayant"
- JEF (Jefferies Financial Group Inc.) score 7.1 — "Only 9% up since last MD but Jefferies sees 10% more in Kotak Mahindra Bank shares after A"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.6 — "Down 10% in a month; Bajaj Finance approves  ₹11,700 cr QIP,  ₹5,800 cr warrants to Bajaj "
- NVDA (NVIDIA Corporation) score 6.6 — "NVDA - MORGAN STANLEY RENAMES NVIDIA TO TOP PICK"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.1 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.0 — "ESDS, Lumino, Purple Style Labs: 18 IPO stocks facing anchor lock-in expiry in October - C"
- MS (Morgan Stanley) score 4.4 — "NVDA - MORGAN STANLEY RENAMES NVIDIA TO TOP PICK"
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