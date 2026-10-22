# Transmission Layer — board brief · 2026-10-22 09:23Z

data as of **2026-10-22** · 97 series · 16 red / 34 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.868, 14d in regime; vol-pct 0.736, breadth-off 1.0, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.38, contra nifty_50 corr20=0.43, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-27. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.01, corr60 0.11, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.04, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.24, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.49, corr60 0.23, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.5035700777074084e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=1864) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.3] commodities · 2 series ↑
- brent [COMMODITIES]: last 112.11, z20 2.47, zc 1.65, resid-z 0.37 [priced], 1d 3.02%, 1-session move +3.02% ≥ 1.5%; |z20|=2.47; 1y-pct=97
- wti [COMMODITIES]: last 99.47, z20 1.29, zc 0.85, resid-z -1.47 [quiet], 1d 2.39%, 1-session move +2.39% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.551 vs brent, historically leads by 5d
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.388 vs wti, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.523 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.519 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.511 vs brent
- Source: Crude oil above $100, US election uncertainty: Will global factors keep Sensex, Nifty 50 under pressure? Experts decode — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/crude-oil-above-100-us-election-uncertainty-will-global-factors-keep-sensex-nifty-50-under-pressure-experts-decode-11792654365472.html
- Source: Iran’s Oil Reserves Run Dry as U.S. Naval Blockade Tightens — OilPrice, 2026-10-22. https://oilprice.com/Latest-Energy-News/World-News/Irans-Oil-Reserves-Run-Dry-as-US-Naval-Blockade-Tightens.html
- Source: India's West Asia oil imports return to pre-war levels in September — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/commodities/indias-west-asia-oil-imports-return-to-pre-war-levels-in-september/article71610330.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.82] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4101.20, z20 -1.69, zc -1.17, resid-z -1.25 [quiet], 1d -1.18%, |z20|=1.69; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 56.01, z20 -1.67, zc -1.09, resid-z -0.44 [quiet], 1d -2.45%, |z20|=1.67; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 73.22, z20 1.50, zc n/a, resid-z n/a [quiet], 1d 1.31%, GSR<75 (extreme low); |z20|=1.50
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.526 vs comex_silver, historically leads by 5d
- Watch next: dxy (inverse) — not yet - watch; rho -0.526 vs comex_gold
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.504 vs comex_silver
- Source: Stocks, gold, or cryptocurrency: Here's how they have performed in 5 years - Which one should you buy? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/stocks-gold-or-cryptocurrency-heres-how-they-have-performed-in-5-years-which-one-should-you-buy-11792655530044.html
- Source: Today’s Gold Rate in India October 22: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-22-2026/article71610670.ece
- Source: Today’s Gold Rate in India October 22: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-22-2026/article71610669.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.82] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 56972.35, z20 -2.15, zc -0.98, resid-z -0.26 [quiet], 1d -1.04%, |z20|=2.15
- india_vix [INDICES]: last 15.90, z20 1.59, zc 0.23, resid-z n/a [quiet], 1d 1.37%, |z20|=1.59
- nifty_50 [INDICES]: last 22646.25, z20 -0.45, zc -0.72, resid-z -1.28 [quiet], 1d -0.72%, 1y-pct=4
- dyn_policybzr_ns [EQUITIES]: last 1030.50, z20 -0.35, zc 0.69, resid-z 1.22 [quiet], 1d 2.23%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.643 via nifty_50, z -2.73, reacted); nifty_metal (rho 0.635 via nifty_midcap_100, z -1.46, reacted); dyn_jiofin_bo (rho 0.635 via nifty_midcap_100, z -1.28, reacted); dyn_bajfinance_ns (rho -0.619 via india_vix, z -1.44, reacted); dyn_indusindbk_bo (rho -0.557 via india_vix, z -1.44, reacted)
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.531 vs nifty_50, historically leads by 2d
- **India receivers**: nifty_fmcg (rho 0.643, z -2.73); nifty_metal (rho 0.635, z -1.46); dyn_jiofin_bo (rho 0.635, z -1.28); dyn_bajfinance_ns (rho -0.619, z -1.44)
- Source: Crude oil above $100, US election uncertainty: Will global factors keep Sensex, Nifty 50 under pressure? Experts decode — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/crude-oil-above-100-us-election-uncertainty-will-global-factors-keep-sensex-nifty-50-under-pressure-experts-decode-11792654365472.html
- Source: Sensex today | Stock Market Live: Sensex, Nifty struggle to rise in choppy trade; 432 stocks hit 52-week lows — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-22nd-october-2026/article71608127.ece
- Source: Nifty trims early losses to 91 points by noon; broad market bleeds as 432 stocks hit 52-week lows — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/nifty-trims-early-losses-to-91-points-by-noon-broad-market-bleeds-as-432-stocks-hit-52-week-lows/article71610598.ece
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.33] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 46099.28, z20 -2.01, zc -1.18, resid-z 0.26 [quiet], 1d -1.68%, |z20|=2.01
- nikkei_225 [INDICES]: last 63139.59, z20 -1.87, zc -1.34, resid-z 0.22 [quiet], 1d -2.29%, |z20|=1.87
- kospi [INDICES]: last 5531.37, z20 -1.70, zc -1.01, resid-z 0.52 [quiet], 1d -3.56%, |z20|=1.70
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.451 via kospi, z -1.03, reacted); dyn_idbi_ns (rho 0.401 via nikkei_225, z -1.96, reacted); midcap_largecap_ratio (rho 0.361 via kospi, z -2.83, reacted)
- **India receivers**: dyn_cartrade_ns (rho 0.451, z -1.03); dyn_idbi_ns (rho 0.401, z -1.96); midcap_largecap_ratio (rho 0.361, z -2.83)
- Source: Global Market: Japan’s Nikkei falls as chip stocks retreat on AI spending concerns — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-as-chip-stocks-retreat-on-ai-spending-concerns/articleshow/135106795.cms
- Source: Japan’s Nikkei jumps over 1% as AI optimism lifts chip stocks; exports rise 16.7% — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-jumps-over-1-as-ai-optimism-lifts-chip-stocks-exports-rise-16-7/articleshow/135081946.cms

