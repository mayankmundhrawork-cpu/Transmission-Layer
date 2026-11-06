# Transmission Layer — board brief · 2026-11-06 00:58Z

data as of **2026-11-06** · 97 series · 17 red / 34 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 2d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 1.0)
- [INVERTED] **safe_haven_gold** — corr20 -0.2, corr60 -0.25, contra nifty_50 corr20=0.31, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.16, corr60 0.12, last shift 2026-09-16. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 0.04, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.9, last shift 2026-09-18. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.34, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.12, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.34, corr60 0.3, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **34 of 89** scanned series survive multiplicity control (effective p ≤ 0.025747442877204207)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.594, β 0.491, p 0.0); driver zc -2.6 → expected -1.686%. Type hit-rate 0.836 (n=1890).
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.562, β 0.3359, p 0.0); driver zc -3.69 → expected -1.502%. Type hit-rate 0.836 (n=1890).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.56, β 0.4296, p 0.0); driver zc -4.23 → expected -1.855%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.56, β 0.4409, p 0.0); driver zc -3.95 → expected -1.801%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_demz → asx_200: leads 1d (ccf 0.532, β 0.4011, p 0.0); driver zc -3.22 → expected -1.392%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.528, β -0.3104, p 0.0); driver zc -3.95 → expected 1.268%. Type hit-rate 0.836 (n=1890).
- **SETUP** vix → asx_200: leads 1d (ccf -0.481, β -0.041, p 0.0); driver zc 5.96 → expected -2.848%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.478, β 0.191, p 0.0); driver zc -3.06 → expected -1.23%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.448, β -0.3946, p 0.0); driver zc -3.95 → expected 1.612%. Type hit-rate 0.836 (n=1890).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.429, β 0.0268, p 0.0); driver zc 5.96 → expected 1.864%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.373, β -2.4622, p 0.00745); driver zc -3.95 → expected 10.056%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.36, β 0.5644, p 0.0); driver zc -3.95 → expected -2.305%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.328, β 0.1398, p 1e-05); driver zc -3.95 → expected -0.571%. Type hit-rate 0.836 (n=1890).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.324, β 0.3682, p 1e-05); driver zc -3.69 → expected -1.646%. Type hit-rate 0.836 (n=1890).
- **SETUP** vix → nifty_metal: leads 1d (ccf -0.32, β -0.0506, p 0.00023); driver zc 5.96 → expected -3.514%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.31, β 0.379, p 0.0); driver zc -3.95 → expected -1.548%. Type hit-rate 0.836 (n=1890).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.293, β 0.2596, p 0.0); driver zc -3.69 → expected -1.161%. Type hit-rate 0.836 (n=1890).
- **SETUP** russell_2000 → nifty_50: leads 1d (ccf 0.282, β 0.1849, p 0.0); driver zc -3.69 → expected -0.827%. Type hit-rate 0.836 (n=1890).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.281, β 0.3394, p 0.0); driver zc -4.23 → expected -1.465%. Type hit-rate 0.836 (n=1890).
- **SETUP** dyn_demz → nifty_midcap_100: leads 1d (ccf 0.28, β 0.3113, p 0.0); driver zc -3.22 → expected -1.08%. Type hit-rate 0.836 (n=1890).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.269, β -0.0331, p 0.00013); driver zc 5.96 → expected -2.299%. Type hit-rate 0.836 (n=1890).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.265, β 0.2278, p 1e-05); driver zc -4.02 → expected -1.433%. Type hit-rate 0.836 (n=1890).
- Track record · residual_reversion: hit-rate **0.508** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.836** (n=1890) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 13.38] cross-asset · 9 series ↓
- vix [INDICES]: last 28.15, z20 5.75, zc 5.96, resid-z n/a [moved], 1d 69.48%, 1-session move +69.48% ≥ 15.0%; |z20|=5.75; 1y-pct=98
- sp500 [INDICES]: last 7356.73, z20 -4.54, zc -4.23, resid-z -0.47 [priced], 1d -4.32%, |z20|=4.54
- dyn_vt [EQUITIES]: last 151.37, z20 -4.37, zc -3.95, resid-z -0.03 [priced], 1d -4.08%, |z20|=4.37
- nasdaq_100 [INDICES]: last 26647.86, z20 -3.44, zc -4.02, resid-z -3.34 [unexplained], 1d -6.29%, |z20|=3.44
- dyn_demz [EQUITIES]: last 46.87, z20 -2.56, zc -3.22, resid-z 1.51 [unexplained], 1d -3.47%, |z20|=2.56
- dyn_coin [EQUITIES]: last 136.84, z20 -2.26, zc -2.06, resid-z -0.20 [priced], 1d -9.68%, |z20|=2.26; 1y-pct=0
- btc_usd [CRYPTO]: last 76178.39, z20 -1.81, zc -0.02, resid-z -0.50 [quiet], 1d -0.04%, |z20|=1.81
- russell_2000 [INDICES]: last 2729.20, z20 -1.70, zc -3.69, resid-z 0.25 [priced], 1d -4.47%, |z20|=1.70
- eth_usd [CRYPTO]: last 2240.47, z20 -1.50, zc -0.18, resid-z 0.47 [quiet], 1d -0.77%, |z20|=1.50
- **Mechanism**: cross-asset · 9 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.54).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.534 vs dyn_coin
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.507 vs dyn_coin
- Source: Worst US stock rout since 2020 leaves virtually nowhere to hide as Nasdaq plunges 6.4%, Dow sheds 1,833 points — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/worst-us-stock-rout-since-2020-leaves-virtually-nowhere-to-hide-as-nasdaq-plunges-64-dow-sheds-1833-points/article71671756.ece
- Source: Wall Street fear gauge soars as retail traders bolt amid market rout — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/wall-street-fear-gauge-soars-as-retail-traders-bolt-amid-market-rout/article71671752.ece
- Source: Is this ‘the big one’ for the stock market? Wall Street sounds off as tech plunges. — MarketWatch Top, 2026-11-05. https://www.marketwatch.com/story/is-this-the-big-one-for-the-stock-market-wall-street-sounds-off-as-tech-plunges-185df529?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.54), 2025-10-23 (d=0.69), 2025-12-29 (d=1.0)

