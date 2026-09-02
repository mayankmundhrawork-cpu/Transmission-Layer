# Transmission Layer — board brief · 2026-09-02 19:23Z

data as of **2026-09-02** · 98 series · 10 red / 38 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.4, 2d in regime; vol-pct 0.271, breadth-off 0.529, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.41, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.88, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.09, corr60 0.31, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.04, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.12, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.08, corr60 0.21, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.0009001744811842904)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.49, β 0.2162, p 0.0); driver zc 2.79 → expected 0.721%. Type hit-rate 0.829 (n=2019).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2334, p 0.0); driver zc 2.84 → expected 0.698%. Type hit-rate 0.829 (n=2019).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.37, β -0.2122, p 0.0); driver zc 2.84 → expected -0.634%. Type hit-rate 0.829 (n=2019).
- Track record · residual_reversion: hit-rate **0.5** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2019) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.08] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.34, z20 3.15, zc 2.79, resid-z 2.28 [unexplained], 1d 0.00%, |z20|=3.15; 1y-pct=99
- dyn_bond [EQUITIES]: last 89.79, z20 -2.87, zc 0.11, resid-z 0.00 [quiet], 1d 0.04%, |z20|=2.87; 1y-pct=0
- ust_10y [RATES]: last 4.75, z20 2.04, zc 1.32, resid-z 0.99 [quiet], 1d 0.42%, |z20|=2.04; 1y-pct=99
- tips_10y_real [RATES]: last 2.44, z20 1.28, zc 2.13, resid-z 1.76 [unexplained], 1d 0.83%, 1y-pct=98
- ust_30y [RATES]: last 5.25, z20 0.74, zc 0.71, resid-z 0.58 [quiet], 1d 0.57%, 1y-pct=97
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.346 vs ust_2y, historically leads by 1d
- Source: Here’s another way rising bond yields could take a bite out of Americans’ wallets — MarketWatch Top, 2026-09-02. https://www.marketwatch.com/story/heres-another-way-rising-bond-yields-could-take-a-bite-out-of-americans-wallets-b15a720c?mod=mw_rss_topstories
- Source: Rising global bond yields, FCNR-B inflows and SEBI's CAS to shape market dynamics: HDFC Securities CEO Dhiraj Relli — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/stocks/news/rising-global-bond-yields-fcnr-b-inflows-and-sebis-cas-to-shape-market-dynamics-hdfc-securities-ceo-dhiraj-relli/articleshow/133713847.cms
- Source: Fed's Williams ties rising bond yields to strong economy, CNBC reports — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/us-stocks/news/feds-williams-ties-rising-bond-yields-to-strong-economy-cnbc-reports/articleshow/133713712.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.4] dyn_heromotoco_ns ↓
- dyn_heromotoco_ns [EQUITIES]: last 5300.00, z20 -3.40, zc -3.00, resid-z -2.88 [unexplained], 1d -4.59%, |z20|=3.40
- **Mechanism**: dyn_heromotoco_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho 0.354 via dyn_heromotoco_ns, z -2.76, reacted)
- **India receivers**: dyn_voltas_ns (rho 0.354, z -2.76)
- Source: August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowdown — Mint Markets, 2026-09-02. https://www.livemint.com/market/mark-to-market/august-auto-sales-maruti-tata-mahindra-tvs-motor-11788333468302.html
- Source: Hero MotoCorp, Eicher Motors fall despite strong August sales — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/hero-motocorp-eicher-motors-fall-despite-strong-august-sales/article71418612.ece
- Source: Why Hero MotoCorp shares fell 5% despite record dispatches — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/stock-markets/hero-motocorp-shares-slide-5-as-retail-data-disappoints-despite-record-dispatch-numbers/article71418322.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [AMBER 5.01] commodities · 2 series ↑
- wti [COMMODITIES]: last 90.79, z20 2.18, zc 0.23, resid-z 0.29 [quiet], 1d 0.63%, |z20|=2.18
- brent [COMMODITIES]: last 95.43, z20 1.70, zc 0.30, resid-z 0.37 [quiet], 1d 0.82%, |z20|=1.70
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.512 vs wti
- Source: US yields ease from highs after data as crude prices eyed — Mint Markets, 2026-09-02. https://www.livemint.com/market/us-yields-ease-from-highs-after-data-as-crude-prices-eyed-11788375805189.html
- Source: Prediction platform Kalshi targets US oil market with perpetual WTI contract — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/prediction-platform-kalshi-targets-us-oil-market-with-perpetual-wti-oil-futures-perps-contracts/articleshow/133718527.cms
- Source: Chevron Bets $7 Billion on Venezuela Oil Expansion — OilPrice, 2026-09-02. https://oilprice.com/Latest-Energy-News/World-News/Chevron-Bets-7-Billion-on-Venezuela-Oil-Expansion.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.82] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1536.40, z20 -2.82, zc -1.31, resid-z -0.75 [quiet], 1d -1.95%, |z20|=2.82; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Narayanan of ICICI Pru AMC — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/expert-view-favour-value-over-growth-it-not-an-outright-contra-bet-says-chockalingam-narayanan-of-icici-pru-amc-11788256314458.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 4.56] natgas ↑
- natgas [COMMODITIES]: last 2.99, z20 2.56, zc 0.96, resid-z 0.91 [quiet], 1d 2.89%, |z20|=2.56
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.048 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.004 vs natgas, historically leads by 4d
- Source: Qatar and UAE Turn to Rare LNG Ship Transfers as Hormuz Crisis Drags On — OilPrice, 2026-09-02. https://oilprice.com/Latest-Energy-News/World-News/Qatar-and-UAE-Turn-to-Rare-LNG-Ship-Transfers-as-Hormuz-Crisis-Drags-On.html
- Source: Pakistan Rejects Costly LNG Cargo as Blackout Risk Deepens — OilPrice, 2026-09-02. https://oilprice.com/Latest-Energy-News/World-News/Pakistan-Rejects-Costly-LNG-Cargo-as-Blackout-Risk-Deepens.html
- Source: Asia Spot LNG Prices Hit 5-Month High as Hormuz Blockage Drags On — OilPrice, 2026-09-01. https://oilprice.com/Latest-Energy-News/World-News/Asia-Spot-LNG-Prices-Hit-5-Month-High-as-Hormuz-Blockage-Drags-On.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.15] dyn_coalindia_ns ↑
- dyn_coalindia_ns [EQUITIES]: last 417.85, z20 2.15, zc 3.71, resid-z 3.32 [unexplained], 1d 4.05%, |z20|=2.15
- **Mechanism**: dyn_coalindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/mahanadi-coalfields-files-drhp-with-sebi-for-ipo-coal-india-plans-to-sell-10-stake/article71420575.ece
- Source: Coal India arm Mahanadi Coalfields files IPO papers, plans OFS of up to 66 cr shares — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/ipos/fpos/coal-india-arm-mahanadi-coalfields-files-drhp-for-ipo-ofs-up-to-66-18-crore-shares/articleshow/133705532.cms
- Source: Coal India shares rally despite market slump: Here’s why — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/coal-india-shares-rally-despite-market-slump-heres-why/article71418093.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

