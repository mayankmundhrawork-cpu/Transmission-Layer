# Transmission Layer — board brief · 2026-07-16 11:16Z

data as of **2026-07-16** · 98 series · 16 red / 35 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.402, 8d in regime; vol-pct 0.554, breadth-off 0.25, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.12, corr60 -0.44, contra nifty_50 corr20=0.37, last shift 2026-05-29. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.82, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.45, corr60 0.36, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.01, last shift 2026-05-27. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.79, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.04, corr60 -0.05, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.28, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.34, corr60 0.23, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 87** scanned series survive multiplicity control (effective p ≤ 0.0002834212197515562)
- **SETUP** dyn_blk → asx_200: leads 1d (ccf 0.5, β 0.2404, p 0.0); driver zc 3.88 → expected 1.561%. Type hit-rate 0.818 (n=2407).
- **SETUP** dyn_blk → taiwan_weighted: leads 1d (ccf 0.371, β 0.3551, p 0.0); driver zc 3.88 → expected 2.306%. Type hit-rate 0.818 (n=2407).
- **SETUP** dyn_blk → aud_usd: leads 1d (ccf 0.342, β 0.1274, p 1e-05); driver zc 3.88 → expected 0.828%. Type hit-rate 0.818 (n=2407).
- **SETUP** dyn_blk → usd_mxn: leads 1d (ccf -0.326, β -0.1327, p 0.0); driver zc 3.88 → expected -0.861%. Type hit-rate 0.818 (n=2407).
- **SETUP** dyn_pypl → nifty_it: leads 1d (ccf 0.286, β 0.1637, p 0.0); driver zc 7.0 → expected 2.817%. Type hit-rate 0.818 (n=2407).
- Track record · residual_reversion: hit-rate **0.493** (n=1145) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2407) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.57] dyn_pypl ↑
- dyn_pypl [EQUITIES]: last 55.52, z20 6.57, zc 7.00, resid-z -0.56 [moved], 1d 17.20%, |z20|=6.57
- **Mechanism**: The surge in PayPal shares following a reported $53 billion buyout offer from Stripe and Advent International has triggered a rally in the US markets, with the S&P 500 and Dow Jones Industrial Average rising. This move is likely to propagate through the VALID vix_equity_inverse channel, where a vol spike would typically lead to an equity drawdown, but in this case, the positive news has led to a rise in equities. The metal_copper_channel may also play a role, as global copper leads Indian metal equities, potentially influencing the Indian market.
- **Gap**: No gap: the big raw move in dyn_pypl has a relatively small resid_z of 0.99, indicating that the move is largely priced in and not an anomaly
- **India take**: The Indian instruments dyn_patanjali_ns and dyn_pcjeweller_ns have already reacted to the move in dyn_pypl, with dyn_patanjali_ns having a negative correlation and dyn_pcjeweller_ns having a positive correlation. The metal_copper_channel may also influence the Indian metal equities.
- Watch next: dyn_patanjali_ns (down) — already moved; rho=-0.615 via dyn_pypl
- Watch next: dyn_pcjeweller_ns (up) — already moved; rho=0.359 via dyn_pypl
- **India receivers**: dyn_patanjali_ns (rho -0.639, z -4.41); dyn_pcjeweller_ns (rho 0.364, z 1.59); dyn_nuvoco_ns (rho 0.357, z 2.56); nifty_it (rho 0.142, z 1.43)
- Source: PayPal’s battered stock is getting a record boost from a report of buyout interest — MarketWatch Top, 2026-07-15. https://www.marketwatch.com/story/a-53-billion-lifeline-stripe-and-advent-reportedly-team-up-to-bid-for-battered-paypal-3bc6fcc2?mod=mw_rss_topstories
- Source: PayPal shares jump over 15% after Stripe, Advent make $53 billion buyout offer — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/paypal-shares-jump-over-15-after-stripe-advent-make-53-billion-buyout-offer/articleshow/132418333.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-04-16 (d=0.05)

