# Transmission Layer — board brief · 2026-07-29 07:53Z

data as of **2026-07-29** · 98 series · 11 red / 41 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.477, 4d in regime; vol-pct 0.62, breadth-off 0.333, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.44, contra nifty_50 corr20=0.32, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.33, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.01, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.52, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_infy → dyn_techm_ns: leads 1d (ccf 0.28, β 0.2381, p 0.0); driver zc 1.93 → expected 1.323%. Type hit-rate 0.817 (n=3240).
- Track record · residual_reversion: hit-rate **0.492** (n=1136) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3240) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.87] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.60, z20 4.87, zc 1.97, resid-z -0.11 [moved], 1d 4.20%, |z20|=4.87; 1y-pct=100
- **Mechanism**: The recent surge in dyn_lth is largely priced, with a small resid_z of -0.11, indicating that the move is mostly explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may propagate this move, potentially influencing Indian metal equities. However, the weak channels, including inr_oil_channel and dxy_inr_channel, may limit the transmission of this move to the Indian market.
- **Gap**: No gap: the small resid_z of -0.11 suggests that the move is mostly priced, with no significant unexplained component
- **India take**: The Indian instrument that may express this move is the Nifty Metal index, which may react negatively due to the potential risk-off sentiment. However, the reaction has not yet occurred, and the index is still watching for further developments.
- Watch next: nifty_50 (down) — not yet - watch; Potential risk-off sentiment may impact Indian equities
- Source: Gold price outlook: Chris Wood of Jefferies says it's time to buy gold again; believes next rally could be bigger — Mint Markets, 2026-07-28. https://www.livemint.com/market/commodities/gold-price-outlook-chris-wood-of-jefferies-says-its-time-to-buy-gold-again-believes-next-rally-could-be-bigger-11785232982540.html
- Source: US Fed meeting begins today: Check date, time and where to watch Kevin Warsh's speech — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/us-fed-meeting-begins-today-check-date-time-and-where-to-watch-kevin-warshs-speech-11785222523367.html
- Source: HUL shares slide 5% after weaker-than-expected Q1; PAT dips 3% to Rs 2,673 crore on one-time credit — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-slide-5-after-weaker-than-expected-q1-pat-dips-3-to-rs-2673-crore-on-one-time-credit/articleshow/132676380.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 6.66] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 40025.12, z20 -3.34, zc -1.29, resid-z -2.27 [unexplained], 1d -3.79%, |z20|=3.34
- nikkei_225 [INDICES]: last 61429.44, z20 -2.79, zc -0.56, resid-z -1.81 [unexplained], 1d -1.50%, |z20|=2.79
- kospi [INDICES]: last 5634.66, z20 -2.53, zc -1.10, resid-z -2.57 [unexplained], 1d -6.39%, |z20|=2.53
- **Mechanism**: The recent decline in global indices, including Taiwan Weighted, Nikkei 225, and Kospi, is driven by unexplained moves with significant resid_z values, indicating that these declines are not fully priced in by factor exposures. This move is likely to propagate through the valid channels, such as the vix_equity_inverse channel, which shows a strong inverse correlation between vol spike and equity drawdown. The metal_copper_channel also provides a potential transmission mechanism, given the co-movement between global copper prices and Indian metal equities.
- **Gap**: No gap: the declines in global indices are largely unexplained, but the Indian transmission candidates have already reacted, suggesting that the event-to-price gap has been largely closed
- **India take**: The Indian instruments, such as dyn_hdbfs_bo, nifty_metal, dyn_techm_ns, and dyn_pcjeweller_ns, have already reacted to the global index moves, with most of them showing a decline in line with the global market sentiment. The Nifty is likely to open higher, but the underlying sentiment is expected to remain cautious due to geopolitical tensions in the Middle East.
- Watch next: dyn_hdbfs_bo (down) — already moved; reacted to Nikkei 225 move
- Watch next: nifty_metal (down) — already moved; reacted to Kospi move
- Watch next: dyn_techm_ns (up) — already moved; reacted to Taiwan Weighted move
- Watch next: dyn_pcjeweller_ns (down) — already moved; reacted to Taiwan Weighted move
- **India receivers**: dyn_hdbfs_bo (rho 0.468, z -2.11); nifty_metal (rho 0.443, z 1.53); dyn_techm_ns (rho -0.414, z 2.02); dyn_pcjeweller_ns (rho 0.387, z -1.41)
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html
- Source: GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. selloff, fueled by concerns over AI spending and China's technological progress. South Korea's Kospi plunged 10%, triggering two trading halts, while Japan's Nikkei fell 4%. U.S. chip stocks — DeItaone, 2026-07-28. https://t.me/walter_bloomberg/33992

