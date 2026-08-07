# Transmission Layer — board brief · 2026-08-07 13:35Z

data as of **2026-08-07** · 98 series · 12 red / 30 amber · 8 events surfaced (17 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.333, 2d in regime; vol-pct 0.415, breadth-off 0.25, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.39, contra nifty_50 corr20=0.06, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.83, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.4, corr60 0.34, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.05, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.03, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.13, corr60 0.18, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 3.956591173648327e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1163) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.833** (n=2380) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.92] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4410.70, z20 4.93, zc 2.11, resid-z 2.33 [unexplained], 1d 3.98%, |z20|=4.93; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.45, z20 3.79, zc 1.82, resid-z -0.91 [priced], 1d 4.90%, |z20|=3.79; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6545.56, z20 2.65, zc 0.77, resid-z 0.20 [quiet], 1d 0.66%, |z20|=2.65; 1y-pct=100
- cac_40 [INDICES]: last 8735.25, z20 2.41, zc 0.54, resid-z -0.02 [quiet], 1d 0.41%, |z20|=2.41; 1y-pct=100
- dyn_vt [EQUITIES]: last 161.04, z20 2.29, zc 0.70, resid-z -0.25 [quiet], 1d 0.70%, |z20|=2.29; 1y-pct=100
- dax [INDICES]: last 26373.19, z20 2.26, zc 1.15, resid-z 0.45 [quiet], 1d 0.89%, |z20|=2.26; 1y-pct=100
- dyn_nvda [EQUITIES]: last 222.68, z20 2.20, zc 0.65, resid-z 2.23 [unexplained], 1d 1.69%, |z20|=2.20; 1y-pct=97
- sp500 [INDICES]: last 7739.39, z20 2.03, zc 0.39, resid-z -1.21 [quiet], 1d 0.38%, |z20|=2.03; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.64, z20 1.71, zc -0.32, resid-z -1.40 [quiet], 1d -0.72%, |z20|=1.71; 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 53831.04, z20 1.69, zc -0.10, resid-z -1.01 [quiet], 1d -0.10%, |z20|=1.69; 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.44, z20 -1.43, zc n/a, resid-z n/a [quiet], 1d -0.88%, GSR<75 (extreme low)
- russell_2000 [INDICES]: last 3001.55, z20 1.25, zc -0.45, resid-z -0.36 [quiet], 1d -0.58%, 1y-pct=96
- **Mechanism**: The recent surge in gold and silver prices, with COMEX gold and silver showing z20 levels of 4.93 and 3.79 respectively, is driving the current market move. The gold-silver comove channel is valid, with a correlation of 0.91 over the past 20 days, indicating a strong co-movement between the two metals. This move is also reflected in the Indian markets, with Nifty Metal reacting to the surge in COMEX silver.
- **Gap**: No gap: The big raw move in COMEX gold is priced, with a resid_z of 2.33, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument Nifty Metal has reacted to the surge in COMEX silver, with a z20 level of 2.25. Other Indian transmission candidates, such as Nifty 50 and Nifty Midcap 100, have also reacted to the global market move.
- Watch next: COMEX Gold (up) — already moved; High z20 level and valid gold-silver comove channel
- Watch next: Nifty Metal (up) — already moved; Reacted to surge in COMEX silver
- **India receivers**: nifty_fmcg (rho -0.535, z 0.66); nifty_50 (rho 0.534, z 1.29); nifty_midcap_100 (rho 0.514, z 1.29); nifty_metal (rho 0.478, z 2.25)
- Source: How S&P 500 options action may help explain the rising volatility in memory stocks — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/how-s-p-500-options-action-may-help-explain-volatility-in-memory-stocks-58d95beb?mod=mw_rss_topstories
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market futures climb after July jobs report; chip stocks rally — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-peace-deal-crude-oil-fed-warsh-rate-hike-jobs-data-sandisk-cloudflare-atlassian-chip-stock-price-news-7th-august-2026/liveblog/133034022.cms
- Source: Gold alone isn't enough for your daughter’s Streedhan. Wealth manager Aarti Gupta explains why — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/stocks/news/gold-alone-isnt-enough-for-your-daughters-streedhan-wealth-manager-aarti-gupta-explains-why/articleshow/133033944.cms
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [RED 5.07] dxy ↓
- dxy [FX]: last 99.47, z20 -2.07, zc -1.43, resid-z -0.64 [quiet], 1d -0.50%, 20d range extreme; |z20|=2.07
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a move in monetary metals. However, the INVERTED safe_haven_gold channel suggests that the usual risk-off safe-haven bid for gold may not be present. The VALID metal_copper_channel could also play a role, as global copper leads Indian metal equities.
- **Gap**: No gap: The big raw move in DXY has a small resid_z of -0.92, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is likely to be the MCX Gold or MCX Copper, but the weak dxy_inr_channel and inr_oil_channel suggest that the transmission to Indian markets may be limited. The metal_copper_channel, however, could lead to a move in Indian metal equities.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in Comex gold prices 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.7] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.57, z20 -1.87, zc -0.04, resid-z -0.01 [quiet], 1d -0.02%, |z20|=1.87
- dyn_amzn [EQUITIES]: last 276.40, z20 1.58, zc 0.87, resid-z -0.83 [quiet], 1d 1.52%, 1y-pct=99
- **Mechanism**: The recent USD/JPY intervention by Japan has led to a sharp move in the currency pair, with the yen appreciating significantly. This move has not been fully priced in by the market, as evidenced by the low resid_z values for USD/JPY and DYN_AMZN. The intervention has also led to a re-evaluation of risk assets, with DYN_AMZN showing a significant move. The metal_copper_channel and vix_equity_inverse channels are valid and may play a role in transmitting this move to Indian markets.
- **Gap**: No gap: the big raw move in USD/JPY has a small resid_z, indicating that the move is largely priced in
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the USD/JPY move, while dyn_cartrade_ns remains quiet. The metal_copper_channel may transmit the move to Indian metal equities.
- Watch next: dyn_muthootfin_ns (down) — already moved; reacted to USD/JPY move
- **India receivers**: dyn_muthootfin_ns (rho -0.513, z -1.61); dyn_cartrade_ns (rho -0.351, z -0.09)
- Source: Global Market: Japan reveals record $40 billion yen-buying intervention as currency pressure persists — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-reveals-record-40-billion-yen-buying-intervention-as-currency-pressure-persists/articleshow/133021238.cms
- Source: Yen Surrenders Nearly Half Its Gains from US-Japan Intervention — Mint Markets, 2026-08-07. https://www.livemint.com/market/yen-surrenders-nearly-half-its-gains-from-us-japan-intervention-11786062248662.html
- Source: Japan Carmakers See Yen Remaining Near Post-Intervention Levels — Mint Markets, 2026-08-06. https://www.livemint.com/market/japan-carmakers-see-yen-remaining-near-post-intervention-levels-11786051302266.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 4.63] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 164.03, z20 2.63, zc 1.04, resid-z -0.06 [quiet], 1d 5.20%, |z20|=2.63
- **Mechanism**: The recent surge in dyn_pltr is driven by its strong Q2 results, which have overshadowed controversy surrounding the company. The move is largely priced, given the small resid_z of -0.06, indicating that the market has already accounted for the factors driving the stock's performance. The VALID metal_copper_channel and gold_silver_comove channels suggest a broader market trend, but the specific drivers of dyn_pltr's move are more closely tied to its individual performance.
- **Gap**: No gap: the move in dyn_pltr is largely priced, with a small resid_z and a significant z20 level, indicating that the market has already accounted for the factors driving the stock's performance.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted, given its rho of 0.404 with dyn_pltr. Further moves in dyn_pltr may continue to influence dyn_atherenerg_ns, but the initial reaction has already occurred.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.404 via dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.402, z 2.5)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 4.56] fx · 3 series ↑
- usd_mxn [FX]: last 17.13, z20 -3.24, zc -1.34, resid-z -1.14 [quiet], 1d -0.57%, |z20|=3.24; 1y-pct=1
- eur_usd [FX]: last 1.16, z20 2.13, zc 0.23, resid-z -0.10 [quiet], 1d 0.09%, |z20|=2.13
- aud_usd [FX]: last 0.71, z20 2.12, zc 0.19, resid-z 0.34 [quiet], 1d 0.10%, |z20|=2.12
- **Mechanism**: The recent surge in FX markets, particularly in usd_mxn, eur_usd, and aud_usd, is driven by priced moves with small resid_z values, indicating that the big raw moves are largely explained by factor exposures. The RISK_ON regime and VALID channels such as gold_silver_comove and metal_copper_channel suggest a risk-on environment with potential for further moves in metals and related equities.
- **Gap**: No gap: the moves in usd_mxn, eur_usd, and aud_usd are largely priced, with small resid_z values indicating that the big raw moves are explained by factor exposures.
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_mxn, given its high correlation. Further moves in metals and related equities may be expressed through Indian metal equities, which have not yet reacted.
- Watch next: usd_mxn (down) — already moved; high z20 level
- **India receivers**: dyn_muthootfin_ns (rho -0.561, z -1.61)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [RED 4.5] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1484.00, z20 2.50, zc 0.65, resid-z 0.38 [quiet], 1d 2.12%, |z20|=2.50; 1y-pct=100
- **Mechanism**: The recent increase in mutual funds' stake in Ather Energy for the 5th straight quarter, coupled with the company's production facilities operating at full capacity and demand outpacing supply, suggests a potential bigger rally brewing. This move is likely priced, given the small resid_z of -0.55, indicating that the current price move is largely explained by factor exposures. The VALID metal_copper_channel may also play a role in transmitting global copper price movements to Indian metal equities, including Ather Energy.
- **Gap**: No gap: the current price move is largely explained by factor exposures, as indicated by the small resid_z of -0.55
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock, which has already reacted with a quiet move. Other Indian metal equities, such as those in the Nifty Metal index, may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential rally in Ather Energy may spill over to the broader Indian market
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.32] cross-asset · 4 series ↑
- tips_10y_real [RATES]: last 2.41, z20 0.66, zc 0.25, resid-z 0.01 [quiet], 1d 0.42%, 1y-pct=96
- ust_30y [RATES]: last 5.17, z20 0.64, zc -0.24, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=97
- dyn_bond [EQUITIES]: last 90.85, z20 -0.15, zc 1.05, resid-z 0.00 [quiet], 1d 0.32%, 1y-pct=4
- ust_10y [RATES]: last 4.63, z20 0.07, zc 0.00, resid-z -0.28 [quiet], 1d 0.00%, 1y-pct=95
- **Mechanism**: The recent surge in global bond inflows, driven by strong demand for US high-yield debt, has led to a decrease in bond yields, which is propagating through the valid gold_silver_comove and metal_copper_channel. However, the resid_z values for the affected series are relatively small, indicating that the move is largely priced in.
- **Gap**: No gap: the recent move in bond yields is largely priced in, as evidenced by the small resid_z values
- **India take**: The Indian 10-year government bond yield may react to the decrease in US bond yields, potentially leading to a decrease in Indian bond yields as well. However, the reaction has not occurred yet.
- Watch next: tips_10y_real (down) — already moved; real yields are decreasing due to bond inflows
- Source: GLOBAL BOND INFLOWS SURGE AS EQUITY DEMAND COOLS Global bond funds attracted $23 billion this week, driven by strong demand for US high-yield debt. US bond inflows jumped to $17.8 billion from $7.9 billion last week, while Canadian and eurozone government bonds also saw solid — DeItaone, 2026-08-07. https://t.me/walter_bloomberg/34498
- Source: There are good reasons why higher bond yields are here to stay, this strategist says — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/there-are-good-reasons-why-higher-bond-yields-are-here-to-stay-this-strategist-says-2a89d5ae?mod=mw_rss_topstories
- Source: There are good reasons higher bond yields are here to stay, this strategist says — MarketWatch Top, 2026-08-07. https://www.marketwatch.com/story/there-are-good-reasons-why-higher-bond-yields-are-here-to-stay-this-strategist-says-2a89d5ae?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.02] dyn_msft ↑
- dyn_msft [EQUITIES]: last 503.64, z20 2.02, zc 0.20, resid-z -0.53 [quiet], 1d 0.76%, |z20|=2.02
- **Mechanism**: dyn_msft ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billion in AI revenue from OpenAI in the year ended June, suggesting the ChatGPT maker accounts for more than half—and possibly around 70%—of its AI business. The figures highlight Microsoft's — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34422
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