### [RED 9.63] cross-asset · 7 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1070.00, z20 5.30, zc 4.34, resid-z 3.26 [unexplained], 1d 7.65%, |z20|=5.30
- nifty_50 [INDICES]: last 24536.60, z20 3.89, zc 2.69, resid-z 3.41 [unexplained], 1d 2.40%, |z20|=3.89
- dyn_indusindbk_bo [EQUITIES]: last 911.00, z20 3.56, zc 2.49, resid-z 3.81 [unexplained], 1d 5.67%, |z20|=3.56
- dyn_jiofin_bo [EQUITIES]: last 229.50, z20 3.35, zc 1.93, resid-z 2.53 [unexplained], 1d 3.29%, |z20|=3.35
- nifty_metal [INDICES]: last 12592.85, z20 2.85, zc 0.58, resid-z -0.37 [quiet], 1d 0.86%, |z20|=2.85
- nifty_fmcg [INDICES]: last 46472.90, z20 2.46, zc 0.32, resid-z -2.96 [unexplained], 1d 0.45%, |z20|=2.46
- nifty_midcap_100 [INDICES]: last 60615.85, z20 2.32, zc 1.59, resid-z 3.69 [unexplained], 1d 1.85%, |z20|=2.32
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.23).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.681 via nifty_metal, z 1.5, reacted); dyn_muthootfin_ns (rho 0.645 via nifty_midcap_100, z 3.11, reacted); dyn_indianb_ns (rho 0.606 via nifty_midcap_100, z 3.02, reacted); midcap_largecap_ratio (rho 0.551 via nifty_midcap_100, z -1.24, reacted); dyn_havells_ns (rho 0.539 via nifty_midcap_100, z 0.33, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.561 vs dyn_bajfinance_ns
- Watch next: dyn_havells_ns (co-move) — not yet - watch; rho 0.539 vs nifty_midcap_100
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.503 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.681, z 1.5); dyn_muthootfin_ns (rho 0.645, z 3.11); dyn_indianb_ns (rho 0.606, z 3.02); midcap_largecap_ratio (rho 0.551, z -1.24)
- Source: Nifty posts best single-day gain since April, crosses 24,500 for first time in three months — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/nifty-posts-best-single-day-gain-since-april-crosses-24500-for-first-time-in-three-months/article71669761.ece
- Source: Terrific Thursday for stock market! Nifty jumps 576 pts, Sensex 2,009 pts after US election results; bank, IT shares fly — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/terrific-thursday-for-stock-market-nifty-jumps-576-pts-sensex-2-009-pts-after-us-election-results-bank-it-shares-fly-11793879260120.html
- Source: Sensex today | Stock Market Highlights: Sensex surges 2,009 pts, Nifty tops 24,500; Financials and autos lead rally — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-5-november-2026/article71665358.ece
- Historical analogues: 2025-07-21 (d=1.23), 2025-07-14 (d=1.37), 2025-12-23 (d=1.54)

