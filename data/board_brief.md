# Transmission Layer — board brief · 2026-07-16 21:49Z

data as of **2026-07-16** · 98 series · 12 red / 38 amber · 8 events surfaced (38 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.395, 8d in regime; vol-pct 0.554, breadth-off 0.235, Markov P(high-vol) 0.023)
- [INVERTED] **safe_haven_gold** — corr20 -0.17, corr60 -0.45, contra nifty_50 corr20=0.37, last shift 2026-05-29. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.83, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.46, corr60 0.36, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.01, last shift 2026-05-27. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.79, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 -0.06, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.22, corr60 -0.28, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.34, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 88** scanned series survive multiplicity control (effective p ≤ 0.00024255046857080131)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.508, β 0.2123, p 0.0); driver zc -2.4 → expected -0.946%. Type hit-rate 0.82 (n=2776).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.268, β 0.0866, p 0.00336); driver zc -2.4 → expected -0.386%. Type hit-rate 0.82 (n=2776).
- **SETUP** dyn_ms → usd_mxn: leads 1d (ccf -0.26, β -0.0917, p 0.00039); driver zc -2.4 → expected 0.408%. Type hit-rate 0.82 (n=2776).
- Track record · residual_reversion: hit-rate **0.491** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2776) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.52] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 71.37, z20 1.69, zc n/a, resid-z n/a [quiet], 1d 0.79%, GSR<75 (extreme low); |z20|=1.69
- comex_silver [COMMODITIES]: last 55.76, z20 -1.53, zc -0.80, resid-z 0.27 [quiet], 1d -2.36%, |z20|=1.53
- **Mechanism**: The recent increase in the gold-silver ratio, coupled with the decline in Comex silver prices, may propagate through the VALID gold_silver_comove channel, indicating a potential rotation between gold and silver. However, the current move in gold_silver_ratio is priced, given its relatively small resid_z and the fact that the ratio is still below its historical average. The decline in Comex silver prices may be attributed to the escalating Middle East tensions and the resulting expectations of higher interest rates.
- **Gap**: No gap: The current move in gold_silver_ratio is priced, and Comex silver prices have already declined in response to the escalating Middle East tensions.
- **India take**: The Indian instruments that express this move are MCX gold and silver futures, which have already reacted to the global trends, with MCX gold August futures down 0.39% and MCX silver September futures down 0.44%.
- Watch next: comex_copper (down) — not yet - watch; Negative correlation with gold_silver_ratio
- Source: Gold, silver prices today: Comex gold and silver extend losses as Middle East tensions fuel rate hike fears — Mint Markets, 2026-07-16. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-and-silver-extend-losses-as-middle-east-tensions-lift-rate-hike-fears-11784218381820.html
- Source: Gold and silver prices drop on MCX as escalating Middle East conflict strengthens US Fed rate hike expectations — Mint Markets, 2026-07-16. https://www.livemint.com/market/commodities/gold-and-silver-price-today-rate-drops-on-mcx-as-middle-east-conflict-strengthens-us-fed-rate-hike-expectations-11784172681844.html
- Source: Gold-Silver ratio rises to 69: Here's what it means for investors. Is it time to buy gold or silver? — Mint Markets, 2026-07-15. https://www.livemint.com/market/commodities/goldsilver-ratio-rises-to-69-heres-what-it-means-for-investors-is-it-time-to-buy-gold-or-silver-11784101247199.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.38] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1623.10, z20 -5.38, zc -7.44, resid-z -7.99 [unexplained], 1d -10.52%, |z20|=5.38; 1y-pct=0
- **Mechanism**: The decline in ICICI Lombard's stock price is attributed to its weak Q1 results, which triggered brokerage downgrades. This event is likely to propagate through the metal_copper_channel and vix_equity_inverse channels, as the market reacts to the earnings disappointment. However, the primary driver of the move is the company-specific news, rather than a broader market or macroeconomic factor.
- **Gap**: No gap: the big raw move in ICICI Lombard's stock price is largely explained by the weak Q1 results and subsequent brokerage downgrades, leaving a relatively small resid_z of -7.97, indicating that the move is mostly priced in.
- **India take**: The Indian instruments that express this move are the Nifty Midcap 100 and Dyn Nuvoco NS, with the latter having already reacted to the news. The Nifty Midcap 100 is still quiet and worth watching for potential follow-through.
- Watch next: nifty_midcap_100 (down) — not yet - watch; rho=0.418 via dyn_icicigi_bo
- Watch next: dyn_nuvoco_ns (down) — already moved; rho=0.398 via dyn_icicigi_bo
- **India receivers**: nifty_midcap_100 (rho 0.418, z 0.95); dyn_nuvoco_ns (rho 0.398, z 2.56); dyn_indianb_ns (rho 0.371, z -0.25); dyn_adanient_bo (rho 0.352, z 0.77)
- Source: Market wrap: ICICI Lombard, IndiGo among top gainers & losers on Nifty and Sensex today — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-icici-lombard-indigo-among-top-gainers-losers-on-nifty-and-sensex-today/articleshow/132439120.cms
- Source: ICICI Lombard shares slump after weak Q1 results trigger brokerage downgrades — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/icici-lombard-shares-slump-15-to-52-week-low-after-weak-q1-results-trigger-brokerage-downgrades/article71228507.ece
- Source: Why standalone health insurers may outshine ICICI Lombard after Q1 — Mint Markets, 2026-07-16. https://www.livemint.com/market/mark-to-market/icici-lombard-star-health-standalone-health-insurers-sahi-health-insurance-general-insurance-q1fy27-11784186386060.html
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [RED 6.41] dyn_patanjali_ns ↓
- dyn_patanjali_ns [EQUITIES]: last 345.00, z20 -4.41, zc -0.18, resid-z -0.15 [quiet], 1d -0.83%, |z20|=4.41; 1y-pct=0
- **Mechanism**: The decline in Patanjali Foods share price is driven by heavy selling, with no material developments reported by the company. The sharp fall is likely a result of technical factors, with the next key support seen in the Rs 325-330 zone. The move is largely priced, given the small resid_z value of -0.14, indicating that the decline is largely explained by factor exposures.
- **Gap**: No gap: the decline in Patanjali Foods share price is largely explained by factor exposures, with a small resid_z value of -0.14, indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a z20 value of -1.46. The decline in Patanjali Foods share price may have a limited impact on the broader Indian market, given the company's specific issues.
- Watch next: dyn_tataelxsi_ns (down) — already moved; rho=0.433 with dyn_patanjali_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.433, z -1.46)
- Source: Patanjali Foods shares crash 20%, stock nearly halves in value in one year. What's ahead? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/patanjali-foods-shares-crash-20-stock-nearly-halves-in-value-in-one-year-whats-ahead/articleshow/132410105.cms
- Source: Patanjali Foods share price crashes 20%, extending losses for third straight session; what should investors do? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/patanjali-foods-share-price-crashes-20-extends-its-losses-for-third-session-what-should-investors-do-11784098857317.html
- Historical analogues: 2025-01-27 (d=0.01), 2026-07-06 (d=0.02), 2026-05-28 (d=0.05)

