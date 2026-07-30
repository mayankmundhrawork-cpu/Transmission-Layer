# Transmission Layer — board brief · 2026-07-30 17:12Z

data as of **2026-07-30** · 98 series · 15 red / 35 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.512, 1d in regime; vol-pct 0.612, breadth-off 0.412, Markov P(high-vol) 0.21)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.46, contra nifty_50 corr20=0.22, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.81, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.32, corr60 0.32, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.02, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.84, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.03, corr60 -0.04, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.11, corr60 -0.24, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.24, corr60 0.19, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **6 of 90** scanned series survive multiplicity control (effective p ≤ 0.004954149997571822)
- **SETUP** nasdaq_100 → dyn_453950_ks: leads 1d (ccf 0.599, β 0.8746, p 0.0); driver zc 2.14 → expected 2.747%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.581, β 0.4651, p 0.0); driver zc 2.05 → expected 0.852%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.579, β 0.4466, p 0.0); driver zc 1.59 → expected 0.651%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.547, β 1.1086, p 0.0); driver zc 2.05 → expected 2.032%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → dyn_453950_ks: leads 1d (ccf 0.541, β 1.0553, p 0.0); driver zc 1.59 → expected 1.539%. Type hit-rate 0.808 (n=3275).
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.541, β 0.6269, p 0.0); driver zc 2.14 → expected 1.969%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.525, β 0.8607, p 0.0); driver zc 2.05 → expected 1.578%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.514, β 0.8163, p 0.0); driver zc 1.59 → expected 1.19%. Type hit-rate 0.808 (n=3275).
- **SETUP** nasdaq_100 → asx_200: leads 1d (ccf 0.507, β 0.293, p 0.0); driver zc 2.14 → expected 0.92%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.504, β 0.2072, p 0.0); driver zc 1.64 → expected 0.72%. Type hit-rate 0.808 (n=3275).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.471, β 0.5947, p 0.0); driver zc 2.14 → expected 1.868%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.463, β 0.8227, p 0.0); driver zc 2.05 → expected 1.508%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.46, β 0.7819, p 0.0); driver zc 1.59 → expected 1.14%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_infy → nifty_it: leads 1d (ccf 0.446, β 0.3353, p 0.0); driver zc -1.8 → expected -1.823%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_ms → dyn_453950_ks: leads 1d (ccf 0.424, β 0.4503, p 0.0); driver zc 1.64 → expected 1.565%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.407, β 0.8764, p 0.0); driver zc 2.05 → expected 1.606%. Type hit-rate 0.808 (n=3275).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.397, β 0.615, p 0.0); driver zc 2.14 → expected 1.931%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.394, β 0.3298, p 0.0); driver zc 1.64 → expected 1.146%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.388, β 0.3536, p 0.0); driver zc 1.64 → expected 1.229%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.364, β 0.7561, p 0.0); driver zc 1.59 → expected 1.102%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.361, β -2.4545, p 0.00539); driver zc 2.05 → expected -4.499%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.341, β 0.5382, p 0.0); driver zc 2.05 → expected 0.986%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.311, β 0.4773, p 0.00018); driver zc 1.59 → expected 0.696%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_ms → kospi: leads 1d (ccf 0.301, β 0.3389, p 0.0); driver zc 1.64 → expected 1.178%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.297, β 0.3639, p 0.0); driver zc 2.05 → expected 0.667%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_infy → dyn_techm_ns: leads 1d (ccf 0.28, β 0.2386, p 0.0); driver zc -1.8 → expected -1.297%. Type hit-rate 0.808 (n=3275).
- **SETUP** nasdaq_100 → nifty_metal: leads 1d (ccf 0.277, β 0.3109, p 0.00047); driver zc 2.14 → expected 0.976%. Type hit-rate 0.808 (n=3275).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.272, β 0.3244, p 0.0); driver zc 1.59 → expected 0.473%. Type hit-rate 0.808 (n=3275).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.265, β 0.3784, p 0.0); driver zc 2.05 → expected 0.694%. Type hit-rate 0.808 (n=3275).
- Track record · residual_reversion: hit-rate **0.492** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.808** (n=3275) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 15.02] cross-asset · 5 series ↑
- dyn_msft [EQUITIES]: last 455.58, z20 11.09, zc 10.42, resid-z 0.65 [moved], 1d 16.66%, |z20|=11.09
- eur_usd [FX]: last 1.15, z20 4.46, zc 3.81, resid-z 4.23 [unexplained], 1d 1.24%, |z20|=4.46
- usd_jpy [FX]: last 159.67, z20 -4.11, zc -8.29, resid-z -8.11 [unexplained], 1d -2.56%, |z20|=4.11
- aud_usd [FX]: last 0.70, z20 1.96, zc 1.61, resid-z 2.13 [unexplained], 1d 0.76%, |z20|=1.96
- usd_mxn [FX]: last 17.35, z20 -1.88, zc -1.09, resid-z -1.46 [quiet], 1d -0.49%, |z20|=1.88
- **Mechanism**: The surge in Microsoft's shares has triggered a cross-asset move, with the stock's 16% jump easing concerns over AI spending and reinforcing investor confidence in its long-term artificial intelligence strategy and cloud leadership. This move is propagating through the valid vix_equity_inverse channel, where a vol spike would typically lead to an equity drawdown, but in this case, the strong earnings have led to a risk-on sentiment. The move is also influenced by the metal_copper_channel, where global copper leads Indian metal equities, and the gold_silver_comove channel, where monetary metals co-move.
- **Gap**: No gap: The big raw move in Microsoft's shares is largely priced, with a resid_z of 0.65, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument dyn_thangamayl_ns has reacted to the move in Microsoft's shares, with a rho of -0.368. The eur_inr has also reacted, with a rho of 0.367 via eur_usd.
- Watch next: dyn_msft (up) — already moved; Strong earnings and guidance
- Watch next: eur_usd (up) — not yet - watch; Resid_z is high, indicating unexplained movement
- **India receivers**: dyn_thangamayl_ns (rho -0.368, z -2.53); eur_inr (rho 0.367, z 1.57)
- Source: Microsoft shares surge 16% as AI cloud bet starts showing up in numbers — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/microsoft-shares-surge-16-as-ai-cloud-bet-starts-showing-up-in-numbers/articleshow/132742769.cms
- Source: Microsoft jumps over 15% after results, Meta sinks 9% as AI concerns weigh investor sentiment — What we know — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/meta-sinks-9-pc-microsoft-jumps-15-pc-results-earnings-us-tech-stocks-invest-artificial-intelligence-ai-concern-business-11785418926072.html
- Source: US stocks: US market advances as Microsoft results ease AI spending fears — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-opens-higher-as-microsofts-results-temper-some-ai-jitters/articleshow/132741802.cms
- Historical analogues: 2025-04-02 (d=0.53), 2025-08-15 (d=0.57), 2025-10-30 (d=0.58)

