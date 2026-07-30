# Transmission Layer — board brief · 2026-07-30 11:32Z

data as of **2026-07-30** · 98 series · 17 red / 35 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.54, 1d in regime; vol-pct 0.747, breadth-off 0.333, Markov P(high-vol) 0.13)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.44, contra nifty_50 corr20=0.23, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.81, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.33, corr60 0.32, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.02, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.94, corr60 -0.83, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 -0.04, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.11, corr60 -0.24, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.28, corr60 0.2, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.001577691388751301)
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.552, β 0.3404, p 0.0); driver zc -1.73 → expected -0.459%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.525, β 0.8609, p 0.0); driver zc -1.73 → expected -1.16%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.514, β 0.8166, p 0.0); driver zc -1.88 → expected -1.193%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.512, β -0.4165, p 0.0); driver zc -1.73 → expected 0.561%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.47, β -0.3133, p 0.0); driver zc -1.73 → expected 0.422%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.463, β 0.8229, p 0.0); driver zc -1.73 → expected -1.109%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.46, β 0.7822, p 0.0); driver zc -1.88 → expected -1.143%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.458, β 0.272, p 0.0); driver zc -1.88 → expected -0.397%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.437, β -0.3426, p 0.0); driver zc -1.88 → expected 0.501%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.413, β 0.3269, p 0.0); driver zc -2.6 → expected -1.656%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.41, β 0.238, p 0.0); driver zc -1.51 → expected -0.84%. Type hit-rate 0.808 (n=3302).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.407, β -0.3497, p 0.0); driver zc -2.56 → expected 0.749%. Type hit-rate 0.808 (n=3302).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.406, β 0.7526, p 0.0); driver zc -2.56 → expected -1.611%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.396, β -0.2549, p 0.0); driver zc -1.88 → expected 0.372%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.395, β 0.3409, p 0.0); driver zc -2.6 → expected -1.727%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.394, β 0.3299, p 0.0); driver zc -2.11 → expected -1.311%. Type hit-rate 0.808 (n=3302).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.391, β 0.2549, p 1e-05); driver zc -2.56 → expected -0.546%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.388, β 0.3536, p 0.0); driver zc -2.11 → expected -1.406%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_gs → usd_brl: leads 1d (ccf -0.378, β -0.1515, p 0.0); driver zc -2.6 → expected 0.768%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.361, β -2.455, p 0.00538); driver zc -1.73 → expected 3.308%. Type hit-rate 0.808 (n=3302).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.346, β -0.2439, p 0.0); driver zc -2.56 → expected 0.522%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.341, β 0.5383, p 0.0); driver zc -1.73 → expected -0.725%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.336, β 0.1499, p 0.0); driver zc -1.73 → expected -0.202%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.333, β 0.071, p 0.0); driver zc -1.51 → expected -0.25%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_gs → kospi: leads 1d (ccf 0.327, β 0.3498, p 0.0); driver zc -2.6 → expected -1.773%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_nvda → usd_mxn: leads 1d (ccf -0.317, β -0.073, p 0.0); driver zc -1.51 → expected 0.258%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.311, β 0.4775, p 0.00018); driver zc -1.88 → expected -0.698%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.304, β -0.1001, p 2e-05); driver zc -2.6 → expected 0.507%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_gs → aud_usd: leads 1d (ccf 0.302, β 0.0917, p 0.00106); driver zc -2.6 → expected -0.465%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.297, β 0.364, p 0.0); driver zc -1.73 → expected -0.491%. Type hit-rate 0.808 (n=3302).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.272, β 0.3245, p 0.0); driver zc -1.88 → expected -0.474%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.267, β 0.0853, p 0.00337); driver zc -2.11 → expected -0.339%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.265, β 0.3785, p 0.0); driver zc -1.73 → expected -0.51%. Type hit-rate 0.808 (n=3302).
- **SETUP** dyn_ms → usd_mxn: leads 1d (ccf -0.256, β -0.0884, p 0.00051); driver zc -2.11 → expected 0.351%. Type hit-rate 0.808 (n=3302).
- Track record · residual_reversion: hit-rate **0.492** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.808** (n=3302) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.48] cross-asset · 13 series ↓
- sp500 [INDICES]: last 7320.23, z20 -3.41, zc -1.88, resid-z -0.55 [priced], 1d -1.46%, |z20|=3.41
- dyn_vt [EQUITIES]: last 152.27, z20 -3.21, zc -1.73, resid-z -1.72 [unexplained], 1d -1.35%, |z20|=3.21
- nasdaq_100 [INDICES]: last 27211.63, z20 -2.92, zc -1.46, resid-z -1.59 [unexplained], 1d -1.99%, |z20|=2.92
- dyn_ms [EQUITIES]: last 203.17, z20 -2.78, zc -2.11, resid-z -1.23 [moved], 1d -3.97%, |z20|=2.78
- russell_2000 [INDICES]: last 2906.70, z20 -2.60, zc -1.36, resid-z 0.53 [quiet], 1d -1.59%, |z20|=2.60
- dyn_nvda [EQUITIES]: last 190.06, z20 -2.35, zc -1.51, resid-z 0.20 [priced], 1d -3.53%, |z20|=2.35
- dow_jones [INDICES]: last 51618.29, z20 -2.28, zc -2.56, resid-z -2.24 [unexplained], 1d -2.14%, |z20|=2.28
- dyn_gs [EQUITIES]: last 980.98, z20 -2.24, zc -2.60, resid-z -1.19 [moved], 1d -5.07%, |z20|=2.24
- vix [INDICES]: last 19.34, z20 1.52, zc -0.60, resid-z n/a [quiet], 1d -6.39%, |z20|=1.52
- tips_10y_real [RATES]: last 2.41, z20 1.22, zc -0.74, resid-z -0.93 [quiet], 1d -1.23%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.74, z20 -1.17, zc -1.22, resid-z 0.22 [quiet], 1d -0.35%, 1y-pct=2
- ust_2y [RATES]: last 4.26, z20 0.71, zc -0.90, resid-z -0.95 [quiet], 1d -1.16%, 1y-pct=97
- ust_10y [RATES]: last 4.61, z20 0.55, zc -0.91, resid-z -0.95 [quiet], 1d -0.86%, 1y-pct=96
- **Mechanism**: The recent decline in US equities, led by the S&P 500 and Nasdaq 100, is attributed to rising US bond yields and cautious investor sentiment. This move is priced in, as indicated by the low resid_z values for these indices. The transmission of this move to Indian markets is expected through the verified transmission setup of dyn_vt to aud_usd and taiwan_weighted.
- **Gap**: No gap: the move in US equities is largely priced in, with low resid_z values indicating that the decline is explained by factor exposures
- **India take**: The Indian instrument that expresses this move is nifty_fmcg, which has not reacted yet. The transmission setup of dyn_vt to aud_usd and taiwan_weighted suggests that a decline in nifty_fmcg is expected.
- Watch next: nifty_fmcg (down) — not yet - watch; rho=-0.457 via dyn_nvda
- **India receivers**: nifty_fmcg (rho -0.457, z 0.74)
- Source: Wall Street just suffered a historic crash in high-flying stocks. Here is why a quick tech rebound could be a trap. — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/wall-street-just-suffered-a-historic-crash-in-high-flying-stocks-here-is-why-a-quick-tech-rebound-could-be-a-trap-c021318a?mod=mw_rss_topstories
- Source: The World Cup winners wore Adidas shirts. But the company’s investors are still crying foul. — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/the-world-cup-winners-wore-adidas-shirts-but-the-companys-investors-are-still-crying-foul-2224d39a?mod=mw_rss_topstories
- Source: Sensex, Nifty 50 rise, but mid, small-caps falter; rising US bond yields keep investors cautious — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/sensex-nifty-50-rise-but-mid-small-caps-falter-rising-us-bond-yields-keep-investors-cautious-11785405396383.html
- Historical analogues: 2026-05-22 (d=0.33), 2024-10-11 (d=0.9), 2025-05-20 (d=0.91)

