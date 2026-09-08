# Transmission Layer — board brief · 2026-09-08 19:26Z

data as of **2026-09-08** · 98 series · 10 red / 35 amber · 8 events surfaced (32 suppressed)

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
- [WEAK] **gsr_stress_gauge** — corr20 0.01, corr60 0.21, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.504** (n=1128) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=1974) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.64] usd_jpy ↓
- usd_jpy [FX]: last 153.88, z20 -4.64, zc -1.77, resid-z -3.04 [unexplained], 1d -1.48%, |z20|=4.64
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.53 vs usd_jpy
- Source: The yen's sudden surge upsets the carry trade faithful — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/forex/forex-news/the-yens-sudden-surge-upsets-the-carry-trade-faithful/articleshow/133921530.cms
- Source: Global Market: Yen rally threatens to unravel lucrative carry trade ahead of BOJ rate decision — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-yen-rally-threatens-to-unravel-lucrative-carry-trade-ahead-of-boj-rate-decision/articleshow/133913871.cms
- Source: Yen extends rally to new seven-month high; dollar subdued ahead of CPI — Mint Markets, 2026-09-08. https://www.livemint.com/market/yen-extends-rally-to-new-seven-month-high-dollar-subdued-ahead-of-cpi-11788828964221.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 5.6] cross-asset · 3 series ↑
- brent [COMMODITIES]: last 98.59, z20 2.28, zc 0.70, resid-z 0.03 [quiet], 1d 1.40%, |z20|=2.28
- wti [COMMODITIES]: last 93.51, z20 2.16, zc 0.46, resid-z -0.12 [quiet], 1d 0.99%, |z20|=2.16
- dow_jones [INDICES]: last 52822.24, z20 -1.99, zc -0.59, resid-z -0.48 [quiet], 1d -1.11%, |z20|=1.99
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.741 vs dow_jones, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.685 vs dow_jones, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.646 vs dow_jones, historically leads by 1d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.641 vs dow_jones, historically leads by 5d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.572 vs brent, historically leads by 4d
- Source: How the U.S. Is Targeting Iran's Oil Money — OilPrice, 2026-09-08. https://oilprice.com/Geopolitics/Middle-East/How-the-US-Is-Targeting-Irans-Oil-Money.html
- Source: Chevron to Double Venezuela Rig Count in $7 Billion Oil Push — OilPrice, 2026-09-08. https://oilprice.com/Latest-Energy-News/World-News/Chevron-to-Double-Venezuela-Rig-Count-in-7-Billion-Oil-Push.html
- Source: Canada’s Oil Pivot to Asia Is Starting to Materialize — OilPrice, 2026-09-08. https://oilprice.com/Latest-Energy-News/World-News/Canadas-Oil-Pivot-to-Asia-Is-Starting-to-Materialize.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.33), 2025-08-22 (d=0.49)

### [RED 5.45] comex_copper ↑
- comex_copper [COMMODITIES]: last 6.80, z20 3.45, zc 0.54, resid-z 0.57 [quiet], 1d 1.17%, |z20|=3.45; 1y-pct=100
- **Mechanism**: comex_copper ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.578 vs comex_copper, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.551 vs comex_copper, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.538 vs comex_copper, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.641 vs comex_copper
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.615 vs comex_copper
- Source: Copper hits record high, UltraTech’s Ultravolt on the offensive: A double whammy for cable makers in FY27? — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/copper-hits-record-high-ultratechs-ultravolt-on-the-offensive-a-double-whammy-for-cable-makers-in-fy27/articleshow/133913050.cms
- Source: Copper hits new peak of $14,533/metric ton. Can its reddish glow brighten even further? — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/commodities/news/copper-hits-new-peak-of-14533/metric-ton-can-its-reddish-glow-brighten-even-further/articleshow/133911837.cms
- Source: Copper Ascends to New Heights on Tight Supply and Tariff Fears — Mint Markets, 2026-09-08. https://www.livemint.com/market/copper-ascends-to-new-heights-on-tight-supply-and-tariff-fears-11788847556298.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

