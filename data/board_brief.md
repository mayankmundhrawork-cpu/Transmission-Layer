# Transmission Layer — board brief · 2026-08-03 13:58Z

data as of **2026-08-03** · 98 series · 21 red / 29 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.36, 1d in regime; vol-pct 0.367, breadth-off 0.353, Markov P(high-vol) 0.07)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.44, contra nifty_50 corr20=0.21, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.32, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.24, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.29, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.00244553738718456)
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.322, β 0.05, p 0.0); driver zc -2.26 → expected -0.529%. Type hit-rate 0.822 (n=3072).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.264, β 0.0328, p 0.00023); driver zc -2.26 → expected -0.348%. Type hit-rate 0.822 (n=3072).
- Track record · residual_reversion: hit-rate **0.493** (n=1136) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=3072) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.82] cross-asset · 2 series ↑
- usd_jpy [FX]: last 156.49, z20 -6.99, zc -6.07, resid-z -5.83 [unexplained], 1d -2.30%, |z20|=6.99
- dyn_amzn [EQUITIES]: last 284.23, z20 4.07, zc 6.66, resid-z 1.43 [moved], 1d 4.66%, |z20|=4.07; 1y-pct=100
- **Mechanism**: The recent surge in the Japanese yen against the US dollar, triggered by coordinated intervention from the US and Japan, has led to a sharp decline in Japanese stocks, particularly those with high export exposure. This move has also been accompanied by a decline in oil prices, following the US President's announcement of a potential deal to end the fighting in the Middle East. The transmission of this event to Indian markets is through the correlated instruments, particularly the reacted dyn_muthootfin_ns and dyn_thangamayl_ns.
- **Gap**: No gap: the big raw move in usd_jpy has a small resid_z, indicating it is PRICED
- **India take**: The Indian instruments dyn_muthootfin_ns and dyn_thangamayl_ns have already reacted to the yen surge, while dyn_cartrade_ns is yet to react. The transmission of the event to Indian markets is through the correlated instruments, particularly those with high export exposure.
- Watch next: dyn_muthootfin_ns (down) — already moved; reacted to yen surge
- Watch next: dyn_thangamayl_ns (down) — already moved; reacted to yen surge
- Watch next: dyn_cartrade_ns (down) — not yet - watch; yet to react to yen surge
- **India receivers**: dyn_muthootfin_ns (rho -0.512, z -3.09); dyn_thangamayl_ns (rho -0.369, z -3.5); dyn_cartrade_ns (rho -0.364, z 0.13)
- Source: Asian stocks mixed as yen jumps against dollar, while oil prices fall — BusinessLine Mkts, 2026-08-03. https://www.thehindubusinessline.com/markets/asian-stocks-mixed-as-yen-jumps-against-dollar-while-oil-prices-fall/article71300032.ece
- Source: Global Market: Japan stocks slide as stronger Yen hits exporters; Nikkei drops Over 2% — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-slide-as-stronger-yen-hits-exporters-nikkei-drops-over-2/articleshow/132820004.cms
- Source: Yen Rises Amid Speculation of More Intervention After US Support — Mint Markets, 2026-08-03. https://www.livemint.com/market/yen-rises-amid-speculation-of-more-intervention-after-us-support-11785727800287.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 7.91] cross-asset · 7 series ↑
- cac_40 [INDICES]: last 8616.63, z20 3.57, zc 0.32, resid-z 0.18 [quiet], 1d 1.26%, |z20|=3.57; 1y-pct=99
- stoxx_50 [INDICES]: last 6415.14, z20 2.82, zc 0.20, resid-z -0.13 [quiet], 1d 0.90%, |z20|=2.82; 1y-pct=100
- dax [INDICES]: last 26012.56, z20 2.81, zc 0.08, resid-z -0.25 [quiet], 1d 1.50%, |z20|=2.81; 1y-pct=100
- dow_jones [INDICES]: last 53127.05, z20 2.07, zc 0.47, resid-z 0.22 [quiet], 1d 1.22%, |z20|=2.07; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.46, z20 1.56, zc -0.06, resid-z -0.83 [quiet], 1d 0.40%, |z20|=1.56; 1y-pct=95; co-occur[metal_copper] same-direction (channel VALID)
- ftse_100 [INDICES]: last 10847.97, z20 1.36, zc -0.46, resid-z -0.48 [quiet], 1d -0.19%, 1y-pct=98
- sp500 [INDICES]: last 7556.09, z20 1.17, zc 0.67, resid-z 0.56 [quiet], 1d 0.89%, 1y-pct=97
- **Mechanism**: The recent de-escalation of tensions in the Middle East has led to a sharp decline in crude oil prices, resulting in improved investor risk appetite and a subsequent rise in US stock futures. This move is largely priced, with most indices showing small resid_z values, indicating that the market has already accounted for the change in sentiment. The metal_copper_channel, which is VALID, also suggests that the global copper price move may lead to a reaction in Indian metal equities.
- **Gap**: No gap: the market has already priced in the change in sentiment following the de-escalation of tensions in the Middle East, with most indices showing small resid_z values.
- **India take**: Indian instruments such as Nifty 50, Nifty Midcap 100, and Nifty IT have already reacted to the global equity move, with their z20 values indicating a similar level of enthusiasm. The metal_copper_channel may lead to further reactions in Indian metal equities.
- Watch next: nifty_50 (up) — already moved; reacted to global equity move
- Watch next: nifty_midcap_100 (up) — already moved; reacted to global equity move
- Watch next: nifty_it (up) — already moved; reacted to global equity move
- **India receivers**: nifty_50 (rho 0.545, z 3.43); nifty_midcap_100 (rho 0.51, z 2.51); nifty_it (rho 0.366, z 2.46)
- Source: US stock market today: Wall Street futures gain as easing Iran tensions trigger sharp fall in oil prices — Mint Markets, 2026-08-03. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-gain-as-easing-iran-tensions-trigger-sharp-fall-in-oil-prices-11785756062931.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US futures rise on Mideast deal hopes; healthcare in focus — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-trump-us-iran-attacks-hormuz-crude-oil-fed-warsh-spacex-micron-amazon-amd-chip-stock-price-news-3rd-august-2026/liveblog/132831640.cms
- Source: SpaceX's first results put Elon Musk's AI spending under Wall Street's microscope — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/spacexs-first-results-put-elon-musks-ai-spending-under-wall-streets-microscope/articleshow/132828359.cms
- Historical analogues: 2024-10-10 (d=0.93), 2024-11-07 (d=1.0), 2024-10-03 (d=1.01)

