# Transmission Layer — board brief · 2026-07-16 06:08Z

data as of **2026-07-16** · 98 series · 12 red / 38 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.462, 8d in regime; vol-pct 0.55, breadth-off 0.375, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.08, corr60 -0.45, contra nifty_50 corr20=0.37, last shift 2026-05-20. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.46, corr60 0.36, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.01, last shift 2026-05-27. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.79, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.03, corr60 -0.05, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.28, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.32, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 87** scanned series survive multiplicity control (effective p ≤ 0.0002834212197515562)
- **SETUP** dyn_blk → asx_200: leads 1d (ccf 0.499, β 0.2402, p 0.0); driver zc 3.88 → expected 1.56%. Type hit-rate 0.817 (n=2433).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.467, β 0.1393, p 0.0); driver zc 2.05 → expected 0.823%. Type hit-rate 0.817 (n=2433).
- **SETUP** dyn_blk → taiwan_weighted: leads 1d (ccf 0.371, β 0.3551, p 0.0); driver zc 3.88 → expected 2.306%. Type hit-rate 0.817 (n=2433).
- **SETUP** dyn_jef → nikkei_225: leads 1d (ccf 0.367, β 0.2418, p 0.0); driver zc 2.05 → expected 1.43%. Type hit-rate 0.817 (n=2433).
- **SETUP** dyn_blk → usd_mxn: leads 1d (ccf -0.328, β -0.1334, p 0.0); driver zc 3.88 → expected -0.866%. Type hit-rate 0.817 (n=2433).
- **SETUP** dyn_jef → usd_mxn: leads 1d (ccf -0.257, β -0.065, p 9e-05); driver zc 2.05 → expected -0.384%. Type hit-rate 0.817 (n=2433).
- Track record · residual_reversion: hit-rate **0.489** (n=1136) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2433) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.57] dyn_pypl ↑
- dyn_pypl [EQUITIES]: last 55.52, z20 6.57, zc 7.00, resid-z -0.56 [moved], 1d 17.20%, |z20|=6.57
- **Mechanism**: The surge in PayPal shares following a reported $53 billion buyout offer from Stripe and Advent International has triggered a rally in the US markets, with the S&P 500 and Dow Jones Industrial Average rising. This move is likely to propagate through the VALID vix_equity_inverse channel, where a vol spike would typically lead to an equity drawdown, but in this case, the positive news has led to a rise in equities. The metal_copper_channel may also play a role, as global copper leads Indian metal equities, potentially influencing the Indian market.
- **Gap**: No gap: the big raw move in dyn_pypl has a relatively small resid_z of 0.99, indicating that the move is largely priced in and not an anomaly
- **India take**: The Indian instruments dyn_patanjali_ns and dyn_pcjeweller_ns have already reacted to the move in dyn_pypl, with dyn_patanjali_ns having a negative correlation and dyn_pcjeweller_ns having a positive correlation. The metal_copper_channel may also influence the Indian metal equities.
- Watch next: dyn_patanjali_ns (down) — already moved; rho=-0.615 via dyn_pypl
- Watch next: dyn_pcjeweller_ns (up) — already moved; rho=0.359 via dyn_pypl
- **India receivers**: dyn_patanjali_ns (rho -0.639, z -4.17); dyn_pcjeweller_ns (rho 0.365, z 1.75); dyn_nuvoco_ns (rho 0.36, z 2.72); nifty_it (rho 0.141, z 1.65)
- Source: PayPal’s battered stock is getting a record boost from a report of buyout interest — MarketWatch Top, 2026-07-15. https://www.marketwatch.com/story/a-53-billion-lifeline-stripe-and-advent-reportedly-team-up-to-bid-for-battered-paypal-3bc6fcc2?mod=mw_rss_topstories
- Source: PayPal shares jump over 15% after Stripe, Advent make $53 billion buyout offer — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/paypal-shares-jump-over-15-after-stripe-advent-make-53-billion-buyout-offer/articleshow/132418333.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-04-16 (d=0.05)

