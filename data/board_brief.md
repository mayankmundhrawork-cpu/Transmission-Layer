# Transmission Layer — board brief · 2026-11-20 12:48Z

data as of **2026-11-20** · 97 series · 22 red / 42 amber · 8 events surfaced (42 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.915, 5d in regime; vol-pct 0.996, breadth-off 0.833, Markov P(high-vol) 0.466)
- [WEAK] **safe_haven_gold** — corr20 -0.08, corr60 -0.2, contra nifty_50 corr20=0.24, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-25. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.01, corr60 0.08, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.91, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.25, corr60 0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.29, corr60 0.3, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 1.4910934182710278e-05)
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.32, β 0.3563, p 2e-05); driver zc -1.6 → expected -0.762%. Type hit-rate 0.82 (n=2077).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.289, β 0.2491, p 0.0); driver zc -1.6 → expected -0.533%. Type hit-rate 0.82 (n=2077).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.276, β 0.3188, p 0.0); driver zc -1.81 → expected -0.636%. Type hit-rate 0.82 (n=2077).
- Track record · residual_reversion: hit-rate **0.512** (n=1157) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2077) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.438** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.97] cross-asset · 10 series ↓
- dow_jones [INDICES]: last 49112.63, z20 -4.20, zc -2.00, resid-z -1.49 [moved], 1d -2.16%, |z20|=4.20
- dyn_schd [EQUITIES]: last 34.19, z20 -3.55, zc -1.40, resid-z -2.73 [unexplained], 1d -1.47%, |z20|=3.55
- dyn_ms [EQUITIES]: last 174.98, z20 -3.50, zc -1.85, resid-z -0.43 [priced], 1d -3.42%, |z20|=3.50
- russell_2000 [INDICES]: last 2656.24, z20 -3.07, zc -1.60, resid-z -0.77 [priced], 1d -2.14%, |z20|=3.07
- sp500 [INDICES]: last 7177.56, z20 -2.93, zc -1.81, resid-z -1.20 [moved], 1d -1.99%, |z20|=2.93
- vix [INDICES]: last 30.73, z20 2.72, zc 0.65, resid-z n/a [quiet], 1d 8.05%, |z20|=2.72; 1y-pct=99
- dyn_gs [EQUITIES]: last 847.52, z20 -2.63, zc -1.52, resid-z 0.28 [priced], 1d -2.94%, |z20|=2.63
- dyn_bac [EQUITIES]: last 48.56, z20 -2.60, zc -0.49, resid-z -0.25 [quiet], 1d -0.72%, |z20|=2.60
- dyn_nvda [EQUITIES]: last 146.00, z20 -1.89, zc -1.02, resid-z -1.04 [quiet], 1d -3.29%, 1y-pct=0
- nasdaq_100 [INDICES]: last 26523.44, z20 -1.86, zc -1.28, resid-z 1.89 [unexplained], 1d -2.19%, |z20|=1.86
- **Mechanism**: cross-asset · 10 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.38).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho 0.405 via dyn_bac, z -3.02, reacted); dyn_kaynes_ns (rho 0.392 via dyn_bac, z -1.68, reacted)
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.5 vs dyn_schd, historically leads by 4d
- **India receivers**: usd_inr (rho 0.405, z -3.02); dyn_kaynes_ns (rho 0.392, z -1.68)
- Source: Bank of America strategist warns doom loop could hit stocks with Wall Street underpricing hard-landing risks — MarketWatch Top, 2026-11-20. https://www.marketwatch.com/story/bank-of-america-strategist-warns-doom-loop-could-hit-stocks-with-wall-street-underpricing-hard-landing-risks-c3181e57?mod=mw_rss_topstories
- Source: Missed Anthropic's record IPO? Shares cool off after Nasdaq debut - Here's how Indians can invest — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/missed-anthropics-record-ipo-shares-cool-off-after-nasdaq-debut-heres-how-indians-can-invest-11795176413482.html
- Source: NSE record: With  ₹5.6 lakh cr mcap, overtakes HKEX, Nasdaq to become world's 5th-largest listed exchange ​- top 5 list — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/nse-record-with-rs-5-6-lakh-cr-mcap-overtakes-hkex-nasdaq-to-become-worlds-5th-largest-listed-exchange-top-5-list-11795168082205.html
- Historical analogues: 2026-05-22 (d=0.38), 2025-08-22 (d=1.1), 2025-08-14 (d=1.11)

