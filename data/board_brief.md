# Transmission Layer — board brief · 2026-07-29 16:56Z

data as of **2026-07-29** · 98 series · 17 red / 34 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.603, 1d in regime; vol-pct 0.793, breadth-off 0.412, Markov P(high-vol) 0.036)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.42, contra nifty_50 corr20=0.28, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.02, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.06, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.53, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.59, β 0.5003, p 0.0); driver zc -1.89 → expected -0.79%. Type hit-rate 0.817 (n=3240).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.502, β 0.2083, p 0.0); driver zc -1.66 → expected -0.652%. Type hit-rate 0.817 (n=3240).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.493, β 0.1964, p 0.0); driver zc -2.03 → expected -0.778%. Type hit-rate 0.817 (n=3240).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.414, β -0.358, p 0.0); driver zc -1.89 → expected 0.565%. Type hit-rate 0.817 (n=3240).
- **SETUP** dyn_gs → usd_brl: leads 1d (ccf -0.385, β -0.1551, p 0.0); driver zc -2.03 → expected 0.614%. Type hit-rate 0.817 (n=3240).
- **SETUP** dow_jones → india_vix: leads 1d (ccf -0.292, β -2.0541, p 0.02719); driver zc -1.89 → expected 3.242%. Type hit-rate 0.817 (n=3240).
- **SETUP** dow_jones → nifty_50: leads 1d (ccf 0.26, β 0.2411, p 0.00014); driver zc -1.89 → expected -0.38%. Type hit-rate 0.817 (n=3240).
- Track record · residual_reversion: hit-rate **0.493** (n=1137) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3240) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.57] cross-asset · 11 series ↓
- dyn_vt [EQUITIES]: last 152.86, z20 -2.69, zc -1.23, resid-z -0.57 [quiet], 1d -0.97%, |z20|=2.69
- nasdaq_100 [INDICES]: last 27416.45, z20 -2.60, zc -0.92, resid-z -1.60 [unexplained], 1d -1.25%, |z20|=2.60
- vix [INDICES]: last 19.96, z20 2.55, zc 1.24, resid-z n/a [quiet], 1d 9.61%, |z20|=2.55
- russell_2000 [INDICES]: last 2908.21, z20 -2.54, zc -1.31, resid-z -0.41 [quiet], 1d -1.54%, |z20|=2.54
- sp500 [INDICES]: last 7364.89, z20 -2.52, zc -1.10, resid-z -0.38 [quiet], 1d -0.86%, |z20|=2.52
- dyn_nvda [EQUITIES]: last 191.85, z20 -2.04, zc -1.12, resid-z -0.37 [quiet], 1d -2.62%, |z20|=2.04
- tips_10y_real [RATES]: last 2.44, z20 1.79, zc 0.00, resid-z -0.30 [quiet], 1d 0.41%, |z20|=1.79; 1y-pct=100
- ust_2y [RATES]: last 4.31, z20 1.52, zc -0.71, resid-z -1.16 [quiet], 1d -0.46%, |z20|=1.52; 1y-pct=98
- ust_10y [RATES]: last 4.65, z20 1.11, zc -0.44, resid-z -0.72 [quiet], 1d -0.85%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.79, z20 -1.07, zc -1.04, resid-z 0.09 [quiet], 1d -0.30%, 1y-pct=2
- ust_30y [RATES]: last 5.12, z20 0.83, zc -0.30, resid-z -0.44 [quiet], 1d -0.78%, 1y-pct=97
- **Mechanism**: The recent drop in equities and rise in volatility, as indicated by the VIX, is driven by concerns over Nvidia's circular financing loop and the potential risks associated with it. This has led to a decline in risk appetite, causing a shift towards safe-haven assets. However, the gold channel is currently inverted, and the real rates gold inverse channel is weak, suggesting that the traditional safe-haven bid may not be effective. Instead, the valid gold silver comove channel and metal copper channel may influence the price of Indian metal equities.
- **Gap**: No gap: the big raw move in equities has a small resid_z, indicating that it is largely priced in
- **India take**: The Indian instrument that expresses this move is nifty_metal, which has already reacted to the decline in dyn_nvda. The metal copper channel may further influence the price of Indian metal equities.
- Watch next: nifty_metal (down) — already moved; reacted to dyn_nvda
- **India receivers**: nifty_metal (rho 0.453, z 1.72)
- Source: Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor — and how big is the risk? — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nvidias-750-billion-circular-financing-loop-how-it-became-banker-supplier-and-investor-and-how-big-is-the-risk-11785243777113.html
- Source: World Nuclear Association: $6 Trillion Needed to Hit 2050 Capacity Goals — OilPrice, 2026-07-29. https://oilprice.com/Latest-Energy-News/World-News/World-Nuclear-Association-6-Trillion-Needed-to-Hit-2050-Capacity-Goals.html
- Source: US Treasury yields rise after three-day fall as oil jumps, Fed decision looms — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/bonds/us-treasury-yields-rise-after-three-day-fall-as-oil-jumps-fed-decision-looms/articleshow/132712865.cms
- Historical analogues: 2026-05-22 (d=0.36), 2026-05-05 (d=0.62), 2025-05-20 (d=0.68)

