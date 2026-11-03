# Transmission Layer — board brief · 2026-11-03 11:53Z

data as of **2026-11-03** · 97 series · 11 red / 31 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.713, 3d in regime; vol-pct 0.88, breadth-off 0.545, Markov P(high-vol) 0.264)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.46, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.16, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.06, corr60 0.06, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.32, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.13, corr60 -0.11, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.56, corr60 0.38, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.588, β 0.4859, p 0.0); driver zc -1.53 → expected -0.531%. Type hit-rate 0.829 (n=1674).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.565, β 0.436, p 0.0); driver zc -2.46 → expected -0.792%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.562, β 0.4472, p 0.0); driver zc -2.26 → expected -0.747%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.524, β -0.3106, p 0.0); driver zc -2.26 → expected 0.519%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.47, β 0.1797, p 0.0); driver zc -1.97 → expected -0.643%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.452, β 0.1288, p 0.0); driver zc -2.41 → expected -0.794%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.451, β -0.3979, p 0.0); driver zc -2.26 → expected 0.665%. Type hit-rate 0.829 (n=1674).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.448, β -0.258, p 0.0); driver zc -2.46 → expected 0.469%. Type hit-rate 0.829 (n=1674).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.431, β -0.1811, p 0.0); driver zc -2.59 → expected 0.627%. Type hit-rate 0.829 (n=1674).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.381, β -0.237, p 0.0); driver zc -1.53 → expected 0.259%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.378, β -2.4982, p 0.00637); driver zc -2.26 → expected 4.175%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.353, β 0.5549, p 0.0); driver zc -2.26 → expected -0.927%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.321, β 0.1408, p 1e-05); driver zc -2.26 → expected -0.235%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.317, β -0.0909, p 3e-05); driver zc -1.97 → expected 0.325%. Type hit-rate 0.829 (n=1674).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.316, β 0.4867, p 0.00026); driver zc -2.46 → expected -0.885%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.307, β 0.3757, p 0.0); driver zc -2.26 → expected -0.628%. Type hit-rate 0.829 (n=1674).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.275, β 0.329, p 0.0); driver zc -2.46 → expected -0.598%. Type hit-rate 0.829 (n=1674).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.262, β 0.2238, p 1e-05); driver zc -2.59 → expected -0.775%. Type hit-rate 0.829 (n=1674).
- Track record · residual_reversion: hit-rate **0.507** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=1674) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.78] indices · 2 series ↑
- nifty_50 [INDICES]: last 23810.85, z20 3.95, zc 1.91, resid-z 0.94 [moved], 1d 1.58%, |z20|=3.95
- nifty_fmcg [INDICES]: last 45580.05, z20 1.95, zc 3.29, resid-z 2.99 [unexplained], 1d 3.65%, |z20|=1.95
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.701 via nifty_50, z 0.37, quiet); dyn_jiofin_bo (rho 0.637 via nifty_50, z 0.41, quiet); dyn_bajfinance_ns (rho 0.612 via nifty_50, z 0.99, quiet); dyn_indusindbk_bo (rho 0.551 via nifty_50, z -0.04, quiet); nifty_metal (rho 0.547 via nifty_50, z 0.61, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.701 vs nifty_50, historically leads by 3d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.637 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.701 vs nifty_50
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.612 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.551 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.701, z 0.37); dyn_jiofin_bo (rho 0.637, z 0.41); dyn_bajfinance_ns (rho 0.612, z 0.99); dyn_indusindbk_bo (rho 0.551, z -0.04)
- Source: Nifty crosses 23,800 for first time since August on falling crude prices, earnings boost — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/nifty-crosses-23800-for-first-time-since-august-on-falling-crude-prices-earnings-boost/article71660642.ece
- Source: Sensex today | Stock Market Highlights: Sensex jumps 1,225 pts at close, Nifty crosses 23,800; indices rise for 4th straight session — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-3-november-2026/article71657258.ece
- Source: Nifty tops 23,600 at midday as Banks, Telecom lead broad rally — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/nifty-tops-23600-at-midday-as-banks-telecom-lead-broad-rally/article71659941.ece
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [RED 6.72] cross-asset · 4 series ↓
- ust_2y [RATES]: last 4.56, z20 -3.06, zc -0.84, resid-z -0.81 [quiet], 1d -1.08%, |z20|=3.06
- ust_10y [RATES]: last 4.94, z20 -1.79, zc -0.75, resid-z -1.16 [quiet], 1d -0.80%, |z20|=1.79
- tips_10y_real [RATES]: last 2.60, z20 -1.76, zc -0.63, resid-z -0.61 [quiet], 1d -1.14%, |z20|=1.76
- dyn_schd [EQUITIES]: last 35.88, z20 1.62, zc 0.53, resid-z -0.68 [quiet], 1d 0.29%, 1y-pct=100
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.531 vs dyn_schd, historically leads by 4d
- Watch next: kospi (inverse) — not yet - watch; rho -0.596 vs dyn_schd
- Source: Small-cap stock under  ₹50 jumps 5% after announcement of Q2 Results 2026, dividend | Up 65% in 6 months; do you own? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/smallcap-stock-under-rs-50-jumps-5-after-announcement-of-q2-results-2026-dividend-up-65-in-6-months-do-you-own-11793700056652.html
- Source: German bond yields rise as oil climbs ahead of US Midterm elections — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/news/german-bond-yields-rise-as-oil-climbs-ahead-of-us-midterm-elections/articleshow/135490769.cms
- Source: Asian Paints surges 2.7% as investors rush ahead of dividend ex-date — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/stock-markets/asian-paints-surges-27-as-investors-rush-ahead-of-dividend-ex-date/article71659864.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.57), 2025-05-19 (d=1.16)

