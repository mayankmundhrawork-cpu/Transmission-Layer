# Transmission Layer — board brief · 2026-07-23 06:43Z

data as of **2026-07-23** · 98 series · 8 red / 36 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.53, 13d in regime; vol-pct 0.561, breadth-off 0.5, Markov P(high-vol) 0.025)
- [WEAK] **safe_haven_gold** — corr20 0.02, corr60 -0.43, contra nifty_50 corr20=0.05, last shift 2026-05-29. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.5, corr60 0.34, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.09, corr60 -0.04, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.81, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.1, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.27, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.397, β 0.2399, p 0.0); driver zc 2.32 → expected 0.568%. Type hit-rate 0.819 (n=3067).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.36, β -0.2369, p 0.0); driver zc 2.32 → expected -0.56%. Type hit-rate 0.819 (n=3067).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.28, β 0.2911, p 0.01352); driver zc 2.08 → expected 0.373%. Type hit-rate 0.819 (n=3067).
- Track record · residual_reversion: hit-rate **0.49** (n=1162) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=3067) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.18] commodities · 2 series ↑
- brent [COMMODITIES]: last 96.29, z20 2.35, zc 0.88, resid-z 0.97 [quiet], 1d 2.36%, 1-session move +2.36% ≥ 1.5%; |z20|=2.35; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 88.32, z20 2.24, zc 0.69, resid-z 0.55 [quiet], 1d 1.72%, 1-session move +1.72% ≥ 1.5%; |z20|=2.24
- **Mechanism**: The recent surge in oil prices, driven by Middle East tensions and Houthi blockades, is propagating through the commodities channel, affecting brent and wti prices. This move is largely priced, given the small resid_z values of 0.97 and 0.55 for brent and wti, respectively. The valid gold_silver_comove and metal_copper_channel may also play a role in transmitting this shock to Indian metal equities.
- **Gap**: No gap: the move in oil prices is largely priced, with small resid_z values indicating that the current price levels are consistent with factor exposures.
- **India take**: The Indian rupee may come under pressure due to higher oil prices, which could lead to a decline in Indian metal equities, such as those in the nifty_midcap_100 index. However, the RBI's intervention may help shield the rupee from excessive volatility.
- Watch next: nifty_midcap_100 (down) — not yet - watch; negative correlation with brent
- **India receivers**: nifty_midcap_100 (rho -0.658, z -0.73); nifty_50 (rho -0.504, z -1.13); dyn_hdbfs_bo (rho -0.482, z -3.71)
- Source: Two Saudi Oil Tankers Targeted as Houthi Blockade Disrupts Red Sea Shipping — OilPrice, 2026-07-23. https://oilprice.com/Latest-Energy-News/World-News/Two-Saudi-Oil-Tankers-Targeted-as-Houthi-Blockade-Disrupts-Red-Sea-Shipping.html
- Source: Rupee likely shielded by RBI intervention as oil surges — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-likely-shielded-by-rbi-intervention-as-oil-surges/articleshow/132572568.cms
- Source: Oil prices scorch Indian bonds; rising Treasury yields add to pressure — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/oil-prices-scorch-indian-bonds-rising-treasury-yields-add-to-pressure/articleshow/132572526.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.95] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.26, z20 2.01, zc 0.92, resid-z 1.09 [quiet], 1d 1.19%, |z20|=2.01; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.73, z20 -1.80, zc -0.82, resid-z -0.11 [quiet], 1d -0.24%, 1y-pct=0
- ust_10y [RATES]: last 4.63, z20 1.71, zc 0.67, resid-z 0.94 [quiet], 1d 0.65%, |z20|=1.71; 1y-pct=99
- tips_10y_real [RATES]: last 2.37, z20 1.58, zc 0.49, resid-z 0.64 [quiet], 1d 0.85%, |z20|=1.58; 1y-pct=100
- ust_30y [RATES]: last 5.13, z20 1.54, zc 0.61, resid-z 0.79 [quiet], 1d 0.39%, |z20|=1.54; 1y-pct=99
- **Mechanism**: The recent rise in US Treasury yields, particularly the 2-year and 10-year yields, is putting pressure on Indian government bonds, as higher oil prices and rising Treasury yields threaten to revive inflation pressures and weaken the Indian rupee. This situation is likely to significantly impact energy-intensive industries and economies, given India's high dependence on crude oil imports. The mechanism of transmission is through the VALID gold_silver_comove and metal_copper_channel, which indicate a co-movement of monetary metals and global copper leading Indian metal equities.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with resid_z values indicating that the moves are largely explained by factor exposures.
- **India take**: The Indian 10-year government bond yield may react to the rising US Treasury yields, and the recent decline in Indian government bonds may continue. The INR may also weaken due to higher oil prices, which could impact energy-intensive industries and the overall economy.
- Watch next: nifty_50 (down) — not yet - watch; Weakened INR due to higher oil prices may negatively impact Indian equities
- Source: Oil prices scorch Indian bonds; rising Treasury yields add to pressure — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/oil-prices-scorch-indian-bonds-rising-treasury-yields-add-to-pressure/articleshow/132572526.cms
- Source: ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/icici-bank-sets-initial-guidance-for-first-dollar-bond-in-nearly-9-years-bankers-say/articleshow/132571495.cms
- Source: After equities and mutual funds, it’s time for bond SIPs — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/after-equities-and-mutual-funds-its-time-for-bond-sips/article71254365.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.71] dyn_hdbfs_bo ↓
- dyn_hdbfs_bo [EQUITIES]: last 694.95, z20 -3.71, zc -0.97, resid-z -0.61 [quiet], 1d -1.72%, |z20|=3.71
- **Mechanism**: The decline in dyn_hdbfs_bo is largely priced, with a resid_z of -0.98, indicating that the move is mostly explained by factor exposures. The event is likely related to HDB Financial's bond reissue, which may have influenced investor sentiment. The lack of a significant unexplained component suggests that the market has already incorporated the news into the price.
- **Gap**: No gap: the move in dyn_hdbfs_bo is largely explained by factor exposures, with a small resid_z
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has not yet reacted. Additionally, dyn_jiofin_bo has already reacted, indicating some transmission of the move to other Indian financial instruments.
- Watch next: nifty_midcap_100 (down) — not yet - watch; correlated instrument with rho=0.558
- **India receivers**: nifty_midcap_100 (rho 0.563, z -0.73); nifty_50 (rho 0.415, z -1.13); dyn_eternal_ns (rho 0.399, z 0.82); usd_inr (rho -0.389, z 1.29)
- Source: HDB Financial to reissue 3-year bonds, bankers say — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/hdb-financial-to-reissue-3-year-bonds-bankers-say/articleshow/132537022.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.06), 2025-12-31 (d=0.06)

