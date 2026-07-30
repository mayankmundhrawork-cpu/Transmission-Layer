# Transmission Layer — board brief · 2026-07-30 06:47Z

data as of **2026-07-30** · 98 series · 14 red / 34 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.461, 1d in regime; vol-pct 0.422, breadth-off 0.5, Markov P(high-vol) 0.13)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.43, contra nifty_50 corr20=0.22, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.81, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.34, corr60 0.32, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.02, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.94, corr60 -0.83, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.04, corr60 -0.04, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.11, corr60 -0.24, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.36, corr60 0.21, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.627632343627951e-05)
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.525, β 0.8609, p 0.0); driver zc -1.73 → expected -1.16%. Type hit-rate 0.815 (n=3258).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.514, β 0.8166, p 0.0); driver zc -1.88 → expected -1.193%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.514, β -0.4176, p 0.0); driver zc -1.73 → expected 0.563%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.472, β -0.3143, p 0.0); driver zc -1.73 → expected 0.424%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.463, β 0.8229, p 0.0); driver zc -1.73 → expected -1.109%. Type hit-rate 0.815 (n=3258).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.46, β 0.7822, p 0.0); driver zc -1.88 → expected -1.143%. Type hit-rate 0.815 (n=3258).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.439, β -0.3437, p 0.0); driver zc -1.88 → expected 0.502%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.413, β 0.3269, p 0.0); driver zc -2.6 → expected -1.656%. Type hit-rate 0.815 (n=3258).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.412, β -0.0708, p 5e-05); driver zc 1.71 → expected -0.941%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.41, β 0.238, p 0.0); driver zc -1.51 → expected -0.84%. Type hit-rate 0.815 (n=3258).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.409, β -0.3516, p 0.0); driver zc -2.56 → expected 0.753%. Type hit-rate 0.815 (n=3258).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.406, β 0.7526, p 0.0); driver zc -2.56 → expected -1.611%. Type hit-rate 0.815 (n=3258).
- **SETUP** vix → usd_brl: leads 1d (ccf 0.403, β 0.0343, p 0.0); driver zc 1.71 → expected 0.456%. Type hit-rate 0.815 (n=3258).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.398, β -0.256, p 0.0); driver zc -1.88 → expected 0.374%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.395, β 0.3409, p 0.0); driver zc -2.6 → expected -1.727%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.394, β 0.3299, p 0.0); driver zc -2.11 → expected -1.311%. Type hit-rate 0.815 (n=3258).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.394, β 0.2569, p 1e-05); driver zc -2.56 → expected -0.55%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.388, β 0.3536, p 0.0); driver zc -2.11 → expected -1.406%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_gs → usd_brl: leads 1d (ccf -0.381, β -0.1525, p 0.0); driver zc -2.6 → expected 0.773%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.361, β -2.4547, p 0.00539); driver zc -1.73 → expected 3.308%. Type hit-rate 0.815 (n=3258).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.36, β -0.0666, p 0.00773); driver zc 1.71 → expected -0.885%. Type hit-rate 0.815 (n=3258).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.348, β -0.2458, p 0.0); driver zc -2.56 → expected 0.526%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.342, β 0.5394, p 0.0); driver zc -1.73 → expected -0.727%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.338, β 0.1508, p 0.0); driver zc -1.73 → expected -0.203%. Type hit-rate 0.815 (n=3258).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.338, β 0.0235, p 0.00061); driver zc 1.71 → expected 0.313%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_gs → kospi: leads 1d (ccf 0.327, β 0.3498, p 0.0); driver zc -2.6 → expected -1.773%. Type hit-rate 0.815 (n=3258).
- **SETUP** vix → india_vix: leads 1d (ccf 0.324, β 0.2088, p 0.01154); driver zc 1.71 → expected 2.775%. Type hit-rate 0.815 (n=3258).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.312, β 0.4786, p 0.00017); driver zc -1.88 → expected -0.699%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.307, β -0.101, p 2e-05); driver zc -2.6 → expected 0.512%. Type hit-rate 0.815 (n=3258).
- **SETUP** vix → nifty_metal: leads 1d (ccf -0.297, β -0.0443, p 0.00036); driver zc 1.71 → expected -0.589%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.265, β 0.3781, p 0.0); driver zc -1.73 → expected -0.509%. Type hit-rate 0.815 (n=3258).
- **SETUP** dyn_ms → usd_mxn: leads 1d (ccf -0.259, β -0.0893, p 0.00044); driver zc -2.11 → expected 0.355%. Type hit-rate 0.815 (n=3258).
- Track record · residual_reversion: hit-rate **0.492** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=3258) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.48] cross-asset · 13 series ↓
- sp500 [INDICES]: last 7320.23, z20 -3.41, zc -1.88, resid-z -0.55 [priced], 1d -1.46%, |z20|=3.41
- dyn_vt [EQUITIES]: last 152.27, z20 -3.21, zc -1.73, resid-z -1.72 [unexplained], 1d -1.35%, |z20|=3.21
- vix [INDICES]: last 20.63, z20 3.13, zc 1.71, resid-z n/a [moved], 1d 13.29%, |z20|=3.13
- nasdaq_100 [INDICES]: last 27211.63, z20 -2.92, zc -1.46, resid-z -1.59 [unexplained], 1d -1.99%, |z20|=2.92
- dyn_ms [EQUITIES]: last 203.17, z20 -2.78, zc -2.11, resid-z -1.23 [moved], 1d -3.97%, |z20|=2.78
- russell_2000 [INDICES]: last 2906.70, z20 -2.60, zc -1.36, resid-z 0.53 [quiet], 1d -1.59%, |z20|=2.60
- dyn_nvda [EQUITIES]: last 190.06, z20 -2.35, zc -1.51, resid-z 0.20 [priced], 1d -3.53%, |z20|=2.35
- dow_jones [INDICES]: last 51618.29, z20 -2.28, zc -2.56, resid-z -2.24 [unexplained], 1d -2.14%, |z20|=2.28
- dyn_gs [EQUITIES]: last 980.98, z20 -2.24, zc -2.60, resid-z -1.19 [moved], 1d -5.07%, |z20|=2.24
- tips_10y_real [RATES]: last 2.41, z20 1.22, zc -0.74, resid-z -0.93 [quiet], 1d -1.23%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.74, z20 -1.17, zc -1.22, resid-z 0.22 [quiet], 1d -0.35%, 1y-pct=2
- ust_2y [RATES]: last 4.26, z20 0.71, zc -0.90, resid-z -0.95 [quiet], 1d -1.16%, 1y-pct=97
- ust_10y [RATES]: last 4.61, z20 0.55, zc -0.91, resid-z -0.95 [quiet], 1d -0.86%, 1y-pct=96
- **Mechanism**: The recent decline in US equities, led by the S&P 500 and Nasdaq 100, is driven by a rotation out of AI-driven megacap technology stocks, which had been the primary drivers of the market rally. This rotation is causing a pullback in the stocks that had powered the AI-led market rally. The VIX, a measure of market volatility, has increased, indicating a shift in market sentiment. The decline in US equities is also reflected in the Indian market, with the Nifty FMCG index showing a negative correlation with the US market.
- **Gap**: No gap: The decline in US equities is largely priced in, with the S&P 500 and Nasdaq 100 showing significant moves, but the residual_z values indicate that the moves are largely explained by factors, leaving little room for a gap.
- **India take**: The Indian market is likely to follow the US market decline, with the Nifty FMCG index showing a negative correlation with the US market. However, the Indian market has not yet reacted significantly to the US market decline.
- Watch next: nifty_fmcg (down) — quiet; Negative correlation with US market
- Watch next: sp500 (down) — already moved; Rotation out of AI-driven megacap technology stocks
- Watch next: dyn_vt (down) — unexplained; Residual move not explained by factors
- **India receivers**: nifty_fmcg (rho -0.457, z 0.63)
- Source: Magnificent seven earnings to decide next move for Wall Street — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/magnificent-seven-earnings-to-decide-next-move-for-wall-street/slideshow/132728976.cms
- Source: Eicher Motors share price target: What are Morgan Stanley, Nomura saying about Royal Enfield maker? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/eicher-motors-share-price-target-what-are-morgan-stanley-nomura-saying-about-royal-enfield-maker/articleshow/132726822.cms
- Source: Bond market is calling Warsh’s bluff on inflation fight as yields surge — MarketWatch Top, 2026-07-29. https://www.marketwatch.com/story/bond-market-is-calling-warshs-bluff-on-inflation-fight-as-yields-surge-4700f9b5?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.33), 2024-10-11 (d=0.9), 2025-05-20 (d=0.91)

