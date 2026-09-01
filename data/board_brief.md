# Transmission Layer — board brief · 2026-09-01 09:23Z

data as of **2026-09-01** · 98 series · 11 red / 32 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.355, 1d in regime; vol-pct 0.293, breadth-off 0.417, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.39, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.17, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.01, last shift 2026-07-16. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.34, corr60 -0.83, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.15, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.15, corr60 0.21, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.49, β 0.2162, p 0.0); driver zc 2.79 → expected 0.721%. Type hit-rate 0.828 (n=1992).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.351, β -0.1179, p 0.0); driver zc 2.79 → expected -0.393%. Type hit-rate 0.828 (n=1992).
- Track record · residual_reversion: hit-rate **0.497** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1992) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.69] cross-asset · 4 series ↑
- ust_2y [RATES]: last 4.34, z20 4.03, zc 2.79, resid-z 2.28 [unexplained], 1d 3.33%, |z20|=4.03; 1y-pct=99
- ust_10y [RATES]: last 4.73, z20 1.35, zc 1.32, resid-z 0.99 [quiet], 1d 1.28%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.44, z20 -1.06, zc -1.45, resid-z 0.00 [quiet], 1d -0.09%, 1y-pct=1
- tips_10y_real [RATES]: last 2.42, z20 0.58, zc 2.13, resid-z 1.76 [unexplained], 1d 3.42%, 1d move +8.0bps ≥ 5bps; 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.898 vs ust_10y
- Watch next: brent (co-move) — not yet - watch; rho 0.591 vs ust_10y
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.338 vs ust_2y, historically leads by 1d
- Source: From the U.K. to Japan, bond yields are jumping as U.S. bonds tumble — MarketWatch Top, 2026-09-01. https://www.marketwatch.com/story/from-the-u-k-to-japan-bond-yields-are-jumping-as-u-s-bonds-tumble-d8b71075?mod=mw_rss_topstories
- Source: Global Market: UK 10-year gilt yields hit highest level since 2008 as oil prices stoke inflation fears — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-uk-10-year-gilt-yields-hit-highest-level-since-2008-as-oil-prices-stoke-inflation-fears/articleshow/133673995.cms
- Source: US Treasury selloff pushes India 10-year bond yield towards 7% — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/bonds/us-treasury-selloff-pushes-india-10-year-bond-yield-towards-7/articleshow/133672835.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.31), 2025-05-23 (d=0.52)

