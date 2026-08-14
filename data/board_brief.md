# Transmission Layer — board brief · 2026-08-14 15:06Z

data as of **2026-08-14** · 98 series · 8 red / 39 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.208, 2d in regime; vol-pct 0.239, breadth-off 0.176, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.41, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.85, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.29, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.12, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.81, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.11, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.21, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.17, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0007248582980661222)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2521) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.27] cross-asset · 14 series ↑
- comex_gold [COMMODITIES]: last 4440.00, z20 2.04, zc 1.24, resid-z 0.62 [quiet], 1d 1.75%, |z20|=2.04; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3063.66, z20 1.88, zc 0.30, resid-z 0.84 [quiet], 1d 0.35%, |z20|=1.88; 1y-pct=100
- comex_silver [COMMODITIES]: last 65.47, z20 1.77, zc 0.39, resid-z -1.02 [quiet], 1d 0.93%, |z20|=1.77; co-occur[gold_silver] same-direction (channel VALID)
- dyn_nvda [EQUITIES]: last 225.94, z20 1.63, zc 0.11, resid-z 1.25 [quiet], 1d 0.28%, 1y-pct=99
- dyn_vt [EQUITIES]: last 162.35, z20 1.59, zc -0.03, resid-z 0.94 [quiet], 1d -0.02%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30029.52, z20 1.50, zc -0.14, resid-z 0.61 [quiet], 1d -0.18%, 1y-pct=95
- sp500 [INDICES]: last 7791.77, z20 1.45, zc -0.12, resid-z -0.45 [quiet], 1d -0.09%, 1y-pct=99
- vix [INDICES]: last 14.47, z20 -1.41, zc -0.14, resid-z n/a [quiet], 1d -1.09%, 1y-pct=3
- dax [INDICES]: last 26431.12, z20 1.34, zc 0.70, resid-z 0.48 [quiet], 1d 0.50%, 1y-pct=100
- stoxx_50 [INDICES]: last 6541.91, z20 1.31, zc -0.07, resid-z -0.23 [quiet], 1d -0.05%, 1y-pct=99
- gold_silver_ratio [DERIVED]: last 67.81, z20 -1.10, zc n/a, resid-z n/a [quiet], 1d 0.82%, GSR<75 (extreme low)
- dow_jones [INDICES]: last 53782.80, z20 0.94, zc -0.15, resid-z -0.22 [quiet], 1d -0.11%, 1y-pct=97
- comex_copper [COMMODITIES]: last 6.60, z20 0.90, zc 0.06, resid-z -0.14 [quiet], 1d 0.14%, 1y-pct=97
- cac_40 [INDICES]: last 8644.16, z20 0.79, zc -0.10, resid-z -0.30 [quiet], 1d -0.07%, 1y-pct=96
- **Mechanism**: The recent surge in Reddit shares following its inclusion in the S&P 500 index has led to a ripple effect in the global markets, with the risk-on regime and valid gold-silver co-move channel contributing to the current market sentiment. The metal copper channel is also valid, indicating a potential transmission to Indian metal equities. However, the real rates gold inverse and gsr stress gauge channels are weak, which may limit the upside potential of gold and silver.
- **Gap**: No gap: the big raw move in Reddit shares is largely priced, given the clear news-driven catalyst and the expected influx of index fund buying.
- **India take**: The Indian metal sector, as represented by nifty_metal, may react positively to the strength in comex_silver, while nifty_midcap_100 has already reacted to the move in dax. However, the reaction in Indian markets may be muted due to the weak channels such as inr_oil_channel and dxy_inr_channel.
- Watch next: nifty_metal (up) — not yet - watch; correlated with comex_silver
- Watch next: nifty_midcap_100 (up) — already moved; correlated with dax
- **India receivers**: nifty_metal (rho 0.511, z 0.45); nifty_midcap_100 (rho 0.498, z 1.06); nifty_fmcg (rho -0.496, z -1.62); nifty_50 (rho 0.489, z 0.16)
- Source: Reddit shares jump 15% as social media platform set to join S&P 500 — Mint Markets, 2026-08-14. https://www.livemint.com/market/stock-market-news/reddit-shares-jump-15-as-social-media-platform-set-to-join-s-p-500-11786715061238.html
- Source: US stocks: Reddit surges 14% on S&P 500 inclusion, set to replace AvalonBay — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-reddit-surges-14-on-sp-500-inclusion-set-to-replace-avalonbay/articleshow/133244407.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US futures subdued as higher oil prices curb risk appetite after S&P 500’s record close — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-hormuz-deal-crude-oil-fed-warsh-rate-hike-applied-materials-apple-reddit-chip-stock-price-news-14th-august-2026/liveblog/133241270.cms
- Historical analogues: 2024-11-26 (d=0.9), 2025-10-31 (d=0.97), 2025-10-24 (d=1.11)

