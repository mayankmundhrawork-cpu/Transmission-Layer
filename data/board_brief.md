# Transmission Layer — board brief · 2026-11-25 14:15Z

data as of **2026-11-25** · 97 series · 9 red / 42 amber · 8 events surfaced (34 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.882, 8d in regime; vol-pct 0.996, breadth-off 0.769, Markov P(high-vol) 0.588)
- [WEAK] **safe_haven_gold** — corr20 -0.15, corr60 -0.27, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.1, corr60 0.08, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.19, corr60 -0.01, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.29, corr60 0.36, last shift 2026-10-07. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **11 of 88** scanned series survive multiplicity control (effective p ≤ 0.009880031515541177)
- **SETUP** vix → asx_200: leads 1d (ccf -0.484, β -0.0413, p 0.0); driver zc 1.8 → expected -0.807%. Type hit-rate 0.818 (n=2160).
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.483, β 0.2082, p 0.0); driver zc -2.02 → expected -0.569%. Type hit-rate 0.818 (n=2160).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.458, β 0.2397, p 0.0); driver zc -2.21 → expected -0.571%. Type hit-rate 0.818 (n=2160).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.257, β -0.029, p 0.00029); driver zc 1.8 → expected -0.566%. Type hit-rate 0.818 (n=2160).
- Track record · residual_reversion: hit-rate **0.509** (n=1140) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2160) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.01] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 88.53, z20 2.69, zc n/a, resid-z n/a [quiet], 1d 1.31%, GSR>85 (extreme high); |z20|=2.69; 1y-pct=100
- comex_silver [COMMODITIES]: last 39.62, z20 -2.36, zc -0.66, resid-z 0.13 [quiet], 1d -2.80%, |z20|=2.36; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3507.50, z20 -2.20, zc -0.57, resid-z -3.12 [unexplained], 1d -1.53%, |z20|=2.20; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.59 via comex_gold, z -0.55, quiet); dyn_karurvysya_ns (rho 0.496 via comex_gold, z 0.65, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.574 vs comex_silver, historically leads by 4d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.52 vs gold_silver_ratio, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.59, z -0.55); dyn_karurvysya_ns (rho 0.496, z 0.65)
- Source: India holds 84% of its gold reserves domestically as RBI brings more gold onshore — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/gold/india-holds-84-of-its-gold-reserves-domestically-as-rbi-brings-more-gold-onshore/article71742772.ece
- Source: Gold price prediction: Despite 27% decline from January peak, UBS still retains  ₹1.50 lakh/10 gram target for 2027 — Mint Markets, 2026-11-25. https://www.livemint.com/market/commodities/gold-price-prediction-despite-27-decline-from-january-peak-ubs-still-retains-rs-1-50-lakh-10-gram-target-for-2027-11795601553956.html
- Source: India’s gold loan portfolio surges 60.6% to ₹23.3 lakh crore, smaller cities drive growth: Report — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/money-and-banking/indias-gold-loan-portfolio-surges-606-to-233-lakh-crore-smaller-cities-drive-growth-report/article71741372.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 8.77] cross-asset · 5 series ↓
- dyn_ms [EQUITIES]: last 168.80, z20 -2.35, zc -0.81, resid-z 0.74 [quiet], 1d -2.20%, |z20|=2.35
- dyn_gs [EQUITIES]: last 806.15, z20 -2.34, zc -0.75, resid-z -0.65 [quiet], 1d -2.12%, |z20|=2.34
- dax [INDICES]: last 24877.44, z20 -2.06, zc -0.40, resid-z -0.75 [quiet], 1d -0.56%, |z20|=2.06
- stoxx_50 [INDICES]: last 5957.32, z20 -2.03, zc -0.58, resid-z -0.30 [quiet], 1d -0.77%, |z20|=2.03
- vix [INDICES]: last 31.51, z20 1.84, zc 1.80, resid-z n/a [moved], 1d 19.54%, 1-session move +19.54% ≥ 15.0%; |z20|=1.84; 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-02 (z-distance 0.74).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.491 via dax, z -0.55, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.901 vs dax
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.644 vs dyn_gs, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.491, z -0.55)
- Source: Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Sachs-Sees-US-Natural-Gas-Demand-Surging-on-Data-Center-Boom.html
- Source: Goldman Sachs, SocGen buy Rs 920 crore stake in Lenskart — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/stocks/news/goldman-sachs-socgen-buy-rs-920-crore-stake-in-lenskart/articleshow/136145273.cms
- Source: SPY $QQQ - GOLDMAN SAYS MARKET POSITIONING SIGNALS ABOVE-AVERAGE S&P 500 RETURNS Goldman Sachs says its sentiment and positioning indicator has fallen to the 36th percentile, its lowest since Liberation Day, historically a favorable level for future equity returns. Strategist Christian Mueller-Gliss — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39115
- Historical analogues: 2026-04-02 (d=0.74), 2025-10-28 (d=1.12), 2025-04-02 (d=1.77)

