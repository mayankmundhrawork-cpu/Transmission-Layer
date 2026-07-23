# Transmission Layer — board brief · 2026-07-23 11:27Z

data as of **2026-07-23** · 98 series · 6 red / 39 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.521, 13d in regime; vol-pct 0.626, breadth-off 0.417, Markov P(high-vol) 0.025)
- [WEAK] **safe_haven_gold** — corr20 -0.07, corr60 -0.44, contra nifty_50 corr20=0.07, last shift 2026-05-29. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.49, corr60 0.34, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.11, corr60 -0.05, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.81, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.1, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.27, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.34, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 6.607329525865069e-05)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.571, β -0.4456, p 0.0); driver zc 2.32 → expected -1.054%. Type hit-rate 0.819 (n=3034).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2388, p 0.0); driver zc 2.32 → expected 0.565%. Type hit-rate 0.819 (n=3034).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.358, β -0.2357, p 0.0); driver zc 2.32 → expected -0.558%. Type hit-rate 0.819 (n=3034).
- Track record · residual_reversion: hit-rate **0.493** (n=1165) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=3034) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.44] commodities · 2 series ↑
- wti [COMMODITIES]: last 90.54, z20 2.61, zc 1.72, resid-z 0.54 [moved], 1d 4.27%, 1-session move +4.27% ≥ 1.5%; |z20|=2.61
- brent [COMMODITIES]: last 92.89, z20 1.88, zc -0.47, resid-z 0.97 [quiet], 1d -1.25%, |z20|=1.88; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent surge in crude oil prices, driven by escalating tensions in West Asia, has led to a sharp jump in WTI and Brent prices, which in turn has negatively impacted the Indian stock market, with the Sensex and Nifty ending lower for the fourth straight session. The rise in oil prices has also put pressure on the Indian rupee, with investors taking short positions against it due to concerns about India's economic stability. The metal_copper_channel and gold_silver_comove channels are valid and may transmit the effects of the oil price surge to Indian metal equities and the broader market.
- **Gap**: No gap: the big raw move in oil prices has a relatively small resid_z, indicating that the move is largely priced in
- **India take**: The Indian stock market, particularly the Nifty Midcap 100 and Nifty 50, have already reacted to the surge in Brent prices, and further downside is possible. The metal_copper_channel may also transmit the effects of the oil price surge to Indian metal equities.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to Brent price surge
- Watch next: nifty_50 (down) — already moved; reacted to Brent price surge
- **India receivers**: nifty_midcap_100 (rho -0.64, z -1.35); nifty_50 (rho -0.494, z -1.55)
- Source: Sensex today | Stock Market Highlights: Markets slip for 4th straight day as crude rises; Sensex drops 363 pts, Nifty ends below 23,870 — BusinessLine Mkts, 2026-07-23. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-23rd-july-2026/article71253376.ece
- Source: Oil nears $100 a barrel after Houthis claim strikes on Saudi Arabian tankers — MarketWatch Top, 2026-07-23. https://www.marketwatch.com/story/oil-nears-100-a-barrel-after-houthis-claim-strikes-on-saudi-arabian-tankers-4d9949c2?mod=mw_rss_topstories
- Source: Rupee ends nearly flat as central bank intervention blunts oil strain — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-ends-nearly-flat-as-central-bank-intervention-blunts-oil-strain/articleshow/132577509.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.95] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.26, z20 2.01, zc 0.92, resid-z 1.09 [quiet], 1d 1.19%, |z20|=2.01; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.73, z20 -1.80, zc -0.82, resid-z -0.11 [quiet], 1d -0.24%, 1y-pct=0
- ust_10y [RATES]: last 4.63, z20 1.71, zc 0.67, resid-z 0.94 [quiet], 1d 0.65%, |z20|=1.71; 1y-pct=99
- tips_10y_real [RATES]: last 2.37, z20 1.58, zc 0.49, resid-z 0.64 [quiet], 1d 0.85%, |z20|=1.58; 1y-pct=100
- ust_30y [RATES]: last 5.13, z20 1.54, zc 0.61, resid-z 0.79 [quiet], 1d 0.39%, |z20|=1.54; 1y-pct=99
- **Mechanism**: The recent rise in US Treasury yields, driven by escalating Middle East tensions and higher oil prices, is putting pressure on Indian government bonds. This move is priced, as evidenced by the small resid_z values across the US Treasury yield curve. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may lead to rotations in Indian metal equities.
- **Gap**: No gap: the move in US Treasury yields is largely priced, with small resid_z values across the curve
- **India take**: Indian government bonds, such as the 10-year GoI bond, may come under pressure due to rising US Treasury yields and higher oil prices. ICICI Bank's planned dollar bond issuance may also be affected by these market conditions.
- Watch next: nifty_metal (down) — not yet - watch; Indian metal equities may react to global copper and monetary metal co-movement
- Source: Indonesia's Danantara plans dollar bond sale worth at least $500 mln, sources say — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/indonesias-danantara-plans-dollar-bond-sale-worth-at-least-500-mln-sources-say/articleshow/132573818.cms
- Source: Oil prices scorch Indian bonds; rising Treasury yields add to pressure — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/oil-prices-scorch-indian-bonds-rising-treasury-yields-add-to-pressure/articleshow/132572526.cms
- Source: ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/icici-bank-sets-initial-guidance-for-first-dollar-bond-in-nearly-9-years-bankers-say/articleshow/132571495.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.95] dyn_hdbfs_bo ↓
- dyn_hdbfs_bo [EQUITIES]: last 691.85, z20 -3.95, zc -1.22, resid-z -0.86 [quiet], 1d -2.16%, |z20|=3.95
- **Mechanism**: The recent decline in dyn_hdbfs_bo is largely priced, with a resid_z of -0.86, indicating that the move is mostly explained by factor exposures. The valid vix_equity_inverse channel suggests that the vol spike is likely to lead to an equity drawdown, which may propagate to Indian equities via transmission candidates such as nifty_midcap_100 and nifty_50.
- **Gap**: No gap: the move in dyn_hdbfs_bo is largely priced, with a small resid_z, indicating that the event is already reflected in the price
- **India take**: Indian instruments such as nifty_midcap_100 and nifty_50 have already reacted to the decline in dyn_hdbfs_bo, with z20 levels of -1.35 and -1.55, respectively. The usd_inr has also reacted, with a z20 level of 1.34.
- Watch next: nifty_midcap_100 (down) — already moved; reacted with z20=-1.35
- **India receivers**: nifty_midcap_100 (rho 0.571, z -1.35); nifty_50 (rho 0.422, z -1.55); dyn_eternal_ns (rho 0.409, z 0.54); usd_inr (rho -0.39, z 1.34)
- Source: HDB Financial to reissue 3-year bonds, bankers say — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/hdb-financial-to-reissue-3-year-bonds-bankers-say/articleshow/132537022.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.06), 2025-12-31 (d=0.06)