### [RED 7.03] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 262.00, z20 3.71, zc 1.84, resid-z 2.39 [unexplained], 1d 2.16%, |z20|=3.71
- nifty_50 [INDICES]: last 24774.30, z20 3.43, zc 0.36, resid-z 0.42 [quiet], 1d 1.60%, |z20|=3.43
- nifty_midcap_100 [INDICES]: last 63668.10, z20 2.51, zc 0.40, resid-z -0.10 [quiet], 1d 1.26%, |z20|=2.51; 1y-pct=100
- **Mechanism**: The move in dyn_jiofin_bo is unexplained by factor exposures, with a high resid_z of 2.39, suggesting a potential anomaly. However, the move is accompanied by a high z20 level of 3.71, indicating a big raw move that is likely priced. The Nifty 50 and Nifty Midcap 100 indices have also moved, but their resid_z values are relatively low, indicating that their moves are largely explained by factor exposures.
- **Gap**: No gap: the move in dyn_jiofin_bo is largely priced, with a high z20 level and a relatively low resid_z value compared to its z20 level
- **India take**: The Indian instrument dyn_muthootfin_ns has reacted, with a rho of 0.692 with nifty_midcap_100, while dyn_indianb_ns and dyn_indusindbk_bo remain quiet. The Nifty Metal index has also reacted, with a rho of 0.599 with nifty_midcap_100.
- Watch next: dyn_jiofin_bo (up) — already moved; high resid_z and z20 levels
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -3.09); dyn_bharatcoal_ns (rho 0.633, z -1.52); dyn_indianb_ns (rho 0.622, z 0.79); dyn_indusindbk_bo (rho 0.614, z 0.04)
- Source: Nifty surges past key resistance in CAS debut; crude slump, Iran talks lift sentiment — BusinessLine Mkts, 2026-08-03. https://www.thehindubusinessline.com/markets/nifty-surges-past-key-resistance-in-cas-debut-crude-slump-iran-talks-lift-sentiment/article71301185.ece
- Source: Market wrap: TCS, IndiGo, Sun Pharma among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-indigo-sun-pharma-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132831712.cms
- Source: 200 point-jump in 2 minutes: Why Nifty made a surprising surge before closing bell — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/stocks/news/200-point-jump-in-2-minutes-why-nifty-made-a-surprising-surge-near-the-closing-bell/articleshow/132829268.cms
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 6.34] dyn_msft ↑
- dyn_msft [EQUITIES]: last 489.11, z20 4.34, zc 0.72, resid-z 6.76 [unexplained], 1d 5.25%, |z20|=4.34
- **Mechanism**: The recent surge in Microsoft's stock price, driven by its AI-fuelled rally and strong earnings, has created a ripple effect in the market. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, while the VALID metal_copper_channel indicates that global copper leads Indian metal equities. However, the INVERTED safe_haven_gold channel and WEAK inr_oil_channel may limit the transmission of this move to Indian markets.
- **Gap**: No gap: the big raw move in dyn_msft has a small resid_z, indicating that it is PRICED and not an anomaly
- **India take**: The Indian instrument dyn_thangamayl_ns has already reacted to the move in dyn_msft, with a negative correlation. However, the metal_copper_channel may still transmit the move to Indian metal equities.
- Watch next: dyn_thangamayl_ns (down) — already moved; reacted to dyn_msft move
- **India receivers**: dyn_thangamayl_ns (rho -0.383, z -3.5)
- Source: Microsoft's AI-Fuelled Rally: 5 reasons Wall Street is bullish again — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/microsofts-ai-fuelled-rally-5-reasons-wall-street-is-bullish-again/articleshow/132822805.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [RED 6.23] fx · 3 series ↓
- eur_usd [FX]: last 1.15, z20 2.92, zc 1.31, resid-z 1.62 [unexplained], 1d 0.02%, |z20|=2.92
- usd_mxn [FX]: last 17.29, z20 -2.55, zc -1.30, resid-z -1.35 [quiet], 1d -0.29%, |z20|=2.55
- usd_brl [FX]: last 5.07, z20 -1.56, zc -1.29, resid-z -1.37 [quiet], 1d -0.20%, |z20|=1.56
- **Mechanism**: fx · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.52 via usd_mxn, z -3.09, reacted)
- Watch next: gbp_usd (co-move) — not yet - watch; rho 0.848 vs eur_usd, historically leads by 4d
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.718 vs eur_usd, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho -0.52, z -3.09)
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-05 (d=0.14), 2025-04-01 (d=0.29)

