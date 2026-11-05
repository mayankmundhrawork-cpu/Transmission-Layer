# Transmission Layer — board brief · 2026-11-05 19:56Z

data as of **2026-11-05** · 97 series · 19 red / 30 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.773, 1d in regime; vol-pct 0.957, breadth-off 0.588, Markov P(high-vol) 1.0)
- [INVERTED] **safe_haven_gold** — corr20 -0.21, corr60 -0.27, contra nifty_50 corr20=0.34, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.16, corr60 0.12, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.09, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.89, last shift 2026-09-17. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.33, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.09, corr60 -0.11, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.32, corr60 0.29, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **15 of 89** scanned series survive multiplicity control (effective p ≤ 0.013893701577248674)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.597, β 0.4939, p 0.0); driver zc -2.13 → expected -1.413%. Type hit-rate 0.821 (n=1829).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.566, β 0.441, p 0.0); driver zc -3.48 → expected -1.568%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.565, β 0.4534, p 0.0); driver zc -3.27 → expected -1.537%. Type hit-rate 0.821 (n=1829).
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.563, β 0.3341, p 0.0); driver zc -3.54 → expected -1.442%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.553, β 0.339, p 0.0); driver zc -3.27 → expected -1.149%. Type hit-rate 0.821 (n=1829).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.54, β 0.6225, p 0.0); driver zc -3.29 → expected -3.203%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.534, β 0.8714, p 0.0); driver zc -3.27 → expected -2.954%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_demz → asx_200: leads 1d (ccf 0.534, β 0.408, p 0.0); driver zc -3.22 → expected -1.416%. Type hit-rate 0.821 (n=1829).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.529, β 0.8301, p 0.0); driver zc -3.48 → expected -2.951%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.523, β -0.3117, p 0.0); driver zc -3.27 → expected 1.057%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → asx_200: leads 1d (ccf -0.502, β -0.0455, p 0.0); driver zc 4.67 → expected -2.469%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_schd → asx_200: leads 1d (ccf 0.496, β 0.4335, p 0.0); driver zc -1.57 → expected -0.694%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.473, β 0.183, p 0.0); driver zc -2.68 → expected -1.093%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.466, β -0.0838, p 0.0); driver zc 4.67 → expected -4.546%. Type hit-rate 0.821 (n=1829).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.46, β 0.2742, p 0.0); driver zc -3.48 → expected -0.975%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.448, β -0.3945, p 0.0); driver zc -3.27 → expected 1.337%. Type hit-rate 0.821 (n=1829).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.447, β -0.2583, p 0.0); driver zc -3.48 → expected 0.918%. Type hit-rate 0.821 (n=1829).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.44, β 0.1913, p 0.0); driver zc -3.29 → expected -0.984%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_demz → aud_usd: leads 1d (ccf 0.437, β 0.2551, p 0.0); driver zc -3.22 → expected -0.885%. Type hit-rate 0.821 (n=1829).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.428, β -0.181, p 0.0); driver zc -3.29 → expected 0.931%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.428, β 0.0282, p 0.0); driver zc 4.67 → expected 1.53%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.425, β -0.0288, p 0.0); driver zc 4.67 → expected -1.565%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_demz → usd_mxn: leads 1d (ccf -0.413, β -0.2337, p 0.0); driver zc -3.22 → expected 0.811%. Type hit-rate 0.821 (n=1829).
- **SETUP** russell_2000 → aud_usd: leads 1d (ccf 0.388, β 0.1762, p 0.0); driver zc -3.54 → expected -0.761%. Type hit-rate 0.821 (n=1829).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.385, β 0.2459, p 4e-05); driver zc -2.13 → expected -0.704%. Type hit-rate 0.821 (n=1829).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.382, β -0.237, p 0.0); driver zc -2.13 → expected 0.678%. Type hit-rate 0.821 (n=1829).
- **SETUP** russell_2000 → usd_mxn: leads 1d (ccf -0.382, β -0.1683, p 0.0); driver zc -3.54 → expected 0.727%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.372, β -2.4487, p 0.0076); driver zc -3.27 → expected 8.302%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.35, β 0.5511, p 0.0); driver zc -3.27 → expected -1.868%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → india_vix: leads 1d (ccf 0.348, β 0.2295, p 0.01169); driver zc 4.67 → expected 12.451%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.319, β 0.1393, p 1e-05); driver zc -3.27 → expected -0.472%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.319, β -0.092, p 2e-05); driver zc -2.68 → expected 0.55%. Type hit-rate 0.821 (n=1829).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.315, β 0.486, p 0.00027); driver zc -3.48 → expected -1.728%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_gs → aud_usd: leads 1d (ccf 0.314, β 0.093, p 0.00108); driver zc -2.68 → expected -0.555%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.308, β 0.3755, p 0.0); driver zc -3.27 → expected -1.273%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → nifty_metal: leads 1d (ccf -0.305, β -0.0481, p 0.00049); driver zc 4.67 → expected -2.611%. Type hit-rate 0.821 (n=1829).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.302, β 0.087, p 0.0); driver zc -2.15 → expected -0.454%. Type hit-rate 0.821 (n=1829).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.292, β 0.325, p 0.00041); driver zc -3.54 → expected -1.403%. Type hit-rate 0.821 (n=1829).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.281, β 0.2424, p 0.0); driver zc -3.54 → expected -1.046%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.28, β 0.364, p 0.0); driver zc -3.27 → expected -1.234%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_demz → nifty_midcap_100: leads 1d (ccf 0.278, β 0.308, p 0.0); driver zc -3.22 → expected -1.069%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → dyn_jiofin_bo: leads 1d (ccf -0.277, β -0.0554, p 0.0); driver zc 4.67 → expected -3.004%. Type hit-rate 0.821 (n=1829).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.276, β 0.33, p 0.0); driver zc -3.48 → expected -1.173%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → nifty_50: leads 1d (ccf -0.268, β -0.0243, p 3e-05); driver zc 4.67 → expected -1.318%. Type hit-rate 0.821 (n=1829).
- **SETUP** dyn_demz → nifty_50: leads 1d (ccf 0.267, β 0.2192, p 4e-05); driver zc -3.22 → expected -0.761%. Type hit-rate 0.821 (n=1829).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.266, β -0.0601, p 0.0); driver zc -2.15 → expected 0.314%. Type hit-rate 0.821 (n=1829).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.265, β -0.0324, p 0.00015); driver zc 4.67 → expected -1.755%. Type hit-rate 0.821 (n=1829).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.261, β 0.2235, p 1e-05); driver zc -3.29 → expected -1.15%. Type hit-rate 0.821 (n=1829).
- **SETUP** russell_2000 → nifty_50: leads 1d (ccf 0.258, β 0.1652, p 6e-05); driver zc -3.54 → expected -0.713%. Type hit-rate 0.821 (n=1829).
- **SETUP** dow_jones → nifty_50: leads 1d (ccf 0.254, β 0.2311, p 0.00034); driver zc -2.13 → expected -0.661%. Type hit-rate 0.821 (n=1829).
- **SETUP** eth_usd → usd_mxn: leads 1d (ccf -0.25, β -0.0372, p 0.0); driver zc -1.65 → expected 0.252%. Type hit-rate 0.821 (n=1829).
- Track record · residual_reversion: hit-rate **0.508** (n=1122) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=1829) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.51] cross-asset · 6 series ↓
- vix [INDICES]: last 25.62, z20 4.36, zc 4.67, resid-z n/a [moved], 1d 54.24%, 1-session move +54.24% ≥ 15.0%; |z20|=4.36; 1y-pct=95
- sp500 [INDICES]: last 7415.33, z20 -3.77, zc -3.48, resid-z 0.64 [priced], 1d -3.55%, |z20|=3.77
- dyn_vt [EQUITIES]: last 152.46, z20 -3.59, zc -3.27, resid-z -1.23 [moved], 1d -3.39%, |z20|=3.59
- nasdaq_100 [INDICES]: last 26973.93, z20 -3.04, zc -3.29, resid-z -0.13 [priced], 1d -5.15%, |z20|=3.04
- dyn_demz [EQUITIES]: last 46.87, z20 -2.56, zc -3.22, resid-z 0.20 [priced], 1d -3.47%, |z20|=2.56
- russell_2000 [INDICES]: last 2733.61, z20 -1.58, zc -3.54, resid-z -0.90 [priced], 1d -4.32%, |z20|=1.58
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.766 vs vix
- Source: Bloom Energy’s stock is one of the S&P 500’s biggest losers amid fears of data-center delays — MarketWatch Top, 2026-11-05. https://www.marketwatch.com/story/bloom-energys-stock-is-one-of-the-s-p-500s-biggest-losers-amid-fears-of-data-center-delays-a44c96bb?mod=mw_rss_topstories
- Source: US stock market crash: Chip stocks extend sell-off, AMD, Arm, Qualcomm and Sandisk plunge up to 17%; Nasdaq down 6% — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/us-stock-market-crash-chip-stocks-extend-sell-off-amd-arm-qualcomm-and-sandisk-plunge-up-to-17-nasdaq-down-6-11793900308301.html
- Source: Nasdaq tumbles over 3% as tech stocks extend selloff after Democrats sweep midterms; Tesla plunges 9%, chipmakers slide — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-falls-at-open-after-midterms-fueled-surge-as-chip-data-center-stocks-fall/articleshow/135577537.cms
- Historical analogues: 2026-05-22 (d=0.49), 2025-10-23 (d=0.7), 2025-05-05 (d=0.8)

