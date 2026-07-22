# Transmission Layer — board brief · 2026-07-22 11:28Z

data as of **2026-07-22** · 98 series · 9 red / 41 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.464, 12d in regime; vol-pct 0.596, breadth-off 0.333, Markov P(high-vol) 0.043)
- [WEAK] **safe_haven_gold** — corr20 0.06, corr60 -0.43, contra nifty_50 corr20=0.07, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.47, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 -0.01, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.01, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.28, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.25, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.265, β 0.0329, p 0.00019); driver zc 2.11 → expected 0.317%. Type hit-rate 0.816 (n=3113).
- Track record · residual_reversion: hit-rate **0.494** (n=1152) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=3113) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.3] commodities · 2 series ↑
- wti [COMMODITIES]: last 87.37, z20 2.46, zc 1.16, resid-z 0.77 [quiet], 1d 2.90%, 1-session move +2.90% ≥ 1.5%; |z20|=2.46
- brent [COMMODITIES]: last 84.76, z20 1.01, zc -2.69, resid-z 0.80 [moved], 1d -6.87%, 1-session move -6.87% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent jump in oil prices, triggered by escalating U.S.-Iran hostilities and threats to shipping in the Middle East, is propagating through the commodities channel. The move in WTI and Brent crude is largely priced, with resid_z values of 0.77 and 0.8, respectively, indicating that the move is mostly explained by factor exposures. However, the channel marked inr_oil_channel is WEAK, which may limit the transmission of this move to the Indian market.
- **Gap**: No gap: the move in WTI and Brent crude is largely priced, with resid_z values indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has a rho of -0.621 with WTI and has not yet reacted to the move in oil prices. The metal_copper_channel, which is VALID, may also transmit the move to Indian metal equities.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 1d
- **India receivers**: nifty_midcap_100 (rho -0.621, z -0.11)
- Source: Oil prices climb to six-week high as hopes of de-escalation in Iran diminish — MarketWatch Top, 2026-07-22. https://www.marketwatch.com/story/oil-prices-climb-to-six-week-high-as-hopes-of-de-escalation-in-iran-diminish-b5fb0942?mod=mw_rss_topstories
- Source: Oil Jumps Nearly 4% as Houthis Threaten Red Sea Blockade — OilPrice, 2026-07-22. https://oilprice.com/Latest-Energy-News/World-News/Oil-Jumps-Nearly-4-as-Houthis-Threaten-Red-Sea-Blockade.html
- Source: Brent Crude tops $95 as US-Iran tensions, Hormuz blockade drive oil rally — Mint Markets, 2026-07-22. https://www.livemint.com/market/commodities/brent-crude-tops-95-as-us-iran-tensions-hormuz-blockade-drive-oil-rally-11784714555942.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.05] brent_wti_spread ↓
- brent_wti_spread [DERIVED]: last -2.61, z20 -6.05, zc n/a, resid-z n/a [quiet], 1d -142.79%, |z20|=6.05; 1y-pct=1
- **Mechanism**: The brent_wti_spread decline is a priced move with a z20 level of -6.053, indicating that the move is largely explained by factors. The spread's decline may propagate through the metal_copper_channel, which is a valid channel, potentially impacting Indian metal equities. However, the inr_oil_channel is weak, suggesting that the usual transmission mechanism from oil prices to INR is not currently active.
- **Gap**: No gap: the brent_wti_spread move is a priced move with a z20 level of -6.053, indicating that the move is largely explained by factors.
- **India take**: The Indian instrument that may express this move is the Nifty Metal index, which may decline due to the potential impact from the metal_copper_channel. However, the INR may not react strongly due to the weak inr_oil_channel.
- Watch next: nifty_metal (down) — not yet - watch; potential impact from metal_copper_channel
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-04 (d=0.0), 2026-05-06 (d=0.01)

### [RED 5.47] dyn_hdbfs_bo ↓
- dyn_hdbfs_bo [EQUITIES]: last 707.10, z20 -3.47, zc -1.05, resid-z -0.98 [quiet], 1d -1.86%, |z20|=3.47
- **Mechanism**: The decline in dyn_hdbfs_bo is largely priced, with a resid_z of -0.98, indicating that the move is mostly explained by factor exposures. The event is likely related to HDB Financial's bond reissue, which may have influenced investor sentiment. The lack of a significant unexplained component suggests that the market has already incorporated the news into the price.
- **Gap**: No gap: the move in dyn_hdbfs_bo is largely explained by factor exposures, with a small resid_z
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has not yet reacted. Additionally, dyn_jiofin_bo has already reacted, indicating some transmission of the move to other Indian financial instruments.
- Watch next: nifty_midcap_100 (down) — not yet - watch; correlated instrument with rho=0.558
- **India receivers**: nifty_midcap_100 (rho 0.558, z -0.11); nifty_50 (rho 0.413, z -0.71); usd_inr (rho -0.401, z 1.44); dyn_jiofin_bo (rho 0.378, z -1.19)
- Source: HDB Financial to reissue 3-year bonds, bankers say — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/hdb-financial-to-reissue-3-year-bonds-bankers-say/articleshow/132537022.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.06), 2025-12-31 (d=0.06)