### [RED 6.56] indices · 4 series ↑
- ftse_100 [INDICES]: last 10924.18, z20 2.90, zc 0.61, resid-z 0.31 [quiet], 1d 0.49%, |z20|=2.90; 1y-pct=100
- cac_40 [INDICES]: last 8478.97, z20 1.50, zc 0.25, resid-z -0.25 [quiet], 1d 0.23%, 1y-pct=96
- dax [INDICES]: last 25519.02, z20 1.16, zc 0.22, resid-z -0.22 [quiet], 1d 0.22%, 1y-pct=98
- dow_jones [INDICES]: last 52731.60, z20 1.01, zc 1.29, resid-z 0.89 [quiet], 1d 1.00%, 1y-pct=98
- **Mechanism**: The recent surge in US stocks, particularly the Dow Jones, has been driven by investor expectations of positive earnings and a potential dovish stance from the Federal Reserve. This move has been priced in, with small resid_z values indicating that the factor exposures have largely explained the price movement. The valid vix_equity_inverse channel suggests that the current low volatility environment may persist, supporting the equity market. However, the weak inr_oil_channel and dxy_inr_channel imply that the Indian Rupee may weaken if oil prices rise or the US dollar strengthens, potentially affecting Indian equities.
- **Gap**: No gap: the recent move in US stocks has been largely priced in, with small resid_z values indicating that factor exposures have explained the price movement.
- **India take**: The Nifty 50, which has a historical lead of 1 day vs the CAC 40, may react positively to the US stock market surge, while the Nifty Midcap 100 may also follow the DAX's lead. However, the Indian Rupee's potential weakness due to oil price rises or US dollar strength may affect Indian equities.
- Watch next: nifty_50 (up) — not yet - watch; historical lead of 1 day vs cac_40
- **India receivers**: nifty_50 (rho 0.603, z 0.82); nifty_midcap_100 (rho 0.584, z 0.88)
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks turn positive as Dow surges 650 pts despite chip rout — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-brent-crude-oil-fed-warsh-rate-hike-big-tech-earnings-amazon-meta-apple-microsoft-tesla-spacex-chip-stock-price-news-28th-june-2026/liveblog/132684702.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Dow soars 500 pts despite tech slump as investors eye earnings, Fed meet — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-brent-crude-oil-fed-warsh-rate-hike-big-tech-earnings-amazon-meta-apple-microsoft-tesla-spacex-chip-stock-price-news-28th-june-2026/liveblog/132684702.cms
- Source: U.S. STOCKS EXTEND GAINS, DOW JONES UP 1.08% — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33935
- Historical analogues: 2024-11-11 (d=0.71), 2024-11-21 (d=0.97), 2024-10-11 (d=1.0)

