# Transmission Layer — board brief · 2026-11-25 23:06Z

data as of **2026-11-25** · 97 series · 8 red / 45 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.93, 8d in regime; vol-pct 0.978, breadth-off 0.882, Markov P(high-vol) 0.213)
- [WEAK] **safe_haven_gold** — corr20 -0.13, corr60 -0.24, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.02, corr60 0.07, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.04, corr60 0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.18, corr60 -0.01, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.27, corr60 0.34, last shift 2026-10-07. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 88** scanned series survive multiplicity control (effective p ≤ 0.000779424725164013)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.509** (n=1140) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2160) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.8] cross-asset · 4 series ↓
- gold_silver_ratio [DERIVED]: last 86.82, z20 2.13, zc n/a, resid-z n/a [quiet], 1d -0.65%, GSR>85 (extreme high); |z20|=2.13; 1y-pct=99
- comex_silver [COMMODITIES]: last 41.67, z20 -1.82, zc 0.53, resid-z 0.25 [quiet], 1d 2.23%, |z20|=1.82; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 5.48, z20 -1.70, zc 1.02, resid-z 1.70 [unexplained], 1d 2.22%, |z20|=1.70; co-occur[metal_copper] suppressed: channel WEAK
- comex_gold [COMMODITIES]: last 3617.80, z20 -1.58, zc 0.58, resid-z -2.50 [unexplained], 1d 1.57%, |z20|=1.58; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.58 via comex_gold, z -0.55, quiet); dyn_karurvysya_ns (rho 0.488 via comex_gold, z 0.65, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.567 vs comex_silver, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.58, z -0.55); dyn_karurvysya_ns (rho 0.488, z 0.65)
- Source: Copper slumps to lowest in 11 months as investors flee — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/commodities/copper-slumps-to-lowest-in-11-months-as-investors-flee/articleshow/136172100.cms
- Source: MCX gold plunges  ₹4,420/10g, silver sheds nearly  ₹8,800/kg as PCE data fuels December Fed rate hike bets — Mint Markets, 2026-11-25. https://www.livemint.com/market/commodities/mcx-gold-plunges-rs-4-500-10g-silver-sheds-nearly-rs-8-800-kg-as-pce-data-fuels-december-fed-rate-hike-fears-11795621934097.html
- Source: RBI raises share of domestically held gold reserves, data shows — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/forex/forex-news/rbi-raises-share-of-domestically-held-gold-reserves-data-shows/articleshow/136165807.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 7.95] natgas ↑
- natgas [COMMODITIES]: last 3.67, z20 2.95, zc 2.61, resid-z 3.55 [unexplained], 1d 10.59%, 1-session move +10.59% ≥ 5.0%; |z20|=2.95
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global LNG Supply Crunch Set to Spill Into 2027 — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Global-LNG-Supply-Crunch-Set-to-Spill-Into-2027.html
- Source: Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Sachs-Sees-US-Natural-Gas-Demand-Surging-on-Data-Center-Boom.html
- Source: Iran Faces a Deepening Natural Gas Crisis Ahead of Winter — OilPrice, 2026-11-24. https://oilprice.com/Energy/Energy-General/Iran-Faces-a-Deepening-Natural-Gas-Crisis-Ahead-of-Winter.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 7.63] usd_inr ↓
- usd_inr [FX]: last 92.22, z20 -2.63, zc -1.81, resid-z -1.11 [moved], 1d -0.75%, 20d range extreme; |z20|=2.63
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.43 via usd_inr, z 0.73, quiet); dyn_havells_ns (rho -0.411 via usd_inr, z 1.21, reacted); nifty_it (rho -0.409 via usd_inr, z 0.29, quiet); dyn_tataelxsi_ns (rho -0.362 via usd_inr, z 0.43, quiet); dyn_inoxindia_ns (rho -0.351 via usd_inr, z 2.08, reacted)
- **India receivers**: dyn_indianb_ns (rho -0.43, z 0.73); dyn_havells_ns (rho -0.411, z 1.21); nifty_it (rho -0.409, z 0.29); dyn_tataelxsi_ns (rho -0.362, z 0.43)
- Source: Rupee hits eight-month high as foreign inflows lift markets; Nifty nears record peak — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/rupee-hits-eight-month-high-as-foreign-inflows-lift-markets-nifty-nears-record-peak/article71743427.ece
- Source: Rupee soars 69 paise to settle at its eight-month high of 92.16 against US dollar — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/forex/rupee-soars-69-paise-to-settle-at-its-eight-month-high-of-9216-against-us-dollar/article71742189.ece
- Source: Rupee scales 8-month high after holiday as foreign flows to Indian equities persist — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-scales-8-month-high-after-holiday-as-foreign-flows-to-indian-equities-persist/articleshow/136158513.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.6] cross-asset · 6 series ↓
- stoxx_50 [INDICES]: last 5904.97, z20 -2.45, zc -1.23, resid-z -2.26 [unexplained], 1d -1.65%, |z20|=2.45
- dax [INDICES]: last 24736.99, z20 -2.32, zc -0.80, resid-z -1.88 [unexplained], 1d -1.12%, |z20|=2.32
- dyn_ms [EQUITIES]: last 167.53, z20 -2.15, zc -0.29, resid-z -1.14 [quiet], 1d -0.75%, |z20|=2.15
- dyn_gs [EQUITIES]: last 800.45, z20 -2.12, zc -0.25, resid-z -1.23 [quiet], 1d -0.69%, |z20|=2.12; 1y-pct=5
- ftse_100 [INDICES]: last 10433.66, z20 -1.68, zc -0.43, resid-z -0.73 [quiet], 1d -0.32%, |z20|=1.68
- vix [INDICES]: last 28.32, z20 1.18, zc 0.68, resid-z n/a [quiet], 1d 7.44%, 1y-pct=98
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-01 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.487 via dax, z -0.55, quiet); dyn_kaynes_ns (rho 0.428 via ftse_100, z -2.31, reacted); dyn_tataelxsi_ns (rho 0.359 via ftse_100, z 0.43, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.9 vs stoxx_50
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.762 vs dyn_gs
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.526 vs stoxx_50, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.515 vs stoxx_50, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.487, z -0.55); dyn_kaynes_ns (rho 0.428, z -2.31); dyn_tataelxsi_ns (rho 0.359, z 0.43)
- Source: SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Christian Mueller-Glissmann warns that markets remain fragile as investors question AI investment returns and elevated borrowing costs. Goldman's risk appetite indicator has not reached levels typically associated — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39170
- Source: CBOE VOLATILITY INDEX UP 4.54 POINTS AT 30.88 — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39169
- Source: Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Sachs-Sees-US-Natural-Gas-Demand-Surging-on-Data-Center-Boom.html
- Historical analogues: 2026-04-01 (d=0.82), 2025-10-31 (d=1.49), 2025-10-24 (d=1.62)