### [RED 6.0] dyn_pypl ↑
- dyn_pypl [EQUITIES]: last 56.74, z20 4.00, zc 0.85, resid-z 7.78 [unexplained], 1d 2.21%, |z20|=4.00
- **Mechanism**: The surge in PayPal shares following a $53 billion buyout offer from Stripe and Advent International has triggered a rally in the US markets, with the S&P 500 and Dow Jones Industrial Average rising. This move is likely to propagate through the vix_equity_inverse channel, which is currently valid, leading to a potential decline in volatility and further gains in equity markets. However, the move in dyn_pypl is priced, with a resid_z of -0.56, indicating that the unexplained component is relatively small.
- **Gap**: No gap: the move in dyn_pypl is priced, with a resid_z of -0.56, indicating that the unexplained component is relatively small
- **India take**: The Indian instrument nifty_it has reacted to the move in dyn_pypl, with a rho of 0.148, and is likely to continue its upward trend. Additionally, dyn_patanjali_ns has also reacted, with a rho of -0.629, indicating a potential decline in its value.
- Watch next: nifty_it (up) — reacted; rho=0.148 via dyn_pypl
- **India receivers**: dyn_patanjali_ns (rho -0.632, z -4.41); nifty_it (rho 0.145, z 1.43)
- Source: PayPal’s battered stock is getting a record boost from a report of buyout interest — MarketWatch Top, 2026-07-15. https://www.marketwatch.com/story/a-53-billion-lifeline-stripe-and-advent-reportedly-team-up-to-bid-for-battered-paypal-3bc6fcc2?mod=mw_rss_topstories
- Source: PayPal shares jump over 15% after Stripe, Advent make $53 billion buyout offer — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/paypal-shares-jump-over-15-after-stripe-advent-make-53-billion-buyout-offer/articleshow/132418333.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-04-16 (d=0.05)