### [RED 9.63] cross-asset · 7 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1070.00, z20 5.30, zc 4.34, resid-z 3.05 [unexplained], 1d 7.65%, |z20|=5.30
- nifty_50 [INDICES]: last 24536.60, z20 3.89, zc 2.69, resid-z 3.36 [unexplained], 1d 2.40%, |z20|=3.89
- dyn_indusindbk_bo [EQUITIES]: last 911.00, z20 3.56, zc 2.48, resid-z 3.39 [unexplained], 1d 5.67%, |z20|=3.56
- dyn_jiofin_bo [EQUITIES]: last 229.50, z20 3.35, zc 1.93, resid-z 2.03 [unexplained], 1d 3.29%, |z20|=3.35
- nifty_metal [INDICES]: last 12592.85, z20 2.85, zc 0.58, resid-z -0.59 [quiet], 1d 0.86%, |z20|=2.85
- nifty_fmcg [INDICES]: last 46472.90, z20 2.46, zc 0.32, resid-z -2.87 [unexplained], 1d 0.45%, |z20|=2.46
- nifty_midcap_100 [INDICES]: last 60615.85, z20 2.32, zc 1.59, resid-z 2.85 [unexplained], 1d 1.85%, |z20|=2.32
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.23).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.681 via nifty_metal, z 1.5, reacted); dyn_muthootfin_ns (rho 0.641 via nifty_midcap_100, z 3.11, reacted); dyn_indianb_ns (rho 0.601 via nifty_midcap_100, z 3.02, reacted); midcap_largecap_ratio (rho 0.548 via nifty_midcap_100, z -1.24, reacted); dyn_havells_ns (rho 0.536 via nifty_midcap_100, z 0.33, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.566 vs dyn_bajfinance_ns
- Watch next: dyn_havells_ns (co-move) — not yet - watch; rho 0.536 vs nifty_midcap_100
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.51 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.681, z 1.5); dyn_muthootfin_ns (rho 0.641, z 3.11); dyn_indianb_ns (rho 0.601, z 3.02); midcap_largecap_ratio (rho 0.548, z -1.24)
- Source: Nifty posts best single-day gain since April, crosses 24,500 for first time in three months — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/nifty-posts-best-single-day-gain-since-april-crosses-24500-for-first-time-in-three-months/article71669761.ece
- Source: Terrific Thursday for stock market! Nifty jumps 576 pts, Sensex 2,009 pts after US election results; bank, IT shares fly — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/terrific-thursday-for-stock-market-nifty-jumps-576-pts-sensex-2-009-pts-after-us-election-results-bank-it-shares-fly-11793879260120.html
- Source: Sensex today | Stock Market Highlights: Sensex surges 2,009 pts, Nifty tops 24,500; Financials and autos lead rally — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-5-november-2026/article71665358.ece
- Historical analogues: 2025-07-21 (d=1.23), 2025-07-14 (d=1.37), 2025-12-23 (d=1.54)