### [AMBER 5.79] wti ↓
- wti [COMMODITIES]: last 84.15, z20 -0.79, zc 1.08, resid-z 0.71 [quiet], 1d 2.56%, 1-session move +2.56% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.461 via wti, z 2.08, reacted); nifty_fmcg (rho -0.451 via wti, z 2.14, reacted); dyn_adanient_bo (rho -0.443 via wti, z 0.14, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.778 vs wti
- **India receivers**: dyn_inoxindia_ns (rho -0.461, z 2.08); nifty_fmcg (rho -0.451, z 2.14); dyn_adanient_bo (rho -0.443, z 0.14)
- Source: Oil Traders Ignore Growing Threat to Persian Gulf Supply — OilPrice, 2026-11-25. https://oilprice.com/Energy/Crude-Oil/Oil-Traders-Ignore-Growing-Threat-to-Persian-Gulf-Supply.html
- Source: U.S. Rig Count Holds Steady as Oil Production Hits Fifth Straight Record — OilPrice, 2026-11-25. https://oilprice.com/Energy/Crude-Oil/US-Rig-Count-Holds-Steady-as-Oil-Production-Hits-Fifth-Straight-Record.html
- Source: U.S.-Backed Consortium Signs Deal for Lukoil's International Oil Empire — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/US-Backed-Consortium-Signs-Deal-for-Lukoils-International-Oil-Empire.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 5.12] rates · 2 series ↑
- hy_oas [RATES]: last 3.72, z20 2.29, zc 0.71, resid-z 0.43 [quiet], 1d 2.48%, |z20|=2.29; 1y-pct=99
- ig_oas [RATES]: last 0.98, z20 2.17, zc 0.45, resid-z 0.00 [quiet], 1d 1.03%, |z20|=2.17; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.486 via ig_oas, z -2.06, reacted); nifty_it (rho 0.389 via ig_oas, z 0.29, quiet)
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.502 vs hy_oas, historically leads by 3d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.541 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.486, z -2.06); nifty_it (rho 0.389, z 0.29)
- Source: Dividend vs fixed deposits: 5 high yield stocks generating better income than FDs - CyberTech, Majestic Auto, to Premco — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/dividend-vs-fixed-deposits-5-high-yield-stocks-generating-better-income-than-fds-cybertech-majestic-auto-to-premco-11795463444218.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [RED 4.68] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 163.83, z20 2.68, zc 1.04, resid-z 0.00 [quiet], 1d 2.82%, |z20|=2.68
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: LG Electronics shares to be in focus as promoter to sell 2% stake to meet public float norms; check details — Mint Markets, 2026-11-25. https://www.livemint.com/market/lg-electronics-shares-to-be-in-focus-as-promoter-to-sell-2-stake-to-meet-public-float-norms-check-details-11795612944008.html
- Source: NSE shares hit record high after ICICI Securities initiates coverage with Buy; check target price and key triggers — Mint Markets, 2026-11-25. https://www.livemint.com/market/stock-market-news/nse-shares-hit-record-high-after-icici-securities-initiates-coverage-with-buy-check-target-price-and-key-triggers-11795600817257.html
- Source: Multibagger Alert! Up 102% in 1 year, more rally seen in this small-cap power stock - here's why | Check target, upside — Mint Markets, 2026-11-25. https://www.livemint.com/market/stock-market-news/multibagger-alert-up-102-in-1-year-more-rally-seen-in-this-small-cap-power-stock-heres-why-check-target-upside-11795594809008.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 4.53] indices · 2 series ↓
- kospi [INDICES]: last 4701.90, z20 -1.69, zc -1.48, resid-z -1.67 [unexplained], 1d -6.08%, |z20|=1.69
- nikkei_225 [INDICES]: last 57117.11, z20 -1.67, zc -1.00, resid-z -1.33 [quiet], 1d -2.60%, |z20|=1.67
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.43 via nikkei_225, z 0.85, quiet)
- Watch next: dyn_2545_tw (co-move) — not yet - watch; rho 0.579 vs kospi, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.43, z 0.85)
- Source: Stock market outlook today,25 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-25. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-25-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11795566965791.html
- Source: Asian markets follow Wall Street: Nikkei, Kospi jump up to 8% as Jensen Huang’s return sparks rally in AI stocks — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/asian-markets-follow-wall-street-nikkei-kospi-jump-up-to-8-as-jensen-huang-s-return-sparks-rally-in-ai-stocks-11795485047635.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-07-02 (d=0.5), 2025-04-21 (d=1.1)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↓ (4.33), usd_mxn ↑ (4.29), fx · 2 series ↓ (4.16), equities · 2 series ↓ (4.14), dyn_tgt ↑ (3.8), dyn_bajfinance_ns ↑ (3.21), dyn_eternal_ns ↑ (3.08), dyn_lth ↑ (3.06), shanghai_comp ↓ (3.01), dyn_2545_tw ↓ (2.87), cross-asset · 2 series ↓ (2.75), dyn_4417_t ↑ (2.51)

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
- COALINDIA.NS (COAL INDIA LTD) score 73.0 — "USTR PROPOSES TARIFF RATES OF UP TO 25% FOR CAMBODIA, INDONESIA, SOUTH KOREA, MALAYSIA, TA"
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.7 — "USTR PROPOSES TARIFF RATES OF UP TO 25% FOR CAMBODIA, INDONESIA, SOUTH KOREA, MALAYSIA, TA"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 68.4 — "USTR PROPOSES TARIFF RATES OF UP TO 25% FOR CAMBODIA, INDONESIA, SOUTH KOREA, MALAYSIA, TA"
- NVDA (NVIDIA Corporation) score 66.3 — "CRWV $ORCL $NVDA - AI CREDIT RISKS OVERSHADOW JENSEN HUANG'S RETURN Mounting debt concerns"
- INDIANB.NS (INDIAN BANK) score 54.5 — "BANKS SELL AI DATA CENTER LOANS AS FINANCING RISKS MOUNT Major banks are reducing exposure"
- BAC (Bank of America Corporation) score 41.1 — "BANKS SELL AI DATA CENTER LOANS AS FINANCING RISKS MOUNT Major banks are reducing exposure"
- TGT (Target Corporation) score 37.7 — "Baroda BNP Paribas Mutual Fund targets ₹1.50 lakh crore AUM in 5 years"
- HDB (HDFC Bank Limited) score 37.0 — "BANKS SELL AI DATA CENTER LOANS AS FINANCING RISKS MOUNT Major banks are reducing exposure"
- OHI (Omega Healthcare Investors, In) score 35.9 — "SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Chr"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 33.2 — "BANKS SELL AI DATA CENTER LOANS AS FINANCING RISKS MOUNT Major banks are reducing exposure"
- IDBI.NS (IDBI BANK LIMITED) score 33.2 — "BANKS SELL AI DATA CENTER LOANS AS FINANCING RISKS MOUNT Major banks are reducing exposure"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 33.2 — "BANKS SELL AI DATA CENTER LOANS AS FINANCING RISKS MOUNT Major banks are reducing exposure"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.8 — "HP’s stock is a standout gainer in the tech selloff, as an earnings beat still matters"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 31.4 — "HP’s stock is a standout gainer in the tech selloff, as an earnings beat still matters"
- TECH (Bio-Techne Corp) score 31.4 — "HP’s stock is a standout gainer in the tech selloff, as an earnings beat still matters"
- BLLN (BillionToOne, Inc.) score 28.0 — "PhonePe revives IPO plans, eyes $12-15 billion valuation; filing likely in a fortnight"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 27.4 — "CRWV $ORCL $NVDA - AI CREDIT RISKS OVERSHADOW JENSEN HUANG'S RETURN Mounting debt concerns"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.3 — "UK Energy Bills Set to Soar 26% as Iran War Drives Up Gas Prices"
- 301077.SZ (CHINASTARS) score 21.3 — "TRUMP ADMINISTRATION PROPOSES NEW TARIFFS ON 14 MAJOR TRADING PARTNERS The U.S. has conclu"
- LTH (Life Time Group Holdings, Inc.) score 19.8 — "Nasdaq 100 plunges nearly 5%, briefly enters bear-market zone as AI fears and fresh tariff"
- CHKP (Check Point Software Technolog) score 18.8 — "Multibagger Alert! Up 102% in 1 year, more rally seen in this small-cap power stock - here"
- COIN (Coinbase Global, Inc.) score 18.1 — "Global LNG Supply Crunch Set to Spill Into 2027"
- BOND (PIMCO Active Bond Exchange-Tra) score 14.0 — "Indian bonds rise as oil eases, traders await RBI rate decision"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.7 — "Top Nifty Bank gainer today: HDFC Bank shares jump 4% as index soars 2%— Should you buy or"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.1 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.1 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.2 — "ANT - ANTHROPIC SHARES EXTEND LOSSES; LAST DOWN 12.7%"
- JIOFIN.BO (Jio Financial Services Limited) score 9.3 — "Jio Financial Services vs Reliance vs Jio Platforms shares: Which Mukesh Ambani's stock to"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.3 — "Bajaj Auto Share Price Highlights: Bajaj Auto Stock Price History"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.8 — "CITADEL SECURITIES SMASHES ANNUAL REVENUE RECORD IN JUST NINE MONTHS Citadel Securities ge"
- META (Meta) score 7.8 — "MCX rates: Gold crashes 13%, silver plunges 20% in Nov 2026; is worst over? What should pr"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.1 — "Climate Finance Dispute Derails COP31 Negotiations"
- GS (Goldman Sachs Group, Inc. (The) score 5.8 — "SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Chr"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.0 — "Top stocks to watch today: Tata Steel, Lenskart, Adani Enterprises, PhysicsWallah, Hindalc"
- CRWV (CoreWeave, Inc.) score 4.6 — "CRWV $ORCL $NVDA - AI CREDIT RISKS OVERSHADOW JENSEN HUANG'S RETURN Mounting debt concerns"
- MS (Morgan Stanley) score 4.3 — "JPMorgan Sees $450 Billion AI Debt Blitz in 2027 Before Plateau"
- TATASTEEL.BO (TATA STEEL LTD.) score 2.8 — "Why APL Apollo Tubes shares crashed 15% today to plunge at 52-week low; downgrade from bro"
- ETERNAL.NS (ETERNAL LIMITED) score 1.8 — "BSE, Eternal, Titan, SBI among 18 Nifty 50 stocks that rallied 10–43% in 2026; what's driv"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.2 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
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