### [RED 7.38] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1623.10, z20 -5.38, zc -7.44, resid-z -7.95 [unexplained], 1d -10.52%, |z20|=5.38; 1y-pct=0
- **Mechanism**: The recent decline in ICICI Lombard's stock price can be attributed to its dismal Q1 results, which missed estimates and raised concerns over the company's near-term profitability outlook. The weak underwriting, higher claims, and regulatory headwinds have led to a sharp decline in the stock price. The metal_copper_channel and vix_equity_inverse channels are valid and may influence the propagation of this move. However, the inr_oil_channel and dxy_inr_channel are weak and may not play a significant role in this scenario.
- **Gap**: No gap: The big raw move in ICICI Lombard's stock price is largely priced in, given the significant decline in its stock price following the disappointing Q1 results. The resid_z of -7.95 indicates that the move is largely explained by the factors, leaving little room for a gap.
- **India take**: The Indian instrument that expresses this move is dyn_nuvoco_ns, which has already reacted with a z20 of 2.56. Other Indian transmission candidates such as nifty_midcap_100, dyn_indianb_ns, and dyn_adanient_bo are quiet, with z20 values of 0.95, -0.25, and 0.77, respectively.
- Watch next: nifty_midcap_100 (down) — quiet; rho=0.418 via dyn_icicigi_bo
- **India receivers**: nifty_midcap_100 (rho 0.418, z 0.95); dyn_nuvoco_ns (rho 0.398, z 2.56); dyn_indianb_ns (rho 0.371, z -0.25); dyn_adanient_bo (rho 0.352, z 0.77)
- Source: Why standalone health insurers may outshine ICICI Lombard after Q1 — Mint Markets, 2026-07-16. https://www.livemint.com/market/mark-to-market/icici-lombard-star-health-standalone-health-insurers-sahi-health-insurance-general-insurance-q1fy27-11784186386060.html
- Source: Q1 Results Today Live: Wipro, Jio Financial, Tech Mahindra, Polycab, BHEL, ITC Hotels, CEAT, WeWork India to announce Q1 results, Union Bank, Groww, HDBFS, HDFC AMC, HDFC Life, ICICI Pru Life, ICICI Lombard, Angel One shares in focus — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-wipro-jio-financial-tech-mahindra-polycab-india-bhel-piramal-finance-itc-hotels-ceat-wework-hdbfs-groww-icici-pru-hdfc-results-16-july-2026/article71225300.ece
- Source: Explained: Why ICICI Lombard shares tumbled 15% in their biggest fall since the COVID crash — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/explained-why-icici-lombard-shares-tumbled-15-in-their-biggest-fall-since-the-covid-crash/articleshow/132430960.cms
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [RED 6.41] dyn_patanjali_ns ↓
- dyn_patanjali_ns [EQUITIES]: last 345.00, z20 -4.41, zc -0.18, resid-z -0.14 [quiet], 1d -0.83%, |z20|=4.41; 1y-pct=0
- **Mechanism**: The decline in Patanjali Foods share price is driven by heavy selling, with no material developments reported by the company. The sharp fall is likely a result of technical factors, with the next key support seen in the Rs 325-330 zone. The move is largely priced, given the small resid_z value of -0.14, indicating that the decline is largely explained by factor exposures.
- **Gap**: No gap: the decline in Patanjali Foods share price is largely explained by factor exposures, with a small resid_z value of -0.14, indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a z20 value of -1.46. The decline in Patanjali Foods share price may have a limited impact on the broader Indian market, given the company's specific issues.
- Watch next: dyn_tataelxsi_ns (down) — already moved; rho=0.433 with dyn_patanjali_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.433, z -1.46)
- Source: Patanjali Foods shares crash 20%, stock nearly halves in value in one year. What's ahead? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/patanjali-foods-shares-crash-20-stock-nearly-halves-in-value-in-one-year-whats-ahead/articleshow/132410105.cms
- Source: Patanjali Foods share price crashes 20%, extending losses for third straight session; what should investors do? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/patanjali-foods-share-price-crashes-20-extends-its-losses-for-third-session-what-should-investors-do-11784098857317.html
- Historical analogues: 2025-01-27 (d=0.01), 2026-07-06 (d=0.02), 2026-05-28 (d=0.05)