### [AMBER 6.09] brent ↑
- brent [COMMODITIES]: last 93.14, z20 1.09, zc 0.54, resid-z 2.21 [unexplained], 1d 2.64%, 1-session move +2.64% ≥ 1.5%
- **Mechanism**: Brent crude oil prices have moved up, driven by Japan's rare purchase of Canadian oil cargo, potentially diversifying away from Middle Eastern crude. This move may propagate through the metal_copper_channel, as global copper leads Indian metal equities. However, the inr_oil_channel is weak, which may limit the transmission to Indian markets.
- **Gap**: No gap: the big raw move in brent with small resid_z=2.21 is PRICED, not an anomaly, given the historical analogues and the current market regime.
- **India take**: The Indian instrument that expresses this move is dyn_hdbfs_bo, which has already reacted. Other potential responders, such as nifty_midcap_100, are still quiet.
- Watch next: nifty_midcap_100 (down) — not yet - watch; negative correlation with brent
- Watch next: dyn_hdbfs_bo (down) — already moved; negative correlation with brent
- **India receivers**: nifty_midcap_100 (rho -0.499, z 0.48); midcap_largecap_ratio (rho -0.402, z -0.3); dyn_hdbfs_bo (rho -0.384, z -2.05)
- Source: Japan Buys Rare Canadian Oil Cargo — OilPrice, 2026-07-30. https://oilprice.com/Latest-Energy-News/World-News/Japan-Buys-Rare-Canadian-Oil-Cargo.html
- Source: Crude oil futures fall despite continued US-Iran strikes — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-fall-despite-continued-us-iran-strikes/article71284338.ece
- Source: Vedanta Oil & Gas shares dip 4% despite becoming profitable in Q1 — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/vedanta-oil-gas-shares-dip-4-despite-becoming-profitable-in-q1/articleshow/132726751.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 5.9] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 40010.41, z20 -2.58, zc -0.02, resid-z -0.79 [quiet], 1d -0.07%, |z20|=2.58
- kospi [INDICES]: last 5609.33, z20 -2.28, zc -0.16, resid-z -0.70 [quiet], 1d -0.95%, |z20|=2.28
- nikkei_225 [INDICES]: last 61807.90, z20 -2.15, zc 0.26, resid-z 0.08 [quiet], 1d 0.61%, |z20|=2.15
- **Mechanism**: The recent decline in global indices, including the Nikkei and Kospi, is largely priced in, with small resid_z values indicating that the moves are largely explained by factor exposures. The transmission channels from these indices to Indian instruments, such as dyn_hdbfs_bo and nifty_metal, have already reacted, suggesting that the Indian market has largely absorbed the global sentiment. The valid channels, including the gold_silver_comove and metal_copper_channel, do not indicate any significant stress or rotation that would lead to a large gap.
- **Gap**: No gap: The small resid_z values and already reacted transmission channels indicate that the Indian market has largely priced in the global decline.
- **India take**: The Indian instruments, such as dyn_hdbfs_bo and nifty_metal, have already reacted to the global decline, and the nifty_midcap_100 is expected to follow suit. However, the Indian market is likely to open higher due to positive opening cues, despite the underlying cautious sentiment.
- Watch next: nifty_50 (down) — not yet - watch; Global risk-off sentiment
- **India receivers**: dyn_hdbfs_bo (rho 0.476, z -2.05); nifty_metal (rho 0.441, z 1.2); dyn_techm_ns (rho -0.419, z 2.3); dyn_pcjeweller_ns (rho 0.412, z -1.72)
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html
- Source: GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. selloff, fueled by concerns over AI spending and China's technological progress. South Korea's Kospi plunged 10%, triggering two trading halts, while Japan's Nikkei fell 4%. U.S. chip stocks — DeItaone, 2026-07-28. https://t.me/walter_bloomberg/33992