### [RED 7.75] commodities · 2 series ↓
- brent [COMMODITIES]: last 98.31, z20 -1.92, zc 1.00, resid-z -3.36 [unexplained], 1d 3.90%, 1-session move +3.90% ≥ 1.5%; |z20|=1.92
- wti [COMMODITIES]: last 90.63, z20 -1.66, zc 0.77, resid-z -2.95 [unexplained], 1d 2.85%, 1-session move +2.85% ≥ 1.5%; |z20|=1.66
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.454 via wti, z 3.11, reacted)
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.605 vs brent
- **India receivers**: dyn_muthootfin_ns (rho -0.454, z 3.11)
- Source: Oil Prices Rebound Sharply After Brutal Midweek Rout — OilPrice, 2026-11-05. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Rebound-Sharply-After-Brutal-Midweek-Rout.html
- Source: US yields fall in choppy session as oil rises and equities sink — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/us-stocks/news/us-yields-fall-in-choppy-session-as-oil-rises-and-equities-sink/articleshow/135585328.cms
- Source: Guyana’s Oil Boom Could Ease the Global Supply Crunch — OilPrice, 2026-11-05. https://oilprice.com/Energy/Energy-General/Guyanas-Oil-Boom-Could-Ease-the-Global-Supply-Crunch.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 5.61] indices · 2 series ↓
- taiwan_weighted [INDICES]: last 41541.62, z20 -2.78, zc -1.61, resid-z 0.60 [moved], 1d -3.28%, |z20|=2.78
- nikkei_225 [INDICES]: last 61089.31, z20 -1.58, zc -1.08, resid-z 0.62 [quiet], 1d -1.77%, |z20|=1.58
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.464 via nikkei_225, z -0.4, quiet); nifty_50 (rho -0.428 via taiwan_weighted, z 3.89, reacted); midcap_largecap_ratio (rho 0.406 via taiwan_weighted, z -1.24, reacted)
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.511 vs taiwan_weighted
- **India receivers**: dyn_idbi_ns (rho 0.464, z -0.4); nifty_50 (rho -0.428, z 3.89); midcap_largecap_ratio (rho 0.406, z -1.24)
- Source: Stock market outlook today, 4 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-4-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11793752972780.html
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 5.11] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 2839.00, z20 3.11, zc 1.28, resid-z 2.16 [unexplained], 1d 4.77%, |z20|=3.11
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.641 via dyn_muthootfin_ns, z 2.32, reacted); dyn_jiofin_bo (rho 0.616 via dyn_muthootfin_ns, z 3.35, reacted); nifty_metal (rho 0.574 via dyn_muthootfin_ns, z 2.85, reacted); nifty_50 (rho 0.527 via dyn_muthootfin_ns, z 3.89, reacted); nifty_fmcg (rho 0.479 via dyn_muthootfin_ns, z 2.46, reacted)
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.51 vs dyn_muthootfin_ns
- **India receivers**: nifty_midcap_100 (rho 0.641, z 2.32); dyn_jiofin_bo (rho 0.616, z 3.35); nifty_metal (rho 0.574, z 2.85); nifty_50 (rho 0.527, z 3.89)
- Source: Muthoot Microfin posts record disbursements, PAT jumps 3.6x in Q2 FY27 — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/muthoot-microfin-posts-record-disbursements-pat-jumps-36x-in-q2-fy27/article71670335.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 5.09] comex_copper ↓
- comex_copper [COMMODITIES]: last 6.26, z20 -3.09, zc -1.13, resid-z 1.53 [unexplained], 1d -2.28%, |z20|=3.09
- **Mechanism**: comex_copper ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.544 vs comex_copper
- Source: China’s Copper Squeeze Deepens as Buyers Scramble for Spot Metal — Mint Markets, 2026-11-05. https://www.livemint.com/market/chinas-copper-squeeze-deepens-as-buyers-scramble-for-spot-metal-11793847941597.html
- Source: Copper Falls as Traders Assess AI Trade, US-Iran Diplomacy Hopes — Mint Markets, 2026-11-03. https://www.livemint.com/market/copper-falls-as-traders-assess-ai-trade-us-iran-diplomacy-hopes-11793742834384.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