### [AMBER 4.14] nifty_50 ↓
- nifty_50 [INDICES]: last 23914.45, z20 -2.14, zc -1.11, resid-z -0.86 [quiet], 1d -0.59%, |z20|=2.14
- **Mechanism**: nifty_50 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.721 via nifty_50, z -1.36, reacted); nifty_midcap_100 (rho 0.64 via nifty_50, z -2.85, reacted); nifty_fmcg (rho 0.611 via nifty_50, z -1.76, reacted); nifty_it (rho 0.521 via nifty_50, z 0.19, quiet); dyn_adanient_bo (rho 0.489 via nifty_50, z -1.68, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.742 vs nifty_50
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.521 vs nifty_50, historically leads by 3d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.625 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.721, z -1.36); nifty_midcap_100 (rho 0.64, z -2.85); nifty_fmcg (rho 0.611, z -1.76); nifty_it (rho 0.521, z 0.19)
- Source: Sensex today | Stock Market Highlights: Sensex ends 373 pts lower at 76,570, Nifty below 24,000; Asian Paints, HDFC Bank fall most — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-2nd-september-2026/article71416736.ece
- Source: Stock Market prediction tomorrow, September 3: What will happen to Sensex, Nifty, Bank Nifty, KOSPI, Nikkei on Thursday — Mint Markets, 2026-09-02. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-september-3-what-will-happen-to-sensex-nifty-bank-nifty-kospi-nikkei-on-thursday-11788342601997.html
- Source: Microcap stock Nukleus Office Solutions rise over 7% despite weak trends on Dalal Street — Mint Markets, 2026-09-02. https://www.livemint.com/market/stock-market-news/microcap-stock-nukleus-office-solutions-rise-over-7-despite-weak-trends-on-dalal-street-11788339391795.html
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

### [AMBER 4.12] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1686.10, z20 2.12, zc -0.71, resid-z -0.84 [quiet], 1d -2.29%, |z20|=2.12; 1y-pct=99
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy surges 130% in 2026, outpacing Tesla, BYD — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/ather-energy-surges-130-in-2026-outpacing-tesla-byd/article71414201.ece
- Source: Ather Energy’s 130% stock surge leaves Tesla and BYD behind in 2026 — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/stocks/news/ather-energys-130-stock-surge-leaves-tesla-and-byd-behind-in-2026/articleshow/133672575.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
wheat ↑ (4.09), indices · 3 series ↓ (4.0), nikkei_225 ↓ (3.86), dyn_dell ↑ (3.62), dyn_tataelxsi_ns ↓ (3.53), dyn_havells_ns ↓ (3.45), midcap_largecap_ratio ↑ (3.43), gold_silver_ratio ↓ (3.27), bovespa ↑ (3.17), dyn_nvda ↑ (3.1), nifty_midcap_100 ↓ (2.85), dyn_voltas_ns ↓ (2.76)

