# Transmission Layer — board brief · 2026-11-05 12:15Z

data as of **2026-11-05** · 97 series · 21 red / 27 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.507, 2d in regime; vol-pct 0.681, breadth-off 0.333, Markov P(high-vol) 0.176)
- [INVERTED] **safe_haven_gold** — corr20 -0.63, corr60 -0.53, contra nifty_50 corr20=0.35, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.23, corr60 0.14, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.76, last shift 2026-09-17. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.33, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.09, corr60 -0.11, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.62, corr60 0.41, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0031777392947298644)
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.534, β 0.8716, p 0.0); driver zc 1.94 → expected 1.477%. Type hit-rate 0.818 (n=1941).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.529, β 0.8301, p 0.0); driver zc 1.75 → expected 1.314%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.528, β 0.8746, p 0.0); driver zc 1.94 → expected 1.483%. Type hit-rate 0.818 (n=1941).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.509, β 0.8207, p 0.0); driver zc 1.75 → expected 1.299%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_demz → nikkei_225: leads 1d (ccf 0.499, β 0.775, p 0.0); driver zc 2.33 → expected 1.636%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_demz → taiwan_weighted: leads 1d (ccf 0.478, β 0.7571, p 0.0); driver zc 2.33 → expected 1.599%. Type hit-rate 0.818 (n=1941).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.445, β 0.7413, p 0.0); driver zc 3.94 → expected 2.248%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.416, β 0.3192, p 0.0); driver zc 1.81 → expected 1.144%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.401, β 0.314, p 0.0); driver zc 1.81 → expected 1.125%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.399, β 0.9982, p 0.0); driver zc 1.94 → expected 1.692%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.372, β -2.4491, p 0.0076); driver zc 1.94 → expected -4.151%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.363, β -0.0909, p 0.0); driver zc 3.39 → expected -0.503%. Type hit-rate 0.818 (n=1941).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.344, β 0.8304, p 0.0); driver zc 1.75 → expected 1.315%. Type hit-rate 0.818 (n=1941).
- **SETUP** dyn_demz → kospi: leads 1d (ccf 0.33, β 0.7845, p 0.0); driver zc 2.33 → expected 1.657%. Type hit-rate 0.818 (n=1941).
- Track record · residual_reversion: hit-rate **0.508** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=1941) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.63] cross-asset · 7 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1070.00, z20 5.30, zc 4.34, resid-z 2.30 [unexplained], 1d 7.65%, |z20|=5.30
- nifty_50 [INDICES]: last 24536.60, z20 3.89, zc 2.69, resid-z 0.72 [moved], 1d 2.40%, |z20|=3.89
- dyn_indusindbk_bo [EQUITIES]: last 911.00, z20 3.56, zc 2.48, resid-z 1.98 [unexplained], 1d 5.67%, |z20|=3.56
- dyn_jiofin_bo [EQUITIES]: last 229.50, z20 3.35, zc 1.93, resid-z 0.32 [priced], 1d 3.29%, |z20|=3.35
- nifty_metal [INDICES]: last 12592.85, z20 2.85, zc 0.58, resid-z -1.30 [quiet], 1d 0.86%, |z20|=2.85
- nifty_fmcg [INDICES]: last 46472.90, z20 2.46, zc 0.32, resid-z -2.58 [unexplained], 1d 0.45%, |z20|=2.46
- nifty_midcap_100 [INDICES]: last 60615.85, z20 2.32, zc 1.59, resid-z -0.04 [priced], 1d 1.85%, |z20|=2.32
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.23).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.681 via nifty_metal, z 1.5, reacted); dyn_muthootfin_ns (rho 0.641 via nifty_midcap_100, z 3.11, reacted); dyn_indianb_ns (rho 0.601 via nifty_midcap_100, z 3.02, reacted); midcap_largecap_ratio (rho 0.548 via nifty_midcap_100, z -1.24, reacted); nifty_it (rho 0.535 via nifty_50, z 1.1, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.566 vs dyn_bajfinance_ns
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.51 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.681, z 1.5); dyn_muthootfin_ns (rho 0.641, z 3.11); dyn_indianb_ns (rho 0.601, z 3.02); midcap_largecap_ratio (rho 0.548, z -1.24)
- Source: Terrific Thursday for stock market! Nifty jumps 576 pts, Sensex 2,009 pts after US election results; bank, IT shares fly — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/terrific-thursday-for-stock-market-nifty-jumps-576-pts-sensex-2-009-pts-after-us-election-results-bank-it-shares-fly-11793879260120.html
- Source: Sensex today | Stock Market Highlights: Sensex surges 2,009 pts, Nifty tops 24,500; Financials and autos lead rally — BusinessLine Mkts, 2026-11-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-5-november-2026/article71665358.ece
- Source: Samvat 2083 Outlook Ahead of Diwali, Muhurat Trading: Nifty at 27,000 soon? What Choice Wealth's Dheeraj said - Strategy — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/samvat-2083-outlook-ahead-of-diwali-muhurat-trading-nifty-at-27-000-soon-what-choice-wealths-dheeraj-said-strategy-11793867994138.html
- Historical analogues: 2025-07-21 (d=1.23), 2025-07-14 (d=1.37), 2025-12-23 (d=1.54)

