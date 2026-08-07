# Transmission Layer — board brief · 2026-08-07 15:09Z

data as of **2026-08-07** · 98 series · 12 red / 30 amber · 8 events surfaced (16 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.355, 1d in regime; vol-pct 0.415, breadth-off 0.294, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.4, contra nifty_50 corr20=0.07, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.38, corr60 0.33, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.04, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.03, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.18, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.00011338702506846765)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1163) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.833** (n=2380) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.91] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4403.40, z20 4.83, zc 2.02, resid-z 2.33 [unexplained], 1d 3.80%, |z20|=4.83; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 63.61, z20 3.26, zc 1.31, resid-z -1.43 [quiet], 1d 3.53%, |z20|=3.26; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6537.82, z20 2.56, zc 0.63, resid-z 0.18 [quiet], 1d 0.54%, |z20|=2.56; 1y-pct=100
- cac_40 [INDICES]: last 8732.80, z20 2.39, zc 0.50, resid-z 0.18 [quiet], 1d 0.38%, |z20|=2.39; 1y-pct=100
- dyn_nvda [EQUITIES]: last 223.64, z20 2.33, zc 0.82, resid-z 2.23 [unexplained], 1d 2.12%, |z20|=2.33; 1y-pct=98
- dyn_vt [EQUITIES]: last 161.08, z20 2.31, zc 0.73, resid-z -0.25 [quiet], 1d 0.72%, |z20|=2.31; 1y-pct=100
- dax [INDICES]: last 26387.83, z20 2.29, zc 1.22, resid-z 0.64 [quiet], 1d 0.95%, |z20|=2.29; 1y-pct=100
- sp500 [INDICES]: last 7751.83, z20 2.15, zc 0.56, resid-z -1.21 [quiet], 1d 0.54%, |z20|=2.15; 1y-pct=100
- dow_jones [INDICES]: last 54010.92, z20 1.93, zc 0.23, resid-z -0.27 [quiet], 1d 0.23%, |z20|=1.93; 1y-pct=99
- russell_2000 [INDICES]: last 3023.33, z20 1.93, zc 0.58, resid-z 0.41 [quiet], 1d 0.73%, |z20|=1.93; 1y-pct=99
- vix [INDICES]: last 14.95, z20 -1.54, zc -0.16, resid-z n/a [quiet], 1d -1.32%, |z20|=1.54
- comex_copper [COMMODITIES]: last 6.60, z20 1.43, zc -0.59, resid-z -1.75 [unexplained], 1d -1.32%, 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 69.22, z20 -0.55, zc n/a, resid-z n/a [quiet], 1d 0.26%, GSR<75 (extreme low)
- **Mechanism**: The recent move in gold and silver prices, along with the co-movement of monetary metals, suggests a potential safe-haven bid. However, the channel status indicates that the safe_haven_gold channel is INVERTED, and the real_rates_gold_inverse channel is WEAK, which may limit the upside for gold. The metal_copper_channel is VALID, which could support the move in copper and related metals. The vix_equity_inverse channel is also VALID, indicating a potential inverse relationship between volatility and equity prices.
- **Gap**: No gap: The big raw move in gold and silver prices is largely PRICED, with resid_z values indicating that the moves are largely explained by factor exposures.
- **India take**: The Indian instruments such as nifty_metal and nifty_50 have already reacted to the global moves, with nifty_metal showing a z20 value of 2.25. The nifty_fmcg, on the other hand, remains quiet with a z20 value of 0.66.
- Watch next: comex_gold (up) — unexplained; resid_z=2.33, indicating unexplained move
- Watch next: comex_silver (up) — quiet; resid_z=-1.43, indicating explained move
- Watch next: comex_copper (up) — unexplained; resid_z=-1.75, indicating unexplained move
- **India receivers**: nifty_50 (rho 0.535, z 1.29); nifty_fmcg (rho -0.533, z 0.66); nifty_midcap_100 (rho 0.513, z 1.29); nifty_metal (rho 0.479, z 2.25)
- Source: Keralam jewellers seek review of gold, silver import duty structure — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/gold/kerala-jewellers-seek-review-of-gold-silver-import-duty-structure/article71275849.ece
- Source: Silver futures decline to ₹2.17 lakh/kg — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/gold/silver-futures-decline-to-217-lakhkg/article71275702.ece
- Source: Wall Street: S&P 500, Nasdaq edge higher after jobs data — Mint Markets, 2026-08-07. https://www.livemint.com/market/stock-market-news/wall-street-s-p-500-nasdaq-edge-higher-after-jobs-data-11786110178723.html
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [RED 5.16] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 170.41, z20 3.16, zc 1.85, resid-z -0.06 [moved], 1d 9.29%, |z20|=3.16
- **Mechanism**: The recent surge in dyn_pltr is driven by its strong Q2 results, which saw a 93% increase in revenue. This move is priced, given the small resid_z of -0.06, indicating that the factor exposures have largely explained the move. The metal_copper_channel and gold_silver_comove channels are valid and may influence the propagation of this move, but the primary driver is the company's performance.
- **Gap**: No gap: the move in dyn_pltr is largely explained by its factor exposures, with a small resid_z of -0.06, indicating that the price move is priced in.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted, given its rho of 0.4 with dyn_pltr. Further moves in dyn_pltr may continue to influence dyn_atherenerg_ns.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.4 via dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.4, z 2.5)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 4.78] dxy ↓
- dxy [FX]: last 99.64, z20 -1.78, zc -0.93, resid-z -0.64 [quiet], 1d -0.33%, 20d range extreme; |z20|=1.78
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a move in monetary metals. However, the INVERTED safe_haven_gold channel suggests that the usual risk-off safe-haven bid for gold may not be present. The VALID metal_copper_channel could also play a role, as global copper leads Indian metal equities.
- **Gap**: No gap: The big raw move in DXY has a small resid_z of -0.92, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is likely to be the MCX Gold or MCX Copper, but the weak dxy_inr_channel and inr_oil_channel suggest that the transmission to Indian markets may be limited. The metal_copper_channel, however, could lead to a move in Indian metal equities.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in Comex gold prices 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.55] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.90, z20 -1.72, zc 0.45, resid-z 0.44 [quiet], 1d 0.19%, |z20|=1.72
- dyn_amzn [EQUITIES]: last 276.48, z20 1.58, zc 0.89, resid-z -0.83 [quiet], 1d 1.55%, 1y-pct=99
- **Mechanism**: The recent US jobs data and potential yen carry-trade unwind have led to a surge in the yen against the dollar, while concerns over AI spending and uncertainty over Fed policy have driven volatility in the US bond markets. This has resulted in a quiet move in usd_jpy and dyn_amzn, with the latter having a high z20 level but a low resid_z, indicating that the move is largely priced in.
- **Gap**: No gap: the move in usd_jpy and dyn_amzn is largely priced in, with resid_z values indicating that the unexplained component is relatively small.
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_jpy, while dyn_cartrade_ns remains quiet. The metal_copper_channel may also transmit the global copper leads to Indian metal equities.
- Watch next: dyn_googl (up) — not yet - watch; high correlation with dyn_amzn
- **India receivers**: dyn_muthootfin_ns (rho -0.512, z -1.61); dyn_cartrade_ns (rho -0.351, z -0.09)
- Source: YEN JUMPS 1% AGAINST DOLLAR AFTER US JOBS DATA — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34513
- Source: SELL AMERICA” TRADE RETURNS AS FED & YEN RISKS RISE Barclays says the “Sell America” trade is resurfacing, particularly across the dollar and US bond markets. Uncertainty over Fed policy, a potential yen carry-trade unwind and concerns over AI spending are driving volatility. — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34506
- Source: GOLDMAN: YEN INTERVENTION REINFORCES DOLLAR DOMINANCE Goldman Sachs says the latest US-Japan intervention to support the yen strengthens, rather than weakens, the dollar’s status as the world’s leading reserve currency. Washington’s intervention in EUR/JPY and Japan’s potential — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34504
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 4.5] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1484.00, z20 2.50, zc 0.65, resid-z 0.46 [quiet], 1d 2.12%, |z20|=2.50; 1y-pct=100
- **Mechanism**: The recent increase in mutual funds' stake in Ather Energy for the 5th straight quarter, coupled with the company's production facilities operating at full capacity and demand outpacing supply, suggests a potential bigger rally brewing. This move is likely priced, given the small resid_z of -0.55, indicating that the current price move is largely explained by factor exposures. The VALID metal_copper_channel may also play a role in transmitting global copper price movements to Indian metal equities, including Ather Energy.
- **Gap**: No gap: the current price move is largely explained by factor exposures, as indicated by the small resid_z of -0.55
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock, which has already reacted with a quiet move. Other Indian metal equities, such as those in the Nifty Metal index, may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential rally in Ather Energy may spill over to the broader Indian market
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 4.46] fx · 3 series ↑
- usd_mxn [FX]: last 17.14, z20 -3.14, zc -1.23, resid-z -1.08 [quiet], 1d -0.52%, |z20|=3.14; 1y-pct=1
- aud_usd [FX]: last 0.71, z20 2.03, zc 0.11, resid-z 0.26 [quiet], 1d 0.06%, |z20|=2.03
- eur_usd [FX]: last 1.16, z20 1.99, zc 0.05, resid-z -0.14 [quiet], 1d 0.02%, |z20|=1.99
- **Mechanism**: The recent surge in FX markets, particularly in usd_mxn, eur_usd, and aud_usd, is driven by priced moves with small resid_z values, indicating that the big raw moves are largely explained by factor exposures. The RISK_ON regime and VALID channels such as gold_silver_comove and metal_copper_channel suggest a risk-on environment with potential for further moves in metals and related equities.
- **Gap**: No gap: the moves in usd_mxn, eur_usd, and aud_usd are largely priced, with small resid_z values indicating that the big raw moves are explained by factor exposures.
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_mxn, given its high correlation. Further moves in metals and related equities may be expressed through Indian metal equities, which have not yet reacted.
- Watch next: usd_mxn (down) — already moved; high z20 level
- **India receivers**: dyn_muthootfin_ns (rho -0.563, z -1.61)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 4.32] cross-asset · 4 series ↑
- tips_10y_real [RATES]: last 2.41, z20 0.66, zc 0.25, resid-z 0.01 [quiet], 1d 0.42%, 1y-pct=96
- ust_30y [RATES]: last 5.17, z20 0.64, zc -0.24, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=97
- dyn_bond [EQUITIES]: last 90.71, z20 -0.58, zc 0.53, resid-z 0.00 [quiet], 1d 0.16%, 1y-pct=2
- ust_10y [RATES]: last 4.63, z20 0.07, zc 0.00, resid-z -0.28 [quiet], 1d 0.00%, 1y-pct=95
- **Mechanism**: The recent surge in global bond inflows and cooling equity demand may be driving the quiet moves in rates instruments, such as tips_10y_real and ust_30y. The 'Sell America' trade resurfacing and uncertainty over Fed policy are contributing to volatility in US bond markets. The correlation between monetary metals, as seen in the VALID gold_silver_comove channel, may also be influencing the moves in rates instruments.
- **Gap**: No gap: the big raw moves in rates instruments are largely priced, with small resid_z values indicating that the moves are explained by factor exposures.
- **India take**: The Indian 10-year government bond yield may react to the surge in global bond inflows and the 'Sell America' trade, potentially leading to a decrease in yields. However, the INR may not weaken significantly due to the WEAK inr_oil_channel and dxy_inr_channel.
- Watch next: tips_10y_real (down) — already moved; high 1y-pct of 96
- Watch next: ust_30y (down) — already moved; high 1y-pct of 97
- Source: SELL AMERICA” TRADE RETURNS AS FED & YEN RISKS RISE Barclays says the “Sell America” trade is resurfacing, particularly across the dollar and US bond markets. Uncertainty over Fed policy, a potential yen carry-trade unwind and concerns over AI spending are driving volatility. — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34506
- Source: US JOBS DATA COULD MAKE OR BREAK SEPTEMBER FED HIKE Bond traders are bracing for Friday’s US jobs report as markets price more than a 50% chance of a September Fed rate hike. Economists expect around 80,000 jobs were added in July. A strong report, particularly higher wage — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34502
- Source: GLOBAL BOND INFLOWS SURGE AS EQUITY DEMAND COOLS Global bond funds attracted $23 billion this week, driven by strong demand for US high-yield debt. US bond inflows jumped to $17.8 billion from $7.9 billion last week, while Canadian and eurozone government bonds also saw solid — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34498
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 3.63] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.25, z20 1.63, zc 0.20, resid-z -0.60 [quiet], 1d 0.48%, 1y-pct=100
- **Mechanism**: The recent move in dyn_tech is priced, with a small resid_z of -0.6, indicating that the move is largely explained by factor exposures. The valid vix_equity_inverse channel suggests that a vol spike could lead to an equity drawdown, but the current regime is neutral. The metal_copper_channel is also valid, but its connection to dyn_tech is not direct.
- **Gap**: No gap: the move in dyn_tech is largely priced, with a small resid_z
- **India take**: The Indian instrument dyn_inoxindia_ns has a negative rho with dyn_tech, but has not reacted yet. It may be expected to move down due to its correlation with dyn_tech.
- Watch next: dyn_inoxindia_ns (down) — quiet; negative rho with dyn_tech
- **India receivers**: dyn_inoxindia_ns (rho -0.402, z -0.0)
- Source: I’m an unemployed software developer who is skeptical of AI. Can I still find a job in tech? — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/im-an-unemployed-software-developer-who-is-skeptical-of-ai-can-i-still-find-a-job-in-tech-4413875e?mod=mw_rss_topstories
- Source: Q1 Results Today Live: SBI, Titan and Hindalco post Q1 profit growth, Ola Electric & BEML Q1 loss narrowed y-o-y, Hitachi Energy, PFC, Oil India, Kaynes Tech, Ramco Cements, Afcons Infra, Lemon Tree, Cello to announce Q1 results — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-sbi-titan-hindalco-power-finance-corporation-godrej-consumer-oil-india-nlc-kaynes-tech-ramco-cements-afcons-infra-lemon-tree-cello-hitachi-lic-trent-results-07-august-202/article71313123.ece
- Source: Q1 Results Today Live: SBI PAT rises 10.2%, BEML loss narrows in Q1, Godrej Consumer con. PAT up 11.5%, Titan, Hindalco, Hitachi Energy, PFC, Oil India, NLC, Kaynes Tech, Ramco Cements, Afcons Infra, Lemon Tree, Cello to announce Q1 results — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-sbi-titan-hindalco-power-finance-corporation-godrej-consumer-oil-india-nlc-kaynes-tech-ramco-cements-afcons-infra-lemon-tree-cello-hitachi-lic-trent-results-07-august-202/article71313123.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