### [RED 4.92] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.19, z20 -2.92, zc -1.53, resid-z 0.29 [priced], 1d -2.28%, |z20|=2.92; 1y-pct=0
- **Mechanism**: The decline in dyn_hdb is largely priced, with a small resid_z of 0.29, suggesting that the move is largely explained by factor exposures. The vix_equity_inverse channel is valid, with a strong negative correlation between vol spike and equity drawdown, which may contribute to the propagation of the move.
- **Gap**: No gap: The decline in dyn_hdb is largely priced, with a small resid_z of 0.29, suggesting that the move is largely explained by factor exposures.
- **India take**: The Indian instrument nifty_50 has already reacted, with a z20 of -1.13, while nifty_midcap_100 remains quiet with a z20 of -0.73. The decline in dyn_hdb may transmit to other Indian equities, particularly those with high correlations with HDFC Bank.
- Watch next: nifty_midcap_100 (down) — not yet - watch; Historical lead of 1d and positive correlation with dyn_hdb
- Watch next: india_vix (up) — not yet - watch; Historical lead of 1d and negative correlation with dyn_hdb
- **India receivers**: nifty_50 (rho 0.666, z -1.13); nifty_midcap_100 (rho 0.534, z -0.73); dyn_jiofin_bo (rho 0.479, z -1.17)
- Source: HDFC Bank shares slide 10% in four day after Q1 results but brokerages see up to 40% upside. Here’s why — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-slide-10-in-four-day-after-q1-results-but-brokerages-see-up-to-40-upside-heres-why/articleshow/132573294.cms
- Source: HDFC Bank shares tumble over 8% in three days on net interest margin concerns — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-tumble-over-8-in-three-days-on-net-interest-margin-concerns/article71253282.ece
- Source: HDFC Bank share price drops for third straight session after Q1FY27 results: Should you buy on dip or avoid? — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-drops-for-third-straight-session-after-q1fy27-results-should-you-buy-on-dip-or-avoid-11784700700233.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.66] commodities · 3 series ↑
- corn [COMMODITIES]: last 486.00, z20 3.34, zc 4.13, resid-z 1.09 [moved], 1d 5.19%, |z20|=3.34; 1y-pct=100
- wheat [COMMODITIES]: last 706.50, z20 1.98, zc 0.05, resid-z 1.59 [unexplained], 1d 0.11%, |z20|=1.98; 1y-pct=100
- soybeans [COMMODITIES]: last 1242.75, z20 1.66, zc 0.78, resid-z 0.83 [quiet], 1d 0.79%, |z20|=1.66; 1y-pct=100
- **Mechanism**: The recent surge in commodity prices, particularly corn, wheat, and soybeans, is driven by a combination of factors, including supply and demand imbalances and market sentiment. The move is largely priced, with a significant portion of the price action explained by factor exposures. However, the unexplained component, as measured by resid_z, suggests that there may be some residual momentum that could drive further price action. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper prices may influence Indian metal equities.
- **Gap**: No gap: the move in commodity prices is largely priced, with a significant portion of the price action explained by factor exposures
- **India take**: The Indian instruments that express this move are dyn_patanjali_ns and dyn_tataelxsi_ns, which have already reacted to the surge in wheat prices, while dyn_adanient_bo remains quiet despite its exposure to soybeans
- Watch next: corn (up) — already moved; high z20 score and low resid_z indicate a priced move
- Watch next: wheat (up) — not yet - watch; unexplained move with high resid_z suggests potential for further price action
- Watch next: soybeans (up) — quiet; low z20 score and low resid_z indicate a quiet market
- **India receivers**: dyn_patanjali_ns (rho -0.515, z -1.58); dyn_adanient_bo (rho -0.38, z -0.5); dyn_tataelxsi_ns (rho -0.36, z -1.48)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [AMBER 4.49] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 336.25, z20 2.49, zc -0.14, resid-z -0.05 [quiet], 1d -0.52%, |z20|=2.49; 1y-pct=98
- **Mechanism**: dyn_karurvysya_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.496 via dyn_karurvysya_ns, z 0.34, quiet); nifty_midcap_100 (rho 0.488 via dyn_karurvysya_ns, z -0.73, quiet); dyn_jiofin_bo (rho 0.473 via dyn_karurvysya_ns, z -1.17, reacted); nifty_50 (rho 0.466 via dyn_karurvysya_ns, z -1.13, reacted); dyn_havells_ns (rho 0.407 via dyn_karurvysya_ns, z 1.55, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.496, z 0.34); nifty_midcap_100 (rho 0.488, z -0.73); dyn_jiofin_bo (rho 0.473, z -1.17); nifty_50 (rho 0.466, z -1.13)
- Source: Broker’s Call: Karur Vysya Bank (Buy) — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/brokers-call-karur-vysya-bank-buy/article71248725.ece
- Source: Karur Vysya Bank shares jump 13% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Top Gainers & Losers on July 21: Karur Vysya Bank, TVS Motor, Zen Tech, Meesho, Thermax among top gainers today — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-july-21-karur-vysya-bank-tvs-motor-zen-tech-meesho-thermax-among-top-gainers-today-11784625895681.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [AMBER 4.15] usd_jpy ↑
- usd_jpy [FX]: last 163.10, z20 2.15, zc -0.15, resid-z 0.92 [quiet], 1d -0.05%, |z20|=2.15; 1y-pct=99
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.524 vs usd_jpy, historically leads by 1d
- Source: US-Iran tensions underpin dollar as yen nears 40-year low — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/forex/forex-news/us-iran-tensions-underpin-dollar-as-yen-nears-40-year-low/articleshow/132570439.cms
- Source: Yen’s Slump in Trade-Weighted Gauge Shows Its Broad-Based Drop — Mint Markets, 2026-07-23. https://www.livemint.com/market/yens-slump-in-trade-weighted-gauge-shows-its-broad-based-drop-11784768496092.html
- Source: Yen Rebound Ebbs After Brief Rally on Outlook for BOJ Rate Hikes — Mint Markets, 2026-07-22. https://www.livemint.com/market/yen-rebound-ebbs-after-brief-rally-on-outlook-for-boj-rate-hikes-11784754197557.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 4.07] dyn_bharatcoal_ns ↓
- dyn_bharatcoal_ns [EQUITIES]: last 34.98, z20 -2.07, zc 0.06, resid-z n/a [quiet], 1d 0.17%, |z20|=2.07
- **Mechanism**: dyn_bharatcoal_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Sotefin Bharat IPO listing: Shares hit upper circuit after listing at a 10% premium; details here — Mint Markets, 2026-07-23. https://www.livemint.com/market/ipo/sotefin-bharat-ipo-listing-shares-hit-upper-circuit-after-listing-at-a-10-premium-details-here-11784782273860.html
- Source: Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/sotefin-bharat-shares-set-for-bse-sme-debut-today-gmp-signals-muted-listing/articleshow/132571290.cms
- Source: Bharat Coking Coal shares fall 7% after Q1FY27 net loss — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/bharat-coking-coal-shares-fall-8-after-q1fy27-net-loss/article71252055.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-11 (d=0.3), 2026-07-03 (d=0.75)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (3.92), indices · 3 series ↑ (3.89), cross-asset · 2 series ↑ (3.87), dyn_icicigi_bo ↓ (3.8), fx · 2 series ↑ (3.36), usd_inr ↑ (3.29), dyn_gs ↑ (3.01), brent_wti_spread ↑ (2.77), dyn_lth ↑ (2.73), dyn_indusindbk_bo ↑ (2.34), bovespa ↑ (2.15), dyn_inoxindia_ns ↑ (2.08)

