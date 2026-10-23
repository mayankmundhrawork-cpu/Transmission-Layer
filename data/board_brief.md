# Transmission Layer — board brief · 2026-10-23 23:07Z

data as of **2026-10-23** · 97 series · 24 red / 43 amber · 8 events surfaced (39 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.833, 15d in regime; vol-pct 0.791, breadth-off 0.875, Markov P(high-vol) 0.031)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.37, contra nifty_50 corr20=0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.01, corr60 0.13, last shift 2026-08-28. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.22, corr60 0.06, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.77, last shift 2026-09-02. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.14, corr60 -0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.04, corr60 -0.14, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.53, corr60 0.24, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **8 of 89** scanned series survive multiplicity control (effective p ≤ 0.003389620038554586)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.591, β 0.4889, p 0.0); driver zc -1.62 → expected -0.609%. Type hit-rate 0.818 (n=1877).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.46, β 0.7756, p 0.0); driver zc -1.62 → expected -0.966%. Type hit-rate 0.818 (n=1877).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.409, β -0.3417, p 0.0); driver zc -1.62 → expected 0.426%. Type hit-rate 0.818 (n=1877).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.396, β 0.2549, p 2e-05); driver zc -1.62 → expected -0.318%. Type hit-rate 0.818 (n=1877).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.379, β -0.2343, p 0.0); driver zc -1.62 → expected 0.292%. Type hit-rate 0.818 (n=1877).
- Track record · residual_reversion: hit-rate **0.5** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=1877) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.26] cross-asset · 5 series ↓
- ust_10y [RATES]: last 4.96, z20 -3.60, zc -3.31, resid-z -3.95 [unexplained], 1d -3.31%, |z20|=3.60
- ust_2y [RATES]: last 4.65, z20 -3.44, zc -2.65, resid-z -2.93 [unexplained], 1d -3.33%, |z20|=3.44
- tips_10y_real [RATES]: last 2.64, z20 -3.33, zc -2.43, resid-z -2.52 [unexplained], 1d -4.35%, 1d move -12.0bps ≥ 5bps; |z20|=3.33
- ust_30y [RATES]: last 5.29, z20 -2.82, zc -3.00, resid-z -3.38 [unexplained], 1d -2.40%, |z20|=2.82
- dyn_bond [EQUITIES]: last 88.51, z20 2.22, zc -0.52, resid-z 0.08 [quiet], 1d -0.20%, |z20|=2.22
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho 0.354 via ust_2y, z -2.08, reacted)
- Watch next: dxy (inverse) — not yet - watch; rho -0.56 vs dyn_bond
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.506 vs dyn_bond
- **India receivers**: dyn_atherenerg_ns (rho 0.354, z -2.08)
- Source: US Treasury yields rise but 10-year stays below 5% as AI jitters persist — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-rise-but-10-year-stays-below-5-as-ai-jitters-persist/articleshow/135151795.cms
- Source: India's 10-year bond falls for 10th week in record slump — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/bonds/indias-10-year-bond-falls-for-10th-week-in-record-slump/articleshow/135145225.cms
- Source: Global Market: Eurozone bond markets stabilise after volatile week — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-markets-stabilise-after-volatile-week/articleshow/135142036.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.13] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4010.00, z20 -3.37, zc -0.91, resid-z -2.09 [unexplained], 1d -1.24%, |z20|=3.37; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 53.96, z20 -2.35, zc -0.54, resid-z 0.40 [quiet], 1d -1.47%, |z20|=2.35; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 74.31, z20 1.81, zc n/a, resid-z n/a [quiet], 1d 0.23%, GSR<75 (extreme low); |z20|=1.81
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.506 vs comex_silver, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.518 vs comex_gold
- Source: GOLD TESTS $4,000 AS INFLATION FEARS TRIGGER SELLING Gold futures fell 1.10% to $3,980.80/oz, heading for a nearly 4% weekly loss. Rising oil prices are fueling inflation concerns and expectations of higher interest rates, pressuring the metal. Saxo Bank warns that short-term speculative selling is  — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37472
- Source: Silver crashes  ₹56000/kg from August peak; gold slides 23000/10 grams. What’s driving the selloff in precious metals — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/silver-crashes-rs-56000-kg-from-august-peak-gold-slides-23000-10-grams-what-s-driving-the-selloff-in-precious-metals-11792763090890.html
- Source: UBS SEES $4,000 AS KEY SUPPORT FOR GOLD UBS expects gold could retest $4,000/oz, but sees strong dip-buying demand establishing a floor. Despite rising U.S. real yields and a stronger dollar, central bank buying, Chinese demand and debt concerns continue to support prices. UBS forecasts 750–1,000 me — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37459
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.9] commodities · 2 series ↑
- wti [COMMODITIES]: last 103.44, z20 2.07, zc 1.44, resid-z 0.93 [quiet], 1d 3.99%, 1-session move +3.99% ≥ 1.5%; |z20|=2.07; 1y-pct=95
- brent [COMMODITIES]: last 111.66, z20 1.88, zc -0.57, resid-z -1.32 [quiet], 1d -1.33%, |z20|=1.88; 1y-pct=96
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.369 via wti, z -2.99, reacted)
- **India receivers**: nifty_midcap_100 (rho -0.369, z -2.99)
- Source: Oil markets are on edge ahead of the weekend, as midterm elections near and fresh U.S. strikes on Iran are predicted — MarketWatch Top, 2026-10-23. https://www.marketwatch.com/story/oil-markets-are-on-edge-ahead-of-the-weekend-as-midterm-elections-near-and-fresh-u-s-strikes-on-iran-are-predicted-8c27e634?mod=mw_rss_topstories
- Source: U.S. Rig Count Holds Steady as Oil Prices Surge — OilPrice, 2026-10-23. https://oilprice.com/Energy/Energy-General/US-Rig-Count-Holds-Steady-as-Oil-Prices-Surge.html
- Source: $120 Oil Is Almost Here, and Trump Has Few Good Options — OilPrice, 2026-10-23. https://oilprice.com/Energy/Energy-General/120-Oil-Is-Almost-Here-and-Trump-Has-Few-Good-Options.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.44] cross-asset · 7 series ↓
- dyn_swiggy_ns [EQUITIES]: last 176.00, z20 -3.10, zc -7.14, resid-z -6.69 [unexplained], 1d -16.75%, |z20|=3.10; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 55799.90, z20 -2.99, zc -2.14, resid-z -3.16 [unexplained], 1d -2.21%, |z20|=2.99
- india_vix [INDICES]: last 16.81, z20 2.26, zc 1.13, resid-z n/a [quiet], 1d 6.68%, |z20|=2.26
- dyn_jiofin_bo [EQUITIES]: last 205.00, z20 -2.17, zc -1.93, resid-z -1.51 [unexplained], 1d -2.84%, |z20|=2.17; 1y-pct=0
- nifty_metal [INDICES]: last 11473.35, z20 -1.97, zc -1.99, resid-z -2.04 [unexplained], 1d -2.75%, |z20|=1.97
- dyn_policybzr_ns [EQUITIES]: last 1015.00, z20 -0.66, zc -0.66, resid-z -0.11 [quiet], 1d -2.21%, 1y-pct=2
- nifty_50 [INDICES]: last 22600.00, z20 -0.54, zc -0.40, resid-z -0.13 [quiet], 1d -0.39%, 1y-pct=3
- **Mechanism**: cross-asset · 7 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.642 via nifty_50, z -2.61, reacted); dyn_bajfinance_ns (rho -0.621 via india_vix, z -2.14, reacted); dyn_adanient_bo (rho 0.6 via nifty_metal, z -2.07, reacted); midcap_largecap_ratio (rho 0.587 via nifty_midcap_100, z -3.53, reacted); dyn_indusindbk_bo (rho -0.568 via india_vix, z -1.83, reacted)
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.558 vs nifty_midcap_100, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.524 vs nifty_50, historically leads by 2d
- **India receivers**: nifty_fmcg (rho 0.642, z -2.61); dyn_bajfinance_ns (rho -0.621, z -2.14); dyn_adanient_bo (rho 0.6, z -2.07); midcap_largecap_ratio (rho 0.587, z -3.53)
- Source: U.S. ECONOMY BOOMS, BUT INFLATION WARNING FLASHES RED October's flash S&P Global PMI signals strong economic growth alongside accelerating inflation. 🔸 Composite PMI: 57.6 vs. 58.4 prior 🔸 Services PMI: 57.9 vs. 58.8 🔸 Manufacturing PMI: 56.0 — 53-month high 🔸 GDP growth: Consistent with roughly 5%  — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37466
- Source: U.S. S&P GLOBAL OCTOBER FLASH COMPOSITE PMI AT 57.6 (VS 58.4 IN SEPTEMBER) U.S. S&P GLOBAL OCTOBER FLASH SERVICES PMI AT 57.9 (FORECAST 58.0) U.S. S&P GLOBAL OCTOBER FLASH MANUFACTURING PMI AT 56.0 (FORECAST 55.5) — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37465
- Source: Bharat Electronics among 4 Sensex stocks to hit 52-week lows; shares fall up to 9% in a month — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/stocks/news/bharat-electronics-among-4-sensex-stocks-to-hit-52-week-lows-shares-fall-up-to-9-in-a-month/slideshow/135147674.cms
- Historical analogues: 2025-07-21 (d=1.08), 2025-12-19 (d=1.16), 2025-07-14 (d=1.31)