### [RED 6.35] commodities · 2 series ↑
- corn [COMMODITIES]: last 479.50, z20 3.52, zc 5.50, resid-z 4.13 [unexplained], 1d 7.03%, |z20|=3.52; 1y-pct=100
- wheat [COMMODITIES]: last 687.25, z20 1.36, zc 2.98, resid-z 2.05 [unexplained], 1d 5.29%, 1y-pct=99
- **Mechanism**: The recent surge in corn and wheat prices is driven by supply concerns due to heat waves impacting crop yields in the US, as reported by the USDA. This has led to a significant price increase, with corn futures rising by as much as 4.6%. The metal_copper_channel and gold_silver_comove channels are valid and may influence the price movement of Indian metal equities and other correlated instruments.
- **Gap**: No gap: the big raw move in corn and wheat prices is largely explained by the USDA's yield reduction and heat waves, leaving resid_z values of 4.13 and 2.05, respectively, indicating that the price move is mostly priced in.
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted with a z20 value of 3.07, indicating some transmission of the global commodity price movement to the Indian market. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.417, z 3.07)
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [AMBER 6.03] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 2.36, zc 1.06, resid-z 1.14 [quiet], 1d 0.47%, |z20|=2.36
- usd_mxn [FX]: last 17.00, z20 -2.31, zc -0.89, resid-z -0.80 [quiet], 1d -0.34%, |z20|=2.31; 1y-pct=0
- gbp_usd [FX]: last 1.36, z20 1.80, zc 0.95, resid-z 0.83 [quiet], 1d 0.40%, |z20|=1.80
- eur_usd [FX]: last 1.16, z20 1.68, zc 1.43, resid-z 1.26 [quiet], 1d 0.49%, |z20|=1.68
- **Mechanism**: The recent rebound in cash acceptance in the euro area and steady oil prices have led to a slight increase in the euro and other currencies against the US dollar, as the market's anticipation of a Federal Reserve rate increase lessens. This move is largely priced, given the small resid_z values for the affected currency pairs.
- **Gap**: No gap: the move is largely priced, with small resid_z values for the affected currency pairs.
- **India take**: The Indian rupee may weaken against the euro, as expressed through the eur_inr pair, which has already reacted to the move. Other Indian instruments, such as dyn_icicigi_bo, may also be affected through their correlation with the gbp_usd pair.
- Watch next: eur_usd (up) — already moved; reacted to ECB press on cash acceptance
- Watch next: aud_usd (up) — already moved; reacted to general dollar weakness
- **India receivers**: dyn_muthootfin_ns (rho -0.55, z -1.66); eur_inr (rho 0.481, z 2.38); dyn_icicigi_bo (rho -0.425, z -0.53)
- Source: Cash remains most widely accepted payment method in euro area — ECB press, 2026-08-13. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260813~389729d6a9.en.html
- Source: Euro zone bonds little changed as oil prices steady — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-little-changed-as-oil-prices-steady/articleshow/133203702.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.07] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 612.00, z20 3.07, zc 1.87, resid-z 1.52 [unexplained], 1d 2.53%, |z20|=3.07; 1y-pct=99
- **Mechanism**: The recent surge in Lenskart Solutions' stock price can be attributed to the company's strong Q1 results, which showed a near four-fold jump in profit, and the buzz around its potential MSCI inclusion. This positive news has led to increased investor interest, driving up the stock price. The VALID metal_copper_channel and vix_equity_inverse channels indicate a risk-on environment, which supports the stock's upward movement.
- **Gap**: No gap: the stock's price move is largely priced in, given the significant increase in profit and positive market sentiment
- **India take**: The Indian instrument that expresses this move is Lenskart Solutions, which has already reacted positively to the news, and other retail-focused stocks may follow suit. The Nifty Retail index may also be affected, potentially leading to a broader market impact.
- Watch next: Lenskart Solutions (up) — already moved; strong Q1 results and MSCI inclusion buzz
- Source: Lenskart Solutions among 7 stocks hitting 52-week highs; surge up to 20% in a month — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-7-stocks-hitting-52-week-highs-surge-up-to-20-in-a-month/slideshow/133210592.cms
- Source: Lenskart shares soar after strong Q1 results and MSCI inclusion buzz — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/lenskart-shares-zoom-nearly-7-to-fresh-52-week-high-after-strong-q1-results-and-msci-inclusion-buzz/article71339607.ece
- Source: Lenskart shares hit record high after Q1 profit jumps nearly four-fold; Motilal Oswal lifts target price — Mint Markets, 2026-08-13. https://www.livemint.com/market/stock-market-news/lenskart-shares-hit-record-high-after-q1-profit-jumps-nearly-four-fold-motilal-oswal-lifts-target-price-11786610679031.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.88] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.01, z20 2.88, zc -0.29, resid-z 1.57 [unexplained], 1d -2.44%, |z20|=2.88
- **Mechanism**: The dyn_301077_sz move is unexplained by factor exposures, with a resid_z of 1.57, suggesting a potential anomaly. However, the big raw move with small resid_z indicates that the move is largely priced in. The VALID metal_copper_channel and gold_silver_comove channels may be influencing the move, but the WEAK/INVERTED channels, such as safe_haven_gold and inr_oil_channel, are not available as mechanisms. The RISK_ON regime and vix_equity_inverse channel also support the move.
- **Gap**: No gap: the move is largely priced in with a small resid_z
- **India take**: The Indian instrument that expresses this move is likely to be metal equities, such as Hindalco or Tata Steel, which may react positively due to the VALID metal_copper_channel. However, the reaction is already reflected in the price.
- Watch next: dyn_301077_sz (up) — already moved; unexplained move with high z20 level
- Source: Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-on-ai-optimism-hong-kong-shares-mostly-flat/articleshow/133199079.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.66] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.66, zc n/a, resid-z n/a [quiet], 1d -0.41%, 52-wk extreme (pct=98); |z20|=1.66; 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 1.66, indicating a potential mean reversion. However, the resid_z is None, suggesting that the move is largely priced in by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly relate to the midcap_largecap_ratio, but the vix_equity_inverse channel may influence the broader equity market, including midcaps.
- **Gap**: No gap: the move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to the midcap_largecap_ratio move, while other transmission candidates like Dyn Bharat Coal and Dyn Fincables have not yet reacted significantly. The Indian metal equities may be influenced by the global copper prices through the metal_copper_channel.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.535, z 1.06); dyn_bharatcoal_ns (rho 0.404, z -0.93); dyn_fincables_ns (rho 0.397, z 2.31); dyn_pcjeweller_ns (rho 0.364, z 0.27)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.56] rates · 3 series ↑
- ust_30y [RATES]: last 5.24, z20 1.24, zc 0.00, resid-z -0.12 [quiet], 1d 0.00%, 1y-pct=98
- ust_10y [RATES]: last 4.68, z20 0.50, zc -0.43, resid-z -0.76 [quiet], 1d -0.43%, 1y-pct=96
- tips_10y_real [RATES]: last 2.42, z20 0.47, zc -0.26, resid-z -0.80 [quiet], 1d -0.41%, 1y-pct=96
- **Mechanism**: The recent surge in bond yields, driven by AI-driven demand and increased borrowing by governments, has led to a rise in inflation-adjusted borrowing costs across major economies. This move is priced, as evidenced by the small resid_z values for the affected series, indicating that the move is largely explained by factor exposures.
- **Gap**: No gap: the move in bond yields is largely explained by factor exposures, as indicated by the small resid_z values
- **India take**: Indian government bonds, such as the 10-year GoI bond, may react positively to the easing oil prices and lower US Treasury yields, although the fresh supply from the weekly debt auction could limit further advances. The metal_copper_channel may also influence Indian metal equities.
- Watch next: ust_30y (down) — already moved; High yields have priced in the current market conditions
- Source: Bond yields are at multiyear highs, yet stocks have hit fresh records. Here’s how long the defiance can last. — MarketWatch Top, 2026-08-14. https://www.marketwatch.com/story/rates-are-at-multiyear-highs-yet-stocks-hit-fresh-records-heres-how-long-the-defiance-may-last-b29a5d14?mod=mw_rss_topstories
- Source: AI-driven surge in bond yields could be next risk for markets and growth — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/ai-driven-surge-in-bond-yields-could-be-next-risk-for-markets-and-growth/article71344109.ece
- Source: Indian bonds poised for positive start on lower oil prices, Treasury yields — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/indian-bonds-poised-for-positive-start-on-lower-oil-prices-treasury-yields/article71343962.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