### [RED 7.71] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1611.35, z20 -5.71, zc 0.02, resid-z 0.55 [quiet], 1d -9.89%, |z20|=5.71; 1y-pct=0
- **Mechanism**: The decline in ICICI Lombard's Q1 net profit by 46% due to large fire claims and the Supreme Court's Motor TP verdict has led to a sharp fall in its share price, which may propagate to other correlated instruments such as Hero MotoCorp. The valid channel of vix_equity_inverse may also contribute to the move, as a vol spike could lead to an equity drawdown.
- **Gap**: No gap: the big raw move in ICICI Lombard's share price is largely explained by the significant decline in its Q1 net profit, leaving a relatively small resid_z of 0.55, indicating that the move is mostly priced in.
- **India take**: The Indian instrument that expresses this move is Nifty Midcap 100, which has already reacted with a z20 of 1.51. Other correlated instruments such as Hero MotoCorp, Adani Enterprises, and Jio Financial Services may also be affected, but have not yet moved.
- Watch next: dyn_heromotoco_ns (down) — not yet - watch; historically leads by 4d
- **India receivers**: dyn_heromotoco_ns (rho 0.518, z 0.19); nifty_midcap_100 (rho 0.51, z 1.51); dyn_adanient_bo (rho 0.489, z 0.97); dyn_indianb_ns (rho 0.457, z 0.09)
- Source: Q1 Results Today Live: Wipro, Jio Financial, Tech Mahindra, Polycab, BHEL, ITC Hotels, CEAT, WeWork India to announce Q1 results, Union Bank, Groww, HDBFS, HDFC AMC, HDFC Life, ICICI Pru Life, ICICI Lombard, Angel One shares in focus — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-wipro-jio-financial-tech-mahindra-polycab-india-bhel-piramal-finance-itc-hotels-ceat-wework-hdbfs-groww-icici-pru-hdfc-results-16-july-2026/article71225300.ece
- Source: ICICI Lombard General Insurance shares tumble 15% after Q1 profit takes a hit — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/icici-lombard-general-insurance-shares-tumble-15-after-q1-profit-takes-a-hit/articleshow/132430258.cms
- Source: ICICI Lombard share price crashes 15% to 52-week low after Q1 profit tanks 46%; Should you buy the dip? — Mint Markets, 2026-07-16. https://www.livemint.com/market/stock-market-news/icici-lombard-share-price-crashes-15-to-52-week-low-after-q1-profit-tanks-46-should-you-buy-the-dip-11784177808627.html
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [RED 6.28] cross-asset · 4 series ↑
- dyn_gs [EQUITIES]: last 1152.26, z20 2.62, zc 0.22, resid-z 4.90 [unexplained], 1d 1.08%, |z20|=2.62; 1y-pct=100
- dyn_ms [EQUITIES]: last 228.51, z20 1.65, zc 0.19, resid-z 1.33 [quiet], 1d 0.37%, 1y-pct=100
- sp500 [INDICES]: last 7572.20, z20 1.42, zc 0.50, resid-z -0.75 [quiet], 1d 0.38%, 1y-pct=98
- dow_jones [INDICES]: last 52658.02, z20 1.00, zc 0.39, resid-z -0.34 [quiet], 1d 0.29%, 1y-pct=98
- **Mechanism**: The recent surge in crude oil prices due to escalating US-Iran tensions is likely to propagate through the metal_copper_channel, a VALID channel, potentially impacting Indian metal equities. The vix_equity_inverse channel also suggests that the current vol spike could lead to an equity drawdown. However, the weak inr_oil_channel and dxy_inr_channel may limit the transmission of oil price shocks to the Indian market.
- **Gap**: No gap: The current move in dyn_gs and other series is largely priced, with resid_z values not significantly exceeding the z20 levels, indicating that the market has already factored in the recent events.
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which may react negatively to the surge in oil prices and subsequent potential drawdown in equities. However, the reaction is not yet evident, and the market is still watching for further developments.
- Watch next: nifty_50 (down) — not yet - watch; Potential impact of oil price surge on Indian metal equities and subsequent transmission to the broader market
- Source: Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $110/bbl, says Goldman Sachs — Mint Markets, 2026-07-16. https://www.livemint.com/market/commodities/crude-oil-prices-rise-for-4th-session-amid-escalating-us-iran-war-brent-likely-to-hit-110-bbl-says-goldman-sachs-11784163944139.html
- Source: JP Morgan moving closer to a milestone no bank has ever reached: A $1 trillion market value — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/jp-morgan-moving-closer-to-a-milestone-no-bank-has-ever-reached-a-1-trillion-market-value/articleshow/132418396.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.32), 2024-11-11 (d=0.55)

