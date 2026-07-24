# Transmission Layer — board brief · 2026-07-24 21:48Z

data as of **2026-07-24** · 98 series · 10 red / 31 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.599, 1d in regime; vol-pct 0.67, breadth-off 0.529, Markov P(high-vol) 0.031)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.45, contra nifty_50 corr20=0.14, last shift 2026-06-01. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.06, corr60 -0.03, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.09, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.25, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_infy → nifty_it: leads 1d (ccf 0.438, β 0.3319, p 0.0); driver zc 1.51 → expected 1.4%. Type hit-rate 0.82 (n=3054).
- **SETUP** dyn_infy → dyn_techm_ns: leads 1d (ccf 0.276, β 0.2362, p 0.0); driver zc 1.51 → expected 0.996%. Type hit-rate 0.82 (n=3054).
- Track record · residual_reversion: hit-rate **0.491** (n=1163) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=3054) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.706** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.92] commodities · 2 series ↑
- brent [COMMODITIES]: last 98.38, z20 2.09, zc -0.61, resid-z -0.72 [quiet], 1d -2.29%, 1-session move -2.29% ≥ 1.5%; |z20|=2.09; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 90.47, z20 2.07, zc -0.58, resid-z -0.56 [quiet], 1d -1.87%, 1-session move -1.87% ≥ 1.5%; |z20|=2.07
- **Mechanism**: The recent surge in oil prices, led by Brent and WTI, is driven by supply chain disruptions and geopolitical tensions, which have resulted in a priced move with small resid_z values, indicating that the market has already factored in the risks. The move is not an anomaly, but rather a reflection of the current market conditions. The VALID gold_silver_comove and metal_copper_channel suggest that the market is responding to the supply chain disruptions and monetary metals co-move, while the INVERTED safe_haven_gold channel indicates a risk-off sentiment.
- **Gap**: No gap: the move in oil prices is priced, with small resid_z values, and the Indian transmission candidates have already reacted
- **India take**: The Indian instruments, such as nifty_midcap_100 and nifty_50, have already reacted to the oil price surge, while dyn_indusindbk_bo remains quiet. The move in oil prices is likely to have a negative impact on the Indian economy, given the country's dependence on oil imports.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to oil price surge
- Watch next: nifty_50 (down) — already moved; reacted to oil price surge
- **India receivers**: nifty_midcap_100 (rho -0.665, z -1.28); nifty_50 (rho -0.517, z -1.94); dyn_indusindbk_bo (rho -0.496, z 0.01)
- Source: The world is facing its largest oil shock ever. Here is why prices are not higher. — MarketWatch Top, 2026-07-24. https://www.marketwatch.com/story/the-world-is-facing-its-largest-oil-shock-ever-here-is-why-prices-are-not-higher-0bb943c7?mod=mw_rss_topstories
- Source: The Red Sea Is Becoming Saudi Arabia's Biggest Oil Bottleneck — OilPrice, 2026-07-24. https://oilprice.com/Energy/Crude-Oil/The-Red-Sea-Is-Becoming-Saudi-Arabias-Biggest-Oil-Bottleneck.html
- Source: Stocks edge back up as oil prices pause climb but yields hover near highs — Mint Markets, 2026-07-24. https://www.livemint.com/market/stocks-edge-back-up-as-oil-prices-pause-climb-but-yields-hover-near-highs-11784917992500.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.68] cross-asset · 7 series ↑
- ust_2y [RATES]: last 4.37, z20 3.34, zc 1.08, resid-z 0.05 [quiet], 1d 1.39%, |z20|=3.34; 1y-pct=100
- nasdaq_100 [INDICES]: last 28136.26, z20 -2.63, zc -0.77, resid-z 0.27 [quiet], 1d -1.12%, |z20|=2.63
- ust_10y [RATES]: last 4.71, z20 2.25, zc 0.89, resid-z -0.10 [quiet], 1d 0.86%, |z20|=2.25; 1y-pct=100
- tips_10y_real [RATES]: last 2.43, z20 2.16, zc 0.99, resid-z -0.07 [quiet], 1d 1.67%, |z20|=2.16; 1y-pct=100
- russell_2000 [INDICES]: last 2929.91, z20 -2.11, zc -0.28, resid-z -0.79 [quiet], 1d -0.35%, |z20|=2.11
- dyn_bond [EQUITIES]: last 90.54, z20 -1.68, zc 0.36, resid-z -0.45 [quiet], 1d 0.11%, 1y-pct=0
- ust_30y [RATES]: last 5.17, z20 1.63, zc 0.62, resid-z -0.15 [quiet], 1d 0.39%, |z20|=1.63; 1y-pct=99
- **Mechanism**: The recent move in US stocks, particularly the Nasdaq, is driven by concerns over AI spending and geopolitical tensions, which has led to a decline in chip stocks. This move is priced in, as indicated by the low resid_z values for the affected series. The valid vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, which is already being reflected in the market. The metal_copper_channel also indicates that global copper leads Indian metal equities, which could lead to a reaction in the Indian market.
- **Gap**: No gap: the current move in US stocks is largely priced in, with low resid_z values indicating that the market has already accounted for the factors driving the move.
- **India take**: The Indian market, particularly the Nifty 50, may react to the decline in US stocks and the valid metal_copper_channel, which could lead to a decline in Indian metal equities. However, the reaction has not yet occurred, and the market is waiting to see how the situation develops.
- Watch next: nifty_50 (down) — not yet - watch; Indian equities may react to the decline in US stocks and the valid metal_copper_channel
- Source: US stocks today: Nasdaq lags on angst over AI spending ahead of earnings reports — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-nasdaq-lags-on-angst-over-ai-spending-ahead-of-earnings-reports/articleshow/132614541.cms
- Source: US stocks today: S&P 500, Nasdaq fall as investors juggle earnings, Mideast risks and tariffs — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-stocks-open-subdued-after-tech-rout-mideast-tariffs-in-focus/articleshow/132607371.cms
- Source: US stock market today: S&P 500, Nasdaq futures edge higher as oil retreats; Intel jumps 4% — Mint Markets, 2026-07-24. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-edge-higher-as-oil-retreats-intel-jumps-4-11784894223255.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.39), 2025-05-20 (d=0.55)