## India macro
- nifty_50: 23939.4492 (1d -0.24%, z20 -1.13, flag none)
- nifty_midcap_100: 61995.1484 (1d -0.46%, z20 -0.73, flag none)
- usd_inr: 96.5350 (1d 0.20%, z20 1.29, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5897 (1d -0.23%, z20 0.25, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 84.9 — "From Gift Nifty, Tesla Q2 earnings to crude oil prices: 8 key things that changed for Indi"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.0 — "Stock recommendations for 23 July from MarketSmith India"
- HDB (HDFC Bank Limited) score 68.7 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- BAC (Bank of America Corporation) score 66.8 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 66.5 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- IDBI.NS (IDBI BANK LIMITED) score 59.1 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- COIN (Coinbase Global, Inc.) score 49.5 — "Global Refiners Are Cutting Out Oil Traders To Buy Venezuelan Crude Directly"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.6 — "Stocks to watch: Reliance, HCL Tech, Sona BLW, HFCL, Mahindra Lifespace, Vedanta Oil, Saat"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 46.8 — "Stock recommendations for 23 July from MarketSmith India"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.6 — "Stocks to watch: Reliance, HCL Tech, Sona BLW, HFCL, Mahindra Lifespace, Vedanta Oil, Saat"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.6 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- OHI (Omega Healthcare Investors, In) score 29.4 — "Alphabet's quarterly earnings beat Wall Street estimates, but here's what is spooking inve"
- CHKP (Check Point Software Technolog) score 24.0 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.3 — "FAR bonds lose their pull as tailwinds fade"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.0 — "NTPC Green Energy shares zoom 9% after Q1 results"
- COALINDIA.NS (COAL INDIA LTD) score 19.4 — "Stock recommendations for 23 July from MarketSmith India"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.7 — "Adani Green shares tumble 5% after Q1 results. Here’s why Bernstein has an Underperform ra"
- VT (Vanguard Total World Stock Ind) score 12.5 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- GS (Goldman Sachs Group, Inc. (The) score 11.3 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.3 — "Bluestone Jewellery shares rocket 36% in just three days after Q1 results. Can the momentu"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "Oracle Financial Services shares jump 5% on strong Q1 results; PAT soars 121%, revenue up "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.8 — "Oracle Financial Services shares jump 5% on strong Q1 results; PAT soars 121%, revenue up "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.5 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- MS (Morgan Stanley) score 7.1 — "InMobi IPO: SoftBank-backed Indian ad tech firm appoints JPMorgan, Jefferies for its upcom"
- META (Meta) score 6.8 — "The Metals Selloff Is Creating New Winners And Losers"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.3 — "Bluestone Jewellery shares rocket 36% in just three days after Q1 results. Can the momentu"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.2 — "Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.3 — "Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why"
- LTH (Life Time Group Holdings, Inc.) score 5.2 — "India's capex boom is different this time and not dependent on one sector: TCG AMC"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 5.1 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.9 — "Tata Group stock Indian Hotels falls 1% despite strong Q1 results 2026. Should you buy or "
- NVDA (NVIDIA Corporation) score 4.6 — "AMD plans to invest to up $5 billion into Anthropic as it seeks to cut into Nvidia’s domin"
- ETERNAL.NS (ETERNAL LIMITED) score 4.0 — "Eternal share price rises 3% on strong Q1 results. Is it a stock to buy today?"
- NFLX (Netflix, Inc.) score 3.3 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- BHEL.NS (BHEL) score 2.9 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 2.7 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 2.7 — "Dollar wavers as markets grapple with Gulf tensions"
- BIOCON.BO (BIOCON LTD.) score 0.7 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.3 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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