### [AMBER 6.74] commodities · 2 series ↑
- wti [COMMODITIES]: last 84.50, z20 0.91, zc 2.00, resid-z 1.66 [unexplained], 1d 6.61%, 1-session move +6.61% ≥ 1.5%
- brent [COMMODITIES]: last 90.31, z20 0.84, zc 1.89, resid-z 1.97 [unexplained], 1d 7.40%, 1-session move +7.40% ≥ 1.5%
- **Mechanism**: The recent surge in oil prices, driven by geopolitical tensions between the US and Iran, has led to a significant increase in WTI and Brent crude prices. This move is unexplained by factor exposures, with resid_z values of 1.66 and 1.97 for WTI and Brent, respectively. The risk-off regime and the valid gold_silver_comove channel suggest that safe-haven assets are being sought, which could further drive up oil prices.
- **Gap**: No gap: the big raw move in oil prices is largely priced, given the significant increase in prices and the unexplained component being relatively small compared to the overall move.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has a negative correlation with WTI and has not yet reacted to the surge in oil prices. The midcap_largecap_ratio is another potential candidate, but its reaction is also pending.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 1d and has a negative correlation with WTI
- **India receivers**: nifty_midcap_100 (rho -0.532, z 0.97); midcap_largecap_ratio (rho -0.449, z 0.23)
- Source: Global oil prices top $88 a barrel after Trump vows retaliation for surprise Iranian attack on U.S. troops — MarketWatch Top, 2026-07-29. https://www.marketwatch.com/story/oil-prices-rise-after-u-s-and-saudi-arabia-attack-iran-backed-militias-in-iraq-f0f409ea?mod=mw_rss_topstories
- Source: Glencore Sees $3.3 Billion Trading Profit as Iran War Rattles Oil Markets — OilPrice, 2026-07-29. https://oilprice.com/Latest-Energy-News/World-News/Glencore-Sees-33-Billion-Trading-Profit-as-Iran-War-Rattles-Oil-Markets.html
- Source: Oil prices rebound, jump 8% as Trump warns Iran after attacks on US forces; Brent nears $90 — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/oil-prices-rebound-jump-8-as-trump-warns-iran-after-attacks-on-us-forces-brent-nears-90-11785339835236.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.66] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 40025.12, z20 -3.34, zc -1.29, resid-z -1.60 [unexplained], 1d -3.79%, |z20|=3.34
- nikkei_225 [INDICES]: last 61429.44, z20 -2.79, zc -0.56, resid-z -0.53 [quiet], 1d -1.50%, |z20|=2.79
- kospi [INDICES]: last 5634.66, z20 -2.53, zc -1.12, resid-z -1.31 [quiet], 1d -6.46%, |z20|=2.53
- **Mechanism**: The recent decline in global indices, including Taiwan Weighted, Nikkei 225, and Kospi, is driven by unexplained moves with significant resid_z values, indicating that these declines are not fully priced in by factor exposures. This move is likely to propagate through the valid channels, such as the vix_equity_inverse channel, which shows a strong inverse correlation between vol spike and equity drawdown. The metal_copper_channel also provides a potential transmission mechanism, given the co-movement between global copper prices and Indian metal equities.
- **Gap**: No gap: the declines in global indices are largely unexplained, but the Indian transmission candidates have already reacted, suggesting that the event-to-price gap has been largely closed
- **India take**: The Indian instruments, such as dyn_hdbfs_bo, nifty_metal, dyn_techm_ns, and dyn_pcjeweller_ns, have already reacted to the global index moves, with most of them showing a decline in line with the global market sentiment. The Nifty is likely to open higher, but the underlying sentiment is expected to remain cautious due to geopolitical tensions in the Middle East.
- Watch next: dyn_hdbfs_bo (down) — already moved; reacted to Nikkei 225 move
- Watch next: nifty_metal (down) — already moved; reacted to Kospi move
- Watch next: dyn_techm_ns (up) — already moved; reacted to Taiwan Weighted move
- Watch next: dyn_pcjeweller_ns (down) — already moved; reacted to Taiwan Weighted move
- **India receivers**: dyn_hdbfs_bo (rho 0.468, z -2.09); nifty_metal (rho 0.437, z 1.72); dyn_techm_ns (rho -0.411, z 1.98); dyn_pcjeweller_ns (rho 0.386, z -1.38)
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html
- Source: GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. selloff, fueled by concerns over AI spending and China's technological progress. South Korea's Kospi plunged 10%, triggering two trading halts, while Japan's Nikkei fell 4%. U.S. chip stocks — DeItaone, 2026-07-28. https://t.me/walter_bloomberg/33992