### [AMBER 5.57] fx · 3 series ↑
- gbp_usd [FX]: last 1.35, z20 2.25, zc 1.42, resid-z 1.43 [quiet], 1d 0.61%, |z20|=2.25
- usd_brl [FX]: last 5.10, z20 -1.84, zc 0.32, resid-z 0.46 [quiet], 1d 0.28%, |z20|=1.84
- aud_usd [FX]: last 0.70, z20 1.52, zc 0.49, resid-z 0.54 [quiet], 1d 0.35%, |z20|=1.52
- **Mechanism**: The recent move in FX markets, particularly in gbp_usd, usd_brl, and aud_usd, is largely priced in, with resid_z values indicating that the moves are mostly explained by factor exposures. The correlated instruments that have not moved, such as eur_usd and usd_mxn, may be due for a move based on their historical correlations. The verified transmission setups, such as dyn_ms -> aud_usd, also suggest potential lead-lag relationships that could drive future price action.
- **Gap**: No gap: the recent FX moves are largely priced in, with resid_z values close to zero, indicating that the market has already adjusted to the new information.
- **India take**: The Indian instrument eur_inr has already reacted to the FX move, while nifty_midcap_100 remains quiet. The metal_copper_channel, which is a valid channel, may also influence Indian metal equities.
- Watch next: eur_usd (up) — not yet - watch; historical correlation with gbp_usd
- **India receivers**: eur_inr (rho 0.369, z 2.0); nifty_midcap_100 (rho 0.351, z 0.95)
- Source: Sterling & Wilson Renewable Energy stock tumbles 7% despite record order book of ₹13,000 crore — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/stock-markets/sterling-wilson-renewable-energy-stock-tumbles-7-despite-record-order-book-of-13000-crore/article71229166.ece
- Historical analogues: 2025-08-25 (d=0.25), 2025-05-30 (d=0.46), 2025-05-21 (d=0.48)

### [RED 5.09] dyn_bhel_ns ↑
- dyn_bhel_ns [EQUITIES]: last 440.00, z20 3.09, zc 2.12, resid-z 2.07 [unexplained], 1d 5.28%, |z20|=3.09; 1y-pct=100
- **Mechanism**: The recent surge in BHEL's stock price can be attributed to its strong Q1 results, with a net profit of ₹377 crore and a 40% revenue growth, which has led to a positive sentiment among investors. This move is not entirely priced, as the resid_z of 2.02 indicates that there are still unexplained factors at play. The metal_copper_channel, which is a valid channel, may also be contributing to the move, as copper prices can impact Indian metal equities.
- **Gap**: No gap: The move in BHEL's stock price is largely explained by its strong Q1 results and the positive sentiment among investors, with a resid_z of 2.02 indicating some unexplained factors, but not a significant gap.
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has not yet reacted. The midcap_largecap_ratio has reacted, but other transmission candidates such as dyn_jiofin_bo and nifty_metal are quiet.
- Watch next: nifty_midcap_100 (up) — not yet - watch; Correlated instrument with rho=0.544
- **India receivers**: nifty_midcap_100 (rho 0.544, z 0.95); midcap_largecap_ratio (rho 0.473, z 1.04); dyn_jiofin_bo (rho 0.382, z -0.99); nifty_metal (rho 0.376, z -0.76)
- Source: Q1 Results Today Highlights: Wipro Q1 con. PAT flat, Tech Mahindra profit rises, BHEL posts ₹382 cr profit; Polycab, ITC Hotels, Jio Financial profit up, CEAT profit falls — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-wipro-jio-financial-tech-mahindra-polycab-india-bhel-piramal-finance-itc-hotels-ceat-wework-hdbfs-groww-icici-pru-hdfc-results-16-july-2026/article71225300.ece
- Source: BHEL among 6 midcap stocks that hit 52-week highs and rallied up to 20% in a month — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/bhel-among-6-midcap-stocks-that-hit-52-week-highs-and-rallied-up-to-20-in-a-month/slideshow/132439796.cms
- Source: BHEL shares jump 4% after Maharatna PSU posts net profit of Rs 377 crore in Q1, revenue jumps 40% — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/bhel-shares-jump-4-after-maharatna-psu-posts-net-profit-of-rs-377-crore-in-q1-revenue-jumps-40/articleshow/132438300.cms
- Historical analogues: 2025-12-29 (d=0.0), 2026-06-03 (d=0.01), 2025-02-10 (d=0.02)

