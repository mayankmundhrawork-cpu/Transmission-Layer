# Transmission Layer — board brief · 2026-10-30 10:51Z

data as of **2026-10-30** · 97 series · 12 red / 37 amber · 8 events surfaced (37 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.732, 2d in regime; vol-pct 0.714, breadth-off 0.75, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.4, contra nifty_50 corr20=0.42, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.11, last shift 2026-09-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 0.08, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-11. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.08, corr60 -0.14, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.52, corr60 0.32, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 1.4279752047485772e-08)
- **SETUP** dyn_schd → asx_200: leads 1d (ccf 0.488, β 0.4236, p 0.0); driver zc 1.91 → expected 0.645%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.453, β 0.129, p 0.0); driver zc 1.51 → expected 0.445%. Type hit-rate 0.838 (n=1605).
- Track record · residual_reversion: hit-rate **0.506** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.838** (n=1605) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.26] commodities · 2 series ↑
- wti [COMMODITIES]: last 104.12, z20 1.43, zc 0.82, resid-z -0.97 [quiet], 1d 2.08%, 1-session move +2.08% ≥ 1.5%; 1y-pct=96
- brent [COMMODITIES]: last 113.48, z20 1.01, zc -0.61, resid-z -0.95 [quiet], 1d -1.22%, 1y-pct=96
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.443 via wti, z -0.92, quiet); nifty_fmcg (rho -0.385 via wti, z -0.58, quiet)
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.415 vs wti, historically leads by 4d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.593 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.586 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.565 vs brent
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.533 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.443, z -0.92); nifty_fmcg (rho -0.385, z -0.58)
- Source: Wall Street Banks Raise Oil Price Forecasts as Supply Fears Deepen — OilPrice, 2026-10-30. https://oilprice.com/Latest-Energy-News/World-News/Wall-Street-Banks-Raise-Oil-Price-Forecasts-as-Supply-Fears-Deepen.html
- Source: High Oil Prices Set to Trigger New Wave of North Sea Mergers — OilPrice, 2026-10-30. https://oilprice.com/Latest-Energy-News/World-News/High-Oil-Prices-Set-to-Trigger-New-Wave-of-North-Sea-Mergers.html
- Source: Gold slips as higher oil, US inflation data bolster Fed hike bets — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/gold/gold-slips-as-higher-oil-us-inflation-data-bolster-fed-hike-bets/article71644215.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.76] dyn_jef ↑
- dyn_jef [EQUITIES]: last 49.15, z20 4.76, zc 1.51, resid-z 1.72 [unexplained], 1d 3.45%, |z20|=4.76
- **Mechanism**: dyn_jef ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.387 via dyn_jef, z -1.34, reacted); dyn_bajfinance_ns (rho 0.368 via dyn_jef, z -0.53, quiet)
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.526 vs dyn_jef, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.547 vs dyn_jef
- **India receivers**: dyn_indusindbk_bo (rho 0.387, z -1.34); dyn_bajfinance_ns (rho 0.368, z -0.53)
- Source: NSE's electronic gold receipts could generate ₹1,260 crore revenue by FY30, says Jefferies — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/nses-electronic-gold-receipts-could-generate-1260-crore-revenue-by-fy30-says-jefferies/article71644103.ece
- Source: Coal India shares fall 3% after Q2 results; Jefferies, Motilal Oswal, others cut target price — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/coal-india-shares-fall-3-after-q2-results-jefferies-motilal-oswal-others-cut-target-price/articleshow/135349282.cms
- Source: Q2 earnings upgrades hold above 50%, says Jefferies. Is the profit cycle turning? — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/q2-earnings-upgrades-hold-above-50-says-jefferies-is-the-profit-cycle-turning/articleshow/135345343.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [RED 5.85] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 78.81, z20 2.53, zc n/a, resid-z n/a [quiet], 1d 2.03%, |z20|=2.53
- comex_silver [COMMODITIES]: last 50.65, z20 -2.40, zc -1.28, resid-z -0.80 [quiet], 1d -2.94%, |z20|=2.40; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3992.20, z20 -2.26, zc -0.88, resid-z -0.99 [quiet], 1d -0.97%, |z20|=2.26; 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.554 vs comex_silver, historically leads by 5d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.508 vs gold_silver_ratio, historically leads by 5d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.558 vs gold_silver_ratio
- Source: NSE's electronic gold receipts could generate ₹1,260 crore revenue by FY30, says Jefferies — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/nses-electronic-gold-receipts-could-generate-1260-crore-revenue-by-fy30-says-jefferies/article71644103.ece
- Source: Silver futures decline to ₹1.85 lakh per kg — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/commodities/silver-futures-decline-to-185-lakh-per-kg/article71644300.ece
- Source: Gold slips as higher oil, US inflation data bolster Fed hike bets — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/gold/gold-slips-as-higher-oil-us-inflation-data-bolster-fed-hike-bets/article71644215.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.54] crypto · 2 series ↓
- btc_usd [CRYPTO]: last 77408.05, z20 -2.71, zc -0.20, resid-z -1.78 [unexplained], 1d -0.47%, |z20|=2.71
- eth_usd [CRYPTO]: last 2238.14, z20 -1.95, zc -0.13, resid-z -1.53 [unexplained], 1d -0.50%, |z20|=1.95
- **Mechanism**: crypto · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-02-27 (z-distance 0.15).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Bitcoin hits 6-week low, drops below $78,000 as Binance’s $6 billion hack rattles crypto markets. What should investors do? — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-hits-6-week-low-drops-below-78000-as-binances-6-billion-hack-rattles-crypto-markets-what-should-investors-do/articleshow/135349699.cms
- Source: Binance hack: Tether, Circle freeze $2.4 billion in crypto assets; Bitcoin tumbles below $79,000 | Here's what happened — Mint Markets, 2026-10-30. https://www.livemint.com/market/cryptocurrency/binance-hack-tether-circle-freeze-2-4-billion-in-crypto-assets-bitcoin-tumbles-below-79-000-heres-what-happened-11793321650037.html
- Source: Bitcoin trades near $80,000 after Fed holds rates, signals possibility of further tightening — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-trades-near-80000-after-fed-holds-rates-signals-possibility-of-further-tightening/articleshow/135309957.cms
- Historical analogues: 2025-02-27 (d=0.15), 2026-01-29 (d=0.15), 2025-11-20 (d=0.15)