### [RED 7.01] dxy ↓
- dxy [FX]: last 99.97, z20 -4.01, zc -2.50, resid-z -0.17 [priced], 1d -0.83%, 20d range extreme; |z20|=4.01
- **Mechanism**: The recent decline in the US Dollar Index (DXY) is a priced move with a small resid_z, indicating that it is largely explained by factor exposures. The move may propagate through the VALID gold_silver_comove channel, as monetary metals tend to co-move. However, the INVERTED safe_haven_gold channel suggests that the traditional risk-off safe-haven bid for gold may not be in play.
- **Gap**: No gap: the move in DXY is largely priced, with a small resid_z of -0.17
- **India take**: The Indian instrument that expresses this move is likely to be the USDINR, which may weaken due to the decline in DXY. However, the WEAK dxy_inr_channel suggests that this transmission may not be robust.
- Watch next: ust_2y (down) — not yet - watch; historically leads DXY by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 6.24] cross-asset · 6 series ↑
- ftse_100 [INDICES]: last 10886.25, z20 2.09, zc -0.30, resid-z -1.40 [quiet], 1d -0.20%, |z20|=2.09; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.48, z20 2.08, zc 1.47, resid-z 0.52 [quiet], 1d 3.31%, |z20|=2.08; 1y-pct=95; co-occur[metal_copper] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4168.00, z20 1.68, zc 2.47, resid-z -0.85 [priced], 1d 3.30%, |z20|=1.68
- cac_40 [INDICES]: last 8476.16, z20 1.41, zc 0.92, resid-z -0.08 [quiet], 1d 0.81%, 1y-pct=96
- dax [INDICES]: last 25574.62, z20 1.25, zc 0.49, resid-z -0.79 [quiet], 1d 0.45%, 1y-pct=98
- stoxx_50 [INDICES]: last 6334.67, z20 0.91, zc 1.48, resid-z 0.38 [quiet], 1d 1.37%, 1y-pct=98
- **Mechanism**: The recent move in global markets, particularly in commodities such as copper and gold, is driven by a combination of factors including market sentiment and economic indicators. The VALID metal_copper_channel and gold_silver_comove channels suggest a co-movement between these metals and potential transmission to Indian metal equities. However, the INVERTED safe_haven_gold channel indicates a risk-off sentiment, which may lead to a gold bid and impact the Indian market.
- **Gap**: No gap: the big raw move in commodities such as copper and gold has a small resid_z, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has already reacted to global market sentiment. The nifty_midcap_100 has not yet moved, but is worth watching.
- Watch next: nifty_50 (up) — already moved; reacted to global market sentiment
- Watch next: nifty_midcap_100 (up) — not yet - watch; quiet despite global market moves
- **India receivers**: nifty_50 (rho 0.549, z 1.01); nifty_midcap_100 (rho 0.536, z 0.51)
- Source: Gold futures slip to ₹1.41 lakh/10g on firm US dollar — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/gold/gold-futures-slip-to-141-lakh10g-on-firm-us-dollar/article71284840.ece
- Source: Today’s Gold Rate in India July 30: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-july-30-2026/article71284521.ece
- Source: India’s gold demand falls 6% as volatile prices turn away consumers — BusinessLine Mkts, 2026-07-30. https://www.thehindubusinessline.com/markets/gold/indias-gold-demand-falls-6-as-volatile-prices-turn-away-consumers/article71284287.ece
- Historical analogues: 2026-03-31 (d=0.78), 2025-07-28 (d=0.87), 2024-11-07 (d=0.88)