### [RED 5.06] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.23, z20 -3.06, zc -1.22, resid-z -0.78 [quiet], 1d -7.88%, |z20|=3.06
- **Mechanism**: The recent decline in dyn_qessf is a priced move with a small resid_z of 1.08, indicating that the factor exposures have largely explained the move. The metal_copper_channel is valid, which could potentially transmit the move to Indian metal equities. However, the absence of a strong channel linking dyn_qessf to Indian markets limits the propagation of this move.
- **Gap**: No gap: the move in dyn_qessf is largely explained by its factor exposures, with a small resid_z of 1.08, indicating no significant anomaly.
- **India take**: The Indian instrument that could express this move is the Nifty Metal index, which may react to the decline in dyn_qessf through the metal_copper_channel, although the transmission is not yet evident. The Nifty 50, as mentioned in the PL Capital report, has a raised target, which may limit the downside potential.
- Watch next: nifty_metal (down) — not yet - watch; potential transmission through metal_copper_channel
- Source: PL Capital raises Nifty target to 27,019; favours banks, NBFCs, capital goods and defence — BusinessLine Mkts, 2026-07-15. https://www.thehindubusinessline.com/markets/pl-capital-raises-nifty-target-to-27019-favours-banks-nbfcs-capital-goods-and-defence/article71224935.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [AMBER 4.9] cross-asset · 2 series ↓
- dyn_mu [EQUITIES]: last 853.66, z20 -2.06, zc -0.94, resid-z -1.64 [unexplained], 1d -5.60%, |z20|=2.06
- nasdaq_100 [INDICES]: last 29035.01, z20 -1.58, zc -1.19, resid-z -1.18 [quiet], 1d -1.58%, |z20|=1.58
- **Mechanism**: The recent decline in US stocks, particularly in the Nasdaq 100, is driven by chipmaker weakness, which is offsetting gains in other sectors. This move is not fully explained by factor exposures, as indicated by the resid_z values of -1.64 and -1.18 for dyn_mu and nasdaq_100, respectively. The valid vix_equity_inverse channel suggests that the vol spike may lead to further equity drawdown.
- **Gap**: No gap: the move in dyn_mu and nasdaq_100 is largely priced, given the small resid_z values and the presence of a valid vix_equity_inverse channel
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react to the decline in US stocks through the metal_copper_channel. However, the reaction has not occurred yet, as the inr_oil_channel and dxy_inr_channel are weak.
- Watch next: dyn_vt (down) — not yet - watch; historically leads by 4d
- Watch next: sp500 (down) — not yet - watch; historically leads by 3d
- Source: US stocks today: Nasdaq ends lower as chip weakness offsets solid earnings, economic data — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-stocks-end-lower-as-chip-weakness-offsets-solid-earnings-economic-data/articleshow/132447866.cms
- Source: US stocks today: S&P 500, Nasdaq fall as chip stocks weaken; earnings and data in focus — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-sp-500-nasdaq-open-lower-as-chip-stocks-weaken/articleshow/132440760.cms
- Source: US Data Watch: 13 Nasdaq 100 stocks deliver multibaggers return in CY26 — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/us-data-watch-13-nasdaq-100-stocks-deliver-multibaggers-return-in-cy26/slideshow/132440115.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-08 (d=0.07), 2026-05-15 (d=0.13)

## Watchlist (below surfacing floor)
commodities · 2 series ↑ (4.86), shanghai_comp ↓ (4.56), dyn_nuvoco_ns ↑ (4.56), indices · 2 series ↓ (4.53), dyn_bac ↑ (4.2), midcap_largecap_ratio ↑ (4.04), dyn_blk ↑ (4.02), natgas ↓ (3.95), usd_inr ↑ (3.92), commodities · 2 series ↑ (3.89), dyn_atherenerg_ns ↑ (3.62), dyn_tataelxsi_ns ↓ (3.46)

