# Transmission Layer — board brief · 2026-11-05 00:53Z

data as of **2026-11-05** · 97 series · 14 red / 30 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 1d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.176)
- [INVERTED] **safe_haven_gold** — corr20 -0.68, corr60 -0.54, contra nifty_50 corr20=0.27, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.13, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.05, corr60 0.06, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.76, last shift 2026-09-17. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.32, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.09, corr60 -0.11, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.63, corr60 0.41, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.003389620038554586)
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.542, β 0.8954, p 0.0); driver zc 1.94 → expected 1.518%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.541, β 0.8808, p 0.0); driver zc 1.94 → expected 1.493%. Type hit-rate 0.83 (n=1848).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.535, β 0.838, p 0.0); driver zc 1.75 → expected 1.327%. Type hit-rate 0.83 (n=1848).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.521, β 0.8383, p 0.0); driver zc 1.75 → expected 1.327%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_demz → nikkei_225: leads 1d (ccf 0.507, β 0.7854, p 0.0); driver zc 2.33 → expected 1.658%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_demz → taiwan_weighted: leads 1d (ccf 0.494, β 0.7817, p 0.0); driver zc 2.33 → expected 1.651%. Type hit-rate 0.83 (n=1848).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.475, β -0.0852, p 0.0); driver zc -2.47 → expected 1.742%. Type hit-rate 0.83 (n=1848).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.456, β 0.7589, p 0.0); driver zc 3.94 → expected 2.301%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.449, β -0.3969, p 0.0); driver zc 1.94 → expected -0.673%. Type hit-rate 0.83 (n=1848).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.435, β -0.0806, p 0.0); driver zc -2.47 → expected 1.648%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.422, β 0.3236, p 0.0); driver zc 1.81 → expected 1.159%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.414, β 0.3231, p 0.0); driver zc 1.81 → expected 1.158%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.408, β 1.0125, p 0.0); driver zc 1.94 → expected 1.716%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.362, β -0.0919, p 0.0); driver zc 3.39 → expected -0.508%. Type hit-rate 0.83 (n=1848).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.351, β 0.8424, p 0.0); driver zc 1.75 → expected 1.333%. Type hit-rate 0.83 (n=1848).
- **SETUP** dyn_demz → kospi: leads 1d (ccf 0.339, β 0.8003, p 0.0); driver zc 2.33 → expected 1.69%. Type hit-rate 0.83 (n=1848).
- **SETUP** vix → kospi: leads 1d (ccf -0.335, β -0.0921, p 0.0); driver zc -2.47 → expected 1.884%. Type hit-rate 0.83 (n=1848).
- Track record · residual_reversion: hit-rate **0.509** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=1848) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.54] cross-asset · 5 series ↑
- dyn_jef [EQUITIES]: last 51.18, z20 3.61, zc 1.71, resid-z 0.48 [priced], 1d 5.40%, |z20|=3.61
- dow_jones [INDICES]: last 53357.03, z20 2.88, zc 3.94, resid-z 3.95 [unexplained], 1d 3.03%, |z20|=2.88
- dyn_gs [EQUITIES]: last 928.20, z20 2.44, zc 1.81, resid-z -0.28 [priced], 1d 3.58%, |z20|=2.44
- russell_2000 [INDICES]: last 2856.96, z20 2.08, zc 1.36, resid-z -0.56 [quiet], 1d 1.58%, |z20|=2.08
- vix [INDICES]: last 16.57, z20 -0.53, zc -2.47, resid-z n/a [moved], 1d -20.45%, 1-session move -20.45% ≥ 15.0%
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.54).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.452 via dyn_jef, z 0.13, quiet)
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.683 vs dow_jones, historically leads by 1d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.653 vs dyn_jef, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.561 vs dyn_jef, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.52 vs dyn_jef, historically leads by 5d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.626 vs dow_jones
- **India receivers**: dyn_indusindbk_bo (rho 0.452, z 0.13)
- Source: S&P 500 HAS RISEN AFTER EVERY US MIDTERM ELECTION SINCE 1942 The S&P 500 has delivered positive returns in the 12 months following every US midterm election since 1942, according to Dow Jones Market Data. 🔸 Average one-year gain: Approximately 13% 🔸 1954 midterms: +33% 🔸 1994 midterms: +27% 🔸 1986 m — DeItaone, 2026-11-04. https://t.me/walter_bloomberg/38050
- Source: DOW JONES EXTENDS GAINS TO HIT TWO-MONTH HIGH; LAST UP 2.95% — DeItaone, 2026-11-04. https://t.me/walter_bloomberg/38047
- Source: Wall Street cheers US midterm results as Dow Jones jumps 1300 points; Amazon, Apple, Microsoft among top gainers — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/wall-street-cheers-us-midterm-results-as-dow-jones-jumps-1300-points-amazon-apple-microsoft-among-top-gainers-11793807617877.html
- Historical analogues: 2026-05-22 (d=0.54), 2026-05-14 (d=0.6), 2025-05-19 (d=0.78)