### [RED 6.18] indices · 3 series ↓
- nikkei_225 [INDICES]: last 57654.11, z20 -2.86, zc -3.36, resid-z 0.92 [moved], 1d -5.62%, |z20|=2.86
- taiwan_weighted [INDICES]: last 41541.62, z20 -2.78, zc -1.61, resid-z 1.18 [moved], 1d -3.28%, |z20|=2.78
- kospi [INDICES]: last 5092.28, z20 -2.28, zc -1.18, resid-z 0.53 [quiet], 1d -4.66%, |z20|=2.28
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.481 via kospi, z 1.1, reacted); midcap_largecap_ratio (rho 0.464 via kospi, z -1.24, reacted); nifty_50 (rho -0.441 via taiwan_weighted, z 3.89, reacted); dyn_idbi_ns (rho 0.41 via nikkei_225, z -0.4, quiet); dyn_techm_ns (rho -0.363 via kospi, z 0.92, quiet)
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.509 vs taiwan_weighted
- **India receivers**: nifty_it (rho -0.481, z 1.1); midcap_largecap_ratio (rho 0.464, z -1.24); nifty_50 (rho -0.441, z 3.89); dyn_idbi_ns (rho 0.41, z -0.4)
- Source: Stock market outlook today, 4 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-4-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11793752972780.html

### [RED 5.11] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 2839.00, z20 3.11, zc 1.27, resid-z 2.49 [unexplained], 1d 4.77%, |z20|=3.11
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.645 via dyn_muthootfin_ns, z 2.32, reacted); dyn_jiofin_bo (rho 0.612 via dyn_muthootfin_ns, z 3.35, reacted); nifty_metal (rho 0.585 via dyn_muthootfin_ns, z 2.85, reacted); nifty_50 (rho 0.521 via dyn_muthootfin_ns, z 3.89, reacted); nifty_fmcg (rho 0.471 via dyn_muthootfin_ns, z 2.46, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.645, z 2.32); dyn_jiofin_bo (rho 0.612, z 3.35); nifty_metal (rho 0.585, z 2.85); nifty_50 (rho 0.521, z 3.89)
- Source: Muthoot Microfin posts record disbursements, PAT jumps 3.6x in Q2 FY27 — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/muthoot-microfin-posts-record-disbursements-pat-jumps-36x-in-q2-fy27/article71670335.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [AMBER 5.06] cross-asset · 3 series ↓
- ust_2y [RATES]: last 4.58, z20 -1.75, zc -0.51, resid-z -0.66 [quiet], 1d -0.65%, |z20|=1.75
- ust_10y [RATES]: last 4.90, z20 -1.63, zc -0.93, resid-z -1.10 [quiet], 1d -1.01%, |z20|=1.63
- dyn_schd [EQUITIES]: last 35.41, z20 0.75, zc -2.16, resid-z 2.43 [unexplained], 1d -2.21%, 1y-pct=98
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.843 vs ust_2y
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.014 vs ust_2y, historically leads by 1d
- Source: ConocoPhillips Doubles Profit to $4 Billion, Raises Dividend — OilPrice, 2026-11-05. https://oilprice.com/Latest-Energy-News/World-News/ConocoPhillips-Doubles-Profit-to-4-Billion-Raises-Dividend.html
- Source: Dividend stocks: Coal India, TCS, HUDCO, HCL Tech, GAIL among top 10 dividend paying stocks - Check yield, annual return — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/dividend-stocks-coal-india-tcs-hudco-hcl-tech-gail-among-top-10-dividend-paying-stocks-check-yield-annual-return-11793892901046.html
- Source: PSU dividend jackpot! ONGC vs NTPC vs CONCOR vs Petronet: Who offers highest payout? Record date, technical targets — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/psu-dividend-jackpot-ongc-vs-ntpc-vs-concor-vs-petronet-who-offers-highest-payout-record-date-technical-targets-11793880794114.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.46), 2025-05-19 (d=1.07)

