# Transmission Layer — board brief · 2026-09-08 08:51Z

data as of **2026-09-08** · 98 series · 11 red / 37 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.401, 1d in regime; vol-pct 0.218, breadth-off 0.583, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.45, corr60 -0.4, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.12, corr60 0.3, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 0.07, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.15, corr60 -0.06, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.16, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.03, corr60 0.22, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.00011811782483794886)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.503** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=1948) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.3] commodities · 2 series ↑
- brent [COMMODITIES]: last 99.14, z20 2.47, zc 0.98, resid-z 0.02 [quiet], 1d 1.96%, 1-session move +1.96% ≥ 1.5%; |z20|=2.47
- wti [COMMODITIES]: last 94.40, z20 2.41, zc 0.90, resid-z -0.12 [quiet], 1d 1.95%, 1-session move +1.95% ≥ 1.5%; |z20|=2.41
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.569 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.694 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.535 vs brent
- Source: Sensex today | Stock Market Live: Sensex drops over 500 points, Nifty near 23,650 as US-Iran tensions and crude weigh, Nifty Defence hits record high — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-8th-september-2026/article71441098.ece
- Source: Oil Prices Near $100 After Fresh Attacks on Saudi Energy Sites — OilPrice, 2026-09-08. https://oilprice.com/Energy/Oil-Prices/Oil-Prices-Near-100-After-Fresh-Attacks-on-Saudi-Energy-Sites.html
- Source: Goldman Sachs’ big warning! Oil prices could soar to $120 if attacks on shipping continue in Hormuz Strait — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/commodities/news/goldman-sachs-big-warning-oil-prices-could-soar-to-120-if-attacks-on-shipping-continue-in-hormuz-strait/articleshow/133915395.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.43] usd_jpy ↓
- usd_jpy [FX]: last 154.12, z20 -4.43, zc -1.59, resid-z -2.75 [unexplained], 1d -1.33%, |z20|=4.43
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.518 vs usd_jpy
- Source: Global Market: Yen rally threatens to unravel lucrative carry trade ahead of BOJ rate decision — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-yen-rally-threatens-to-unravel-lucrative-carry-trade-ahead-of-boj-rate-decision/articleshow/133913871.cms
- Source: Yen extends rally to new seven-month high; dollar subdued ahead of CPI — Mint Markets, 2026-09-08. https://www.livemint.com/market/yen-extends-rally-to-new-seven-month-high-dollar-subdued-ahead-of-cpi-11788828964221.html
- Source: Japan's foreign reserves drop by a record $80 billion in August following yen intervention — CNBC Economy, 2026-09-07. https://www.cnbc.com/2026/09/07/japan-foreign-reserves-yen-intervention.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 5.72] cross-asset · 3 series ↓
- dyn_tataelxsi_ns [EQUITIES]: last 3482.50, z20 -2.40, zc -0.24, resid-z 0.22 [quiet], 1d -0.41%, |z20|=2.40; 1y-pct=1
- dyn_techm_ns [EQUITIES]: last 1550.10, z20 -2.34, zc -0.55, resid-z -0.37 [quiet], 1d -0.89%, |z20|=2.34
- nifty_it [INDICES]: last 29931.35, z20 -1.89, zc -0.14, resid-z 0.21 [quiet], 1d -0.21%, |z20|=1.89
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.566 via nifty_it, z -1.25, reacted); nifty_50 (rho 0.499 via nifty_it, z -2.69, reacted); dyn_cartrade_ns (rho -0.433 via dyn_techm_ns, z 1.48, reacted)
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.528 vs nifty_it
- **India receivers**: dyn_tatatech_ns (rho 0.566, z -1.25); nifty_50 (rho 0.499, z -2.69); dyn_cartrade_ns (rho -0.433, z 1.48)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Today — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-livestock-price-today-live-updates-08-sep-2026/liveblog/133905653.cms
- Source: Market wrap:  L&T, Bharti Airtel, Infosys, Tech Mahindra top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-lt-bharti-airtel-infosys-tech-mahindra-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/133878571.cms
- Source: Sensex today | Stock Market Highlights: Sensex, Nifty decline 0.50%; Infosys, Tech Mahindra lead losses — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-7th-september-2026/article71437259.ece
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [AMBER 5.26] cross-asset · 4 series ↑
- ust_10y [RATES]: last 4.77, z20 1.59, zc -0.43, resid-z 0.29 [quiet], 1d -0.42%, |z20|=1.59; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.04, z20 -1.49, zc -0.03, resid-z -0.38 [quiet], 1d -0.01%, 1y-pct=1
- ust_2y [RATES]: last 4.34, z20 1.48, zc -0.89, resid-z -0.06 [quiet], 1d -1.14%, 1y-pct=98
- ust_30y [RATES]: last 5.25, z20 0.47, zc -0.48, resid-z -0.10 [quiet], 1d -0.38%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.862 vs ust_10y
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.549 vs dyn_bond, historically leads by 3d
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.527 vs ust_10y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.511 vs dyn_bond
- Source: Biocon shares rise 2% on 10-year Pertuzumab supply deal for breast cancer therapy in Brazil — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/biocon-shares-rise-2-on-10-year-pertuzumab-supply-deal-for-breast-cancer-therapy-in-brazil/articleshow/133910110.cms
- Source: Spain mandates new 20-year green bond syndication, seeks to raise €4 billion — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/bonds/spain-mandates-new-20-year-green-bond-syndication-seeks-to-raise-4-billion/articleshow/133881336.cms
- Source: Is the stock market open today for Labor Day? What about bond trading and mail delivery? — MarketWatch Top, 2026-09-07. https://www.marketwatch.com/story/is-the-stock-market-open-on-labor-day-does-the-post-office-deliver-mail-6d58fd77?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 4.95] comex_copper ↑
- comex_copper [COMMODITIES]: last 6.77, z20 2.95, zc 0.32, resid-z 0.58 [quiet], 1d 0.69%, |z20|=2.95; 1y-pct=100
- **Mechanism**: comex_copper ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.58 vs comex_copper, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.554 vs comex_copper, historically leads by 1d
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.546 vs comex_copper, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.54 vs comex_copper, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.644 vs comex_copper
- Source: Copper hits record high, UltraTech’s Ultravolt on the offensive: A double whammy for cable makers in FY27? — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/copper-hits-record-high-ultratechs-ultravolt-on-the-offensive-a-double-whammy-for-cable-makers-in-fy27/articleshow/133913050.cms
- Source: Copper hits new peak of $14,533/metric ton. Can its reddish glow brighten even further? — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/commodities/news/copper-hits-new-peak-of-14533/metric-ton-can-its-reddish-glow-brighten-even-further/articleshow/133911837.cms
- Source: Copper Ascends to New Heights on Tight Supply and Tariff Fears — Mint Markets, 2026-09-08. https://www.livemint.com/market/copper-ascends-to-new-heights-on-tight-supply-and-tariff-fears-11788847556298.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