### [RED 6.43] cross-asset · 5 series ↑
- ftse_100 [INDICES]: last 10936.36, z20 2.50, zc 0.38, resid-z 0.27 [quiet], 1d 0.26%, |z20|=2.50; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.44, z20 1.65, zc 1.16, resid-z 0.26 [quiet], 1d 2.61%, |z20|=1.65; co-occur[metal_copper] same-direction (channel VALID)
- cac_40 [INDICES]: last 8489.06, z20 1.62, zc 1.10, resid-z 0.92 [quiet], 1d 0.96%, |z20|=1.62; 1y-pct=97
- dax [INDICES]: last 25509.63, z20 1.04, zc 0.21, resid-z 1.34 [quiet], 1d 0.19%, 1y-pct=98
- stoxx_50 [INDICES]: last 6303.05, z20 0.32, zc 0.93, resid-z 1.23 [quiet], 1d 0.87%, 1y-pct=96
- **Mechanism**: The recent move in global indices and commodities, particularly copper, is driven by anticipation of the Federal Reserve's interest rate decision and supply concerns in the Middle East. The metal_copper_channel, which is VALID, suggests that global copper prices can lead Indian metal equities. However, the resid_z values for the affected series are relatively low, indicating that the moves are largely priced in.
- **Gap**: No gap: the moves in the affected series are largely priced in, as indicated by the low resid_z values.
- **India take**: The Nifty 50 has already reacted to the global moves, while the Nifty Midcap 100 is still quiet. The metal_copper_channel may lead to further moves in Indian metal equities.
- Watch next: nifty_50 (up) — already moved; rho=0.547 via cac_40
- Watch next: nifty_midcap_100 (up) — not yet - watch; rho=0.539 via dax
- **India receivers**: nifty_50 (rho 0.547, z 1.01); nifty_midcap_100 (rho 0.539, z 0.51)
- Source: Copper slips ahead of Fed rate decision, aluminium rises on Gulf fighting — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/commodities/news/copper-slips-ahead-of-fed-rate-decision-aluminium-rises-on-gulf-fighting/articleshow/132712953.cms
- Historical analogues: 2025-04-17 (d=0.49), 2024-10-03 (d=0.59), 2025-04-01 (d=0.72)