### [RED 7.36] commodities · 2 series ↑
- wti [COMMODITIES]: last 87.82, z20 1.53, zc 1.16, resid-z 0.02 [quiet], 1d 2.40%, 1-session move +2.40% ≥ 1.5%; |z20|=1.53
- brent [COMMODITIES]: last 92.21, z20 0.96, zc 0.89, resid-z -0.12 [quiet], 1d 1.90%, 1-session move +1.90% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.519 vs wti
- Source: Global Market: UK 10-year gilt yields hit highest level since 2008 as oil prices stoke inflation fears — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-uk-10-year-gilt-yields-hit-highest-level-since-2008-as-oil-prices-stoke-inflation-fears/articleshow/133673995.cms
- Source: Nifty holds 24,000 at midday as IT gains, banking drag; crude above ₹8,250 — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/nifty-holds-24000-at-midday-as-it-gains-banking-drag-crude-above-8250/article71414171.ece
- Source: Oil companies set for earnings recovery in Q2 despite uncertainty — Mint Markets, 2026-09-01. https://www.livemint.com/market/mark-to-market/omc-outlook-ioc-bpcl-hpcl-earnings-crude-oil-prices-11788241041505.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.97] commodities · 3 series ↑
- wheat [COMMODITIES]: last 784.75, z20 2.65, zc 1.70, resid-z 1.56 [unexplained], 1d 3.73%, |z20|=2.65; 1y-pct=100
- corn [COMMODITIES]: last 539.50, z20 2.47, zc 3.73, resid-z -0.15 [moved], 1d 4.76%, |z20|=2.47; 1y-pct=100
- soybeans [COMMODITIES]: last 1301.75, z20 2.40, zc 2.03, resid-z 1.30 [moved], 1d 2.08%, |z20|=2.40; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Australia Raises Wheat Crop Forecast as Export Demand Picks Up — Mint Markets, 2026-08-31. https://www.livemint.com/market/australia-raises-wheat-crop-forecast-as-export-demand-picks-up-11788215862266.html
- Source: Chicago wheat falls on selling pressure after recent highs — Mint Markets, 2026-08-31. https://www.livemint.com/market/chicago-wheat-falls-on-selling-pressure-after-recent-highs-11788203489599.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.49] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1732.00, z20 3.49, zc 0.26, resid-z -0.17 [quiet], 1d 0.83%, |z20|=3.49; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy surges 130% in 2026, outpacing Tesla, BYD — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/ather-energy-surges-130-in-2026-outpacing-tesla-byd/article71414201.ece
- Source: Ather Energy’s 130% stock surge leaves Tesla and BYD behind in 2026 — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/stocks/news/ather-energys-130-stock-surge-leaves-tesla-and-byd-behind-in-2026/articleshow/133672575.cms
- Source: Ather Energy share price hits lifetime high | Delivers 423% returns from IPO price — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-hits-lifetime-high-delivers-423-returns-from-ipo-price-11788162211726.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 5.1] dyn_lth ↓
- dyn_lth [EQUITIES]: last 42.01, z20 -3.10, zc -0.85, resid-z -0.94 [quiet], 1d -3.45%, |z20|=3.10
- **Mechanism**: dyn_lth ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: Japan bond yields hit 3% for first time in 30 years amid inflation, fiscal risks — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-bond-yields-hit-3-for-first-time-in-30-years-amid-inflation-fiscal-risks/articleshow/133671709.cms
- Source: Stocks to watch and why on September 1: PVR INOX, E2E Networks, NCC, Brigade Enterprises, Time Technoplast and more — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/stocks-to-watch-and-why-on-september-1-pvr-inox-e2e-networks-ncc-brigade-enterprises-indegene-and-more-11788197253602.html
- Source: BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent defended his U.S. bond-market intervention after criticism from Stanley Druckenmiller. Bessent suggested the veteran investor “lost money” around the time he submitted his critical op-ed. He also defended Treasur — DeItaone, 2026-08-31. https://t.me/walter_bloomberg/35250
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [AMBER 4.97] indices · 2 series ↓
- nifty_midcap_100 [INDICES]: last 63234.15, z20 -2.14, zc -2.77, resid-z -2.08 [unexplained], 1d -1.55%, |z20|=2.14
- nifty_50 [INDICES]: last 23979.50, z20 -1.93, zc -0.77, resid-z 0.39 [quiet], 1d -0.42%, |z20|=1.93
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.738 via nifty_50, z -1.67, reacted); nifty_fmcg (rho 0.593 via nifty_50, z -1.78, reacted); dyn_indianb_ns (rho 0.568 via nifty_midcap_100, z -0.07, quiet); dyn_adanient_bo (rho 0.536 via nifty_midcap_100, z -2.79, reacted); nifty_it (rho 0.516 via nifty_50, z 0.58, quiet)
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.568 vs nifty_midcap_100, historically leads by 1d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.516 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.698 vs nifty_midcap_100
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.511 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.738, z -1.67); nifty_fmcg (rho 0.593, z -1.78); dyn_indianb_ns (rho 0.568, z -0.07); dyn_adanient_bo (rho 0.536, z -2.79)
- Source: Sensex today | Stock Market Live Updates: Nifty, Sensex trade range-bound amid banking sell-off — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-1st-september-2026/article71412225.ece
- Source: Maruti Suzuki is top Nifty 50 loser today - what's driving the fall? — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/maruti-suzuki-is-top-nifty-50-loser-today-whats-driving-the-fall-11788248841268.html
- Source: Nifty holds 24,000 at midday as IT gains, banking drag; crude above ₹8,250 — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/nifty-holds-24000-at-midday-as-it-gains-banking-drag-crude-above-8250/article71414171.ece
- Historical analogues: 2025-07-21 (d=0.6), 2024-11-07 (d=0.84), 2025-07-14 (d=0.96)