### [AMBER 6.37] commodities · 2 series ↑
- wti [COMMODITIES]: last 81.85, z20 0.54, zc 0.99, resid-z -1.06 [quiet], 1d 3.27%, 1-session move +3.27% ≥ 1.5%
- brent [COMMODITIES]: last 86.94, z20 0.45, zc 0.87, resid-z -1.33 [quiet], 1d 3.39%, 1-session move +3.39% ≥ 1.5%
- **Mechanism**: The recent surge in commodities, particularly WTI and Brent crude oil, is driven by supply concerns and geopolitical tensions, which has led to a price increase. However, the resid_z values for both WTI and Brent are negative, indicating that the move is largely priced in and not an anomaly. The valid metal_copper_channel and gold_silver_comove channels suggest that the commodity move may have implications for Indian metal equities and the broader commodity complex.
- **Gap**: No gap: The recent move in commodities is largely priced in, as evidenced by the negative resid_z values for WTI and Brent.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has a negative correlation with Brent crude oil. However, it has not reacted yet, and its z20 level is 0.88, indicating a quiet move so far.
- Watch next: nifty_midcap_100 (down) — not yet - watch; Historical lead of 1d and negative correlation with WTI
- Watch next: dyn_bond (up) — not yet - watch; Negative correlation with WTI
- **India receivers**: nifty_midcap_100 (rho -0.572, z 0.88); midcap_largecap_ratio (rho -0.452, z 0.09)
- Source: Q1 Results Today Live: Adani Ports profit jumps, Colgate Q1 PAT up 7%, Craftsman Automation logs ₹94 cr profit, Thangamayil Jewellery shares tank 10% after results, Adani Enterprises, Asian Paints, Eicher Motors, Waaree Energies, Prestige Estates, Dabur, Vedanta Oil, ACME Solar to announce Q1 results — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-adani-enterprises-adani-ports-asian-paints-eicher-motors-waaree-energies-colgate-prestige-estates-syrma-sgs-tech-dabur-hexaware-tech-vedanta-oil-acme-results-29-july-2026/article71276282.ece
- Source: India bonds tiptoe along ahead of Fed meet; oil prices weigh — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/bonds/india-bonds-tiptoe-along-ahead-of-fed-meet-oil-prices-weigh/articleshow/132703905.cms
- Source: New Zealand Awards First Offshore Oil License Since Ending Drilling Ban — OilPrice, 2026-07-29. https://oilprice.com/Latest-Energy-News/World-News/New-Zealand-Awards-First-Offshore-Oil-License-Since-Ending-Drilling-Ban.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.02] dyn_infy ↑
- dyn_infy [EQUITIES]: last 12.35, z20 4.02, zc 1.93, resid-z 1.60 [unexplained], 1d 5.56%, |z20|=4.02
- **Mechanism**: The recent surge in Indian IT stocks, led by Infosys and TCS, is driven by strong Q1 earnings, optimism around AI-driven demand, and improving investor sentiment. This move is propagated through the verified transmission setup between dyn_infy and dyn_techm_ns, where dyn_infy leads dyn_techm_ns by 1 day. The channel status indicates a valid vix_equity_inverse relationship, suggesting that the vol spike may lead to an equity drawdown, but the current move is driven by fundamentals rather than risk-off sentiment.
- **Gap**: No gap: the move in dyn_infy is largely explained by its fundamentals and transmission to other IT stocks, with a relatively small resid_z of 1.6 indicating that the move is mostly priced in.
- **India take**: The Indian IT sector, particularly Nifty IT and stocks like TCS, Infosys, and Tech Mahindra, have reacted positively to the Q1 earnings and AI-driven demand optimism, with nifty_it and dyn_techm_ns already showing a reaction.
- Watch next: dyn_techm_ns (up) — reacted; follows dyn_infy
- **India receivers**: nifty_it (rho 0.599, z 2.77); dyn_techm_ns (rho 0.582, z 2.02); dyn_tataelxsi_ns (rho 0.378, z 0.66)
- Source: TCS vs Infosys vs Wipro vs HCL Tech: Which IT stock to buy after Q1 results? — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/tcs-vs-infosys-vs-wipro-vs-hcl-tech-which-it-stock-to-buy-after-q1-results-11785302857002.html
- Source: IT stocks on a roll: TCS, Infosys, Coforge and others rally up to 5% for second straight day. What's driving this surge? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/it-stocks-on-a-roll-tcs-infosys-coforge-and-others-rally-up-to-5-for-second-straight-day-whats-driving-this-surge/articleshow/132701697.cms
- Source: TCS, Infosys, Coforge, other IT stocks rally up to 10% after Nvidia-led chip rout. Is AI trade ending? — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/tcs-infosys-coforge-other-it-stocks-rally-up-to-10-after-nvidia-led-chip-rout-is-ai-trade-ending/articleshow/132675510.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

### [RED 5.96] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 313.20, z20 3.96, zc 0.65, resid-z -0.08 [quiet], 1d 1.57%, |z20|=3.96
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.582 via dyn_eternal_ns, z 0.88, quiet); dyn_jiofin_bo (rho 0.474 via dyn_eternal_ns, z 2.07, reacted); nifty_50 (rho 0.451 via dyn_eternal_ns, z 0.82, quiet); dyn_havells_ns (rho 0.427 via dyn_eternal_ns, z 2.13, reacted); dyn_indusindbk_bo (rho 0.398 via dyn_eternal_ns, z 0.07, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.582 vs dyn_eternal_ns, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.582, z 0.88); dyn_jiofin_bo (rho 0.474, z 2.07); nifty_50 (rho 0.451, z 0.82); dyn_havells_ns (rho 0.427, z 2.13)
- Source: Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/eternal-shares-jump-over-20-in-one-month-will-the-stock-cross-its-october-peak-of-rs-368/articleshow/132700500.cms
- Source: Market wrap: TCS, Eternal, HUL, BEL among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-eternal-hul-bel-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132684231.cms
- Source: Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/eternal-among-4-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/132674117.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

