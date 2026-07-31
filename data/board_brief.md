# Transmission Layer — board brief · 2026-07-31 08:16Z

data as of **2026-07-31** · 98 series · 14 red / 31 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.369, 2d in regime; vol-pct 0.405, breadth-off 0.333, Markov P(high-vol) 0.304)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.46, contra nifty_50 corr20=0.24, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.33, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.04, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.84, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.06, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.17, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.3, corr60 0.21, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.002977997490474893)
- **SETUP** nasdaq_100 → dyn_453950_ks: leads 1d (ccf 0.598, β 0.8763, p 0.0); driver zc 2.28 → expected 2.925%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.579, β 0.4626, p 0.0); driver zc 2.36 → expected 0.979%. Type hit-rate 0.816 (n=3193).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.578, β 0.4459, p 0.0); driver zc 1.81 → expected 0.74%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.545, β 1.1073, p 0.0); driver zc 2.36 → expected 2.342%. Type hit-rate 0.816 (n=3193).
- **SETUP** sp500 → dyn_453950_ks: leads 1d (ccf 0.54, β 1.0539, p 0.0); driver zc 1.81 → expected 1.748%. Type hit-rate 0.816 (n=3193).
- **SETUP** nasdaq_100 → asx_200: leads 1d (ccf 0.506, β 0.2918, p 0.0); driver zc 2.28 → expected 0.974%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.503, β 0.2063, p 0.0); driver zc 1.61 → expected 0.711%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_ms → dyn_453950_ks: leads 1d (ccf 0.425, β 0.4513, p 0.0); driver zc 1.61 → expected 1.555%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.36, β -2.4452, p 0.00537); driver zc 2.36 → expected -5.173%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.343, β 0.5385, p 0.0); driver zc 2.36 → expected 1.139%. Type hit-rate 0.816 (n=3193).
- **SETUP** nasdaq_100 → nifty_metal: leads 1d (ccf 0.279, β 0.3128, p 0.00042); driver zc 2.28 → expected 1.044%. Type hit-rate 0.816 (n=3193).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.265, β 0.3778, p 0.0); driver zc 2.36 → expected 0.799%. Type hit-rate 0.816 (n=3193).
- Track record · residual_reversion: hit-rate **0.49** (n=1145) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=3193) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 12.39] dyn_msft ↑
- dyn_msft [EQUITIES]: last 451.48, z20 10.39, zc 9.76, resid-z 0.08 [moved], 1d 15.60%, |z20|=10.39
- **Mechanism**: The surge in Microsoft's stock price is largely explained by its strong earnings report, which beat expectations and highlighted the company's successful AI investments. This move is priced, as evidenced by the low resid_z value of 0.08, indicating that the stock's reaction is largely in line with its factor exposures. The valid vix_equity_inverse channel suggests that the equity market's inverse relationship with volatility is intact, which could lead to further gains if volatility subsides.
- **Gap**: No gap: the move in Microsoft's stock is largely explained by its earnings report and is in line with its factor exposures, as indicated by the low resid_z value.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react positively to the strength in US equities, particularly if the vix_equity_inverse channel holds. However, the reaction is not yet evident.
- Watch next: nifty_50 (up) — not yet - watch; Indian equities may follow the US market's lead
- Source: Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/microsofts-ai-bet-pays-off-key-takeaways-from-its-blockbuster-quarter/slideshow/132757561.cms
- Source: Micron, Sandisk and other chip stocks get major boosts in the wake of Microsoft’s earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/micron-sandisk-and-other-chip-stocks-get-major-boosts-in-the-wake-of-microsofts-earnings-25460e61?mod=mw_rss_topstories
- Source: Why Microsoft’s stock soared to a historic gain after earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/why-microsofts-stock-is-soaring-toward-a-historic-gain-after-earnings-96cd5b1e?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [RED 7.25] fx · 4 series ↑
- eur_usd [FX]: last 1.15, z20 3.59, zc 1.10, resid-z 1.44 [quiet], 1d 0.41%, |z20|=3.59
- aud_usd [FX]: last 0.70, z20 2.22, zc 2.15, resid-z 2.05 [unexplained], 1d 1.02%, |z20|=2.22
- usd_mxn [FX]: last 17.34, z20 -2.14, zc -1.39, resid-z -1.19 [quiet], 1d -0.60%, |z20|=2.14
- usd_brl [FX]: last 5.06, z20 -1.70, zc -1.74, resid-z -1.70 [unexplained], 1d -1.29%, |z20|=1.70
- **Mechanism**: The recent surge in oil prices, driven by heightened hostilities in the Middle East, has led to a decline in Euro zone government bonds and a rise in yields. This has created a ripple effect in the foreign exchange market, with the EUR/USD, AUD/USD, USD/MXN, and USD/BRL experiencing significant moves. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may influence Indian metal equities.
- **Gap**: No gap: The big raw moves in EUR/USD, AUD/USD, USD/MXN, and USD/BRL are largely priced, given their relatively small resid_z values, indicating that the market has already factored in the recent events.
- **India take**: The Indian instrument that expresses this move is the USD/INR, which may weaken due to the oil price surge and its impact on India's import bill. However, the weak dxy_inr_channel and inr_oil_channel suggest that this relationship is not currently robust.
- Watch next: eur_usd (down) — already moved; Oil price surge and ECB's digital euro app announcement
- Watch next: aud_usd (down) — already moved; Oil price surge and global copper leads Indian metal equities
- Watch next: usd_mxn (up) — already moved; Oil price surge and US Federal Reserve decision
- Watch next: usd_brl (up) — already moved; Oil price surge and US Federal Reserve decision
- Source: Digital euro app to incorporate highest accessibility standards — ECB press, 2026-07-30. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260730~3b3bfbb565.en.html
- Source: Euro zone bonds snap three-day rally, yields rise with oil — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-snap-three-day-rally-yields-rise-with-oil/articleshow/132712805.cms
- Source: Euro zone bond rally ends as oil surge, Fed decision weigh on investors — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-rally-ends-as-oil-surge-fed-decision-weigh-on-investors/articleshow/132706628.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-19 (d=0.34), 2025-03-31 (d=0.34)