### [RED 8.04] commodities · 2 series ↓
- brent [COMMODITIES]: last 96.67, z20 -2.21, zc 0.56, resid-z -2.95 [unexplained], 1d 2.17%, 1-session move +2.17% ≥ 1.5%; |z20|=2.21
- wti [COMMODITIES]: last 89.77, z20 -1.85, zc 0.50, resid-z -2.57 [unexplained], 1d 1.87%, 1-session move +1.87% ≥ 1.5%; |z20|=1.85
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.471 via wti, z 3.11, reacted); nifty_midcap_100 (rho -0.463 via wti, z 2.32, reacted)
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.722 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.666 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.652 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.648 vs brent
- **India receivers**: dyn_muthootfin_ns (rho -0.471, z 3.11); nifty_midcap_100 (rho -0.463, z 2.32)
- Source: Rupee finds its footing as oil worries cool, traders watch flow momentum — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-finds-its-footing-as-oil-worries-cool-traders-watch-flow-momentum/articleshow/135569527.cms
- Source: Eurozone bond yields edge lower as oil prices stabilise, ECB rate bets ease — ET Markets, 2026-11-05. https://economictimes.indiatimes.com/markets/us-stocks/news/eurozone-bond-yields-edge-lower-as-oil-prices-stabilise-ecb-rate-bets-ease/articleshow/135568561.cms
- Source: Oil cools, FPIs return: Is Dalal Street ready to run? — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/oil-cools-fpis-return-is-dalal-street-ready-to-run-11793858558879.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.27] cross-asset · 4 series ↑
- dyn_jef [EQUITIES]: last 51.18, z20 3.61, zc 1.71, resid-z 0.48 [priced], 1d 5.40%, |z20|=3.61
- dow_jones [INDICES]: last 53357.03, z20 2.88, zc 3.94, resid-z 3.99 [unexplained], 1d 3.03%, |z20|=2.88
- dyn_gs [EQUITIES]: last 928.20, z20 2.44, zc 1.81, resid-z -0.28 [priced], 1d 3.58%, |z20|=2.44
- russell_2000 [INDICES]: last 2856.96, z20 2.08, zc 1.36, resid-z -0.52 [quiet], 1d 1.58%, |z20|=2.08
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.696 vs dow_jones, historically leads by 1d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.683 vs dow_jones, historically leads by 1d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.653 vs dyn_jef, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.561 vs dyn_jef, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.52 vs dyn_jef, historically leads by 5d
- Source: S&P 500 HAS RISEN AFTER EVERY US MIDTERM ELECTION SINCE 1942 The S&P 500 has delivered positive returns in the 12 months following every US midterm election since 1942, according to Dow Jones Market Data. 🔸 Average one-year gain: Approximately 13% 🔸 1954 midterms: +33% 🔸 1994 midterms: +27% 🔸 1986 m — DeItaone, 2026-11-04. https://t.me/walter_bloomberg/38050
- Source: DOW JONES EXTENDS GAINS TO HIT TWO-MONTH HIGH; LAST UP 2.95% — DeItaone, 2026-11-04. https://t.me/walter_bloomberg/38047
- Source: Wall Street cheers US midterm results as Dow Jones jumps 1300 points; Amazon, Apple, Microsoft among top gainers — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/wall-street-cheers-us-midterm-results-as-dow-jones-jumps-1300-points-amazon-apple-microsoft-among-top-gainers-11793807617877.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.62), 2025-05-16 (d=0.72)