### [RED 5.9] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 40010.41, z20 -2.58, zc -0.02, resid-z -0.79 [quiet], 1d -0.07%, |z20|=2.58
- kospi [INDICES]: last 5609.33, z20 -2.28, zc -0.16, resid-z -0.70 [quiet], 1d -0.95%, |z20|=2.28
- nikkei_225 [INDICES]: last 61807.90, z20 -2.15, zc 0.26, resid-z 0.08 [quiet], 1d 0.61%, |z20|=2.15
- **Mechanism**: The recent decline in global indices, including Taiwan Weighted, Kospi, and Nikkei 225, is largely priced in, with small resid_z values indicating that the moves are mostly explained by factor exposures. The transmission channels from these indices to Indian instruments, such as dyn_hdbfs_bo, nifty_metal, and dyn_techm_ns, have already reacted, suggesting that the Indian market has largely absorbed the global sentiment. The valid channels, including gold_silver_comove and metal_copper_channel, do not indicate any significant risk-off or safe-haven bids that would exacerbate the decline.
- **Gap**: No gap: the decline in global indices is largely priced in, with small resid_z values and reacted transmission channels
- **India take**: The Indian market, as expressed through instruments like nifty_midcap_100, may still react to the weak global cues, but the extent of the decline is likely to be limited due to the already reacted transmission channels. The Indian instruments, such as dyn_hdbfs_bo and nifty_metal, have already shown a reaction to the global sentiment.
- Watch next: nifty_midcap_100 (down) — not yet - watch; weak global cues and lack of domestic triggers
- **India receivers**: dyn_hdbfs_bo (rho 0.481, z -1.74); nifty_metal (rho 0.441, z 1.56); dyn_techm_ns (rho -0.421, z 2.13); dyn_pcjeweller_ns (rho 0.412, z -1.59)
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html