### [RED 5.53] dyn_cartrade_ns ↓
- dyn_cartrade_ns [EQUITIES]: last 2173.00, z20 -3.53, zc -1.83, resid-z -2.10 [unexplained], 1d -6.54%, |z20|=3.53
- **Mechanism**: dyn_cartrade_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3,377. Here’s why — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/cartrade-tech-shares-tank-over-6-after-q2-results-but-nomura-raises-target-price-to-rs-3377-heres-why/articleshow/135290221.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [RED 5.48] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.35, z20 3.48, zc 2.20, resid-z -0.99 [moved], 1d 5.13%, |z20|=3.48; 1y-pct=98
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Borosil shares skyrocket 16% after strong Q2 results | Is it time to book profits? Target price, stop loss here — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/borosil-shares-skyrocket-16-after-strong-q2-results-is-it-time-to-book-profits-target-price-stop-loss-here-11793335910559.html
- Source: ITC, RIL, HDFC Bank among top laggards as Nifty falls over 12% in 2026: Time to buy beaten-down stocks or wait for a recovery? — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/itc-ril-hdfc-bank-among-top-laggards-as-nifty-falls-over-12-in-2026-time-to-buy-beaten-down-stocks-or-wait-for-a-recovery/articleshow/135345201.cms
- Source: Suzlon Energy Q2 Results: Profit plunges 69% YoY to Rs 394 crore due to one-time deferred tax — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/earnings/suzlon-energy-q2-results-profit-plunges-69-yoy-to-rs-394-crore-revenue-rises-26/articleshow/135304125.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 4.94] dyn_gs ↑
- dyn_gs [EQUITIES]: last 927.52, z20 2.94, zc 0.14, resid-z 0.69 [quiet], 1d 0.25%, |z20|=2.94
- **Mechanism**: dyn_gs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.832 vs dyn_gs, historically leads by 2d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.826 vs dyn_gs, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.802 vs dyn_gs, historically leads by 2d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.605 vs dyn_gs, historically leads by 2d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.678 vs dyn_gs
- Source: Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages after Q2 results. Buy, sell or hold? — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/asian-paints-shares-in-focus-as-jefferies-goldman-sachs-other-brokerages-cut-target-prices-after-q2-results-buy-sell-or-hold/articleshow/135342271.cms
- Source: GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects just one additional Fed rate hike, compared with three currently priced by markets, suggesting the current tightening cycle could be among the smallest since 1983. Strategist Vickie Chang highlighted historicall — DeItaone, 2026-10-28. https://t.me/walter_bloomberg/37659
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.11), 2025-05-13 (d=0.14)

### [RED 4.61] dyn_sepn ↑
- dyn_sepn [EQUITIES]: last 45.17, z20 2.61, zc 0.54, resid-z 0.16 [quiet], 1d 2.08%, |z20|=2.61; 1y-pct=99
- **Mechanism**: dyn_sepn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Q2 results impact: 2 Vedanta stocks rally up to 14% after Sept quarter earnings. How have they performed since demerger? — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/q2-results-impact-2-vedanta-stocks-rally-up-to-14-after-sept-quarter-earnings-how-have-they-performed-since-demerger/articleshow/135344818.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.52), dyn_coalindia_ns ↓ (4.23), shanghai_comp ↓ (4.21), dyn_301077_sz ↓ (4.1), dyn_ohi ↑ (4.01), dyn_tech ↑ (3.92), dyn_jiofin_bo ↓ (3.8), nifty_50 ↑ (3.74), dyn_schd ↑ (3.73), usd_cny ↓ (3.7), dyn_4417_t ↑ (3.46), dyn_atherenerg_ns ↑ (3.16)