### [RED 4.86] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 13.46, z20 2.86, zc -0.37, resid-z -0.89 [quiet], 1d -3.37%, |z20|=2.86; 1y-pct=97
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PC Jeweller shares fall 5% after sharp 3-day rally; stock up 388% in 3 years — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/pc-jeweller-shares-fall-5-after-sharp-3-day-rally-stock-up-388-in-3-years/articleshow/133911978.cms
- Source: PC Jeweller Share Price: Jewellery stock falls over 5% after a 3-day buying spree - what's behind the sharp U-turn? — Mint Markets, 2026-09-08. https://www.livemint.com/market/pc-jeweller-share-price-jewellery-stock-falls-over-5-after-a-3-day-buying-spree-whats-behind-the-sharp-uturn-11788842316363.html
- Source: PC Jeweller share price surges 15% today - jumps 35% in 1 month - rally reason explained — Mint Markets, 2026-09-07. https://www.livemint.com/market/stock-market-news/pc-jeweller-share-price-surges-15-today-jumps-35-in-1-month-rally-reason-explained-11788756711988.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [AMBER 4.82] commodities · 2 series ↑
- corn [COMMODITIES]: last 541.75, z20 1.99, zc -0.50, resid-z -0.72 [quiet], 1d 5.81%, |z20|=1.99; 1y-pct=100
- wheat [COMMODITIES]: last 760.25, z20 1.46, zc -1.26, resid-z -1.53 [unexplained], 1d 6.18%, 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho -0.383 via corn, z 1.88, reacted)
- **India receivers**: dyn_coalindia_ns (rho -0.383, z 1.88)
- Source: Wheat soars after US efforts to end Black Sea conflicts yield little progress — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/commodities/wheat-soars-after-us-efforts-to-end-black-sea-conflicts-yield-little-progress/article71441197.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.69] nifty_50 ↓
- nifty_50 [INDICES]: last 23654.35, z20 -2.69, zc -1.03, resid-z 0.12 [quiet], 1d -0.52%, |z20|=2.69
- **Mechanism**: nifty_50 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.731 via nifty_50, z -1.72, reacted); nifty_midcap_100 (rho 0.61 via nifty_50, z -2.03, reacted); nifty_fmcg (rho 0.604 via nifty_50, z -1.45, reacted); dyn_indusindbk_bo (rho 0.503 via nifty_50, z -0.71, quiet); nifty_it (rho 0.499 via nifty_50, z -1.89, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.717 vs nifty_50
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.62 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.503 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.731, z -1.72); nifty_midcap_100 (rho 0.61, z -2.03); nifty_fmcg (rho 0.604, z -1.45); dyn_indusindbk_bo (rho 0.503, z -0.71)
- Source: Sensex today | Stock Market Live: Sensex drops over 500 points, Nifty near 23,650 as US-Iran tensions and crude weigh, Nifty Defence hits record high — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-8th-september-2026/article71441098.ece
- Source: Bulls, bears slug it out as Nifty nears key support — Mint Markets, 2026-09-08. https://www.livemint.com/market/stock-market-news/nifty-outlook-fpi-short-positions-domestic-investors-23600-support-11788851861032.html
- Source: Defence stocks rally as Nifty Defence hits record high after ₹1.10 lakh crore procurement approval — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/defence-stocks-rally-as-nifty-defence-hits-record-high-after-110-lakh-crore-procurement-approval-hal-midhani-data-patterns-top-gainers/article71441371.ece
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