### [RED 7.7] natgas ↑
- natgas [COMMODITIES]: last 3.63, z20 2.70, zc 2.26, resid-z 1.07 [moved], 1d 9.18%, 1-session move +9.18% ≥ 5.0%; |z20|=2.70
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global LNG Supply Crunch Set to Spill Into 2027 — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Global-LNG-Supply-Crunch-Set-to-Spill-Into-2027.html
- Source: Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Sachs-Sees-US-Natural-Gas-Demand-Surging-on-Data-Center-Boom.html
- Source: Iran Faces a Deepening Natural Gas Crisis Ahead of Winter — OilPrice, 2026-11-24. https://oilprice.com/Energy/Energy-General/Iran-Faces-a-Deepening-Natural-Gas-Crisis-Ahead-of-Winter.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 7.63] usd_inr ↓
- usd_inr [FX]: last 92.22, z20 -2.63, zc -1.81, resid-z -0.71 [moved], 1d -0.75%, 20d range extreme; |z20|=2.63; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.43 via usd_inr, z 0.73, quiet); dyn_havells_ns (rho -0.411 via usd_inr, z 1.21, reacted); nifty_it (rho -0.409 via usd_inr, z 0.29, quiet); dyn_tataelxsi_ns (rho -0.362 via usd_inr, z 0.43, quiet); dyn_inoxindia_ns (rho -0.351 via usd_inr, z 2.08, reacted)
- **India receivers**: dyn_indianb_ns (rho -0.43, z 0.73); dyn_havells_ns (rho -0.411, z 1.21); nifty_it (rho -0.409, z 0.29); dyn_tataelxsi_ns (rho -0.362, z 0.43)
- Source: Rupee soars 69 paise to settle at its eight-month high of 92.16 against US dollar — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/forex/rupee-soars-69-paise-to-settle-at-its-eight-month-high-of-9216-against-us-dollar/article71742189.ece
- Source: Rupee scales 8-month high after holiday as foreign flows to Indian equities persist — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-scales-8-month-high-after-holiday-as-foreign-flows-to-indian-equities-persist/articleshow/136158513.cms
- Source: Sensex today | Stock Market Highlights: Sensex surges 1,502 points, Nifty reclaims 25,800 as rupee hits eight-month high — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/sensex-nifty50-highlights-stock-market-updates-25-november-2026/article71734420.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.02] brent ↓
- brent [COMMODITIES]: last 89.30, z20 -1.02, zc -1.06, resid-z 0.87 [quiet], 1d -2.30%, 1-session move -2.30% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Big Oil and Big Tech Lobby EU for Faster Gas-Fired Data Center Permits — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Big-Oil-and-Big-Tech-Lobby-EU-for-Faster-Gas-Fired-Data-Center-Permits.html
- Source: RBI may opt for 25 bps rate hike as oil eases, inflation risks persist: Baroda BNP Paribas MF CIO — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/stocks/news/rbi-may-opt-for-25-bps-rate-hike-as-oil-eases-inflation-risks-persist-baroda-bnp-paribas-mf-cio/articleshow/136162711.cms
- Source: Iran War Is Pushing Record Numbers of Fuel Tankers Into Crude Trade — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Iran-War-Is-Pushing-Record-Numbers-of-Fuel-Tankers-Into-Crude-Trade.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.43] usd_mxn ↑
- usd_mxn [FX]: last 19.82, z20 5.43, zc 3.29, resid-z 4.57 [unexplained], 1d 3.37%, |z20|=5.43; 1y-pct=100
- **Mechanism**: usd_mxn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-07-10 (d=0.0), 2025-01-31 (d=0.01), 2026-07-01 (d=0.02)

