# Transmission Layer — board brief · 2026-07-29 11:52Z

data as of **2026-07-29** · 98 series · 12 red / 36 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.483, 4d in regime; vol-pct 0.633, breadth-off 0.333, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.44, contra nifty_50 corr20=0.3, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.28, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.01, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.06, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.52, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_infy → dyn_techm_ns: leads 1d (ccf 0.279, β 0.2375, p 0.0); driver zc 1.93 → expected 1.319%. Type hit-rate 0.817 (n=3240).
- Track record · residual_reversion: hit-rate **0.492** (n=1136) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3240) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.87] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.60, z20 4.87, zc 1.97, resid-z -0.11 [moved], 1d 4.20%, |z20|=4.87; 1y-pct=100
- **Mechanism**: The recent surge in dyn_lth is driven by a significant increase in revenue, which may not be fully priced in by the market. However, the resid_z of -0.11 suggests that the move is largely explained by factor exposures, indicating that the market has already accounted for the news. The valid metal_copper_channel may also play a role in transmitting global copper price movements to Indian metal equities.
- **Gap**: No gap: the market has already priced in the revenue increase and the resid_z is relatively low
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which may react negatively due to the potential risk-off sentiment. However, the reaction has not occurred yet.
- Watch next: nifty_50 (down) — not yet - watch; potential risk-off sentiment
- Source: ‘Nothing seems to shake this market.’ Why it’s time to go all-in on stocks, according to these bullish strategists. — MarketWatch Top, 2026-07-29. https://www.marketwatch.com/story/oil-is-up-40-and-tech-is-tumbling-why-its-time-to-go-all-in-on-stocks-according-to-these-bullish-strategists-41d812f7?mod=mw_rss_topstories
- Source: Adani Enterprises Q1 results: Net loss at  ₹1,160 crore after one-time hit; revenue jumps 50% YoY — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/adani-enterprises-q1-results-net-loss-of-adani-group-firm-at-rs-1-160-crore-after-one-time-hit-revenue-jumps-50-yoy-11785318914015.html
- Source: Adani Enterprises Q1 Results: Co reports loss of Rs 1,160 cr on one-time expense; revenue surges 50% YoY — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/earnings/adani-enterprises-q1-results-co-reports-loss-of-rs-1160-cr-revenue-rises-50-yoy/articleshow/132707551.cms
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
- **India receivers**: dyn_hdbfs_bo (rho 0.468, z -2.09); nifty_metal (rho 0.438, z 1.72); dyn_techm_ns (rho -0.411, z 1.98); dyn_pcjeweller_ns (rho 0.386, z -1.38)
- Source: Global Market: Japan's Nikkei swings between gains and losses as AI stock selloff persists — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-swings-between-gains-and-losses-as-ai-stock-selloff-persists/articleshow/132702082.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you should know before the Indian stock market opens on Wednesday — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-markets-equity-heatmap-you-should-know-before-indian-stock-market-opens-on-wednesday-11785292239206.html
- Source: GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. selloff, fueled by concerns over AI spending and China's technological progress. South Korea's Kospi plunged 10%, triggering two trading halts, while Japan's Nikkei fell 4%. U.S. chip stocks — DeItaone, 2026-07-28. https://t.me/walter_bloomberg/33992