### [RED 5.77] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 31565.50, z20 2.94, zc 0.80, resid-z 0.50 [quiet], 1d 1.42%, |z20|=2.94
- dyn_techm_ns [EQUITIES]: last 1681.20, z20 2.30, zc 1.17, resid-z -0.79 [quiet], 1d 2.24%, |z20|=2.30; 1y-pct=96
- **Mechanism**: The recent acquisition of Mahindra & Mahindra's Truck and Bus Division by SML Mahindra has led to a surge in SML Mahindra shares, which may propagate to other stocks in the commercial vehicle sector through the metal_copper_channel, given the VALID status of this channel. The move in Nifty IT and Dyn Techm NS may be related to the broader market sentiment and the NEUTRAL regime. However, the resid_z values indicate that the moves are largely priced in, with only a small unexplained component.
- **Gap**: No gap: the moves in Nifty IT and Dyn Techm NS are largely priced in, with resid_z values of 0.5 and -0.79, respectively, indicating that the raw moves are mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is Dyn Tata Elxsi NS, which has not yet reacted but is being watched. The Nifty IT index has also moved, but its move is largely priced in.
- Watch next: dyn_tataelxsi_ns (up) — not yet - watch; correlated instrument with rho=0.671 vs Nifty IT
- **India receivers**: dyn_tataelxsi_ns (rho 0.671, z 0.65)
- Source: SML Mahindra shares rally over 18% on acquisition of M&M’s truck division. What it means for shareholders? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-shares-rally-over-18-on-acquisition-of-mahindra-mahindras-truck-and-bus-division-what-does-it-mean-for-shareholders/articleshow/132729786.cms
- Source: SML Mahindra to acquire Mahindra Truck and Bus division in commercial vehicle consolidation — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-to-acquire-mahindra-truck-and-bus-division-in-commercial-vehicle-consolidation/articleshow/132709583.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.65] dyn_infy ↑
- dyn_infy [EQUITIES]: last 12.65, z20 3.65, zc 0.79, resid-z 1.85 [unexplained], 1d 2.43%, |z20|=3.65
- **Mechanism**: The move in dyn_infy is driven by its correlation with Indian IT stocks, particularly Infosys, which have seen a surge in prices due to strong Q1 results and fresh foreign fund inflows. This move is further supported by the risk-off regime, where investors are shifting towards software exporters. The valid gold_silver_comove and metal_copper_channel also indicate a potential rotation into metals, which could be a contributing factor.
- **Gap**: No gap: The move in dyn_infy is largely priced in, given its z20 level of 3.65 and resid_z of 1.85, indicating that the move is largely explained by its factor exposures.
- **India take**: The Indian instruments nifty_it and dyn_techm_ns have already reacted to the move in dyn_infy, given their high correlations of 0.608 and 0.576, respectively. However, dyn_tataelxsi_ns, which has a correlation of 0.393 with dyn_infy, has not yet moved and is worth watching.
- Watch next: dyn_tataelxsi_ns (up) — not yet - watch; Historically leads dyn_infy by 1d and has a correlation of 0.393
- **India receivers**: nifty_it (rho 0.609, z 2.94); dyn_techm_ns (rho 0.573, z 2.3); dyn_tataelxsi_ns (rho 0.385, z 0.65)
- Source: Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-29-july-2026/article71276758.ece
- Source: Sensex today | Stock Market Live: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-29-july-2026/article71276758.ece
- Source: TCS vs Infosys vs Wipro vs HCL Tech: Which IT stock to buy after Q1 results? — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/tcs-vs-infosys-vs-wipro-vs-hcl-tech-which-it-stock-to-buy-after-q1-results-11785302857002.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