### [RED 5.33] dyn_wit ↑
- dyn_wit [EQUITIES]: last 2.15, z20 3.33, zc 1.25, resid-z 1.37 [quiet], 1d 4.88%, |z20|=3.33
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: IT mid-caps vs large-caps: TCS, Infosys, Wipro vs Persistent, Coforge, Tata Tech - Who leads the Q2 results 2026 race? — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/it-mid-caps-vs-large-caps-tcs-infosys-wipro-vs-persistent-coforge-tata-tech-who-leads-the-q2-results-2026-race-11792600156200.html
- Source: Market Trading Guide: Wipro among 5 stock recommendations for Thursday — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-wipro-among-5-stock-recommendations-for-thursday/slideshow/135095527.cms
- Source: Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - Check stop loss, targets — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/top-2-stocks-to-buy-or-sell-for-short-term-wipro-dixon-technologies-by-nagaraj-shetti-check-stop-loss-targets-11792580012562.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [RED 5.23] dow_jones ↑
- dow_jones [INDICES]: last 52851.78, z20 3.23, zc 0.83, resid-z 0.68 [quiet], 1d 0.68%, |z20|=3.23
- **Mechanism**: dow_jones ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.717 vs dow_jones, historically leads by 1d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.879 vs dow_jones
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.65 vs dow_jones, historically leads by 1d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.579 vs dow_jones, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.747 vs dow_jones
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq surges at open as SpaceX, SuperMicro results lift AI stocks — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-ai-stocks-spacex-super-micro-tesla-netflix-fed-rate-hike-treasury-yields-stock-price-news-21st-september-2026/liveblog/135092299.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq surges 1% as SpaceX, AI stocks rise while Netflix slips — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-ai-stocks-spacex-super-micro-tesla-netflix-fed-rate-hike-treasury-yields-stock-price-news-21st-september-2026/liveblog/135092299.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: Nasdaq leads Wall Street higher as SpaceX, Super Micro lift AI sentiment — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-ai-stocks-spacex-super-micro-tesla-netflix-fed-rate-hike-treasury-yields-stock-price-news-21st-september-2026/liveblog/135092299.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-28 (d=0.1), 2025-08-22 (d=0.11)

