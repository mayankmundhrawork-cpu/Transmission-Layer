# Transmission Layer — board brief · 2026-09-08 14:32Z

data as of **2026-09-08** · 98 series · 6 red / 39 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.325, 3d in regime; vol-pct 0.179, breadth-off 0.471, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.45, corr60 -0.4, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.12, corr60 0.3, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 0.07, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.06, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.16, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.02, corr60 0.22, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.503** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=1974) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.52] usd_jpy ↓
- usd_jpy [FX]: last 154.02, z20 -4.52, zc -1.66, resid-z -2.86 [unexplained], 1d -1.39%, |z20|=4.52
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.536 vs usd_jpy
- Source: The yen's sudden surge upsets the carry trade faithful — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/forex/forex-news/the-yens-sudden-surge-upsets-the-carry-trade-faithful/articleshow/133921530.cms
- Source: Global Market: Yen rally threatens to unravel lucrative carry trade ahead of BOJ rate decision — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-yen-rally-threatens-to-unravel-lucrative-carry-trade-ahead-of-boj-rate-decision/articleshow/133913871.cms
- Source: Yen extends rally to new seven-month high; dollar subdued ahead of CPI — Mint Markets, 2026-09-08. https://www.livemint.com/market/yen-extends-rally-to-new-seven-month-high-dollar-subdued-ahead-of-cpi-11788828964221.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 6.11] comex_copper ↑
- comex_copper [COMMODITIES]: last 6.85, z20 4.11, zc 0.83, resid-z 0.57 [quiet], 1d 1.82%, |z20|=4.11; 1y-pct=100
- **Mechanism**: comex_copper ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.572 vs comex_copper, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.533 vs comex_copper, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.632 vs comex_copper
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.562 vs comex_copper
- Watch next: sp500 (co-move) — not yet - watch; rho 0.533 vs comex_copper
- Source: Copper hits record high, UltraTech’s Ultravolt on the offensive: A double whammy for cable makers in FY27? — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/copper-hits-record-high-ultratechs-ultravolt-on-the-offensive-a-double-whammy-for-cable-makers-in-fy27/articleshow/133913050.cms
- Source: Copper hits new peak of $14,533/metric ton. Can its reddish glow brighten even further? — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/commodities/news/copper-hits-new-peak-of-14533/metric-ton-can-its-reddish-glow-brighten-even-further/articleshow/133911837.cms
- Source: Copper Ascends to New Heights on Tight Supply and Tariff Fears — Mint Markets, 2026-09-08. https://www.livemint.com/market/copper-ascends-to-new-heights-on-tight-supply-and-tariff-fears-11788847556298.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

### [AMBER 5.57] cross-asset · 3 series ↑
- dow_jones [INDICES]: last 52739.19, z20 -2.25, zc -0.59, resid-z -0.48 [quiet], 1d -1.26%, |z20|=2.25
- brent [COMMODITIES]: last 98.37, z20 2.21, zc 0.59, resid-z 0.03 [quiet], 1d 1.17%, |z20|=2.21
- wti [COMMODITIES]: last 93.48, z20 2.15, zc 0.44, resid-z -0.12 [quiet], 1d 0.96%, |z20|=2.15
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.822 vs dow_jones, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.741 vs dow_jones, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.685 vs dow_jones, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.641 vs dow_jones, historically leads by 5d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.571 vs brent, historically leads by 4d
- Source: US stocks mixed as Middle East conflict pushes oil prices higher — Mint Markets, 2026-09-08. https://www.livemint.com/market/stock-market-news/us-stocks-mixed-as-middle-east-conflict-pushes-oil-prices-higher-11788875231997.html
- Source: $100 Brent Looms as China’s Oil Buying Rebounds — OilPrice, 2026-09-08. https://oilprice.com/Energy/Energy-General/100-Brent-Looms-as-Chinas-Oil-Buying-Rebounds.html
- Source: US stocks today: US stocks mixed at open as Gulf tensions send oil to over six-week high — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-mixed-at-open-as-gulf-tensions-send-oil-to-over-six-week-high/articleshow/133927807.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.33), 2025-08-22 (d=0.49)