### [AMBER 5.45] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 90.96, z20 -1.52, zc -0.60, resid-z -0.49 [quiet], 1d -0.18%, 1y-pct=1
- ust_30y [RATES]: last 5.11, z20 1.46, zc -0.92, resid-z -1.56 [unexplained], 1d 0.99%, 1y-pct=98
- ust_10y [RATES]: last 4.60, z20 1.44, zc -0.45, resid-z -1.35 [quiet], 1d 1.10%, 1y-pct=98
- tips_10y_real [RATES]: last 2.35, z20 1.38, zc -0.98, resid-z -2.43 [unexplained], 1d 1.73%, 1y-pct=99
- ust_2y [RATES]: last 4.21, z20 1.02, zc 0.37, resid-z -0.28 [quiet], 1d 0.72%, 1y-pct=98
- **Mechanism**: The recent surge in US Treasury yields, driven by inflation concerns and rising oil prices, is propagating through the global bond market, affecting instruments such as dyn_bond and ust_30y. This move is priced, as evidenced by the relatively small resid_z values, indicating that the market has already accounted for the factors driving the yield increase.
- **Gap**: No gap: The move in US Treasury yields is largely priced, with small resid_z values indicating that the market has already accounted for the driving factors.
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the global bond market volatility. However, the GoI yield has not yet reacted significantly, and the goi_ust_comove channel is marked as INSUFFICIENT_DATA, indicating a lack of clear transmission.
- Watch next: nifty_50 (down) — not yet - watch; Potential transmission of global bond market volatility to Indian equities
- Source: Global Market: Singapore launches green bond issue targeting up to $2 billion — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-singapore-launches-green-bond-issue-targeting-up-to-2-billion/articleshow/132551864.cms
- Source: Treasury Yields Hit Two-Month High as Oil Sparks Inflation Risk — Mint Markets, 2026-07-21. https://www.livemint.com/market/treasury-yields-hit-two-month-high-as-oil-sparks-inflation-risk-11784645430148.html
- Source: ICICI Bank eyes $500 million dollar bond issue via GIFT City — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/icici-bank-eyes-500-million-dollar-bond-issue-via-gift-city/articleshow/132538886.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.45] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 338.00, z20 3.45, zc -0.17, resid-z 0.61 [quiet], 1d -0.68%, |z20|=3.45; 1y-pct=99
- **Mechanism**: The recent surge in Karur Vysya Bank's stock price can be attributed to its strong Q1 FY27 results, with a record profit of ₹756 crore, up 45% year-on-year. The bank's net interest margin (NIM) also improved to 4.26%, beating expectations. This positive earnings surprise has led to a re-rating of the stock, driving its price up. The VALID metal_copper_channel and vix_equity_inverse channels suggest a favorable risk-on environment, supporting the move.
- **Gap**: No gap: the big raw move in Karur Vysya Bank's stock price is largely priced in, given its strong earnings performance and improving NIM, with a resid_z of 0.61, which is not unusually high.
- **India take**: The Indian instrument that expresses this move is dyn_indusindbk_bo, which has already reacted, while nifty_midcap_100 is still waiting to react. Other transmission candidates like dyn_jiofin_bo and dyn_havells_ns have also reacted, indicating a broad-based move in the financial and banking sector.
- Watch next: dyn_indusindbk_bo (up) — already moved; high correlation with Karur Vysya Bank
- Watch next: nifty_midcap_100 (up) — not yet - watch; moderate correlation with Karur Vysya Bank
- **India receivers**: dyn_indusindbk_bo (rho 0.534, z 1.9); nifty_midcap_100 (rho 0.491, z -0.11); dyn_jiofin_bo (rho 0.477, z -1.19); nifty_50 (rho 0.469, z -0.71)
- Source: Broker’s Call: Karur Vysya Bank (Buy) — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/brokers-call-karur-vysya-bank-buy/article71248725.ece
- Source: Karur Vysya Bank shares jump 13% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Top Gainers & Losers on July 21: Karur Vysya Bank, TVS Motor, Zen Tech, Meesho, Thermax among top gainers today — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-july-21-karur-vysya-bank-tvs-motor-zen-tech-meesho-thermax-among-top-gainers-today-11784625895681.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 4.74] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.75, z20 -2.74, zc 0.41, resid-z 0.54 [quiet], 1d 0.61%, |z20|=2.74; 1y-pct=4
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.651 via dyn_hdb, z -0.71, quiet); nifty_midcap_100 (rho 0.511 via dyn_hdb, z -0.11, quiet); dyn_indusindbk_bo (rho 0.489 via dyn_hdb, z 1.9, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.651 vs dyn_hdb, historically leads by 1d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.525 vs dyn_hdb, historically leads by 1d
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.511 vs dyn_hdb, historically leads by 1d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.618 vs dyn_hdb
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.591 vs dyn_hdb
- **India receivers**: nifty_50 (rho 0.651, z -0.71); nifty_midcap_100 (rho 0.511, z -0.11); dyn_indusindbk_bo (rho 0.489, z 1.9)
- Source: HDFC Bank share price drops for third straight session after Q1FY27 results: Should you buy on dip or avoid? — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-drops-for-third-straight-session-after-q1fy27-results-should-you-buy-on-dip-or-avoid-11784700700233.html
- Source: HDFC Bank shares fall over 7 per cent in two days after Q1 earnings — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-over-7-per-cent-in-two-days-after-q1-earnings/article71249104.ece
- Source: Sensex today | Stock Market Live: Sensex drops 250 pts, Nifty below 24,200; HDFC Bank lead losers — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-21st-may-2026/article71245381.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.68] commodities · 3 series ↑
- corn [COMMODITIES]: last 481.00, z20 3.36, zc 4.94, resid-z 0.69 [moved], 1d 6.24%, |z20|=3.36; 1y-pct=100
- wheat [COMMODITIES]: last 690.00, z20 1.89, zc 0.85, resid-z 0.25 [quiet], 1d 1.77%, |z20|=1.89; 1y-pct=100
- soybeans [COMMODITIES]: last 1227.25, z20 1.44, zc 0.63, resid-z -0.07 [quiet], 1d 0.64%, 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_patanjali_ns (rho -0.524 via wheat, z -1.95, reacted); dyn_adanient_bo (rho -0.36 via soybeans, z 0.34, quiet); dyn_tataelxsi_ns (rho -0.351 via wheat, z -1.69, reacted)
- **India receivers**: dyn_patanjali_ns (rho -0.524, z -1.95); dyn_adanient_bo (rho -0.36, z 0.34); dyn_tataelxsi_ns (rho -0.351, z -1.69)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.63] dyn_coin ↑
- dyn_coin [EQUITIES]: last 175.92, z20 2.63, zc 2.11, resid-z 0.20 [priced], 1d 9.66%, |z20|=2.63
- **Mechanism**: dyn_coin ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: 'Global economy is crashing': Rich Dad Poor Dad author Robert Kiyosaki repeats stock market crash prediction — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/global-economy-is-crashing-rich-dad-poor-dad-author-robert-kiyosaki-repeats-stock-market-crash-prediction-11784713956376.html
- Source: Global Market: Airbus shares surge over 5% after €5 billion buyback, ambitious 2029 profit targets — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-airbus-shares-surge-over-5-after-5-billion-buyback-ambitious-2029-profit-targets/articleshow/132556495.cms
- Source: Global Market: Chinese tech firms raise over $27 billion in Hong Kong to fuel AI, chip expansion — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-chinese-tech-firms-raise-over-27-billion-in-hong-kong-to-fuel-ai-chip-expansion/articleshow/132554758.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-03 (d=0.0), 2025-08-08 (d=0.08)

