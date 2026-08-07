# Transmission Layer — board brief · 2026-08-07 00:14Z

data as of **2026-08-07** · 98 series · 10 red / 27 amber · 8 events surfaced (14 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.329, 1d in regime; vol-pct 0.422, breadth-off 0.235, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.45, corr60 -0.42, contra nifty_50 corr20=0.07, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.81, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.33, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.06, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.02, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.12, corr60 0.17, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.0008081156037280657)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.835** (n=2625) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.05] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4307.60, z20 2.99, zc 0.00, resid-z 2.33 [unexplained], 1d 0.00%, |z20|=2.99; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6512.81, z20 2.76, zc 0.62, resid-z 1.58 [unexplained], 1d 0.55%, |z20|=2.76; 1y-pct=100
- cac_40 [INDICES]: last 8715.36, z20 2.69, zc 0.68, resid-z 1.83 [unexplained], 1d 0.53%, |z20|=2.69; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.72, z20 2.21, zc -0.00, resid-z 0.61 [quiet], 1d -0.01%, |z20|=2.21; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.90, z20 2.10, zc 0.00, resid-z -1.31 [quiet], 1d 0.00%, |z20|=2.10; co-occur[gold_silver] same-direction (channel VALID)
- dax [INDICES]: last 26162.17, z20 2.07, zc 0.17, resid-z 0.85 [quiet], 1d 0.14%, |z20|=2.07; 1y-pct=99
- dow_jones [INDICES]: last 53897.82, z20 2.05, zc -0.80, resid-z -0.69 [quiet], 1d -0.83%, |z20|=2.05; 1y-pct=99
- sp500 [INDICES]: last 7711.38, z20 2.02, zc -0.15, resid-z -1.21 [quiet], 1d -0.16%, |z20|=2.02; 1y-pct=99
- dyn_vt [EQUITIES]: last 159.94, z20 2.00, zc -0.13, resid-z -0.25 [quiet], 1d -0.14%, 1y-pct=99
- russell_2000 [INDICES]: last 3001.08, z20 1.23, zc -0.47, resid-z -0.35 [quiet], 1d -0.60%, 1y-pct=96
- gold_silver_ratio [DERIVED]: last 69.60, z20 -0.18, zc n/a, resid-z n/a [quiet], 1d 0.00%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold prices, alongside other commodities and indices, is driven by a combination of factors including optimism surrounding renewed U.S.-Iran diplomacy and lower oil prices. The VALID gold_silver_comove channel suggests that monetary metals are co-moving, while the VALID metal_copper_channel indicates that global copper is leading Indian metal equities. However, the INVERTED safe_haven_gold channel implies that the risk-off safe-haven bid for gold may be weakening.
- **Gap**: No gap: the big raw move in comex_gold with resid_z=2.33 is not an anomaly, but rather a priced move given the current market conditions and factor exposures.
- **India take**: The Indian instruments nifty_50, nifty_midcap_100, and nifty_metal have already reacted to the global market moves, with rho values of 0.539, 0.514, and 0.474 respectively. The nifty_metal index, in particular, has a high z20 value of 2.31, indicating a strong reaction to the global metal prices.
- Watch next: comex_gold (down) — already moved; resid_z=2.33 indicates unexplained move
- Watch next: stoxx_50 (down) — already moved; resid_z=1.58 indicates unexplained move
- **India receivers**: nifty_50 (rho 0.539, z 1.73); nifty_midcap_100 (rho 0.514, z 1.14); nifty_metal (rho 0.474, z 2.31)
- Source: Lower Oil Prices Lend Support For The Gold Rally — OilPrice, 2026-08-07. https://oilprice.com/Metals/Gold/Lower-Oil-Prices-Lend-Support-For-The-Gold-Rally.html
- Source: Gold prices are breaking higher after a tough stretch. Could fresh records be within reach? — MarketWatch Top, 2026-08-06. https://www.marketwatch.com/story/gold-prices-are-breaking-higher-after-a-tough-stretch-could-fresh-records-be-within-reach-1e1a872f?mod=mw_rss_topstories
- Source: Honeywell Aerospace lands in Wall Street’s ‘penalty box’ after gloomy guidance triggers 23% stock selloff — MarketWatch Top, 2026-08-06. https://www.marketwatch.com/story/honeywell-aerospace-lands-in-wall-streets-penalty-box-after-gloomy-guidance-triggers-21-stock-selloff-ea8b032c?mod=mw_rss_topstories
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [RED 6.76] usd_inr ↓
- usd_inr [FX]: last 95.08, z20 -1.76, zc -0.05, resid-z -0.20 [quiet], 1d -0.02%, 20d range extreme; |z20|=1.76
- **Mechanism**: The recent depreciation of the Indian rupee against the US dollar is driven by importer demand and geopolitical risks, despite central bank interventions and falling oil prices. The valid metal_copper_channel and gold_silver_comove channels suggest that global commodity trends may influence Indian metal equities and monetary metals. However, the weak dxy_inr_channel and inr_oil_channel imply that the broad dollar strength and oil prices may not significantly impact the INR. The RISK_ON regime and valid vix_equity_inverse channel indicate a risk-on environment with potential for equity drawdowns.
- **Gap**: No gap: the recent move in usd_inr is largely priced, with a small resid_z of -0.2 and a high z20 level of -1.76, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instruments dyn_bharatcoal_ns and dyn_havells_ns have already reacted to the usd_inr move, while eur_inr remains quiet. The INR may continue to be influenced by global commodity trends and risk-on environment.
- Watch next: dyn_bharatcoal_ns (up) — already moved; reacted to usd_inr move
- Watch next: dyn_havells_ns (up) — already moved; reacted to usd_inr move
- **India receivers**: dyn_bharatcoal_ns (rho 0.419, z -1.0); dyn_havells_ns (rho 0.417, z 1.66); eur_inr (rho 0.386, z 0.44)
- Source: Indian rupee slips on importer bids, far forward premiums ease to one-month low — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/forex/forex-news/indian-rupee-slips-on-importer-bids-far-forward-premiums-ease-to-one-month-low/articleshow/132997510.cms
- Source: Rupee falls 9 paise to 95.17 against US dollar in early trade — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/forex/rupee-falls-9-paise-to-9517-against-us-dollar-in-early-trade/article71312081.ece
- Source: Rupee opens flat at 95.13 against US dollar — Mint Markets, 2026-08-06. https://www.livemint.com/market/stock-market-news/rupee-opens-flat-at-95-13-against-us-dollar-11785987437216.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [AMBER 5.41] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.00, z20 2.09, zc 0.44, resid-z 0.39 [quiet], 1d 0.96%, |z20|=2.09
- nifty_50 [INDICES]: last 24636.00, z20 1.73, zc 0.07, resid-z 0.38 [quiet], 1d 0.05%, |z20|=1.73
- nifty_midcap_100 [INDICES]: last 63324.85, z20 1.14, zc -0.58, resid-z -1.01 [quiet], 1d -0.43%, 1y-pct=98
- **Mechanism**: The move in Indian benchmark indices, led by Reliance Industries and SBI, is driven by easing crude oil prices and the Reserve Bank of India's steady policy stance, which has resulted in selective buying in heavyweight stocks. This move is further supported by the VALID metal_copper_channel and vix_equity_inverse channels. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which may limit the upside. The low resid_z values for nifty_50 and nifty_midcap_100 indicate that the move is largely priced in.
- **Gap**: No gap: the low resid_z values for nifty_50 and nifty_midcap_100 indicate that the move is largely priced in, with no significant unexplained component.
- **India take**: The Indian instruments that express this move are dyn_muthootfin_ns, dyn_bharatcoal_ns, and nifty_metal, which have already reacted to the easing crude oil prices and the Reserve Bank of India's steady policy stance. However, dyn_indusindbk_bo remains quiet and may be worth watching.
- Watch next: dyn_jiofin_bo (up) — already moved; z20 level is high at 2.09
- Watch next: nifty_50 (up) — already moved; z20 level is high at 1.73
- **India receivers**: dyn_muthootfin_ns (rho 0.693, z -1.76); dyn_bharatcoal_ns (rho 0.651, z -1.0); dyn_indusindbk_bo (rho 0.626, z -0.6); dyn_indianb_ns (rho 0.603, z 2.61)
- Source: Nifty CAS gap narrows as markets adapt to new system — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/nifty-cas-gap-narrows-as-markets-adapt-to-new-system/article71313875.ece
- Source: Market wrap: Reliance Industries, SBI, Power Grid among top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-reliance-industries-sbi-power-grid-among-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133002408.cms
- Source: Sensex today | Stock Market Highlights: Sensex climbs 374 pts; Nifty ends above 24,600 on RBI, crude oil cues — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-6-august-2026/article71309748.ece
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [AMBER 4.79] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 90.56, z20 -1.12, zc -1.12, resid-z 0.00 [quiet], 1d -0.34%, 1y-pct=1
- tips_10y_real [RATES]: last 2.41, z20 0.66, zc 0.25, resid-z 0.01 [quiet], 1d 0.42%, 1y-pct=96
- ust_30y [RATES]: last 5.17, z20 0.64, zc -0.24, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=97
- ust_10y [RATES]: last 4.63, z20 0.07, zc 0.00, resid-z -0.28 [quiet], 1d 0.00%, 1y-pct=95
- **Mechanism**: The recent rise in US Treasury yields, driven by increasing oil prices and concerns about the Strait of Hormuz, is propagating through the VALID gold_silver_comove and metal_copper_channel, potentially impacting Indian metal equities. The RISK_ON regime, with a low probability of high-volatility, suggests a cautious market environment.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with small resid_z values indicating that the market has already accounted for the factors driving the move
- **India take**: Indian metal equities, such as those in the metal_copper_channel, may react to the global copper price movements, while the INR may weaken due to the potential increase in oil prices. The Nifty 50 may also be impacted by the risk-off sentiment, but has not reacted yet.
- Watch next: nifty_50 (down) — not yet - watch; Potential safe-haven bid in gold may lead to a risk-off sentiment, impacting Indian equities
- Watch next: usd_inr (up) — not yet - watch; Oil price increase may lead to a higher import bill, weakening the INR
- Source: As Alphabet burns through cash on AI, it’s turning back to the bond market — MarketWatch Top, 2026-08-06. https://www.marketwatch.com/story/as-alphabet-burns-through-cash-on-ai-its-turning-back-to-the-bond-market-04e85f31?mod=mw_rss_topstories
- Source: US Treasury yields rise as oil climbs before jobs report — Mint Markets, 2026-08-06. https://www.livemint.com/market/us-treasury-yields-rise-as-oil-climbs-before-jobs-report-11786043154633.html
- Source: Alphabet lures investors to mega bond deal with high premiums — Mint Markets, 2026-08-06. https://www.livemint.com/market/stock-market-news/alphabet-lures-investors-to-mega-bond-deal-with-high-premiums-11786034088038.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.46] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1445.00, z20 2.46, zc -0.53, resid-z -0.55 [quiet], 1d -1.75%, |z20|=2.46; 1y-pct=99
- **Mechanism**: The recent increase in mutual funds' stake in Ather Energy for the 5th straight quarter, coupled with the company's production facilities operating at full capacity and demand outpacing supply, suggests a potential bigger rally brewing. This move is likely priced, given the small resid_z of -0.55, indicating that the current price move is largely explained by factor exposures. The VALID metal_copper_channel may also play a role in transmitting global copper price movements to Indian metal equities, including Ather Energy.
- **Gap**: No gap: the current price move is largely explained by factor exposures, as indicated by the small resid_z of -0.55
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock, which has already reacted with a quiet move. Other Indian metal equities, such as those in the Nifty Metal index, may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential rally in Ather Energy may spill over to the broader Indian market
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.3] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 155.98, z20 2.30, zc -0.30, resid-z -0.06 [quiet], 1d -1.55%, |z20|=2.30
- **Mechanism**: dyn_pltr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho 0.401 via dyn_pltr, z 2.46, reacted)
- **India receivers**: dyn_atherenerg_ns (rho 0.401, z 2.46)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [AMBER 4.28] dyn_msft ↑
- dyn_msft [EQUITIES]: last 499.86, z20 2.28, zc 0.67, resid-z -0.53 [quiet], 1d 2.54%, |z20|=2.28
- **Mechanism**: The recent surge in Microsoft's stock price, driven by its AI revenue disclosure, is likely to propagate through the VALID metal_copper_channel, as global copper leads Indian metal equities. However, the resid_z of -0.53 suggests that the move is largely priced in, leaving limited room for further unexplained growth. The RISK_ON regime and VALID vix_equity_inverse channel also support the notion that the market has already factored in the positive news.
- **Gap**: No gap: the resid_z of -0.53 indicates that the move is largely priced in, leaving limited room for further unexplained growth
- **India take**: The Indian instrument that expresses this move is likely to be the Nifty Metal index, which may react positively to the global copper lead, although it has not yet done so. The Hindalco or Tata Steel stocks could also be affected, given their exposure to the metal sector.
- Watch next: nifty_50 (up) — not yet - watch; Indian metal equities may follow global copper's lead
- Source: OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billion in AI revenue from OpenAI in the year ended June, suggesting the ChatGPT maker accounts for more than half—and possibly around 70%—of its AI business. The figures highlight Microsoft's — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34422
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [AMBER 3.99] dyn_coin ↓
- dyn_coin [EQUITIES]: last 145.35, z20 -1.99, zc -0.61, resid-z 0.03 [quiet], 1d -3.03%, 1y-pct=1
- **Mechanism**: dyn_coin ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.834 vs dyn_coin
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.804 vs dyn_coin
- Source: U.S. Diesel Exports Hit Record High as Global Supply Crunch Deepens — OilPrice, 2026-08-06. https://oilprice.com/Energy/Energy-General/US-Diesel-Exports-Hit-Record-High-as-Global-Supply-Crunch-Deepens.html
- Source: Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1 — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-softbanks-ai-strategy-stays-on-course-despite-flat-openai-valuation-in-q1/articleshow/132996579.cms
- Source: Global Market: European shares hit record high as peace hopes, strong earnings lift sentiment — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-hit-record-high-as-peace-hopes-strong-earnings-lift-sentiment/articleshow/132996067.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-03 (d=0.0), 2025-08-08 (d=0.08)