### [RED 5.4] usd_jpy ↑
- usd_jpy [FX]: last 163.79, z20 3.40, zc 1.39, resid-z 1.35 [quiet], 1d 0.44%, |z20|=3.40; 1y-pct=100
- **Mechanism**: The USD/JPY move is driven by the US Treasury Department's call for the Bank of Japan to raise interest rates, coupled with surging oil prices reigniting inflation worries. This has led to a strengthening of the dollar, while the yen languishes at 40-year lows despite Japan's pledges to support it. The valid metal_copper_channel and vix_equity_inverse channels suggest that global economic trends and risk-off sentiment are influencing the currency pair.
- **Gap**: No gap: The USD/JPY move is largely priced, with a resid_z of 1.35 indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian Rupee (INR) may weaken against the US Dollar (USD) due to the strengthening of the dollar, although the weak dxy_inr_channel suggests that this transmission mechanism is not currently robust. Indian metal equities may be influenced by the global copper price, which is linked to the USD/JPY pair through the metal_copper_channel.
- Watch next: asx_200 (down) — not yet - watch; Historical correlation with USD/JPY and leading indicator status
- Source: Yen records biggest weekly drop in over two months, dollar climbs for the week — Mint Markets, 2026-07-24. https://www.livemint.com/market/yen-records-biggest-weekly-drop-in-over-two-months-dollar-climbs-for-the-week-11784919025317.html
- Source: Yen heads for biggest weekly drop since May despite Tokyo's support pledges — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/forex/forex-news/yen-heads-for-biggest-weekly-drop-since-may-despite-tokyos-support-pledges/articleshow/132606629.cms
- Source: Global Market: US urges BOJ to keep raising rates, flags persistent yen weakness despite narrower yield gap — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-us-urges-boj-to-keep-raising-rates-flags-persistent-yen-weakness-despite-narrower-yield-gap/articleshow/132596001.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 4.84] dxy ↑
- dxy [FX]: last 101.46, z20 1.84, zc 0.11, resid-z 0.08 [quiet], 1d 0.03%, 20d range extreme; |z20|=1.84; 1y-pct=99
- **Mechanism**: The recent surge in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a decline in gold prices. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which could support gold prices. The VALID metal_copper_channel may also influence Indian metal equities.
- **Gap**: No gap: The DXY move is largely priced, with a small resid_z of -0.69, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that may express this move is the MCX Gold, which may decline if the gold_silver_comove channel dominates. However, the reaction is yet to be seen.
- Watch next: comex_gold (down) — not yet - watch; Historically leads DXY by 3 days
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.65] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 51.74, z20 2.65, zc 1.15, resid-z -0.02 [quiet], 1d 1.50%, |z20|=2.65; 1y-pct=100
- **Mechanism**: The recent surge in dyn_ohi is accompanied by a low resid_z of -0.11, indicating that the move is largely priced in by factor exposures. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may influence Indian metal equities. However, the weak inr_oil_channel and dxy_inr_channel imply that the transmission of oil price and dollar strength to INR is not robust.
- **Gap**: No gap: the low resid_z indicates that the move is largely explained by factor exposures
- **India take**: Indian metal equities, such as those in the Nifty Metal index, may react to the co-movement of monetary metals and global copper, while the INR may not weaken significantly due to the weak inr_oil_channel and dxy_inr_channel.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: Gold, silver prices today: Comex gold rebounds above $4,070; silver at $59 as investors assess Middle East tensions — Mint Markets, 2026-07-24. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-rebounds-above-4-070-silver-at-59-as-investors-assess-middle-east-tensions-11784905494690.html
- Source: US stocks mixed as oil retreats below $100, fresh tariffs and earnings keep investors on edge — Mint Markets, 2026-07-24. https://www.livemint.com/market/stock-market-news/us-stocks-mixed-as-investors-digest-fresh-earnings-trump-tariffs-in-focus-11784900781196.html
- Source: US stocks today: S&P 500, Nasdaq fall as investors juggle earnings, Mideast risks and tariffs — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-stocks-open-subdued-after-tech-rout-mideast-tariffs-in-focus/articleshow/132607371.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [RED 4.6] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.21, z20 -2.60, zc -0.96, resid-z 0.27 [quiet], 1d -6.01%, |z20|=2.60
- **Mechanism**: The decline in dyn_qessf is largely priced, with a small resid_z of 0.27, indicating that the move is mostly explained by factor exposures. The valid metal_copper_channel suggests that global copper prices may be influencing Indian metal equities. However, the absence of a strong channel linking dyn_qessf to Indian markets means that the propagation mechanism is unclear.
- **Gap**: No gap: the small resid_z and mostly priced move suggest that the current price reflects available information
- **India take**: The Indian instrument that may express this move is the Nifty Metal index, which has not yet reacted significantly. The metal_copper_channel suggests that Indian metal equities may follow global copper prices.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may spill over into Indian equities
- Source: Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/ashish-kacholia-exits-defence-stock-that-rallied-108-in-q1-do-you-own-it/articleshow/132597323.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 4.01] commodities · 2 series ↑
- corn [COMMODITIES]: last 487.25, z20 3.18, zc 3.99, resid-z 3.26 [unexplained], 1d 5.01%, |z20|=3.18; 1y-pct=100
- soybeans [COMMODITIES]: last 1252.50, z20 1.77, zc 1.20, resid-z 1.12 [quiet], 1d 1.21%, |z20|=1.77; 1y-pct=100
- **Mechanism**: The recent surge in commodities, particularly corn and soybeans, is driven by unexplained factors, as evidenced by their high resid_z values. This move may propagate through the global commodity complex, potentially influencing Indian metal equities via the metal_copper_channel. However, the lack of a clear transmission channel from commodities to Indian markets, aside from the dyn_adanient_bo, which has already reacted, limits the potential for a significant impact.
- **Gap**: No gap: the big raw move in commodities is largely unexplained by factors, but the resid_z values, while high, do not necessarily imply an anomaly given the magnitude of the move
- **India take**: The Indian instrument dyn_adanient_bo has already reacted to the move in soybeans, and further transmission to Indian metal equities may occur through the metal_copper_channel. However, the impact is likely to be limited.
- Watch next: dyn_adanient_bo (down) — already moved; reacted to soybeans
- **India receivers**: dyn_adanient_bo (rho -0.374, z -1.42)
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-20 (d=0.16), 2025-04-03 (d=0.17)