### [AMBER 5.26] cross-asset · 4 series ↑
- ust_10y [RATES]: last 4.77, z20 1.59, zc -0.43, resid-z 0.29 [quiet], 1d -0.42%, |z20|=1.59; 1y-pct=99
- ust_2y [RATES]: last 4.34, z20 1.48, zc -0.89, resid-z -0.06 [quiet], 1d -1.14%, 1y-pct=98
- dyn_bond [EQUITIES]: last 89.99, z20 -1.48, zc -0.03, resid-z -0.38 [quiet], 1d -0.06%, 1y-pct=1
- ust_30y [RATES]: last 5.25, z20 0.47, zc -0.48, resid-z -0.10 [quiet], 1d -0.38%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.862 vs ust_10y
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.549 vs dyn_bond, historically leads by 3d
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.527 vs ust_10y, historically leads by 1d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.501 vs ust_10y, historically leads by 4d
- Source: Five pressure points to watch as Treasury yields creep toward 5% — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/five-pressure-points-to-watch-as-treasury-yields-creep-toward-5/slideshow/133929693.cms
- Source: Thailand's Kasikornbank launches $800 million US dollar bond sale, term sheet shows — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/bonds/thailands-kasikornbank-launches-800-million-us-dollar-bond-sale-term-sheet-shows/articleshow/133927264.cms
- Source: Amazon hires banks for first ever sterling bond sale — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/news/amazon-hires-banks-for-first-ever-sterling-bond-sale/articleshow/133926799.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 4.96] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.96, zc n/a, resid-z n/a [quiet], 1d 0.82%, 52-wk extreme (pct=99); |z20|=1.96; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.453 via midcap_largecap_ratio, z -2.79, reacted); nifty_midcap_100 (rho 0.438 via midcap_largecap_ratio, z -1.87, reacted); nifty_fmcg (rho -0.417 via midcap_largecap_ratio, z -1.56, reacted)
- **India receivers**: nifty_50 (rho -0.453, z -2.79); nifty_midcap_100 (rho 0.438, z -1.87); nifty_fmcg (rho -0.417, z -1.56)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.94] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 13.55, z20 2.94, zc -0.30, resid-z -0.79 [quiet], 1d -2.73%, |z20|=2.94; 1y-pct=97
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
- Source: Crude shock sends Nifty to three-month low; Rupee slips — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/crude-shock-sends-nifty-to-three-month-low-rupee-slips/article71443299.ece
- Source: Market wrap: BEL, HUL, ICICI Bank, Axis Bank top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-bel-hul-icici-bank-axis-bank-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/133923188.cms
- Source: Sensex today | Stock Market Highlights: Sensex down 555 pts, Nifty ends at 23,635 as crude oil nears $100 — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-8th-september-2026/article71441098.ece
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

### [RED 4.77] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 66.28, z20 -1.77, zc n/a, resid-z n/a [quiet], 1d -0.49%, GSR<75 (extreme low); |z20|=1.77
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.365 via gold_silver_ratio, z -1.87, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.85 vs gold_silver_ratio
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.502 vs gold_silver_ratio, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho -0.365, z -1.87)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
dyn_hdb ↓ (4.61), dyn_qcom ↑ (4.58), commodities · 2 series ↑ (4.5), dyn_icicigi_bo ↓ (4.49), dyn_indianb_ns ↓ (4.46), dyn_lenskart_ns ↑ (3.76), cross-asset · 2 series ↓ (3.1), dyn_ifci_ns ↑ (2.83), usd_cny ↓ (2.78), dyn_dell ↑ (2.53), dyn_havells_ns ↓ (2.48), asx_200 ↓ (2.45)

