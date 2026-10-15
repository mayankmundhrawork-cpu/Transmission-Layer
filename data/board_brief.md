# Transmission Layer — board brief · 2026-10-15 09:08Z

data as of **2026-10-15** · 97 series · 12 red / 25 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.746, 9d in regime; vol-pct 0.658, breadth-off 0.833, Markov P(high-vol) 0.042)
- [INVERTED] **safe_haven_gold** — corr20 -0.32, corr60 -0.41, contra nifty_50 corr20=0.36, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.21, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 0.15, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.02, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.27, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.73, corr60 0.22, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.002699796063260207)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.569, β 0.4417, p 0.0); driver zc -1.56 → expected -0.475%. Type hit-rate 0.824 (n=2110).
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.569, β 0.3361, p 0.0); driver zc -1.68 → expected -0.648%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.567, β 0.4546, p 0.0); driver zc -1.8 → expected -0.598%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.517, β -0.4102, p 0.0); driver zc -1.8 → expected 0.539%. Type hit-rate 0.824 (n=2110).
- **SETUP** nasdaq_100 → asx_200: leads 1d (ccf 0.482, β 0.2779, p 0.0); driver zc -1.99 → expected -0.553%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.467, β 0.2298, p 0.0); driver zc -3.23 → expected -1.086%. Type hit-rate 0.824 (n=2110).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.449, β -0.346, p 0.0); driver zc -1.56 → expected 0.372%. Type hit-rate 0.824 (n=2110).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.426, β -0.2411, p 0.0); driver zc -1.99 → expected 0.48%. Type hit-rate 0.824 (n=2110).
- **SETUP** russell_2000 → usd_brl: leads 1d (ccf -0.425, β -0.2488, p 0.0); driver zc -1.68 → expected 0.48%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.367, β -2.4265, p 0.0084); driver zc -1.8 → expected 3.19%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.336, β 0.5362, p 1e-05); driver zc -1.8 → expected -0.705%. Type hit-rate 0.824 (n=2110).
- **SETUP** sp500 → india_vix: leads 1d (ccf -0.333, β -2.1553, p 0.01833); driver zc -1.56 → expected 2.318%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.329, β 0.1451, p 1e-05); driver zc -1.8 → expected -0.191%. Type hit-rate 0.824 (n=2110).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.298, β 0.4652, p 0.00058); driver zc -1.56 → expected -0.5%. Type hit-rate 0.824 (n=2110).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.29, β 0.3242, p 0.00036); driver zc -1.68 → expected -0.625%. Type hit-rate 0.824 (n=2110).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.289, β 0.3567, p 0.0); driver zc -1.8 → expected -0.469%. Type hit-rate 0.824 (n=2110).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.278, β 0.2407, p 0.0); driver zc -1.68 → expected -0.464%. Type hit-rate 0.824 (n=2110).
- **SETUP** russell_2000 → india_vix: leads 1d (ccf -0.272, β -1.2626, p 0.00243); driver zc -1.68 → expected 2.436%. Type hit-rate 0.824 (n=2110).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.255, β 0.3079, p 2e-05); driver zc -1.56 → expected -0.331%. Type hit-rate 0.824 (n=2110).
- Track record · residual_reversion: hit-rate **0.496** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2110) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.66] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 73.63, z20 2.83, zc n/a, resid-z n/a [quiet], 1d -0.44%, GSR<75 (extreme low); |z20|=2.83
- comex_silver [COMMODITIES]: last 56.68, z20 -1.82, zc 0.70, resid-z 0.02 [quiet], 1d 2.03%, |z20|=1.82
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.822 vs comex_silver, historically leads by 4d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.536 vs gold_silver_ratio, historically leads by 5d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.524 vs gold_silver_ratio, historically leads by 3d
- Source: Silver futures rise to ₹2.08 lakh per kg — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/gold/silver-futures-rise-to-208-lakh-per-kg/article71586939.ece
- Source: Silver futures plunge 4% on MCX ahead of US CPI; rising oil adds pressure — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/commodities/silver-futures-plunge-4-on-mcx-ahead-of-us-cpi-rising-oil-adds-pressure/articleshow/134946048.cms
- Source: SPOT SILVER FALLS NEARLY 3% TO $57.58/OZ — DeItaone, 2026-10-14. https://t.me/walter_bloomberg/37071
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.68] usd_inr ↓
- usd_inr [FX]: last 95.04, z20 -2.68, zc -0.55, resid-z -0.11 [quiet], 1d -0.26%, 20d range extreme; |z20|=2.68
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.362 via usd_inr, z 1.55, reacted); dyn_idbi_ns (rho -0.36 via usd_inr, z -0.25, quiet)
- **India receivers**: dyn_karurvysya_ns (rho -0.362, z 1.55); dyn_idbi_ns (rho -0.36, z -0.25)
- Source: Rupee hedging turmoil exposes strain in India's FX market — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-hedging-turmoil-exposes-strain-in-indias-fx-market/article71587071.ece
- Source: Rupee continues its winning streak against US dollar — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-continues-its-winning-streak-against-us-dollar/article71586682.ece
- Source: Rupee extends rise but falters past 95/$ on importer hedging, outflows — BusinessLine Mkts, 2026-10-14. https://www.thehindubusinessline.com/markets/forex/rupee-extends-rise-but-falters-past-95-on-importer-hedging-outflows/article71583244.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 7.31] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1634.60, z20 3.99, zc 2.18, resid-z 0.98 [priced], 1d 3.77%, |z20|=3.99
- nifty_it [INDICES]: last 30735.70, z20 3.41, zc 1.11, resid-z -0.15 [quiet], 1d 1.87%, |z20|=3.41
- dyn_tataelxsi_ns [EQUITIES]: last 3685.20, z20 3.41, zc 0.69, resid-z -0.50 [quiet], 1d 1.71%, |z20|=3.41
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.519 via dyn_tataelxsi_ns, z -0.18, quiet); dyn_justdial_bo (rho 0.501 via nifty_it, z 1.05, reacted); nifty_50 (rho 0.478 via dyn_tataelxsi_ns, z 0.39, quiet); dyn_tatatech_ns (rho 0.473 via nifty_it, z 1.35, reacted); midcap_largecap_ratio (rho -0.377 via dyn_techm_ns, z -3.19, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.519 vs dyn_tataelxsi_ns
- **India receivers**: nifty_fmcg (rho 0.519, z -0.18); dyn_justdial_bo (rho 0.501, z 1.05); nifty_50 (rho 0.478, z 0.39); dyn_tatatech_ns (rho 0.473, z 1.35)
- Source: Q2 Results Today Live: Nestle Q2 PAT up 36% y-o-y, Polycab profit rises 44%, Wipro, Tech Mahindra, Jio Financial, IRFC, HDFC AMC, HDFC Life, Tata Communications, KVB, IIFL, Persistent Systems, 360 ONE WAM, Angel One to announce Q2 results — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-wipro-nestle-india-tech-mahindra-jio-financial-persistent-systems-irfc-polycab-hdfc-amc-tata-communication-results-groww-tata-tech-leela-emmvee-15-october-2026/article71586591.ece
- Source: Top stocks to buy: Why experts suggest Tata Elxsi, Zensar Tech, Havells India | Check target, support, stop loss — Mint Markets, 2026-10-15. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-why-experts-suggest-tata-elxsi-zensar-tech-havells-india-check-target-support-stop-loss-11792052043429.html
- Source: Q2 Results Live Updates: Wipro, Tech Mahindra set to announce September quarter earnings today. Check brokerage estimates, share price — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/stocks/live-blog/wipro-q2-results-today-live-updates-tech-mahindra-quarter-2-fy27-earnings-dividend-share-price-updates-15-october-2026/liveblog/134959381.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 6.19] midcap_largecap_ratio ↓
- midcap_largecap_ratio [DERIVED]: last 2.58, z20 -3.19, zc n/a, resid-z n/a [quiet], 1d -1.82%, break below 100-DMA; |z20|=3.19
- **Mechanism**: midcap_largecap_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.514 via midcap_largecap_ratio, z -0.63, quiet); dyn_techm_ns (rho -0.377 via midcap_largecap_ratio, z 3.99, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.514 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.514, z -0.63); dyn_techm_ns (rho -0.377, z 3.99)
- Historical analogues: 2025-12-31 (d=0.0), 2025-07-03 (d=0.11), 2025-07-23 (d=0.2)