### [AMBER 3.98] nikkei_225 ↓
- nikkei_225 [INDICES]: last 64604.84, z20 -1.98, zc -1.49, resid-z -1.36 [quiet], 1d -2.74%, |z20|=1.98
- **Mechanism**: nikkei_225 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_hdbfs_bo (rho 0.463 via nikkei_225, z -2.88, reacted); nifty_metal (rho 0.443 via nikkei_225, z -1.61, reacted)
- **India receivers**: dyn_hdbfs_bo (rho 0.463, z -2.88); nifty_metal (rho 0.443, z -1.61)
- Source: Japan's Nikkei falls more than 2% on AI spending worries — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-falls-more-than-2-on-ai-spending-worries/articleshow/132594822.cms
- Source: Japan's Nikkei rises as chip shares gain, BOJ's rate hike prospects weigh — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-rises-as-chip-shares-gain-bojs-rate-hike-prospects-weigh/articleshow/132572655.cms
- Source: Asian stocks today: Kospi, Nikkei surge up to 4% as semiconductor stocks rally; SK Hynix, Samsung lead — Mint Markets, 2026-07-23. https://www.livemint.com/market/stock-market-news/asian-stocks-today-kospi-nikkei-surge-up-to-4-as-semiconductor-stocks-rally-sk-hynix-samsung-lead-11784770474517.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-21 (d=0.23), 2026-06-11 (d=0.6)