### [RED 6.29] cross-asset · 2 series ↑
- dyn_jiofin_bo [EQUITIES]: last 249.60, z20 3.46, zc 2.93, resid-z 2.72 [unexplained], 1d 5.27%, |z20|=3.46
- nifty_midcap_100 [INDICES]: last 62843.70, z20 0.97, zc 0.80, resid-z -0.33 [quiet], 1d 0.68%, 1y-pct=98
- **Mechanism**: The recent surge in profits of IT companies such as Coforge and Amazon Web Services India, driven by increased demand for AI-led services and strategic acquisitions, may be propagating through the transmission_follow channel, influencing Indian equity markets. However, the metal_copper_channel and gold_silver_comove channels are currently valid, but their influence on the current event is unclear. The vix_equity_inverse channel suggests a potential inverse relationship between vol spike and equity drawdown, which may be relevant given the current RISK_OFF regime.
- **Gap**: No gap: the big raw move in dyn_jiofin_bo with small resid_z is PRICED, not an anomaly, given its high correlation with nifty_50 and other transmission candidates
- **India take**: The Indian instrument that expresses this move is nifty_50, which has not yet reacted significantly, while dyn_adanient_bo has already reacted. Other transmission candidates such as dyn_indusindbk_bo and nifty_fmcg remain quiet.
- Watch next: dyn_jiofin_bo (up) — already moved; unexplained move with high resid_z
- **India receivers**: nifty_50 (rho 0.874, z 0.77); dyn_indusindbk_bo (rho 0.654, z 0.16); nifty_fmcg (rho 0.627, z 0.81); dyn_indianb_ns (rho 0.621, z 0.12)
- Source: Amazon Web Services India net profit jumps over 10-fold to Rs 242 cr in FY26 — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/earnings/amazon-web-services-india-net-profit-jumps-over-10-fold-to-rs-242-cr-in-fy26/articleshow/132715491.cms
- Source: Coforge Q1 Results: Profit soars 63% to Rs 519 crore driven by Encora acquisition, AI-led services demand — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/earnings/coforge-q1-results-profit-soars-63-to-rs-519-crore-driven-by-encora-acquisition-ai-led-services-demand/articleshow/132688523.cms
- Historical analogues: 2025-07-15 (d=0.22), 2024-10-01 (d=0.26), 2025-05-30 (d=0.49)

### [RED 5.71] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 311.60, z20 3.71, zc 0.44, resid-z -0.35 [quiet], 1d 1.05%, |z20|=3.71
- **Mechanism**: The recent surge in dyn_eternal_ns is driven by its robust growth levers and a positive shift in its medium-term trend, as indicated by technical indicators. This move is priced, with a small resid_z of -0.35, suggesting that the factor exposures have largely explained the move. The correlated instrument nifty_midcap_100, which historically leads dyn_eternal_ns by 4 days, has not yet moved, potentially setting up a transmission follow opportunity.
- **Gap**: No gap: The recent 20% surge in dyn_eternal_ns is largely explained by its factor exposures, with a small resid_z of -0.35, indicating that the move is priced.
- **India take**: The Indian instrument dyn_jiofin_bo has already reacted, while nifty_50 and nifty_midcap_100 have not yet moved, potentially setting up a transmission follow opportunity. The move in dyn_eternal_ns may also be expressed through other Indian instruments such as dyn_havells_ns, which has already reacted.
- Watch next: nifty_midcap_100 (up) — not yet - watch; Historical lead-lag relationship with dyn_eternal_ns
- **India receivers**: nifty_midcap_100 (rho 0.58, z 0.97); dyn_jiofin_bo (rho 0.449, z 3.46); nifty_50 (rho 0.445, z 0.77); dyn_havells_ns (rho 0.422, z 2.09)
- Source: Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/eternal-shares-jump-over-20-in-one-month-will-the-stock-cross-its-october-peak-of-rs-368/articleshow/132700500.cms
- Source: Market wrap: TCS, Eternal, HUL, BEL among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-eternal-hul-bel-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132684231.cms
- Source: Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/eternal-among-4-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/132674117.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