## India macro
- nifty_50: 23053.0996 (1d 0.51%, z20 1.74, flag amber)
- nifty_midcap_100: 57304.4492 (1d -0.92%, z20 -0.92, flag none)
- usd_inr: 94.9500 (1d -0.27%, z20 -0.73, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4858 (1d -1.42%, z20 -1.59, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 101.4 — "Indian shares seen opening higher after earnings-led rebound; higher oil to cap gains"
- COALINDIA.NS (COAL INDIA LTD) score 101.2 — "Indian shares seen opening higher after earnings-led rebound; higher oil to cap gains"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 99.7 — "Indian shares seen opening higher after earnings-led rebound; higher oil to cap gains"
- INDIANB.NS (INDIAN BANK) score 78.3 — "Indian shares seen opening higher after earnings-led rebound; higher oil to cap gains"
- BAC (Bank of America Corporation) score 67.0 — "Stocks to Watch, Oct 30: Reliance, Jio Platforms, NIIT Learning, Sagility, OnMobile, IDBI "
- TGT (Target Corporation) score 65.2 — "Jio Platforms shares: Q2 Results 2026 — date, expectations to preview; should you buy or w"
- COIN (Coinbase Global, Inc.) score 62.2 — "Negative bias seen amid global headwinds"
- HDB (HDFC Bank Limited) score 59.9 — "HDFC Life Share Price Live Updates: HDFC Life Price Movement Analysis"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.6 — "Stocks to Watch, Oct 30: Reliance, Jio Platforms, NIIT Learning, Sagility, OnMobile, IDBI "
- IDBI.NS (IDBI BANK LIMITED) score 58.4 — "Stocks to Watch, Oct 30: Reliance, Jio Platforms, NIIT Learning, Sagility, OnMobile, IDBI "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 58.4 — "Stocks to Watch, Oct 30: Reliance, Jio Platforms, NIIT Learning, Sagility, OnMobile, IDBI "
- OHI (Omega Healthcare Investors, In) score 57.6 — "Retail investors borrow  ₹2,227 crore via MTF to buy Jio Platforms shares on listing debut"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.9 — "Why Sterlite Technologies shares hit 5% lower circuit today? Down 9% in 3 days - What's dr"
- CHKP (Check Point Software Technolog) score 44.6 — "Core4 Engineers SME shares to list today: Check IPO subscription status and other key deta"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "Why Sterlite Technologies shares hit 5% lower circuit today? Down 9% in 3 days - What's dr"
- TECH (Bio-Techne Corp) score 39.4 — "Why Sterlite Technologies shares hit 5% lower circuit today? Down 9% in 3 days - What's dr"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 38.8 — "JSW Energy among 6 Nifty500 stocks showing RSI trending up"
- RS (Reliance, Inc.) score 31.1 — "Top stocks to watch today: Reliance, Jio Platforms, Trent, BEL, RVNL shares in focus on Fr"
- LTH (Life Time Group Holdings, Inc.) score 30.4 — "IndiGo shares rise 3.8% post Q2 results; analysts divided on recovery timeline"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.4 — "India's 10-year bond heads for first weekly gain in 11 weeks, set to end record losing run"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 26.4 — "Reliance Industries Q2 results 2026 today: Preview, should you buy, sell or hold ahead of "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.5 — "Tata Capital among 4 Nifty500 stocks closing above VWAP"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.5 — "Tata Capital among 4 Nifty500 stocks closing above VWAP"
- 301077.SZ (CHINASTARS) score 20.9 — "Global Market: China stocks extend losing streak to 12 weeks as global AI selloff hits tec"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.3 — "Crash! Why Equitas Small Finance Bank stock is so much down today? Share price plunges 12%"
- JEF (Jefferies Financial Group Inc.) score 16.9 — "Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages af"
- JIOFIN.BO (Jio Financial Services Limited) score 16.1 — "Jio Financial Services promoter holding rises to 50.98% after 25 crore share allotment"
- SCHD (Schwab US Dividend Equity ETF) score 15.2 — "Laurus Labs share price at record high after Q2 results 20⁠⁩26, dividend announcement - Sh"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 15.2 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.2 — "UKRAINE REPORTEDLY HALTS STRIKES ON RUSSIAN REFINERIES AFTER TRUMP PRESSURE Ukraine has re"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.0 — "Crash! Why Equitas Small Finance Bank stock is so much down today? Share price plunges 12%"
- SEPN (Septerna, Inc.) score 12.5 — "Q2 results impact: 2 Vedanta stocks rally up to 14% after Sept quarter earnings. How have "
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.6 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- META (Meta) score 8.1 — "Shanghai Exchange Halts Duty-Free Metal Delivery Against Futures"
- INFY (Infosys Limited) score 7.1 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- VT (Vanguard Total World Stock Ind) score 7.0 — "World's First Permanent Nuclear Waste Site Wins License in Finland"
- GS (Goldman Sachs Group, Inc. (The) score 6.2 — "Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages af"
- SWIGGY.NS (SWIGGY LIMITED) score 2.1 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.6 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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