### [RED 5.61] indices · 2 series ↓
- taiwan_weighted [INDICES]: last 41541.62, z20 -2.78, zc -1.61, resid-z 0.04 [moved], 1d -3.28%, |z20|=2.78
- nikkei_225 [INDICES]: last 61089.31, z20 -1.58, zc -1.08, resid-z 0.01 [quiet], 1d -1.77%, |z20|=1.58
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.464 via nikkei_225, z -0.4, quiet); nifty_50 (rho -0.428 via taiwan_weighted, z 3.89, reacted); midcap_largecap_ratio (rho 0.406 via taiwan_weighted, z -1.24, reacted)
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.511 vs taiwan_weighted
- **India receivers**: dyn_idbi_ns (rho 0.464, z -0.4); nifty_50 (rho -0.428, z 3.89); midcap_largecap_ratio (rho 0.406, z -1.24)
- Source: Stock market outlook today, 4 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-4-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11793752972780.html
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

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
- Source: Lenskart investors give thumbs up to growth over margin strategy — Mint Markets, 2026-11-05. https://www.livemint.com/market/mark-to-market/lenskart-investors-give-thumbs-up-to-growth-over-margin-strategy-11793865227400.html
- Source: Worst Samvat in 15 years! Sensex, Nifty crash up to 8%: Can investors expect a bull run in Samvat 2083? What experts say — Mint Markets, 2026-11-05. https://www.livemint.com/market/worst-samvat-in-15-years-sensex-nifty-crash-up-to-8-can-investors-expect-a-bull-run-in-samvat-2083-what-experts-say-11793860986454.html
- Source: Most investors are blind to the possibility of a market crash. Here is the five-part strategy to survive one. — MarketWatch Top, 2026-11-05. https://www.marketwatch.com/story/most-investors-are-blind-to-the-possibility-of-a-market-crash-here-is-the-five-part-strategy-to-survive-one-a1762911?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [RED 5.08] indices · 4 series ↑
- cac_40 [INDICES]: last 8246.26, z20 3.41, zc 0.77, resid-z 1.67 [unexplained], 1d 0.84%, |z20|=3.41
- stoxx_50 [INDICES]: last 6306.00, z20 3.21, zc 0.56, resid-z 1.44 [quiet], 1d 0.64%, |z20|=3.21
- dax [INDICES]: last 26642.42, z20 3.04, zc 0.62, resid-z 1.52 [unexplained], 1d 0.77%, |z20|=3.04; 1y-pct=100
- ftse_100 [INDICES]: last 10915.24, z20 2.13, zc 0.68, resid-z 2.48 [unexplained], 1d 0.79%, |z20|=2.13; 1y-pct=100
- **Mechanism**: indices · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.572 via dax, z 2.32, reacted); nifty_50 (rho 0.511 via cac_40, z 3.89, reacted); dyn_tataelxsi_ns (rho 0.499 via ftse_100, z 1.14, reacted); dyn_jiofin_bo (rho 0.492 via ftse_100, z 3.35, reacted); dyn_muthootfin_ns (rho 0.472 via cac_40, z 3.11, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.665 vs stoxx_50, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.575 vs stoxx_50, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.572 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.572, z 2.32); nifty_50 (rho 0.511, z 3.89); dyn_tataelxsi_ns (rho 0.499, z 1.14); dyn_jiofin_bo (rho 0.492, z 3.35)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2026-03-31 (d=0.71)

### [RED 4.97] dyn_lth ↑
- dyn_lth [EQUITIES]: last 47.38, z20 2.97, zc 2.77, resid-z 0.84 [moved], 1d 6.32%, |z20|=2.97; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.44 via dyn_lth, z 3.11, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.44, z 3.11)
- Source: Bank of England hikes interest rate for the first time since Iran war, warns inflation will near 5% — CNBC Economy, 2026-11-05. https://www.cnbc.com/2026/11/05/interest-rates-inflation-uk.html
- Source: Tata Motors Commercial Vehicles shares vroom 8% amid mega Sensex, Nifty rally | Time to book profits or hold? Details — Mint Markets, 2026-11-05. https://www.livemint.com/market/stock-market-news/tata-motors-commercial-vehicles-shares-vroom-8-amid-mega-sensex-nifty-rally-time-to-book-profits-or-hold-details-11793851200361.html
- Source: Democrats Win Texas Oil Regulator Seat for First Time Since 1990 — OilPrice, 2026-11-04. https://oilprice.com/Energy/Crude-Oil/Democrats-Win-Texas-Oil-Regulator-Seat-for-First-Time-Since-1990.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

## Watchlist (below surfacing floor)
dyn_hdb ↑ (4.94), asx_200 ↑ (4.13), dyn_tech ↑ (3.96), equities · 2 series ↑ (3.85), dyn_schd ↑ (3.7), dyn_atherenerg_ns ↑ (3.55), dyn_rs ↑ (3.46), dyn_4417_t ↑ (3.4), dyn_muthootfin_ns ↑ (3.11), dyn_techm_ns ↑ (2.92), rates · 2 series ↑ (2.58), dyn_sepn ↑ (2.56)