### [RED 6.56] cross-asset · 4 series ↓
- sp500 [INDICES]: last 7542.33, z20 -2.90, zc -2.46, resid-z -2.23 [unexplained], 1d -0.50%, |z20|=2.90
- nasdaq_100 [INDICES]: last 27996.29, z20 -2.40, zc -2.59, resid-z -0.35 [priced], 1d -1.37%, |z20|=2.40
- vix [INDICES]: last 21.43, z20 2.28, zc 0.14, resid-z n/a [quiet], 1d 1.32%, |z20|=2.28
- dyn_vt [EQUITIES]: last 155.12, z20 -2.10, zc -2.26, resid-z 0.41 [priced], 1d -0.14%, |z20|=2.10
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.741 vs sp500, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.83 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.575 vs sp500, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.711 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.626 vs dyn_vt
- Source: This signal from the corporate bond market has historically preceded big drawdowns for the S&P 500 — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/this-signal-from-the-corporate-bond-market-has-historically-preceded-big-drawdowns-for-the-s-p-500-8c1a3d25?mod=mw_rss_topstories
- Source: Stock market outlook today, 3 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Taiwan cues — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-3-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-taiwan-cues-11793666426237.html
- Source: Nasdaq-100 tumbles into its third correction this year as AI worries mount — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/nasdaq-100-tumbles-into-its-third-correction-this-year-as-ai-worries-mount-abee4c0d?mod=mw_rss_topstories
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 6.01] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 137.87, z20 -3.17, zc -2.31, resid-z -1.49 [moved], 1d -3.95%, |z20|=3.17; 1y-pct=0
- btc_usd [CRYPTO]: last 76966.23, z20 -1.95, zc 0.18, resid-z 0.48 [quiet], 1d 0.38%, |z20|=1.95
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Is the AI boom losing steam? Global economy faces growing risks — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/is-the-ai-boom-losing-steam-global-economy-faces-growing-risks/articleshow/135491964.cms
- Source: NSE International Exchange begins 23.5-hour trading, extends market access across global time zones — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/stocks/news/nse-international-exchange-begins-23-5-hour-trading-extends-market-access-across-global-time-zones/articleshow/135488585.cms
- Source: China to expand global access to yuan assets, promote Hong Kong as offshore hub — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/china-to-expand-global-access-to-yuan-assets-promote-hong-kong-as-offshore-hub/articleshow/135484600.cms
- Historical analogues: 2026-05-22 (d=0.16), 2025-08-19 (d=0.28), 2026-04-02 (d=0.34)

