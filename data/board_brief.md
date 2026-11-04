# Transmission Layer — board brief · 2026-11-04 19:43Z

data as of **2026-11-04** · 97 series · 15 red / 29 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.565, 1d in regime; vol-pct 0.659, breadth-off 0.471, Markov P(high-vol) 0.288)
- [INVERTED] **safe_haven_gold** — corr20 -0.66, corr60 -0.53, contra nifty_50 corr20=0.27, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.86, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.13, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.0, corr60 0.07, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.77, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.35, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.13, corr60 -0.11, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.64, corr60 0.41, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **7 of 89** scanned series survive multiplicity control (effective p ≤ 0.007145201904799503)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.588, β 0.4864, p 0.0); driver zc 3.98 → expected 1.487%. Type hit-rate 0.825 (n=1893).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.564, β 0.4355, p 0.0); driver zc 1.97 → expected 0.779%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.562, β 0.4472, p 0.0); driver zc 2.03 → expected 0.796%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.558, β 0.3433, p 0.0); driver zc 2.03 → expected 0.611%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.543, β 0.8887, p 0.0); driver zc 2.03 → expected 1.581%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.542, β 0.8933, p 0.0); driver zc 2.03 → expected 1.59%. Type hit-rate 0.825 (n=1893).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.537, β 0.8447, p 0.0); driver zc 1.97 → expected 1.512%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_demz → asx_200: leads 1d (ccf 0.53, β 0.4016, p 0.0); driver zc 2.3 → expected 0.84%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.524, β -0.3106, p 0.0); driver zc 2.03 → expected -0.553%. Type hit-rate 0.825 (n=1893).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.521, β 0.8365, p 0.0); driver zc 1.97 → expected 1.497%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_demz → nikkei_225: leads 1d (ccf 0.51, β 0.7943, p 0.0); driver zc 2.3 → expected 1.661%. Type hit-rate 0.825 (n=1893).
- **SETUP** vix → asx_200: leads 1d (ccf -0.495, β -0.0446, p 0.0); driver zc -2.35 → expected 0.872%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_demz → taiwan_weighted: leads 1d (ccf 0.494, β 0.7805, p 0.0); driver zc 2.3 → expected 1.632%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_schd → asx_200: leads 1d (ccf 0.491, β 0.4255, p 0.0); driver zc 1.68 → expected 0.622%. Type hit-rate 0.825 (n=1893).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.478, β -0.0864, p 0.0); driver zc -2.35 → expected 1.688%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.47, β 0.1798, p 0.0); driver zc 1.78 → expected 0.633%. Type hit-rate 0.825 (n=1893).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.466, β 0.2781, p 0.0); driver zc 1.97 → expected 0.498%. Type hit-rate 0.825 (n=1893).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.461, β 0.777, p 0.0); driver zc 3.98 → expected 2.375%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.452, β 0.1287, p 0.0); driver zc 1.78 → expected 0.718%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.451, β -0.3979, p 0.0); driver zc 2.03 → expected -0.708%. Type hit-rate 0.825 (n=1893).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.448, β -0.258, p 0.0); driver zc 1.97 → expected -0.462%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_demz → aud_usd: leads 1d (ccf 0.444, β 0.2599, p 0.0); driver zc 2.3 → expected 0.543%. Type hit-rate 0.825 (n=1893).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.435, β -0.0805, p 0.0); driver zc -2.35 → expected 1.573%. Type hit-rate 0.825 (n=1893).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.432, β -0.0295, p 0.0); driver zc -2.35 → expected 0.576%. Type hit-rate 0.825 (n=1893).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.43, β 0.0283, p 0.0); driver zc -2.35 → expected -0.553%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.426, β 0.3272, p 0.0); driver zc 1.78 → expected 1.152%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.414, β 0.3221, p 0.0); driver zc 1.78 → expected 1.134%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_demz → usd_mxn: leads 1d (ccf -0.414, β -0.234, p 0.0); driver zc 2.3 → expected -0.489%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.412, β 1.0228, p 0.0); driver zc 2.03 → expected 1.82%. Type hit-rate 0.825 (n=1893).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.394, β 0.2543, p 2e-05); driver zc 3.98 → expected 0.777%. Type hit-rate 0.825 (n=1893).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.381, β -0.2368, p 0.0); driver zc 3.98 → expected -0.724%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.362, β -0.0916, p 0.0); driver zc 3.58 → expected -0.533%. Type hit-rate 0.825 (n=1893).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.354, β 0.8502, p 0.0); driver zc 1.97 → expected 1.521%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_demz → kospi: leads 1d (ccf 0.344, β 0.8143, p 0.0); driver zc 2.3 → expected 1.702%. Type hit-rate 0.825 (n=1893).
- **SETUP** vix → kospi: leads 1d (ccf -0.342, β -0.0944, p 0.0); driver zc -2.35 → expected 1.844%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_gs → kospi: leads 1d (ccf 0.326, β 0.389, p 0.0); driver zc 1.78 → expected 1.37%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_gs → aud_usd: leads 1d (ccf 0.319, β 0.0948, p 0.0008); driver zc 1.78 → expected 0.334%. Type hit-rate 0.825 (n=1893).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.316, β -0.0909, p 3e-05); driver zc 1.78 → expected -0.32%. Type hit-rate 0.825 (n=1893).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.267, β -0.0601, p 0.0); driver zc 1.74 → expected -0.215%. Type hit-rate 0.825 (n=1893).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.261, β 0.2651, p 0.02682); driver zc 2.34 → expected 0.494%. Type hit-rate 0.825 (n=1893).
- **SETUP** eth_usd → usd_mxn: leads 1d (ccf -0.251, β -0.0372, p 0.0); driver zc 1.71 → expected -0.237%. Type hit-rate 0.825 (n=1893).
- Track record · residual_reversion: hit-rate **0.509** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.825** (n=1893) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.28] cross-asset · 7 series ↑
- dyn_jef [EQUITIES]: last 51.27, z20 3.67, zc 1.78, resid-z -3.25 [unexplained], 1d 5.58%, |z20|=3.67
- brent [COMMODITIES]: last 94.67, z20 -2.94, zc -4.32, resid-z -2.69 [unexplained], 1d -8.62%, 1-session move -8.62% ≥ 1.5%; |z20|=2.94
- dow_jones [INDICES]: last 53369.66, z20 2.91, zc 3.98, resid-z 3.83 [unexplained], 1d 3.06%, |z20|=2.91
- dyn_gs [EQUITIES]: last 927.65, z20 2.40, zc 1.78, resid-z -0.21 [priced], 1d 3.52%, |z20|=2.40
- wti [COMMODITIES]: last 88.16, z20 -2.21, zc -3.53, resid-z -2.31 [unexplained], 1d -8.25%, 1-session move -8.25% ≥ 1.5%; |z20|=2.21
- russell_2000 [INDICES]: last 2855.49, z20 2.03, zc 1.32, resid-z -0.71 [quiet], 1d 1.53%, |z20|=2.03
- vix [INDICES]: last 16.76, z20 -0.43, zc -2.35, resid-z n/a [moved], 1d -19.54%, 1-session move -19.54% ≥ 15.0%
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.519 via wti, z 1.87, reacted); nifty_midcap_100 (rho -0.511 via wti, z 1.25, reacted); dyn_indusindbk_bo (rho 0.449 via dyn_jef, z 0.13, quiet)
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.642 vs dyn_jef, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.561 vs dyn_jef, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.529 vs dyn_jef, historically leads by 5d
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.717 vs brent
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.579 vs vix
- **India receivers**: dyn_muthootfin_ns (rho -0.519, z 1.87); nifty_midcap_100 (rho -0.511, z 1.25); dyn_indusindbk_bo (rho 0.449, z 0.13)
- Source: Oil Crashes 9% as Trump and Vance Blame Iran War for Midterm Rout — OilPrice, 2026-11-04. https://oilprice.com/Latest-Energy-News/World-News/Oil-Crashes-9-as-Trump-and-Vance-Blame-Iran-War-for-Midterm-Rout.html
- Source: Wall Street cheers US midterm results as Dow Jones jumps 1300 points; Amazon, Apple, Microsoft among top gainers — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/wall-street-cheers-us-midterm-results-as-dow-jones-jumps-1300-points-amazon-apple-microsoft-among-top-gainers-11793807617877.html
- Source: US Oil Inventories Fall Further As Demand Holds — OilPrice, 2026-11-04. https://oilprice.com/Energy/Crude-Oil/US-Oil-Inventories-Fall-Further-As-Demand-Holds.html
- Historical analogues: 2026-05-22 (d=0.46), 2025-10-28 (d=0.87), 2025-08-14 (d=0.87)