### [AMBER 5.3] brent ↑
- brent [COMMODITIES]: last 104.01, z20 0.30, zc -1.01, resid-z -1.24 [quiet], 1d -1.93%, 1-session move -1.93% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.866 vs brent, historically leads by 5d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.627 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.604 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.582 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.572 vs brent
- Source: India’s edible oil imports up 3.27% in Nov-Sept on higher palm oil shipments — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/economy/agri-business/indias-edible-oil-imports-up-327-in-nov-sept-on-higher-palm-oil-shipments/article71587067.ece
- Source: Bessent urges World Bank to end restrictions on upstream oil, gas financing — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/bessent-urges-world-bank-to-end-restrictions-on-upstream-oil-gas-financing/articleshow/134961053.cms
- Source: Oil Prices Fall as Trump Considers Easing Sanctions on Shadow Fleet Tankers — OilPrice, 2026-10-15. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Fall-as-Trump-Considers-Easing-Sanctions-on-Shadow-Fleet-Tankers.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [AMBER 5.2] crypto · 2 series ↓
- eth_usd [CRYPTO]: last 2372.81, z20 -2.37, zc -0.48, resid-z -0.27 [quiet], 1d -1.88%, |z20|=2.37
- btc_usd [CRYPTO]: last 81240.39, z20 -2.00, zc -0.19, resid-z -0.19 [quiet], 1d -0.39%, |z20|=2.00
- **Mechanism**: crypto · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-27 (z-distance 0.19).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.558 vs eth_usd, historically leads by 1d
- Source: Bitcoin Slides as Wall Street Risk Pullback Tests Bullish Turn — Mint Markets, 2026-10-14. https://www.livemint.com/market/bitcoin-slides-as-wall-street-risk-pullback-tests-bullish-turn-11792003663551.html
- Source: Bitcoin hovers near $83K as Asian stock sell-off triggers over $800 million in crypto liquidations — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-hovers-near-83k-as-asian-stock-sell-off-triggers-over-800-million-in-crypto-liquidations/articleshow/134939967.cms
- Source: MICHAEL SAYLOR PREDICTS BITCOIN WILL SURGE BACK ABOVE $100,000 Strategy ($MSTR ) Chairman Michael Saylor says Bitcoin's bear market is over, predicting a return above $100,000. Key takeaways: * Bitcoin: Trading near $83,000. * Bottom: Saylor believes BTC bottomed just below $60,000. * Forecast: Expe — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37031
- Historical analogues: 2026-05-27 (d=0.19), 2025-03-01 (d=0.2), 2026-06-09 (d=0.23)