### [RED 6.17] dyn_patanjali_ns ↓
- dyn_patanjali_ns [EQUITIES]: last 348.55, z20 -4.17, zc 0.04, resid-z -12.03 [unexplained], 1d 0.19%, |z20|=4.17; 1y-pct=0
- **Mechanism**: The sharp decline in Patanjali Foods share price is largely unexplained by factor exposures, with a high residual_z of -12.03, suggesting a potential overreaction. The metal_copper_channel and vix_equity_inverse channels are valid and may be contributing to the move. However, the lack of a clear narrative and the absence of a strong transmission candidate channel suggests that the move may be idiosyncratic to Patanjali Foods.
- **Gap**: No gap: the decline in Patanjali Foods share price is largely unexplained by factor exposures, but the move is already reflected in the price
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a rho of 0.437 via dyn_patanjali_ns. The decline in Patanjali Foods share price may have a limited impact on the broader Indian market.
- Watch next: dyn_patanjali_ns (down) — already moved; sharp decline in share price
- **India receivers**: dyn_tataelxsi_ns (rho 0.437, z -1.39)
- Source: Patanjali Foods shares crash 20%, stock nearly halves in value in one year. What's ahead? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/patanjali-foods-shares-crash-20-stock-nearly-halves-in-value-in-one-year-whats-ahead/articleshow/132410105.cms
- Source: Patanjali Foods share price crashes 20%, extending losses for third straight session; what should investors do? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/patanjali-foods-share-price-crashes-20-extends-its-losses-for-third-session-what-should-investors-do-11784098857317.html
- Historical analogues: 2025-01-27 (d=0.01), 2026-07-06 (d=0.02), 2026-05-28 (d=0.05)

### [AMBER 5.32] rates · 4 series ↑
- ust_30y [RATES]: last 5.08, z20 1.66, zc -0.54, resid-z -0.46 [quiet], 1d -0.39%, |z20|=1.66; 1y-pct=97
- ust_10y [RATES]: last 4.58, z20 1.57, zc -0.87, resid-z -0.69 [quiet], 1d -0.87%, |z20|=1.57; 1y-pct=98
- tips_10y_real [RATES]: last 2.33, z20 1.47, zc -0.71, resid-z -0.63 [quiet], 1d -1.27%, 1y-pct=99
- ust_2y [RATES]: last 4.18, z20 0.53, zc -1.45, resid-z -1.28 [quiet], 1d -1.88%, 1y-pct=97
- **Mechanism**: The recent surge in oil prices, driven by tensions in the U.S.-Iran relationship, has led to a rise in Euro zone bond yields, which in turn has caused Indian government bond yields to increase. This is reflected in the 10-year bond yield hitting a three-week high. The mechanism of transmission is through the metal_copper_channel and the vix_equity_inverse, which are both valid channels.
- **Gap**: No gap: The move in Indian bond yields is largely priced in, given the global rate hikes and deficient monsoon, as well as the recent spike in oil prices.
- **India take**: The Indian 10-year bond yield is expected to trade in the 6.60-6.90% range over the next month, according to PGIM India's Puneet Pal. The recent surge in oil prices has already led to a weakening of the rupee and a decline in stock values in Mumbai.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment due to oil price spike
- Source: 10-year bond yield may trade in 6.60-6.90% range over the next month: PGIM India MF's Puneet Pal — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/10-year-bond-yield-may-trade-in-6-60-6-90-range-over-the-next-month-pgim-india-mfs-puneet-pal/articleshow/132409495.cms
- Source: Euro zone bond yields tick higher along with oil prices after big swings — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-along-with-oil-prices-after-big-swings/articleshow/132409354.cms
- Source: Oil spike jolts Indian bonds, 10-year yield hits three-week high — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/oil-spike-jolts-indian-bonds-10-year-yield-hits-three-week-high/articleshow/132391105.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [AMBER 4.8] commodities · 2 series ↑
- brent [COMMODITIES]: last 84.60, z20 1.97, zc -0.19, resid-z 0.44 [quiet], 1d -0.41%, |z20|=1.97; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 79.46, z20 1.89, zc -0.08, resid-z 0.42 [quiet], 1d -0.18%, |z20|=1.89
- **Mechanism**: The recent decline in oil prices, despite escalating Middle East tensions, is likely due to the easing of supply chain disruptions and the return of foreign investors to the Indian market. This has led to a decrease in earnings risks for Indian companies, causing a neutral outlook for Indian equities. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may lead to rotations in the market.
- **Gap**: No gap: the move in brent and wti is priced, with small resid_z values of 0.44 and 0.42 respectively, indicating that the current price reflects the factor exposures.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the wti price movement. The easing of oil prices may lead to a decrease in import costs and government finances, potentially benefiting Indian equities.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to wti price movement
- **India receivers**: nifty_midcap_100 (rho -0.523, z 1.51)
- Source: Asian shares mostly decline with South Korea’s Kospi down 6.6%, while oil prices slip — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/asian-shares-mostly-decline-with-south-koreas-kospi-down-66-while-oil-prices-slip/article71228684.ece
- Source: HSBC upgrades Indian equities to 'neutral' on easing oil prices, return of foreign flows — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/hsbc-upgrades-indian-equities-to-neutral-on-easing-oil-prices-return-of-foreign-flows/articleshow/132430487.cms
- Source: Oil is crude once again! Is $95 the new normal and what it means for Indian investors? — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/commodities/news/oil-is-crude-once-again-is-95-the-new-normal-and-what-it-means-for-indian-investors/articleshow/132430022.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.76] dyn_biocon_bo ↑
- dyn_biocon_bo [EQUITIES]: last 443.20, z20 2.76, zc 0.66, resid-z -0.46 [quiet], 1d 1.97%, |z20|=2.76; 1y-pct=100
- **Mechanism**: The recent sale of Mylan's 5.64% stake in Biocon for ₹3,679 crore has led to a surge in Biocon's shares, indicating strong institutional demand. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The surge in Biocon's shares may also be influenced by the VALID gold_silver_comove channel, as the pharmaceutical company's performance can be linked to the broader market trends.
- **Gap**: No gap: the big raw move in Biocon's shares is accompanied by a relatively small resid_z, indicating that the move is largely priced in.
- **India take**: The Indian instrument that expresses this move is dyn_justdial_bo, which has already reacted to the surge in Biocon's shares. The strong institutional demand for Biocon's shares may also have a positive impact on the broader Indian market, particularly the pharmaceutical sector.
- Watch next: dyn_justdial_bo (up) — already moved; rho=0.506 via dyn_biocon_bo
- **India receivers**: dyn_justdial_bo (rho 0.446, z 2.52); nifty_metal (rho 0.353, z -0.44)
- Source: Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/stock-markets/mylan-exits-biocon-sells-entire-564-stake-for-3679-crore-via-block-deals/article71222744.ece
- Source: Rs 1,839 crore Biocon block deal: ICICI Pru MF biggest buyer along with Citi and Goldman Sachs — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/rs-1839-crore-biocon-block-deal-icici-pru-mf-biggest-buyer-along-with-citi-and-goldman-sachs/articleshow/132393595.cms
- Source: Biocon among 4 midcap stocks that hit 52-week highs and rallied up to 21% in a month — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/biocon-among-4-midcap-stocks-that-hit-52-week-highs-and-rallied-up-to-21-in-a-month/slideshow/132389833.cms
- Historical analogues: 2025-12-26 (d=0.01), 2024-11-13 (d=0.04), 2025-07-31 (d=0.08)