### [RED 6.74] cross-asset · 5 series ↑
- cac_40 [INDICES]: last 8567.07, z20 2.81, zc 1.07, resid-z -0.10 [quiet], 1d 0.96%, |z20|=2.81; 1y-pct=99
- stoxx_50 [INDICES]: last 6417.38, z20 2.51, zc 1.09, resid-z 0.41 [quiet], 1d 1.15%, |z20|=2.51; 1y-pct=100
- ftse_100 [INDICES]: last 10982.78, z20 2.51, zc 1.35, resid-z -1.28 [quiet], 1d 0.78%, |z20|=2.51; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.52, z20 2.26, zc 0.49, resid-z 0.09 [quiet], 1d 1.12%, |z20|=2.26; 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- dax [INDICES]: last 25871.79, z20 2.21, zc 1.15, resid-z -0.72 [quiet], 1d 1.01%, |z20|=2.21; 1y-pct=100
- **Mechanism**: The recent move in global indices and commodities, particularly copper, is driven by the anticipation of the Federal Reserve's interest rate decision and the easing of supply constraints in China. The metal_copper_channel, which is VALID, suggests that global copper prices lead Indian metal equities, potentially influencing the Indian market. The vix_equity_inverse channel, also VALID, indicates a strong inverse relationship between volatility and equity prices, which could contribute to the current market sentiment.
- **Gap**: No gap: the recent move in global indices and commodities is largely priced in, with resid_z values close to zero for most series, indicating that the current prices are largely explained by factor exposures.
- **India take**: The Indian market, as represented by the Nifty 50 and Nifty Midcap 100, has already reacted to the global developments, with both indices showing a positive correlation with global indices. The metal_copper_channel may continue to influence the Indian market, particularly metal equities.
- Watch next: nifty_50 (up) — already moved; reacted to global indices
- Watch next: nifty_midcap_100 (up) — already moved; reacted to global indices
- **India receivers**: nifty_50 (rho 0.55, z 1.49); nifty_midcap_100 (rho 0.533, z 1.15)
- Source: Copper slips ahead of Fed rate decision, aluminium rises on Gulf fighting — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/commodities/news/copper-slips-ahead-of-fed-rate-decision-aluminium-rises-on-gulf-fighting/articleshow/132712953.cms
- Historical analogues: 2025-04-17 (d=0.49), 2024-10-03 (d=0.59), 2025-04-01 (d=0.72)