### [AMBER 4.94] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 138.68, z20 -2.11, zc -1.80, resid-z 1.14 [moved], 1d -8.46%, |z20|=2.11; 1y-pct=0
- btc_usd [CRYPTO]: last 76211.03, z20 -2.06, zc -2.15, resid-z -0.83 [priced], 1d -5.22%, |z20|=2.06
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.23).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.541 vs dyn_coin
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.512 vs btc_usd
- Source: Guyana’s Oil Boom Could Ease the Global Supply Crunch — OilPrice, 2026-11-05. https://oilprice.com/Energy/Energy-General/Guyanas-Oil-Boom-Could-Ease-the-Global-Supply-Crunch.html
- Source: Signature Global clocks Rs 67 cr profit in Q2 vs loss yr ago, revenue rises over 2-fold — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/digital-real-estate/realty-news/signature-global-clocks-rs-67-cr-profit-in-q2-vs-loss-yr-ago-revenue-rises-over-2-fold/articleshow/135577590.cms
- Source: Bullish momentum to sustain for Indian stocks on global rally — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/bullish-momentum-to-sustain-for-indian-stocks-on-global-rally/article71668413.ece
- Historical analogues: 2026-05-22 (d=0.23), 2025-08-19 (d=0.26), 2026-04-02 (d=0.41)

