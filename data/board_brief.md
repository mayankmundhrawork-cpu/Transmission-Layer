# Transmission Layer — board brief · 2026-08-13 19:18Z

data as of **2026-08-13** · 98 series · 9 red / 38 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.223, 2d in regime; vol-pct 0.27, breadth-off 0.176, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.85, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.32, corr60 0.36, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.07, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.8, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.23, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.04, corr60 0.17, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2503) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.03] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4412.40, z20 2.03, zc 0.05, resid-z 0.33 [quiet], 1d 0.08%, |z20|=2.03; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3056.17, z20 1.94, zc 0.29, resid-z -0.59 [quiet], 1d 0.35%, |z20|=1.94; 1y-pct=100
- dyn_vt [EQUITIES]: last 162.43, z20 1.84, zc 0.67, resid-z 0.98 [quiet], 1d 0.55%, 1y-pct=100
- dyn_nvda [EQUITIES]: last 225.63, z20 1.81, zc 0.27, resid-z 0.48 [quiet], 1d 0.69%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30119.62, z20 1.80, zc 0.94, resid-z 0.63 [quiet], 1d 1.27%, |z20|=1.80; 1y-pct=96
- sp500 [INDICES]: last 7801.53, z20 1.71, zc 0.85, resid-z -1.19 [quiet], 1d 0.68%, |z20|=1.71; 1y-pct=100
- comex_silver [COMMODITIES]: last 64.71, z20 1.70, zc -0.52, resid-z -0.69 [quiet], 1d -1.30%, |z20|=1.70; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6544.01, z20 1.48, zc 0.20, resid-z -0.68 [quiet], 1d 0.15%, 1y-pct=99
- dax [INDICES]: last 26290.12, z20 1.21, zc -0.21, resid-z -0.65 [quiet], 1d -0.16%, 1y-pct=98
- dow_jones [INDICES]: last 53806.89, z20 1.06, zc 0.09, resid-z -1.35 [quiet], 1d 0.07%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.19, z20 -0.95, zc n/a, resid-z n/a [quiet], 1d 1.39%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8649.46, z20 0.91, zc -0.40, resid-z -0.97 [quiet], 1d -0.29%, 1y-pct=97
- comex_copper [COMMODITIES]: last 6.59, z20 0.90, zc -0.06, resid-z -0.70 [quiet], 1d -0.13%, 1y-pct=96
- **Mechanism**: The recent move in gold prices, driven by US inflation data, has triggered a co-movement in other monetary metals such as silver, with the gold-silver ratio indicating an extreme low. This has led to a quiet move in various indices, including the Russell 2000 and Nasdaq 100, as well as equities like dyn_vt and dyn_nvda. The VALID gold_silver_comove channel suggests that the move in gold and silver is likely to continue, with potential implications for Indian metal equities.
- **Gap**: No gap: the big raw move in gold has a small resid_z of 0.33, indicating that the move is largely priced in.
- **India take**: The move in gold and silver prices may have implications for Indian metal equities, such as those in the Nifty Metal index, which has a rho of 0.523 with comex_silver. The Nifty Metal index has not yet reacted to the move in gold and silver prices.
- Watch next: nifty_metal (up) — not yet - watch; rho=0.523 via comex_silver
- **India receivers**: nifty_metal (rho 0.523, z 0.85); nifty_midcap_100 (rho 0.513, z 1.73); nifty_fmcg (rho -0.502, z -0.89); nifty_50 (rho 0.493, z 0.32)
- Source: Gold retreats on profit-taking after hitting two-month peak following inflation data — Mint Markets, 2026-08-13. https://www.livemint.com/market/gold-retreats-on-profit-taking-after-hitting-two-month-peak-following-inflation-data-11786647773501.html
- Source: Sandisk’s stock is flying higher. Here are the new targets that are exciting Wall Street. — MarketWatch Top, 2026-08-13. https://www.marketwatch.com/story/sandisks-stock-is-flying-higher-here-are-the-new-targets-that-are-exciting-wall-street-4eaab99d?mod=mw_rss_topstories
- Source: Gem, jewellery export up a tad on rise in gold prices — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/gold/gem-jewellery-export-up-a-tad-on-rise-in-gold-prices/article71340934.ece
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.01), 2024-10-15 (d=1.11)