### [RED 6.28] cross-asset · 4 series ↑
- dyn_gs [EQUITIES]: last 1152.26, z20 2.62, zc 0.22, resid-z 4.90 [unexplained], 1d 1.08%, |z20|=2.62; 1y-pct=100
- dyn_ms [EQUITIES]: last 228.51, z20 1.65, zc 0.19, resid-z 1.33 [quiet], 1d 0.37%, 1y-pct=100
- sp500 [INDICES]: last 7572.20, z20 1.42, zc 0.50, resid-z -0.75 [quiet], 1d 0.38%, 1y-pct=98
- dow_jones [INDICES]: last 52658.02, z20 1.00, zc 0.39, resid-z -0.34 [quiet], 1d 0.29%, 1y-pct=98
- **Mechanism**: The recent surge in US investment banking fees, driven by a rebound in IPOs, M&A deals, and corporate debt issuance, is positively impacting equity markets. This, combined with the potential for Apple to reach a $5 trillion market valuation, is contributing to the current upward trend in equities, as reflected in the z20 levels of dyn_gs and dyn_ms. The VALID vix_equity_inverse channel suggests that the current low vol environment supports further equity gains.
- **Gap**: No gap: the high z20 levels and low resid_z values for dyn_gs and dyn_ms indicate that the current price move is largely explained by factor exposures and is therefore priced in.
- **India take**: The Indian equities, such as Nifty 50, may react positively to the global equity trend, potentially driven by the VALID metal_copper_channel and the low vol environment. However, the reaction is yet to be observed.
- Watch next: dyn_gs (up) — already moved; high z20 level and low resid_z indicate priced move
- Watch next: dyn_ms (up) — already moved; high z20 level and low resid_z indicate priced move
- Source: US Stock Market: Wall Street investment banking revival gains momentum as IPOs, M&A fuel deal boom — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-wall-street-investment-banking-revival-gains-momentum-as-ipos-ma-fuel-deal-boom/articleshow/132433420.cms
- Source: Apple's $5 Trillion Dream: Why Wall Street is turning bullish again — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/apples-5-trillion-dream-why-wall-street-is-turning-bullish-again/slideshow/132433234.cms
- Source: Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $110/bbl, says Goldman Sachs — Mint Markets, 2026-07-16. https://www.livemint.com/market/commodities/crude-oil-prices-rise-for-4th-session-amid-escalating-us-iran-war-brent-likely-to-hit-110-bbl-says-goldman-sachs-11784163944139.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.32), 2024-11-11 (d=0.55)

### [RED 5.9] fx · 3 series ↑
- usd_brl [FX]: last 5.08, z20 -2.59, zc -0.27, resid-z -0.27 [quiet], 1d -0.23%, |z20|=2.59
- gbp_usd [FX]: last 1.35, z20 2.52, zc 1.81, resid-z 1.88 [unexplained], 1d 0.77%, |z20|=2.52
- aud_usd [FX]: last 0.70, z20 1.67, zc 0.62, resid-z 0.81 [quiet], 1d 0.44%, |z20|=1.67
- **Mechanism**: The recent move in FX markets, particularly the strengthening of GBP and AUD against the USD, is driven by unexplained factors as evidenced by the high resid_z values for gbp_usd and aud_usd. This move is not fully priced in and may propagate through the gold_silver_comove and metal_copper_channel, which are currently valid. However, the inr_oil_channel and dxy_inr_channel are weak, which may limit the transmission to Indian markets.
- **Gap**: No gap: the recent move in FX markets is largely unexplained but does not represent a significant deviation from historical norms, given the current regime and channel status.
- **India take**: The Indian instrument that expresses this move is eur_inr, which has already reacted with a rho of 0.374 via gbp_usd. The move may also be transmitted to Indian metal equities through the metal_copper_channel.
- Watch next: gbp_usd (up) — already moved; High resid_z value indicates unexplained move
- **India receivers**: eur_inr (rho 0.374, z 2.18)
- Source: Sterling & Wilson Renewable Energy stock tumbles 7% despite record order book of ₹13,000 crore — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/stock-markets/sterling-wilson-renewable-energy-stock-tumbles-7-despite-record-order-book-of-13000-crore/article71229166.ece
- Historical analogues: 2025-08-25 (d=0.25), 2025-05-30 (d=0.46), 2025-05-21 (d=0.48)