### [RED 4.7] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 24.59, z20 2.70, zc 0.55, resid-z 0.98 [quiet], 1d 1.07%, |z20|=2.70
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.355 via dyn_hdb, z 3.89, reacted)
- **India receivers**: nifty_50 (rho 0.355, z 3.89)
- Source: HDFC Bank climbs for third straight session, up 12% from last week’s Low — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-climbs-for-third-straight-session-up-12-from-last-weeks-low/article71668872.ece
- Source: HDFC Bank shares witness strong buying, rise 7% in 1 month. Can new CEO, improving fundamentals drive next leg of rally? — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/hdfc-bank-shares-witness-strong-buying-rise-7-in-1-month-can-new-ceo-improving-fundamentals-drive-next-leg-of-rally-11793861115989.html
- Source: HDFC Bank Share Price Live Updates: HDFC Bank's Performance Snapshot — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/hdfc-bank-stock-price-live-updates-05-nov-2026/liveblog/135557239.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

## Watchlist (below surfacing floor)
dyn_lth ↑ (4.46), asx_200 ↑ (4.13), equities · 2 series ↑ (3.85), indices · 2 series ↑ (3.79), dyn_atherenerg_ns ↑ (3.55), dyn_4417_t ↑ (3.4), dyn_tech ↑ (3.32), dyn_schd ↑ (2.97), dyn_techm_ns ↑ (2.92), shanghai_comp ↓ (2.33), hang_seng ↑ (2.3), dyn_rs ↓ (2.18)

## India macro
- nifty_50: 24536.5996 (1d 2.40%, z20 3.89, flag red)
- nifty_midcap_100: 60615.8516 (1d 1.85%, z20 2.32, flag amber)
- usd_inr: 94.4650 (1d -0.30%, z20 -1.09, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4704 (1d -0.54%, z20 -1.24, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · AMFI SIP / MF flows T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 100.9 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- INOXINDIA.NS (INOX INDIA LIMITED) score 100.1 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 99.3 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- INDIANB.NS (INDIAN BANK) score 68.0 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- OHI (Omega Healthcare Investors, In) score 50.8 — "Sebi revises currency derivative norms for domestic investors, FPIs; allows to trade up to"
- HDB (HDFC Bank Limited) score 48.3 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- BAC (Bank of America Corporation) score 47.9 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.9 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.7 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- TECH (Bio-Techne Corp) score 44.7 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 43.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- TGT (Target Corporation) score 36.3 — "Maharashtra state discom targets February 2027 IPO, aims to raise over  ₹10,000 crore"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.0 — "India to Require State Utilities to Add Energy Storage Capacity"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.5 — "Rising oil prices cap India bond rally; traders cash in gains"
- COIN (Coinbase Global, Inc.) score 28.9 — "Signature Global clocks Rs 67 cr profit in Q2 vs loss yr ago, revenue rises over 2-fold"
- 301077.SZ (CHINASTARS) score 28.0 — "Iran Opens Strait of Hormuz to China and India as U.S. Blockade Continues"
- CHKP (Check Point Software Technolog) score 27.7 — "PFC dividend: Up 200% in 5 yrs, Maharatna PSU's shares rally 5% in 3 days - Check dividend"
- LTH (Life Time Group Holdings, Inc.) score 23.0 — "Nifty posts best single-day gain since April, crosses 24,500 for first time in three month"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.3 — "Bajaj Finserv Share Price Highlights: Bajaj Finserv Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 20.3 — "Federal Reserve Board announces termination of enforcement action with Allegiant United Ho"
- RS (Reliance, Inc.) score 20.0 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 17.8 — "Gold ETFs fall 4% in a month ahead of Dhanteras 2026: Is this a buying opportunity? Expert"
- SCHD (Schwab US Dividend Equity ETF) score 15.3 — "PFC dividend: Up 200% in 5 yrs, Maharatna PSU's shares rally 5% in 3 days - Check dividend"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.3 — "Muthoot Microfin posts record disbursements, PAT jumps 3.6x in Q2 FY27"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.7 — "Ex-Politburo member Ma Xingrui’s corruption charges extend to end of last century"
- DEMZ (Democratic Large Cap Core ETF) score 11.5 — "AI, data-center stocks slip as Democratic sweep clouds expansion plans"
- META (Meta) score 10.8 — "China’s Copper Squeeze Deepens as Buyers Scramble for Spot Metal"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.9 — "Tata Steel Share Price Live Updates: Tata Steel's Price Update and Volatility Insights"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.9 — "Tata Steel Share Price Live Updates: Tata Steel's Price Update and Volatility Insights"
- SEPN (Septerna, Inc.) score 8.8 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.6 — "Adani Ports & Special Economic Zone Share Price Live Updates: Intimation Of Interaction Wi"
- JEF (Jefferies Financial Group Inc.) score 6.4 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.3 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have just $500 in sa"
- VT (Vanguard Total World Stock Ind) score 5.9 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 4.9 — "Infosys Share Price Live Updates: Infosys Price Update and Trends"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.1 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.5 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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