### [RED 5.6] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3916.10, z20 -2.28, zc -0.74, resid-z -2.77 [unexplained], 1d -1.35%, |z20|=2.28; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 79.83, z20 2.20, zc n/a, resid-z n/a [quiet], 1d 2.00%, |z20|=2.20
- comex_silver [COMMODITIES]: last 49.06, z20 -2.17, zc -1.07, resid-z -0.80 [quiet], 1d -3.28%, |z20|=2.17; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.527 vs comex_gold
- Source: Gold demand down 30% in September quarter as high prices hurt jewellery sales — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/gold/gold-demand-down-30-in-september-quarter-as-high-prices-hurt-jewellery-sales/article71660046.ece
- Source: Silver prices crash  ₹8,500/kg, gold drops  ₹2,000/10g as US-Iran tensions revive inflation fears; is more fall ahead? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/silver-prices-crash-rs-8-500-kg-gold-drops-rs-2-000-10g-as-us-iran-tensions-revive-inflation-fears-is-more-fall-ahead-11793698796709.html
- Source: Today’s Gold Rate in India November 3: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-3-2026/article71660045.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.51] brent ↓
- brent [COMMODITIES]: last 106.52, z20 -0.51, zc 0.80, resid-z -1.52 [unexplained], 1d 1.67%, 1-session move +1.67% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.39 via brent, z 0.37, quiet)
- Watch next: wti (co-move) — not yet - watch; rho 0.794 vs brent, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho -0.39, z 0.37)
- Source: Nifty crosses 23,800 for first time since August on falling crude prices, earnings boost — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/nifty-crosses-23800-for-first-time-since-august-on-falling-crude-prices-earnings-boost/article71660642.ece
- Source: Oil has had a massive run, but a prominent bull sees a turning point on midterm eve — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/oil-has-had-a-massive-run-but-a-prominent-bull-sees-a-turning-point-on-midterm-eve-be2c5fa7?mod=mw_rss_topstories
- Source: Rupee nudges higher, forward premiums dip with focus on US midterm, oil moves — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-nudges-higher-forward-premiums-dip-with-focus-on-us-midterm-oil-moves/articleshow/135492726.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [AMBER 5.15] wti ↑
- wti [COMMODITIES]: last 98.53, z20 0.15, zc 0.86, resid-z -1.34 [quiet], 1d 2.15%, 1-session move +2.15% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.418 via wti, z 0.37, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.794 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.541 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.418, z 0.37)
- Source: Nifty crosses 23,800 for first time since August on falling crude prices, earnings boost — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/nifty-crosses-23800-for-first-time-since-august-on-falling-crude-prices-earnings-boost/article71660642.ece
- Source: Oil has had a massive run, but a prominent bull sees a turning point on midterm eve — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/oil-has-had-a-massive-run-but-a-prominent-bull-sees-a-turning-point-on-midterm-eve-be2c5fa7?mod=mw_rss_topstories
- Source: Rupee nudges higher, forward premiums dip with focus on US midterm, oil moves — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-nudges-higher-forward-premiums-dip-with-focus-on-us-midterm-oil-moves/articleshow/135492726.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 4.73] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 928.00, z20 -2.73, zc -0.12, resid-z -1.06 [quiet], 1d -0.32%, |z20|=2.73; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.578 via dyn_policybzr_ns, z 0.99, quiet); nifty_midcap_100 (rho 0.52 via dyn_policybzr_ns, z 0.37, quiet); nifty_50 (rho 0.482 via dyn_policybzr_ns, z 3.95, reacted); dyn_indusindbk_bo (rho 0.45 via dyn_policybzr_ns, z -0.04, quiet); nifty_metal (rho 0.367 via dyn_policybzr_ns, z 0.61, quiet)
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.578 vs dyn_policybzr_ns, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.723 vs dyn_policybzr_ns
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.52 vs dyn_policybzr_ns
- **India receivers**: dyn_bajfinance_ns (rho 0.578, z 0.99); nifty_midcap_100 (rho 0.52, z 0.37); nifty_50 (rho 0.482, z 3.95); dyn_indusindbk_bo (rho 0.45, z -0.04)
- Source: Broker’s call: PB Fintech (Buy) — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/brokers-call-pb-fintech-buy/article71656563.ece
- Source: MobiKwik shares zoom 10% as fintech firm posts record Rs 12 crore profit in Q2 — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/mobikwik-shares-zoom-10-as-fintech-firm-posts-record-rs-12-crore-profit-in-q2/articleshow/135452378.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.51), dyn_jef ↑ (4.42), dyn_atherenerg_ns ↑ (4.37), dyn_tgt ↑ (4.19), rates · 2 series ↑ (3.9), shanghai_comp ↓ (3.77), dyn_4417_t ↑ (3.65), dyn_sepn ↑ (3.28), dyn_tech ↑ (3.27), taiwan_weighted ↓ (2.89), dyn_techm_ns ↑ (2.82), eur_usd ↓ (2.64)