### [AMBER 4.53] cross-asset · 2 series ↓
- btc_usd [CRYPTO]: last 62594.96, z20 -1.69, zc -0.77, resid-z -0.82 [quiet], 1d -1.27%, |z20|=1.69
- dyn_coin [EQUITIES]: last 148.83, z20 -0.91, zc -0.71, resid-z 0.11 [quiet], 1d -3.29%, 1y-pct=4
- **Mechanism**: The recent decline in bitcoin and dyn_coin prices can be attributed to weak liquidity and subdued institutional demand, despite softer US inflation data. This move is largely priced, given the small resid_z values for both series, indicating that the decline is largely explained by factor exposures. The VALID metal_copper_channel and vix_equity_inverse channels suggest that global risk sentiment and volatility are influencing the move.
- **Gap**: No gap: the move in btc_usd and dyn_coin is largely priced, with small resid_z values indicating that the decline is explained by factor exposures
- **India take**: The Indian instrument that expresses this move is likely to be the metal equities, given the VALID metal_copper_channel. However, the response of Indian metal equities has not been significant yet, and the INR has not weakened significantly due to the WEAK inr_oil_channel.
- Watch next: eth_usd (down) — not yet - watch; high correlation with btc_usd
- Source: Batten down the hatches and allocate defensively because global liquidity has peaked, argues veteran strategist — MarketWatch Top, 2026-08-14. https://www.marketwatch.com/story/batten-down-the-hatches-and-allocate-defensively-because-global-liquidity-has-peaked-argues-veteran-strategist-b68673b0?mod=mw_rss_topstories
- Source: Bitcoin hovers near $63,000 despite softer US inflation as weak liquidity weighs on crypto — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-hovers-near-63000-despite-softer-us-inflation-as-weak-liquidity-weighs-on-crypto/articleshow/133236737.cms
- Source: Global Market: Rising real yields raise fresh risks for stocks and global economic growth — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-rising-real-yields-raise-fresh-risks-for-stocks-and-global-economic-growth/articleshow/133236127.cms
- Historical analogues: 2026-05-22 (d=0.03), 2026-04-02 (d=0.2), 2025-10-22 (d=0.36)