### [AMBER 6.51] commodities · 2 series ↑
- wti [COMMODITIES]: last 82.80, z20 0.67, zc 1.35, resid-z -1.06 [quiet], 1d 4.47%, 1-session move +4.47% ≥ 1.5%
- brent [COMMODITIES]: last 88.11, z20 0.58, zc 1.22, resid-z -1.33 [quiet], 1d 4.78%, 1-session move +4.78% ≥ 1.5%
- **Mechanism**: The recent surge in commodities, specifically WTI and Brent, with a 1-session move of +4.47% and +4.78% respectively, may propagate through the metal_copper_channel, given its valid status and positive correlation. However, the inr_oil_channel, which typically transmits oil price movements to the INR, is currently weak, potentially limiting the transmission to Indian markets.
- **Gap**: No gap: The recent move in WTI and Brent is largely priced, with resid_z values of -1.06 and -1.33, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that may express this move is the nifty_midcap_100, which has a negative correlation with WTI and has not yet reacted. Additionally, the midcap_largecap_ratio may also be affected, given its negative correlation with WTI.
- Watch next: nifty_midcap_100 (down) — not yet - watch; Historical lead of 1d and negative correlation with WTI
- **India receivers**: nifty_midcap_100 (rho -0.556, z 0.97); midcap_largecap_ratio (rho -0.45, z 0.23)
- Source: Oil prices rise after U.S. and Saudi Arabia attack Iran-backed militias in Iraq — MarketWatch Top, 2026-07-29. https://www.marketwatch.com/story/oil-prices-rise-after-u-s-and-saudi-arabia-attack-iran-backed-militias-in-iraq-f0f409ea?mod=mw_rss_topstories
- Source: Q1 Results Today Live: Adani Enterprises con. loss at ₹1462 cr, Vedanta Oil logs ₹695 cr profit, Asian Paints, Adani Ports, Colgate, V-Guard Q1 profit rise, Thangamayil Jewellery shares tank 10% after results; Eicher Motors, Waaree Energies, Prestige Estates, Dabur, ACME Solar to announce Q1 results — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-adani-enterprises-adani-ports-asian-paints-eicher-motors-waaree-energies-colgate-prestige-estates-syrma-sgs-tech-dabur-hexaware-tech-vedanta-oil-acme-results-29-july-2026/article71276282.ece
- Source: Vedanta Oil & Gas Q1 Results: Co swings to black with Rs 945 crore profit, revenue up 9% YoY — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/earnings/vedanta-oil-gas-q1-results-co-swings-to-black-with-rs-945-crore-profit-revenue-up-9-yoy/articleshow/132709673.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.29] cross-asset · 2 series ↑
- dyn_jiofin_bo [EQUITIES]: last 249.60, z20 3.46, zc 2.93, resid-z 2.67 [unexplained], 1d 5.27%, |z20|=3.46
- nifty_midcap_100 [INDICES]: last 62843.70, z20 0.97, zc 0.80, resid-z -0.61 [quiet], 1d 0.68%, 1y-pct=98
- **Mechanism**: The recent surge in Coforge's profits, driven by the Encora acquisition and AI-led services demand, has led to a significant increase in the stock's price, with dyn_jiofin_bo showing an unexplained move. This move is likely to propagate through the correlated instruments, particularly nifty_50, given their high correlation coefficient of 0.874.
- **Gap**: No gap: The big raw move in dyn_jiofin_bo with a small resid_z indicates that the move is largely priced in, leaving little room for a significant event-to-price gap.
- **India take**: The Indian instrument that expresses this move is nifty_50, which has not yet reacted. Another potential responder is dyn_indusindbk_bo, which is correlated with nifty_midcap_100.
- Watch next: nifty_50 (up) — not yet - watch; High correlation with dyn_jiofin_bo
- Watch next: dyn_indusindbk_bo (up) — not yet - watch; Correlated with nifty_midcap_100
- **India receivers**: nifty_50 (rho 0.874, z 0.77); dyn_indusindbk_bo (rho 0.654, z 0.16); nifty_fmcg (rho 0.627, z 0.81); dyn_indianb_ns (rho 0.621, z 0.12)
- Source: Coforge Q1 Results: Profit soars 63% to Rs 519 crore driven by Encora acquisition, AI-led services demand — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/earnings/coforge-q1-results-profit-soars-63-to-rs-519-crore-driven-by-encora-acquisition-ai-led-services-demand/articleshow/132688523.cms
- Source: AMZN - AMAZON: LEO WILL PARTNER WITH MOBILE NETWORK OPERATORS TO EXTEND MOBILE CONNECTIVITY SERVICES GLOBALLY, WITH SATELLITE DEPLOYMENT BEGINNING IN 2028 — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33925
- Historical analogues: 2025-07-15 (d=0.22), 2024-10-01 (d=0.26), 2025-05-30 (d=0.49)