### [RED 6.14] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 159.03, z20 4.14, zc 2.04, resid-z 0.79 [moved], 1d 4.64%, |z20|=4.14
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.355 via dyn_chkp, z -1.83, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.355, z -1.83)
- Source: Supreme Petrochem Q2 results, dividend 2026: Check amount, record date, yield, history, stock returns — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/supreme-petrochem-q2-results-dividend-2026-check-amount-record-date-yield-history-stock-returns-11792772862871.html
- Source: NBFC stock crashes 25% in month, but ICICI Securities sees a potential 50% rally - Do you own it? Check target price — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/nbfc-stock-crashes-25-in-month-but-icici-securities-sees-a-potential-50-rally-do-you-own-it-check-target-price-11792757924909.html
- Source: FMCG stocks to buy: Anand Rathi names Marico, GCPL, Asian Paints, Mrs Bector Food - check ratings and target prices — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/fmcg-stocks-to-buy-now-anand-rathi-names-marico-gcpl-asian-paints-mrs-bector-food-check-ratings-and-target-prices-11792751055004.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 6.08] cross-asset · 4 series ↓
- dyn_vt [EQUITIES]: last 155.88, z20 -2.42, zc -0.46, resid-z -1.21 [quiet], 1d -0.41%, |z20|=2.42
- vix [INDICES]: last 19.45, z20 2.24, zc 0.22, resid-z n/a [quiet], 1d 2.21%, |z20|=2.24
- nasdaq_100 [INDICES]: last 28956.07, z20 -2.12, zc -0.01, resid-z -0.62 [quiet], 1d -0.01%, |z20|=2.12
- sp500 [INDICES]: last 7622.99, z20 -1.97, zc -0.62, resid-z -1.84 [unexplained], 1d -0.53%, |z20|=1.97
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.776 vs dyn_vt, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.689 vs dyn_vt
- Watch next: dax (co-move) — not yet - watch; rho 0.62 vs dyn_vt
- Source: Can Nvidia’s stock become a safe haven as Wall Street rethinks the AI trade? — MarketWatch Top, 2026-10-23. https://www.marketwatch.com/story/can-nvidias-stock-become-a-safe-haven-as-wall-street-rethinks-the-ai-trade-64862936?mod=mw_rss_topstories
- Source: PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially underestimated prediction markets, according to Bank of America's Shaun Kelley. Platforms like Kalshi have challenged traditional sportsbooks, including DraftKings and FanDuel. Their key advantages: access across all — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37491
- Source: S&P 500 AND NASDAQ HIT A FIVE-WEEK LOW; LAST DOWN 0.4% AND 0.2%, RESPECTIVELY — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37464
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [AMBER 5.43] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 164.40, z20 -2.11, zc -0.60, resid-z -0.79 [quiet], 1d -2.77%, |z20|=2.11
- btc_usd [CRYPTO]: last 80678.47, z20 -1.82, zc -0.35, resid-z -0.44 [quiet], 1d -0.78%, |z20|=1.82
- eth_usd [CRYPTO]: last 2362.37, z20 -1.51, zc -0.26, resid-z -0.23 [quiet], 1d -1.00%, |z20|=1.51
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.35).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.394 via btc_usd, z -2.72, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.394, z -2.72)
- Source: U.S. ECONOMY BOOMS, BUT INFLATION WARNING FLASHES RED October's flash S&P Global PMI signals strong economic growth alongside accelerating inflation. 🔸 Composite PMI: 57.6 vs. 58.4 prior 🔸 Services PMI: 57.9 vs. 58.8 🔸 Manufacturing PMI: 56.0 — 53-month high 🔸 GDP growth: Consistent with roughly 5%  — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37466
- Source: U.S. S&P GLOBAL OCTOBER FLASH COMPOSITE PMI AT 57.6 (VS 58.4 IN SEPTEMBER) U.S. S&P GLOBAL OCTOBER FLASH SERVICES PMI AT 57.9 (FORECAST 58.0) U.S. S&P GLOBAL OCTOBER FLASH MANUFACTURING PMI AT 56.0 (FORECAST 55.5) — DeItaone, 2026-10-23. https://t.me/walter_bloomberg/37465
- Source: Global Market: Eurozone bond markets stabilise after volatile week — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-markets-stabilise-after-volatile-week/articleshow/135142036.cms
- Historical analogues: 2025-10-22 (d=0.35), 2025-03-31 (d=0.51), 2025-10-30 (d=0.52)