## Watchlist (below surfacing floor)
dxy ↓ (4.34), nikkei_225 ↑ (3.73), dyn_bac ↑ (3.71), dyn_tatatech_ns ↑ (3.56), dyn_atherenerg_ns ↑ (3.33), usd_brl ↑ (3.3), dyn_tech ↑ (2.91), dyn_lth ↑ (2.83), dyn_indusindbk_bo ↑ (2.7), dyn_hdb ↓ (2.66), indices · 2 series ↑ (2.6), bovespa ↓ (2.55)

## India macro
- nifty_50: 24366.0000 (1d -0.12%, z20 0.16, flag none)
- nifty_midcap_100: 63782.6484 (1d -0.53%, z20 1.06, flag amber)
- usd_inr: 95.4150 (1d 0.07%, z20 -0.68, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6177 (1d -0.41%, z20 1.66, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 105.9 — "Sebi proposes easier digital KYC for Indians living abroad"
- INOXINDIA.NS (INOX INDIA LIMITED) score 104.9 — "Sebi proposes easier digital KYC for Indians living abroad"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 104.5 — "Sebi proposes easier digital KYC for Indians living abroad"
- INDIANB.NS (INDIAN BANK) score 72.0 — "Sebi proposes easier digital KYC for Indians living abroad"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.8 — "Technocraft Ventures ends debut day with 47% gains; LEAP India settles 9% below listing pr"
- BAC (Bank of America Corporation) score 54.9 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.5 — "Technocraft Ventures ends debut day with 47% gains; LEAP India settles 9% below listing pr"
- OHI (Omega Healthcare Investors, In) score 54.0 — "Under Chandrasekaran, as Tata stocks changed, so did their investors"
- TECH (Bio-Techne Corp) score 53.9 — "Technocraft Ventures ends debut day with 47% gains; LEAP India settles 9% below listing pr"
- COIN (Coinbase Global, Inc.) score 53.9 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- HDB (HDFC Bank Limited) score 47.7 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- CHKP (Check Point Software Technolog) score 45.9 — "Behari Lal Engineering IPO Day 3: Issue booked 93.21x so far. Check GMP, subscriptions, ke"
- IDBI.NS (IDBI BANK LIMITED) score 43.3 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.3 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.1 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- LTH (Life Time Group Holdings, Inc.) score 38.4 — "Applied Materials shares are down on guidance and margin concerns. Analysts call it time t"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 32.8 — "Under Chandrasekaran, as Tata stocks changed, so did their investors"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.7 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.6 — "India bonds end week flat, but demand for long notes firms"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 28.9 — "Under Chandrasekaran, as Tata stocks changed, so did their investors"
- 301077.SZ (CHINASTARS) score 26.5 — "Unitree IPO: China’s humanoid robot starset for potentially explosive Shanghai debut"
- JIOFIN.BO (Jio Financial Services Limited) score 21.1 — "Skyways Air Services IPO to open August 24 at ₹138 upper band"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 19.1 — "India's Coal Demand Set to Hit 1.6 Billion Tons by 2030"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.2 — "Muthoot Fincorp files draft papers for ₹3,000 crore IPO"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.2 — "Crypto exchanges are evolving into financial superapps; traditional assets emerge as key g"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.1 — "DEEPSEEK ANNOUNCES ADJUSTMENT TO API RPICING - STATEMENT"
- MS (Morgan Stanley) score 12.8 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 10.9 — "Bharat Dynamics Q1 results: Profit sees sixfold increase, revenue surges 131% YoY"
- META (Meta) score 9.4 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.8 — "Brokerages initiate coverage on Vedanta Aluminium, Kalyan Jewellers, 3 other stocks with u"
- NVDA (NVIDIA Corporation) score 8.2 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.8 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- AAPL (Apple Inc.) score 5.7 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 5.5 — "China’s next economic ambition: workshop for the Muslim world"
- RDDT (Reddit, Inc.) score 4.8 — "US stocks mixed after weak retail sales data, Reddit jumps 14.7%, Middle East in focus"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.5 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.4 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 1.8 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 1.8 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 1.6 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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