### [RED 4.92] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.19, z20 -2.92, zc -1.53, resid-z 0.29 [priced], 1d -2.28%, |z20|=2.92; 1y-pct=0
- **Mechanism**: The recent decline in HDFC Bank's shares, despite steady earnings growth, may be driven by concerns over net interest margin pressures and weaker operating profit. However, brokerages remain bullish, citing improving margins, healthy loan growth, and attractive valuations. The transmission_follow signal, with a historical hit-rate of 0.819, suggests that correlated instruments may follow the move in dyn_hdb.
- **Gap**: No gap: the decline in HDFC Bank's shares is largely priced in, with a resid_z of 0.29, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instruments, such as nifty_50 and nifty_midcap_100, have already reacted to the move in dyn_hdb, with a correlation of 0.663 and 0.529, respectively. The dyn_jiofin_bo has also reacted, with a correlation of 0.478.
- Watch next: nifty_50 (up) — already moved; reacted to dyn_hdb move
- **India receivers**: nifty_50 (rho 0.663, z -1.55); nifty_midcap_100 (rho 0.529, z -1.35); dyn_jiofin_bo (rho 0.478, z -1.62)
- Source: HDFC Bank shares slide 10% in four day after Q1 results but brokerages see up to 40% upside. Here’s why — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-slide-10-in-four-day-after-q1-results-but-brokerages-see-up-to-40-upside-heres-why/articleshow/132573294.cms
- Source: HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upside. Here’s why — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-slide-10-in-four-day-after-q1-results-but-brokerages-see-up-to-40-upside-heres-why/articleshow/132573294.cms
- Source: HDFC Bank shares tumble over 8% in three days on net interest margin concerns — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-tumble-over-8-in-three-days-on-net-interest-margin-concerns/article71253282.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.86] usd_jpy ↑
- usd_jpy [FX]: last 163.40, z20 2.86, zc 0.35, resid-z 0.36 [quiet], 1d 0.13%, |z20|=2.86; 1y-pct=100
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.518 vs usd_jpy, historically leads by 1d
- Source: US-Iran tensions underpin dollar as yen nears 40-year low — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/forex/forex-news/us-iran-tensions-underpin-dollar-as-yen-nears-40-year-low/articleshow/132570439.cms
- Source: Yen’s Slump in Trade-Weighted Gauge Shows Its Broad-Based Drop — Mint Markets, 2026-07-23. https://www.livemint.com/market/yens-slump-in-trade-weighted-gauge-shows-its-broad-based-drop-11784768496092.html
- Source: Yen Rebound Ebbs After Brief Rally on Outlook for BOJ Rate Hikes — Mint Markets, 2026-07-22. https://www.livemint.com/market/yen-rebound-ebbs-after-brief-rally-on-outlook-for-boj-rate-hikes-11784754197557.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 4.83] commodities · 3 series ↑
- corn [COMMODITIES]: last 488.75, z20 3.51, zc 4.60, resid-z 1.07 [moved], 1d 5.79%, |z20|=3.51; 1y-pct=100
- wheat [COMMODITIES]: last 707.50, z20 2.00, zc 0.11, resid-z 1.58 [unexplained], 1d 0.25%, |z20|=2.00; 1y-pct=100
- soybeans [COMMODITIES]: last 1243.75, z20 1.68, zc 0.86, resid-z 0.83 [quiet], 1d 0.87%, |z20|=1.68; 1y-pct=100
- **Mechanism**: The recent surge in commodity prices, particularly corn, wheat, and soybeans, is driven by a combination of factors, including supply and demand imbalances and market sentiment. The move is largely priced, with a significant portion of the price action explained by factor exposures. However, the unexplained component, as measured by resid_z, suggests that there may be some residual momentum that could drive further price action. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper prices may influence Indian metal equities.
- **Gap**: No gap: the move in commodity prices is largely priced, with a significant portion of the price action explained by factor exposures
- **India take**: The Indian instruments that express this move are dyn_patanjali_ns and dyn_tataelxsi_ns, which have already reacted to the surge in wheat prices, while dyn_adanient_bo remains quiet despite its exposure to soybeans
- Watch next: corn (up) — already moved; high z20 score and low resid_z indicate a priced move
- Watch next: wheat (up) — not yet - watch; unexplained move with high resid_z suggests potential for further price action
- Watch next: soybeans (up) — quiet; low z20 score and low resid_z indicate a quiet market
- **India receivers**: dyn_patanjali_ns (rho -0.515, z -1.64); dyn_adanient_bo (rho -0.388, z -1.73); dyn_tataelxsi_ns (rho -0.36, z -1.71)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.58] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 337.90, z20 2.58, zc -0.10, resid-z 0.35 [quiet], 1d -0.37%, |z20|=2.58; 1y-pct=99
- **Mechanism**: dyn_karurvysya_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.493 via dyn_karurvysya_ns, z 0.31, quiet); nifty_midcap_100 (rho 0.483 via dyn_karurvysya_ns, z -1.35, reacted); dyn_jiofin_bo (rho 0.472 via dyn_karurvysya_ns, z -1.62, reacted); nifty_50 (rho 0.464 via dyn_karurvysya_ns, z -1.55, reacted); dyn_havells_ns (rho 0.409 via dyn_karurvysya_ns, z 1.32, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.493, z 0.31); nifty_midcap_100 (rho 0.483, z -1.35); dyn_jiofin_bo (rho 0.472, z -1.62); nifty_50 (rho 0.464, z -1.55)
- Source: Broker’s Call: Karur Vysya Bank (Buy) — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/brokers-call-karur-vysya-bank-buy/article71248725.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [AMBER 4.19] dyn_bharatcoal_ns ↓
- dyn_bharatcoal_ns [EQUITIES]: last 34.80, z20 -2.19, zc -0.12, resid-z n/a [quiet], 1d -0.34%, |z20|=2.19
- **Mechanism**: dyn_bharatcoal_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Sotefin Bharat IPO listing: Shares hit upper circuit after listing at a 10% premium; details here — Mint Markets, 2026-07-23. https://www.livemint.com/market/ipo/sotefin-bharat-ipo-listing-shares-hit-upper-circuit-after-listing-at-a-10-premium-details-here-11784782273860.html
- Source: Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/sotefin-bharat-shares-set-for-bse-sme-debut-today-gmp-signals-muted-listing/articleshow/132571290.cms
- Source: Bharat Coking Coal shares fall 7% after Q1FY27 net loss — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/bharat-coking-coal-shares-fall-8-after-q1fy27-net-loss/article71252055.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-11 (d=0.3), 2026-07-03 (d=0.75)