### [RED 4.72] dyn_nuvoco_ns ↑
- dyn_nuvoco_ns [EQUITIES]: last 360.50, z20 2.72, zc -0.72, resid-z 4.07 [unexplained], 1d -4.44%, |z20|=2.72
- **Mechanism**: dyn_nuvoco_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-12 (z-distance 0.03).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.522 via dyn_nuvoco_ns, z 2.52, reacted); nifty_midcap_100 (rho 0.432 via dyn_nuvoco_ns, z 1.51, reacted); dyn_pcjeweller_ns (rho 0.396 via dyn_nuvoco_ns, z 1.75, reacted); midcap_largecap_ratio (rho 0.361 via dyn_nuvoco_ns, z 1.25, reacted)
- **India receivers**: dyn_justdial_bo (rho 0.522, z 2.52); nifty_midcap_100 (rho 0.432, z 1.51); dyn_pcjeweller_ns (rho 0.396, z 1.75); midcap_largecap_ratio (rho 0.361, z 1.25)
- Source: Broker’s Call: Nuvoco Vistas (Accumulate) — BusinessLine Mkts, 2026-07-15. https://www.thehindubusinessline.com/markets/brokers-call-nuvoco-vistas-accumulate/article71224959.ece
- Source: Nuvoco Vistas share price rallies 12% on strong Q1 results FY27. Should you buy or sell? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/nuvoco-vistas-share-price-rallies-12-on-strong-q1-results-fy27-should-you-buy-or-sell-11784091753229.html
- Source: Nuvoco Vistas shares soar 10% after strong Q1. Why Nomura, Choice see up to 47% upside? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/nuvoco-vistas-shares-soar-10-after-strong-q1-why-nomura-choice-see-up-to-47-upside/articleshow/132406082.cms
- Historical analogues: 2025-08-12 (d=0.03), 2025-08-05 (d=0.05), 2025-07-29 (d=0.05)

## Watchlist (below surfacing floor)
dyn_bac ↑ (4.66), indices · 2 series ↓ (4.65), dyn_blk ↑ (4.49), midcap_largecap_ratio ↑ (4.25), shanghai_comp ↓ (4.24), gold_silver_ratio ↑ (4.13), usd_inr ↑ (3.89), natgas ↓ (3.89), dyn_atherenerg_ns ↑ (3.7), comex_copper ↑ (3.64), dyn_cupid_ns ↑ (3.49), corn ↑ (3.46)