### [AMBER 5.06] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 102.38, z20 -1.74, zc -1.25, resid-z 1.63 [unexplained], 1d -5.88%, 1y-pct=0
- btc_usd [CRYPTO]: last 58229.22, z20 -1.57, zc -0.96, resid-z -0.85 [quiet], 1d -2.54%, |z20|=1.57; 1y-pct=0
- eth_usd [CRYPTO]: last 1634.21, z20 -1.41, zc -0.68, resid-z -0.83 [quiet], 1d -2.59%, 1y-pct=4
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.24).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.607 vs btc_usd
- Source: Precious metals plunge in Indian markets on global cues, strong currencies — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/gold/precious-metals-plunge-in-indian-markets-on-global-cues-strong-currencies/article71742954.ece
- Source: Global convulsions, courtesy AI stocks, creates a $385 billion winner — India — Mint Markets, 2026-11-25. https://www.livemint.com/market/stock-market-news/india-stock-market-sensex-nifty-today-ai-stocks-11795607301635.html
- Source: Global LNG Supply Crunch Set to Spill Into 2027 — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Global-LNG-Supply-Crunch-Set-to-Spill-Into-2027.html
- Historical analogues: 2025-10-22 (d=0.24), 2025-10-30 (d=0.37), 2025-03-31 (d=0.39)

### [AMBER 4.96] rates · 2 series ↑
- ig_oas [RATES]: last 0.97, z20 2.13, zc 2.78, resid-z 0.71 [priced], 1d -1.02%, |z20|=2.13; 1y-pct=99
- hy_oas [RATES]: last 3.63, z20 1.94, zc 3.00, resid-z 0.45 [priced], 1d -3.46%, |z20|=1.94; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.481 via ig_oas, z -2.06, reacted); nifty_it (rho 0.385 via ig_oas, z 0.29, quiet)
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.515 vs hy_oas, historically leads by 2d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.512 vs hy_oas, historically leads by 3d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.546 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.481, z -2.06); nifty_it (rho 0.385, z 0.29)
- Source: Dividend vs fixed deposits: 5 high yield stocks generating better income than FDs - CyberTech, Majestic Auto, to Premco — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/dividend-vs-fixed-deposits-5-high-yield-stocks-generating-better-income-than-fds-cybertech-majestic-auto-to-premco-11795463444218.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

## Watchlist (below surfacing floor)
dyn_tgt ↑ (4.84), indices · 2 series ↓ (4.53), fx · 2 series ↓ (4.53), dyn_crwv ↓ (3.44), dyn_tech ↑ (3.4), dyn_lth ↑ (3.25), dyn_bajfinance_ns ↑ (3.21), dyn_eternal_ns ↑ (3.08), shanghai_comp ↓ (3.01), dyn_nvda ↓ (2.92), dyn_2545_tw ↓ (2.87), cross-asset · 2 series ↓ (2.75)