### [AMBER 5.38] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 46041.43, z20 -2.06, zc -1.26, resid-z 0.02 [quiet], 1d -1.81%, |z20|=2.06
- nikkei_225 [INDICES]: last 62726.83, z20 -1.89, zc -0.15, resid-z 0.34 [quiet], 1d -0.29%, |z20|=1.89
- kospi [INDICES]: last 5524.45, z20 -1.51, zc -0.05, resid-z 0.53 [quiet], 1d -0.17%, |z20|=1.51
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.446 via kospi, z -1.28, reacted); dyn_idbi_ns (rho 0.429 via nikkei_225, z -3.07, reacted)
- **India receivers**: dyn_cartrade_ns (rho 0.446, z -1.28); dyn_idbi_ns (rho 0.429, z -3.07)
- Source: Japan’s Nikkei falls over 1% as Wall Street tech selloff rattles markets — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-falls-over-1-as-wall-street-tech-selloff-rattles-markets/articleshow/135133891.cms
- Source: Stock market outlook today, 23 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-23-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11792716174246.html
- Source: Global Market: Japan’s Nikkei falls as chip stocks retreat on AI spending concerns — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-as-chip-stocks-retreat-on-ai-spending-concerns/articleshow/135106795.cms

## Watchlist (below surfacing floor)
dyn_meta ↓ (5.35), natgas ↓ (5.25), usd_jpy ↓ (5.18), dyn_tatatech_ns ↓ (5.02), dyn_lth ↑ (4.85), dyn_coalindia_ns ↓ (4.62), cross-asset · 2 series ↑ (4.57), dyn_bajfinance_ns ↓ (4.14), dyn_atherenerg_ns ↓ (4.08), dyn_adanient_bo ↓ (4.07), hy_oas ↑ (4.04), usd_cny ↓ (3.82)