## India macro
- nifty_50: 24145.6504 (1d 0.28%, z20 0.36, flag none)
- nifty_midcap_100: 62990.6016 (1d -0.02%, z20 1.51, flag amber)
- usd_inr: 96.3200 (1d -0.11%, z20 1.89, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6088 (1d -0.30%, z20 1.25, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 60.0 — "First gold, now global stocks: have Indian investors forgotten the risks?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 58.9 — "First gold, now global stocks: have Indian investors forgotten the risks?"
- HDB (HDFC Bank Limited) score 51.6 — "HDFC Life Share Price Live Updates: HDFC Life Stock Details"
- COIN (Coinbase Global, Inc.) score 44.2 — "As Ukraine Cripples Russian Refining, Global Diesel Markets Pay the Price"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.0 — "Motilal Oswal picks 9 bank stocks with up to 36% upside potential ahead of Q1 results. Do "
- BOND (PIMCO Active Bond Exchange-Tra) score 23.7 — "Tata Capital raises $400 million in dollar bond sale after strong demand"
- BAC (Bank of America Corporation) score 23.5 — "Motilal Oswal picks 9 bank stocks with up to 36% upside potential ahead of Q1 results. Do "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 23.4 — "SpaceX stock drops below IPO price, putting focus on upcoming tech IPOs"
- CHKP (Check Point Software Technolog) score 18.8 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 1"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.7 — "Stocks to watch: Wipro, Jio Financial, Ather Energy among shares in focus today; check lis"
- VT (Vanguard Total World Stock Ind) score 16.0 — "Argentina beat England 2-1 to reach World Cup final . They will play Spain in final"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.5 — "Your Netflix bill is up 29% in just over a year. It’s time for Washington to step in."
- SKHYV (SK hynix Inc. American Deposit) score 11.5 — "Why the huge premium on SK Hynix’s U.S.-listed shares may prove short-lived"
- IDBI.NS (IDBI BANK LIMITED) score 10.4 — "Motilal Oswal picks 9 bank stocks with up to 36% upside potential ahead of Q1 results. Do "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Steel Share Price Live Updates: Tata Steel's Price and Returns Overview"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.4 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ shows slight price increase"
- MS (Morgan Stanley) score 6.1 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.9 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- META (Meta) score 5.6 — "Global Market: China Q2 growth slows to 4.3% yoy; Asia, metals stocks likely to remain vol"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 5.4 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- GS (Goldman Sachs Group, Inc. (The) score 5.2 — "Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $11"
- SWIGGY.NS (SWIGGY LIMITED) score 4.9 — "Stocks to buy for short term: Swiggy among 3 shares Amol Athawale of Kotak Securities reco"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.5 — "PL Capital raises Nifty target to 27,019; favours banks, NBFCs, capital goods and defence"
- PYPL (PayPal Holdings, Inc.) score 3.5 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BLK (BlackRock, Inc.) score 3.5 — "BlackRock assets hit record $15 trillion on boost from buoyant markets, ETF inflows"
- BIOCON.BO (BIOCON LTD.) score 3.3 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.2 — "AI Boom Sends U.S. Electricity Demand to New High"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 3.0 — "HDB Financial shares jump 5% on Q1 profit cheer. What are Nomura, Motilal Oswal saying?"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.9 — "ICICI Lombard shares slump 15% to 52-week low after weak Q1 results trigger brokerage down"
- NUVOCO.NS (NUVOCO VISTAS CORP LTD) score 2.5 — "Broker’s Call: Nuvoco Vistas (Accumulate)"
- IS0LD.XD (iShares Germany Govt Bond UCIT) score 2.5 — "Govt bonds extend recovery tracking rise in US treasuries"
- MU (Micron Technology, Inc.) score 2.3 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- TEO (Telecom Argentina SA) score 2.3 — "Argentina beat England 2-1 to reach World Cup final . They will play Spain in final"
- LGDS (JPMorgan Fundamental Data Scie) score 2.3 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- CUPID.NS (CUPID LIMITED) score 2.3 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- JIOFIN.BO (Jio Financial Services Limited) score 2.0 — "Jio Financial Services Share Price Live Updates: Jio Financial Services' stock price slips"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 1.9 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.7 — "Ather Energy shares rally 6% after Hero MotoCorp approves Rs 1,000 crore additional invest"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.7 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"
- JEF (Jefferies Financial Group Inc.) score 1.5 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"

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