### [RED 6.02] dyn_infy ↑
- dyn_infy [EQUITIES]: last 12.35, z20 4.02, zc 1.93, resid-z 1.60 [unexplained], 1d 5.56%, |z20|=4.02
- **Mechanism**: The surge in Indian IT stocks, led by Infosys and TCS, is driving the move in dyn_infy, which has a high correlation with these stocks. The verified transmission setup between dyn_infy and dyn_techm_ns, with a lead-lag of 1 day, suggests that the move in dyn_infy will be followed by a move in dyn_techm_ns. The channel status shows that the vix_equity_inverse channel is valid, indicating a potential inverse relationship between vol spike and equity drawdown.
- **Gap**: No gap: the move in dyn_infy is largely priced, with a resid_z of 1.6, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instruments nifty_it and dyn_techm_ns have reacted to the move in dyn_infy, with nifty_it already having reacted and dyn_techm_ns expected to follow. The move in Indian IT stocks is expected to continue, driven by strong Q1 earnings and optimism around AI-driven demand.
- Watch next: dyn_techm_ns (up) — not yet - watch; verified transmission setup with dyn_infy
- **India receivers**: nifty_it (rho 0.601, z 2.69); dyn_techm_ns (rho 0.583, z 1.98); dyn_tataelxsi_ns (rho 0.376, z 0.79)
- Source: Sensex today | Stock Market Live: Sensex rises 888 pts to close at 77,654, Nifty ends at 24,250; Hindustan Unilever, Infosys top gainers — BusinessLine Mkts, 2026-07-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-29-july-2026/article71276758.ece
- Source: TCS vs Infosys vs Wipro vs HCL Tech: Which IT stock to buy after Q1 results? — Mint Markets, 2026-07-29. https://www.livemint.com/market/stock-market-news/tcs-vs-infosys-vs-wipro-vs-hcl-tech-which-it-stock-to-buy-after-q1-results-11785302857002.html
- Source: IT stocks on a roll: TCS, Infosys, Coforge and others rally up to 5% for second straight day. What's driving this surge? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/it-stocks-on-a-roll-tcs-infosys-coforge-and-others-rally-up-to-5-for-second-straight-day-whats-driving-this-surge/articleshow/132701697.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

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
- Watch next: wti (co-move) — not yet - watch; rho 0.504 vs ust_10y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.653 vs tips_10y_real
- Watch next: brent (inverse) — not yet - watch; rho -0.514 vs dyn_bond
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.506 vs dyn_bond
- Source: Euro zone bond rally ends as oil surge, Fed decision weigh on investors — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-rally-ends-as-oil-surge-fed-decision-weigh-on-investors/articleshow/132706628.cms
- Source: US Stock Market: Bond investors turn cautious ahead of Fed meeting as inflation risks cloud rate outlook — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-bond-investors-turn-cautious-ahead-of-fed-meeting-as-inflation-risks-cloud-rate-outlook/articleshow/132699838.cms
- Source: Investors are piling into bond funds at a rapid rate. That’s a problem — but not for stocks. — MarketWatch Top, 2026-07-28. https://www.marketwatch.com/story/investors-are-piling-into-bond-funds-at-a-rapid-rate-thats-a-problem-09aaa039?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.71] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 311.60, z20 3.71, zc 0.44, resid-z -0.36 [quiet], 1d 1.05%, |z20|=3.71
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.58 via dyn_eternal_ns, z 0.97, quiet); dyn_jiofin_bo (rho 0.449 via dyn_eternal_ns, z 3.46, reacted); nifty_50 (rho 0.445 via dyn_eternal_ns, z 0.77, quiet); dyn_havells_ns (rho 0.422 via dyn_eternal_ns, z 2.09, reacted); dyn_indusindbk_bo (rho 0.395 via dyn_eternal_ns, z 0.16, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.58 vs dyn_eternal_ns, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.58, z 0.97); dyn_jiofin_bo (rho 0.449, z 3.46); nifty_50 (rho 0.445, z 0.77); dyn_havells_ns (rho 0.422, z 2.09)
- Source: Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368? — ET Markets, 2026-07-29. https://economictimes.indiatimes.com/markets/stocks/news/eternal-shares-jump-over-20-in-one-month-will-the-stock-cross-its-october-peak-of-rs-368/articleshow/132700500.cms
- Source: Market wrap: TCS, Eternal, HUL, BEL among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-eternal-hul-bel-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132684231.cms
- Source: Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/eternal-among-4-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/132674117.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

### [RED 5.54] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 409.70, z20 -3.54, zc -0.08, resid-z -0.15 [quiet], 1d -0.11%, |z20|=3.54
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/coal-india-q1-capex-rises-16-6-yoy-to-rs-3-399-crore-in-beats-quarterly-target-11785250551117.html
- Source: Coal India shares fall 4% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Source: Coal India shares fall over 3% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

## Watchlist (below surfacing floor)
asx_200 ↑ (4.51), nasdaq_100 ↓ (4.47), gold_silver_ratio ↑ (4.02), dyn_ohi ↑ (3.89), dyn_tech ↑ (3.86), natgas ↓ (3.76), dyn_bac ↑ (3.71), dyn_aapl ↑ (3.58), indices · 2 series ↑ (3.49), dyn_hdb ↓ (3.29), dyn_301077_sz ↓ (3.12), eur_usd ↓ (3.09)