### [RED 4.79] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2848.00, z20 -2.79, zc -1.34, resid-z -1.10 [quiet], 1d -2.50%, |z20|=2.79
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.536 via dyn_adanient_bo, z -2.14, reacted); nifty_50 (rho 0.517 via dyn_adanient_bo, z -1.93, reacted); dyn_indusindbk_bo (rho 0.401 via dyn_adanient_bo, z -1.85, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.536, z -2.14); nifty_50 (rho 0.517, z -1.93); dyn_indusindbk_bo (rho 0.401, z -1.85)
- Source: Adani Power leads group rally as buying bets lift sentiment — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/adani-power-leads-group-rally-as-buying-bets-lift-sentiment/article71414084.ece
- Source: How Adani Group stocks are performing today after share prices plunged yesterday | Top gainers and losers — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/adani-green-to-adani-power-how-adani-group-stocks-are-performing-today-after-share-prices-plunged-yesterday-11788241077630.html
- Source: Adani group stocks face heavy selling pressure; Adani Enterprises tumbles nearly 8% — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/adani-group-stocks-face-heavy-selling-pressure-adani-enterprises-tumbles-nearly-8/articleshow/133657152.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 4.64] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 138.94, z20 2.64, zc 1.38, resid-z 1.58 [unexplained], 1d 0.45%, |z20|=2.64
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.386 via dyn_chkp, z 1.32, reacted)
- **India receivers**: dyn_karurvysya_ns (rho -0.386, z 1.32)
- Source: Solar stock to 'Buy' for over 20% returns: Check share price target - recommendation rationale explained — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/solar-stock-to-buy-for-over-20-returns-check-share-price-target-recommendation-rationale-explained-11788252000353.html
- Source: Gold, Silver Price Outlook: Can Gold prices hit  ₹1,70,000 per 10 grams after Jackson Hole shock | Check 2026 targets — Mint Markets, 2026-09-01. https://www.livemint.com/market/commodities/gold-price-outlook-silver-price-outlook-can-gold-prices-hit-rs-1-70-000-after-jackson-hole-shock-check-2026-targets-11788247741029.html
- Source: Veegaland Developers IPO: Price band set at  ₹130- ₹140 per share; check key dates, issue details — Mint Markets, 2026-09-01. https://www.livemint.com/market/ipo/veegaland-developers-ipo-price-band-set-at-rs-130-rs-140-per-share-check-key-dates-issue-details-11788247391496.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2024-10-18 (d=0.02)

## Watchlist (below surfacing floor)
indices · 4 series ↓ (4.4), natgas ↑ (4.0), dyn_hdb ↓ (3.88), midcap_largecap_ratio ↑ (3.59), usd_jpy ↑ (3.5), ust_2s10s ↓ (3.35), gold_silver_ratio ↑ (3.26), dyn_lenskart_ns ↑ (3.18), hy_oas ↓ (2.64), russell_2000 ↓ (2.6), dyn_havells_ns ↓ (2.48), dyn_inoxindia_ns ↑ (2.43)