### [RED 5.9] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 40010.41, z20 -2.58, zc -0.02, resid-z -0.07 [quiet], 1d -0.07%, |z20|=2.58
- kospi [INDICES]: last 5609.33, z20 -2.28, zc -0.16, resid-z -0.46 [quiet], 1d -0.95%, |z20|=2.28
- nikkei_225 [INDICES]: last 61807.90, z20 -2.15, zc 0.26, resid-z 0.09 [quiet], 1d 0.61%, |z20|=2.15
- **Mechanism**: The recent decline in global indices, including Taiwan Weighted, Kospi, and Nikkei 225, is largely priced in, with small resid_z values indicating that the moves are mostly explained by factor exposures. The transmission channels from these indices to Indian instruments, such as dyn_hdbfs_bo, nifty_metal, and dyn_techm_ns, have already reacted, suggesting that the Indian market has largely absorbed the global sentiment. The valid channels, including gold_silver_comove and metal_copper_channel, do not indicate any significant risk-off or safe-haven bids that would exacerbate the decline.
- **Gap**: No gap: the decline in global indices is largely priced in, with small resid_z values and reacted transmission channels
- **India take**: The Indian market, as expressed through instruments like nifty_midcap_100, may still react to the weak global cues, but the extent of the decline is likely to be limited due to the already reacted transmission channels. The Indian instruments, such as dyn_hdbfs_bo and nifty_metal, have already shown a reaction to the global sentiment.
- Watch next: nifty_midcap_100 (down) — not yet - watch; weak global cues and lack of domestic triggers
- **India receivers**: dyn_hdbfs_bo (rho 0.481, z -1.74); nifty_metal (rho 0.441, z 1.56); dyn_techm_ns (rho -0.421, z 2.13); dyn_pcjeweller_ns (rho 0.412, z -1.59)
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html

