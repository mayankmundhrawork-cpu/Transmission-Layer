# Transmission Layer — board brief · 2026-08-26 13:14Z

data as of **2026-08-26** · 98 series · 14 red / 33 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.247, 2d in regime; vol-pct 0.16, breadth-off 0.333, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.31, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.87, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.36, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.03, corr60 -0.08, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.3, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.3, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.298, β 0.4299, p 0.0); driver zc 1.69 → expected 0.221%. Type hit-rate 0.816 (n=2273).
- Track record · residual_reversion: hit-rate **0.503** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2273) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.91] dyn_dks ↓
- dyn_dks [EQUITIES]: last 124.40, z20 -7.91, zc -11.45, resid-z -1.12 [moved], 1d -30.63%, |z20|=7.91; 1y-pct=0
- **Mechanism**: dyn_dks ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Dick’s Sporting Goods slumps after earnings miss: What’s next? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/dicks-sporting-goods-slumps-after-earnings-miss-whats-next/slideshow/133532630.cms
- Source: Dick’s Sporting Goods’ epic drop hits other footwear giants, as shoppers sour on retro sneakers — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/dicks-sporting-goods-stock-is-having-its-worst-day-ever-as-sneakers-arent-selling-without-deeper-discounts-5a868358?mod=mw_rss_topstories
- Source: Dick’s Sporting Goods’ stock is having its worst day ever, as sneakers aren’t selling without deeper discounts — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/dicks-sporting-goods-stock-is-having-its-worst-day-ever-as-sneakers-arent-selling-without-deeper-discounts-5a868358?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-01 (d=0.0), 2025-08-15 (d=0.12)

### [AMBER 7.26] cross-asset · 4 series ↑
- brent [COMMODITIES]: last 85.60, z20 -0.60, zc -1.31, resid-z -1.09 [quiet], 1d -3.36%, 1-session move -3.36% ≥ 1.5%
- dyn_vt [EQUITIES]: last 160.99, z20 0.57, zc 0.75, resid-z -0.42 [quiet], 1d 0.56%, 1y-pct=98
- wti [COMMODITIES]: last 80.54, z20 -0.56, zc -0.90, resid-z -0.76 [quiet], 1d -2.21%, 1-session move -2.21% ≥ 1.5%
- dow_jones [INDICES]: last 53572.91, z20 0.30, zc 0.35, resid-z -0.77 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.959 vs dyn_vt, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.944 vs dyn_vt, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.835 vs dyn_vt
- Watch next: vix (inverse) — not yet - watch; rho -0.812 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.597 vs dyn_vt, historically leads by 5d
- Source: India’s Russian Oil Imports Slide From Record High as Supply Tightens — OilPrice, 2026-08-26. https://oilprice.com/Latest-Energy-News/World-News/Indias-Russian-Oil-Imports-Slide-From-Record-High-as-Supply-Tightens.html
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks subdued as Nvidia results, inflation take center stage — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-us-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-nvidia-earnings-forecast-fed-rate-intuit-adobe-stock-price-news-26th-august-2026/liveblog/133540745.cms
- Source: Global Market: European shares edge higher as oil prices fall, Nvidia earnings in focus — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-edge-higher-as-oil-prices-fall-nvidia-earnings-in-focus/articleshow/133535441.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 6.59] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 158.87, z20 2.93, zc 1.12, resid-z -0.68 [quiet], 1d 14.39%, |z20|=2.93; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.19, z20 2.66, zc 0.81, resid-z -0.65 [quiet], 1d 4.30%, |z20|=2.66
- btc_usd [CRYPTO]: last 78073.33, z20 2.06, zc -0.18, resid-z -0.37 [quiet], 1d -0.63%, |z20|=2.06
- eth_usd [CRYPTO]: last 2445.29, z20 1.87, zc 0.02, resid-z -0.70 [quiet], 1d 0.09%, |z20|=1.87
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 0.96).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.425 via btc_usd, z 2.5, reacted)
- **India receivers**: nifty_metal (rho 0.425, z 2.5)
- Source: Top Gainers & Losers on 26 Aug: SBFC Finance, Capri Global, Hindustan Copper, SAIL, OLA, Vedanta among top gainers — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-26-aug-sbfc-finance-capri-global-hindustan-copper-sail-ola-vedanta-among-top-gainers-11787739634109.html
- Source: Bitcoin consolidates near $79K ahead of US PCE, GDP Data; whales book record $1.2 billion profit in 3 days — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-consolidates-near-79k-ahead-of-us-pce-gdp-data-whales-book-record-1-2-billion-profit-in-3-days/articleshow/133536752.cms
- Source: Capri Global Capital shares pop 9% on strong volumes, hit highest level in over a month — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/capri-global-capital-shares-pop-9-on-strong-volumes-hit-highest-level-in-over-a-month-11787736616461.html
- Historical analogues: 2025-08-11 (d=0.96), 2024-10-31 (d=1.14), 2025-08-22 (d=1.17)