### [RED 6.94] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.63, z20 4.94, zc 4.42, resid-z 0.59 [moved], 1d 13.76%, |z20|=4.94
- **Mechanism**: The recent surge in dyn_301077_sz is largely priced, with a small resid_z of 0.59, indicating that the move is mostly explained by factor exposures. The VALID metal_copper_channel and VALID gold_silver_comove channels suggest that global commodity trends are influencing the move. However, the WEAK inr_oil_channel and WEAK dxy_inr_channel indicate that the Indian rupee and oil prices are not significantly impacting the move.
- **Gap**: No gap: the small resid_z of 0.59 indicates that the move is mostly explained by factor exposures, and there is no significant unexplained component.
- **India take**: The Indian instrument that expresses this move is likely to be metal equities, such as Hindalco or Tata Steel, which may react positively to the global commodity trends. However, the reaction may be muted due to the weak inr_oil_channel and dxy_inr_channel.
- Watch next: dyn_301077_sz (up) — already moved; resid_z is small, indicating the move is largely priced
- Source: Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-on-ai-optimism-hong-kong-shares-mostly-flat/articleshow/133199079.cms
- Source: Global Market: China stocks rise as tech shares lead gains ahead of US CPI — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-as-tech-shares-lead-gains-ahead-of-us-cpi/articleshow/133172233.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [AMBER 6.15] commodities · 2 series ↓
- wti [COMMODITIES]: last 81.08, z20 -0.32, zc -0.88, resid-z -0.45 [quiet], 1d -2.63%, 1-session move -2.63% ≥ 1.5%
- brent [COMMODITIES]: last 86.91, z20 -0.22, zc -0.78, resid-z -0.43 [quiet], 1d -2.33%, 1-session move -2.33% ≥ 1.5%
- **Mechanism**: The recent decline in WTI and Brent crude oil prices can be attributed to the influx of Middle Eastern oil hitting American shores, which may alleviate the market squeeze caused by wartime demand for American exports. This supply increase may lead to a decrease in oil prices, which in turn could affect the demand for oil and related markets. The valid metal_copper_channel and the weak inr_oil_channel may also play a role in transmitting this move to Indian metal equities and the INR.
- **Gap**: No gap: the big raw move in oil prices has a relatively small resid_z, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted to the WTI move. The Dyn Bharat Coal NS, which has a correlation with WTI, is still quiet and worth watching.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI move
- **India receivers**: nifty_midcap_100 (rho -0.424, z 1.73); dyn_bharatcoal_ns (rho -0.376, z -0.79)
- Source: An Influx of Middle Eastern Oil Is Finally Hitting American Shores — Mint Markets, 2026-08-13. https://www.livemint.com/market/an-influx-of-middle-eastern-oil-is-finally-hitting-american-shores-11786646737926.html
- Source: Oil Shocks Could Accelerate EV Adoption, WoodMac Says — OilPrice, 2026-08-13. https://oilprice.com/Latest-Energy-News/World-News/Oil-Shocks-Could-Accelerate-EV-Adoption-WoodMac-Says.html
- Source: Jefferies: Diesel Cracks Reveal the Real Oil Market Squeeze — OilPrice, 2026-08-13. https://oilprice.com/Energy/Crude-Oil/Jefferies-Diesel-Cracks-Reveal-the-Real-Oil-Market-Squeeze.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.76] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.76, zc n/a, resid-z n/a [quiet], 1d 0.32%, 52-wk extreme (pct=100); |z20|=2.76; 1y-pct=100
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 2.88, indicating a significant deviation from its historical mean. This move is likely priced, given the high z20 level and the fact that the resid_z is None, suggesting that the move is largely explained by factor exposures. The RISK_ON regime and VALID channels such as gold_silver_comove and metal_copper_channel may contribute to the propagation of this move.
- **Gap**: No gap: the move is largely priced, with a high z20 level and no unexplained component (resid_z=None)
- **India take**: The Nifty Midcap 100 index has already reacted to this move, given its high correlation with the midcap_largecap_ratio. Other Indian transmission candidates such as dyn_fincables_ns and dyn_indianb_ns have also reacted, while dyn_bharatcoal_ns and dyn_pcjeweller_ns remain quiet.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.53, z 1.73); dyn_bharatcoal_ns (rho 0.41, z -0.79); dyn_fincables_ns (rho 0.402, z 2.9); dyn_pcjeweller_ns (rho 0.376, z -0.21)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 5.53] commodities · 2 series ↑
- corn [COMMODITIES]: last 472.25, z20 2.69, zc 2.61, resid-z 2.37 [unexplained], 1d 3.34%, |z20|=2.69; 1y-pct=98
- wheat [COMMODITIES]: last 668.50, z20 0.40, zc 1.29, resid-z 1.10 [quiet], 1d 2.41%, 1y-pct=96
- **Mechanism**: The recent surge in corn prices, triggered by the USDA's unexpected yield cut due to heat waves, has created a ripple effect in the commodities market. This move is largely unexplained by factor exposures, as indicated by the high resid_z values for corn and wheat. The valid metal_copper_channel and gold_silver_comove channels may facilitate the transmission of this commodities move to Indian metal equities.
- **Gap**: No gap: the big raw move in corn has a small resid_z relative to its z20, indicating it is largely priced in
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted to the wheat price move, given its correlation with wheat. Other Indian metal equities may follow suit due to the valid metal_copper_channel.
- Watch next: dyn_lenskart_ns (up) — already moved; rho=0.382 with wheat
- **India receivers**: dyn_lenskart_ns (rho 0.38, z 2.26)
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Source: WHEAT JUMPS AFTER RUSSIAN PORT STRIKE Wheat futures surged 2.4% after Ukrainian drones reportedly struck two grain terminals at Russia’s Novorossiysk port. The terminals handle roughly 15 million metric tons of grain exports annually, raising concerns over disruptions to — DeItaone, 2026-08-12. https://t.me/walter_bloomberg/34681
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.9] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1249.30, z20 2.90, zc -0.57, resid-z -0.80 [quiet], 1d -2.40%, |z20|=2.90; 1y-pct=99
- **Mechanism**: The recent surge in Finolex Cables' shares is driven by its strong Q1 performance, with a 52.6% YoY rise in net profit and a 44.3% increase in revenue. This move is priced, given the company's robust operational performance and the resultant expansion in margins. The metal_copper_channel, which is currently valid, may also contribute to the propagation of this move, as global copper leads Indian metal equities.
- **Gap**: No gap: the move in Finolex Cables' shares is largely explained by its strong Q1 performance and is therefore priced
- **India take**: The Indian instruments that express this move are the nifty_midcap_100 and midcap_largecap_ratio, both of which have already reacted to the surge in Finolex Cables' shares. Additionally, dyn_bharatcoal_ns may also be affected, although it has not yet reacted.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to dyn_fincables_ns
- Watch next: midcap_largecap_ratio (up) — already moved; reacted to dyn_fincables_ns
- **India receivers**: nifty_midcap_100 (rho 0.422, z 1.73); midcap_largecap_ratio (rho 0.402, z 2.76); dyn_bharatcoal_ns (rho 0.38, z -0.79)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Source: Finolex Cables shares jump 10% on strong Q1 performance; revenue crosses Rs 2,000 crore mark — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/finolex-cables-shares-jump-10-on-strong-q1-performance-revenue-crosses-rs-2000-crore-mark/articleshow/133172179.cms
- Source: Q1 Results Today Live: Tata Motors, Apollo Hospitals, HAL, Grasim GMR Airports, Lenskart, Abbott, VA Tech, IRCON, AIA, IRCTC, Sun TV, EID Parry to announce Q1 results, NBCC, Siemens, RVNL, Kalpataru, MRF, Zydus Lifesciences, KPI Green, Manappuram Finance in focus, TD Power Systems, Finolex shares hit 52-week high — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-hal-grasim-ind-tata-motors-apollo-hospitals-gmr-airports-lenskart-gic-abbott-aia-engg-irctc-sun-tv-eid-parry-va-tech-ircon-titagarh-results-12-august-2026/article71332017.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