### [AMBER 6.23] commodities · 2 series ↓
- brent [COMMODITIES]: last 82.81, z20 -0.40, zc 0.28, resid-z 0.70 [quiet], 1d -8.11%, 1-session move -8.11% ≥ 1.5%
- wti [COMMODITIES]: last 78.59, z20 -0.27, zc 0.36, resid-z 0.65 [quiet], 1d -7.18%, 1-session move -7.18% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.498 via wti, z 2.51, reacted); midcap_largecap_ratio (rho -0.415 via wti, z -1.14, reacted); dyn_hdbfs_bo (rho -0.381 via brent, z -1.26, reacted)
- **India receivers**: nifty_midcap_100 (rho -0.498, z 2.51); midcap_largecap_ratio (rho -0.415, z -1.14); dyn_hdbfs_bo (rho -0.381, z -1.26)
- Source: Indian Oil Subsidiary CPCL Plans 280,000 Bpd Manali Refinery — OilPrice, 2026-08-03. https://oilprice.com/Latest-Energy-News/World-News/Indian-Oil-Subsidiary-CPCL-Plans-280000-Bpd-Manali-Refinery.html
- Source: Global oil prices fall below $83 a barrel to hover at 3-week low after Trump calls off planned attack and says Iran talks to resume Monday — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/oil-prices-fall-to-three-week-low-after-trump-calls-off-planned-attack-631a8683?mod=mw_rss_topstories
- Source: Nifty surges past key resistance in CAS debut; crude slump, Iran talks lift sentiment — BusinessLine Mkts, 2026-08-03. https://www.thehindubusinessline.com/markets/nifty-surges-past-key-resistance-in-cas-debut-crude-slump-iran-talks-lift-sentiment/article71301185.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 6.07] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 90.28, z20 -2.14, zc -1.14, resid-z 0.13 [quiet], 1d -0.24%, |z20|=2.14; 1y-pct=0
- ust_30y [RATES]: last 5.21, z20 2.08, zc 0.29, resid-z 1.09 [quiet], 1d 0.19%, |z20|=2.08; 1y-pct=100
- ust_10y [RATES]: last 4.68, z20 1.39, zc 0.22, resid-z 1.94 [unexplained], 1d 0.21%, 1y-pct=99
- tips_10y_real [RATES]: last 2.41, z20 1.11, zc 0.00, resid-z 1.88 [unexplained], 1d 0.00%, 1y-pct=98
- ust_2y [RATES]: last 4.23, z20 0.15, zc 0.18, resid-z 2.50 [unexplained], 1d 0.24%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.634 vs dyn_bond, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.527 vs dyn_bond, historically leads by 3d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.518 vs tips_10y_real, historically leads by 4d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.551 vs dyn_bond
- Watch next: brent (inverse) — not yet - watch; rho -0.514 vs dyn_bond
- Source: US 10-year yield falls from 18-month high on Iran peace talk hopes — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/bonds/us-10-year-yield-falls-from-18-month-high-on-iran-peace-talk-hopes/articleshow/132831577.cms
- Source: Warsh tightened more by pausing than by lifting rates, this bond-market veteran argues. Here’s the math. — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/warsh-tightened-more-by-pausing-than-by-lifting-rates-this-bond-market-veteran-argues-heres-the-math-31cb15a1?mod=mw_rss_topstories
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.71] dxy ↓
- dxy [FX]: last 99.76, z20 -2.71, zc -0.56, resid-z -2.49 [unexplained], 1d -0.04%, 20d range extreme; |z20|=2.71
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.539 vs dxy, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
dyn_thangamayl_ns ↓ (5.5), dyn_muthootfin_ns ↓ (5.09), gold_silver_ratio ↑ (4.81), dyn_coin ↓ (4.59), dyn_chkp ↓ (4.26), dyn_lth ↑ (4.02), dyn_tech ↑ (3.46), nifty_metal ↑ (3.27), dyn_atherenerg_ns ↑ (3.07), usd_cny ↓ (2.89), dyn_havells_ns ↑ (2.88), ust_2s10s ↑ (2.6)

