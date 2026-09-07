# Transmission Layer — board brief · 2026-09-07 22:49Z

data as of **2026-09-07** · 98 series · 9 red / 36 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.217, 2d in regime; vol-pct 0.183, breadth-off 0.25, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.44, corr60 -0.4, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.11, corr60 0.3, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.08, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.07, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.16, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.05, corr60 0.22, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0012819059673201405)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.505** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1972) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.4] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 13.97, z20 5.40, zc 3.06, resid-z 5.23 [unexplained], 1d 17.79%, |z20|=5.40; 1y-pct=98
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PC Jeweller share price surges 15% today - jumps 35% in 1 month - rally reason explained — Mint Markets, 2026-09-07. https://www.livemint.com/market/stock-market-news/pc-jeweller-share-price-surges-15-today-jumps-35-in-1-month-rally-reason-explained-11788756711988.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [RED 7.17] usd_jpy ↓
- usd_jpy [FX]: last 154.24, z20 -5.17, zc -0.88, resid-z -1.92 [unexplained], 1d -0.91%, |z20|=5.17
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho -0.409 via usd_jpy, z 5.4, reacted)
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.525 vs usd_jpy
- **India receivers**: dyn_pcjeweller_ns (rho -0.409, z 5.4)
- Source: Japan's foreign reserves drop by a record $80 billion in August following yen intervention — CNBC Economy, 2026-09-07. https://www.cnbc.com/2026/09/07/japan-foreign-reserves-yen-intervention.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 5.26] cross-asset · 4 series ↑
- ust_10y [RATES]: last 4.77, z20 1.59, zc -0.43, resid-z 0.29 [quiet], 1d -0.42%, |z20|=1.59; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.04, z20 -1.49, zc -0.03, resid-z -0.38 [quiet], 1d -0.01%, 1y-pct=1
- ust_2y [RATES]: last 4.34, z20 1.48, zc -0.89, resid-z -0.06 [quiet], 1d -1.14%, 1y-pct=98
- ust_30y [RATES]: last 5.25, z20 0.47, zc -0.48, resid-z -0.10 [quiet], 1d -0.38%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.858 vs ust_10y
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.524 vs ust_10y, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.524 vs dyn_bond, historically leads by 3d
- Watch next: ust_2s10s (inverse) — not yet - watch; rho -0.506 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.506 vs dyn_bond
- Source: Spain mandates new 20-year green bond syndication, seeks to raise €4 billion — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/bonds/spain-mandates-new-20-year-green-bond-syndication-seeks-to-raise-4-billion/articleshow/133881336.cms
- Source: Is the stock market open today for Labor Day? What about bond trading and mail delivery? — MarketWatch Top, 2026-09-07. https://www.marketwatch.com/story/is-the-stock-market-open-on-labor-day-does-the-post-office-deliver-mail-6d58fd77?mod=mw_rss_topstories
- Source: Global Market: Japanese bond yields rise as BOJ rate hike bets keep markets on edge — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-rise-as-boj-rate-hike-bets-keep-markets-on-edge/articleshow/133871174.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [AMBER 5.05] commodities · 2 series ↑
- wti [COMMODITIES]: last 92.63, z20 2.22, zc 0.56, resid-z -0.12 [quiet], 1d 1.26%, |z20|=2.22
- brent [COMMODITIES]: last 97.28, z20 2.13, zc 0.49, resid-z 0.02 [quiet], 1d 1.04%, |z20|=2.13
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.672 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.521 vs wti
- Source: Washington’s Venezuela Oil Deal Is About Much More Than Crude — OilPrice, 2026-09-07. https://oilprice.com/Energy/Crude-Oil/Washingtons-Venezuela-Oil-Deal-Is-About-Much-More-Than-Crude.html
- Source: Rosneft Ships First Crude From $157 Billion Vostok Oil Project — OilPrice, 2026-09-07. https://oilprice.com/Energy/Crude-Oil/Rosneft-Ships-First-Crude-From-157-Billion-Vostok-Oil-Project.html
- Source: IRAN’S OIL REVENUES COLLAPSE AS BLOCKADE TIGHTENS Iran’s oil income is rapidly shrinking as a US naval blockade restricts exports and offshore stockpiles fall. Iranian crude stored outside the Gulf has dropped from 90 million to 29 million barrels, while shipments to China are dwindling. With oil fu — DeItaone, 2026-09-07. https://t.me/walter_bloomberg/35497
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 4.84] cross-asset · 2 series ↓
- dyn_techm_ns [EQUITIES]: last 1564.00, z20 -2.01, zc -1.30, resid-z -1.00 [quiet], 1d -2.06%, |z20|=2.01
- nifty_it [INDICES]: last 29995.20, z20 -1.98, zc -1.54, resid-z -1.07 [moved], 1d -2.28%, |z20|=1.98
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.642 via nifty_it, z -2.55, reacted); dyn_tatatech_ns (rho 0.544 via nifty_it, z -1.59, reacted); nifty_50 (rho 0.526 via nifty_it, z -2.25, reacted); dyn_cartrade_ns (rho -0.448 via dyn_techm_ns, z 1.77, reacted)
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.516 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.642, z -2.55); dyn_tatatech_ns (rho 0.544, z -1.59); nifty_50 (rho 0.526, z -2.25); dyn_cartrade_ns (rho -0.448, z 1.77)
- Source: Market wrap:  L&T, Bharti Airtel, Infosys, Tech Mahindra top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-lt-bharti-airtel-infosys-tech-mahindra-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/133878571.cms
- Source: Sensex today | Stock Market Highlights: Sensex, Nifty decline 0.50%; Infosys, Tech Mahindra lead losses — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-7th-september-2026/article71437259.ece
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Analysis — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-07-sep-2026/liveblog/133862746.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 4.6] comex_copper ↑
- comex_copper [COMMODITIES]: last 6.72, z20 2.60, zc 0.84, resid-z 0.58 [quiet], 1d 1.84%, |z20|=2.60; 1y-pct=100
- **Mechanism**: comex_copper ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.634 vs comex_copper, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.593 vs comex_copper, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.567 vs comex_copper, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.686 vs comex_copper
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.588 vs comex_copper
- Source: Copper's Longest Rally Since 1994 Collides With a Shrinking Supply Chain — OilPrice, 2026-09-07. https://oilprice.com/Metals/Commodities/Coppers-Longest-Rally-Since-1994-Collides-With-a-Shrinking-Supply-Chain.html
- Source: Copper prices scale fresh record high as focus turns to tight supplies outside US — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/copper-price-touches-record-high-focus-on-tight-supplies-outside-us/articleshow/133889161.cms
- Source: COPPER SURGES TO ALL-TIME HIGH Copper hit a record $14,533 a ton on the London Metal Exchange, fueled by fears of potential US tariffs on refined copper imports. Prices have jumped 17% over the past year, supported by tight mine supply and rising demand from data centers, renewable energy and power  — DeItaone, 2026-09-07. https://t.me/walter_bloomberg/35496
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