### [AMBER 5.26] cross-asset · 4 series ↑
- ust_10y [RATES]: last 4.77, z20 1.59, zc -0.43, resid-z 0.29 [quiet], 1d -0.42%, |z20|=1.59; 1y-pct=99
- ust_2y [RATES]: last 4.34, z20 1.48, zc -0.89, resid-z -0.06 [quiet], 1d -1.14%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.01, z20 -1.40, zc -0.03, resid-z -0.38 [quiet], 1d -0.03%, 1y-pct=1
- ust_30y [RATES]: last 5.25, z20 0.47, zc -0.48, resid-z -0.10 [quiet], 1d -0.38%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.862 vs ust_10y
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.527 vs ust_10y, historically leads by 1d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.503 vs ust_10y, historically leads by 4d
- Source: Thailand's Kasikornbank launches $800 million US dollar bond sale, term sheet shows — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/bonds/thailands-kasikornbank-launches-800-million-us-dollar-bond-sale-term-sheet-shows/articleshow/133927264.cms
- Source: Amazon hires banks for first ever sterling bond sale — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/news/amazon-hires-banks-for-first-ever-sterling-bond-sale/articleshow/133926799.cms
- Source: Global Market: Eurozone bond yields hold near multi-year highs as markets await ECB decision — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-hold-near-multi-year-highs-as-markets-await-ecb-decision/articleshow/133918411.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 4.96] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.96, zc n/a, resid-z n/a [quiet], 1d 0.82%, 52-wk extreme (pct=99); |z20|=1.96; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.453 via midcap_largecap_ratio, z -2.79, reacted); nifty_midcap_100 (rho 0.438 via midcap_largecap_ratio, z -1.87, reacted); nifty_fmcg (rho -0.417 via midcap_largecap_ratio, z -1.56, reacted)
- **India receivers**: nifty_50 (rho -0.453, z -2.79); nifty_midcap_100 (rho 0.438, z -1.87); nifty_fmcg (rho -0.417, z -1.56)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.94] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 13.55, z20 2.94, zc -0.30, resid-z -0.80 [quiet], 1d -2.73%, |z20|=2.94; 1y-pct=97
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PC Jeweller shares fall 5% after sharp 3-day rally; stock up 388% in 3 years — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/pc-jeweller-shares-fall-5-after-sharp-3-day-rally-stock-up-388-in-3-years/articleshow/133911978.cms
- Source: PC Jeweller Share Price: Jewellery stock falls over 5% after a 3-day buying spree - what's behind the sharp U-turn? — Mint Markets, 2026-09-08. https://www.livemint.com/market/pc-jeweller-share-price-jewellery-stock-falls-over-5-after-a-3-day-buying-spree-whats-behind-the-sharp-uturn-11788842316363.html
- Source: PC Jeweller share price surges 15% today - jumps 35% in 1 month - rally reason explained — Mint Markets, 2026-09-07. https://www.livemint.com/market/stock-market-news/pc-jeweller-share-price-surges-15-today-jumps-35-in-1-month-rally-reason-explained-11788756711988.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [RED 4.79] nifty_50 ↓
- nifty_50 [INDICES]: last 23635.10, z20 -2.79, zc -1.19, resid-z 0.12 [quiet], 1d -0.61%, |z20|=2.79
- **Mechanism**: nifty_50 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.728 via nifty_50, z -1.62, reacted); nifty_fmcg (rho 0.609 via nifty_50, z -1.56, reacted); nifty_midcap_100 (rho 0.603 via nifty_50, z -1.87, reacted); nifty_it (rho 0.5 via nifty_50, z -1.99, reacted); dyn_indusindbk_bo (rho 0.498 via nifty_50, z -0.41, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.715 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.728, z -1.62); nifty_fmcg (rho 0.609, z -1.56); nifty_midcap_100 (rho 0.603, z -1.87); nifty_it (rho 0.5, z -1.99)
- Source: Market wrap: BEL, HUL, ICICI Bank, Axis Bank top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-bel-hul-icici-bank-axis-bank-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/133923188.cms
- Source: Sensex today | Stock Market Highlights: Sensex down 555 pts, Nifty ends at 23,635 as crude oil nears $100 — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-8th-september-2026/article71441098.ece
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Wed | Kospi, Taiwan Index, Nikkei cues to watch | 9 Sept — Mint Markets, 2026-09-08. https://www.livemint.com/market/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-wed-kospi-taiwan-index-nikkei-cues-to-watch-9-sept-11788861714934.html
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

### [AMBER 4.62] commodities · 2 series ↑
- corn [COMMODITIES]: last 536.00, z20 1.79, zc -0.50, resid-z -0.71 [quiet], 1d 4.69%, |z20|=1.79; 1y-pct=100
- wheat [COMMODITIES]: last 746.25, z20 1.13, zc -1.26, resid-z -1.52 [unexplained], 1d 4.22%, 1y-pct=98
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho -0.382 via corn, z 2.02, reacted)
- **India receivers**: dyn_coalindia_ns (rho -0.382, z 2.02)
- Source: Wheat soars after US efforts to end Black Sea conflicts yield little progress — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/commodities/wheat-soars-after-us-efforts-to-end-black-sea-conflicts-yield-little-progress/article71441197.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