### [AMBER 4.99] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1794.90, z20 2.16, zc -0.77, resid-z -1.34 [quiet], 1d -2.17%, |z20|=2.16; 1y-pct=99
- nifty_it [INDICES]: last 31948.35, z20 1.99, zc -0.91, resid-z -0.83 [quiet], 1d -1.46%, |z20|=1.99
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.758 via nifty_it, z 1.91, reacted); nifty_50 (rho 0.519 via nifty_it, z -0.45, quiet); dyn_justdial_bo (rho 0.51 via nifty_it, z 2.88, reacted); midcap_largecap_ratio (rho -0.418 via dyn_techm_ns, z -2.83, reacted); dyn_tatatech_ns (rho 0.404 via nifty_it, z -1.33, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.506 vs dyn_techm_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.758, z 1.91); nifty_50 (rho 0.519, z -0.45); dyn_justdial_bo (rho 0.51, z 2.88); midcap_largecap_ratio (rho -0.418, z -2.83)
- Source: SML Isuzu shares: SML Mahindra shares tank for 3rd session in row after 33% gain in 6 months | Buy, sell or hold? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/sml-isuzu-shares-sml-mahindra-shares-tank-for-3rd-session-in-row-after-33-gain-in-6-months-buy-sell-or-hold-11792645465680.html
- Source: Mahindra Finance Q2 net profit surges 55% to Rs 882 crore on volumes, lower credit cost — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-finance-q2-net-profit-surges-55-to-rs-882-crore-on-volumes-lower-credit-cost/articleshow/135094556.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [AMBER 4.32] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 143.49, z20 2.32, zc 0.83, resid-z 0.47 [quiet], 1d 1.87%, |z20|=2.32
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.424 via dyn_chkp, z -1.44, reacted); dyn_tatatech_ns (rho 0.358 via dyn_chkp, z -1.33, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.424, z -1.44); dyn_tatatech_ns (rho 0.358, z -1.33)
- Source: UltraTech Cement shares down 11% in a year: InCred Equities says recovery ahead | Check target, upside, rationale — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/ultratech-cement-shares-down-11-in-a-year-incred-equities-says-recovery-ahead-check-target-upside-rationale-11792649432607.html
- Source: Fujiyama Power Systems share price falls 15% in a month: Is 45% upside still on the table? Check DAM Capital target — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/fujiyama-power-systems-share-price-falls-15-in-a-month-is-45-upside-still-on-the-table-check-dam-capital-target-11792651886721.html
- Source: Hero Motors shares hit 5% lower circuit; stock still up 42% from IPO price | Check key support level — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/hero-motors-shares-hit-5-lower-circuit-stock-still-up-42-from-ipo-price-check-key-support-level-11792651819533.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (4.31), comex_copper ↓ (4.3), dyn_rs ↑ (4.28), dyn_tech ↑ (4.06), dyn_301077_sz ↓ (3.9), hang_seng ↓ (3.81), gbp_usd ↑ (3.62), dyn_jiofin_bo ↓ (3.28), usd_cny ↓ (3.09), dyn_justdial_bo ↑ (2.88), midcap_largecap_ratio ↓ (2.83), usd_jpy ↓ (2.82)