## Watchlist (below surfacing floor)
dyn_indianb_ns ↑ (3.2), dyn_coin ↓ (3.16), usd_cny ↓ (3.13), dyn_tech ↑ (3.1), dyn_bac ↑ (2.9), dyn_hdb ↓ (2.77), dyn_cupid_ns ↑ (2.65), dyn_icicigi_bo ↓ (2.47), dyn_indusindbk_bo ↑ (2.42), asx_200 ↑ (2.32), dyn_lth ↓ (2.3), nifty_metal ↑ (2.25)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 107.5 — "India's Crude Oil Output Falls for Third Straight Year"
- COALINDIA.NS (COAL INDIA LTD) score 106.0 — "India's Crude Oil Output Falls for Third Straight Year"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 105.5 — "India's Crude Oil Output Falls for Third Straight Year"
- INDIANB.NS (INDIAN BANK) score 73.1 — "Fossil Group is said to invite banks for India unit IPO"
- TECHM.NS (TECH MAHINDRA LIMITED) score 61.4 — "Q1 Results Today Live: SBI, Titan and Hindalco post Q1 profit growth, Ola Electric & BEML "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 60.6 — "Q1 Results Today Live: SBI, Titan and Hindalco post Q1 profit growth, Ola Electric & BEML "
- OHI (Omega Healthcare Investors, In) score 58.3 — "Global Market: European shares rise as healthcare stocks offset geopolitical concerns; inv"
- COIN (Coinbase Global, Inc.) score 58.2 — "GLOBAL BOND INFLOWS SURGE AS EQUITY DEMAND COOLS Global bond funds attracted $23 billion t"
- TECH (Bio-Techne Corp) score 57.5 — "Q1 Results Today Live: SBI, Titan and Hindalco post Q1 profit growth, Ola Electric & BEML "
- BAC (Bank of America Corporation) score 53.3 — "Fossil Group is said to invite banks for India unit IPO"
- HDB (HDFC Bank Limited) score 50.8 — "Fossil Group is said to invite banks for India unit IPO"
- IDBI.NS (IDBI BANK LIMITED) score 49.1 — "Fossil Group is said to invite banks for India unit IPO"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 49.1 — "Fossil Group is said to invite banks for India unit IPO"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 48.1 — "Fossil Group is said to invite banks for India unit IPO"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 42.3 — "Hitachi Energy India Q1 Results: Net profit rises over twofold to Rs 294 crore"
- LTH (Life Time Group Holdings, Inc.) score 35.9 — "TRUMP: AI ‘BIGGER THAN THE INTERNET BY MANY TIMES’"
- CHKP (Check Point Software Technolog) score 33.9 — "LEAP India IPO Day 1: Issue subscribed 6% so far. GMP hints 12% listing gain. Check key da"
- 301077.SZ (CHINASTARS) score 31.4 — "TRUMP: WE DON’T WANT TO SEE CHINA TAKE OVER CRYPTO"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.2 — "There are good reasons higher bond yields are here to stay, this strategist says"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.1 — "Top Gainers & Losers on 7 August: Bajaj Finance, Navin Fluorine, Trent, Tata Capital, Swig"
- JIOFIN.BO (Jio Financial Services Limited) score 14.6 — "BSE Index Services launches BSE REITs Index. Here's everything you need to know"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.4 — "Top Gainers & Losers on 7 August: Bajaj Finance, Navin Fluorine, Trent, Tata Capital, Swig"
- MS (Morgan Stanley) score 14.0 — "AI frenzy spooks investors but JPMorgan CEO Jamie Dimon says spending boom likely to pay o"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.4 — "TRUMP: FED RATE DECISION ISN’T JUST UP TO WARSH Asked whether Fed Chair Kevin Warsh should"
- VT (Vanguard Total World Stock Ind) score 10.9 — "TRUMP: U.S. SHOULD PAY LOWEST INTEREST RATE IN WORLD TRUMP: FED RATE DECISION ‘NOT TOTALLY"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.9 — "IT stocks lead Nifty gains as financials bleed; West Asia, crude oil weigh on mood"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.6 — "Titan Q1 Results: Net profit jumps 63% to  ₹1,777 crore on steady jewellery demand; revenu"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.4 — "Adani Green Energy shares can rally up to 23%. Why Axis Capital, Elara initiated coverage"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.3 — "ICICI Bank, Axis Bank tap dollar debt again in less than two months: Report"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.3 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- NVDA (NVIDIA Corporation) score 6.2 — "NVDA - US REVIEWS CHINA’S OFFSHORE NVIDIA CHIP ACCESS AFTER AI GAINS"
- META (Meta) score 5.8 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- PLTR (Palantir Technologies Inc.) score 5.7 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 5.6 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- GOOGL (Alphabet) score 4.9 — "Alphabet, Meta Platforms to SK Hynix: What does the AI trade bubble burst mean for the Ind"
- MSFT (Microsoft Corporation) score 4.7 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- AAPL (Apple Inc.) score 4.3 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- SNDK (Sandisk Corporation) score 4.0 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
- INFY (Infosys Limited) score 3.8 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
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