### [AMBER 5.72] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.44, z20 1.79, zc 0.00, resid-z -0.30 [quiet], 1d 0.41%, |z20|=1.79; 1y-pct=100
- ust_2y [RATES]: last 4.31, z20 1.52, zc -0.71, resid-z -1.16 [quiet], 1d -0.46%, |z20|=1.52; 1y-pct=98
- ust_10y [RATES]: last 4.65, z20 1.11, zc -0.44, resid-z -0.72 [quiet], 1d -0.85%, 1y-pct=98
- ust_30y [RATES]: last 5.12, z20 0.83, zc -0.30, resid-z -0.44 [quiet], 1d -0.78%, 1y-pct=97
- dyn_bond [EQUITIES]: last 91.06, z20 -0.52, zc 0.97, resid-z 0.09 [quiet], 1d 0.28%, 1y-pct=3
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2s10s (inverse) — not yet - watch; rho -0.544 vs ust_2y, historically leads by 1d
- Watch next: wti (co-move) — not yet - watch; rho 0.509 vs ust_10y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.653 vs tips_10y_real
- Watch next: dxy (co-move) — not yet - watch; rho 0.534 vs tips_10y_real
- Watch next: brent (inverse) — not yet - watch; rho -0.521 vs dyn_bond
- Source: US Stock Market: Bond investors turn cautious ahead of Fed meeting as inflation risks cloud rate outlook — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-bond-investors-turn-cautious-ahead-of-fed-meeting-as-inflation-risks-cloud-rate-outlook/articleshow/132699838.cms
- Source: Investors are piling into bond funds at a rapid rate. That’s a problem — but not for stocks. — MarketWatch Top, 2026-07-28. https://www.marketwatch.com/story/investors-are-piling-into-bond-funds-at-a-rapid-rate-thats-a-problem-09aaa039?mod=mw_rss_topstories
- Source: Treasury yields retreat as oil tumbles before Fed policy decision — Mint Markets, 2026-07-28. https://www.livemint.com/market/treasury-yields-retreat-as-oil-tumbles-before-fed-policy-decision-11785264502739.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.6] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 31129.10, z20 2.77, zc 1.33, resid-z 0.64 [quiet], 1d 2.34%, |z20|=2.77
- dyn_techm_ns [EQUITIES]: last 1647.50, z20 2.02, zc 0.39, resid-z -0.42 [quiet], 1d 0.75%, |z20|=2.02
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.695 via nifty_it, z 0.66, quiet); nifty_50 (rho 0.389 via nifty_it, z 0.82, quiet); dyn_jiofin_bo (rho 0.376 via nifty_it, z 2.07, reacted)
- Watch next: dyn_tataelxsi_ns (co-move) — not yet - watch; rho 0.695 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.695, z 0.66); nifty_50 (rho 0.389, z 0.82); dyn_jiofin_bo (rho 0.376, z 2.07)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Surges Past Resistance — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-live-updates-28-jul-2026/liveblog/132674133.cms
- Source: Stocks to buy for short term: BHEL, Mahindra and Mahindra among 6 stocks experts recommend for next 1-2 weeks — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/stocks-to-buy-for-short-term-bhel-mahindra-and-mahindra-among-6-stocks-experts-recommend-for-next-1-2-weeks-11785165963810.html
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

## Watchlist (below surfacing floor)
dyn_coalindia_ns ↓ (5.32), cross-asset · 2 series ↑ (4.9), asx_200 ↑ (4.51), nasdaq_100 ↓ (4.47), commodities · 3 series ↑ (4.16), dyn_ohi ↑ (3.89), dyn_tech ↑ (3.86), gold_silver_ratio ↑ (3.77), dyn_bac ↑ (3.71), natgas ↓ (3.66), dyn_aapl ↑ (3.58), dyn_hdb ↓ (3.29)