## Watchlist (below surfacing floor)
dyn_olaelec_ns ↓ (4.53), usd_jpy ↑ (4.49), dyn_icicigi_bo ↓ (4.4), dyn_bharatcoal_ns ↓ (4.28), dyn_qessf ↓ (4.22), dyn_nflx ↓ (4.03), dyn_indusindbk_bo ↑ (3.9), dyn_ohi ↑ (3.87), indices · 3 series ↑ (3.8), dyn_bac ↑ (3.5), usd_inr ↑ (3.44), gold_silver_ratio ↑ (3.1)

## India macro
- nifty_50: 23991.0508 (1d -0.81%, z20 -0.71, flag none)
- nifty_midcap_100: 62284.6484 (1d -1.10%, z20 -0.11, flag none)
- usd_inr: 96.5650 (1d 0.08%, z20 1.44, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5962 (1d -0.29%, z20 0.56, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 81.5 — "Bandhan Bank shares crash 15% after Q1 results; lender cuts RoA guidance. Should you buy, "
- INOXINDIA.NS (INOX INDIA LIMITED) score 73.1 — "InMobi IPO: SoftBank-backed Indian ad tech firm appoints JPMorgan, Jefferies for its upcom"
- HDB (HDFC Bank Limited) score 70.2 — "Bandhan Bank shares crash 15% after Q1 results; lender cuts RoA guidance. Should you buy, "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 67.6 — "Bandhan Bank shares crash 15% after Q1 results; lender cuts RoA guidance. Should you buy, "
- BAC (Bank of America Corporation) score 66.7 — "Bandhan Bank shares crash 15% after Q1 results; lender cuts RoA guidance. Should you buy, "
- IDBI.NS (IDBI BANK LIMITED) score 58.6 — "Bandhan Bank shares crash 15% after Q1 results; lender cuts RoA guidance. Should you buy, "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.3 — "Sterlite Tech shares tumble 27% from June peak after 400% surge in 2026. Should you catch "
- COIN (Coinbase Global, Inc.) score 46.7 — "Global Market: Chinese stocks advance on AI, chip rally; Hong Kong shares slip"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.0 — "Sterlite Tech shares tumble 27% from June peak after 400% surge in 2026. Should you catch "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 36.7 — "InMobi IPO: SoftBank-backed Indian ad tech firm appoints JPMorgan, Jefferies for its upcom"
- OHI (Omega Healthcare Investors, In) score 28.5 — "Cube Highways Trust InvIT subscription opens today. Here are key details for investors"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 25.6 — "Bandhan Bank shares crash 15% after Q1 results; lender cuts RoA guidance. Should you buy, "
- BOND (PIMCO Active Bond Exchange-Tra) score 22.4 — "Global Market: Singapore launches green bond issue targeting up to $2 billion"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.7 — "U.S.-Iran Conflict Threatens Long-Term Energy Shock Across Asia"
- CHKP (Check Point Software Technolog) score 21.6 — "Caliber Mining & Logistics IPO allotment date today. GMP, steps to check allotment status "
- VT (Vanguard Total World Stock Ind) score 15.0 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.2 — "Adani Power Q1 Results: Profit jumps 42% YoY to Rs 4,806 cr; co approves Rs 15,000 cr fund"
- GS (Goldman Sachs Group, Inc. (The) score 11.2 — "US Stock Market: Goldman Sachs launches new private markets platform to expand offerings f"
- JIOFIN.BO (Jio Financial Services Limited) score 11.0 — "M&M Financial shares zoom 8% after Q1 profit jumps, brokerages lift target prices"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 10.3 — "ICICI Bank eyes $500 million dollar bond issue via GIFT City"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.2 — "Mahindra Finance shares surge 19% in just 2 sessions on Q1 boost; should you buy, sell, ho"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.4 — "M&M Financial shares zoom 8% after Q1 profit jumps, brokerages lift target prices"
- MS (Morgan Stanley) score 8.6 — "InMobi IPO: SoftBank-backed Indian ad tech firm appoints JPMorgan, Jefferies for its upcom"
- META (Meta) score 7.0 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.4 — "BlueStone Jewellery shares soar 29% in 2 days after stellar Q1 show. Should you buy, sell "
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 6.2 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 5.8 — "Tata Group stock Indian Hotels falls 1% despite strong Q1 results 2026. Should you buy or "
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.3 — "HFCL's X-factor is defence & aerospace? Deven Choksey sees another 66% upside potential, h"
- NVDA (NVIDIA Corporation) score 4.5 — "Nvidia among 6 megacaps that Morningstar says are undervalued. See full list"
- NFLX (Netflix, Inc.) score 3.9 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- SKHYV (SK hynix Inc. American Deposit) score 3.6 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 3.4 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 3.3 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 3.2 — "Dollar wavers as markets grapple with Gulf tensions"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 3.0 — "Bharat Coking Coal share price crashes 7% after Q1FY27 results"
- LTH (Life Time Group Holdings, Inc.) score 3.0 — "Vedanta shares drop 26% in two months, erase all post-demerger gains. Time to buy or bette"
- COALINDIA.NS (COAL INDIA LTD) score 2.8 — "Bharat Coking Coal shares crash 8% after Coal India arm posts Rs 68 crore Q1 net loss"
- BIOCON.BO (BIOCON LTD.) score 0.8 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.5 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.4 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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