## Watchlist (below surfacing floor)
dyn_hdb ↓ (3.98), nifty_50 ↓ (3.94), dyn_bac ↑ (3.65), eur_usd ↓ (3.63), dyn_patanjali_ns ↓ (3.36), dyn_aapl ↑ (3.26), gold_silver_ratio ↑ (3.21), usd_inr ↑ (3.2), wheat ↑ (3.13), dyn_lth ↑ (3.05), dyn_nflx ↓ (2.94), dyn_icicigi_bo ↓ (2.9)

## India macro
- nifty_50: 23787.0000 (1d -0.35%, z20 -1.94, flag amber)
- nifty_midcap_100: 61682.1016 (1d -0.02%, z20 -1.28, flag none)
- usd_inr: 96.5520 (1d -0.01%, z20 1.20, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5931 (1d 0.33%, z20 0.44, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 86.1 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.9 — "How scrap is at the centre of India’s changing metals growth story"
- HDB (HDFC Bank Limited) score 68.4 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- BAC (Bank of America Corporation) score 68.3 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.3 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- IDBI.NS (IDBI BANK LIMITED) score 60.2 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 57.5 — "How scrap is at the centre of India’s changing metals growth story"
- COIN (Coinbase Global, Inc.) score 56.7 — "Trump's new global tariff draws rebukes from trade partners over forced labor justificatio"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.4 — "Market wrap: HCLTech, Bajaj Finance, Eternal among top gainers and losers on Nifty and Sen"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.7 — "Market wrap: HCLTech, Bajaj Finance, Eternal among top gainers and losers on Nifty and Sen"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.4 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- COALINDIA.NS (COAL INDIA LTD) score 38.7 — "How scrap is at the centre of India’s changing metals growth story"
- OHI (Omega Healthcare Investors, In) score 34.4 — "Kalind shares jump 5% on ex-bonus, ex-split day; investors see 86% price adjustment"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.3 — "India bonds end three-day losing streak but post second straight weekly decline"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.7 — "Juniper Green Energy to open Rs 1,800-cr IPO on July 30"
- CHKP (Check Point Software Technolog) score 22.5 — "Cube Highways Trust InvIT IPO Day 3: Issue subscribed 1.67x so far. Check GMP, issue detai"
- INFY (Infosys Limited) score 16.3 — "Infosys shares dip after Q1 results; brokerages trim target prices"
- LTH (Life Time Group Holdings, Inc.) score 15.8 — "Quote of the day by John Rogers: "All of us, all of the time, have to be on guard against "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.2 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.9 — "Kalind shares jump 5% on ex-bonus, ex-split day; investors see 86% price adjustment"
- VT (Vanguard Total World Stock Ind) score 11.3 — "The world is facing its largest oil shock ever. Here is why prices are not higher."
- JIOFIN.BO (Jio Financial Services Limited) score 10.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Financial Snapshot"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Financial Snapshot"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.2 — "ICICI Bank prices $1 billion debt in largest dollar issue by Indian private lender"
- META (Meta) score 8.2 — "How scrap is at the centre of India’s changing metals growth story"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.8 — "Q1 Results Today Highlights: Tata Consumer con. PAT up 28.4%, ACC PAT declines 61.5%, Shri"
- GS (Goldman Sachs Group, Inc. (The) score 7.8 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- MS (Morgan Stanley) score 7.3 — "Infosys shares fall 3% as JPMorgan downgrades stock, Jefferies cuts target after Q1 result"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.3 — "Sebi clears IPOs of Intellius Recode, Nityas Gems & Jewellery"
- ETERNAL.NS (ETERNAL LIMITED) score 6.2 — "Market wrap: HCLTech, Bajaj Finance, Eternal among top gainers and losers on Nifty and Sen"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 5.2 — "Q1 Results Today Live: Shriram Finance, TCP, BoB, Hindustan Zinc, ACC, Dalmia Bharat, Jind"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.5 — "Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it?"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.3 — "IEX Q1 results: Net profit grows 12% YoY to  ₹135 crore; electricity volumes rise 16%"
- NVDA (NVIDIA Corporation) score 4.0 — "AMD’s rivalry with Nvidia is increasingly moving into a new realm"
- AAPL (Apple Inc.) score 3.4 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- INDIGOPNTS.NS (INDIGO PAINTS LIMITED) score 3.4 — "IndiGo faces rough weather in Q1, hit by skyrocketing fuel prices"
- NFLX (Netflix, Inc.) score 3.2 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- WIT (Wipro Limited) score 1.9 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.0 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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