## India macro
- nifty_50: 24249.4492 (1d 1.10%, z20 0.82, flag none)
- nifty_midcap_100: 62801.5000 (1d 0.61%, z20 0.88, flag amber)
- usd_inr: 95.5675 (1d -0.22%, z20 -0.73, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5898 (1d -0.49%, z20 0.09, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 76.4 — "JSW One Platforms appoints bankers for $350-400 million IPO next year"
- INOXINDIA.NS (INOX INDIA LIMITED) score 69.3 — "Go Digit, Graphite India, RVNL, HUDCO, Tanla Platforms, Euro Panel in focus today"
- BAC (Bank of America Corporation) score 61.3 — "JSW One Platforms appoints bankers for $350-400 million IPO next year"
- HDB (HDFC Bank Limited) score 60.6 — "JSW One Platforms appoints bankers for $350-400 million IPO next year"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 60.5 — "Go Digit, Graphite India, RVNL, HUDCO, Tanla Platforms, Euro Panel in focus today"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.8 — "JSW One Platforms appoints bankers for $350-400 million IPO next year"
- IDBI.NS (IDBI BANK LIMITED) score 57.0 — "JSW One Platforms appoints bankers for $350-400 million IPO next year"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.2 — "OPENAI'S ROGUE AGENT ABUSED CUSTOMER ACCOUNT AT SECOND TECH COMPANY, SOURCES SAY"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.0 — "OPENAI'S ROGUE AGENT ABUSED CUSTOMER ACCOUNT AT SECOND TECH COMPANY, SOURCES SAY"
- COALINDIA.NS (COAL INDIA LTD) score 53.7 — "Go Digit, Graphite India, RVNL, HUDCO, Tanla Platforms, Euro Panel in focus today"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 50.2 — "JSW One Platforms appoints bankers for $350-400 million IPO next year"
- COIN (Coinbase Global, Inc.) score 49.0 — "Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock "
- OHI (Omega Healthcare Investors, In) score 34.7 — "US Stock Market: Bond investors turn cautious ahead of Fed meeting as inflation risks clou"
- TECH (Bio-Techne Corp) score 29.5 — "OPENAI'S ROGUE AGENT ABUSED CUSTOMER ACCOUNT AT SECOND TECH COMPANY, SOURCES SAY"
- CHKP (Check Point Software Technolog) score 27.7 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- LTH (Life Time Group Holdings, Inc.) score 23.8 — "Swiggy shares jump 8%, rally 15% in 3 days. What's boosting investor sentiment?"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.7 — "Suzlon Energy share price target: Brokerages see up to 35% upside potential. Here’s why"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.9 — "US Stock Market: Bond investors turn cautious ahead of Fed meeting as inflation risks clou"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's stock price rises amidst mixed ret"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.2 — "Stocks to watch: Adani Enterprises, L&T, RVNL among shares in focus today; check list here"
- 301077.SZ (CHINASTARS) score 12.7 — "TRUMP ADMINISTRATION PLANS ON TUESDAY TO ROLL OUT BANS ON FOREIGN IMPORTS OF NEW MODELS OF"
- MS (Morgan Stanley) score 11.8 — "HUL shares rebound 2% after Q1 results. Here's what Morgan Stanley, Motilal Oswal and othe"
- INFY (Infosys Limited) score 11.6 — "IT stocks on a roll: TCS, Infosys, Coforge and others rally up to 5% for second straight d"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.9 — "Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "The U.S. Army Just Called China’s Bluff in the Rare Earth War"
- JIOFIN.BO (Jio Financial Services Limited) score 8.7 — "TSX hits record high, led by tech and financial shares"
- VT (Vanguard Total World Stock Ind) score 8.2 — "The World’s Largest Sand Battery Is Now Online"
- GS (Goldman Sachs Group, Inc. (The) score 7.8 — "L&T shares rise 4% after Q1 earnings. Why Goldman Sachs, other brokerages remain bullish?"
- META (Meta) score 7.5 — "META - *META, BLACKROCK TO DEVELOP DATA CENTER CAMPUS IN EL PASO, TEXAS"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.1 — "BlueStone Jewellery shares soar 7%. Should you buy at current levels or avoid?"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.4 — "TSX hits record high, led by tech and financial shares"
- NVDA (NVIDIA Corporation) score 6.2 — "AAPL - APPLE TOPS $5 TRILLION VALUATION Apple briefly reached a $5 trillion market capital"
- AAPL (Apple Inc.) score 5.9 — "Apple tops $5 trillion market cap in trading, retakes world’s most valuable company title"
- ETERNAL.NS (ETERNAL LIMITED) score 5.6 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- SKHYV (SK hynix Inc. American Deposit) score 5.5 — "Kospi crashes 12% after SK Hynix earnings; best performing Asian market of 2026 plunges 43"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.2 — "Vedanta Aluminium shares in a sweet spot, says ICICI Securities; initiates coverage with B"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.9 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 2.0 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.4 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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