### [RED 5.3] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.75, z20 3.30, zc 0.10, resid-z 0.81 [quiet], 1d 0.26%, |z20|=3.30; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Samsung Q2 results: Tech giant's revenue reaches all-time high of $119 billion amid strong semiconductor demand — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/samsung-q2-results-tech-giants-revenue-reaches-all-time-high-of-119-billion-amid-strong-semiconductor-demand-11785385136224.html
- Source: CENTCOM WARNS OVER OPSEC RISKS CENTCOM chief Adm. Brad Cooper warned U.S. troops that sharing cellphone videos online could help Iran assess the success of attacks on U.S. bases in near real time. The warning follows deadly Iranian strikes in July and stresses that poor — DeItaone, 2026-07-29. https://t.me/walter_bloomberg/34047
- Source: ‘Nothing seems to shake this market.’ Why it’s time to go all-in on stocks, according to these bullish strategists. — MarketWatch Top, 2026-07-29. https://www.marketwatch.com/story/oil-is-up-40-and-tech-is-tumbling-why-its-time-to-go-all-in-on-stocks-according-to-these-bullish-strategists-41d812f7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 4.7] dyn_waareeener_bo ↓
- dyn_waareeener_bo [EQUITIES]: last 2622.25, z20 -2.70, zc -0.68, resid-z -0.43 [quiet], 1d -2.70%, |z20|=2.70; 1y-pct=4
- **Mechanism**: dyn_waareeener_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho 0.406 via dyn_waareeener_bo, z 0.16, quiet); nifty_midcap_100 (rho 0.377 via dyn_waareeener_bo, z 0.48, quiet); dyn_bharatcoal_ns (rho 0.366 via dyn_waareeener_bo, z -1.89, reacted)
- **India receivers**: dyn_indianb_ns (rho 0.406, z 0.16); nifty_midcap_100 (rho 0.377, z 0.48); dyn_bharatcoal_ns (rho 0.366, z -1.89)
- Source: Waaree Energies share price fell 6% despite strong Q1 results 2026; here's why — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/renewable-energy-stock-waaree-energies-share-price-fell-6-despite-strong-q1-results-2026-heres-why-11785389816080.html
- Source: Waaree Energies shares slide 6% despite 15% profit growth and 79% YoY revenue surge in Q1FY27 — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/waaree-energies-shares-slide-6-despite-15-profit-growth-and-79-yoy-revenue-surge-in-q1fy27/articleshow/132727911.cms
- Source: Waaree Energies shares fall over 6% despite ₹850 crore Q1 profit — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/waaree-energies-shares-fall-over-6-despite-850-crore-q1-profit/article71284394.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-11 (d=0.01), 2025-10-01 (d=0.01)