### [RED 5.65] dyn_infy ↑
- dyn_infy [EQUITIES]: last 12.65, z20 3.65, zc 0.79, resid-z 1.85 [unexplained], 1d 2.43%, |z20|=3.65
- **Mechanism**: The move in dyn_infy is driven by its correlation with Indian IT stocks, particularly Infosys, which have seen a surge in prices due to strong Q1 results and fresh foreign fund inflows. This move is further supported by the risk-off regime, where investors are shifting towards software exporters. The valid gold_silver_comove and metal_copper_channel also indicate a potential rotation into metals, which could be a contributing factor.
- **Gap**: No gap: The move in dyn_infy is largely priced in, given its z20 level of 3.65 and resid_z of 1.85, indicating that the move is largely explained by its factor exposures.
- **India take**: The Indian instruments nifty_it and dyn_techm_ns have already reacted to the move in dyn_infy, given their high correlations of 0.608 and 0.576, respectively. However, dyn_tataelxsi_ns, which has a correlation of 0.393 with dyn_infy, has not yet moved and is worth watching.
- Watch next: dyn_tataelxsi_ns (up) — not yet - watch; Historically leads dyn_infy by 1d and has a correlation of 0.393
- **India receivers**: nifty_it (rho 0.612, z 2.57); dyn_techm_ns (rho 0.576, z 2.13); dyn_tataelxsi_ns (rho 0.385, z 0.49)
- Source: Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-29-july-2026/article71276758.ece
- Source: Sensex today | Stock Market Live: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-29-july-2026/article71276758.ece
- Source: TCS vs Infosys vs Wipro vs HCL Tech: Which IT stock to buy after Q1 results? — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/tcs-vs-infosys-vs-wipro-vs-hcl-tech-which-it-stock-to-buy-after-q1-results-11785302857002.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

### [RED 5.4] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 31188.45, z20 2.57, zc 0.12, resid-z 0.11 [quiet], 1d 0.21%, |z20|=2.57
- dyn_techm_ns [EQUITIES]: last 1669.00, z20 2.13, zc 0.79, resid-z 0.62 [quiet], 1d 1.51%, |z20|=2.13
- **Mechanism**: The recent acquisition of Mahindra & Mahindra's Truck and Bus Division by SML Mahindra has sparked a rally in the stock, with potential synergies and earnings accretion driving the move. This event may propagate through the metal_copper_channel, given the industry overlap, and potentially influence other Indian metal equities. However, the current move in Nifty IT and Dyn Techm NS appears priced, with resid_z values of 0.11 and 0.62, respectively, indicating that the majority of the move can be explained by factor exposures.
- **Gap**: No gap: the current move in Nifty IT and Dyn Techm NS appears priced, with resid_z values indicating that the majority of the move can be explained by factor exposures
- **India take**: The Indian instrument that expresses this move is Dyn Tata Elxsi NS, which has not yet reacted but may potentially move in tandem with Nifty IT. The acquisition news may also influence other Indian metal equities, such as those in the commercial vehicle portfolio.
- Watch next: dyn_tataelxsi_ns (up) — not yet - watch; correlated instrument with rho=0.674 vs Nifty IT
- **India receivers**: dyn_tataelxsi_ns (rho 0.674, z 0.49)
- Source: SML Mahindra shares rally over 18% on acquisition of M&M’s truck division. What it means for shareholders? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-shares-rally-over-18-on-acquisition-of-mahindra-mahindras-truck-and-bus-division-what-does-it-mean-for-shareholders/articleshow/132729786.cms
- Source: SML Mahindra to acquire Mahindra Truck and Bus division in commercial vehicle consolidation — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-to-acquire-mahindra-truck-and-bus-division-in-commercial-vehicle-consolidation/articleshow/132709583.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.3] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.75, z20 3.30, zc 0.10, resid-z 0.81 [quiet], 1d 0.26%, |z20|=3.30; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: 'Wait till payback time!': South Korean retail investors protest as govt apologises after Kospi crashes 40% in a month — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/wait-till-payback-time-south-korean-retail-investors-protest-as-govt-apologises-after-kospi-crashes-40-in-a-month/articleshow/132736424.cms
- Source: Bombay HC grants SEBI time to file affidavits in Embassy REIT matters, regulator indicates likely position — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/bombay-hc-grants-sebi-time-to-file-affidavits-in-embassy-reit-matters-regulator-indicates-likely-position/article71285130.ece
- Source: Samsung Q2 results: Tech giant's revenue reaches all-time high of $119 billion amid strong semiconductor demand — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/samsung-q2-results-tech-giants-revenue-reaches-all-time-high-of-119-billion-amid-strong-semiconductor-demand-11785385136224.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 4.6] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 310.20, z20 2.60, zc -0.22, resid-z -0.57 [quiet], 1d -0.51%, |z20|=2.60
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.556 via dyn_eternal_ns, z 0.51, quiet); dyn_jiofin_bo (rho 0.422 via dyn_eternal_ns, z 1.93, reacted); nifty_50 (rho 0.404 via dyn_eternal_ns, z 1.01, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.556 vs dyn_eternal_ns, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.556, z 0.51); dyn_jiofin_bo (rho 0.422, z 1.93); nifty_50 (rho 0.404, z 1.01)
- Source: Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/eternal-shares-jump-over-20-in-one-month-will-the-stock-cross-its-october-peak-of-rs-368/articleshow/132700500.cms
- Source: Market wrap: TCS, Eternal, HUL, BEL among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-eternal-hul-bel-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132684231.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