## India macro
- nifty_50: 23914.4492 (1d -0.59%, z20 -2.14, flag amber)
- nifty_midcap_100: 63006.8984 (1d -0.52%, z20 -2.85, flag red)
- usd_inr: 94.9600 (1d -0.16%, z20 -0.82, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6347 (1d 0.07%, z20 0.43, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.5 — "Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake"
- COALINDIA.NS (COAL INDIA LTD) score 85.3 — "Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.2 — "Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake"
- INDIANB.NS (INDIAN BANK) score 75.5 — "DUTCH CENTRAL BANK SHIFTS GOLD TO LONDON The Dutch central bank moved 86 tons of gold from"
- BAC (Bank of America Corporation) score 66.7 — "DUTCH CENTRAL BANK SHIFTS GOLD TO LONDON The Dutch central bank moved 86 tons of gold from"
- COIN (Coinbase Global, Inc.) score 59.7 — "Rising global bond yields, FCNR-B inflows and SEBI's CAS to shape market dynamics: HDFC Se"
- BOND (PIMCO Active Bond Exchange-Tra) score 59.2 — "FED’S WILLIAMS: STRONG ECONOMY DRIVING BOND YIELDS New York Fed President John Williams sa"
- HDB (HDFC Bank Limited) score 57.3 — "DUTCH CENTRAL BANK SHIFTS GOLD TO LONDON The Dutch central bank moved 86 tons of gold from"
- IDBI.NS (IDBI BANK LIMITED) score 54.6 — "DUTCH CENTRAL BANK SHIFTS GOLD TO LONDON The Dutch central bank moved 86 tons of gold from"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 54.6 — "DUTCH CENTRAL BANK SHIFTS GOLD TO LONDON The Dutch central bank moved 86 tons of gold from"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 54.6 — "DUTCH CENTRAL BANK SHIFTS GOLD TO LONDON The Dutch central bank moved 86 tons of gold from"
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.6 — "FED’S WILLIAMS: STRONG ECONOMY DRIVING BOND YIELDS New York Fed President John Williams sa"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.2 — "FED’S WILLIAMS: STRONG ECONOMY DRIVING BOND YIELDS New York Fed President John Williams sa"
- TECH (Bio-Techne Corp) score 35.2 — "FED’S WILLIAMS: STRONG ECONOMY DRIVING BOND YIELDS New York Fed President John Williams sa"
- CHKP (Check Point Software Technolog) score 33.8 — "Pranav Constructions announces IPO price band, issue opens September 7. Check details"
- LTH (Life Time Group Holdings, Inc.) score 29.7 — "BESSENT ON IRAN, SANCTIONS: GOING TO SYSTEMICALLY TAKE OUT BAD ACTORS -FOX NEWS INTERVIEW "
- OHI (Omega Healthcare Investors, In) score 29.4 — "Swiggy shareholders' alert! Know why September 7 is a key date for you — food delivery sto"
- 301077.SZ (CHINASTARS) score 29.0 — "China’s corruption investigation procedures"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.7 — "IPO-bound Simple Energy eyes large fundraise to enhance production capacity, supply chain"
- NVDA (NVIDIA Corporation) score 16.6 — "SPCX - OPPENHEIMER LIFTS SPACEX TARGET TO $280 Oppenheimer raised its SpaceX price target "
- PCJEWELLER.NS (PC JEWELLER LTD) score 15.2 — "Deepa Jewellers IPO GMP today: Grey market hints 25% listing gain; check subscription, rev"
- JIOFIN.BO (Jio Financial Services Limited) score 14.6 — "JM Financial Asset Management garners Rs 700 crore from maiden pre-IPO fund"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.5 — "Rays of Belief IPO sees retail frenzy; QIB cold shoulder on day 2"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.7 — "Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.6 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.1 — "JM Financial Asset Management garners Rs 700 crore from maiden pre-IPO fund"
- META (Meta) score 8.2 — "META - META DISABLES CAMERAS ON SOME TAMPERED SMART GLASSES - SEMAFOR"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "How Adani Group stocks are performing today after share prices plunged yesterday | Top gai"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.0 — "Why auto stocks are down today? Eicher, Tata Motors, Hyundai, Bajaj Auto and others - Chec"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.9 — "Why auto stocks are down today? Eicher, Tata Motors, Hyundai, Bajaj Auto and others - Chec"
- MS (Morgan Stanley) score 7.4 — "JPMORGAN: RISING YIELDS WON’T KILL STOCK RALLY JPMorgan remains bullish on global equities"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.2 — "TRUMP: THE UNITED STATES IS, AS WE SPEAK, STRIKING IRANIAN TARGETS NEAR THE STRAIT OF TRUM"
- VT (Vanguard Total World Stock Ind) score 6.7 — "What’s behind the selloff in world bond markets?"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.0 — "Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Na"
- DELL (Dell Technologies Inc.) score 3.8 — "Wall Street rises amid renewed US-Iran clashes, Dell jumps 6.9%, Nvidia gains 1.2%, Tesla "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.3 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.8 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 1.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.7 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas reported strong growth in June quarter, but failed to impress"

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