### [RED 5.4] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 31188.45, z20 2.57, zc 0.12, resid-z 0.17 [quiet], 1d 0.21%, |z20|=2.57
- dyn_techm_ns [EQUITIES]: last 1669.00, z20 2.13, zc 0.79, resid-z 0.67 [quiet], 1d 1.51%, |z20|=2.13
- **Mechanism**: The recent acquisition of Mahindra & Mahindra's Truck and Bus Division by SML Mahindra has sparked a rally in the stock, with potential synergies and earnings accretion driving the move. This event may propagate through the metal_copper_channel, given the industry overlap, and potentially influence other Indian metal equities. However, the current move in Nifty IT and Dyn Techm NS appears priced, with resid_z values of 0.11 and 0.62, respectively, indicating that the majority of the move can be explained by factor exposures.
- **Gap**: No gap: the current move in Nifty IT and Dyn Techm NS appears priced, with resid_z values indicating that the majority of the move can be explained by factor exposures
- **India take**: The Indian instrument that expresses this move is Dyn Tata Elxsi NS, which has not yet reacted but may potentially move in tandem with Nifty IT. The acquisition news may also influence other Indian metal equities, such as those in the commercial vehicle portfolio.
- Watch next: dyn_tataelxsi_ns (up) — not yet - watch; correlated instrument with rho=0.674 vs Nifty IT
- **India receivers**: dyn_tataelxsi_ns (rho 0.674, z 0.49)
- Source: SML Mahindra shares rally over 18% on acquisition of M&M’s truck division. What it means for shareholders? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-shares-rally-over-18-on-acquisition-of-mahindra-mahindras-truck-and-bus-division-what-does-it-mean-for-shareholders/articleshow/132729786.cms
- Source: SML Mahindra to acquire Mahindra Truck and Bus division in commercial vehicle consolidation — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/sml-mahindra-to-acquire-mahindra-truck-and-bus-division-in-commercial-vehicle-consolidation/articleshow/132709583.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.14] dyn_meta ↓
- dyn_meta [EQUITIES]: last 531.18, z20 -3.14, zc -3.85, resid-z 0.01 [moved], 1d -9.29%, |z20|=3.14; 1y-pct=0
- **Mechanism**: The decline in dyn_meta is largely priced, with a small resid_z of 0.01, indicating that the move is mostly explained by factor exposures. The drop in Meta's shares is attributed to concerns over AI spending and its impact on profits, while Microsoft's strong earnings report has boosted investor sentiment. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, which could propagate to Indian markets through transmission candidates such as nifty_midcap_100 and midcap_largecap_ratio.
- **Gap**: No gap: the decline in dyn_meta is largely priced, with a small resid_z of 0.01, indicating that the move is mostly explained by factor exposures
- **India take**: Indian instruments such as nifty_midcap_100 and midcap_largecap_ratio may react to the decline in dyn_meta, but have not yet shown significant movement. dyn_hdbfs_bo and dyn_eternal_ns have already reacted, potentially indicating a transmission of the US market sentiment to Indian markets.
- Watch next: nifty_midcap_100 (down) — quiet; rho=0.448 via dyn_meta
- Watch next: midcap_largecap_ratio (down) — quiet; rho=0.388 via dyn_meta
- **India receivers**: nifty_midcap_100 (rho 0.448, z 0.51); midcap_largecap_ratio (rho 0.388, z -0.52); dyn_hdbfs_bo (rho 0.388, z -1.74); dyn_eternal_ns (rho 0.383, z 2.6)
- Source: Microsoft jumps over 15% after results, Meta sinks 9% as AI concerns weigh investor sentiment — What we know — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/meta-sinks-9-pc-microsoft-jumps-15-pc-results-earnings-us-tech-stocks-invest-artificial-intelligence-ai-concern-business-11785418926072.html
- Source: META - EVERCORE REMOVES META FROM TOP PICK LIST Evercore ISI removed Meta from its TAP Outperform List but maintained an Outperform rating, cutting its price target to $820 from $930. The firm cited rising AI spending, limited visibility on future capex, and a lack of clear — DeItaone, 2026-07-30. https://t.me/walter_bloomberg/34078
- Source: Market Focus: Meta's higher AI budget jolts shares, signals long-term push — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/market-focus-metas-higher-ai-budget-jolts-shares-signals-long-term-push/slideshow/132730549.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [AMBER 4.88] cross-asset · 4 series ↑
- tips_10y_real [RATES]: last 2.41, z20 1.22, zc -0.74, resid-z -0.93 [quiet], 1d -1.23%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.86, z20 -0.82, zc 0.42, resid-z 0.22 [quiet], 1d 0.12%, 1y-pct=2
- ust_2y [RATES]: last 4.26, z20 0.71, zc -0.90, resid-z -0.95 [quiet], 1d -1.16%, 1y-pct=97
- ust_10y [RATES]: last 4.61, z20 0.55, zc -0.91, resid-z -0.95 [quiet], 1d -0.86%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.819 vs tips_10y_real
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.564 vs tips_10y_real, historically leads by 4d
- Watch next: wti (inverse) — not yet - watch; rho -0.549 vs dyn_bond, historically leads by 3d
- Watch next: ust_2s10s (inverse) — not yet - watch; rho -0.548 vs ust_2y, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.542 vs tips_10y_real, historically leads by 4d
- Source: UK bond yields and sterling dip after BoE holds rates steady — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-and-sterling-dip-after-boe-holds-rates-steady/articleshow/132740517.cms
- Source: TREASURY YIELDS HIT 19-YEAR HIGH US Treasury yields climbed after the Federal Reserve held interest rates, with the 30-year yield reaching a 19-year high of 5.24%. Three Fed officials dissented in favor of a rate hike, highlighting concerns over persistent inflation. The — DeItaone, 2026-07-30. https://t.me/walter_bloomberg/34086
- Source: Sensex, Nifty 50 rise, but mid, small-caps falter; rising US bond yields keep investors cautious — Mint Markets, 2026-07-30. https://www.livemint.com/market/stock-market-news/sensex-nifty-50-rise-but-mid-small-caps-falter-rising-us-bond-yields-keep-investors-cautious-11785405396383.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.31), 2025-05-23 (d=0.52)

