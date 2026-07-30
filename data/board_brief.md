# Transmission Layer — board brief · 2026-07-30 21:54Z

data as of **2026-07-30** · 98 series · 16 red / 35 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.435, 1d in regime; vol-pct 0.458, breadth-off 0.412, Markov P(high-vol) 0.313)
- [INVERTED] **safe_haven_gold** — corr20 -0.57, corr60 -0.47, contra nifty_50 corr20=0.22, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.82, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.31, corr60 0.32, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.02, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.84, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.03, corr60 -0.04, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.17, corr60 -0.24, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.25, corr60 0.19, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **9 of 90** scanned series survive multiplicity control (effective p ≤ 0.009322376047437464)
- **SETUP** nasdaq_100 → dyn_453950_ks: leads 1d (ccf 0.599, β 0.8746, p 0.0); driver zc 2.28 → expected 2.919%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.581, β 0.4651, p 0.0); driver zc 2.36 → expected 0.984%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.579, β 0.4466, p 0.0); driver zc 1.81 → expected 0.741%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.547, β 1.1086, p 0.0); driver zc 2.36 → expected 2.345%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → dyn_453950_ks: leads 1d (ccf 0.541, β 1.0553, p 0.0); driver zc 1.81 → expected 1.751%. Type hit-rate 0.811 (n=3158).
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.541, β 0.6269, p 0.0); driver zc 2.28 → expected 2.092%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.525, β 0.8607, p 0.0); driver zc 2.36 → expected 1.821%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.514, β 0.8163, p 0.0); driver zc 1.81 → expected 1.354%. Type hit-rate 0.811 (n=3158).
- **SETUP** nasdaq_100 → asx_200: leads 1d (ccf 0.507, β 0.293, p 0.0); driver zc 2.28 → expected 0.978%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.504, β 0.2072, p 0.0); driver zc 1.62 → expected 0.714%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → asx_200: leads 1d (ccf -0.491, β -0.0417, p 0.0); driver zc -1.64 → expected 0.723%. Type hit-rate 0.811 (n=3158).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.471, β 0.5947, p 0.0); driver zc 2.28 → expected 1.985%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.463, β 0.8227, p 0.0); driver zc 2.36 → expected 1.74%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.46, β 0.7819, p 0.0); driver zc 1.81 → expected 1.297%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_infy → nifty_it: leads 1d (ccf 0.446, β 0.3353, p 0.0); driver zc -1.68 → expected -1.703%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_ms → dyn_453950_ks: leads 1d (ccf 0.424, β 0.4503, p 0.0); driver zc 1.62 → expected 1.552%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.412, β -0.0708, p 5e-05); driver zc -1.64 → expected 1.227%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.407, β 0.8764, p 0.0); driver zc 2.36 → expected 1.854%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → dyn_453950_ks: leads 1d (ccf -0.402, β -0.0855, p 0.00098); driver zc -1.64 → expected 1.481%. Type hit-rate 0.811 (n=3158).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.397, β 0.615, p 0.0); driver zc 2.28 → expected 2.052%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.394, β 0.3298, p 0.0); driver zc 1.62 → expected 1.137%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.388, β 0.3536, p 0.0); driver zc 1.62 → expected 1.219%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.364, β 0.7561, p 0.0); driver zc 1.81 → expected 1.254%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.361, β -2.4545, p 0.00539); driver zc 2.36 → expected -5.192%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.359, β -0.0666, p 0.00773); driver zc -1.64 → expected 1.153%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.341, β 0.5382, p 0.0); driver zc 2.36 → expected 1.138%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → kospi: leads 1d (ccf -0.334, β -0.0756, p 2e-05); driver zc -1.64 → expected 1.31%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → india_vix: leads 1d (ccf 0.324, β 0.2088, p 0.01153); driver zc -1.64 → expected -3.618%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.311, β 0.4773, p 0.00018); driver zc 1.81 → expected 0.792%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_ms → kospi: leads 1d (ccf 0.301, β 0.3389, p 0.0); driver zc 1.62 → expected 1.168%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.297, β 0.3639, p 0.0); driver zc 2.36 → expected 0.77%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → nifty_metal: leads 1d (ccf -0.296, β -0.0442, p 0.00037); driver zc -1.64 → expected 0.766%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_infy → dyn_techm_ns: leads 1d (ccf 0.28, β 0.2386, p 0.0); driver zc -1.68 → expected -1.212%. Type hit-rate 0.811 (n=3158).
- **SETUP** nasdaq_100 → nifty_metal: leads 1d (ccf 0.277, β 0.3109, p 0.00047); driver zc 2.28 → expected 1.038%. Type hit-rate 0.811 (n=3158).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.272, β 0.3244, p 0.0); driver zc 1.81 → expected 0.538%. Type hit-rate 0.811 (n=3158).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.265, β 0.3784, p 0.0); driver zc 2.36 → expected 0.8%. Type hit-rate 0.811 (n=3158).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.252, β -0.0292, p 8e-05); driver zc -1.64 → expected 0.505%. Type hit-rate 0.811 (n=3158).
- Track record · residual_reversion: hit-rate **0.492** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.811** (n=3158) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 14.33] cross-asset · 5 series ↑
- dyn_msft [EQUITIES]: last 451.48, z20 10.39, zc 9.76, resid-z 0.08 [moved], 1d 15.60%, |z20|=10.39
- eur_usd [FX]: last 1.15, z20 4.51, zc 3.85, resid-z 4.40 [unexplained], 1d 1.25%, |z20|=4.51
- usd_jpy [FX]: last 159.59, z20 -4.22, zc -8.44, resid-z -8.22 [unexplained], 1d -2.61%, |z20|=4.22
- usd_mxn [FX]: last 17.32, z20 -2.33, zc -1.44, resid-z -1.81 [unexplained], 1d -0.64%, |z20|=2.33
- aud_usd [FX]: last 0.70, z20 1.96, zc 1.61, resid-z 2.15 [unexplained], 1d 0.76%, |z20|=1.96
- **Mechanism**: The recent surge in the yen against the US dollar, reportedly due to Japan's intervention in the market, has triggered a cross-asset move. This move is propagated through the FX channels, particularly in eur_usd, usd_jpy, usd_mxn, and aud_usd, which have shown unexplained moves. However, the big raw moves in these FX pairs have small resid_z values, indicating that they are largely priced in.
- **Gap**: No gap: the big raw moves in FX pairs have small resid_z values, indicating that they are largely priced in
- **India take**: The Indian instrument eur_inr has reacted to the move in eur_usd, while dyn_thangamayl_ns has reacted to the move in dyn_msft. Further reactions can be expected in these instruments.
- Watch next: dyn_msft (down) — already moved; high z20 level
- Watch next: eur_usd (down) — not yet - watch; unexplained move
- Watch next: usd_jpy (up) — not yet - watch; unexplained move
- Watch next: usd_mxn (up) — not yet - watch; unexplained move
- Watch next: aud_usd (down) — not yet - watch; unexplained move
- **India receivers**: eur_inr (rho 0.366, z 1.53); dyn_thangamayl_ns (rho -0.362, z -2.53)
- Source: Yen Surges as Nikkei Says Japan Intervened in Market Again — Mint Markets, 2026-07-30. https://www.livemint.com/market/yen-surges-as-nikkei-says-japan-intervened-in-market-again-11785446408826.html
- Source: Micron, Sandisk and other chip stocks get major boosts in the wake of Microsoft’s earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/micron-sandisk-and-other-chip-stocks-get-major-boosts-in-the-wake-of-microsofts-earnings-25460e61?mod=mw_rss_topstories
- Source: Why Microsoft’s stock soared to a historic gain after earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/why-microsofts-stock-is-soaring-toward-a-historic-gain-after-earnings-96cd5b1e?mod=mw_rss_topstories
- Historical analogues: 2025-04-02 (d=0.53), 2025-08-15 (d=0.57), 2025-10-30 (d=0.58)