### [RED 6.12] indices · 2 series ↑
- nifty_50 [INDICES]: last 23960.60, z20 3.28, zc 0.69, resid-z 0.72 [quiet], 1d 0.63%, |z20|=3.28
- nifty_fmcg [INDICES]: last 46266.95, z20 2.55, zc 1.05, resid-z 1.47 [quiet], 1d 1.51%, |z20|=2.55
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.703 via nifty_50, z 1.25, reacted); dyn_bajfinance_ns (rho 0.627 via nifty_50, z 2.17, reacted); dyn_jiofin_bo (rho 0.609 via nifty_50, z 2.11, reacted); dyn_indusindbk_bo (rho 0.562 via nifty_50, z 0.13, quiet); nifty_metal (rho 0.552 via nifty_50, z 2.2, reacted)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.505 vs nifty_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.705 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.562 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.703, z 1.25); dyn_bajfinance_ns (rho 0.627, z 2.17); dyn_jiofin_bo (rho 0.609, z 2.11); dyn_indusindbk_bo (rho 0.562, z 0.13)
- Source: US optimism fuels Nifty’s strongest 5-day rally in seven months — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/us-optimism-fuels-niftys-strongest-5-day-rally-in-seven-months/article71665638.ece
- Source: US Midterm Election Results Impact Decoded: Can Sensex, Nifty hit new peak? Gold, silver rates rebound with Trump loss — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-impact-decoded-can-sensex-nifty-hit-new-peak-gold-silver-rates-rebound-with-trump-loss-11793788769424.html
- Source: Stock Market Rally: Bulls to stay? Nifty, Sensex gain 5.5% in 5 sessions; Can the momentum sustain? Key levels to watch — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-rally-bulls-to-stay-nifty-sensex-gain-5-5-in-5-sessions-can-the-momentum-sustain-key-levels-to-watch-11793787625537.html
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