### [AMBER 4.42] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1500.00, z20 -2.42, zc -0.44, resid-z -0.10 [quiet], 1d -0.66%, |z20|=2.42; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: India’s Rs 1 lakh crore digital-media boom: Two stocks ICICI Securities is betting on — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/indias-rs-1-lakh-crore-digital-media-boom-two-stocks-icici-securities-is-betting-on/articleshow/133872047.cms
- Source: ICICI Bank shares in focus as LIC gets RBI nod to acquire 9.99% stake in private lender — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/icici-bank-shares-in-focus-as-lic-gets-rbi-nod-to-acquire-9-99-stake-in-private-lender/articleshow/133861811.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [AMBER 4.25] nifty_50 ↓
- nifty_50 [INDICES]: last 23779.15, z20 -2.25, zc -0.98, resid-z 0.12 [quiet], 1d -0.50%, |z20|=2.25
- **Mechanism**: nifty_50 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.743 via nifty_50, z -1.57, reacted); nifty_midcap_100 (rho 0.645 via nifty_50, z -2.68, reacted); nifty_fmcg (rho 0.627 via nifty_50, z -1.88, reacted); nifty_it (rho 0.526 via nifty_50, z -1.98, reacted); dyn_indusindbk_bo (rho 0.522 via nifty_50, z -0.47, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.739 vs nifty_50
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.601 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.522 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.743, z -1.57); nifty_midcap_100 (rho 0.645, z -2.68); nifty_fmcg (rho 0.627, z -1.88); nifty_it (rho 0.526, z -1.98)
- Source: Crude surge, Fed rate fears drag Nifty lower — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/crude-surge-fed-rate-fears-drag-nifty-lower/article71438795.ece
- Source: Market wrap:  L&T, Bharti Airtel, Infosys, Tech Mahindra top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-09-07. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-lt-bharti-airtel-infosys-tech-mahindra-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/133878571.cms
- Source: Sensex today | Stock Market Highlights: Sensex, Nifty decline 0.50%; Infosys, Tech Mahindra lead losses — BusinessLine Mkts, 2026-09-07. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-7th-september-2026/article71437259.ece
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