## India macro
- nifty_50: 24536.5996 (1d 2.40%, z20 3.89, flag red)
- nifty_midcap_100: 60615.8516 (1d 1.85%, z20 2.32, flag amber)
- usd_inr: 94.4700 (1d -0.29%, z20 -1.08, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4704 (1d -0.54%, z20 -1.24, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · AMFI SIP / MF flows T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 99.0 — "Bullish momentum to sustain for Indian stocks on global rally"
- INOXINDIA.NS (INOX INDIA LIMITED) score 98.1 — "Bullish momentum to sustain for Indian stocks on global rally"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 97.2 — "Bullish momentum to sustain for Indian stocks on global rally"
- INDIANB.NS (INDIAN BANK) score 67.9 — "Bullish momentum to sustain for Indian stocks on global rally"
- OHI (Omega Healthcare Investors, In) score 50.4 — "Adani Ports & Special Economic Zone Share Price Live Updates: Intimation Of Interaction Wi"
- HDB (HDFC Bank Limited) score 48.8 — "HDFC Life Share Price Live Updates: HDFC Life finishes the day at Rs 543.8"
- BAC (Bank of America Corporation) score 48.4 — "ICICI Bank Share Price Live Updates: ICICI Bank Experiences Notable Price Increase"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.7 — "ICICI Bank Share Price Live Updates: ICICI Bank Experiences Notable Price Increase"
- IDBI.NS (IDBI BANK LIMITED) score 43.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Experiences Notable Price Increase"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Experiences Notable Price Increase"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.0 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Recent Trading Activity"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.6 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Recent Trading Activity"
- TECH (Bio-Techne Corp) score 40.6 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Recent Trading Activity"
- TGT (Target Corporation) score 37.0 — "Stocks to buy in November: Axis Direct names Nuvama, BEML and Petronet, sees up to 27% ups"
- 301077.SZ (CHINASTARS) score 29.1 — "China’s Copper Squeeze Deepens as Buyers Scramble for Spot Metal"
- COIN (Coinbase Global, Inc.) score 29.0 — "Bullish momentum to sustain for Indian stocks on global rally"
- CHKP (Check Point Software Technolog) score 27.6 — "Gold rises over 1%, silver gains marginally on MCX. Check 24K, 22K rates in Delhi, Mumbai,"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.4 — "India bonds climb in step with Treasuries as oil sinks"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.9 — "Oil Prices Continue to Fall as Democratic Sweep Shakes Energy Markets"
- RS (Reliance, Inc.) score 21.5 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.8 — "Bajaj Finserv Share Price Live Updates: Bajaj Finserv experiences impressive gains"
- JIOFIN.BO (Jio Financial Services Limited) score 20.8 — "Cipla Share Price Live Updates: Cipla's Financial Snapshot"
- LTH (Life Time Group Holdings, Inc.) score 20.5 — "Tata Motors Commercial Vehicles shares vroom 8% amid mega Sensex, Nifty rally | Time to bo"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 19.2 — "Gold ETFs fall 4% in a month ahead of Dhanteras 2026: Is this a buying opportunity? Expert"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.8 — "Ex-Politburo member Ma Xingrui’s corruption charges extend to end of last century"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.3 — "US Midterm Election results lift banking, financial stocks - SBI Cards, Bajaj Finance, Axi"
- SCHD (Schwab US Dividend Equity ETF) score 13.3 — "Diwali dhamaka! Multibagger stock to consider 1:10 stock split, 4:5 bonus, 100% dividend; "
- META (Meta) score 11.6 — "China’s Copper Squeeze Deepens as Buyers Scramble for Spot Metal"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.7 — "Tata Steel Share Price Live Updates: Tata Steel's Price Update and Volatility Insights"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.7 — "Tata Steel Share Price Live Updates: Tata Steel's Price Update and Volatility Insights"
- DEMZ (Democratic Large Cap Core ETF) score 10.2 — "Oil Prices Continue to Fall as Democratic Sweep Shakes Energy Markets"
- SEPN (Septerna, Inc.) score 9.5 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.3 — "Adani Ports & Special Economic Zone Share Price Live Updates: Intimation Of Interaction Wi"
- JEF (Jefferies Financial Group Inc.) score 6.9 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.8 — "‘I have no financial safety net’: I’m 66, rely on Social Security and have just $500 in sa"
- VT (Vanguard Total World Stock Ind) score 6.3 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- GS (Goldman Sachs Group, Inc. (The) score 5.4 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 5.3 — "Infosys Share Price Live Updates: Infosys Price Update and Trends"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.2 — "Broker’s call: PB Fintech (Buy)"
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