## Watchlist (below surfacing floor)
dyn_icicigi_bo ↓ (4.49), dyn_indianb_ns ↓ (4.46), gold_silver_ratio ↓ (4.08), dyn_hdb ↓ (3.86), dyn_lenskart_ns ↑ (3.76), cross-asset · 2 series ↓ (3.1), usd_cny ↓ (2.88), dyn_ifci_ns ↑ (2.83), dyn_tech ↑ (2.54), dyn_havells_ns ↓ (2.48), bovespa ↑ (2.47), asx_200 ↓ (2.45)

## India macro
- nifty_50: 23635.0996 (1d -0.61%, z20 -2.79, flag red)
- nifty_midcap_100: 62917.6016 (1d 0.21%, z20 -1.87, flag amber)
- usd_inr: 94.8080 (1d 0.40%, z20 -0.74, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6620 (1d 0.82%, z20 1.96, flag red)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.1 — "Indian banks leave sizeable FX risk open on overseas deposits, creating potential rupee ov"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 63.7 — "Indian banks leave sizeable FX risk open on overseas deposits, creating potential rupee ov"
- COALINDIA.NS (COAL INDIA LTD) score 63.5 — "Indian banks leave sizeable FX risk open on overseas deposits, creating potential rupee ov"
- INDIANB.NS (INDIAN BANK) score 56.9 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- BAC (Bank of America Corporation) score 52.0 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- COIN (Coinbase Global, Inc.) score 50.5 — "Global Market: European shares slip as oil surge fuels inflation fears; Novartis plunges"
- HDB (HDFC Bank Limited) score 46.7 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- IDBI.NS (IDBI BANK LIMITED) score 42.7 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.7 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.7 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- OHI (Omega Healthcare Investors, In) score 42.1 — "Why Ola Electric’s  ₹1,500 crore fundraise fails to enthuse investors"
- BOND (PIMCO Active Bond Exchange-Tra) score 38.7 — "Global Market: Eurozone bond yields hold near multi-year highs as markets await ECB decisi"
- CHKP (Check Point Software Technolog) score 37.9 — "Buy Fortis Healthcare shares, says PL Capital; check target price, stock performance"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.3 — "'Buy' Syrma SGS Technology shares: Over 120% returns in 6 months, Emkay sees 41% more upsi"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.2 — "'Buy' Syrma SGS Technology shares: Over 120% returns in 6 months, Emkay sees 41% more upsi"
- TECH (Bio-Techne Corp) score 37.2 — "'Buy' Syrma SGS Technology shares: Over 120% returns in 6 months, Emkay sees 41% more upsi"
- 301077.SZ (CHINASTARS) score 27.0 — "China’s Crude Buying Rebounds as Fuel Exports Jump 29%"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.7 — "Crude Oil Price rises as Iran threatens strike on energy assets"
- LTH (Life Time Group Holdings, Inc.) score 20.4 — "Fly-Hi Maritime, Farm Peace SME shares to list today: Here's what GMP suggests ahead of li"
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.6 — "Deepa Jewellers IPO listing: Shares make strong debut at  ₹221 per share over the IPO pric"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.0 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.4 — "Stocks to Watch Today: AU Small Finance, Adani Power, Swiggy, REC, Neuland Labs and more"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.9 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.9 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "Prenups aren’t just for the rich. Here’s what they can cover."
- MS (Morgan Stanley) score 7.7 — "Beneath the surface, the next stock-market leaders are getting ready to break out, says Mo"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.2 — "Bajaj Finance acquires 5% stake in TrueFan AI as part of Finserv Intelligence"
- NVDA (NVIDIA Corporation) score 6.8 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- JIOFIN.BO (Jio Financial Services Limited) score 6.6 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.6 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.0 — "India Ramps Up Rail Coal Deliveries as Power Plant Stockpiles Dwindle"
- META (Meta) score 5.9 — "Hindustan Copper shares jump 4% as copper prices surge to all-time high. What’s driving th"
- VT (Vanguard Total World Stock Ind) score 5.8 — "World’s biggest money managers are rebuilding gold positions"
- IFCI.NS (IFCI LTD) score 3.3 — "IFCI shares slide 7% after stellar 30% monthly surge amid NSE IPO buzz"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 3.1 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.9 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 1.6 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
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