### [RED 4.57] dyn_waareeener_bo ↓
- dyn_waareeener_bo [EQUITIES]: last 2624.40, z20 -2.57, zc -1.71, resid-z -2.08 [unexplained], 1d -4.15%, |z20|=2.57; 1y-pct=4
- **Mechanism**: dyn_waareeener_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.381 via dyn_waareeener_bo, z 0.51, quiet); dyn_jiofin_bo (rho 0.374 via dyn_waareeener_bo, z 1.93, reacted); dyn_indianb_ns (rho 0.358 via dyn_waareeener_bo, z 0.15, quiet); dyn_bharatcoal_ns (rho 0.35 via dyn_waareeener_bo, z -1.89, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.381, z 0.51); dyn_jiofin_bo (rho 0.374, z 1.93); dyn_indianb_ns (rho 0.358, z 0.15); dyn_bharatcoal_ns (rho 0.35, z -1.89)
- Source: Waaree Energies share price fell 6% despite strong Q1 results 2026; here's why — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/renewable-energy-stock-waaree-energies-share-price-fell-6-despite-strong-q1-results-2026-heres-why-11785389816080.html
- Source: Waaree Energies shares slide 6% despite 15% profit growth and 79% YoY revenue surge in Q1FY27 — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/waaree-energies-shares-slide-6-despite-15-profit-growth-and-79-yoy-revenue-surge-in-q1fy27/articleshow/132727911.cms
- Source: Waaree Energies shares fall over 6% despite ₹850 crore Q1 profit — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/waaree-energies-shares-fall-over-6-despite-850-crore-q1-profit/article71284394.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-11 (d=0.01), 2025-10-01 (d=0.01)

## Watchlist (below surfacing floor)
dyn_thangamayl_ns ↓ (4.53), gold_silver_ratio ↑ (4.29), eur_usd ↑ (4.24), dyn_cupid_ns ↑ (3.75), dyn_tech ↑ (3.51), dyn_ohi ↑ (3.42), dyn_aapl ↑ (3.39), commodities · 2 series ↑ (3.3), dyn_301077_sz ↓ (3.27), hy_oas ↑ (3.21), usd_cny ↓ (3.15), dyn_havells_ns ↑ (2.98)