### [RED 6.15] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 95.25, z20 6.15, zc 2.47, resid-z 2.81 [unexplained], 1d 7.86%, |z20|=6.15
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.383 via dyn_idbi_ns, z 2.5, reacted); dyn_muthootfin_ns (rho 0.376 via dyn_idbi_ns, z 2.36, reacted)
- **India receivers**: nifty_metal (rho 0.383, z 2.5); dyn_muthootfin_ns (rho 0.376, z 2.36)
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

### [AMBER 5.51] cross-asset · 3 series ↑
- comex_copper [COMMODITIES]: last 6.78, z20 2.19, zc 0.49, resid-z 0.99 [quiet], 1d 1.07%, |z20|=2.19; 1y-pct=100; co-occur[metal_copper] suppressed: channel WEAK
- dax [INDICES]: last 26372.52, z20 0.98, zc 0.53, resid-z 0.36 [quiet], 1d 0.41%, 1y-pct=99
- stoxx_50 [INDICES]: last 6487.34, z20 0.29, zc 0.64, resid-z -0.53 [quiet], 1d 0.49%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-25 (z-distance 0.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.519 via dax, z 1.3, reacted)
- Watch next: sp500 (co-move) — not yet - watch; rho 0.622 vs stoxx_50, historically leads by 5d
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.607 vs comex_copper, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.599 vs stoxx_50, historically leads by 5d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.594 vs dax, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.582 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.519, z 1.3)
- Source: Top Gainers & Losers on 26 Aug: SBFC Finance, Capri Global, Hindustan Copper, SAIL, OLA, Vedanta among top gainers — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-26-aug-sbfc-finance-capri-global-hindustan-copper-sail-ola-vedanta-among-top-gainers-11787739634109.html
- Source: Hindustan Copper shares up 5.6%, OFS opened for retail investors today — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/hindustan-copper-shares-up-56-ofs-opened-for-retail-investors-today/article71392239.ece
- Source: Hindustan Copper share price in focus as OFS opens for retail investors today. Should you apply? — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/hindustan-copper-share-price-in-focus-as-ofs-opens-for-retail-investors-today-should-you-apply-11787713785032.html
- Historical analogues: 2025-07-25 (d=0.44), 2025-10-14 (d=0.48), 2024-10-03 (d=0.55)

### [RED 5.23] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3125.00, z20 3.23, zc 0.23, resid-z 0.69 [quiet], 1d 0.60%, |z20|=3.23
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.48 via dyn_adanient_bo, z -1.06, reacted); nifty_midcap_100 (rho 0.462 via dyn_adanient_bo, z 1.3, reacted); dyn_indusindbk_bo (rho 0.44 via dyn_adanient_bo, z -1.74, reacted)
- **India receivers**: nifty_50 (rho 0.48, z -1.06); nifty_midcap_100 (rho 0.462, z 1.3); dyn_indusindbk_bo (rho 0.44, z -1.74)
- Source: Adani’s Cemindia is said to near up to $524 million share sale — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adanis-cemindia-is-said-to-near-up-to-524-million-share-sale/articleshow/133536591.cms
- Source: Adani Ports or Gujarat Pipavav: Which stock benefits more from Gujarat concession extensions? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adani-ports-or-gujarat-pipavav-which-stock-benefits-more-from-gujarat-concession-extensions/articleshow/133532117.cms
- Source: Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharashtra | shares rise — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/gautam-adanis-adani-energy-solutions-wins-rs-4-700-crore-transmission-project-in-maharashtra-shares-rise-11787717367517.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.94] cross-asset · 2 series ↓
- dyn_techm_ns [EQUITIES]: last 1571.00, z20 -2.11, zc -1.20, resid-z -0.86 [quiet], 1d -1.81%, |z20|=2.11
- nifty_it [INDICES]: last 30318.85, z20 -1.69, zc -1.02, resid-z -0.58 [quiet], 1d -1.47%, |z20|=1.69
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.604 via nifty_it, z -1.38, reacted); dyn_tatatech_ns (rho 0.508 via nifty_it, z -0.43, quiet); nifty_50 (rho 0.484 via nifty_it, z -1.06, reacted)
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.508 vs nifty_it, historically leads by 3d
- **India receivers**: dyn_tataelxsi_ns (rho 0.604, z -1.38); dyn_tatatech_ns (rho 0.508, z -0.43); nifty_50 (rho 0.484, z -1.06)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Daily Performance — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-live-updates-26-aug-2026/liveblog/133527928.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 4.83] natgas ↑
- natgas [COMMODITIES]: last 2.88, z20 2.83, zc 1.24, resid-z -0.15 [quiet], 1d 3.86%, |z20|=2.83
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Qatar Loses $24 Billion as LNG Exports Collapse 96% — OilPrice, 2026-08-26. https://oilprice.com/Latest-Energy-News/World-News/Qatar-Loses-24-Billion-as-LNG-Exports-Collapse-96.html
- Source: Hormuz Crisis Boosts Appeal of $42-Billion Tanzania LNG — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/Hormuz-Crisis-Boosts-Appeal-of-42-Billion-Tanzania-LNG.html
- Source: JPMorgan and Santander Lead $15 Billion Financing Push for Argentina LNG — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/JPMorgan-and-Santander-Lead-15-Billion-Financing-Push-for-Argentina-LNG.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.73), commodities · 2 series ↑ (4.53), dyn_icicigi_bo ↓ (4.48), dyn_muthootfin_ns ↑ (4.36), dyn_bond ↑ (4.33), comex_gold ↑ (3.73), dyn_karurvysya_ns ↑ (3.73), indices · 2 series ↑ (3.64), rates · 2 series ↑ (3.39), dyn_lenskart_ns ↑ (3.28), gold_silver_ratio ↑ (3.23), dyn_stylebaaza_ns ↑ (3.15)