### [AMBER 4.69] rates · 3 series ↑
- ust_30y [RATES]: last 5.24, z20 1.37, zc -0.23, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=99
- ust_10y [RATES]: last 4.70, z20 0.96, zc -0.42, resid-z -0.98 [quiet], 1d -0.42%, 1y-pct=98
- tips_10y_real [RATES]: last 2.43, z20 0.80, zc 0.00, resid-z -0.59 [quiet], 1d 0.00%, 1y-pct=97
- **Mechanism**: The recent rise in US Treasury yields, particularly the 10-year yield reaching its highest level since 2007, is likely to propagate through the metal_copper_channel, affecting Indian metal equities. The valid gold_silver_comove channel may also influence the price of gold and silver in the Indian market. However, the weak inr_oil_channel and dxy_inr_channel may limit the transmission of global rate hikes to the Indian rupee.
- **Gap**: No gap: the big raw move in US Treasury yields has a small resid_z, indicating that the move is largely priced in
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the rise in US Treasury yields. However, the weak inr_oil_channel and dxy_inr_channel may limit the transmission of global rate hikes to the Indian rupee.
- Watch next: dyn_bond (down) — not yet - watch; historically leads by 1d
- Watch next: brent (up) — not yet - watch; historically leads by 3d
- Source: Global Market: Japanese bond yields hold near highs as markets brace for BOJ rate hike — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-hold-near-highs-as-markets-brace-for-boj-rate-hike/articleshow/133203276.cms
- Source: Gold and silver trade lacklustre on MCX despite soft US inflation data; elevated dollar, bond yields weigh — Mint Markets, 2026-08-13. https://www.livemint.com/market/commodities/gold-and-silver-prices-today-rates-lacklustre-on-mcx-despite-soft-us-inflation-data-elevated-dollar-bond-yields-weigh-11786591359947.html
- Source: US Sells 10-Year Debt at Highest Yields Since Financial Crisis — Mint Markets, 2026-08-12. https://www.livemint.com/market/us-sells-10-year-debt-at-highest-yields-since-financial-crisis-11786566124472.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