## India macro
- nifty_50: 25819.2500 (1d 1.85%, z20 1.30, flag none)
- nifty_midcap_100: 61582.6992 (1d 0.29%, z20 0.85, flag none)
- usd_inr: 92.2200 (1d -0.75%, z20 -2.63, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.3851 (1d -1.53%, z20 -2.06, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 75.2 — "Indian stocks close to wiping out 2026 losses as foreign money floods back"
- INOXINDIA.NS (INOX INDIA LIMITED) score 70.5 — "Indian stocks close to wiping out 2026 losses as foreign money floods back"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 70.2 — "Indian stocks close to wiping out 2026 losses as foreign money floods back"
- NVDA (NVIDIA Corporation) score 64.5 — "What the options market says to do with Nvidia’s stock — and the rest of the stock market"
- INDIANB.NS (INDIAN BANK) score 56.0 — "Indian stocks close to wiping out 2026 losses as foreign money floods back"
- BAC (Bank of America Corporation) score 41.5 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- TGT (Target Corporation) score 39.9 — "Chartered Speed targets December IPO after Iran war disruption"
- HDB (HDFC Bank Limited) score 38.1 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- OHI (Omega Healthcare Investors, In) score 35.8 — "Why are investors betting on Abercrombie's growth story?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.0 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 34.0 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.0 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.5 — "HFCL vs Sterlite Technologies: Both multibagger stocks hit 5% lower circuit again - Which "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.1 — "HFCL vs Sterlite Technologies: Both multibagger stocks hit 5% lower circuit again - Which "
- TECH (Bio-Techne Corp) score 32.1 — "HFCL vs Sterlite Technologies: Both multibagger stocks hit 5% lower circuit again - Which "
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 26.5 — "Huang boost fades quickly as AI fears sink TSMC, SK Hynix shares"
- BLLN (BillionToOne, Inc.) score 25.1 — "PhonePe resumes IPO process; targets February-March listing at $12-15 billion valuation"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.2 — "UK Energy Price Cap Jumps 26% in January, Highest Since 2023"
- 301077.SZ (CHINASTARS) score 21.1 — "China Goes on Oil Buying Spree as Crude Prices Slide"
- CHKP (Check Point Software Technolog) score 20.4 — "Multibagger Alert! Up 102% in 1 year, more rally seen in this small-cap power stock - here"
- COIN (Coinbase Global, Inc.) score 19.8 — "Global LNG Supply Crunch Set to Spill Into 2027"
- LTH (Life Time Group Holdings, Inc.) score 19.4 — "CIA AND U.S. INTELLIGENCE CHIEF'S OFFICE HIT BY CYBERSECURITY BREACH — NYT The CIA and Off"
- BOND (PIMCO Active Bond Exchange-Tra) score 15.2 — "Indian bonds rise as oil eases, traders await RBI rate decision"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.9 — "Top Nifty Bank gainer today: HDFC Bank shares jump 4% as index soars 2%— Should you buy or"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.3 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.3 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.1 — "ANT - ANTHROPIC SHARES EXTEND LOSSES; LAST DOWN 12.7%"
- JIOFIN.BO (Jio Financial Services Limited) score 10.1 — "Jio Financial Services vs Reliance vs Jio Platforms shares: Which Mukesh Ambani's stock to"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.0 — "Bajaj Auto Share Price Highlights: Bajaj Auto Stock Price History"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.5 — "CITADEL SECURITIES SMASHES ANNUAL REVENUE RECORD IN JUST NINE MONTHS Citadel Securities ge"
- META (Meta) score 8.5 — "MCX rates: Gold crashes 13%, silver plunges 20% in Nov 2026; is worst over? What should pr"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.7 — "Climate Finance Dispute Derails COP31 Negotiations"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.4 — "Top stocks to watch today: Tata Steel, Lenskart, Adani Enterprises, PhysicsWallah, Hindalc"
- GS (Goldman Sachs Group, Inc. (The) score 5.2 — "Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom"
- MS (Morgan Stanley) score 3.6 — "The S&P 500 is headed to 8,200 — and downturns like this one are actually part of the reas"
- TATASTEEL.BO (TATA STEEL LTD.) score 3.0 — "Why APL Apollo Tubes shares crashed 15% today to plunge at 52-week low; downgrade from bro"
- CRWV (CoreWeave, Inc.) score 2.8 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- ETERNAL.NS (ETERNAL LIMITED) score 1.9 — "BSE, Eternal, Titan, SBI among 18 Nifty 50 stocks that rallied 10–43% in 2026; what's driv"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.3 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.8 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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