### [RED 6.83] dxy ↓
- dxy [FX]: last 100.01, z20 -3.83, zc -2.36, resid-z -3.79 [unexplained], 1d -0.78%, 20d range extreme; |z20|=3.83
- **Mechanism**: The recent decline in the US Dollar Index (DXY) is a priced move with a small resid_z, indicating that it is largely explained by factor exposures. The move may propagate through the VALID gold_silver_comove channel, as monetary metals tend to co-move. However, the INVERTED safe_haven_gold channel suggests that the traditional risk-off safe-haven bid for gold may not be in play.
- **Gap**: No gap: the move in DXY is largely priced, with a small resid_z of -0.17
- **India take**: The Indian instrument that expresses this move is likely to be the USDINR, which may weaken due to the decline in DXY. However, the WEAK dxy_inr_channel suggests that this transmission may not be robust.
- Watch next: ust_2y (down) — not yet - watch; historically leads DXY by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 6.42] cross-asset · 6 series ↑
- comex_copper [COMMODITIES]: last 6.50, z20 2.27, zc 1.61, resid-z 0.71 [priced], 1d 3.62%, |z20|=2.27; 1y-pct=97; co-occur[metal_copper] same-direction (channel VALID)
- ftse_100 [INDICES]: last 10886.25, z20 2.09, zc -0.30, resid-z -1.36 [quiet], 1d -0.20%, |z20|=2.09; 1y-pct=99
- comex_gold [COMMODITIES]: last 4162.80, z20 1.58, zc 2.38, resid-z -0.45 [priced], 1d 3.17%, |z20|=1.58
- cac_40 [INDICES]: last 8476.16, z20 1.41, zc 0.92, resid-z -0.17 [quiet], 1d 0.81%, 1y-pct=96
- dax [INDICES]: last 25574.62, z20 1.25, zc 0.49, resid-z -0.83 [quiet], 1d 0.45%, 1y-pct=98
- stoxx_50 [INDICES]: last 6334.67, z20 0.91, zc 1.48, resid-z 0.28 [quiet], 1d 1.37%, 1y-pct=98
- **Mechanism**: The recent surge in COMEX gold and copper prices, driven by softer US inflation and a decline in the US dollar index, has created a ripple effect across global markets. The VALID metal_copper_channel and gold_silver_comove channels are transmitting this move to Indian metal equities and gold prices. However, the INVERTED safe_haven_gold channel suggests that the risk-off safe-haven bid for gold may be weakening, potentially limiting the upside for gold prices.
- **Gap**: No gap: the recent price move in COMEX gold and copper is largely priced in, with resid_z values of 0.71 and -0.45, respectively, indicating that the move is largely explained by factor exposures.
- **India take**: Indian gold prices have reacted to the global move, with prices rising across all cities. The Nifty 50 has also moved in tandem with the global markets, while the Nifty Midcap 100 is still waiting to react.
- Watch next: nifty_50 (up) — already moved; rho=0.549 via cac_40
- Watch next: nifty_midcap_100 (up) — not yet - watch; rho=0.536 via dax
- **India receivers**: nifty_50 (rho 0.549, z 1.01); nifty_midcap_100 (rho 0.536, z 0.51)
- Source: Gold, silver prices today: Comex gold jumps $144, silver gains $1 as softer US inflation dents dollar — Mint Markets, 2026-07-30. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-jumps-144-silver-gains-1-as-softer-us-inflation-dents-dollar-11785426931282.html
- Source: Gold futures slip to ₹1.41 lakh/10g on firm US dollar — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/gold/gold-futures-slip-to-141-lakh10g-on-firm-us-dollar/article71284840.ece
- Source: Today’s Gold Rate in India July 30: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-july-30-2026/article71284521.ece
- Historical analogues: 2026-03-31 (d=0.78), 2025-07-28 (d=0.87), 2024-11-07 (d=0.88)