### [AMBER 5.91] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.20, z20 1.98, zc 3.20, resid-z 2.97 [unexplained], 1d 2.16%, |z20|=1.98; 1y-pct=100
- ust_10y [RATES]: last 4.67, z20 1.32, zc 1.37, resid-z 1.42 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.41, z20 1.17, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.80, z20 -0.97, zc 0.19, resid-z -0.31 [quiet], 1d 0.06%, 1y-pct=2
- ust_2y [RATES]: last 4.22, z20 0.06, zc -0.73, resid-z -0.50 [quiet], 1d -0.94%, 1y-pct=96
- **Mechanism**: The recent move in US Treasury yields, particularly the 30-year yield, is driven by unexplained factors as evidenced by a high resid_z of 2.97. This move is likely to propagate through the valid gold_silver_comove and metal_copper_channel, influencing Indian metal equities. However, the weak inr_oil_channel and dxy_inr_channel may limit the transmission of global yield moves to Indian markets.
- **Gap**: No gap: The move in US Treasury yields is largely priced, with a big raw move accompanied by a small resid_z in most series, indicating that the market has already adjusted to the new yield levels.
- **India take**: The Indian 6.94 per cent 2036 bond yield is expected to move in the range of 6.80 per cent-6.84 per cent, and the recent move in US Treasury yields may influence Indian metal equities through the metal_copper_channel. However, the impact on Indian markets is likely to be limited due to the weak inr_oil_channel and dxy_inr_channel.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment and potential safe-haven bid in gold may lead to a decline in Indian equities.
- Watch next: usd_inr (up) — not yet - watch; Weakening INR due to potential import bill pressures from higher oil prices.
- Source: India bond traders seen leaning bearish in early trade with eyes on fresh supply — BusinessLine Mkts, 2026-07-31. https://www.thehindubusinessline.com/markets/india-bond-traders-seen-leaning-bearish-in-early-trade-with-eyes-on-fresh-supply/article71288940.ece
- Source: UK bond yields and sterling dip after BoE holds rates steady — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-and-sterling-dip-after-boe-holds-rates-steady/articleshow/132740517.cms
- Source: TREASURY YIELDS HIT 19-YEAR HIGH US Treasury yields climbed after the Federal Reserve held interest rates, with the 30-year yield reaching a 19-year high of 5.24%. Three Fed officials dissented in favor of a rate hike, highlighting concerns over persistent inflation. The — DeItaone, 2026-07-30. https://t.me/walter_bloomberg/34086
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.89] dyn_thangamayl_ns ↓
- dyn_thangamayl_ns [EQUITIES]: last 5226.50, z20 -3.89, zc -1.06, resid-z -2.26 [unexplained], 1d -10.00%, |z20|=3.89
- **Mechanism**: dyn_thangamayl_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Thangamayil Jewellery shares crash 19% in 2 days on weak Q2 outlook. What did the company say? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/thangamayil-jewellery-shares-crash-19-in-2-days-on-weak-q2-outlook-what-did-the-company-say/articleshow/132728014.cms
- Source: Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹695 cr profit, Asian Paints, Adani Ports, Colgate, V-Guard Q1 profit rise, Thangamayil Jewellery shares tank 10% after results; Eicher Motors PAT up 21%, Waaree Energies' rise 15%, Dabur's up 15%, ACME Solar con. profit zooms 80% — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-adani-enterprises-adani-ports-asian-paints-eicher-motors-waaree-energies-colgate-prestige-estates-syrma-sgs-tech-dabur-hexaware-tech-vedanta-oil-acme-results-29-july-2026/article71276282.ece
- Source: Q1 Results Today Live: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹695 cr profit, Asian Paints, Adani Ports, Colgate, V-Guard Q1 profit rise, Thangamayil Jewellery shares tank 10% after results; Eicher Motors, Waaree Energies, Prestige Estates, Dabur, ACME Solar to announce Q1 results — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-adani-enterprises-adani-ports-asian-paints-eicher-motors-waaree-energies-colgate-prestige-estates-syrma-sgs-tech-dabur-hexaware-tech-vedanta-oil-acme-results-29-july-2026/article71276282.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-29 (d=0.01), 2026-06-11 (d=0.01)

