# Transmission Layer — board brief · 2026-08-17 07:15Z

data as of **2026-08-17** · 98 series · 9 red / 37 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.137, 2d in regime; vol-pct 0.274, breadth-off 0.0, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.86, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.29, corr60 0.35, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.2, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.17, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.761345828718788e-08)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2423) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.37] cross-asset · 14 series ↑
- russell_2000 [INDICES]: last 3068.24, z20 1.99, zc 0.43, resid-z 1.16 [quiet], 1d 0.50%, |z20|=1.99; 1y-pct=100
- comex_gold [COMMODITIES]: last 4458.70, z20 1.98, zc 1.38, resid-z -0.69 [quiet], 1d 1.79%, |z20|=1.98; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.97, z20 1.77, zc 0.68, resid-z -0.19 [quiet], 1d 1.52%, |z20|=1.77; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.71, z20 1.62, zc 0.76, resid-z 0.00 [quiet], 1d 1.69%, |z20|=1.62; 1y-pct=100
- dyn_vt [EQUITIES]: last 162.24, z20 1.56, zc -0.11, resid-z -0.85 [quiet], 1d -0.09%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 225.16, z20 1.55, zc -0.03, resid-z -0.34 [quiet], 1d -0.06%, 1y-pct=98
- vix [INDICES]: last 14.25, z20 -1.54, zc -0.34, resid-z n/a [quiet], 1d -2.60%, |z20|=1.54; 1y-pct=2
- nasdaq_100 [INDICES]: last 30050.44, z20 1.53, zc -0.09, resid-z 0.20 [quiet], 1d -0.11%, |z20|=1.53; 1y-pct=95
- sp500 [INDICES]: last 7786.01, z20 1.42, zc -0.21, resid-z 0.78 [quiet], 1d -0.17%, 1y-pct=99
- dax [INDICES]: last 26440.31, z20 1.36, zc 0.75, resid-z 0.65 [quiet], 1d 0.53%, 1y-pct=100
- stoxx_50 [INDICES]: last 6539.59, z20 1.29, zc -0.12, resid-z -0.09 [quiet], 1d -0.09%, 1y-pct=99
- gold_silver_ratio [DERIVED]: last 67.58, z20 -1.20, zc n/a, resid-z n/a [quiet], 1d 0.26%, GSR<75 (extreme low)
- dow_jones [INDICES]: last 53733.51, z20 0.88, zc -0.27, resid-z -0.15 [quiet], 1d -0.20%, 1y-pct=96
- cac_40 [INDICES]: last 8636.80, z20 0.74, zc -0.22, resid-z -0.29 [quiet], 1d -0.16%, 1y-pct=96
- **Mechanism**: The recent move in gold and silver prices is driven by a weaker US dollar and easing expectations of a US Fed interest rate hike in September. The gold-silver co-move channel is valid, with a correlation of 0.88 over the past 20 days, indicating that monetary metals are moving together. The vix_equity_inverse channel is also valid, with a correlation of -0.72, suggesting that volatility spikes are leading to equity drawdowns.
- **Gap**: No gap: the move in gold and silver prices is largely priced in, with resid_z values of -0.69 and -0.19, respectively, indicating that the moves are largely explained by factor exposures.
- **India take**: The Indian metal sector, as represented by the nifty_metal index, may react positively to the move in global metal prices, particularly comex_silver. However, the reaction is yet to be seen.
- Watch next: comex_gold (up) — already moved; weaker US dollar and stalled US-Iran talks
- Watch next: comex_silver (up) — already moved; co-movement with gold
- Watch next: nifty_metal (up) — not yet - watch; correlation with comex_silver
- **India receivers**: nifty_metal (rho 0.513, z 0.64); nifty_midcap_100 (rho 0.498, z 0.88); nifty_fmcg (rho -0.493, z -2.63); nifty_50 (rho 0.489, z -0.07)
- Source: Gold Rate Today, Aug 17: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-17-2026/article71355125.ece
- Source: Gold and silver prices rise on MCX on a weaker dollar; US-Iran stalled talks cap gains — Mint Markets, 2026-08-17. https://www.livemint.com/market/commodities/gold-and-silver-prices-rise-on-mcx-on-a-weaker-dollar-us-iran-stalled-talks-cap-gains-11786938089811.html
- Source: Gold Rises to Near $4,400 as Weak Retail Data Weighs on Dollar — Mint Markets, 2026-08-17. https://www.livemint.com/market/gold-rises-to-near-4-400-as-weak-retail-data-weighs-on-dollar-11786937454532.html
- Historical analogues: 2024-11-26 (d=0.9), 2025-10-31 (d=0.97), 2025-10-24 (d=1.11)