## India macro
- nifty_50: 24081.0996 (1d 0.01%, z20 -0.04, flag none)
- nifty_midcap_100: 62731.4492 (1d -0.43%, z20 0.95, flag amber)
- usd_inr: 96.3350 (1d -0.09%, z20 1.92, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6050 (1d -0.44%, z20 1.04, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 66.4 — "India Is Becoming the World's Refining Swing Producer"
- INDIANB.NS (INDIAN BANK) score 59.1 — "Agencies issue joint statement on handling of highly sensitive information during bank exa"
- HDB (HDFC Bank Limited) score 51.8 — "Agencies issue joint statement on handling of highly sensitive information during bank exa"
- COIN (Coinbase Global, Inc.) score 47.3 — "IRAN THREATENS SECOND GLOBAL ENERGY CHOKEPOINT Iran has reportedly told Yemen’s Houthis to"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.4 — "Agencies issue joint statement on handling of highly sensitive information during bank exa"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.6 — "Wipro, Tech Mahindra Q1 Results 2026: Revenue, PAT, guidance, deal wins and key takeaways"
- BAC (Bank of America Corporation) score 29.6 — "Agencies issue joint statement on handling of highly sensitive information during bank exa"
- CHKP (Check Point Software Technolog) score 23.5 — "Wipro declares interim dividend worth Rs 2/share, fixes record date. Check details"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.2 — "Indian bonds rise on steady oil, easing US rate-hike fears"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.9 — "IRAN THREATENS SECOND GLOBAL ENERGY CHOKEPOINT Iran has reportedly told Yemen’s Houthis to"
- VT (Vanguard Total World Stock Ind) score 18.5 — "India Is Becoming the World's Refining Swing Producer"
- IDBI.NS (IDBI BANK LIMITED) score 15.5 — "Agencies issue joint statement on handling of highly sensitive information during bank exa"
- SKHYV (SK hynix Inc. American Deposit) score 11.8 — "NEW 2X SK HYNIX ETF DEBUTS Leverage Shares launched $SKHX on Tuesday, a 2x leveraged ETF t"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.7 — "IEA Warns World Has Just Weeks to Avoid Hormuz Economic Shock"
- JIOFIN.BO (Jio Financial Services Limited) score 9.1 — "Jio Financial Q1 Results: Profit skyrockets 155% YoY to Rs 830 crore"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.1 — "Jio Financial Q1 Results: Profit skyrockets 155% YoY to Rs 830 crore"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.2 — "Tata Steel Share Price Live Updates: Tata Steel's Price and Returns Overview"
- META (Meta) score 6.7 — "Is SpaceX’s stock a bust because it fell below $135? Look what happened after Meta’s IPO."
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.4 — "MSCI India August Review: Groww, Adani Green, Adani Energy among likely additions; Astral,"
- WIT (Wipro Limited) score 6.4 — "Wipro, Tech Mahindra Q1 Results 2026: Revenue, PAT, guidance, deal wins and key takeaways"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.2 — "ICICI Lombard shares slump after weak Q1 results trigger brokerage downgrades"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.0 — "​PC Jeweller share price declines 3% despite the firm announcing achieving a debt-free sta"
- MS (Morgan Stanley) score 5.3 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.8 — "KUWAIT AIRE DEFENCES RESPONDING TO 'HOSTILE DRONE THREATS' - KUWAITI ARMY"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 4.7 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- BHEL.NS (BHEL) score 4.7 — "BHEL shares jump 4% after Maharatna PSU posts net profit of Rs 377 crore in Q1, revenue ju"
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $11"
- SWIGGY.NS (SWIGGY LIMITED) score 4.2 — "Stocks to buy for short term: Swiggy among 3 shares Amol Athawale of Kotak Securities reco"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.7 — "AI trade moves from chips to electricity: Why 7 power stocks are gaining Wall Street atten"
- PYPL (PayPal Holdings, Inc.) score 3.0 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BLK (BlackRock, Inc.) score 3.0 — "BlackRock assets hit record $15 trillion on boost from buoyant markets, ETF inflows"
- BIOCON.BO (BIOCON LTD.) score 2.9 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- 453950.KS (TIGER TSMC Foundry Value Chain) score 2.7 — "TSMC posts 77% profit jump for Q2, surging past market expectations"
- NUVOCO.NS (NUVOCO VISTAS CORP LTD) score 2.2 — "Broker’s Call: Nuvoco Vistas (Accumulate)"
- IS0LD.XD (iShares Germany Govt Bond UCIT) score 2.2 — "Govt bonds extend recovery tracking rise in US treasuries"
- MU (Micron Technology, Inc.) score 2.0 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- NFLX (Netflix, Inc.) score 2.0 — "Netflix earnings in focus as shares gain slightly amid growth concerns"
- TEO (Telecom Argentina SA) score 2.0 — "Argentina beat England 2-1 to reach World Cup final . They will play Spain in final"
- CUPID.NS (CUPID LIMITED) score 1.9 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.4 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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