### [RED 4.6] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 310.20, z20 2.60, zc -0.22, resid-z -0.57 [quiet], 1d -0.51%, |z20|=2.60
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.556 via dyn_eternal_ns, z 0.51, quiet); dyn_jiofin_bo (rho 0.422 via dyn_eternal_ns, z 1.93, reacted); nifty_50 (rho 0.404 via dyn_eternal_ns, z 1.01, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.556 vs dyn_eternal_ns, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.556, z 0.51); dyn_jiofin_bo (rho 0.422, z 1.93); nifty_50 (rho 0.404, z 1.01)
- Source: Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/eternal-shares-jump-over-20-in-one-month-will-the-stock-cross-its-october-peak-of-rs-368/articleshow/132700500.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

## Watchlist (below surfacing floor)
dyn_waareeener_bo ↓ (4.57), dyn_thangamayl_ns ↓ (4.53), dyn_chkp ↓ (4.17), gold_silver_ratio ↑ (4.06), dyn_lth ↑ (4.0), dyn_cupid_ns ↑ (3.75), dyn_tech ↑ (3.54), usd_cny ↓ (3.39), dyn_301077_sz ↓ (3.27), hy_oas ↑ (3.22), dyn_bac ↑ (3.07), commodities · 2 series ↑ (3.03)

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
- INDIANB.NS (INDIAN BANK) score 78.5 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.1 — "Maruti Q1 Results Preview: What could lead to a profit decline for India's largest carmake"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 65.7 — "Maruti Q1 Results Preview: What could lead to a profit decline for India's largest carmake"
- BAC (Bank of America Corporation) score 64.8 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- COALINDIA.NS (COAL INDIA LTD) score 62.7 — "Maruti Q1 Results Preview: What could lead to a profit decline for India's largest carmake"
- HDB (HDFC Bank Limited) score 60.8 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.5 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- IDBI.NS (IDBI BANK LIMITED) score 58.1 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.8 — "SOUTH KOREA WEIGHS SHORT-SELLING BAN The Korea Exchange has reportedly reviewed the techni"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.3 — "SOUTH KOREA WEIGHS SHORT-SELLING BAN The Korea Exchange has reportedly reviewed the techni"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 53.2 — "FED UNCERTAINTY CLOUDS DOLLAR OUTLOOK MUFG warned the dollar outlook has deteriorated afte"
- COIN (Coinbase Global, Inc.) score 51.7 — "Commodity experts, policymakers to brainstorm at 3-day Global Commodity Conclave in Mumbai"
- OHI (Omega Healthcare Investors, In) score 51.7 — "AI Big Short? Why rising credit default swaps are spooking investors and how is it similar"
- TECH (Bio-Techne Corp) score 34.6 — "SOUTH KOREA WEIGHS SHORT-SELLING BAN The Korea Exchange has reportedly reviewed the techni"
- LTH (Life Time Group Holdings, Inc.) score 30.4 — "Study moots phased time-bound reduction of import duty on aluminium to zero"
- CHKP (Check Point Software Technolog) score 29.1 — "Dhaval Packaging IPO Day 1: Issue booked 26% so far. Check GMP, issue details"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.0 — "India bonds slip on Fed uncertainty, war worries"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.2 — "Juniper Green Energy IPO booked 38% on Day 1; QIB portion fully subscribed"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 21.5 — "Market wrap: M&M, Coal India, Adani Ports among top gainers and losers on Nifty and Sensex"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.3 — "Tata Steel Q1 Results: Profit rises 15% to Rs 2,318 crore, revenue climbs 14%"
- MS (Morgan Stanley) score 16.2 — "Investors are overlooking healthcare stocks and should consider these top picks, says JPMo"
- 301077.SZ (CHINASTARS) score 15.7 — "China’s October plenum plan reveals focus on party discipline ahead of 2027 congress"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.8 — "Market wrap: M&M, Coal India, Adani Ports among top gainers and losers on Nifty and Sensex"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.2 — "Shell Reports $9.8 Billion in Adjusted Earnings as Energy Prices Surge"
- META (Meta) score 10.2 — "META - EVERCORE REMOVES META FROM TOP PICK LIST Evercore ISI removed Meta from its TAP Out"
- INFY (Infosys Limited) score 9.9 — "Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty end"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.2 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- JIOFIN.BO (Jio Financial Services Limited) score 8.9 — "My financial adviser says I don’t need a tax-efficient withdrawal plan for my $2.3 million"
- VT (Vanguard Total World Stock Ind) score 7.7 — "The World Cup winners wore Adidas shirts. But the company’s investors are still crying fou"
- GS (Goldman Sachs Group, Inc. (The) score 6.7 — "Goldman Sachs: Diesel Crunch Is Now the Biggest Threat in Oil Markets"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.4 — "My financial adviser says I don’t need a tax-efficient withdrawal plan for my $2.3 million"
- NVDA (NVIDIA Corporation) score 6.0 — "Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor"
- AAPL (Apple Inc.) score 6.0 — "Qualcomm shares fall 5% as higher costs, Apple-related weakness cloud profit forecast"
- MSFT (Microsoft Corporation) score 5.8 — "US stock market today: Wall Street futures recover from Fed-led losses; Microsoft jumps 10"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.6 — "ICICI Prudential MF buys stake in Go Digit General Insurance for ₹139 crore"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 4.1 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- ETERNAL.NS (ETERNAL LIMITED) score 4.0 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- WAAREEENER.BO (Waaree Energies Limited) score 3.6 — "Q1 Results Today Highlights: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹6"
- CUPID.NS (CUPID LIMITED) score 1.8 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"
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