### [AMBER 5.91] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.20, z20 1.98, zc 3.40, resid-z 2.97 [unexplained], 1d 2.16%, |z20|=1.98; 1y-pct=100
- ust_10y [RATES]: last 4.67, z20 1.32, zc 1.37, resid-z 1.42 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.41, z20 1.17, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.80, z20 -0.97, zc 0.19, resid-z -0.31 [quiet], 1d 0.06%, 1y-pct=2
- ust_2y [RATES]: last 4.22, z20 0.06, zc -0.73, resid-z -0.50 [quiet], 1d -0.94%, 1y-pct=96
- **Mechanism**: The recent move in US bond yields, particularly the 30-year yield, is driven by the market's expectation of future rate hikes, as signaled by the US Fed. This move is largely priced in, with a high z-score and a relatively low resid_z, indicating that the market has already factored in the expected rate hikes. The mechanism for this move is the transmission of global monetary policy to the Indian market, particularly through the metal_copper_channel and the gold_silver_comove channels, which are currently valid.
- **Gap**: No gap: The move in US bond yields is largely priced in, with a high z-score and a relatively low resid_z, indicating that the market has already factored in the expected rate hikes.
- **India take**: The Indian market, particularly the Nifty 50, may react to the expected rate hikes in the US, potentially leading to a decline in the index. The metal_copper_channel and the gold_silver_comove channels may also influence the Indian market, particularly the metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment and potential strengthening of the US dollar could lead to a decline in the Nifty 50
- Source: UK bond yields and sterling dip after BoE holds rates steady — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-and-sterling-dip-after-boe-holds-rates-steady/articleshow/132740517.cms
- Source: TREASURY YIELDS HIT 19-YEAR HIGH US Treasury yields climbed after the Federal Reserve held interest rates, with the 30-year yield reaching a 19-year high of 5.24%. Three Fed officials dissented in favor of a rate hike, highlighting concerns over persistent inflation. The — DeItaone, 2026-07-30. https://t.me/walter_bloomberg/34086
- Source: Sensex, Nifty 50 rise, but mid, small-caps falter; rising US bond yields keep investors cautious — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/sensex-nifty-50-rise-but-mid-small-caps-falter-rising-us-bond-yields-keep-investors-cautious-11785405396383.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.9] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 40010.41, z20 -2.58, zc -0.02, resid-z -0.23 [quiet], 1d -0.07%, |z20|=2.58
- kospi [INDICES]: last 5609.33, z20 -2.28, zc -0.16, resid-z -0.55 [quiet], 1d -0.95%, |z20|=2.28
- nikkei_225 [INDICES]: last 61807.90, z20 -2.15, zc 0.26, resid-z -0.00 [quiet], 1d 0.61%, |z20|=2.15
- **Mechanism**: The decline in global indices, including Taiwan Weighted, Kospi, and Nikkei 225, is driven by a combination of factors, including geopolitical tensions in the Middle East and a selloff in AI and chip-related stocks. The sharp move in the yen, following reports of Japan's intervention in the currency market, has also contributed to the decline. The transmission of these global market moves to Indian equities is facilitated by the verified transmission setups, including the lead-lag relationships between Nasdaq 100, SP500, and Taiwanese and Japanese indices.
- **Gap**: No gap: the moves in global indices are largely priced, with small resid_z values indicating that the declines are largely explained by factor exposures
- **India take**: Indian metal equities, such as Nifty Metal, and banking stocks, such as HDFC Bank, have already reacted to the global market moves. The Nifty Midcap 100 index, however, remains quiet, and its reaction to the global market decline is worth watching.
- Watch next: nifty_metal (down) — already moved; reacted to Kospi move
- Watch next: dyn_hdbfs_bo (down) — already moved; reacted to Nikkei 225 move
- **India receivers**: dyn_hdbfs_bo (rho 0.481, z -1.74); nifty_metal (rho 0.441, z 1.56); dyn_techm_ns (rho -0.421, z 2.13); dyn_pcjeweller_ns (rho 0.412, z -1.59)
- Source: Yen Surges as Nikkei Says Japan Intervened in Market Again — Mint Markets, 2026-07-30. https://www.livemint.com/market/yen-surges-as-nikkei-says-japan-intervened-in-market-again-11785446408826.html
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html