## Watchlist (below surfacing floor)
dyn_qessf ↓ (4.18), comex_copper ↑ (4.14), dyn_ohi ↑ (3.92), dyn_icicigi_bo ↓ (3.58), nifty_50 ↓ (3.55), gold_silver_ratio ↑ (3.35), usd_inr ↑ (3.34), dyn_gs ↑ (3.01), dyn_lth ↑ (2.73), usd_cny ↓ (2.33), dyn_indusindbk_bo ↑ (2.31), usd_brl ↓ (2.21)

## India macro
- nifty_50: 23872.1992 (1d -0.52%, z20 -1.55, flag amber)
- nifty_midcap_100: 61695.6992 (1d -0.95%, z20 -1.35, flag none)
- usd_inr: 96.5725 (1d 0.24%, z20 1.34, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5844 (1d -0.43%, z20 -0.04, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 88.1 — "HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upsi"
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.5 — "India’s Solar Manufacturing Push Backfires as Panel Factories Shut Down"
- HDB (HDFC Bank Limited) score 71.7 — "HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upsi"
- BAC (Bank of America Corporation) score 68.8 — "HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upsi"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 68.6 — "HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upsi"
- IDBI.NS (IDBI BANK LIMITED) score 61.4 — "HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upsi"
- COIN (Coinbase Global, Inc.) score 53.3 — "Global Earnings | Hyundai Motor reports 21% drop in Q2 profit, misses forecasts"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 50.7 — "India’s Solar Manufacturing Push Backfires as Panel Factories Shut Down"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.5 — "Global Market: European shares slip as tech stocks drag; ECB policy decision in focus"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.6 — "Global Market: European shares slip as tech stocks drag; ECB policy decision in focus"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.2 — "HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upsi"
- OHI (Omega Healthcare Investors, In) score 30.1 — "Eternal’s investors can prepare for more positive earnings surprises"
- COALINDIA.NS (COAL INDIA LTD) score 24.6 — "India’s Solar Manufacturing Push Backfires as Panel Factories Shut Down"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.3 — "Indonesia's Danantara plans dollar bond sale worth at least $500 mln, sources say"
- CHKP (Check Point Software Technolog) score 22.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.1 — "Top Gainers & Losers on 23 July: SRF, IndusInd Bank, Adani Green Energy, HFCL, CarTrade Te"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 16.1 — "Adani Green share price falls 5% despite strong Q1 results - Should you buy the Adani Grou"
- VT (Vanguard Total World Stock Ind) score 11.9 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.7 — "Bonus bonanza! This textile player announced 1:1 bonus issue, dividend just 14 sessions af"
- GS (Goldman Sachs Group, Inc. (The) score 10.8 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- JIOFIN.BO (Jio Financial Services Limited) score 10.6 — "Oracle Financial Services shares jump 5% on strong Q1 results; PAT soars 121%, revenue up "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.4 — "Oracle Financial Services shares jump 5% on strong Q1 results; PAT soars 121%, revenue up "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.1 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- MS (Morgan Stanley) score 7.8 — "AI stocks are echoing a 1990s market split. JPMorgan warns the next few weeks are critical"
- LTH (Life Time Group Holdings, Inc.) score 7.0 — "NTPC Green shares soar 9% after Q1 earnings. What’s boosting investor sentiment?"
- META (Meta) score 6.5 — "The Metals Selloff Is Creating New Winners And Losers"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.0 — "Bluestone Jewellery shares rocket 36% in just three days after Q1 results. Can the momentu"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.0 — "Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.1 — "Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.9 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- ETERNAL.NS (ETERNAL LIMITED) score 4.8 — "Eternal’s investors can prepare for more positive earnings surprises"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.6 — "Tata Group stock Indian Hotels falls 1% despite strong Q1 results 2026. Should you buy or "
- NVDA (NVIDIA Corporation) score 4.4 — "AMD plans to invest to up $5 billion into Anthropic as it seeks to cut into Nvidia’s domin"
- INFY (Infosys Limited) score 4.0 — "Infosys Q1 Results Live Updates: Infosys Q1 profit rises 12% YoY to Rs 7,769 crore; revenu"
- NFLX (Netflix, Inc.) score 3.1 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- WIT (Wipro Limited) score 2.6 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 2.6 — "Dollar wavers as markets grapple with Gulf tensions"
- BIOCON.BO (BIOCON LTD.) score 0.6 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
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