### [RED 8.02] usd_inr ↓
- usd_inr [FX]: last 92.69, z20 -3.02, zc -1.95, resid-z -1.05 [moved], 1d -0.83%, 20d range extreme; |z20|=3.02; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.44 via usd_inr, z -1.59, reacted); dyn_havells_ns (rho -0.427 via usd_inr, z 1.73, reacted); dyn_indianb_ns (rho -0.417 via usd_inr, z 1.42, reacted); dyn_tataelxsi_ns (rho -0.416 via usd_inr, z 0.94, quiet); dyn_indusindbk_bo (rho -0.407 via usd_inr, z 3.52, reacted)
- **India receivers**: nifty_it (rho -0.44, z -1.59); dyn_havells_ns (rho -0.427, z 1.73); dyn_indianb_ns (rho -0.417, z 1.42); dyn_tataelxsi_ns (rho -0.416, z 0.94)
- Source: Rupee climbs past 93/USD as investors seek shelter in Indian stocks, shorts unwind — ET Markets, 2026-11-20. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-climbs-past-93/usd-as-investors-seek-shelter-in-indian-stocks-shorts-unwind/articleshow/136023536.cms
- Source: Rupee climbs past 93/$ as investors seek shelter in Indian stocks, shorts unwind — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/markets/forex/rupee-climbs-past-93-as-investors-seek-shelter-in-indian-stocks-shorts-unwind/article71723977.ece
- Source: Sharp rupee appreciation may cut IT firms' FY27 earnings by up to 13%: Report — ET Markets, 2026-11-20. https://economictimes.indiatimes.com/markets/forex/sharp-rupee-appreciation-may-cut-it-firms-fy27-earnings-by-up-to-13-report/articleshow/136021296.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 7.41] natgas ↑
- natgas [COMMODITIES]: last 3.58, z20 2.41, zc 2.54, resid-z -1.36 [moved], 1d 9.61%, 1-session move +9.61% ≥ 5.0%; |z20|=2.41
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Mozambique Approves Exxon’s Redesigned $30 Billion Rovuma LNG Plan — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/Mozambique-Approves-Exxons-Redesigned-30-Billion-Rovuma-LNG-Plan.html
- Source: China Gas Upsizes Long-Term LNG Supply with U.S. Venture Global — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/China-Gas-Upsizes-Long-Term-LNG-Supply-with-US-Venture-Global.html
- Source: U.S. natural gas inventories end injection season above normal levels — EIA Today in Energy, 2026-11-18. https://www.eia.gov/todayinenergy/detail.php?id=68484
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 6.71] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3571.10, z20 -3.39, zc -1.60, resid-z -1.97 [unexplained], 1d -3.10%, |z20|=3.39; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 42.15, z20 -2.96, zc -1.66, resid-z 0.09 [priced], 1d -4.88%, |z20|=2.96; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 84.71, z20 2.46, zc n/a, resid-z n/a [quiet], 1d 1.87%, |z20|=2.46; 1y-pct=100
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.554 via comex_gold, z -0.43, quiet); dyn_karurvysya_ns (rho 0.494 via comex_gold, z 0.72, quiet); nifty_metal (rho 0.427 via comex_silver, z 0.11, quiet); dyn_jiofin_bo (rho 0.404 via comex_gold, z 0.59, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.554 vs comex_gold, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.554, z -0.43); dyn_karurvysya_ns (rho 0.494, z 0.72); nifty_metal (rho 0.427, z 0.11); dyn_jiofin_bo (rho 0.404, z 0.59)
- Source: Gold, silver ETF price crash today: Rates at 52-week low — Opportunity for investors or more pain ahead? Experts speak — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/gold-silver-etf-price-crash-today-rates-at-52-week-low-opportunity-for-investors-or-more-pain-ahead-experts-speak-11795163891648.html
- Source: GJC alerts BIS over suspected gold adulteration, urges jewellers to tighten quality checks — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/companies/gjc-alerts-bis-over-suspected-gold-adulteration-urges-jewellers-to-tighten-quality-checks/article71723585.ece
- Source: Gold price crash: Muthoot Finance, Manappuram shares lose sheen, down up to 5% | Is gold heading for deeper correction? — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/gold-price-crash-muthoot-finance-manappuram-shares-lose-sheen-down-up-to-5-is-gold-heading-for-deeper-correction-11795161489903.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.53] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 728.50, z20 4.53, zc 1.36, resid-z 1.20 [quiet], 1d 3.52%, |z20|=4.53
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.562 via dyn_tatatech_ns, z 3.52, reacted); dyn_jiofin_bo (rho 0.505 via dyn_tatatech_ns, z 0.59, quiet); nifty_midcap_100 (rho 0.497 via dyn_tatatech_ns, z 1.24, reacted); dyn_tataelxsi_ns (rho 0.496 via dyn_tatatech_ns, z 0.94, quiet); dyn_indianb_ns (rho 0.442 via dyn_tatatech_ns, z 1.42, reacted)
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.505 vs dyn_tatatech_ns, historically leads by 1d
- **India receivers**: dyn_indusindbk_bo (rho 0.562, z 3.52); dyn_jiofin_bo (rho 0.505, z 0.59); nifty_midcap_100 (rho 0.497, z 1.24); dyn_tataelxsi_ns (rho 0.496, z 0.94)
- Source: Tata Steel shares slide nearly 2% as EU anti-dumping duty and bearish technicals weigh — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/markets/stock-markets/tata-steel-shares-slide-nearly-2-as-eu-anti-dumping-duty-and-bearish-technicals-weigh/article71723418.ece
- Source: Hindustan Zinc vs Tata Steel vs JSW Steel: Which metal stock to buy amid big fall in the metal stocks | Targets — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/hindustan-zinc-vs-tata-steel-vs-jsw-steel-which-metal-stock-to-buy-amid-big-fall-in-the-metal-stocks-targets-11795153441565.html
- Source: Tata Motors PV Share Price Live Updates: Tata Motors PV Stock Price History — ET Markets, 2026-11-20. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-motors-pv-share-price-today-live-20-nov-2026/liveblog/136013458.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [RED 6.25] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 35877.63, z20 -2.93, zc -2.38, resid-z -1.68 [unexplained], 1d -6.63%, |z20|=2.93
- nikkei_225 [INDICES]: last 56576.41, z20 -2.44, zc -3.02, resid-z 0.92 [moved], 1d -4.82%, |z20|=2.44
- kospi [INDICES]: last 4853.85, z20 -1.83, zc -1.89, resid-z 1.37 [moved], 1d -5.53%, |z20|=1.83
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.586 via taiwan_weighted, z 1.5, reacted); midcap_largecap_ratio (rho 0.55 via kospi, z -1.81, reacted); dyn_indusindbk_bo (rho -0.541 via taiwan_weighted, z 3.52, reacted); nifty_it (rho -0.514 via kospi, z -1.59, reacted); nifty_midcap_100 (rho 0.432 via nikkei_225, z 1.24, reacted)
- Watch next: dyn_301077_sz (co-move) — not yet - watch; rho 0.622 vs taiwan_weighted, historically leads by 3d
- **India receivers**: nifty_50 (rho -0.586, z 1.5); midcap_largecap_ratio (rho 0.55, z -1.81); dyn_indusindbk_bo (rho -0.541, z 3.52); nifty_it (rho -0.514, z -1.59)
- Source: Stock market outlook today,20 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-outlook-today-20-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11795135137736.html
- Source: Stock market outlook today,19 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-19-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11795048871272.html