## Watchlist (below surfacing floor)
gold_silver_ratio ↓ (4.25), natgas ↑ (3.83), cross-asset · 2 series ↑ (3.82), midcap_largecap_ratio ↑ (3.44), dyn_tech ↑ (3.1), usd_cny ↓ (2.86), dyn_muthootfin_ns ↓ (2.81), dyn_havells_ns ↓ (2.76), fx · 2 series ↑ (2.75), nifty_midcap_100 ↓ (2.68), taiwan_weighted ↑ (2.64), dyn_dell ↑ (2.58)

## India macro
- nifty_50: 23779.1504 (1d -0.50%, z20 -2.25, flag amber)
- nifty_midcap_100: 62786.0000 (1d -0.47%, z20 -2.68, flag red)
- usd_inr: 94.4750 (1d -0.02%, z20 -1.48, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6404 (1d 0.03%, z20 0.44, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · AMFI SIP / MF flows T-1d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.8 — "360 One Group CEO Bhagat buys 1.3 lakh shares of Novartis India for Rs 22 cr"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 63.8 — "360 One Group CEO Bhagat buys 1.3 lakh shares of Novartis India for Rs 22 cr"
- COALINDIA.NS (COAL INDIA LTD) score 63.5 — "360 One Group CEO Bhagat buys 1.3 lakh shares of Novartis India for Rs 22 cr"
- INDIANB.NS (INDIAN BANK) score 51.3 — "RBI easing drives Indian companies’ $7.70 billion overseas borrowing"
- BAC (Bank of America Corporation) score 47.9 — "TRUMP CALLS FOR BAN ON BOMBARDIER SALES IN US President Trump called for Bombardier sales "
- COIN (Coinbase Global, Inc.) score 43.1 — "Taiwan's Wistron raises $1.5 billion in global share sale to fund raw material purchases"
- HDB (HDFC Bank Limited) score 39.4 — "Pernod Ricard India IPO: Four banks appointed as advisors for proposed mega issue: Report"
- OHI (Omega Healthcare Investors, In) score 38.7 — "Top stocks in focus today: Investors must watch Adani Power, Swiggy, Shiprocket shares on "
- IDBI.NS (IDBI BANK LIMITED) score 38.2 — "Pernod Ricard India IPO: Four banks appointed as advisors for proposed mega issue: Report"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.2 — "Pernod Ricard India IPO: Four banks appointed as advisors for proposed mega issue: Report"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.2 — "Pernod Ricard India IPO: Four banks appointed as advisors for proposed mega issue: Report"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.9 — "L&T plans to raise up to  ₹500 crore via tokenized bonds after REC's success, marking new "
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.4 — "Modern Warfare Is Burning Through the Metals Needed for a High-Tech Future"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 33.3 — "Modern Warfare Is Burning Through the Metals Needed for a High-Tech Future"
- TECH (Bio-Techne Corp) score 33.3 — "Modern Warfare Is Burning Through the Metals Needed for a High-Tech Future"
- CHKP (Check Point Software Technolog) score 29.6 — "Why Systematix is bullish on Apollo Micro Systems after 47% YTD rally; check target price"
- 301077.SZ (CHINASTARS) score 21.3 — "IRAN’S OIL REVENUES COLLAPSE AS BLOCKADE TIGHTENS Iran’s oil income is rapidly shrinking a"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.0 — "GM, Ford Turn EV Battery Bust Into Energy Storage Bet"
- LTH (Life Time Group Holdings, Inc.) score 19.3 — "COPPER SURGES TO ALL-TIME HIGH Copper hit a record $14,533 a ton on the London Metal Excha"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.9 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.4 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.4 — "Tata Motors shares in focus as Iveco Tender offer opens today"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.2 — "PC Jeweller share price surges 15% today - jumps 35% in 1 month - rally reason explained"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.9 — "Top stocks in focus today: Investors must watch Adani Power, Swiggy, Shiprocket shares on "
- NVDA (NVIDIA Corporation) score 7.9 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- JIOFIN.BO (Jio Financial Services Limited) score 7.7 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.3 — "Just like for SpaceX, investors may look to ‘make room’ for AI lab IPOs. These stocks coul"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.9 — "India Ramps Up Rail Coal Deliveries as Power Plant Stockpiles Dwindle"
- VT (Vanguard Total World Stock Ind) score 6.7 — "World’s biggest money managers are rebuilding gold positions"
- MS (Morgan Stanley) score 6.7 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.1 — "Muthoot FinCorp rolls out Rs 700 crore NCD issue. Here's what investors need to know"
- META (Meta) score 5.7 — "COPPER SURGES TO ALL-TIME HIGH Copper hit a record $14,533 a ton on the London Metal Excha"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.3 — "LIC gets RBI approval to acquire up to 9.99% stake in ICICI Bank"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 3.6 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- CNI (Canadian National Railway Comp) score 2.3 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- DELL (Dell Technologies Inc.) score 1.8 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.0 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
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