## India macro
- nifty_50: 24242.0000 (1d 1.07%, z20 0.77, flag none)
- nifty_midcap_100: 62843.6992 (1d 0.68%, z20 0.97, flag amber)
- usd_inr: 95.6475 (1d -0.13%, z20 -0.59, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5923 (1d -0.39%, z20 0.23, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 75.5 — "Sensex jumps 900 points, Nifty 50 ends at 24,250; investors earn  ₹4 lakh crore. Banking, "
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.6 — "VBL shares bounce back after mixed earnings, but can India volume growth hold up?"
- BAC (Bank of America Corporation) score 61.0 — "Sensex jumps 900 points, Nifty 50 ends at 24,250; investors earn  ₹4 lakh crore. Banking, "
- HDB (HDFC Bank Limited) score 60.3 — "Sensex jumps 900 points, Nifty 50 ends at 24,250; investors earn  ₹4 lakh crore. Banking, "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 59.2 — "VBL shares bounce back after mixed earnings, but can India volume growth hold up?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.6 — "Sensex jumps 900 points, Nifty 50 ends at 24,250; investors earn  ₹4 lakh crore. Banking, "
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.0 — "KPIT Tech Q1 Results: Shares rally 10% even as net profit drops 32% YoY to Rs 117 crore. H"
- IDBI.NS (IDBI BANK LIMITED) score 56.8 — "Sensex jumps 900 points, Nifty 50 ends at 24,250; investors earn  ₹4 lakh crore. Banking, "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 56.2 — "KPIT Tech Q1 Results: Shares rally 10% even as net profit drops 32% YoY to Rs 117 crore. H"
- COALINDIA.NS (COAL INDIA LTD) score 52.7 — "VBL shares bounce back after mixed earnings, but can India volume growth hold up?"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 50.3 — "Sensex jumps 900 points, Nifty 50 ends at 24,250; investors earn  ₹4 lakh crore. Banking, "
- COIN (Coinbase Global, Inc.) score 50.1 — "Global Earnings | Nomura's first-quarter profit jumps 39%, boosted by markets"
- OHI (Omega Healthcare Investors, In) score 39.4 — "Global Market: European shares gain as miners, energy stocks lead; investors track Middle "
- TECH (Bio-Techne Corp) score 31.4 — "KPIT Tech Q1 Results: Shares rally 10% even as net profit drops 32% YoY to Rs 117 crore. H"
- CHKP (Check Point Software Technolog) score 27.6 — "These 15 midcap stocks soared up to 98% in a year; check FII and MF holdings"
- LTH (Life Time Group Holdings, Inc.) score 26.9 — "US Fed meeting outcome today: Here's date, time, expectations, where to watch Kevin Warsh'"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.1 — "Euro zone bond rally ends as oil surge, Fed decision weigh on investors"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.9 — "Global Market: European shares gain as miners, energy stocks lead; investors track Middle "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 22.5 — "Adani Ports Q1 results: Profit climbs 9% YoY to  ₹3,620 crore, revenue jumps 19%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.7 — "Tata Consumer Share Price Live Updates: Tata Consumer's stock price rises amidst mixed ret"
- 301077.SZ (CHINASTARS) score 13.2 — "CHINA FOREIGN MINISTRY, ON U.S. BAN ON CHINESE ROBOTS: CHINA ALWAYS OPPOSES U.S. GENERALIS"
- INFY (Infosys Limited) score 12.1 — "Sensex today | Stock Market Live: Sensex rises 888 pts to close at 77,654, Nifty ends at 2"
- MS (Morgan Stanley) score 11.4 — "HUL shares rebound 2% after Q1 results. Here's what Morgan Stanley, Motilal Oswal and othe"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.5 — "Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.9 — "FED IN FOCUS The Fed is widely expected to keep rates unchanged, but Chairman Kevin Warsh "
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.8 — "Multibagger Thangamayil Jewellery share price hits 10% lower circuit despite strong Q1 res"
- JIOFIN.BO (Jio Financial Services Limited) score 8.4 — "TSX hits record high, led by tech and financial shares"
- VT (Vanguard Total World Stock Ind) score 7.9 — "The World’s Largest Sand Battery Is Now Online"
- GS (Goldman Sachs Group, Inc. (The) score 7.5 — "L&T shares rise 4% after Q1 earnings. Why Goldman Sachs, other brokerages remain bullish?"
- META (Meta) score 7.2 — "META - *META, BLACKROCK TO DEVELOP DATA CENTER CAMPUS IN EL PASO, TEXAS"
- NVDA (NVIDIA Corporation) score 7.0 — "Apple briefly touches $5 trillion market cap, becomes the second company after Nvidia to h"
- AAPL (Apple Inc.) score 6.6 — "Apple briefly touches $5 trillion market cap, becomes the second company after Nvidia to h"
- SKHYV (SK hynix Inc. American Deposit) score 6.3 — "SK Hynix shares sent sprawling once more as earnings miss steepens decline"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.2 — "TSX hits record high, led by tech and financial shares"
- ETERNAL.NS (ETERNAL LIMITED) score 5.3 — "Eternal shares jump over 20% in one month. Will the stock cross its October peak of Rs 368"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.0 — "Vedanta Aluminium shares in a sweet spot, says ICICI Securities; initiates coverage with B"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.8 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 1.9 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.3 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
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