### [AMBER 6.25] brent ↓
- brent [COMMODITIES]: last 89.24, z20 -1.25, zc -1.33, resid-z -1.29 [quiet], 1d -2.98%, 1-session move -2.98% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Iraq's Oil Crackdown Sparks New Showdown With Kurdistan — OilPrice, 2026-11-20. https://oilprice.com/Energy/Energy-General/Iraqs-Oil-Crackdown-Sparks-New-Showdown-With-Kurdistan.html
- Source: WTI Crude Sinks More Than 5% as Global Oil Glut Fears Grow — OilPrice, 2026-11-20. https://oilprice.com/Energy/Energy-General/WTI-Crude-Sinks-More-Than-5-as-Global-Oil-Glut-Fears-Grow.html
- Source: Iran Steps Up Hormuz Tanker Attacks as Oil Prices Slide — OilPrice, 2026-11-20. https://oilprice.com/Latest-Energy-News/World-News/Iran-Steps-Up-Hormuz-Tanker-Attacks-as-Oil-Prices-Slide.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.55] indices · 2 series ↓
- asx_200 [INDICES]: last 8592.60, z20 -2.72, zc -1.68, resid-z -1.81 [unexplained], 1d -1.58%, |z20|=2.72
- hang_seng [INDICES]: last 22410.80, z20 -2.14, zc -1.41, resid-z -1.95 [unexplained], 1d -1.89%, |z20|=2.14; 1y-pct=0
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-02 (z-distance 0.07).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.518 via hang_seng, z -0.43, quiet); dyn_indianb_ns (rho 0.503 via asx_200, z 1.42, reacted); dyn_karurvysya_ns (rho 0.423 via asx_200, z 0.72, quiet); dyn_jiofin_bo (rho 0.398 via hang_seng, z 0.59, quiet); nifty_50 (rho 0.359 via asx_200, z 1.5, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.518 vs hang_seng, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.518, z -0.43); dyn_indianb_ns (rho 0.503, z 1.42); dyn_karurvysya_ns (rho 0.423, z 0.72); dyn_jiofin_bo (rho 0.398, z 0.59)
- Source: South Korea's KOSPI up 1.4%, Hang Seng edges higher as chip stocks recover. Can Anthropic's debut revive the AI trade? — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/south-koreas-kospi-up-1-4-hang-seng-edges-higher-as-chip-stocks-recover-can-anthropics-debut-revive-the-ai-trade-11795083814893.html
- Historical analogues: 2026-04-02 (d=0.07), 2025-12-04 (d=0.08), 2025-08-01 (d=0.29)

