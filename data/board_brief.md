# Transmission Layer — board brief · 2026-11-05 01:33Z

data as of **2026-11-05** · 97 series · 15 red / 30 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.75, 1d in regime; vol-pct None, breadth-off 0.75, Markov P(high-vol) 0.176)
- [INVERTED] **safe_haven_gold** — corr20 -0.69, corr60 -0.56, contra nifty_50 corr20=0.26, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.12, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.05, corr60 0.06, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.76, last shift 2026-09-17. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.31, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.09, corr60 -0.11, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.63, corr60 0.41, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **6 of 89** scanned series survive multiplicity control (effective p ≤ 0.002527746855344626)
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.538, β 0.8766, p 0.0); driver zc 1.94 → expected 1.486%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.533, β 0.8795, p 0.0); driver zc 1.94 → expected 1.491%. Type hit-rate 0.818 (n=1943).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.532, β 0.8344, p 0.0); driver zc 1.75 → expected 1.321%. Type hit-rate 0.818 (n=1943).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.513, β 0.8251, p 0.0); driver zc 1.75 → expected 1.306%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_demz → nikkei_225: leads 1d (ccf 0.504, β 0.7806, p 0.0); driver zc 2.33 → expected 1.648%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_demz → taiwan_weighted: leads 1d (ccf 0.484, β 0.7628, p 0.0); driver zc 2.33 → expected 1.611%. Type hit-rate 0.818 (n=1943).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.471, β -0.0845, p 0.0); driver zc -2.47 → expected 1.729%. Type hit-rate 0.818 (n=1943).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.451, β 0.7508, p 0.0); driver zc 3.94 → expected 2.277%. Type hit-rate 0.818 (n=1943).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.422, β -0.0779, p 0.0); driver zc -2.47 → expected 1.593%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.42, β 0.3216, p 0.0); driver zc 1.81 → expected 1.152%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.406, β 0.3163, p 0.0); driver zc 1.81 → expected 1.133%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.405, β 1.008, p 0.0); driver zc 1.94 → expected 1.709%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.362, β -0.0906, p 0.0); driver zc 3.39 → expected -0.501%. Type hit-rate 0.818 (n=1943).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.349, β 0.8385, p 0.0); driver zc 1.75 → expected 1.327%. Type hit-rate 0.818 (n=1943).
- **SETUP** dyn_demz → kospi: leads 1d (ccf 0.336, β 0.7952, p 0.0); driver zc 2.33 → expected 1.679%. Type hit-rate 0.818 (n=1943).
- **SETUP** vix → kospi: leads 1d (ccf -0.332, β -0.0914, p 0.0); driver zc -2.47 → expected 1.869%. Type hit-rate 0.818 (n=1943).
- Track record · residual_reversion: hit-rate **0.509** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=1943) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.94] cross-asset · 7 series ↑
- dyn_jef [EQUITIES]: last 51.18, z20 3.61, zc 1.71, resid-z 0.48 [priced], 1d 5.40%, |z20|=3.61
- dow_jones [INDICES]: last 53357.03, z20 2.88, zc 3.94, resid-z 3.55 [unexplained], 1d 3.03%, |z20|=2.88
- brent [COMMODITIES]: last 94.07, z20 -2.64, zc 0.00, resid-z -3.33 [unexplained], 1d 0.00%, |z20|=2.64
- dyn_gs [EQUITIES]: last 928.20, z20 2.44, zc 1.81, resid-z -0.28 [priced], 1d 3.58%, |z20|=2.44
- wti [COMMODITIES]: last 87.33, z20 -2.33, zc 0.00, resid-z -3.07 [unexplained], 1d 0.00%, |z20|=2.33
- russell_2000 [INDICES]: last 2856.96, z20 2.08, zc 1.36, resid-z -0.80 [quiet], 1d 1.58%, |z20|=2.08
- vix [INDICES]: last 16.57, z20 -0.53, zc -2.47, resid-z n/a [moved], 1d -20.45%, 1-session move -20.45% ≥ 15.0%
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.534 via wti, z 1.87, reacted); nifty_midcap_100 (rho -0.518 via wti, z 1.25, reacted); dyn_indusindbk_bo (rho 0.452 via dyn_jef, z 0.13, quiet)
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.683 vs dow_jones, historically leads by 1d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.653 vs dyn_jef, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.561 vs dyn_jef, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.52 vs dyn_jef, historically leads by 5d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.647 vs dow_jones
- **India receivers**: dyn_muthootfin_ns (rho -0.534, z 1.87); nifty_midcap_100 (rho -0.518, z 1.25); dyn_indusindbk_bo (rho 0.452, z 0.13)
- Source: Global Market Today: Asian stocks rise as oil slides after US midterm elections — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-rise-as-oil-slides-after-us-midterm-elections/articleshow/135555294.cms
- Source: US midterm elections: Crude cools, but Iran war risks keeps markets guessing — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/us-midterm-elections-crude-cools-but-iran-war-risks-keeps-markets-guessing/articleshow/135555256.cms
- Source: Oil Crashes 9% as Trump and Vance Blame Iran War for Midterm Rout — OilPrice, 2026-11-04. https://oilprice.com/Latest-Energy-News/World-News/Oil-Crashes-9-as-Trump-and-Vance-Blame-Iran-War-for-Midterm-Rout.html
- Historical analogues: 2026-05-22 (d=0.46), 2025-10-28 (d=0.87), 2025-08-14 (d=0.87)