### [RED 5.4] commodities · 2 series ↓
- brent [COMMODITIES]: last 94.70, z20 -2.57, zc 0.00, resid-z -2.93 [unexplained], 1d 0.00%, |z20|=2.57
- wti [COMMODITIES]: last 88.09, z20 -2.22, zc -0.01, resid-z -2.60 [unexplained], 1d -0.03%, |z20|=2.22
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.524 via wti, z 1.87, reacted); nifty_midcap_100 (rho -0.516 via wti, z 1.25, reacted)
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.726 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.67 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.661 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.651 vs brent
- **India receivers**: dyn_muthootfin_ns (rho -0.524, z 1.87); nifty_midcap_100 (rho -0.516, z 1.25)
- Source: US midterm elections: Crude cools, but Iran war risks keeps markets guessing — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/us-midterm-elections-crude-cools-but-iran-war-risks-keeps-markets-guessing/articleshow/135555256.cms
- Source: Oil Crashes 9% as Trump and Vance Blame Iran War for Midterm Rout — OilPrice, 2026-11-04. https://oilprice.com/Latest-Energy-News/World-News/Oil-Crashes-9-as-Trump-and-Vance-Blame-Iran-War-for-Midterm-Rout.html
- Source: US CRUDE FUTURES FALL BY MORE THAN $5/BBL, BRENT CRUDE FUTURES DOWN BY MORE THAN $7/BBL — DeItaone, 2026-11-04. https://t.me/walter_bloomberg/38043
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 5.38] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 49.19, z20 3.38, zc 2.61, resid-z 1.36 [moved], 1d 3.49%, |z20|=3.38
- **Mechanism**: dyn_ohi ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Figma’s stock falls as investors worry that AI momentum is coming at a high price — MarketWatch Top, 2026-11-04. https://www.marketwatch.com/story/figmas-stock-falls-as-investors-worry-that-ai-momentum-is-coming-at-a-high-price-1aa2134d?mod=mw_rss_topstories
- Source: Musk stocks lose $120 billion as Democrats’ Texas win rattles investors — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/musk-stocks-lose-120-billion-as-democrats-texas-win-rattles-investors/articleshow/135550872.cms
- Source: 4 market-moving issues investors should watch now that the midterms are over — MarketWatch Top, 2026-11-04. https://www.marketwatch.com/story/4-market-moving-issues-investors-should-watch-now-that-the-midterms-are-over-9a77b3de?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 5.15] fx · 2 series ↑
- gbp_usd [FX]: last 1.35, z20 2.32, zc 1.18, resid-z 1.79 [unexplained], 1d 0.39%, |z20|=2.32
- eur_usd [FX]: last 1.12, z20 1.89, zc 1.23, resid-z 1.70 [unexplained], 1d 0.37%, |z20|=1.89
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.501 vs eur_usd, historically leads by 5d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.203 vs eur_usd, historically leads by 1d
- Source: Meta draws record orders for debut euro bond sale, Bloomberg News reports — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/meta-draws-record-orders-for-debut-euro-bond-sale-bloomberg-news-reports/articleshow/135543860.cms
- Source: Euro zone inflation hits 4% for first time in three years as interest rate hike looms — CNBC Economy, 2026-11-04. https://www.cnbc.com/2026/11/04/euro-zone-cpi-inflation-october-ecb-rate-hike.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.13] indices · 3 series ↑
- cac_40 [INDICES]: last 8194.94, z20 3.81, zc 2.78, resid-z 1.96 [unexplained], 1d 2.18%, |z20|=3.81
- dax [INDICES]: last 26478.84, z20 3.27, zc 2.60, resid-z 1.75 [unexplained], 1d 2.37%, |z20|=3.27; 1y-pct=99
- stoxx_50 [INDICES]: last 6272.85, z20 3.01, zc 2.32, resid-z 1.62 [unexplained], 1d 2.09%, |z20|=3.01
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.563 via dax, z 1.25, reacted); nifty_50 (rho 0.491 via cac_40, z 3.28, reacted); dyn_jiofin_bo (rho 0.487 via dax, z 2.11, reacted); nifty_fmcg (rho 0.468 via cac_40, z 2.55, reacted); dyn_muthootfin_ns (rho 0.461 via cac_40, z 1.87, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.673 vs dax, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.572 vs dax, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.567 vs dax, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.563, z 1.25); nifty_50 (rho 0.491, z 3.28); dyn_jiofin_bo (rho 0.487, z 2.11); nifty_fmcg (rho 0.468, z 2.55)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

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