## Watchlist (below surfacing floor)
natgas ↓ (3.88), dyn_bac ↑ (3.5), dyn_cupid_ns ↑ (3.48), asx_200 ↑ (2.95), dyn_indianb_ns ↑ (2.61), dyn_tech ↑ (2.59), usd_mxn ↓ (2.45), dyn_icicigi_bo ↓ (2.4), nifty_metal ↑ (2.31), dyn_lth ↑ (2.22), usd_cny ↓ (1.68), midcap_largecap_ratio ↓ (1.66)

## India macro
- nifty_50: 24636.0000 (1d 0.05%, z20 1.73, flag amber)
- nifty_midcap_100: 63324.8516 (1d -0.43%, z20 1.14, flag amber)
- usd_inr: 95.0773 (1d -0.02%, z20 -1.76, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5704 (1d -0.47%, z20 -1.66, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.0 — "India tops world in IPO count, ranks third in fundraising in FY26: SEBI Annual Report"
- COALINDIA.NS (COAL INDIA LTD) score 89.3 — "India tops world in IPO count, ranks third in fundraising in FY26: SEBI Annual Report"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.7 — "India tops world in IPO count, ranks third in fundraising in FY26: SEBI Annual Report"
- INDIANB.NS (INDIAN BANK) score 61.7 — "MUFG: DOLLAR STILL UNDERVALUED MUFG says the U.S. dollar remains undervalued against 8 of "
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.0 — "OKLO - OKLO HITS KEY NUCLEAR MILESTONE Oklo's small modular reactor reached criticality, m"
- OHI (Omega Healthcare Investors, In) score 56.6 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks close lower ahead of jobs repo"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 56.0 — "OKLO - OKLO HITS KEY NUCLEAR MILESTONE Oklo's small modular reactor reached criticality, m"
- COIN (Coinbase Global, Inc.) score 53.2 — "U.S. Diesel Exports Hit Record High as Global Supply Crunch Deepens"
- TECH (Bio-Techne Corp) score 52.6 — "OKLO - OKLO HITS KEY NUCLEAR MILESTONE Oklo's small modular reactor reached criticality, m"
- BAC (Bank of America Corporation) score 44.6 — "MUFG: DOLLAR STILL UNDERVALUED MUFG says the U.S. dollar remains undervalued against 8 of "
- HDB (HDFC Bank Limited) score 41.7 — "MUFG: DOLLAR STILL UNDERVALUED MUFG says the U.S. dollar remains undervalued against 8 of "
- IDBI.NS (IDBI BANK LIMITED) score 39.8 — "MUFG: DOLLAR STILL UNDERVALUED MUFG says the U.S. dollar remains undervalued against 8 of "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.8 — "MUFG: DOLLAR STILL UNDERVALUED MUFG says the U.S. dollar remains undervalued against 8 of "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.7 — "MUFG: DOLLAR STILL UNDERVALUED MUFG says the U.S. dollar remains undervalued against 8 of "
- LTH (Life Time Group Holdings, Inc.) score 34.3 — "PRESIDENT’S THURSDAY SCHEDULE 🔸 8:00 AM — Executive Time 🔸 9:00 AM — In-Town Pool Call 🔸 1"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.0 — "Argentina's Shale Boom Is Reshaping Energy Security Across the Americas"
- CHKP (Check Point Software Technolog) score 28.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 6"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.6 — "ALPHABET KICKS OFF 10-PART US DOLLAR INVESTMENT-GRADE BOND SALE"
- 301077.SZ (CHINASTARS) score 25.7 — "China Added More Nuclear Power In A Decade Than The Rest Of The World Combined"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.1 — "Tata Sons faces continued listing uncertainty after RBI classification"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.9 — "Swiggy shares jump nearly 3% as company targets Rs 10,000 crore adjusted EBITDA by FY31"
- MS (Morgan Stanley) score 12.7 — "Somebody will disrupt the market! Why JPMorgan CEO Jamie Dimon is raising alarm over high "
- JIOFIN.BO (Jio Financial Services Limited) score 12.4 — "Can Tips Music's Rs 44 crore share buyback boost its share price? Here's what JM Financial"
- VT (Vanguard Total World Stock Ind) score 10.1 — "India tops world in IPO count, ranks third in fundraising in FY26: SEBI Annual Report"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.8 — "Muthoot Microfin Q1 profit jumps 13-fold on stronger loan growth"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "Can Tips Music's Rs 44 crore share buyback boost its share price? Here's what JM Financial"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.7 — "Top Gainers & Losers on 6 August: Navin Fluorine, Tata Tech, HAL, Pine Labs, Kalyan Jewell"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.4 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Trading Status"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.2 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- PLTR (Palantir Technologies Inc.) score 6.4 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 6.4 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- NVDA (NVIDIA Corporation) score 5.9 — "NVDA - NVIDIA SHARES HIT HIGHEST IN OVER TWO MONTHS, LAST UP 4.3%"
- META (Meta) score 5.5 — "META AI MODEL ACCESSED INTERNET, HACKED A COMPANY: INFORMATION"
- MSFT (Microsoft Corporation) score 5.3 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.1 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- AAPL (Apple Inc.) score 4.9 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- SNDK (Sandisk Corporation) score 4.6 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
- GOOGL (Alphabet) score 4.5 — "Alphabet seeks up to $25 billion in US bond sale to fund AI spending"
- INFY (Infosys Limited) score 4.3 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
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