### [RED 6.12] indices · 2 series ↑
- nifty_50 [INDICES]: last 23960.60, z20 3.28, zc 0.69, resid-z 0.65 [quiet], 1d 0.63%, |z20|=3.28
- nifty_fmcg [INDICES]: last 46266.95, z20 2.55, zc 1.05, resid-z 1.48 [quiet], 1d 1.51%, |z20|=2.55
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.703 via nifty_50, z 1.25, reacted); dyn_bajfinance_ns (rho 0.63 via nifty_50, z 2.17, reacted); dyn_jiofin_bo (rho 0.612 via nifty_50, z 2.11, reacted); dyn_indusindbk_bo (rho 0.56 via nifty_50, z 0.13, quiet); nifty_metal (rho 0.551 via nifty_50, z 2.2, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.703 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.56 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.703, z 1.25); dyn_bajfinance_ns (rho 0.63, z 2.17); dyn_jiofin_bo (rho 0.612, z 2.11); dyn_indusindbk_bo (rho 0.56, z 0.13)
- Source: US optimism fuels Nifty’s strongest 5-day rally in seven months — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/us-optimism-fuels-niftys-strongest-5-day-rally-in-seven-months/article71665638.ece
- Source: US Midterm Election Results Impact Decoded: Can Sensex, Nifty hit new peak? Gold, silver rates rebound with Trump loss — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-impact-decoded-can-sensex-nifty-hit-new-peak-gold-silver-rates-rebound-with-trump-loss-11793788769424.html
- Source: Stock Market Rally: Bulls to stay? Nifty, Sensex gain 5.5% in 5 sessions; Can the momentum sustain? Key levels to watch — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-rally-bulls-to-stay-nifty-sensex-gain-5-5-in-5-sessions-can-the-momentum-sustain-key-levels-to-watch-11793787625537.html
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [AMBER 5.33] cross-asset · 3 series ↓
- ust_2y [RATES]: last 4.59, z20 -2.01, zc -0.84, resid-z -0.81 [quiet], 1d 0.66%, |z20|=2.01
- ust_10y [RATES]: last 4.91, z20 -1.83, zc -0.75, resid-z -1.16 [quiet], 1d -0.61%, |z20|=1.83
- dyn_schd [EQUITIES]: last 36.07, z20 1.56, zc 1.68, resid-z -0.68 [priced], 1d 1.46%, 1y-pct=100
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: kospi (inverse) — not yet - watch; rho -0.516 vs dyn_schd
- Source: These 12 stocks are good bets to beat the 10-year Treasury over the next decade — MarketWatch Top, 2026-11-04. https://www.marketwatch.com/story/these-12-stocks-are-good-bets-to-beat-the-10-year-treasury-over-the-next-decade-cc4f308b?mod=mw_rss_topstories
- Source: How Indian Metals & Ferro Alloys shares performed post Q2; profit up 51%,  ₹5 dividend; what drove performance? — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/how-indian-metals-ferro-alloys-shares-performed-post-q2-results-profit-up-51-rs-5-dividend-what-drove-performa-11793789113686.html
- Source: Eurozone bond yields steady as investors await inflation data; US Treasury yields ease after midterm elections — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/eurozone-bond-yields-steady-as-investors-await-inflation-data-us-treasury-yields-ease-after-midterm-elections/articleshow/135535574.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.46), 2025-05-19 (d=1.07)