### [RED 4.53] dyn_thangamayl_ns ↓
- dyn_thangamayl_ns [EQUITIES]: last 5807.00, z20 -2.53, zc -1.11, resid-z -2.81 [unexplained], 1d -10.00%, |z20|=2.53
- **Mechanism**: dyn_thangamayl_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.352 via dyn_thangamayl_ns, z 0.63, quiet)
- **India receivers**: nifty_fmcg (rho -0.352, z 0.63)
- Source: Thangamayil Jewellery shares crash 19% in 2 days on weak Q2 outlook. What did the company say? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/thangamayil-jewellery-shares-crash-19-in-2-days-on-weak-q2-outlook-what-did-the-company-say/articleshow/132728014.cms
- Source: Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹695 cr profit, Asian Paints, Adani Ports, Colgate, V-Guard Q1 profit rise, Thangamayil Jewellery shares tank 10% after results; Eicher Motors PAT up 21%, Waaree Energies' rise 15%, Dabur's up 15%, ACME Solar con. profit zooms 80% — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-adani-enterprises-adani-ports-asian-paints-eicher-motors-waaree-energies-colgate-prestige-estates-syrma-sgs-tech-dabur-hexaware-tech-vedanta-oil-acme-results-29-july-2026/article71276282.ece
- Source: Q1 Results Today Live: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹695 cr profit, Asian Paints, Adani Ports, Colgate, V-Guard Q1 profit rise, Thangamayil Jewellery shares tank 10% after results; Eicher Motors, Waaree Energies, Prestige Estates, Dabur, ACME Solar to announce Q1 results — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-adani-enterprises-adani-ports-asian-paints-eicher-motors-waaree-energies-colgate-prestige-estates-syrma-sgs-tech-dabur-hexaware-tech-vedanta-oil-acme-results-29-july-2026/article71276282.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-29 (d=0.01), 2026-06-11 (d=0.01)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (4.49), dyn_eternal_ns ↑ (4.19), dyn_cupid_ns ↑ (3.68), dyn_tech ↑ (3.51), indices · 2 series ↑ (3.48), dyn_ohi ↑ (3.42), dyn_aapl ↑ (3.39), dyn_301077_sz ↓ (3.26), hy_oas ↑ (3.21), commodities · 2 series ↑ (2.97), dyn_icicigi_bo ↓ (2.97), dyn_bac ↑ (2.49)