## India macro
- nifty_50: 23635.0996 (1d -0.61%, z20 -2.79, flag red)
- nifty_midcap_100: 62917.6016 (1d 0.21%, z20 -1.87, flag amber)
- usd_inr: 94.8100 (1d 0.40%, z20 -0.74, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6620 (1d 0.82%, z20 1.96, flag red)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 69.9 — "Madhu Kela-backed fund invests in Steamhouse India IPO as company raises Rs 124 crore from"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 65.7 — "Madhu Kela-backed fund invests in Steamhouse India IPO as company raises Rs 124 crore from"
- COALINDIA.NS (COAL INDIA LTD) score 65.5 — "Madhu Kela-backed fund invests in Steamhouse India IPO as company raises Rs 124 crore from"
- INDIANB.NS (INDIAN BANK) score 58.3 — "NSE IPO: Bank of Baroda to divest up to 35% of holding in National Stock Exchange through "
- BAC (Bank of America Corporation) score 52.6 — "NSE IPO: Bank of Baroda to divest up to 35% of holding in National Stock Exchange through "
- COIN (Coinbase Global, Inc.) score 49.2 — "Signature Global to launch 2 housing projects worth Rs 12,000cr in 2nd half of FY27: Chair"
- HDB (HDFC Bank Limited) score 48.5 — "NSE IPO: Bank of Baroda to divest up to 35% of holding in National Stock Exchange through "
- OHI (Omega Healthcare Investors, In) score 45.1 — "Madhu Kela-backed fund invests in Steamhouse India IPO as company raises Rs 124 crore from"
- IDBI.NS (IDBI BANK LIMITED) score 43.7 — "NSE IPO: Bank of Baroda to divest up to 35% of holding in National Stock Exchange through "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.7 — "NSE IPO: Bank of Baroda to divest up to 35% of holding in National Stock Exchange through "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.7 — "NSE IPO: Bank of Baroda to divest up to 35% of holding in National Stock Exchange through "
- BOND (PIMCO Active Bond Exchange-Tra) score 37.0 — "Global Market: Eurozone bond yields hold near multi-year highs as markets await ECB decisi"
- TECHM.NS (TECH MAHINDRA LIMITED) score 36.6 — "Why a stronger Japanese currency could spell trouble for AI and technology stocks"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.5 — "Why a stronger Japanese currency could spell trouble for AI and technology stocks"
- TECH (Bio-Techne Corp) score 36.5 — "Why a stronger Japanese currency could spell trouble for AI and technology stocks"
- CHKP (Check Point Software Technolog) score 36.2 — "Buy Fortis Healthcare shares, says PL Capital; check target price, stock performance"
- 301077.SZ (CHINASTARS) score 27.8 — "A Forgotten Soviet Waterway Could Give China a New Arctic Trade Route"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.5 — "ATHA ENERGY CONTINUES STREAK AT ANGILAK URANIUM PROJECT, INTERSECTING URANIUM IN 7 FOR 7 H"
- LTH (Life Time Group Holdings, Inc.) score 19.5 — "Fly-Hi Maritime, Farm Peace SME shares to list today: Here's what GMP suggests ahead of li"
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.0 — "Deepa Jewellers IPO listing: Shares make strong debut at  ₹221 per share over the IPO pric"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.4 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.9 — "Stocks to Watch Today: AU Small Finance, Adani Power, Swiggy, REC, Neuland Labs and more"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.5 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.5 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.9 — "U.S. consumers grow more uneasy about jobs & finances as high inflation outlook holds stea"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.8 — "Prenups aren’t just for the rich. Here’s what they can cover."
- MS (Morgan Stanley) score 7.3 — "Beneath the surface, the next stock-market leaders are getting ready to break out, says Mo"
- META (Meta) score 6.6 — "India Gold Metaverse appoints Chand as MD of BullionX"
- VT (Vanguard Total World Stock Ind) score 6.5 — "Uganda Set to Become World's Newest Oil Exporter in Early 2027"
- NVDA (NVIDIA Corporation) score 6.5 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- JIOFIN.BO (Jio Financial Services Limited) score 6.3 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.3 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 5.7 — "India Ramps Up Rail Coal Deliveries as Power Plant Stockpiles Dwindle"
- IFCI.NS (IFCI LTD) score 3.2 — "IFCI shares slide 7% after stellar 30% monthly surge amid NSE IPO buzz"
- QCOM (QUALCOMM Incorporated) score 3.0 — "US stocks slip as Middle East conflict pushes oil prices higher; Qualcomm climbs 4%, Intel"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.8 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 1.5 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- DKS (Dick's Sporting Goods Inc) score 0.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
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