## India macro
- nifty_50: 24774.3008 (1d 1.60%, z20 3.43, flag red)
- nifty_midcap_100: 63668.1016 (1d 1.26%, z20 2.51, flag red)
- usd_inr: 95.3270 (1d -0.37%, z20 -1.43, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5699 (1d -0.33%, z20 -1.14, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI MPC decision T-4d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.7 — "India's coal dispatch surges 17.3% in July as production growth stands at 7.5%"
- COALINDIA.NS (COAL INDIA LTD) score 62.4 — "India's coal dispatch surges 17.3% in July as production growth stands at 7.5%"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 61.1 — "India's coal dispatch surges 17.3% in July as production growth stands at 7.5%"
- INDIANB.NS (INDIAN BANK) score 51.7 — "Index derivatives turnover falls as RBI tightens bank funding to prop traders"
- COIN (Coinbase Global, Inc.) score 45.7 — "Market outlook: RBI policy, Q1 earnings and global cues to steer markets this week"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.4 — "Stocks to watch, Aug 3: Tata Motors Passenger vehicles, TMCV, Maruti Suzuki, Mahindra & Ma"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.3 — "Technocraft Ventures IPO: Price band set at  ₹200-212 per share; check key dates, issue de"
- BAC (Bank of America Corporation) score 35.8 — "Index derivatives turnover falls as RBI tightens bank funding to prop traders"
- OHI (Omega Healthcare Investors, In) score 35.1 — "Why are global investors buying up South Korean stocks?"
- HDB (HDFC Bank Limited) score 34.6 — "Index derivatives turnover falls as RBI tightens bank funding to prop traders"
- IDBI.NS (IDBI BANK LIMITED) score 33.6 — "Index derivatives turnover falls as RBI tightens bank funding to prop traders"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 33.6 — "Index derivatives turnover falls as RBI tightens bank funding to prop traders"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.0 — "Index derivatives turnover falls as RBI tightens bank funding to prop traders"
- TECH (Bio-Techne Corp) score 28.7 — "Technocraft Ventures IPO: Price band set at  ₹200-212 per share; check key dates, issue de"
- CHKP (Check Point Software Technolog) score 27.2 — "Crude Check: Direction unclear"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.4 — "IRAN'S TASNIM, QUOTING SENIOR SECURITY OFFICIAL: IRAN'S RESPONSE PLAN INCLUDES CRITICAL IN"
- LTH (Life Time Group Holdings, Inc.) score 24.1 — "MV Electrosystems IPO Day 3 LIVE: GMP signals 28% listing gain, issue subscribed near 200 "
- BOND (PIMCO Active Bond Exchange-Tra) score 24.0 — "Oil, dollar inflows blunt impact on Indian bonds from index inclusion snub"
- 301077.SZ (CHINASTARS) score 14.8 — "China Doubles Down on Clean Energy Even as Coal Keeps Growing"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.9 — "Stocks to watch, Aug 3: Tata Motors Passenger vehicles, TMCV, Maruti Suzuki, Mahindra & Ma"
- MS (Morgan Stanley) score 10.7 — "Urban Company shares jump 13% despite Q1 loss, Morgan Stanley upgrades to overweight"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.3 — "Adani Total Gas raises CNG prices by ₹4 per kg amid rising LNG costs"
- AAPL (Apple Inc.) score 9.1 — "Apple suffers worst rout since 2025 on disappointing outlook"
- JIOFIN.BO (Jio Financial Services Limited) score 9.1 — "Sensex, Nifty gap up on Iran diplomacy, crude slide; financials lead, pharma drags"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.5 — "India's coal dispatch surges 17.3% in July as production growth stands at 7.5%"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.0 — "Sensex, Nifty gap up on Iran diplomacy, crude slide; financials lead, pharma drags"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.6 — "India approves just 1 Chinese FDI proposal worth ₹1 cr, 13 Hong Kong proposals worth ₹610."
- MSFT (Microsoft Corporation) score 6.8 — "Microsoft's AI-Fuelled Rally: 5 reasons Wall Street is bullish again"
- AMZN (Amazon.com, Inc.) score 6.7 — "Amazon soars as cloud revenue surge allays fears over ballooning AI bets"
- VT (Vanguard Total World Stock Ind) score 6.3 — "Healthcare stock Park Medi World inches close to record high after the Q1 results 2026"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.8 — "Thangamayil Jewellery shares crash 32% in a week. What should investors do?"
- GS (Goldman Sachs Group, Inc. (The) score 5.2 — "TRADERS BRACE FOR S&P 500 VOLATILITY Investors are increasing hedges against broader S&P 5"
- META (Meta) score 5.1 — "Global Market: China's factory activity contracts unexpectedly in July; metal, commodity s"
- INFY (Infosys Limited) score 5.0 — "Kospi’s mammoth 17% surge spells caution for Indian IT stocks. Why TCS, Infosys, others ar"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.8 — "Nifty Q1 earnings grow 11% to beat estimate, says Motilal Oswal; picks Bharti Airtel, SBI,"
- NVDA (NVIDIA Corporation) score 4.0 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.0 — "Muthoot Finance shares crash 10% after Q1 results. What Motilal, other brokerages said"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.2 — "Thangamayil Jewellery shares crash 32% in a week. What should investors do?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.1 — "LT Foods shares jump 4% on strong Q1 results; stock outperforms market"
- CUPID.NS (CUPID LIMITED) score 0.7 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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