### [RED 4.81] commodities · 2 series ↑
- corn [COMMODITIES]: last 485.25, z20 3.98, zc 4.47, resid-z 1.25 [moved], 1d 5.72%, |z20|=3.98; 1y-pct=100
- wheat [COMMODITIES]: last 688.75, z20 1.48, zc 1.07, resid-z 1.20 [quiet], 1d 2.07%, 1y-pct=99
- **Mechanism**: The recent surge in commodities, particularly corn and wheat, is driven by their own momentum, with corn's z20 level at 3.9249982985024037 and wheat's at 1.5256880801758035. This move is priced, given the relatively small resid_z values of 1.25 for corn and 1.2 for wheat, indicating that the current price levels are largely explained by factor exposures. The VALID metal_copper_channel and VALID gold_silver_comove channels suggest that the momentum in commodities may continue, potentially influencing Indian metal equities and monetary metals.
- **Gap**: No gap: the current price levels of corn and wheat are largely explained by their factor exposures, with small resid_z values indicating that the move is priced.
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted, with a rho of 0.397 via wheat, and the VALID metal_copper_channel suggests that Indian metal equities may follow the momentum in commodities.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.389, z 2.29)
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.78] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.78, zc n/a, resid-z n/a [quiet], 1d 0.17%, 52-wk extreme (pct=99); |z20|=1.78; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.77, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown, but the midcap_largecap_ratio's move may not be an anomaly.
- **Gap**: No gap: the midcap_largecap_ratio's move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index, which has a correlation of 0.531 with the midcap_largecap_ratio, has not yet reacted and is a potential responder. Other Indian transmission candidates like Dyn Bharatcoal NS and Dyn Fincables NS have already reacted.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.533, z 0.88); dyn_bharatcoal_ns (rho 0.421, z -1.32); dyn_fincables_ns (rho 0.398, z 2.72); dyn_pcjeweller_ns (rho 0.37, z 0.31)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.55] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 2.89, zc 1.89, resid-z 0.17 [moved], 1d 0.83%, |z20|=2.89
- usd_mxn [FX]: last 17.01, z20 -1.93, zc -0.30, resid-z -0.39 [quiet], 1d -0.11%, |z20|=1.93; 1y-pct=0
- gbp_usd [FX]: last 1.36, z20 1.86, zc 1.19, resid-z -0.16 [quiet], 1d 0.49%, |z20|=1.86
- eur_usd [FX]: last 1.16, z20 1.78, zc 1.68, resid-z 0.03 [moved], 1d 0.56%, |z20|=1.78
- **Mechanism**: The recent move in FX markets, particularly in AUD/USD, GBP/USD, and EUR/USD, is driven by a risk-on sentiment, as indicated by the RISK_ON regime. The move is largely priced, with small resid_z values, suggesting that the market has already accounted for the factor exposures. The VALID vix_equity_inverse channel suggests that the low vol spike is consistent with the equity drawdown, while the VALID gold_silver_comove channel indicates that monetary metals are co-moving, but these channels do not directly drive the FX move.
- **Gap**: No gap: the move is largely priced, with small resid_z values, and the market has already accounted for the factor exposures.
- **India take**: The Indian instruments that express this move are eur_inr, which has already reacted, and dyn_icicigi_bo, which remains quiet. The reaction in eur_inr suggests that the Indian market is already pricing in the FX move.
- Watch next: AUD/USD (up) — already moved; High z20 level
- Watch next: GBP/USD (up) — not yet - watch; Positive z20 level
- **India receivers**: dyn_muthootfin_ns (rho -0.552, z -1.05); eur_inr (rho 0.482, z 3.49); dyn_icicigi_bo (rho -0.423, z -0.66)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.39] dxy ↓
- dxy [FX]: last 99.43, z20 -1.39, zc -0.74, resid-z 0.10 [quiet], 1d -0.25%, 20d range extreme
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the metal_copper_channel, a VALID channel, potentially leading to a move in Indian metal equities. The DXY decline, although priced with a small resid_z of 0.1, could still influence global copper prices, which in turn affect Indian metal equities. The VALID gold_silver_comove channel also suggests that monetary metals may co-move, potentially impacting the Indian market.
- **Gap**: No gap: The DXY move is priced with a small resid_z of 0.1, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is likely to be the Indian metal equities, such as Hindalco or Tata Steel, which may react to the potential move in global copper prices. However, the reaction has not occurred yet.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in comex_gold 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.07] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.42, z20 2.07, zc 0.15, resid-z -0.38 [quiet], 1d 0.35%, |z20|=2.07; 1y-pct=100
- **Mechanism**: The recent move in dyn_tech is driven by a shift in investor sentiment, as evident from Tiger Global's portfolio reshuffling, with a focus on semiconductor exposure and emerging technology opportunities. This shift is likely to propagate through the VALID metal_copper_channel, given the historical correlation between global copper prices and Indian metal equities. The RISK_ON regime and the VALID vix_equity_inverse channel also support this move, as investors seek higher returns in a low-volatility environment.
- **Gap**: No gap: the move in dyn_tech is largely priced, with a small resid_z of -0.38, indicating that the current price reflects the factor exposures and the recent shift in investor sentiment.
- **India take**: The Indian instrument that expresses this move is dyn_inoxindia_ns, which has not yet reacted to the shift in investor sentiment. Given the rho of -0.392, a potential upside move in dyn_inoxindia_ns can be expected.
- Watch next: dyn_inoxindia_ns (up) — not yet - watch; rho=-0.392 via dyn_tech
- **India receivers**: dyn_inoxindia_ns (rho -0.392, z -0.06)
- Source: US Stock Market: Tiger Global trims big tech bets, adds AMD and SpaceX in Q2 — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-tiger-global-trims-big-tech-bets-adds-amd-and-spacex-in-q2/articleshow/133286709.cms
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra News — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-17-aug-2026/liveblog/133286151.cms
- Source: Why Goldman Sachs thinks there may be an ‘earnings bubble’ in tech? — BusinessLine Mkts, 2026-08-16. https://www.thehindubusinessline.com/markets/why-goldman-sachs-thinks-there-may-be-an-earnings-bubble-in-tech/article71352404.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.78] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.49, z20 1.78, zc 0.43, resid-z -1.09 [quiet], 1d 0.62%, 1y-pct=99
- **Mechanism**: The recent increase in dyn_bac is driven by its historical correlation with global equities, particularly dow_jones and cac_40, which have not yet moved in tandem. The RISK_ON regime and VALID vix_equity_inverse channel suggest a potential for further equity upside, which could propagate to dyn_bac. However, the quiet move in dyn_bac with a low resid_z of -1.09 indicates that the current price move is largely explained by factor exposures and may not be an anomaly.
- **Gap**: No gap: the current price move in dyn_bac is largely explained by factor exposures, as indicated by a low resid_z of -1.09 and a high r2 of 0.107.
- **India take**: The Indian instrument dyn_cupid_ns has already reacted to the move in dyn_bac, given its correlation of 0.374. Further upside in global equities could lead to additional gains in dyn_cupid_ns.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.374, z 1.62)
- Source: Just 7% of America’s Nuclear Fuel Comes From Home — OilPrice, 2026-08-15. https://oilprice.com/Alternative-Energy/Nuclear-Power/Just-7-of-Americas-Nuclear-Fuel-Comes-From-Home.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 3.49] eur_inr ↑
- eur_inr [FX]: last 110.86, z20 3.49, zc 1.43, resid-z 0.22 [quiet], 1d 0.79%, |z20|=3.49
- **Mechanism**: eur_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho 0.361 via eur_inr, z -0.27, quiet)
- **India receivers**: usd_inr (rho 0.361, z -0.27)
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-08 (d=0.0), 2025-08-26 (d=0.0)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↑ (3.45), dyn_tatatech_ns ↑ (3.16), dyn_coin ↓ (2.95), indices · 2 series ↑ (2.94), dyn_fincables_ns ↑ (2.72), dyn_icicigi_bo ↓ (2.66), nifty_fmcg ↓ (2.63), usd_brl ↑ (2.58), dyn_lenskart_ns ↑ (2.29), dyn_idbi_ns ↓ (2.23), bovespa ↓ (2.17), usd_cny ↓ (1.82)