### [RED 4.52] dyn_crwv ↑
- dyn_crwv [EQUITIES]: last 107.45, z20 2.52, zc -0.04, resid-z 0.90 [quiet], 1d -0.26%, |z20|=2.52
- **Mechanism**: The recent surge in CoreWeave's stock price, driven by strong AI infrastructure company earnings and upbeat quarterly results, has led to a rise in dyn_crwv. This move is priced, with a small resid_z of 0.9, indicating that the factor exposures have largely explained the move. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, but the current RISK_ON regime may mitigate this effect.
- **Gap**: No gap: the move in dyn_crwv is largely priced, with a small resid_z and a significant z20 level of 2.58
- **India take**: The Indian instrument that expresses this move is nifty_fmcg, which has a negative correlation with dyn_crwv. However, nifty_fmcg has not yet reacted to the move in dyn_crwv, and its current status is quiet.
- Watch next: nifty_fmcg (down) — not yet - watch; rho=-0.375 via dyn_crwv
- **India receivers**: nifty_fmcg (rho -0.377, z -0.89)
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: US stocks: CoreWeave, Super Micro surge on signs of sustained AI buildout — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-coreweave-super-micro-surge-on-signs-of-sustained-ai-buildout/articleshow/133187386.cms
- Source: CoreWeave’s stock is rocketing after earnings lead to praise from bulls and bears alike — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/coreweaves-stock-is-rocketing-after-earnings-lead-to-praise-from-bulls-and-bears-alike-46c831e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-13 (d=0.01), 2025-08-05 (d=0.04)

## Watchlist (below surfacing floor)
dyn_cupid_ns ↑ (4.48), indices · 2 series ↑ (4.45), dyn_lenskart_ns ↑ (4.26), dyn_ohi ↓ (4.0), dyn_tatatech_ns ↑ (3.8), dyn_atherenerg_ns ↑ (3.61), dyn_bac ↑ (3.56), dyn_tech ↑ (3.31), fx · 2 series ↑ (3.26), usd_brl ↑ (2.87), dyn_hdb ↓ (2.82), dyn_icicigi_bo ↓ (2.79)