## India macro
- nifty_50: 23810.8496 (1d 1.58%, z20 3.95, flag red)
- nifty_midcap_100: 58598.0508 (1d 1.06%, z20 0.37, flag none)
- usd_inr: 94.7400 (1d -0.17%, z20 -0.87, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4610 (1d -0.51%, z20 -1.68, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · AMFI SIP / MF flows T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 90.6 — "Indian bond rally seen extending on weaker oil, Treasury yields"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.6 — "Indian bond rally seen extending on weaker oil, Treasury yields"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.2 — "Indian bond rally seen extending on weaker oil, Treasury yields"
- INDIANB.NS (INDIAN BANK) score 59.5 — "Indian bond rally seen extending on weaker oil, Treasury yields"
- OHI (Omega Healthcare Investors, In) score 49.1 — "Nifty Expiry Today Prediction 3 Nov: Bulls back in action! Check support, resistance level"
- BAC (Bank of America Corporation) score 45.0 — "HDFC Bank shares surges 2.86%, lead Nifty 50 gainers"
- TGT (Target Corporation) score 44.7 — "Marico share price: FMCG stock gains 8% on strong Q2 results, nears 52-week high - Buy or "
- HDB (HDFC Bank Limited) score 42.5 — "HDFC Bank shares surges 2.86%, lead Nifty 50 gainers"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.5 — "Rupee to benefit from oil plunge while facing technical resistance, dollar strength"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.1 — "HDFC Bank shares surges 2.86%, lead Nifty 50 gainers"
- IDBI.NS (IDBI BANK LIMITED) score 40.0 — "HDFC Bank shares surges 2.86%, lead Nifty 50 gainers"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.0 — "HDFC Bank shares surges 2.86%, lead Nifty 50 gainers"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "Rupee to benefit from oil plunge while facing technical resistance, dollar strength"
- TECH (Bio-Techne Corp) score 39.4 — "Rupee to benefit from oil plunge while facing technical resistance, dollar strength"
- COIN (Coinbase Global, Inc.) score 33.7 — "China to expand global access to yuan assets, promote Hong Kong as offshore hub"
- CHKP (Check Point Software Technolog) score 32.8 — "Nifty Expiry Today Prediction 3 Nov: Bulls back in action! Check support, resistance level"
- RS (Reliance, Inc.) score 30.4 — "Reliance Industries among 8 stocks showing RSI Trending Up"
- 301077.SZ (CHINASTARS) score 28.9 — "‘Speak last’: China’s fifth plenum moves to rein in Communist Party leaders"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.8 — "CVR Energy Nears $4 Billion Refinery Deal With Marathon"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.2 — "Indian bond rally seen extending on weaker oil, Treasury yields"
- LTH (Life Time Group Holdings, Inc.) score 23.5 — "Blockbuster IPO debut of BLS Polymers; 3 times premium as compared to Jio Platforms - All "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.7 — "HDFC Bank share price gains 3% today: Here's why - Is the worst over after a 27% one-year "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.5 — "Bajaj Finserv Q2 Results: Net profit jumps 23% YoY to Rs 2,758 crore, shares rise 2%"
- SCHD (Schwab US Dividend Equity ETF) score 13.2 — "Asian Paints surges 2.7% as investors rush ahead of dividend ex-date"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.1 — "‘Speak last’: China’s fifth plenum moves to rein in Communist Party leaders"
- JIOFIN.BO (Jio Financial Services Limited) score 12.9 — "Anthropic IPO: What its latest financial filing reveals about AI growth"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.6 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.6 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.4 — "Fusion Finance shares surge 10% after strong Q2 results"
- META (Meta) score 9.3 — "Q2 Results Today Live: SBI Q2 PAT up 14%, Bajaj Finserv, Pfizer, Solar Ind, Rane (Madras),"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
- VT (Vanguard Total World Stock Ind) score 8.9 — "ADNOC Chief Says World Has “Eroded Its Supply Buffers”"
- SEPN (Septerna, Inc.) score 8.5 — "Gold demand down 30% in September quarter as high prices hurt jewellery sales"
- JEF (Jefferies Financial Group Inc.) score 8.5 — "ITC shares rise 2% after Q2 results. What are Jefferies, Nuvama and others saying?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.0 — "Diwali stocks by Motilal Oswal: Eternal, Adani Ports among 10 stocks with upside of up to "
- GS (Goldman Sachs Group, Inc. (The) score 7.4 — "DEMOCRATIC SWEEP AT 73%. WALL STREET BRACES FOR MIDTERMS. Prediction markets price a 73% c"
- INFY (Infosys Limited) score 5.3 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.9 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.8 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
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