### [RED 4.83] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 24.69, z20 2.83, zc 0.76, resid-z 2.55 [unexplained], 1d 1.48%, |z20|=2.83
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.367 via dyn_hdb, z 3.89, reacted)
- **India receivers**: nifty_50 (rho 0.367, z 3.89)
- Source: HDFC Bank climbs for third straight session, up 12% from last week’s Low — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-climbs-for-third-straight-session-up-12-from-last-weeks-low/article71668872.ece
- Source: HDFC Bank shares witness strong buying, rise 7% in 1 month. Can new CEO, improving fundamentals drive next leg of rally? — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/hdfc-bank-shares-witness-strong-buying-rise-7-in-1-month-can-new-ceo-improving-fundamentals-drive-next-leg-of-rally-11793861115989.html
- Source: HDFC Bank Share Price Live Updates: HDFC Bank's Performance Snapshot — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/hdfc-bank-stock-price-live-updates-05-nov-2026/liveblog/135557239.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.55] dyn_lth ↑
- dyn_lth [EQUITIES]: last 47.76, z20 2.55, zc 0.22, resid-z 2.95 [unexplained], 1d 0.77%, |z20|=2.55; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.462 via dyn_lth, z 3.11, reacted); dyn_jiofin_bo (rho 0.36 via dyn_lth, z 3.35, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.462, z 3.11); dyn_jiofin_bo (rho 0.36, z 3.35)
- Source: This pancreatic cancer treatment is on track for ‘one of the best drug launches of all time’ — MarketWatch Top, 2026-11-05. https://www.marketwatch.com/story/this-pancreatic-cancer-treatment-is-on-track-for-one-of-the-best-drug-launches-of-all-time-37bf86ce?mod=mw_rss_topstories
- Source: Titan shines in Q2 Results 2026; Net profit doubles to  ₹2,393 crore, aided by one-time gain; jewellery business up 24% — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/titan-shines-in-q2-results-2026-net-profit-doubles-to-rs-2-393-crore-aided-by-one-time-gain-jewellery-business-up-24-11793880484831.html
- Source: Nifty posts best single-day gain since April, crosses 24,500 for first time in three months — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/nifty-posts-best-single-day-gain-since-april-crosses-24500-for-first-time-in-three-months/article71669761.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [AMBER 4.49] comex_copper ↓
- comex_copper [COMMODITIES]: last 6.25, z20 -2.49, zc 0.00, resid-z 2.23 [unexplained], 1d 0.01%, |z20|=2.49
- **Mechanism**: comex_copper ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.585 vs comex_copper
- Source: China’s Copper Squeeze Deepens as Buyers Scramble for Metal — Mint Markets, 2026-11-05. https://www.livemint.com/market/chinas-copper-squeeze-deepens-as-buyers-scramble-for-metal-11793921664348.html
- Source: China’s Copper Squeeze Deepens as Buyers Scramble for Spot Metal — Mint Markets, 2026-11-05. https://www.livemint.com/market/chinas-copper-squeeze-deepens-as-buyers-scramble-for-spot-metal-11793847941597.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

## Watchlist (below surfacing floor)
commodities · 2 series ↓ (4.48), equities · 2 series ↑ (3.85), indices · 2 series ↑ (3.79), dyn_atherenerg_ns ↑ (3.55), dyn_4417_t ↑ (3.27), dyn_techm_ns ↑ (2.92), dyn_tech ↑ (2.91), asx_200 ↑ (2.37), shanghai_comp ↓ (2.33), hang_seng ↑ (2.3), aud_usd ↓ (1.98), soybeans ↓ (1.97)