## India macro
- nifty_50: 24395.8496 (1d -0.16%, z20 0.32, flag none)
- nifty_midcap_100: 64122.0000 (1d 0.15%, z20 1.73, flag amber)
- usd_inr: 95.4400 (1d 0.06%, z20 -0.72, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6284 (1d 0.32%, z20 2.76, flag red)
- Next India prints: NSDL FPI flows T-0d · India WPI T-1d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 94.2 — "LG Electronics India Q1 Results: PAT rises 27% YoY to Rs 653 crore; revenue up 15%"
- INOXINDIA.NS (INOX INDIA LIMITED) score 93.0 — "LG Electronics India Q1 Results: PAT rises 27% YoY to Rs 653 crore; revenue up 15%"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 92.5 — "LG Electronics India Q1 Results: PAT rises 27% YoY to Rs 653 crore; revenue up 15%"
- INDIANB.NS (INDIAN BANK) score 70.1 — "Indian govt should disclose sugar stock after physical verification, says Naiknavare of NF"
- BAC (Bank of America Corporation) score 57.5 — "DETROIT AUTOMAKERS TO ARGUE TO WHITE HOUSE THAT REVISED NORTH AMERICAN TRADE DEAL COULD CO"
- OHI (Omega Healthcare Investors, In) score 55.1 — "Dow Jones| Nasdaq | US Stock Market Today | Live: S&P, Nasdaq gain as investors assess Mid"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.9 — "US stocks: S&P 500 hits intraday record as tech stocks rally, crude oil prices fall"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.4 — "US stocks: S&P 500 hits intraday record as tech stocks rally, crude oil prices fall"
- COIN (Coinbase Global, Inc.) score 51.8 — "Russia’s Diesel Exports Crash to Multiyear-Low amid Tight Global Market"
- TECH (Bio-Techne Corp) score 51.7 — "US stocks: S&P 500 hits intraday record as tech stocks rally, crude oil prices fall"
- HDB (HDFC Bank Limited) score 49.9 — "Bank of Baroda raises $700 million in first overseas bond issue since 2019"
- CHKP (Check Point Software Technolog) score 46.6 — "IPO GMP Today Live Updates: Dhoot Transmission, Milky Mist, Shiprocket & Behari Lal in Foc"
- IDBI.NS (IDBI BANK LIMITED) score 45.7 — "Bank of Baroda raises $700 million in first overseas bond issue since 2019"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.7 — "Bank of Baroda raises $700 million in first overseas bond issue since 2019"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.4 — "Bank of Baroda raises $700 million in first overseas bond issue since 2019"
- LTH (Life Time Group Holdings, Inc.) score 39.8 — "DIESEL CRACKS RISE ABOVE $98.00, AN ALL-TIME HIGH, AFTER REPORTS SAY YEMEN'S HOUTHIS ATTAC"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.5 — "UK Economy Remains Resilient Despite Iran War and Higher Energy Prices"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 29.4 — "Tata Motors CV shares surge over 4% after Q1 profit growth"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.7 — "AMD - AMD EYES $5 BILLION DEBT SALE FOR AI EXPANSION AMD plans to raise up to $5B through "
- 301077.SZ (CHINASTARS) score 26.5 — "High Oil Prices Deliver a Windfall for China’s Coal-to-Chemicals Industry"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 24.7 — "Tata Motors CV shares surge over 4% after Q1 profit growth"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.6 — "Muthoot Fincorp files draft papers for ₹3,000 crore IPO"
- JIOFIN.BO (Jio Financial Services Limited) score 17.6 — "PCE INFLATION SEEN AT 3.6% IN JULY Oxford Economics expects the Fed’s preferred inflation "
- JUSTDIAL.BO (JUST DIAL LTD.) score 17.0 — "DEEPSEEK ANNOUNCES ADJUSTMENT TO API RPICING - STATEMENT"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 16.3 — "Coal India Share Price Live Updates: Coal India  Current Valuation"
- MS (Morgan Stanley) score 14.4 — "UPGRADES • $ABBV: Upgraded Peerperform → Outperform by Wolfe Research; PT $300 • $ABT: Upg"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 13.9 — "Will Bharti Airtel’s ARPU increase after scrapping Rs 299, other popular prepaid plans? Wh"
- NVDA (NVIDIA Corporation) score 9.9 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.5 — "Gem, jewellery export up a tad on rise in gold prices"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.6 — "Sugar stocks Balrampur Chini, Dhampur Sugar, Dalmia Bharat Sugar, others rally up to 7%. H"
- META (Meta) score 7.9 — "Newly-listed metal stock Rajputana Stainless surges 10%, hits record high after strong Q1 "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.1 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- AAPL (Apple Inc.) score 6.9 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 6.7 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.5 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- INTC (Intel Corporation) score 5.1 — "PRESIDENT’S SCHEDULE — AUGUST 13, 2026 🔸 8:00 AM — Executive Time White House · Closed Pre"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.9 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 2.2 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 2.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 1.9 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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