## India macro
- nifty_50: 22646.2500 (1d -0.72%, z20 -0.45, flag amber)
- nifty_midcap_100: 56972.3516 (1d -1.04%, z20 -2.15, flag amber)
- usd_inr: 94.9325 (1d 0.23%, z20 -1.34, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5158 (1d -0.31%, z20 -2.83, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 91.1 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- INOXINDIA.NS (INOX INDIA LIMITED) score 88.4 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 87.1 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- INDIANB.NS (INDIAN BANK) score 80.0 — "HDFC Bank Share Price Live Updates: HDFC Bank Price and Performance Overview"
- BAC (Bank of America Corporation) score 68.7 — "HDFC Bank Share Price Live Updates: HDFC Bank Price and Performance Overview"
- HDB (HDFC Bank Limited) score 62.5 — "HDFC Bank Share Price Live Updates: HDFC Bank Price and Performance Overview"
- IDBI.NS (IDBI BANK LIMITED) score 60.4 — "HDFC Bank Share Price Live Updates: HDFC Bank Price and Performance Overview"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.4 — "HDFC Bank Share Price Live Updates: HDFC Bank Price and Performance Overview"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.4 — "HDFC Bank Share Price Live Updates: HDFC Bank Price and Performance Overview"
- COIN (Coinbase Global, Inc.) score 56.8 — "Global Market: Japan’s Nikkei falls as chip stocks retreat on AI spending concerns"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.0 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- OHI (Omega Healthcare Investors, In) score 52.6 — "Jio IPO: Subscribe on day 2? What investors need to know"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.9 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- TECH (Bio-Techne Corp) score 49.9 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- TGT (Target Corporation) score 44.5 — "U.S. AND ISRAEL REPORTEDLY PLAN NEW IRAN STRIKES AFTER MIDTERMS The U.S. and Israel have r"
- CHKP (Check Point Software Technolog) score 43.2 — "Jio IPO Day 2: GMP at 22%, issue subscribed over 3.16; check brokerage views and key detai"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.9 — "Govt bond selloff to continue as RBI policy minutes hint at more rate hikes"
- RS (Reliance, Inc.) score 31.0 — "Reliance Industries share price: Jio IPO gets blockbuster response, but stock near 52-week"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.1 — "U.S. AND ISRAEL REPORTEDLY PLAN NEW IRAN STRIKES AFTER MIDTERMS The U.S. and Israel have r"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 28.3 — "Vodafone Idea shares: Up 20% in 6 months! Will Q2 results 2026 fuel this rally? Experts' v"
- LTH (Life Time Group Holdings, Inc.) score 24.5 — "U.S. AND ISRAEL REPORTEDLY PLAN NEW IRAN STRIKES AFTER MIDTERMS The U.S. and Israel have r"
- 301077.SZ (CHINASTARS) score 22.5 — "Global Market: Hong Kong stocks slump to four-month low as China stimulus hopes fade"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.9 — "Multibagger stock: Up 30% in 1 year, Shriram Finance among top Nifty gainers - Should you "
- JIOFIN.BO (Jio Financial Services Limited) score 17.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Current Price Upda"
- JUSTDIAL.BO (JUST DIAL LTD.) score 16.9 — "Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.6 — "Multibagger stock: Up 30% in 1 year, Shriram Finance among top Nifty gainers - Should you "
- META (Meta) score 15.0 — "Meta Q3 revenue rises 26% to $64.6 billion, net income jumps 264%"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.4 — "YIELD ON 20-YR U.S. TREASURY BOND PARES DECLINE AFTER $13 BLN AUCTION, LAST DOWN 1.25 BASI"
- SEPN (Septerna, Inc.) score 12.2 — "India's West Asia oil imports return to pre-war levels in September"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.8 — "Q2 results 2026 today, schedule: Swiggy, Adani Energy, HPCL 53 more firms to declare quart"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.2 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.2 — "Stocks to watch, Oct 22: Sagility India, Tata Communications, Bharat Electronics, Omnitech"
- JEF (Jefferies Financial Group Inc.) score 10.6 — "IHCL shares rise 3% as firm raises FY27 guidance. What Jefferies, other brokerages are say"
- GS (Goldman Sachs Group, Inc. (The) score 10.1 — "Goldman Sachs Warns of New Oil Price Shock as Tanker Rates Soar"
- VT (Vanguard Total World Stock Ind) score 6.9 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- NVDA (NVIDIA Corporation) score 6.5 — "NVIDIA MAY ALSO BE A BIDDER FOR AMBARELLA ( $AMBA ) - BETAVILLE"
- WIT (Wipro Limited) score 5.6 — "Market Trading Guide: Wipro among 5 stock recommendations for Thursday"
- ETERNAL.NS (ETERNAL LIMITED) score 5.3 — "Eternal shares jump 2% after strong Q2 show, brokerages see up to 34% upside"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.5 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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