### [RED 5.4] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 31188.45, z20 2.57, zc 0.12, resid-z 0.23 [quiet], 1d 0.21%, |z20|=2.57
- dyn_techm_ns [EQUITIES]: last 1669.00, z20 2.13, zc 0.79, resid-z 0.71 [quiet], 1d 1.51%, |z20|=2.13
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.674 via nifty_it, z 0.49, quiet)
- Watch next: dyn_tataelxsi_ns (co-move) — not yet - watch; rho 0.674 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.674, z 0.49)
- Source: Mahindra Q1 net profit rises 34%, standalone earnings beat estimates — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-q1-net-profit-rises-34-standalone-earnings-beat-estimates/articleshow/132750115.cms
- Source: SML Mahindra shares rally over 18% on acquisition of M&M’s truck division. What it means for shareholders? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-shares-rally-over-18-on-acquisition-of-mahindra-mahindras-truck-and-bus-division-what-does-it-mean-for-shareholders/articleshow/132729786.cms
- Source: SML Mahindra to acquire Mahindra Truck and Bus division in commercial vehicle consolidation — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-to-acquire-mahindra-truck-and-bus-division-in-commercial-vehicle-consolidation/articleshow/132709583.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 4.88] dyn_meta ↓
- dyn_meta [EQUITIES]: last 539.06, z20 -2.88, zc -3.29, resid-z 1.11 [moved], 1d -7.95%, |z20|=2.88; 1y-pct=1
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.455 via dyn_meta, z 0.51, quiet); dyn_hdbfs_bo (rho 0.399 via dyn_meta, z -1.74, reacted); midcap_largecap_ratio (rho 0.39 via dyn_meta, z -0.52, quiet); dyn_eternal_ns (rho 0.388 via dyn_meta, z 2.6, reacted); dyn_techm_ns (rho -0.361 via dyn_meta, z 2.13, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.455, z 0.51); dyn_hdbfs_bo (rho 0.399, z -1.74); midcap_largecap_ratio (rho 0.39, z -0.52); dyn_eternal_ns (rho 0.388, z 2.6)
- Source: Meta’s stock falls hard. Here’s why the company is in Wall Street’s doghouse. — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/metas-stock-is-falling-hard-heres-why-the-company-is-in-wall-streets-doghouse-afae2f55?mod=mw_rss_topstories
- Source: Microsoft jumps over 15% after results, Meta sinks 9% as AI concerns weigh investor sentiment — What we know — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/meta-sinks-9-pc-microsoft-jumps-15-pc-results-earnings-us-tech-stocks-invest-artificial-intelligence-ai-concern-business-11785418926072.html
- Source: META - EVERCORE REMOVES META FROM TOP PICK LIST Evercore ISI removed Meta from its TAP Outperform List but maintained an Outperform rating, cutting its price target to $820 from $930. The firm cited rising AI spending, limited visibility on future capex, and a lack of clear — DeItaone, 2026-07-30. https://t.me/walter_bloomberg/34078
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [RED 4.6] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 310.20, z20 2.60, zc -0.22, resid-z -0.58 [quiet], 1d -0.51%, |z20|=2.60
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.556 via dyn_eternal_ns, z 0.51, quiet); dyn_jiofin_bo (rho 0.422 via dyn_eternal_ns, z 1.93, reacted); nifty_50 (rho 0.404 via dyn_eternal_ns, z 1.01, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.556 vs dyn_eternal_ns, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.556, z 0.51); dyn_jiofin_bo (rho 0.422, z 1.93); nifty_50 (rho 0.404, z 1.01)
- Source: Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/eternal-shares-jump-over-20-in-one-month-will-the-stock-cross-its-october-peak-of-rs-368/articleshow/132700500.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