### [RED 5.26] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 162.25, z20 3.26, zc 2.66, resid-z -0.01 [moved], 1d 5.08%, |z20|=3.26; 1y-pct=95
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Stocks to buy in November: Axis Direct names Nuvama, BEML and Petronet, sees up to 27% upside; target, rationale — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/stocks-to-buy-in-november-axis-direct-names-nuvama-beml-and-petronet-sees-up-to-27-upside-target-rationale-11793790461951.html
- Source: Clean Max shares: Power stock jumps 42% in YTD; will this rally continue after Q2 results 2026? Expert views, target — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/clean-max-shares-power-stock-jumps-42-in-ytd-will-this-rally-continue-after-q2-results-2026-expert-views-target-11793772700847.html
- Source: Bharat Electronics shares gain 3% as Motilal raises target price after Q2; Elara Capital upgrades to Buy — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/stocks/news/bharat-electronics-shares-gain-3-as-motilal-raises-target-price-after-q2-elara-capital-upgrades-to-buy/articleshow/135524961.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 5.13] indices · 3 series ↑
- cac_40 [INDICES]: last 8194.94, z20 3.81, zc 2.78, resid-z 1.90 [unexplained], 1d 2.18%, |z20|=3.81
- dax [INDICES]: last 26478.84, z20 3.27, zc 2.60, resid-z 1.62 [unexplained], 1d 2.37%, |z20|=3.27; 1y-pct=99
- stoxx_50 [INDICES]: last 6272.85, z20 3.01, zc 2.32, resid-z 1.40 [moved], 1d 2.09%, |z20|=3.01
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.563 via dax, z 1.25, reacted); nifty_50 (rho 0.489 via cac_40, z 3.28, reacted); nifty_fmcg (rho 0.466 via cac_40, z 2.55, reacted); dyn_jiofin_bo (rho 0.463 via cac_40, z 2.11, reacted); dyn_muthootfin_ns (rho 0.46 via cac_40, z 1.87, reacted)
- Watch next: sp500 (co-move) — not yet - watch; rho 0.579 vs dax, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.565 vs dax, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.501 vs cac_40, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.563, z 1.25); nifty_50 (rho 0.489, z 3.28); nifty_fmcg (rho 0.466, z 2.55); dyn_jiofin_bo (rho 0.463, z 2.11)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [RED 5.04] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 24.39, z20 3.04, zc 3.58, resid-z 0.88 [moved], 1d 5.82%, |z20|=3.04
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.37 via dyn_hdb, z 3.28, reacted)
- **India receivers**: nifty_50 (rho 0.37, z 3.28)
- Source: HDFC Bank shares extends rally for 2nd day, hits ₹741 intraday high — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-extends-rally-for-second-day-hits-741-intraday-high/article71664326.ece
- Source: HDFC Bank share price gains 3% today: Here's why - Is the worst over after a 27% one-year fall? What experts say — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-gains-3-today-heres-why-is-the-worst-over-after-a-27-one-year-fall-what-experts-say-11793688821749.html
- Source: HDFC Bank shares surges 2.86%, lead Nifty 50 gainers — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-surges-286-lead-nifty-50-gainers/article71659565.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.99] dyn_lth ↑
- dyn_lth [EQUITIES]: last 47.42, z20 2.99, zc 2.81, resid-z -0.91 [moved], 1d 6.39%, |z20|=2.99; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.463 via dyn_lth, z 1.87, reacted); dyn_jiofin_bo (rho 0.388 via dyn_lth, z 2.11, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.463, z 1.87); dyn_jiofin_bo (rho 0.388, z 2.11)
- Source: Democrats Win Texas Oil Regulator Seat for First Time Since 1990 — OilPrice, 2026-11-04. https://oilprice.com/Energy/Crude-Oil/Democrats-Win-Texas-Oil-Regulator-Seat-for-First-Time-Since-1990.html
- Source: Euro zone inflation hits 4% for first time in three years as interest rate hike looms — CNBC Economy, 2026-11-04. https://www.cnbc.com/2026/11/04/euro-zone-cpi-inflation-october-ecb-rate-hike.html
- Source: U.S. jobs market perks up, but it’s still not a great time to get hired — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/u-s-jobs-market-perks-up-but-its-still-not-a-great-time-to-get-hired-bc39f44f?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 4.93] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 48.72, z20 2.93, zc 1.86, resid-z -0.78 [moved], 1d 2.49%, |z20|=2.93
- **Mechanism**: dyn_ohi ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: 4 market-moving issues investors should watch now that the midterms are over — MarketWatch Top, 2026-11-04. https://www.marketwatch.com/story/4-market-moving-issues-investors-should-watch-now-that-the-midterms-are-over-9a77b3de?mod=mw_rss_topstories
- Source: SEBI relaxes KYC rules for NRIs, OCIs: Can overseas investors now onboard digitally from abroad? Decoded — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/sebi-relaxes-kyc-rules-for-nris-ocis-can-overseas-investors-now-onboard-digitally-from-abroad-decoded-11793803371003.html
- Source: Gold ETFs attract ₹3,300 crore in Oct as investors go on a buying spree ahead of Diwali — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/gold-etfs-attract-3300-crore-in-oct-as-investors-go-on-a-buying-spree-ahead-of-diwali/article71665451.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