### [RED 6.12] indices · 2 series ↑
- nifty_50 [INDICES]: last 23960.60, z20 3.28, zc 0.69, resid-z 0.71 [quiet], 1d 0.63%, |z20|=3.28
- nifty_fmcg [INDICES]: last 46266.95, z20 2.55, zc 1.05, resid-z 1.47 [quiet], 1d 1.51%, |z20|=2.55
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.703 via nifty_50, z 1.25, reacted); dyn_bajfinance_ns (rho 0.627 via nifty_50, z 2.17, reacted); dyn_jiofin_bo (rho 0.609 via nifty_50, z 2.11, reacted); dyn_indusindbk_bo (rho 0.562 via nifty_50, z 0.13, quiet); nifty_metal (rho 0.552 via nifty_50, z 2.2, reacted)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.505 vs nifty_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.705 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.562 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.703, z 1.25); dyn_bajfinance_ns (rho 0.627, z 2.17); dyn_jiofin_bo (rho 0.609, z 2.11); dyn_indusindbk_bo (rho 0.562, z 0.13)
- Source: Sensex today | Stock Market Live Updates: Stock to buy today: Usha Martin (₹486) – BUY — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-5-november-2026/article71665358.ece
- Source: US Midterm Election Results 2026 impact: What Trump's loss mean for Sensex, Nifty, gold, silver rates? Experts' views — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-impact-what-trumps-loss-mean-for-sensex-nifty-gold-silver-rates-experts-views-11793838614653.html
- Source: US optimism fuels Nifty’s strongest 5-day rally in seven months — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/us-optimism-fuels-niftys-strongest-5-day-rally-in-seven-months/article71665638.ece
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [RED 5.57] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 163.09, z20 3.57, zc 2.77, resid-z -1.12 [moved], 1d 5.63%, |z20|=3.57; 1y-pct=96
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Stocks to buy in November: Axis Direct names Nuvama, BEML and Petronet, sees up to 27% upside; target, rationale — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/stocks-to-buy-in-november-axis-direct-names-nuvama-beml-and-petronet-sees-up-to-27-upside-target-rationale-11793790461951.html
- Source: Clean Max shares: Power stock jumps 42% in YTD; will this rally continue after Q2 results 2026? Expert views, target — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/clean-max-shares-power-stock-jumps-42-in-ytd-will-this-rally-continue-after-q2-results-2026-expert-views-target-11793772700847.html
- Source: Bharat Electronics shares gain 3% as Motilal raises target price after Q2; Elara Capital upgrades to Buy — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/stocks/news/bharat-electronics-shares-gain-3-as-motilal-raises-target-price-after-q2-elara-capital-upgrades-to-buy/articleshow/135524961.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 5.38] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 49.19, z20 3.38, zc 2.61, resid-z 1.36 [moved], 1d 3.49%, |z20|=3.38
- **Mechanism**: dyn_ohi ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Figma’s stock dips as investors worry that AI momentum is coming at a high price — MarketWatch Top, 2026-11-05. https://www.marketwatch.com/story/figmas-stock-falls-as-investors-worry-that-ai-momentum-is-coming-at-a-high-price-1aa2134d?mod=mw_rss_topstories
- Source: Figma’s stock falls as investors worry that AI momentum is coming at a high price — MarketWatch Top, 2026-11-04. https://www.marketwatch.com/story/figmas-stock-falls-as-investors-worry-that-ai-momentum-is-coming-at-a-high-price-1aa2134d?mod=mw_rss_topstories
- Source: Musk stocks lose $120 billion as Democrats’ Texas win rattles investors — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/musk-stocks-lose-120-billion-as-democrats-texas-win-rattles-investors/articleshow/135550872.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [RED 5.13] indices · 3 series ↑
- cac_40 [INDICES]: last 8194.94, z20 3.81, zc 2.78, resid-z 1.88 [unexplained], 1d 2.18%, |z20|=3.81
- dax [INDICES]: last 26478.84, z20 3.27, zc 2.60, resid-z 1.60 [unexplained], 1d 2.37%, |z20|=3.27; 1y-pct=99
- stoxx_50 [INDICES]: last 6272.85, z20 3.01, zc 2.32, resid-z 1.64 [unexplained], 1d 2.09%, |z20|=3.01
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.563 via dax, z 1.25, reacted); nifty_50 (rho 0.491 via cac_40, z 3.28, reacted); dyn_jiofin_bo (rho 0.487 via dax, z 2.11, reacted); nifty_fmcg (rho 0.468 via cac_40, z 2.55, reacted); dyn_muthootfin_ns (rho 0.461 via cac_40, z 1.87, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.673 vs dax, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.572 vs dax, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.567 vs dax, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.563, z 1.25); nifty_50 (rho 0.491, z 3.28); dyn_jiofin_bo (rho 0.487, z 2.11); nifty_fmcg (rho 0.468, z 2.55)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [AMBER 5.12] fx · 2 series ↑
- gbp_usd [FX]: last 1.35, z20 2.29, zc 1.13, resid-z 1.82 [unexplained], 1d 0.37%, |z20|=2.29
- eur_usd [FX]: last 1.13, z20 2.02, zc 1.34, resid-z 1.71 [unexplained], 1d 0.40%, |z20|=2.02
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.502 vs eur_usd, historically leads by 5d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.191 vs eur_usd, historically leads by 1d
- Source: Meta draws record orders for debut euro bond sale, Bloomberg News reports — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/meta-draws-record-orders-for-debut-euro-bond-sale-bloomberg-news-reports/articleshow/135543860.cms
- Source: Euro zone inflation hits 4% for first time in three years as interest rate hike looms — CNBC Economy, 2026-11-04. https://www.cnbc.com/2026/11/04/euro-zone-cpi-inflation-october-ecb-rate-hike.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.97] dyn_lth ↑
- dyn_lth [EQUITIES]: last 47.38, z20 2.97, zc 2.77, resid-z 0.84 [moved], 1d 6.32%, |z20|=2.97; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.456 via dyn_lth, z 1.87, reacted); dyn_jiofin_bo (rho 0.371 via dyn_lth, z 2.11, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.456, z 1.87); dyn_jiofin_bo (rho 0.371, z 2.11)
- Source: Democrats Win Texas Oil Regulator Seat for First Time Since 1990 — OilPrice, 2026-11-04. https://oilprice.com/Energy/Crude-Oil/Democrats-Win-Texas-Oil-Regulator-Seat-for-First-Time-Since-1990.html
- Source: Euro zone inflation hits 4% for first time in three years as interest rate hike looms — CNBC Economy, 2026-11-04. https://www.cnbc.com/2026/11/04/euro-zone-cpi-inflation-october-ecb-rate-hike.html
- Source: U.S. jobs market perks up, but it’s still not a great time to get hired — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/u-s-jobs-market-perks-up-but-its-still-not-a-great-time-to-get-hired-bc39f44f?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 4.94] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 24.33, z20 2.94, zc 3.39, resid-z 0.98 [moved], 1d 5.53%, |z20|=2.94
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.37 via dyn_hdb, z 3.28, reacted)
- **India receivers**: nifty_50 (rho 0.37, z 3.28)
- Source: HDFC Bank shares extends rally for 2nd day, hits ₹741 intraday high — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-extends-rally-for-second-day-hits-741-intraday-high/article71664326.ece
- Source: HDFC Bank share price gains 3% today: Here's why - Is the worst over after a 27% one-year fall? What experts say — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-gains-3-today-heres-why-is-the-worst-over-after-a-27-one-year-fall-what-experts-say-11793688821749.html
- Source: HDFC Bank shares surges 2.86%, lead Nifty 50 gainers — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-surges-286-lead-nifty-50-gainers/article71659565.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