### [RED 5.65] cross-asset · 2 series ↑
- dyn_jiofin_bo [EQUITIES]: last 251.60, z20 2.81, zc 0.98, resid-z 1.06 [quiet], 1d 2.07%, |z20|=2.81
- nifty_midcap_100 [INDICES]: last 62987.60, z20 1.15, zc 0.62, resid-z 0.30 [quiet], 1d 0.51%, 1y-pct=99
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-15 (z-distance 0.22).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.838 via dyn_jiofin_bo, z 1.49, reacted); dyn_indianb_ns (rho 0.636 via nifty_midcap_100, z 0.56, quiet); dyn_indusindbk_bo (rho 0.622 via nifty_midcap_100, z -0.13, quiet); nifty_metal (rho 0.619 via nifty_midcap_100, z 2.06, reacted); dyn_bharatcoal_ns (rho 0.579 via nifty_midcap_100, z -1.61, reacted)
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.56 vs dyn_jiofin_bo, historically leads by 1d
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.556 vs dyn_jiofin_bo
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.548 vs dyn_jiofin_bo
- **India receivers**: nifty_50 (rho 0.838, z 1.49); dyn_indianb_ns (rho 0.636, z 0.56); dyn_indusindbk_bo (rho 0.622, z -0.13); nifty_metal (rho 0.619, z 2.06)
- Source: Amazon Web Services India net profit jumps over 10-fold to Rs 242 cr in FY26 — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/earnings/amazon-web-services-india-net-profit-jumps-over-10-fold-to-rs-242-cr-in-fy26/articleshow/132715491.cms
- Historical analogues: 2025-07-15 (d=0.22), 2024-10-01 (d=0.26), 2025-05-30 (d=0.49)

### [AMBER 5.38] wti ↑
- wti [COMMODITIES]: last 82.04, z20 0.38, zc -0.51, resid-z 0.47 [quiet], 1d -1.85%, 1-session move -1.85% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.5 via wti, z 1.15, reacted); midcap_largecap_ratio (rho -0.422 via wti, z -0.37, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.968 vs wti
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.595 vs wti
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.555 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.5, z 1.15); midcap_largecap_ratio (rho -0.422, z -0.37)
- Source: Crude oil futures fall 3% to ₹7,811/barrel amid easing supply concerns — BusinessLine Mkts, 2026-07-31. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-fall-3-to-7811barrel-amid-easing-supply-concerns/article71289334.ece
- Source: Oil companies are expected to reap big profits because of US-Iran conflict — BusinessLine Mkts, 2026-07-31. https://www.thehindubusinessline.com/markets/commodities/oil-companies-are-expected-to-reap-big-profits-because-of-us-iran-conflict/article71289246.ece
- Source: Caspian Oil Pipeline Shuts Down Again After Black Sea Drone Attack — OilPrice, 2026-07-31. https://oilprice.com/Latest-Energy-News/World-News/Caspian-Oil-Pipeline-Shuts-Down-Again-After-Black-Sea-Drone-Attack.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.0), 2025-10-22 (d=0.01)

### [RED 5.2] usd_jpy ↓
- usd_jpy [FX]: last 160.31, z20 -3.20, zc -5.78, resid-z -5.40 [unexplained], 1d -1.83%, |z20|=3.20
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.514 vs usd_jpy, historically leads by 1d
- Watch next: kospi (inverse) — not yet - watch; rho -0.619 vs usd_jpy
- Source: Global Market | A history of Japan's biggest interventions to support the yen — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-a-history-of-japans-biggest-interventions-to-support-the-yen/articleshow/132759149.cms
- Source: Global Market: Weak yen lifts Japan's forex reserve surplus to $31 billion in FY25 — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-weak-yen-lifts-japans-forex-reserve-surplus-to-31-billion-in-fy25/articleshow/132755944.cms
- Source: Global Market: BOJ keeps rates unchanged, signals readiness for further hikes as yen remains under pressure — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-boj-keeps-rates-unchanged-signals-readiness-for-further-hikes-as-yen-remains-under-pressure/articleshow/132755708.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

## Watchlist (below surfacing floor)
dyn_meta ↓ (4.88), gold_silver_ratio ↑ (3.94), dyn_cupid_ns ↑ (3.89), usd_cny ↓ (3.76), dyn_lth ↑ (3.45), dyn_tech ↑ (3.37), hy_oas ↑ (3.22), ust_2s10s ↑ (3.09), dyn_aapl ↑ (2.99), dyn_bac ↑ (2.96), dyn_icicigi_bo ↓ (2.92), dyn_301077_sz ↓ (2.79)