## Watchlist (below surfacing floor)
dyn_icicigi_bo ↓ (4.62), midcap_largecap_ratio ↑ (4.59), gold_silver_ratio ↓ (3.84), cross-asset · 2 series ↑ (3.82), natgas ↑ (3.59), dyn_tech ↑ (3.1), dyn_ifci_ns ↑ (2.83), dyn_muthootfin_ns ↓ (2.74), dyn_indianb_ns ↓ (2.65), dyn_dell ↑ (2.58), dyn_havells_ns ↓ (2.52), asx_200 ↓ (2.45)

## India macro
- nifty_50: 23654.3496 (1d -0.52%, z20 -2.69, flag red)
- nifty_midcap_100: 62852.1484 (1d 0.11%, z20 -2.03, flag amber)
- usd_inr: 94.7975 (1d 0.39%, z20 -0.76, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6571 (1d 0.63%, z20 1.59, flag red)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 65.6 — "GE Vernova T&D India share price jumps 8% | Rises 49% YTD. What's behind the rally?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 60.9 — "GE Vernova T&D India share price jumps 8% | Rises 49% YTD. What's behind the rally?"
- COALINDIA.NS (COAL INDIA LTD) score 60.7 — "GE Vernova T&D India share price jumps 8% | Rises 49% YTD. What's behind the rally?"
- INDIANB.NS (INDIAN BANK) score 50.6 — "HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview"
- COIN (Coinbase Global, Inc.) score 49.1 — "MCX gold and silver prices rise on healthy spot demand, positive global cues; experts high"
- BAC (Bank of America Corporation) score 46.5 — "HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview"
- HDB (HDFC Bank Limited) score 39.8 — "HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview"
- OHI (Omega Healthcare Investors, In) score 39.1 — "Kanohar Electricals raises ₹317 crore from anchor investors; IPO opens for subscription"
- IDBI.NS (IDBI BANK LIMITED) score 37.7 — "HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.7 — "HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.7 — "HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Today"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Today"
- TECH (Bio-Techne Corp) score 37.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Today"
- CHKP (Check Point Software Technolog) score 35.8 — "Kanohar Electricals IPO GMP jumps 31% on Day 1. Check review, issue details, subscription."
- BOND (PIMCO Active Bond Exchange-Tra) score 34.6 — "Bonds seen boxed in narrow range as traders eye fresh triggers"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.0 — "Crude oil futures rise after Iran threatens retaliatory strike on energy assets"
- 301077.SZ (CHINASTARS) score 24.3 — "In Gyirong Port, small items speak of the human cost of the China-Nepal disaster"
- LTH (Life Time Group Holdings, Inc.) score 21.6 — "Fly-Hi Maritime, Farm Peace SME shares to list today: Here's what GMP suggests ahead of li"
- PCJEWELLER.NS (PC JEWELLER LTD) score 13.3 — "Deepa Jewellers IPO listing: Shares make strong debut at  ₹221 per share over the IPO pric"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.6 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.0 — "Stocks to Watch Today: AU Small Finance, Adani Power, Swiggy, REC, Neuland Labs and more"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.4 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.4 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.6 — "ESDS Software Solution share price hits 20% upper circuit - up 200% from IPO price in just"
- NVDA (NVIDIA Corporation) score 7.2 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- MS (Morgan Stanley) score 7.0 — "Morgan Stanley’s top picks: Adani Power, Trent, among 10 stocks rated ‘overweight’ by Wall"
- JIOFIN.BO (Jio Financial Services Limited) score 7.0 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.5 — "Stocks to Watch Today: AU Small Finance, Adani Power, Swiggy, REC, Neuland Labs and more"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.3 — "India Ramps Up Rail Coal Deliveries as Power Plant Stockpiles Dwindle"
- META (Meta) score 6.2 — "Hindustan Copper shares jump 4% as copper prices surge to all-time high. What’s driving th"
- VT (Vanguard Total World Stock Ind) score 6.1 — "World’s biggest money managers are rebuilding gold positions"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.8 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- IFCI.NS (IFCI LTD) score 3.5 — "IFCI shares slide 7% after stellar 30% monthly surge amid NSE IPO buzz"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 3.3 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- DELL (Dell Technologies Inc.) score 1.7 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.9 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- DKS (Dick's Sporting Goods Inc) score 0.3 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.2 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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