### [RED 5.54] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 409.70, z20 -3.54, zc -0.08, resid-z -0.22 [quiet], 1d -0.11%, |z20|=3.54
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/coal-india-q1-capex-rises-16-6-yoy-to-rs-3-399-crore-in-beats-quarterly-target-11785250551117.html
- Source: Coal India shares fall 4% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Source: Coal India shares fall over 3% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

### [RED 5.5] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.98, z20 3.50, zc 0.30, resid-z -0.11 [quiet], 1d 0.77%, |z20|=3.50; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: ‘Nothing seems to shake this market.’ Why it’s time to go all-in on stocks, according to these bullish strategists. — MarketWatch Top, 2026-07-29. https://www.marketwatch.com/story/oil-is-up-40-and-tech-is-tumbling-why-its-time-to-go-all-in-on-stocks-according-to-these-bullish-strategists-41d812f7?mod=mw_rss_topstories
- Source: Adani Enterprises Q1 results: Net loss at  ₹1,160 crore after one-time hit; revenue jumps 50% YoY — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/adani-enterprises-q1-results-net-loss-of-adani-group-firm-at-rs-1-160-crore-after-one-time-hit-revenue-jumps-50-yoy-11785318914015.html
- Source: Adani Enterprises Q1 Results: Co reports loss of Rs 1,160 cr on one-time expense; revenue surges 50% YoY — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/earnings/adani-enterprises-q1-results-co-reports-loss-of-rs-1160-cr-revenue-rises-50-yoy/articleshow/132707551.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 5.29] dyn_infy ↑
- dyn_infy [EQUITIES]: last 12.51, z20 3.29, zc 0.41, resid-z 1.60 [unexplained], 1d 1.26%, |z20|=3.29
- **Mechanism**: dyn_infy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.602 via dyn_infy, leads 1d, z 2.69, reacted); dyn_techm_ns (rho 0.577 via dyn_infy, leads 1d, z 1.98, reacted); dyn_tataelxsi_ns (rho 0.384 via dyn_infy, leads 1d, z 0.79, quiet)
- Watch next: dyn_tataelxsi_ns (co-move) — not yet - watch; rho 0.384 vs dyn_infy, historically leads by 1d
- **India receivers**: nifty_it (rho 0.602, z 2.69); dyn_techm_ns (rho 0.577, z 1.98); dyn_tataelxsi_ns (rho 0.384, z 0.79)
- Source: Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-29-july-2026/article71276758.ece
- Source: Sensex today | Stock Market Live: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-29-july-2026/article71276758.ece
- Source: TCS vs Infosys vs Wipro vs HCL Tech: Which IT stock to buy after Q1 results? — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/tcs-vs-infosys-vs-wipro-vs-hcl-tech-which-it-stock-to-buy-after-q1-results-11785302857002.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

## Watchlist (below surfacing floor)
asx_200 ↑ (4.51), dyn_cupid_ns ↑ (4.45), gold_silver_ratio ↑ (4.44), dyn_ms ↓ (4.44), dyn_aapl ↑ (3.61), dyn_tech ↑ (3.61), indices · 2 series ↑ (3.48), dyn_ohi ↑ (3.23), hy_oas ↑ (3.21), dyn_301077_sz ↓ (3.12), eur_usd ↓ (3.09), dyn_bac ↑ (3.02)