## Watchlist (below surfacing floor)
dyn_atherenerg_ns ↑ (4.35), dyn_bajfinance_ns ↑ (4.17), dyn_jiofin_bo ↑ (4.11), dyn_tech ↑ (3.96), dyn_schd ↑ (3.7), comex_copper ↓ (3.57), dyn_rs ↑ (3.46), dyn_4417_t ↑ (3.4), asx_200 ↑ (3.03), dyn_techm_ns ↑ (2.69), rates · 2 series ↑ (2.58), dyn_sepn ↑ (2.56)

## India macro
- nifty_50: 23960.5996 (1d 0.63%, z20 3.28, flag red)
- nifty_midcap_100: 59514.3008 (1d 1.56%, z20 1.25, flag none)
- usd_inr: 94.5300 (1d -0.23%, z20 -1.00, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4838 (1d 0.93%, z20 -1.11, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · AMFI SIP / MF flows T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 92.0 — "Stock recommendations for 5 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.0 — "Stock recommendations for 5 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.0 — "Stock recommendations for 5 November from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 58.6 — "Indian bonds rally most since April as oil slides after US midterm verdict"
- OHI (Omega Healthcare Investors, In) score 50.4 — "Figma’s stock dips as investors worry that AI momentum is coming at a high price"
- BAC (Bank of America Corporation) score 41.4 — "How do Americans feel about the midterm results? It depends on how much money they make."
- TGT (Target Corporation) score 41.0 — "Stocks to buy in November: Axis Direct names Nuvama, BEML and Petronet, sees up to 27% ups"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.0 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- HDB (HDFC Bank Limited) score 39.6 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- TECH (Bio-Techne Corp) score 39.4 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- IDBI.NS (IDBI BANK LIMITED) score 36.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- COIN (Coinbase Global, Inc.) score 31.0 — "Global Market Today: Asian stocks rise as oil slides after US midterm elections"
- 301077.SZ (CHINASTARS) score 29.0 — "US EXTENDS NATIONAL EMERGENCY ORDERS RELATED TO CHINA, IRAN"
- CHKP (Check Point Software Technolog) score 27.3 — "SBI vs SBI Life vs SBI Cards: Which SBI Group stock emerged as the Q2 results 2026 winner?"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.1 — "Beyond Equity: Jiraaf’s Saurav Ghosh on how to customise your portfolio, and the importanc"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.5 — "As Vistra and other energy stocks slide, some analysts warn of an ‘excessive knee-jerk’ re"
- RS (Reliance, Inc.) score 22.7 — "How Jio is unlocking hidden value for Reliance shareholders"
- LTH (Life Time Group Holdings, Inc.) score 20.5 — "Democrats Win Texas Oil Regulator Seat for First Time Since 1990"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 18.7 — "Aptus Value Housing Finance Q2 profit rises 18% to Rs 267 cr"
- JIOFIN.BO (Jio Financial Services Limited) score 16.4 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have $500 in savings"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 15.7 — "US Midterm Election Results 2026 impact: What Trump's loss mean for Sensex, Nifty, gold, s"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.2 — "DOW JONES EXTENDS GAINS TO HIT TWO-MONTH HIGH; LAST UP 2.95%"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.5 — "Aptus Value Housing Finance Q2 profit rises 18% to Rs 267 cr"
- SCHD (Schwab US Dividend Equity ETF) score 12.5 — "Small-cap stock with 1:10 split, 1:2 bonus shares and dividend history jumps 4% after Q2 r"
- META (Meta) score 11.7 — "Meta draws record orders for debut euro bond sale, Bloomberg News reports"
- SEPN (Septerna, Inc.) score 10.5 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- DEMZ (Democratic Large Cap Core ETF) score 10.3 — "US HOUSE DEMOCRATIC LEADER JEFFRIES: HAVE NOT HEARD FROM TRUMP"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.6 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.6 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.0 — "Samvat 2083 stock picks! Adani Power, Coal India, 8 others to add in your portfolio this f"
- JEF (Jefferies Financial Group Inc.) score 7.6 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- VT (Vanguard Total World Stock Ind) score 7.0 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.4 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
- GS (Goldman Sachs Group, Inc. (The) score 6.0 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 3.7 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.3 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.6 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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