### [RED 5.08] dyn_301077_sz ↓
- dyn_301077_sz [EQUITIES]: last 19.80, z20 -3.08, zc -0.97, resid-z -0.36 [quiet], 1d -2.80%, |z20|=3.08; 1y-pct=5
- **Mechanism**: dyn_301077_sz ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Source: China sentences 3 more Myanmar crime bosses to death in scam centre crackdown — SCMP Economy, 2026-10-13. https://www.scmp.com/news/china/politics/article/3370757/china-sentences-3-more-myanmar-crime-bosses-death-scam-centre-crackdown?utm_source=rss_feed
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.92] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3706.48, z20 -2.92, zc -2.24, resid-z -0.24 [moved], 1d -1.61%, |z20|=2.92; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.39 via shanghai_comp, z -1.45, reacted)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.638 vs shanghai_comp, historically leads by 2d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.509 vs shanghai_comp, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.39, z -1.45)
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

## Watchlist (below surfacing floor)
cross-asset · 5 series ↑ (4.56), dyn_bac ↓ (4.5), kospi ↓ (4.32), dyn_rs ↑ (3.77), soybeans ↓ (3.64), dyn_dell ↓ (3.31), russell_2000 ↓ (3.25), vix ↑ (3.14), dyn_4417_t ↑ (3.01), eur_usd ↓ (2.97), dxy ↑ (2.69), dyn_tech ↑ (2.6)