## India macro
- nifty_50: 24303.1992 (1d -0.26%, z20 -0.07, flag none)
- nifty_midcap_100: 63723.8008 (1d -0.09%, z20 0.88, flag amber)
- usd_inr: 95.5975 (1d 0.21%, z20 -0.27, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6220 (1d 0.17%, z20 1.78, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 80.5 — "Coal India Share Price Live Updates: Coal India  Price Movement"
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.0 — "Coal India Share Price Live Updates: Coal India  Price Movement"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.8 — "Coal India Share Price Live Updates: Coal India  Price Movement"
- INDIANB.NS (INDIAN BANK) score 54.6 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- BAC (Bank of America Corporation) score 38.5 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- CHKP (Check Point Software Technolog) score 37.6 — "Horizon Industrial Parks’ Rs 2,600 crore IPO opens. Check GMP, price band and other key de"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.0 — "JANE STREET TAKES $15 BILLION JULY HIT Jane Street lost about $15 billion in July as the A"
- COIN (Coinbase Global, Inc.) score 36.1 — "US Stock Market: Tiger Global trims big tech bets, adds AMD and SpaceX in Q2"
- OHI (Omega Healthcare Investors, In) score 35.5 — "How India's digital infrastructure opened global markets to Indian investors"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.3 — "JANE STREET TAKES $15 BILLION JULY HIT Jane Street lost about $15 billion in July as the A"
- TECH (Bio-Techne Corp) score 35.0 — "JANE STREET TAKES $15 BILLION JULY HIT Jane Street lost about $15 billion in July as the A"
- HDB (HDFC Bank Limited) score 32.7 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- IDBI.NS (IDBI BANK LIMITED) score 30.3 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 30.3 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 30.2 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- LTH (Life Time Group Holdings, Inc.) score 23.3 — "India bonds dip as RBI's diaspora swap move dents sentiment"
- 301077.SZ (CHINASTARS) score 21.1 — "Global Market: China, Hong Kong stocks rise as chipmakers rally on strong earnings"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.7 — "Tata Steel Share Price Live Updates: Tata Steel's Current Market Position"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.5 — "India bonds dip as RBI's diaspora swap move dents sentiment"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.6 — "Tata Steel Share Price Live Updates: Tata Steel's Current Market Position"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.0 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- JIOFIN.BO (Jio Financial Services Limited) score 13.9 — "Tata Consumer Share Price Live Updates: Tata Consumer's Financial Snapshot"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.3 — "Coal India Share Price Live Updates: Coal India  Price Movement"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.7 — "Tata Consumer Share Price Live Updates: Tata Consumer's Financial Snapshot"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.7 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "Just 7% of America’s Nuclear Fuel Comes From Home"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.7 — "Lalithaa Jewellery Mart IPO: Issue booked 24% so far. GMP hints 15% listing pop.  Apply or"
- MS (Morgan Stanley) score 6.9 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.8 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.2 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ News"
- NVDA (NVIDIA Corporation) score 6.0 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- META (Meta) score 5.1 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- RDDT (Reddit, Inc.) score 3.2 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- AAPL (Apple Inc.) score 3.1 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 3.0 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.4 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.3 — "ICICI Bank Share Price Live Updates: ICICI Bank's Market Movement Today"
- CRWV (CoreWeave, Inc.) score 1.0 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 1.0 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.9 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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