## India macro
- nifty_50: 24207.7500 (1d -0.52%, z20 -1.06, flag none)
- nifty_midcap_100: 64099.0508 (1d -0.10%, z20 1.30, flag amber)
- usd_inr: 95.4020 (1d -0.34%, z20 -0.36, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6479 (1d 0.42%, z20 1.73, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 86.0 — "DEUTSCHE BANK SHARES HIT HIGHEST SINCE JULY 2011, UP 4.5%"
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.1 — "Ventura initiates coverage on Meesho and LG India, sees up to 35% upside"
- COALINDIA.NS (COAL INDIA LTD) score 82.0 — "Ventura initiates coverage on Meesho and LG India, sees up to 35% upside"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.7 — "Ventura initiates coverage on Meesho and LG India, sees up to 35% upside"
- BAC (Bank of America Corporation) score 78.2 — "DEUTSCHE BANK SHARES HIT HIGHEST SINCE JULY 2011, UP 4.5%"
- HDB (HDFC Bank Limited) score 72.4 — "DEUTSCHE BANK SHARES HIT HIGHEST SINCE JULY 2011, UP 4.5%"
- IDBI.NS (IDBI BANK LIMITED) score 66.9 — "DEUTSCHE BANK SHARES HIT HIGHEST SINCE JULY 2011, UP 4.5%"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 66.9 — "DEUTSCHE BANK SHARES HIT HIGHEST SINCE JULY 2011, UP 4.5%"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 66.9 — "DEUTSCHE BANK SHARES HIT HIGHEST SINCE JULY 2011, UP 4.5%"
- BOND (PIMCO Active Bond Exchange-Tra) score 60.1 — "There’s so much betting against long-term bonds that a turnaround could catch investors of"
- COIN (Coinbase Global, Inc.) score 55.4 — "BILL GATES PUSHES FOR GLOBAL AI CONTROLS Bill Gates wants to meet China’s President Xi Jin"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.0 — "Hy-Tech Engineers IPO Day 3: GMP at 57%, Issue subscribed 51 times"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.1 — "Hy-Tech Engineers IPO Day 3: GMP at 57%, Issue subscribed 51 times"
- TECH (Bio-Techne Corp) score 53.0 — "Hy-Tech Engineers IPO Day 3: GMP at 57%, Issue subscribed 51 times"
- OHI (Omega Healthcare Investors, In) score 48.1 — "M&A deals double, but execution holds the key for investors: Crisil Ratings"
- LTH (Life Time Group Holdings, Inc.) score 34.0 — "Hy-Tech Engineers IPO Day 3: GMP at 57%, Issue subscribed 51 times"
- CHKP (Check Point Software Technolog) score 32.0 — "Today’s Gold Rate, Aug 26: Check gold rates in Delhi, Mumbai, Chennai"
- 301077.SZ (CHINASTARS) score 27.0 — "‘Massive casualties’ after landslide strikes China-Nepal border"
- NVDA (NVIDIA Corporation) score 24.9 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks subdued as Nv"
- JIOFIN.BO (Jio Financial Services Limited) score 21.9 — "KREMLIN ON VISIT OF CIA CHIEF TO MOSCOW: PUTIN WAS INFORMED ABOUT IT KREMLIN: TOO EARLY TO"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 18.6 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 18.5 — "Hindustan Copper shares up 5.6%, OFS opened for retail investors today"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.4 — "Gold rally takes a breather ahead of US inflation data"
- MS (Morgan Stanley) score 15.8 — "Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail"
- PCJEWELLER.NS (PC JEWELLER LTD) score 15.1 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.0 — "Piero Cipollone: From vision to delivery: building Europe’s tokenised financial market"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.7 — "Adani’s Cemindia is said to near up to $524 million share sale"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.6 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.3 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- META (Meta) score 9.4 — "Hindustan Copper OFS opens for retail investors today. Should you apply in the metals majo"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.5 — "ICICI Prudential AMC shares: Prudential Corporation to divest up to 2% equity, stock up 49"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.3 — "From ITC, Coal India to Vedanta: 5 dividend stocks investors may want to add to their port"
- VT (Vanguard Total World Stock Ind) score 7.4 — "Healthcare stock Park Medi World jumps 3%, rises for 5th consecutive session after this ca"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.1 — "U.S. HOME PRICES BEAT EXPECTATIONS IN JUNE U.S. 20-city home prices rose 0.2% month-over-m"
- DKS (Dick's Sporting Goods Inc) score 5.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.1 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 3.9 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.7 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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