## India macro
- nifty_50: 23004.7500 (1d 1.69%, z20 0.39, flag none)
- nifty_midcap_100: 59303.4492 (1d -0.16%, z20 -0.63, flag none)
- usd_inr: 95.0350 (1d -0.26%, z20 -2.68, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5779 (1d -1.82%, z20 -3.19, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 94.2 — "Stock recommendations for 15 October from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.7 — "Stock recommendations for 15 October from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.4 — "Stock recommendations for 15 October from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 87.8 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- BAC (Bank of America Corporation) score 81.3 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- HDB (HDFC Bank Limited) score 73.7 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- IDBI.NS (IDBI BANK LIMITED) score 70.7 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 70.7 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 70.7 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- TECHM.NS (TECH MAHINDRA LIMITED) score 65.4 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 63.9 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- TECH (Bio-Techne Corp) score 63.9 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- COIN (Coinbase Global, Inc.) score 56.4 — "Global Market: Japanese government bond yields hit one-month lows as investors seek safety"
- OHI (Omega Healthcare Investors, In) score 55.5 — "Ahead of IPO, Tonbo Imaging garners ₹255 cr from anchor investors"
- CHKP (Check Point Software Technolog) score 40.8 — "Tonbo Imaging India IPO opens for subscription; GMP signals 71% listing gain. Check key de"
- TGT (Target Corporation) score 40.0 — "Ashish Kacholia's portfolio stock: Up 70% in YTD | Experts see more upside — target price,"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.2 — "Global Market: Japanese government bond yields hit one-month lows as investors seek safety"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.6 — "Global Market: IMF warns of energy shock, AI correction risks to Asia's growth outlook"
- SEPN (Septerna, Inc.) score 25.8 — "Q2 Results Live Updates: Wipro, Tech Mahindra set to announce September quarter earnings t"
- LTH (Life Time Group Holdings, Inc.) score 25.2 — "HD Fire Protect IPO Day 3: GMP at 33%, Day 2 subscription hits 16.5 times; check key detai"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.1 — "Canara Bank shares crash 6% after Q2 results - Should investors buy, sell, or hold? Expert"
- RS (Reliance, Inc.) score 24.1 — "Top stocks to watch today: Reliance Industries, IDBI Bank, Wipro shares in focus on Thursd"
- 301077.SZ (CHINASTARS) score 23.3 — "Global Market: China stocks fall as hot US inflation data revives rate hike fears"
- JIOFIN.BO (Jio Financial Services Limited) score 19.7 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.3 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.3 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- BZ=F (Brent Crude Oil Last Day Finan) score 16.5 — "Bonus shares, stock split, dividend: Last day to buy as these shares trade ex-date today |"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.0 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Performance"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 11.8 — "LIC Housing Finance among 4 F&O stocks with a sharp rise in futures open interest"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.0 — "Sensex on fire! 1,500-point rally puts bulls back in the driver’s seat. What just happened"
- VT (Vanguard Total World Stock Ind) score 10.5 — "Bessent urges World Bank to end restrictions on upstream oil, gas financing"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.5 — "LIC Housing Finance among 4 F&O stocks with a sharp rise in futures open interest"
- GS (Goldman Sachs Group, Inc. (The) score 7.9 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- JEF (Jefferies Financial Group Inc.) score 6.8 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- META (Meta) score 6.3 — "IT stocks lift Nifty as Adani, Metal stocks slide amid global sellof"
- NVDA (NVIDIA Corporation) score 5.9 — "Nvidia pledges $250 million in computing resources to boost UK AI safety research"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.8 — "Bajaj Broking rolls out algorithm trading platform for retail investors"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.5 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.2 — "Piero Cipollone: Interview with Corriere della Sera"
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