## Watchlist (below surfacing floor)
dyn_indusindbk_bo ↑ (5.52), cross-asset · 3 series ↓ (5.29), fx · 2 series ↓ (5.28), dyn_blln ↓ (4.89), indices · 3 series ↓ (4.82), cross-asset · 3 series ↑ (4.82), comex_copper ↓ (4.59), dyn_meta ↓ (4.33), dyn_tgt ↑ (3.84), usd_mxn ↑ (3.61), dyn_crwv ↓ (3.56), shanghai_comp ↓ (2.98)

## India macro
- nifty_50: 25800.5996 (1d 1.12%, z20 1.50, flag amber)
- nifty_midcap_100: 62021.6016 (1d 0.65%, z20 1.24, flag none)
- usd_inr: 92.6900 (1d -0.83%, z20 -3.02, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4039 (1d -0.46%, z20 -1.81, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 101.1 — "Top stocks to watch today: Coal India, Paytm, Ashoka Buildcon, Hexaware Tech, JK Cement, A"
- INOXINDIA.NS (INOX INDIA LIMITED) score 93.5 — "Top stocks to watch today: Coal India, Paytm, Ashoka Buildcon, Hexaware Tech, JK Cement, A"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 92.6 — "Top stocks to watch today: Coal India, Paytm, Ashoka Buildcon, Hexaware Tech, JK Cement, A"
- INDIANB.NS (INDIAN BANK) score 67.0 — "Indian stocks seen falling from nine-month highs; Asia market rout deepens"
- BAC (Bank of America Corporation) score 54.1 — "Kotak Bank Share Price Live Updates: Kotak Bank Stock Price History"
- NVDA (NVIDIA Corporation) score 48.8 — "TRUMP DID NOT TALK TOO MUCH ABOUT NVIDIA OR THE CHINESE SPY WITH CHINESE PRESIDENT XI -FOX"
- HDB (HDFC Bank Limited) score 48.5 — "Kotak Bank Share Price Live Updates: Kotak Bank Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.9 — "Kotak Bank Share Price Live Updates: Kotak Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 44.9 — "Kotak Bank Share Price Live Updates: Kotak Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.9 — "Kotak Bank Share Price Live Updates: Kotak Bank Stock Price History"
- TGT (Target Corporation) score 42.2 — "This small cap stock has surged 100% in 2026; Brokerage sees 29% more upside - Do you own "
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.4 — "Big dividends, thin profits? 7 stocks that are paying out more than they earn - CyberTech "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.8 — "Big dividends, thin profits? 7 stocks that are paying out more than they earn - CyberTech "
- TECH (Bio-Techne Corp) score 38.8 — "Big dividends, thin profits? 7 stocks that are paying out more than they earn - CyberTech "
- OHI (Omega Healthcare Investors, In) score 37.9 — "India’s ‘no AI play’ remains a bother for fund managers even as foreign investors return"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 28.8 — "Senate Passes Sweeping Energy Permitting Reform Bill in 62-33 Vote"
- COIN (Coinbase Global, Inc.) score 27.9 — "Nifty opens lower as global tech selloff weighs; Max Healthcare, Apollo top gainers"
- 301077.SZ (CHINASTARS) score 26.0 — "China-US-Russia talks, economy concerns, Auto Guangzhou"
- LTH (Life Time Group Holdings, Inc.) score 23.7 — "Rupee rises above 93 against US dollar for first time in over seven months"
- BLLN (BillionToOne, Inc.) score 22.7 — "Anthropic shares fall 5% in after-hours after record $107.3 billion IPO"
- CHKP (Check Point Software Technolog) score 22.7 — "This small cap stock has surged 100% in 2026; Brokerage sees 29% more upside - Do you own "
- BOND (PIMCO Active Bond Exchange-Tra) score 18.4 — "Bonds vs equities: India’s stock market rally faces valuation test"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.2 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 16.0 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Stock Price Histor"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.9 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.9 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Price History"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.9 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Stock Price History"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.1 — "Why Tips Films' shares jump 15% after the announcement of voluntary delisting? Experts's v"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "Anthropic shares soar 21% in blockbuster debut: Can the AI giant justify its $1.8 trillion"
- BZ=F (Brent Crude Oil Last Day Finan) score 8.8 — "SPOT GOLD EXTENDS LOSSES, LAST DOWN NEARLY 2% AT $3,551.75/OZ"
- MS (Morgan Stanley) score 8.4 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- META (Meta) score 8.0 — "Hindustan Zinc vs Tata Steel vs JSW Steel: Which metal stock to buy amid big fall in the m"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.3 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Stock Price History"
- GS (Goldman Sachs Group, Inc. (The) score 5.7 — "Goldman Sachs turns bullish on India stock market, upgrades rating to Overweight; sets Nif"
- SCHD (Schwab US Dividend Equity ETF) score 5.6 — "Big dividends, thin profits? 7 stocks that are paying out more than they earn - CyberTech "
- RS (Reliance, Inc.) score 3.2 — "Reliance Industries shares: After 13% surge in 1 month, JPMorgan sees another 23% upside i"
- CRWV (CoreWeave, Inc.) score 2.9 — "A CoreWeave co-founder just made an unconventional $30 million wager on its battered bonds"
- ETERNAL.NS (ETERNAL LIMITED) score 2.9 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.2 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.6 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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