## India macro
- nifty_50: 24536.5996 (1d 2.40%, z20 3.89, flag red)
- nifty_midcap_100: 60615.8516 (1d 1.85%, z20 2.32, flag amber)
- usd_inr: 94.5154 (1d -0.25%, z20 -1.02, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4704 (1d -0.54%, z20 -1.24, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · AMFI SIP / MF flows T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 98.1 — "India's Renewables Have Saved $100 Billion in Fuel Imports, IEA Says"
- INOXINDIA.NS (INOX INDIA LIMITED) score 97.4 — "India's Renewables Have Saved $100 Billion in Fuel Imports, IEA Says"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 96.6 — "India's Renewables Have Saved $100 Billion in Fuel Imports, IEA Says"
- INDIANB.NS (INDIAN BANK) score 64.8 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- OHI (Omega Healthcare Investors, In) score 52.4 — "ANTHROPIC IPO ODDS PLUNGE AS TECH SELLOFF DEEPENS Anthropic's chances of going public in 2"
- TECHM.NS (TECH MAHINDRA LIMITED) score 50.7 — "BITCOIN PLUNGES BELOW $76,000 AS TECH SELLOFF SPARKS CRYPTO ROUT Bitcoin fell as much as 5"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.6 — "BITCOIN PLUNGES BELOW $76,000 AS TECH SELLOFF SPARKS CRYPTO ROUT Bitcoin fell as much as 5"
- TECH (Bio-Techne Corp) score 48.6 — "BITCOIN PLUNGES BELOW $76,000 AS TECH SELLOFF SPARKS CRYPTO ROUT Bitcoin fell as much as 5"
- BAC (Bank of America Corporation) score 46.6 — "IRAN'S SUPREME LEADER DECLARES US POWER IN IRREVERSIBLE DECLINE Iran's Supreme Leader clai"
- HDB (HDFC Bank Limited) score 46.0 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 41.4 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.4 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- TGT (Target Corporation) score 36.6 — "ANTHROPIC IPO ODDS PLUNGE AS TECH SELLOFF DEEPENS Anthropic's chances of going public in 2"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.5 — "Asia Hopes U.S. Midterm Results Will Ease Energy Crisis"
- COIN (Coinbase Global, Inc.) score 28.6 — "IRAN'S SUPREME LEADER DECLARES US POWER IN IRREVERSIBLE DECLINE Iran's Supreme Leader clai"
- BOND (PIMCO Active Bond Exchange-Tra) score 28.1 — "Rising oil prices cap India bond rally; traders cash in gains"
- 301077.SZ (CHINASTARS) score 27.7 — "China’s Copper Squeeze Deepens as Buyers Scramble for Metal"
- CHKP (Check Point Software Technolog) score 26.4 — "PFC dividend: Up 200% in 5 yrs, Maharatna PSU's shares rally 5% in 3 days - Check dividend"
- LTH (Life Time Group Holdings, Inc.) score 22.9 — "IRAN REVIEWS CONCRETE NUCLEAR DEAL PROPOSALS IN POTENTIAL DIPLOMATIC BREAKTHROUGH Iran is "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.4 — "ANTHROPIC LAUNCHES PERSONAL FINANCE IN CLAUDE Anthropic is introducing Personal Finance in"
- JIOFIN.BO (Jio Financial Services Limited) score 20.3 — "ANTHROPIC LAUNCHES PERSONAL FINANCE IN CLAUDE Anthropic is introducing Personal Finance in"
- RS (Reliance, Inc.) score 19.0 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 17.0 — "Gold ETFs fall 4% in a month ahead of Dhanteras 2026: Is this a buying opportunity? Expert"
- SCHD (Schwab US Dividend Equity ETF) score 15.6 — "ConocoPhillips Doubles Profit to $4 Billion, Raises Dividend"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.6 — "ANTHROPIC LAUNCHES PERSONAL FINANCE IN CLAUDE Anthropic is introducing Personal Finance in"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.1 — "Ex-Politburo member Ma Xingrui’s corruption charges extend to end of last century"
- META (Meta) score 11.3 — "China’s Copper Squeeze Deepens as Buyers Scramble for Metal"
- DEMZ (Democratic Large Cap Core ETF) score 11.0 — "AI, data-center stocks slip as Democratic sweep clouds expansion plans"
- SEPN (Septerna, Inc.) score 10.4 — "DEMOCRATS SWEEP CONGRESS. FED HIKE BETS RETREAT. Following the midterm results, December F"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Steel Share Price Live Updates: Tata Steel's Price Update and Volatility Insights"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Tata Steel Share Price Live Updates: Tata Steel's Price Update and Volatility Insights"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.2 — "Adani Ports & Special Economic Zone Share Price Live Updates: Intimation Of Interaction Wi"
- JEF (Jefferies Financial Group Inc.) score 6.1 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.0 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have just $500 in sa"
- VT (Vanguard Total World Stock Ind) score 5.6 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- GS (Goldman Sachs Group, Inc. (The) score 4.8 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 4.7 — "Infosys Share Price Live Updates: Infosys Price Update and Trends"
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