## Watchlist (below surfacing floor)
dxy ↓ (4.7), dyn_tech ↑ (4.7), dyn_atherenerg_ns ↑ (4.35), dyn_bajfinance_ns ↑ (4.17), dyn_jiofin_bo ↑ (4.11), comex_copper ↓ (3.55), dyn_4417_t ↑ (3.54), dyn_rs ↑ (3.24), dyn_techm_ns ↑ (2.69), rates · 2 series ↑ (2.58), shanghai_comp ↓ (2.48), taiwan_weighted ↓ (2.46)

## India macro
- nifty_50: 23960.5996 (1d 0.63%, z20 3.28, flag red)
- nifty_midcap_100: 59514.3008 (1d 1.56%, z20 1.25, flag none)
- usd_inr: 94.6300 (1d -0.10%, z20 -0.93, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4838 (1d 0.93%, z20 -1.11, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · AMFI SIP / MF flows T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 95.2 — "Come January, RIL to launch ‘Jamnagar of the East Coast’ with Andhra Coal Project"
- INOXINDIA.NS (INOX INDIA LIMITED) score 94.2 — "How Saregama India shares turned music to the ears for investors after 13% price jump - Ho"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 93.1 — "How Saregama India shares turned music to the ears for investors after 13% price jump - Ho"
- INDIANB.NS (INDIAN BANK) score 62.0 — "Indian bonds rally most since April as oil slides after US midterm verdict"
- OHI (Omega Healthcare Investors, In) score 50.1 — "SBI’s conservative FY27 guidance leaves investors wanting more"
- TGT (Target Corporation) score 43.4 — "Stocks to buy in November: Axis Direct names Nuvama, BEML and Petronet, sees up to 27% ups"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.3 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- BAC (Bank of America Corporation) score 42.8 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- HDB (HDFC Bank Limited) score 41.9 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.7 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- TECH (Bio-Techne Corp) score 41.7 — "Sunday PropTech acquires 89-room hotel in Kolkata, marks entry into city"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.3 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- IDBI.NS (IDBI BANK LIMITED) score 38.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- COIN (Coinbase Global, Inc.) score 30.7 — "India’s VC funding declines 3% even as global investments surge 137%: GlobalData"
- 301077.SZ (CHINASTARS) score 29.6 — "China's Rail Line Into Central Asia Is Set for 2031"
- CHKP (Check Point Software Technolog) score 28.9 — "SBI vs SBI Life vs SBI Cards: Which SBI Group stock emerged as the Q2 results 2026 winner?"
- BOND (PIMCO Active Bond Exchange-Tra) score 28.6 — "Beyond Equity: Jiraaf’s Saurav Ghosh on how to customise your portfolio, and the importanc"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.9 — "Ather Energy among 15 stocks that hit 52-week highs and rallied up to 30% in a month"
- RS (Reliance, Inc.) score 24.0 — "How Jio is unlocking hidden value for Reliance shareholders"
- LTH (Life Time Group Holdings, Inc.) score 21.7 — "Democrats Win Texas Oil Regulator Seat for First Time Since 1990"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.7 — "Aptus Value Housing Finance Q2 profit rises 18% to Rs 267 cr"
- JIOFIN.BO (Jio Financial Services Limited) score 17.3 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have $500 in savings"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 15.6 — "490% return in 5 yrs: BEL shares up 9% in week - How much upside do experts see in defence"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.0 — "NASDAQ E-MINI FUTURES EXTEND LOSS, LAST DOWN 1.8%; S&P 500 E-MINI FUTURES DOWN 0.8%"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.3 — "Aptus Value Housing Finance Q2 profit rises 18% to Rs 267 cr"
- SCHD (Schwab US Dividend Equity ETF) score 13.2 — "Small-cap stock with 1:10 split, 1:2 bonus shares and dividend history jumps 4% after Q2 r"
- META (Meta) score 12.4 — "Meta draws record orders for debut euro bond sale, Bloomberg News reports"
- SEPN (Septerna, Inc.) score 11.2 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.2 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.2 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.5 — "Samvat 2083 stock picks! Adani Power, Coal India, 8 others to add in your portfolio this f"
- JEF (Jefferies Financial Group Inc.) score 8.1 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- DEMZ (Democratic Large Cap Core ETF) score 7.7 — "Democratic victory in midterm elections adds a new twist to stock markets' Iran war, AI, a"
- VT (Vanguard Total World Stock Ind) score 7.4 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.8 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
- GS (Goldman Sachs Group, Inc. (The) score 6.3 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 3.9 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.4 — "Broker’s call: PB Fintech (Buy)"
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