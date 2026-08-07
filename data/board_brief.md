# Transmission Layer — board brief · 2026-08-07 22:04Z

data as of **2026-08-07** · 98 series · 11 red / 30 amber · 8 events surfaced (14 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.355, 4d in regime; vol-pct 0.415, breadth-off 0.294, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.4, contra nifty_50 corr20=0.07, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.38, corr60 0.33, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.05, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.03, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.23, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.18, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.0005401753879268334)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.572, β -0.4432, p 0.0); driver zc -1.61 → expected 0.78%. Type hit-rate 0.833 (n=2380).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.397, β 0.2393, p 0.0); driver zc -1.61 → expected -0.421%. Type hit-rate 0.833 (n=2380).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.364, β -0.2255, p 0.0); driver zc -1.61 → expected 0.397%. Type hit-rate 0.833 (n=2380).
- Track record · residual_reversion: hit-rate **0.495** (n=1164) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.833** (n=2380) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.88] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4401.30, z20 4.80, zc 1.99, resid-z 0.24 [priced], 1d 3.76%, |z20|=4.80; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 63.80, z20 3.38, zc 1.43, resid-z -1.23 [quiet], 1d 3.84%, |z20|=3.38; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6528.94, z20 2.46, zc 0.47, resid-z -0.16 [quiet], 1d 0.41%, |z20|=2.46; 1y-pct=100
- dyn_vt [EQUITIES]: last 161.29, z20 2.41, zc 0.86, resid-z 1.02 [quiet], 1d 0.86%, |z20|=2.41; 1y-pct=100
- dyn_nvda [EQUITIES]: last 223.98, z20 2.37, zc 0.88, resid-z -0.17 [quiet], 1d 2.28%, |z20|=2.37; 1y-pct=98
- cac_40 [INDICES]: last 8724.97, z20 2.33, zc 0.38, resid-z -0.14 [quiet], 1d 0.29%, |z20|=2.33; 1y-pct=100
- russell_2000 [INDICES]: last 3033.98, z20 2.28, zc 0.86, resid-z 0.82 [quiet], 1d 1.08%, |z20|=2.28; 1y-pct=99
- dax [INDICES]: last 26354.06, z20 2.22, zc 1.05, resid-z 0.38 [quiet], 1d 0.82%, |z20|=2.22; 1y-pct=100
- sp500 [INDICES]: last 7755.61, z20 2.18, zc 0.61, resid-z -0.45 [quiet], 1d 0.59%, |z20|=2.18; 1y-pct=100
- dow_jones [INDICES]: last 54029.50, z20 1.96, zc 0.27, resid-z -0.43 [quiet], 1d 0.27%, |z20|=1.96; 1y-pct=99
- vix [INDICES]: last 14.89, z20 -1.58, zc -0.21, resid-z n/a [quiet], 1d -1.72%, |z20|=1.58
- comex_copper [COMMODITIES]: last 6.59, z20 1.34, zc -0.68, resid-z -1.96 [unexplained], 1d -1.53%, 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.99, z20 -0.82, zc n/a, resid-z n/a [quiet], 1d -0.08%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold prices is driven by a decline in US rate hike expectations, following weak US jobs data. This has led to a decrease in real yields, making non-yielding gold more attractive. The gold-silver co-move channel is valid, and the metal copper channel also supports the move in gold and silver.
- **Gap**: No gap: the big raw move in gold is priced, given the significant decline in US rate hike expectations and the valid gold-silver co-move channel
- **India take**: The Indian instruments that express this move are Nifty Metal and Nifty Midcap 100, which have already reacted to the global cues. The Nifty 50 has also reacted, driven by its correlation with the CAC 40.
- Watch next: comex_gold (up) — already moved; US rate hike expectations have decreased
- **India receivers**: nifty_50 (rho 0.537, z 1.29); nifty_fmcg (rho -0.532, z 0.66); nifty_midcap_100 (rho 0.514, z 1.29); nifty_metal (rho 0.479, z 2.25)
- Source: The smart way to invest in gold right now as the dollar slips — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/the-smart-way-to-invest-in-gold-right-now-as-the-dollar-slips-22fdf3b2?mod=mw_rss_topstories
- Source: Two reasons why Nvidia’s stock saw its biggest weekly surge in more than a year — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/two-reasons-why-nvidias-stock-saw-its-biggest-weekly-surge-in-more-than-a-year-644875c8?mod=mw_rss_topstories
- Source: Gold hits seven-week high as weak US jobs data dents rate hike bets — Mint Markets, 2026-08-07. https://www.livemint.com/market/gold-hits-seven-week-high-as-weak-us-jobs-data-dents-rate-hike-bets-11786129243519.html
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [RED 6.76] fx · 3 series ↑
- usd_mxn [FX]: last 17.12, z20 -3.45, zc -1.59, resid-z -1.37 [moved], 1d -0.67%, |z20|=3.45; 1y-pct=0
- aud_usd [FX]: last 0.71, z20 2.29, zc 0.35, resid-z 0.49 [quiet], 1d 0.19%, |z20|=2.29
- eur_usd [FX]: last 1.16, z20 2.03, zc 0.11, resid-z -0.10 [quiet], 1d 0.04%, |z20|=2.03
- **Mechanism**: The recent weakness in US jobs data has led to a decline in the US dollar against major currencies, including the Mexican peso, Australian dollar, and euro. This move is largely priced, with the resid_z values indicating that the unexplained component is relatively small. The verified transmission setups, such as the bovespa index leading the aud_usd and usd_mxn, suggest that this move may propagate to other markets.
- **Gap**: No gap: the move in usd_mxn is largely priced, with a resid_z of -1.37, indicating that the unexplained component is relatively small
- **India take**: The Indian instrument that expresses this move is dyn_muthootfin_ns, which has already reacted with a z20 of -1.61. The weakness in the US dollar may lead to a decline in the US dollar against the Indian rupee, which could have a positive impact on Indian metal equities, given the valid metal_copper_channel.
- Watch next: usd_mxn (down) — already moved; weak US jobs data
- **India receivers**: dyn_muthootfin_ns (rho -0.557, z -1.61)
- Source: Dollar falls against yen, euro as weak US jobs data clouds Fed outlook — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dollar-falls-against-yen-euro-as-weak-us-jobs-data-clouds-fed-outlook/articleshow/133040262.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 5.33] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.22, z20 1.40, zc 1.21, resid-z 1.02 [quiet], 1d 0.97%, 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.03, zc 1.32, resid-z 0.90 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.43, z20 1.00, zc 0.51, resid-z -0.28 [quiet], 1d 0.83%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.76, z20 -0.40, zc 0.74, resid-z 0.28 [quiet], 1d 0.23%, 1y-pct=3
- ust_2y [RATES]: last 4.25, z20 0.25, zc 1.32, resid-z 0.95 [quiet], 1d 1.67%, 1y-pct=96
- **Mechanism**: The recent fall in US Treasury yields, triggered by a weaker-than-expected jobs report, has led to a decrease in interest rate expectations, causing a rally in equity markets. This move is largely priced, with resid_z values indicating that the majority of the move can be explained by factor exposures. However, the historically high correlation between US Treasury yields and Indian government bond yields may lead to a transmission of this move to the Indian market.
- **Gap**: No gap: The move in US Treasury yields is largely priced, with resid_z values indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian 10-year government bond yield may react to the decrease in US Treasury yields, potentially leading to a decrease in Indian bond yields. However, the INR_oil_channel is currently weak, which may limit the transmission of this move to the Indian market.
- Watch next: UST_10Y (down) — already moved; Interest rate expectations have decreased
- Source: Treasury yields fall as jobs report dashes hike bets — Mint Markets, 2026-08-07. https://www.livemint.com/market/treasury-yields-fall-as-jobs-report-dashes-hike-bets-11786130890731.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq jumps over 1% as Treasury yields, oil prices fall — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-peace-deal-crude-oil-fed-warsh-rate-hike-jobs-data-sandisk-cloudflare-atlassian-chip-stock-price-news-7th-august-2026/liveblog/133034022.cms
- Source: SELL AMERICA” TRADE RETURNS AS FED & YEN RISKS RISE Barclays says the “Sell America” trade is resurfacing, particularly across the dollar and US bond markets. Uncertainty over Fed policy, a potential yen carry-trade unwind and concerns over AI spending are driving volatility. — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34506
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.3] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 172.00, z20 3.30, zc 2.05, resid-z 0.09 [moved], 1d 10.31%, |z20|=3.30
- **Mechanism**: The recent surge in dyn_pltr is driven by its priced move, with a small resid_z of 0.09, indicating that the move is largely explained by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, suggest that the move may be related to broader market trends. However, the weak channels, including inr_oil_channel and dxy_inr_channel, may limit the transmission of this move to Indian markets.
- **Gap**: No gap: the move in dyn_pltr is largely priced, with a small resid_z of 0.09, indicating no significant event-to-price gap
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted to the move in dyn_pltr, with a rho of 0.398. Further moves in Indian metal equities may be influenced by the global copper channel.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.398 via dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.398, z 2.5)
- Source: Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/palantirs-stock-stages-best-week-since-2024-showing-its-no-longer-an-ai-loser-2fc6c32b?mod=mw_rss_topstories
- Source: Palantir’s stock stages best week since 2024, showing it’s no longer an AI loser — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/palantirs-stock-stages-best-week-since-2024-showing-its-no-longer-an-ai-loser-2fc6c32b?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 4.85] dxy ↓
- dxy [FX]: last 99.60, z20 -1.85, zc -1.04, resid-z 0.76 [quiet], 1d -0.37%, 20d range extreme; |z20|=1.85
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a move in monetary metals. However, the INVERTED safe_haven_gold channel suggests that the usual risk-off safe-haven bid for gold may not be present. The VALID metal_copper_channel could also play a role, as global copper leads Indian metal equities.
- **Gap**: No gap: The big raw move in DXY has a small resid_z of -0.92, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is likely to be the MCX Gold or MCX Copper, but the weak dxy_inr_channel and inr_oil_channel suggest that the transmission to Indian markets may be limited. The metal_copper_channel, however, could lead to a move in Indian metal equities.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in Comex gold prices 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.65] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 262.94, z20 2.65, zc 0.03, resid-z -0.19 [quiet], 1d 0.13%, |z20|=2.65; 1y-pct=100
- **Mechanism**: The recent surge in dyn_cupid_ns can be attributed to the company's strong Q1 performance, with a 194% YoY jump in consolidated net profit, driven by healthy execution across its key operating segments. This move is priced, as indicated by the small resid_z of -0.11, suggesting that the market has already factored in the positive earnings report. The metal_copper_channel, which is currently valid, may also play a role in transmitting global economic trends to Indian metal equities, potentially influencing dyn_cupid_ns.
- **Gap**: No gap: The move in dyn_cupid_ns is priced, with a small resid_z of -0.11, indicating that the market has already factored in the positive earnings report.
- **India take**: The Nifty Midcap 100, which has a rho of 0.361 with dyn_cupid_ns, has already reacted to the move. Indian investors may look to other consumer wellness and personal care companies for potential upside, given the strong performance of Cupid Ltd.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.361 via dyn_cupid_ns
- **India receivers**: nifty_midcap_100 (rho 0.361, z 1.29)
- Source: Cupid net profit jumps 194% YoY to  ₹44 crore in Q1 as margins expand sharply; raises FY27 guidance — Mint Markets, 2026-08-07. https://www.livemint.com/market/stock-market-news/cupid-net-profit-jumps-194-yoy-to-rs-44-crore-in-q1-as-margins-expand-sharply-raises-fy27-guidance-11786119336545.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.62] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.74, z20 -1.79, zc 0.22, resid-z 0.24 [quiet], 1d 0.09%, |z20|=1.79
- dyn_amzn [EQUITIES]: last 274.44, z20 1.46, zc 0.46, resid-z -0.16 [quiet], 1d 0.80%, 1y-pct=98
- **Mechanism**: The recent weakness in the US dollar against the yen and euro, driven by weak US jobs data, has led to a quiet move in usd_jpy and dyn_amzn. The unexplained component of the move, as measured by resid_z, is relatively small, suggesting that the move is largely priced in. However, the historical analogues suggest a potential for further upside in dyn_amzn and usd_jpy.
- **Gap**: No gap: the move in usd_jpy and dyn_amzn is largely priced in, with small resid_z values
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_jpy, while dyn_cartrade_ns remains quiet. Further upside in dyn_amzn could potentially lead to a move in dyn_cartrade_ns.
- Watch next: dyn_amzn (up) — not yet - watch; historical analogue suggests potential for further upside
- **India receivers**: dyn_muthootfin_ns (rho -0.513, z -1.61); dyn_cartrade_ns (rho -0.351, z -0.09)
- Source: Dollar falls against yen, euro as weak US jobs data clouds Fed outlook — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dollar-falls-against-yen-euro-as-weak-us-jobs-data-clouds-fed-outlook/articleshow/133040262.cms
- Source: YEN JUMPS 1% AGAINST DOLLAR AFTER US JOBS DATA — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34513
- Source: SELL AMERICA” TRADE RETURNS AS FED & YEN RISKS RISE Barclays says the “Sell America” trade is resurfacing, particularly across the dollar and US bond markets. Uncertainty over Fed policy, a potential yen carry-trade unwind and concerns over AI spending are driving volatility. — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34506
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 4.5] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1484.00, z20 2.50, zc 0.65, resid-z 0.46 [quiet], 1d 2.12%, |z20|=2.50; 1y-pct=100
- **Mechanism**: The recent increase in mutual funds' stake in Ather Energy for the 5th straight quarter, coupled with the company's production facilities operating at full capacity and demand outpacing supply, suggests a potential bigger rally brewing. This move is likely priced, given the small resid_z of -0.55, indicating that the current price move is largely explained by factor exposures. The VALID metal_copper_channel may also play a role in transmitting global copper price movements to Indian metal equities, including Ather Energy.
- **Gap**: No gap: the current price move is largely explained by factor exposures, as indicated by the small resid_z of -0.55
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock, which has already reacted with a quiet move. Other Indian metal equities, such as those in the Nifty Metal index, may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential rally in Ather Energy may spill over to the broader Indian market
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
dyn_tech ↑ (3.81), dyn_bac ↑ (3.57), dyn_indianb_ns ↑ (3.2), usd_cny ↓ (2.9), dyn_icicigi_bo ↓ (2.47), dyn_indusindbk_bo ↑ (2.42), dyn_lth ↑ (2.41), asx_200 ↑ (2.32), nifty_metal ↑ (2.25), bovespa ↓ (2.09), corn ↑ (1.56), nifty_it ↑ (1.5)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 104.8 — "Indian govt asks sugar dealers to hold maximum 400 tonnes stock till Nov"
- COALINDIA.NS (COAL INDIA LTD) score 103.4 — "Indian govt asks sugar dealers to hold maximum 400 tonnes stock till Nov"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.9 — "Indian govt asks sugar dealers to hold maximum 400 tonnes stock till Nov"
- INDIANB.NS (INDIAN BANK) score 72.2 — "BOFA STICKS WITH FED HIKES DESPITE WEAK JOBS US payrolls fell 23,000 in July, with prior m"
- TECHM.NS (TECH MAHINDRA LIMITED) score 60.4 — "China Is Betting on Quantum Tech to Fix Its Power Grid"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 59.7 — "China Is Betting on Quantum Tech to Fix Its Power Grid"
- BAC (Bank of America Corporation) score 58.6 — "Are target date funds aggressive enough to give Americans retirement savings that last the"
- TECH (Bio-Techne Corp) score 56.9 — "China Is Betting on Quantum Tech to Fix Its Power Grid"
- OHI (Omega Healthcare Investors, In) score 53.7 — "Global Market: European shares rise as healthcare stocks offset geopolitical concerns; inv"
- COIN (Coinbase Global, Inc.) score 53.7 — "GLOBAL BOND INFLOWS SURGE AS EQUITY DEMAND COOLS Global bond funds attracted $23 billion t"
- HDB (HDFC Bank Limited) score 50.6 — "BOFA STICKS WITH FED HIKES DESPITE WEAK JOBS US payrolls fell 23,000 in July, with prior m"
- IDBI.NS (IDBI BANK LIMITED) score 49.1 — "BOFA STICKS WITH FED HIKES DESPITE WEAK JOBS US payrolls fell 23,000 in July, with prior m"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 49.1 — "BOFA STICKS WITH FED HIKES DESPITE WEAK JOBS US payrolls fell 23,000 in July, with prior m"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 48.1 — "BOFA STICKS WITH FED HIKES DESPITE WEAK JOBS US payrolls fell 23,000 in July, with prior m"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 45.6 — "Energy Affordability Trumps Climate in US Midterm Races"
- LTH (Life Time Group Holdings, Inc.) score 39.7 — "Are target date funds aggressive enough to give Americans retirement savings that last the"
- CHKP (Check Point Software Technolog) score 33.2 — "Sebi to cut routine checks by two-thirds, focus on high-risk players"
- 301077.SZ (CHINASTARS) score 30.9 — "China Is Betting on Quantum Tech to Fix Its Power Grid"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.7 — "US JOBS DATA COULD MAKE OR BREAK SEPTEMBER FED HIKE Bond traders are bracing for Friday’s "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.9 — "Top Gainers & Losers on 7 August: Bajaj Finance, Navin Fluorine, Trent, Tata Capital, Swig"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.2 — "SpaceX’s stock just had one of its best days ever — with the first lockup expiration now b"
- JIOFIN.BO (Jio Financial Services Limited) score 13.4 — "BSE Index Services launches BSE REITs Index. Here's everything you need to know"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.2 — "Top Gainers & Losers on 7 August: Bajaj Finance, Navin Fluorine, Trent, Tata Capital, Swig"
- MS (Morgan Stanley) score 12.9 — "AI frenzy spooks investors but JPMorgan CEO Jamie Dimon says spending boom likely to pay o"
- VT (Vanguard Total World Stock Ind) score 12.9 — "HASSETT: TAKE OUT GOVT WORKERS, WORLD CUP, JOBS ROSE 100,000"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.7 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.1 — "IT stocks lead Nifty gains as financials bleed; West Asia, crude oil weigh on mood"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.7 — "Adani Energy Solution QIP to raise ₹3,500 cr oversubscribed three times"
- PLTR (Palantir Technologies Inc.) score 7.2 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.7 — "ICICI Bank, Axis Bank tap dollar debt again in less than two months: Report"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.7 — "Coal India shares fall 4% weighed by weak operating performance"
- NVDA (NVIDIA Corporation) score 6.7 — "Two reasons why Nvidia’s stock saw its biggest weekly surge in more than a year"
- META (Meta) score 5.4 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- AMZN (Amazon.com, Inc.) score 5.2 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- GOOGL (Alphabet) score 4.6 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- MSFT (Microsoft Corporation) score 4.3 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- AAPL (Apple Inc.) score 3.9 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- SNDK (Sandisk Corporation) score 3.7 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
- INFY (Infosys Limited) score 3.5 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
- CUPID.NS (CUPID LIMITED) score 1.2 — "Cupid net profit jumps 194% YoY to  ₹44 crore in Q1 as margins expand sharply; raises FY27"

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