## India macro
- nifty_50: 23979.5000 (1d -0.42%, z20 -1.93, flag amber)
- nifty_midcap_100: 63234.1484 (1d -1.55%, z20 -2.14, flag amber)
- usd_inr: 94.9300 (1d -0.47%, z20 -0.91, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6370 (1d -1.13%, z20 0.59, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 71.3 — "India's oil imports from US, Venezuela largely a function of price: ONGC Chairman"
- COALINDIA.NS (COAL INDIA LTD) score 70.8 — "India's oil imports from US, Venezuela largely a function of price: ONGC Chairman"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 69.0 — "India's oil imports from US, Venezuela largely a function of price: ONGC Chairman"
- INDIANB.NS (INDIAN BANK) score 67.4 — "HDFC Bank share price hits 52-week low after gaining 2.5% on CEO resignation | What's next"
- BAC (Bank of America Corporation) score 62.0 — "HDFC Bank share price hits 52-week low after gaining 2.5% on CEO resignation | What's next"
- HDB (HDFC Bank Limited) score 55.1 — "HDFC Bank share price hits 52-week low after gaining 2.5% on CEO resignation | What's next"
- IDBI.NS (IDBI BANK LIMITED) score 52.8 — "HDFC Bank share price hits 52-week low after gaining 2.5% on CEO resignation | What's next"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.8 — "HDFC Bank share price hits 52-week low after gaining 2.5% on CEO resignation | What's next"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 52.7 — "HDFC Bank share price hits 52-week low after gaining 2.5% on CEO resignation | What's next"
- COIN (Coinbase Global, Inc.) score 46.2 — "Nikkei, KOSPI to US stocks: Global heatmap before the opening bell of the Indian stock mar"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.2 — "IPO GMP Today Live Updates | Deepa Jewellers IPO receives subscription of 0.48x on Day 1 s"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.7 — "IPO GMP Today Live Updates | Deepa Jewellers IPO receives subscription of 0.48x on Day 1 s"
- TECH (Bio-Techne Corp) score 37.6 — "IPO GMP Today Live Updates | Deepa Jewellers IPO receives subscription of 0.48x on Day 1 s"
- BOND (PIMCO Active Bond Exchange-Tra) score 37.2 — "Global Market: Japan bond yields hit 3% for first time in 30 years amid inflation, fiscal "
- OHI (Omega Healthcare Investors, In) score 34.5 — "Hindustan Copper after OFS: Pros and cons investors should know"
- LTH (Life Time Group Holdings, Inc.) score 32.6 — "Fly-Hi Maritime, Farm Peace IPOs open today: Check price, lot size, GMP and key dates"
- 301077.SZ (CHINASTARS) score 28.9 — "China warns of ‘major risk’ of glacier collapse as landslide death toll nears 1,000"
- CHKP (Check Point Software Technolog) score 27.2 — "ESDS Software Solution IPO Day 3: Last day to buy; check GMP, subscription status, and oth"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.7 — "Refinery to the world: Energy expert Anas Alhajji on India's surprising fuel advantage"
- NVDA (NVIDIA Corporation) score 19.2 — "Multibagger AI stock in focus after bagging Rs 1,000 crore term sheet to provide Nvidia Bl"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.3 — "Deepa Jewellers IPO opens for bidding, GMP at 31%: Should you apply or avoid?"
- JIOFIN.BO (Jio Financial Services Limited) score 14.1 — "Skyways Air Services IPO listing: Shares list at 10% discount to the issue price"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.8 — "FOMO alert: Retail investors sold 1,051 stocks before they soared 36% on average"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.3 — "Muthoot Finance approves Muthoot Money merger to create larger gold loan business"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.2 — "How Adani Group stocks are performing today after share prices plunged yesterday | Top gai"
- META (Meta) score 9.2 — "Battle of metals: Gold or silver? What should investors choose as Warsh stokes rate hike f"
- MS (Morgan Stanley) score 9.1 — "BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent de"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.8 — "China Coking Coal Prices Set for Record 46% Monthly Surge"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.7 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.7 — "Tata Steel Share Price Live Updates: Tata Steel's Daily Performance Update"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.6 — "Tata Steel Share Price Live Updates: Tata Steel's Daily Performance Update"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.5 — "Milky Mist Q1 Results: After strong IPO debut, profit and revenue surge | What financials "
- VT (Vanguard Total World Stock Ind) score 6.9 — "Refinery to the world: Energy expert Anas Alhajji on India's surprising fuel advantage"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.6 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.5 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- DKS (Dick's Sporting Goods Inc) score 1.3 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 1.0 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.2 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.0 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.0 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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