## India macro
- nifty_50: 24254.9492 (1d 0.02%, z20 0.77, flag none)
- nifty_midcap_100: 62654.6992 (1d -0.30%, z20 0.48, flag amber)
- usd_inr: 95.7400 (1d 0.15%, z20 -0.53, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5832 (1d -0.32%, z20 -0.30, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 78.1 — "US Fed leaves federal funds rate unchanged: How can a status quo impact the Indian stock m"
- INOXINDIA.NS (INOX INDIA LIMITED) score 71.0 — "US Fed leaves federal funds rate unchanged: How can a status quo impact the Indian stock m"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 64.0 — "US Fed leaves federal funds rate unchanged: How can a status quo impact the Indian stock m"
- BAC (Bank of America Corporation) score 62.9 — "Investors Are Racing to Find America's Next Rare Earth Winner"
- HDB (HDFC Bank Limited) score 59.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- COALINDIA.NS (COAL INDIA LTD) score 58.6 — "US Fed leaves federal funds rate unchanged: How can a status quo impact the Indian stock m"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.1 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- IDBI.NS (IDBI BANK LIMITED) score 56.7 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.4 — "Kaynes Technology among 9 stocks showing bullish RSI upswing"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.7 — "Kaynes Technology among 9 stocks showing bullish RSI upswing"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 51.2 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- COIN (Coinbase Global, Inc.) score 49.7 — "Indian stocks set for flat opening amid global headwinds"
- OHI (Omega Healthcare Investors, In) score 45.4 — "What a divided Fed means for investors"
- TECH (Bio-Techne Corp) score 34.0 — "Kaynes Technology among 9 stocks showing bullish RSI upswing"
- CHKP (Check Point Software Technolog) score 29.0 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 3"
- LTH (Life Time Group Holdings, Inc.) score 27.1 — "Sensex, Nifty trade flat as hawkish Fed pause dents sentiment. What's driving the caution?"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.7 — "India should prioritise energy security over US tariff threats on Russian oil: GTRI"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.6 — "SBI raises  ₹4,691 crore via AT1 bonds at 7.75% rate"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 22.6 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.9 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Update: Price and Trends"
- MS (Morgan Stanley) score 15.8 — "Eicher Motors share price target: What are Morgan Stanley, Nomura saying about Royal Enfie"
- 301077.SZ (CHINASTARS) score 13.0 — "Global Market: China, Hong Kong stocks slip as AI selloff hits chip shares; defensive sect"
- INFY (Infosys Limited) score 11.0 — "Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty end"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.2 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "I’m managing a former colleague who just can’t keep up with her workload. How do I handle "
- JIOFIN.BO (Jio Financial Services Limited) score 8.7 — "Market wrap: Jio Financial, HUL among top gainers and losers on Nifty and Sensex on Wednes"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.7 — "Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target"
- VT (Vanguard Total World Stock Ind) score 7.5 — "World Nuclear Association: $6 Trillion Needed to Hit 2050 Capacity Goals"
- META (Meta) score 6.9 — "Market Trading Guide: Lloyds Metals among 2 stock recommendations for Thursday"
- NVDA (NVIDIA Corporation) score 6.7 — "Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor"
- GS (Goldman Sachs Group, Inc. (The) score 6.3 — "L&T shares rise 4% after Q1 earnings. Why Goldman Sachs, other brokerages remain bullish?"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.0 — "Market wrap: Jio Financial, HUL among top gainers and losers on Nifty and Sensex on Wednes"
- AAPL (Apple Inc.) score 5.5 — "Apple briefly touches $5 trillion market cap, becomes the second company after Nvidia to h"
- SKHYV (SK hynix Inc. American Deposit) score 5.3 — "SK Hynix shares sent sprawling once more as earnings miss steepens decline"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.2 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 4.5 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- ETERNAL.NS (ETERNAL LIMITED) score 4.5 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- WAAREEENER.BO (Waaree Energies Limited) score 4.0 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- CUPID.NS (CUPID LIMITED) score 1.0 — "Cupid makes additional $5 million investment in GII Healthcare platform"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.3 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "

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