## Watchlist (below surfacing floor)
dyn_bac ↑ (3.28), dyn_indianb_ns ↑ (3.2), usd_cny ↓ (3.19), dyn_coin ↓ (2.88), dyn_hdb ↓ (2.72), dyn_cupid_ns ↑ (2.65), dyn_icicigi_bo ↓ (2.47), dyn_indusindbk_bo ↑ (2.42), asx_200 ↑ (2.32), dyn_lth ↑ (2.29), nifty_metal ↑ (2.25), corn ↑ (1.87)

## India macro
- nifty_50: 24570.6504 (1d -0.27%, z20 1.29, flag none)
- nifty_midcap_100: 63462.0508 (1d 0.22%, z20 1.29, flag amber)
- usd_inr: 95.1980 (1d 0.13%, z20 -1.36, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5828 (1d 0.48%, z20 -0.59, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 109.9 — "First MD & CEO of India International Bullion Exchange in GIFT City resigns"
- COALINDIA.NS (COAL INDIA LTD) score 108.5 — "First MD & CEO of India International Bullion Exchange in GIFT City resigns"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 107.9 — "First MD & CEO of India International Bullion Exchange in GIFT City resigns"
- INDIANB.NS (INDIAN BANK) score 74.1 — "WARSH’S “QUIETER FED” PLAN RAISES WALL STREET CONCERNS Fed Chair Kevin Warsh is reportedly"
- TECHM.NS (TECH MAHINDRA LIMITED) score 62.5 — "Poonawalla Vision Fund invests ₹230 crore in Lohum Cleantech"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 61.7 — "Poonawalla Vision Fund invests ₹230 crore in Lohum Cleantech"
- TECH (Bio-Techne Corp) score 58.7 — "Poonawalla Vision Fund invests ₹230 crore in Lohum Cleantech"
- OHI (Omega Healthcare Investors, In) score 57.4 — "Global Market: European shares rise as healthcare stocks offset geopolitical concerns; inv"
- COIN (Coinbase Global, Inc.) score 57.4 — "GLOBAL BOND INFLOWS SURGE AS EQUITY DEMAND COOLS Global bond funds attracted $23 billion t"
- BAC (Bank of America Corporation) score 56.5 — "PRESIDENT TRUMP — FRIDAY SCHEDULE AUGUST 7, 2026 🔸 8:00 AM Executive Time 📍 White House 🔸 "
- HDB (HDFC Bank Limited) score 52.0 — "WARSH’S “QUIETER FED” PLAN RAISES WALL STREET CONCERNS Fed Chair Kevin Warsh is reportedly"
- IDBI.NS (IDBI BANK LIMITED) score 50.4 — "WARSH’S “QUIETER FED” PLAN RAISES WALL STREET CONCERNS Fed Chair Kevin Warsh is reportedly"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 50.4 — "WARSH’S “QUIETER FED” PLAN RAISES WALL STREET CONCERNS Fed Chair Kevin Warsh is reportedly"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 49.4 — "WARSH’S “QUIETER FED” PLAN RAISES WALL STREET CONCERNS Fed Chair Kevin Warsh is reportedly"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 45.7 — "GOLDMAN: YEN INTERVENTION REINFORCES DOLLAR DOMINANCE Goldman Sachs says the latest US-Jap"
- LTH (Life Time Group Holdings, Inc.) score 39.4 — "PRESIDENT TRUMP — FRIDAY SCHEDULE AUGUST 7, 2026 🔸 8:00 AM Executive Time 📍 White House 🔸 "
- CHKP (Check Point Software Technolog) score 34.4 — "Sebi cuts inspection load for market intermediaries, shifts focus to risk-based checks"
- 301077.SZ (CHINASTARS) score 31.9 — "South Korea’s KOSPI falls 11 % as China chip threat hits SK Hynix, Samsung"
- BOND (PIMCO Active Bond Exchange-Tra) score 31.8 — "US JOBS DATA COULD MAKE OR BREAK SEPTEMBER FED HIKE Bond traders are bracing for Friday’s "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.9 — "Top Gainers & Losers on 7 August: Bajaj Finance, Navin Fluorine, Trent, Tata Capital, Swig"
- JIOFIN.BO (Jio Financial Services Limited) score 14.4 — "BSE Index Services launches BSE REITs Index. Here's everything you need to know"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.2 — "US SHOCKS WITH 23,000 JOB LOSSES IN JULY The US economy unexpectedly lost 23,000 jobs in J"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.1 — "Top Gainers & Losers on 7 August: Bajaj Finance, Navin Fluorine, Trent, Tata Capital, Swig"
- MS (Morgan Stanley) score 13.8 — "AI frenzy spooks investors but JPMorgan CEO Jamie Dimon says spending boom likely to pay o"
- VT (Vanguard Total World Stock Ind) score 11.7 — "GOLDMAN: YEN INTERVENTION REINFORCES DOLLAR DOMINANCE Goldman Sachs says the latest US-Jap"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.5 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.7 — "IT stocks lead Nifty gains as financials bleed; West Asia, crude oil weigh on mood"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.3 — "Adani Energy Solution QIP to raise ₹3,500 cr oversubscribed three times"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.2 — "ICICI Bank, Axis Bank tap dollar debt again in less than two months: Report"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.2 — "Coal India shares fall 4% weighed by weak operating performance"
- NVDA (NVIDIA Corporation) score 6.1 — "NVDA - US REVIEWS CHINA’S OFFSHORE NVIDIA CHIP ACCESS AFTER AI GAINS"
- META (Meta) score 5.8 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- PLTR (Palantir Technologies Inc.) score 5.6 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 5.6 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- GOOGL (Alphabet) score 4.9 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- MSFT (Microsoft Corporation) score 4.6 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- AAPL (Apple Inc.) score 4.2 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- SNDK (Sandisk Corporation) score 4.0 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
- INFY (Infosys Limited) score 3.7 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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