## Watchlist (below surfacing floor)
dyn_hdb ↑ (4.94), dxy ↓ (4.85), dyn_atherenerg_ns ↑ (4.35), dyn_bajfinance_ns ↑ (4.17), dyn_jiofin_bo ↑ (4.11), dyn_tech ↑ (3.96), dyn_schd ↑ (3.7), dyn_rs ↑ (3.46), dyn_4417_t ↑ (3.4), dyn_techm_ns ↑ (2.69), rates · 2 series ↑ (2.58), dyn_sepn ↑ (2.56)

## India macro
- nifty_50: 23960.5996 (1d 0.63%, z20 3.28, flag red)
- nifty_midcap_100: 59514.3008 (1d 1.56%, z20 1.25, flag none)
- usd_inr: 94.7484 (1d 0.02%, z20 -0.77, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4838 (1d 0.93%, z20 -1.11, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · AMFI SIP / MF flows T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 92.6 — "Stock recommendations for 5 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.6 — "Stock recommendations for 5 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.6 — "Stock recommendations for 5 November from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 59.0 — "Indian bonds rally most since April as oil slides after US midterm verdict"
- OHI (Omega Healthcare Investors, In) score 49.7 — "Musk stocks lose $120 billion as Democrats’ Texas win rattles investors"
- BAC (Bank of America Corporation) score 41.7 — "How do Americans feel about the midterm results? It depends on how much money they make."
- TGT (Target Corporation) score 41.3 — "Stocks to buy in November: Axis Direct names Nuvama, BEML and Petronet, sees up to 27% ups"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.2 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- HDB (HDFC Bank Limited) score 39.9 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.7 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- TECH (Bio-Techne Corp) score 39.7 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.4 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- IDBI.NS (IDBI BANK LIMITED) score 36.4 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.4 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- COIN (Coinbase Global, Inc.) score 30.2 — "Iran War and AI Boom Drive Global Gas Supply Crunch"
- 301077.SZ (CHINASTARS) score 29.1 — "US EXTENDS NATIONAL EMERGENCY ORDERS RELATED TO CHINA, IRAN"
- CHKP (Check Point Software Technolog) score 27.5 — "SBI vs SBI Life vs SBI Cards: Which SBI Group stock emerged as the Q2 results 2026 winner?"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.3 — "Beyond Equity: Jiraaf’s Saurav Ghosh on how to customise your portfolio, and the importanc"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.6 — "As Vistra and other energy stocks slide, some analysts warn of an ‘excessive knee-jerk’ re"
- RS (Reliance, Inc.) score 22.9 — "How Jio is unlocking hidden value for Reliance shareholders"
- LTH (Life Time Group Holdings, Inc.) score 20.6 — "Democrats Win Texas Oil Regulator Seat for First Time Since 1990"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 18.8 — "Aptus Value Housing Finance Q2 profit rises 18% to Rs 267 cr"
- JIOFIN.BO (Jio Financial Services Limited) score 16.5 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have $500 in savings"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.8 — "490% return in 5 yrs: BEL shares up 9% in week - How much upside do experts see in defence"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.3 — "DOW JONES EXTENDS GAINS TO HIT TWO-MONTH HIGH; LAST UP 2.95%"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.6 — "Aptus Value Housing Finance Q2 profit rises 18% to Rs 267 cr"
- SCHD (Schwab US Dividend Equity ETF) score 12.6 — "Small-cap stock with 1:10 split, 1:2 bonus shares and dividend history jumps 4% after Q2 r"
- META (Meta) score 11.8 — "Meta draws record orders for debut euro bond sale, Bloomberg News reports"
- SEPN (Septerna, Inc.) score 10.6 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- DEMZ (Democratic Large Cap Core ETF) score 10.3 — "US HOUSE DEMOCRATIC LEADER JEFFRIES: HAVE NOT HEARD FROM TRUMP"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.7 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.7 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "Samvat 2083 stock picks! Adani Power, Coal India, 8 others to add in your portfolio this f"
- JEF (Jefferies Financial Group Inc.) score 7.7 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- VT (Vanguard Total World Stock Ind) score 7.1 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.5 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
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