## India macro
- nifty_50: 24242.0000 (1d 1.07%, z20 0.77, flag none)
- nifty_midcap_100: 62843.6992 (1d 0.68%, z20 0.97, flag amber)
- usd_inr: 95.6370 (1d -0.14%, z20 -0.61, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5923 (1d -0.39%, z20 0.23, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 77.9 — "MARKET MOVERS 🟢 UPGRADES $ASTS: Scotiabank upgraded to Sector Perform; PT raised to $50.80"
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.4 — "India bonds slip as oil prices hurt; Fed verdict in focus"
- BAC (Bank of America Corporation) score 64.1 — "MARKET MOVERS 🟢 UPGRADES $ASTS: Scotiabank upgraded to Sector Perform; PT raised to $50.80"
- HDB (HDFC Bank Limited) score 62.4 — "MARKET MOVERS 🟢 UPGRADES $ASTS: Scotiabank upgraded to Sector Perform; PT raised to $50.80"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.8 — "MARKET MOVERS 🟢 UPGRADES $ASTS: Scotiabank upgraded to Sector Perform; PT raised to $50.80"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 59.4 — "India bonds slip as oil prices hurt; Fed verdict in focus"
- IDBI.NS (IDBI BANK LIMITED) score 59.1 — "MARKET MOVERS 🟢 UPGRADES $ASTS: Scotiabank upgraded to Sector Perform; PT raised to $50.80"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.3 — "Indo-MIM IPO vs Xtranet Technologies IPO vs Lohia Corp IPO: What GMP signals about the lis"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.5 — "Indo-MIM IPO vs Xtranet Technologies IPO vs Lohia Corp IPO: What GMP signals about the lis"
- COALINDIA.NS (COAL INDIA LTD) score 53.2 — "India bonds slip as oil prices hurt; Fed verdict in focus"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 52.9 — "MARKET MOVERS 🟢 UPGRADES $ASTS: Scotiabank upgraded to Sector Perform; PT raised to $50.80"
- COIN (Coinbase Global, Inc.) score 48.7 — "Global oil prices top $88 a barrel after Trump vows retaliation for surprise Iranian attac"
- OHI (Omega Healthcare Investors, In) score 39.5 — "ECOMMERCE MOMENTUM BUILDS Bernstein raised its U.S. eCommerce forecasts after estimating Q"
- TECH (Bio-Techne Corp) score 30.9 — "Indo-MIM IPO vs Xtranet Technologies IPO vs Lohia Corp IPO: What GMP signals about the lis"
- LTH (Life Time Group Holdings, Inc.) score 27.7 — "TRUMP'S WEDNESDAY CALENDAR — JULY 29 ▶ 8:00 AM — Executive Time ▶ 10:30 AM — Greets Montan"
- CHKP (Check Point Software Technolog) score 26.3 — "These 15 midcap stocks soared up to 98% in a year; check FII and MF holdings"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.9 — "India bonds slip as oil prices hurt; Fed verdict in focus"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.7 — "Lower crude oil prices reduced U.S.-Canada energy trade value in 2025"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 22.4 — "Q1 Results Today Live: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹695 cr "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.9 — "Tata Consumer Share Price Live Updates: Tata Consumer's stock price rises amidst mixed ret"
- MS (Morgan Stanley) score 14.8 — "FED DECISION: WHAT TO WATCH The Fed is expected to keep rates at 3.5%-3.75%, but markets s"
- 301077.SZ (CHINASTARS) score 12.6 — "CHINA FOREIGN MINISTRY, ON U.S. BAN ON CHINESE ROBOTS: CHINA ALWAYS OPPOSES U.S. GENERALIS"
- INFY (Infosys Limited) score 12.6 — "Sensex today | Stock Market Highlights: Sensex rises 888 pts to close at 77,654, Nifty end"
- JIOFIN.BO (Jio Financial Services Limited) score 10.0 — "Market wrap: Jio Financial, HUL among top gainers and losers on Nifty and Sensex on Wednes"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.0 — "Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.4 — "FED IN FOCUS The Fed is widely expected to keep rates unchanged, but Chairman Kevin Warsh "
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.4 — "Q1 Results Today Live: Adani Enterprises con. loss at ₹1,462 cr, Vedanta Oil logs ₹695 cr "
- VT (Vanguard Total World Stock Ind) score 8.5 — "World Nuclear Association: $6 Trillion Needed to Hit 2050 Capacity Goals"
- META (Meta) score 7.9 — "Market Trading Guide: Lloyds Metals among 2 stock recommendations for Thursday"
- NVDA (NVIDIA Corporation) score 7.6 — "Nvidia’s $750 billion circular financing loop: How it became banker, supplier and investor"
- GS (Goldman Sachs Group, Inc. (The) score 7.2 — "L&T shares rise 4% after Q1 earnings. Why Goldman Sachs, other brokerages remain bullish?"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.9 — "Market wrap: Jio Financial, HUL among top gainers and losers on Nifty and Sensex on Wednes"
- AAPL (Apple Inc.) score 6.3 — "Apple briefly touches $5 trillion market cap, becomes the second company after Nvidia to h"
- SKHYV (SK hynix Inc. American Deposit) score 6.0 — "SK Hynix shares sent sprawling once more as earnings miss steepens decline"
- ETERNAL.NS (ETERNAL LIMITED) score 5.1 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.8 — "Vedanta Aluminium shares in a sweet spot, says ICICI Securities; initiates coverage with B"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.6 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 1.8 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- CUPID.NS (CUPID LIMITED) score 1.1 — "Cupid makes additional $5 million investment in GII Healthcare platform"
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