### [AMBER 5.32] rates · 4 series ↑
- ust_30y [RATES]: last 5.08, z20 1.66, zc -0.54, resid-z -0.46 [quiet], 1d -0.39%, |z20|=1.66; 1y-pct=97
- ust_10y [RATES]: last 4.58, z20 1.57, zc -0.87, resid-z -0.69 [quiet], 1d -0.87%, |z20|=1.57; 1y-pct=98
- tips_10y_real [RATES]: last 2.33, z20 1.47, zc -0.71, resid-z -0.63 [quiet], 1d -1.27%, 1y-pct=99
- ust_2y [RATES]: last 4.18, z20 0.53, zc -1.45, resid-z -1.28 [quiet], 1d -1.88%, 1y-pct=97
- **Mechanism**: The recent surge in oil prices has led to increased inflation expectations, causing bond yields to climb globally. This move is priced, as evidenced by the low resid_z values for the US Treasury yields, indicating that the factor exposures can explain the majority of the move.
- **Gap**: No gap: The move in bond yields is largely explained by the factor exposures, with low resid_z values indicating that the move is priced.
- **India take**: The Indian 10-year bond yield may trade in the 6.60-6.90% range over the next month, according to PGIM India MF's Puneet Pal, and may be influenced by global rate hikes and a deficient monsoon. The metal_copper_channel, which is a valid channel, may also impact Indian metal equities.
- Watch next: dyn_bond (down) — not yet - watch; Historically leads US Treasury yields by 1 day
- Source: Global Market: Japanese bond yields climb as oil surge and fiscal concerns weigh on market — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-climb-as-oil-surge-and-fiscal-concerns-weigh-on-market/articleshow/132431940.cms
- Source: 10-year bond yield may trade in 6.60-6.90% range over the next month: PGIM India MF's Puneet Pal — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/10-year-bond-yield-may-trade-in-6-60-6-90-range-over-the-next-month-pgim-india-mfs-puneet-pal/articleshow/132409495.cms
- Source: Euro zone bond yields tick higher along with oil prices after big swings — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-along-with-oil-prices-after-big-swings/articleshow/132409354.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [RED 5.09] dyn_bhel_ns ↑
- dyn_bhel_ns [EQUITIES]: last 440.00, z20 3.09, zc 2.12, resid-z 1.97 [unexplained], 1d 5.28%, |z20|=3.09; 1y-pct=100
- **Mechanism**: dyn_bhel_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-29 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.544 via dyn_bhel_ns, z 0.95, quiet); midcap_largecap_ratio (rho 0.473 via dyn_bhel_ns, z 1.04, reacted); dyn_jiofin_bo (rho 0.382 via dyn_bhel_ns, z -0.99, quiet); nifty_metal (rho 0.376 via dyn_bhel_ns, z -0.76, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.544 vs dyn_bhel_ns
- **India receivers**: nifty_midcap_100 (rho 0.544, z 0.95); midcap_largecap_ratio (rho 0.473, z 1.04); dyn_jiofin_bo (rho 0.382, z -0.99); nifty_metal (rho 0.376, z -0.76)
- Source: Q1 Results Today Live: Wipro con. PAT flat in Q1, Tech Mahindra con. profit rises, BHEL logs ₹382 cr profit, Jio Financial, CEAT, WeWork to announce Q1 results, Polycab India, ITC Hotels profit up — BusinessLine Mkts, 2026-07-16. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-wipro-jio-financial-tech-mahindra-polycab-india-bhel-piramal-finance-itc-hotels-ceat-wework-hdbfs-groww-icici-pru-hdfc-results-16-july-2026/article71225300.ece
- Source: BHEL Q1 results: BHEL swings to  ₹376.71 crore net profit in June quarter — Mint Markets, 2026-07-16. https://www.livemint.com/market/stock-market-news/bhel-q1-results-bhel-swings-to-376-71-crore-net-profit-in-june-quarter-11784194013221.html
- Source: Q1 results today: Jio Financial, Wipro, Polycab India, BHEL among 41 companies to report earnings — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/earnings/q1-results-today-jio-financial-wipro-polycab-india-bhel-among-41-companies-to-report-earnings/articleshow/132433544.cms
- Historical analogues: 2025-12-29 (d=0.0), 2026-06-03 (d=0.01), 2025-02-10 (d=0.02)

### [RED 4.93] commodities · 3 series ↑
- corn [COMMODITIES]: last 470.75, z20 3.61, zc 4.10, resid-z 1.97 [unexplained], 1d 5.20%, |z20|=3.61; 1y-pct=98
- wheat [COMMODITIES]: last 683.75, z20 3.36, zc 0.32, resid-z 3.63 [unexplained], 1d 0.92%, |z20|=3.36; 1y-pct=100
- soybeans [COMMODITIES]: last 1204.25, z20 1.44, zc 0.16, resid-z -0.82 [quiet], 1d 0.17%, 1y-pct=96
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_patanjali_ns (rho -0.466 via wheat, z -4.41, reacted)
- **India receivers**: dyn_patanjali_ns (rho -0.466, z -4.41)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

## Watchlist (below surfacing floor)
commodities · 2 series ↑ (4.81), dyn_bac ↑ (4.66), shanghai_comp ↓ (4.56), dyn_nuvoco_ns ↑ (4.56), gold_silver_ratio ↑ (4.54), indices · 2 series ↓ (4.53), dyn_biocon_bo ↑ (4.49), dyn_blk ↑ (4.49), midcap_largecap_ratio ↑ (4.04), usd_inr ↑ (3.92), natgas ↓ (3.81), dyn_atherenerg_ns ↑ (3.62)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 66.0 — "India bonds extend recovery tracking rise in U.S. Treasuries"
- INDIANB.NS (INDIAN BANK) score 61.1 — "The Rs 1.5 lakh crore bank guarantee link that could rattle NSE, BSE and MCX"
- HDB (HDFC Bank Limited) score 53.1 — "The Rs 1.5 lakh crore bank guarantee link that could rattle NSE, BSE and MCX"
- COIN (Coinbase Global, Inc.) score 48.1 — "Global Market:  China stocks slide as tech sell-off hits mainland markets; Alibaba lifts H"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.9 — "The Rs 1.5 lakh crore bank guarantee link that could rattle NSE, BSE and MCX"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.2 — "Wipro, Tech Mahindra Q1 Results 2026 LIVE: Revenue, PAT, guidance, deal wins and key takea"
- BAC (Bank of America Corporation) score 27.3 — "TRUMP: IRAN HAS ALLOWED AN AMERICAN CITIZEN, WHO WAS WRONGFULLY DETAINED IN DECEMBER OF 20"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.6 — "India bonds extend recovery tracking rise in U.S. Treasuries"
- CHKP (Check Point Software Technolog) score 23.9 — "Dolly Khanna Portfolio: Exits two stocks, trims stake in one in Q1FY27; check details"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.9 — "MSCI India August Review: Groww, Adani Green, Adani Energy among likely additions; Astral,"
- VT (Vanguard Total World Stock Ind) score 17.2 — "Alpine Texaworld IPO Day 3: Issue fully subscribed on last day. Check GMP, other details -"
- IDBI.NS (IDBI BANK LIMITED) score 13.9 — "The Rs 1.5 lakh crore bank guarantee link that could rattle NSE, BSE and MCX"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.0 — "IEA Warns World Has Just Weeks to Avoid Hormuz Economic Shock"
- SKHYV (SK hynix Inc. American Deposit) score 11.9 — "Turbo-charged SK Hynix volatility shows no sign of abating as AI euphoria swings to fatigu"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.1 — "Tata Steel Share Price Live Updates: Tata Steel's Price and Returns Overview"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.1 — "MSCI India August Review: Groww, Adani Green, Adani Energy among likely additions; Astral,"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.6 — "​PC Jeweller share price declines 3% despite the firm announcing achieving a debt-free sta"
- META (Meta) score 6.4 — "Metal stock Shyam Metalics hits a record high after this business update. Details here"
- JIOFIN.BO (Jio Financial Services Limited) score 5.9 — "From Dixon Tech to Cyient DLM- why are electronics manufacturing services stocks rising? E"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 5.9 — "Q1 results today: Jio Financial, Wipro, Polycab India, BHEL among 41 companies to report e"
- MS (Morgan Stanley) score 5.8 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.3 — "KUWAIT AIRE DEFENCES RESPONDING TO 'HOSTILE DRONE THREATS' - KUWAITI ARMY"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 5.2 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $11"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.7 — "Explained: Why ICICI Lombard shares tumbled 15% in their biggest fall since the COVID cras"
- SWIGGY.NS (SWIGGY LIMITED) score 4.7 — "Stocks to buy for short term: Swiggy among 3 shares Amol Athawale of Kotak Securities reco"
- WIT (Wipro Limited) score 3.9 — "Wipro Q1 results: Profit remains flat YoY at  ₹3,352 crore; declares interim dividend of  "
- PYPL (PayPal Holdings, Inc.) score 3.4 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BLK (BlackRock, Inc.) score 3.3 — "BlackRock assets hit record $15 trillion on boost from buoyant markets, ETF inflows"
- BIOCON.BO (BIOCON LTD.) score 3.2 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.1 — "AI Boom Sends U.S. Electricity Demand to New High"
- 453950.KS (TIGER TSMC Foundry Value Chain) score 3.0 — "TSMC posts 77% profit jump for Q2, surging past market expectations"
- NUVOCO.NS (NUVOCO VISTAS CORP LTD) score 2.4 — "Broker’s Call: Nuvoco Vistas (Accumulate)"
- IS0LD.XD (iShares Germany Govt Bond UCIT) score 2.4 — "Govt bonds extend recovery tracking rise in US treasuries"
- MU (Micron Technology, Inc.) score 2.2 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- TEO (Telecom Argentina SA) score 2.2 — "Argentina beat England 2-1 to reach World Cup final . They will play Spain in final"
- LGDS (JPMorgan Fundamental Data Scie) score 2.2 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- CUPID.NS (CUPID LIMITED) score 2.1 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- BHEL.NS (BHEL) score 2.0 — "BHEL Q1 results: BHEL swings to  ₹376.71 crore net profit in June quarter"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.6 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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