## India macro
- nifty_50: 24296.5996 (1d 0.19%, z20 1.01, flag none)
- nifty_midcap_100: 62668.9492 (1d -0.28%, z20 0.51, flag amber)
- usd_inr: 95.6800 (1d 0.09%, z20 -0.65, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5793 (1d -0.47%, z20 -0.52, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 77.6 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- INOXINDIA.NS (INOX INDIA LIMITED) score 70.8 — "Brent climbs above $90 a barrel as fresh US-Iran conflict raises risks for India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 64.1 — "Brent climbs above $90 a barrel as fresh US-Iran conflict raises risks for India"
- BAC (Bank of America Corporation) score 62.1 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- COALINDIA.NS (COAL INDIA LTD) score 59.9 — "Brent climbs above $90 a barrel as fresh US-Iran conflict raises risks for India"
- HDB (HDFC Bank Limited) score 58.9 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.5 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.8 — "Oneindig Technologies IPO Day 1: Issue booked 15% so far. Check GMP, other key details"
- IDBI.NS (IDBI BANK LIMITED) score 56.1 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.2 — "Oneindig Technologies IPO Day 1: Issue booked 15% so far. Check GMP, other key details"
- COIN (Coinbase Global, Inc.) score 51.4 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 50.9 — "Global Market: Bank of England expected to hold rates steady as inflation risks stay in fo"
- OHI (Omega Healthcare Investors, In) score 50.4 — "Investors are overlooking healthcare stocks and should consider these top picks, says JPMo"
- TECH (Bio-Techne Corp) score 35.5 — "Oneindig Technologies IPO Day 1: Issue booked 15% so far. Check GMP, other key details"
- CHKP (Check Point Software Technolog) score 30.7 — "Dhaval Packaging IPO Day 1: Issue booked 26% so far. Check GMP, issue details"
- LTH (Life Time Group Holdings, Inc.) score 27.9 — "Bombay HC grants SEBI time to file affidavits in Embassy REIT matters, regulator indicates"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.4 — "US bond yield is global finance’s Achilles heel: Uday Kotak after Fed meeting"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.5 — "Shell Reports $9.8 Billion in Adjusted Earnings as Energy Prices Surge"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 21.6 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- MS (Morgan Stanley) score 17.1 — "Investors are overlooking healthcare stocks and should consider these top picks, says JPMo"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.2 — "Q1 Results Today Live: Swiggy narrows loss, Bajaj Finance, M&M, Gillette, Vedanta, Vedanta"
- 301077.SZ (CHINASTARS) score 13.4 — "China’s Coal Prices Surge as Scorching Heat Drives Power Demand"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.7 — "Shell Reports $9.8 Billion in Adjusted Earnings as Energy Prices Surge"
- INFY (Infosys Limited) score 10.5 — "Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty end"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.8 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.3 — "China’s Coal Prices Surge as Scorching Heat Drives Power Demand"
- META (Meta) score 8.6 — "Market Focus: Meta's higher AI budget jolts shares, signals long-term push"
- JIOFIN.BO (Jio Financial Services Limited) score 8.3 — "Market wrap: Jio Financial, HUL among top gainers and losers on Nifty and Sensex on Wednes"
- VT (Vanguard Total World Stock Ind) score 8.1 — "The World Cup winners wore Adidas shirts. But the company’s investors are still crying fou"
- NVDA (NVIDIA Corporation) score 6.4 — "Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor"
- GS (Goldman Sachs Group, Inc. (The) score 6.0 — "L&T shares rise 4% after Q1 earnings. Why Goldman Sachs, other brokerages remain bullish?"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.9 — "ICICI Prudential MF buys stake in Go Digit General Insurance for ₹139 crore"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 5.7 — "Market wrap: Jio Financial, HUL among top gainers and losers on Nifty and Sensex on Wednes"
- AAPL (Apple Inc.) score 5.3 — "Apple briefly touches $5 trillion market cap, becomes the second company after Nvidia to h"
- SKHYV (SK hynix Inc. American Deposit) score 5.0 — "SK Hynix shares sent sprawling once more as earnings miss steepens decline"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 4.3 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- ETERNAL.NS (ETERNAL LIMITED) score 4.3 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- WAAREEENER.BO (Waaree Energies Limited) score 3.8 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- CUPID.NS (CUPID LIMITED) score 1.9 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"
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