## India macro
- nifty_50: 24395.5996 (1d 0.32%, z20 1.49, flag none)
- nifty_midcap_100: 62987.6016 (1d 0.51%, z20 1.15, flag amber)
- usd_inr: 95.4300 (1d -0.31%, z20 -1.19, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5819 (1d 0.19%, z20 -0.37, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.3 — "Stock recommendations for 31 July from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 73.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 3"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 69.8 — "Stock recommendations for 31 July from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 67.3 — "Stock recommendations for 31 July from MarketSmith India"
- BAC (Bank of America Corporation) score 59.0 — "Axis Bank Share Price Live Updates: Axis Bank  Records Small Drop"
- HDB (HDFC Bank Limited) score 56.6 — "HDFC Life Share Price Live Updates: HDFC Life's Daily Performance Update"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.2 — "HCL Tech Share Price Live Updates: HCL Tech's Financial Snapshot"
- COIN (Coinbase Global, Inc.) score 54.7 — "Gift Nifty signals 100-point gap-up amid strong global cues"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 54.4 — "Axis Bank Share Price Live Updates: Axis Bank  Records Small Drop"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.0 — "HCL Tech Share Price Live Updates: HCL Tech's Financial Snapshot"
- IDBI.NS (IDBI BANK LIMITED) score 53.3 — "Axis Bank Share Price Live Updates: Axis Bank  Records Small Drop"
- OHI (Omega Healthcare Investors, In) score 52.5 — "Fusion Klassroom Edutech raises ₹11.08 crore from anchor investors ahead of IPO"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 49.0 — "Axis Bank Share Price Live Updates: Axis Bank  Records Small Drop"
- TECH (Bio-Techne Corp) score 37.8 — "HCL Tech Share Price Live Updates: HCL Tech's Financial Snapshot"
- CHKP (Check Point Software Technolog) score 32.1 — "Stocks to watch: Maruti Suzuki, IOC, Tata Steel among shares in focus today; check list he"
- LTH (Life Time Group Holdings, Inc.) score 27.3 — "MV Electrosystems IPO Day 2: GMP jumps, indicating 30% listing gains; issue subscribed 3.6"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.6 — "Juniper Green Energy IPO Day 2: GMP at 4%; Check subscription status and key details. Shou"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.4 — "India bond traders seen leaning bearish in early trade with eyes on fresh supply"
- 301077.SZ (CHINASTARS) score 20.5 — "How China Became the Ultimate Swing Oil Buyer"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 19.6 — "Adani Energy plans another share sale by early next fiscal year"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.9 — "Stocks to watch: Maruti Suzuki, IOC, Tata Steel among shares in focus today; check list he"
- MS (Morgan Stanley) score 15.0 — "M&M shares climb 3% after strong Q1 results. Morgan Stanley sees up to 29% upside scope"
- MSFT (Microsoft Corporation) score 12.3 — "Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter"
- JIOFIN.BO (Jio Financial Services Limited) score 11.7 — "HCL Tech Share Price Live Updates: HCL Tech's Financial Snapshot"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.7 — "The U.S. Just Took A Big Step to Break China's Magnet Dominance"
- META (Meta) score 10.7 — "Global Market: China's factory activity contracts unexpectedly in July; metal, commodity s"
- INFY (Infosys Limited) score 10.6 — "Kospi’s mammoth 17% surge spells caution for Indian IT stocks. Why TCS, Infosys, others ar"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.6 — "HCL Tech Share Price Live Updates: HCL Tech's Financial Snapshot"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.4 — "Market wrap: M&M, Coal India, Adani Ports among top gainers and losers on Nifty and Sensex"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.0 — "Penny stock under  ₹10 PC Jeweller pares early losses, jumps around 3% from today's low; h"
- AAPL (Apple Inc.) score 7.2 — "APPLE BEATS ESTIMATES ON IPHONE, MAC STRENGTH Results EPS: $2.02 ($1.91 ex-tariff refunds)"
- GS (Goldman Sachs Group, Inc. (The) score 6.7 — "Goldman Sachs Asset Management launches AI investment platform: Report"
- VT (Vanguard Total World Stock Ind) score 6.6 — "The World Cup winners wore Adidas shirts. But the company’s investors are still crying fou"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.9 — "Higher oil prices could push Fed to resume rate hikes later this year: ICICI Bank report"
- NVDA (NVIDIA Corporation) score 5.2 — "Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor"
- ETERNAL.NS (ETERNAL LIMITED) score 4.5 — "Zepto IPO hurdle revives investor interest in Swiggy, Eternal; shares set for best month i"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.5 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- WAAREEENER.BO (Waaree Energies Limited) score 3.1 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- CUPID.NS (CUPID LIMITED) score 1.6 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.2 — "Mukul Agrawal-portfolio multibagger stock LT Foods jumps 5% after Q1 results; details here"

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