## Watchlist (below surfacing floor)
dyn_waareeener_bo ↓ (4.57), dyn_thangamayl_ns ↓ (4.53), dyn_cupid_ns ↑ (3.75), gold_silver_ratio ↑ (3.7), dyn_lth ↑ (3.45), dyn_tech ↑ (3.37), dyn_301077_sz ↓ (3.27), hy_oas ↑ (3.22), usd_cny ↓ (3.17), vix ↓ (3.09), ust_2s10s ↑ (3.09), dyn_aapl ↑ (2.99)

## India macro
- nifty_50: 24296.5996 (1d 0.19%, z20 1.01, flag none)
- nifty_midcap_100: 62668.9492 (1d -0.28%, z20 0.51, flag amber)
- usd_inr: 95.6700 (1d 0.07%, z20 -0.67, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5793 (1d -0.47%, z20 -0.52, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 75.0 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.9 — "Maruti Q1 Results Preview: What could lead to a profit decline for India's largest carmake"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 62.8 — "Maruti Q1 Results Preview: What could lead to a profit decline for India's largest carmake"
- BAC (Bank of America Corporation) score 61.9 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- COALINDIA.NS (COAL INDIA LTD) score 60.0 — "Maruti Q1 Results Preview: What could lead to a profit decline for India's largest carmake"
- HDB (HDFC Bank Limited) score 58.1 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.8 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- IDBI.NS (IDBI BANK LIMITED) score 55.6 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.4 — "Mahindra Q1 net profit rises 34%, standalone earnings beat estimates"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.9 — "Get ready to buy the dip in tech stocks. Why the recent selling won’t break the bull marke"
- OHI (Omega Healthcare Investors, In) score 51.4 — "Warsh’s Wall Street cred takes a hit as investors doubt the Fed chair’s inflation-fighting"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 50.9 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- COIN (Coinbase Global, Inc.) score 49.4 — "Commodity experts, policymakers to brainstorm at 3-day Global Commodity Conclave in Mumbai"
- TECH (Bio-Techne Corp) score 34.1 — "Get ready to buy the dip in tech stocks. Why the recent selling won’t break the bull marke"
- LTH (Life Time Group Holdings, Inc.) score 29.1 — "Study moots phased time-bound reduction of import duty on aluminium to zero"
- CHKP (Check Point Software Technolog) score 28.8 — "US stocks: Microsoft adds $485 billion to investors' wealth as shares rise 15%. Check why"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.0 — "John Kerry: Europe's Energy Crisis Is a Bigger Threat Than Any Weapon"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.8 — "India bonds slip on Fed uncertainty, war worries"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 20.5 — "Market wrap: M&M, Coal India, Adani Ports among top gainers and losers on Nifty and Sensex"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.6 — "Tata Steel Q1 net profit beats estimates; approves Rs 33,873 crore capex"
- 301077.SZ (CHINASTARS) score 16.0 — "China’s Trade With Central Asia Surges 6.5%"
- MS (Morgan Stanley) score 15.5 — "Investors are overlooking healthcare stocks and should consider these top picks, says JPMo"
- MSFT (Microsoft Corporation) score 12.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends sharply higher as Microso"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.7 — "HASSETT: THINK WARSH’S JOB JUST GOT A BIT EASIER WITH TODAY’S INFLATION DATA"
- META (Meta) score 10.7 — "Meta’s stock falls hard. Here’s why the company is in Wall Street’s doghouse."
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.4 — "Market wrap: M&M, Coal India, Adani Ports among top gainers and losers on Nifty and Sensex"
- INFY (Infosys Limited) score 9.5 — "Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty end"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.8 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- JIOFIN.BO (Jio Financial Services Limited) score 8.5 — "My financial adviser says I don’t need a tax-efficient withdrawal plan for my $2.3 million"
- GS (Goldman Sachs Group, Inc. (The) score 7.4 — "Goldman Sachs Asset Management launches AI investment platform: Report"
- VT (Vanguard Total World Stock Ind) score 7.3 — "The World Cup winners wore Adidas shirts. But the company’s investors are still crying fou"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.2 — "My financial adviser says I don’t need a tax-efficient withdrawal plan for my $2.3 million"
- NVDA (NVIDIA Corporation) score 5.8 — "Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor"
- AAPL (Apple Inc.) score 5.7 — "Qualcomm shares fall 5% as higher costs, Apple-related weakness cloud profit forecast"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.4 — "ICICI Prudential MF buys stake in Go Digit General Insurance for ₹139 crore"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.9 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- ETERNAL.NS (ETERNAL LIMITED) score 3.9 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- WAAREEENER.BO (Waaree Energies Limited) score 3.5 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- CUPID.NS (CUPID LIMITED) score 1.7 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.2 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "

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