## India macro
- nifty_50: 22600.0000 (1d -0.39%, z20 -0.54, flag amber)
- nifty_midcap_100: 55799.8984 (1d -2.21%, z20 -2.99, flag red)
- usd_inr: 94.9300 (1d 0.65%, z20 -1.11, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4690 (1d -1.83%, z20 -3.53, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 97.0 — "EAAA India Alternatives mops up Rs 360 crore from anchor investors; IPO opens on Oct 26"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 95.7 — "EAAA India Alternatives mops up Rs 360 crore from anchor investors; IPO opens on Oct 26"
- INOXINDIA.NS (INOX INDIA LIMITED) score 95.0 — "EAAA India Alternatives mops up Rs 360 crore from anchor investors; IPO opens on Oct 26"
- INDIANB.NS (INDIAN BANK) score 80.3 — "PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially undere"
- BAC (Bank of America Corporation) score 72.8 — "PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially undere"
- HDB (HDFC Bank Limited) score 64.2 — "PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially undere"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 62.7 — "PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially undere"
- IDBI.NS (IDBI BANK LIMITED) score 61.9 — "PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially undere"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 61.9 — "PREDICTION MARKETS ARE DISRUPTING THE SPORTS BETTING INDUSTRY Wall Street initially undere"
- OHI (Omega Healthcare Investors, In) score 60.2 — "Investors piled a record sum into a leveraged semiconductor ETF last week. Things didn’t w"
- COIN (Coinbase Global, Inc.) score 57.8 — "U.S. S&P GLOBAL OCTOBER FLASH COMPOSITE PMI AT 57.6 (VS 58.4 IN SEPTEMBER) U.S. S&P GLOBAL"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.2 — "Q2 Results Today Highlights: JSW Steel posts ₹5,359 cr profit; Adani Power jumps 134%, Inf"
- TGT (Target Corporation) score 44.9 — "Top telecom shares to buy: Bharti Airtel, Vodafone Idea, Indus Towers by Ambit Capital wit"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.6 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- TECH (Bio-Techne Corp) score 44.6 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- CHKP (Check Point Software Technolog) score 43.3 — "Supreme Petrochem Q2 results, dividend 2026: Check amount, record date, yield, history, st"
- LTH (Life Time Group Holdings, Inc.) score 33.7 — "RUSSIAN DEFMIN SAYS CEASEFIRE IN RUSSIAN-CONTROLLED OLESHKY TO BEGIN ON OCT. 27 - IFX RUSS"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.6 — "Global Market: French bond selloff raises debt concerns across Europe amid social unrest"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.9 — "Why Trump and Carney Haven’t Touched Energy in Their Tariff War"
- RS (Reliance, Inc.) score 28.4 — "IPO Subscription status comparison: Reliance Jio IPO vs Hyundai IPO vs NSE IPO - Who won t"
- 301077.SZ (CHINASTARS) score 27.5 — "What will China’s fifth plenum mean for the root-and-branch corruption drive?"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 23.8 — "Chennai Petroleum vs MRPL: Which PSU refinery stock wins on Q2 profit, revenue, dividends?"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.8 — "Jana Small Finance Bank Q2 profit jumps 127%, raises FY27 growth outlook"
- JIOFIN.BO (Jio Financial Services Limited) score 20.4 — "U.S. S&P GLOBAL OCTOBER FLASH COMPOSITE PMI AT 57.6 (VS 58.4 IN SEPTEMBER) U.S. S&P GLOBAL"
- BZ=F (Brent Crude Oil Last Day Finan) score 18.6 — "Investors piled a record sum into a leveraged semiconductor ETF last week. Things didn’t w"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 18.5 — "Q2 Results Today Highlights: JSW Steel posts ₹5,359 cr profit; Adani Power jumps 134%, Inf"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.3 — "RBI governor reiterates listing requirement for top NBFCs as focus intensifies on Tata Son"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.3 — "RBI governor reiterates listing requirement for top NBFCs as focus intensifies on Tata Son"
- META (Meta) score 17.9 — "GOLD TESTS $4,000 AS INFLATION FEARS TRIGGER SELLING Gold futures fell 1.10% to $3,980.80/"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.6 — "Jana Small Finance Bank Q2 profit jumps 127%, raises FY27 growth outlook"
- SEPN (Septerna, Inc.) score 17.0 — "CANADIAN RETAIL SALES SURGE, SIGNALING STRONGER CONSUMER DEMAND Canada's retail sales post"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.4 — "Some Republicans are opposing Trump on tariffs. Maine’s Susan Collins just got him to back"
- JEF (Jefferies Financial Group Inc.) score 10.8 — "Swiggy vs Eternal shares compared: Which is better stock to buy post Q2 results? Jefferies"
- GS (Goldman Sachs Group, Inc. (The) score 8.6 — "Ola Electric shares dip 5% after Goldman Sachs downgrades stock to Sell. Here’s why"
- NVDA (NVIDIA Corporation) score 6.4 — "Can Nvidia’s stock become a safe haven as Wall Street rethinks the AI trade?"
- SWIGGY.NS (SWIGGY LIMITED) score 5.9 — "Swiggy vs Eternal shares compared: Which is better stock to buy post Q2 results? Jefferies"
- VT (Vanguard Total World Stock Ind) score 5.7 — "Reliance Jio IPO Global Record: Another feather in cap! History created - 1st IPO worldwid"
- WIT (Wipro Limited) score 5.5 — "Top stocks to buy: IT stocks soar! TCS, Infosys, HCL Tech, Wipro - Nifty IT up over 3% tod"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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