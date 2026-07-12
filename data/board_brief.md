# Transmission Layer — board brief · 2026-07-12 19:01Z

data as of **2026-07-12** · 89 series · 8 red / 25 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.356, 4d in regime; vol-pct 0.524, breadth-off 0.188, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.27, corr60 -0.45, contra nifty_50 corr20=0.42, last shift 2026-05-18. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.47, corr60 0.38, last shift 2026-05-20. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 -0.03, last shift 2026-03-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.78, last shift 2026-05-11. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-12. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.2, corr60 0.26, last shift 2026-04-20. Channel: gold/silver ratio rises under monetary stress

## Events (ranked)

### [RED 7.7] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 480.20, z20 5.70, zc 0.90, resid-z 1.63 [unexplained], 1d 8.40%, |z20|=5.70
- **Mechanism**: The recent surge in dyn_kalyankjil_ns is driven by its breakout potential and favourable technical indicators, as highlighted by LKP Securities. This move is also supported by the positive market sentiment and strong earnings from TCS, which boosted investor confidence. The metal_copper_channel and gold_silver_comove channels are valid and may contribute to the propagation of this move.
- **Gap**: No gap: the move in dyn_kalyankjil_ns is largely priced, with a resid_z of 1.63 and a z20 of 5.70, indicating that the move is mostly explained by its factor exposures
- **India take**: The Indian instruments that express this move are nifty_midcap_100, dyn_indianb_ns, and dyn_pcjeweller_ns, which have already reacted to the surge in dyn_kalyankjil_ns. The nifty_50 has not yet reacted, but its rho of 0.41 suggests it may follow suit.
- Watch next: nifty_midcap_100 (up) — reacted; rho=0.574 via dyn_kalyankjil_ns
- Watch next: dyn_indianb_ns (up) — reacted; rho=0.512 via dyn_kalyankjil_ns
- Watch next: nifty_50 (up) — quiet; rho=0.41 via dyn_kalyankjil_ns
- **India receivers**: nifty_midcap_100 (rho 0.574, z 1.6); dyn_indianb_ns (rho 0.512, z 1.35); dyn_pcjeweller_ns (rho 0.445, z 1.89); nifty_50 (rho 0.41, z 0.82)
- Source: From Kalyan Jewellers' 52-week high to Trent's reality check: LKP Securities' top trading ideas — ET Markets, 2026-07-12. https://economictimes.indiatimes.com/markets/stocks/news/from-kalyan-jewellers-52-week-high-to-trents-reality-check-lkp-securities-top-trading-ideas/articleshow/132341207.cms
- Source: F&O Talk: Mid, smallcaps to continue outperformance as Q1 begins, says Sudeep Shah; outlines Kalyan Jewellers, TCS strategy — ET Markets, 2026-07-11. https://economictimes.indiatimes.com/markets/expert-view/fo-talk-mid-smallcaps-to-continue-outperformance-as-q1-begins-says-sudeep-shah-outlines-kalyan-jewellers-tcs-strategy/articleshow/132326016.cms
- Historical analogues: 2026-01-07 (d=1.99), 2026-06-15 (d=2.01), 2025-07-02 (d=3.07)

### [RED 5.82] dyn_meta ↑
- dyn_meta [EQUITIES]: last 669.31, z20 3.82, zc 2.00, resid-z 1.39 [moved], 1d 5.99%, |z20|=3.82
- **Mechanism**: The recent surge in dyn_meta is driven by its high z20 level of 3.819, indicating a strong move. However, with a resid_z of 1.39, the move is largely priced in, suggesting that the unexplained component is relatively small. The valid vix_equity_inverse channel indicates a potential inverse relationship between volatility and equity performance, which could contribute to the move. The metal_copper_channel also shows a positive correlation, potentially influencing the move through commodity markets.
- **Gap**: No gap: the move in dyn_meta is largely priced in, with a resid_z of 1.39 indicating a relatively small unexplained component
- **India take**: Indian instruments such as dyn_indianb_ns, dyn_swiggy_ns, and nifty_midcap_100 have already reacted to the move in dyn_meta, with correlations ranging from 0.398 to 0.408. Further moves in these instruments will depend on the sustainability of the dyn_meta surge.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to dyn_meta move
- **India receivers**: dyn_indianb_ns (rho 0.408, z 1.35); dyn_swiggy_ns (rho 0.4, z 2.06); nifty_midcap_100 (rho 0.398, z 1.6)
- Source: Meta’s stock roars back to life as it notches its best week in years — MarketWatch Top, 2026-07-10. https://www.marketwatch.com/story/metas-stock-roars-back-to-life-as-it-heads-for-its-best-week-in-years-0ff0fa7d?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [AMBER 5.62] cross-asset · 5 series ↑
- sp500 [INDICES]: last 7575.38, z20 1.69, zc 0.52, resid-z 0.11 [quiet], 1d 0.42%, |z20|=1.69; 1y-pct=98
- vix [INDICES]: last 15.04, z20 -1.56, zc -0.60, resid-z n/a [quiet], 1d -5.05%, |z20|=1.56
- dow_jones [INDICES]: last 52640.31, z20 1.01, zc 0.36, resid-z -0.05 [quiet], 1d 0.29%, 1y-pct=98
- dyn_vt [EQUITIES]: last 157.60, z20 0.96, zc 0.45, resid-z -0.50 [quiet], 1d 0.38%, 1y-pct=96
- dyn_ms [EQUITIES]: last 222.28, z20 0.76, zc 0.04, resid-z 0.51 [quiet], 1d 0.07%, 1y-pct=98
- **Mechanism**: The recent move in US equities, as seen in the S&P 500 and Dow Jones, is largely priced in, with a small resid_z value indicating that the move is mostly explained by factor exposures. The VIX, however, has a larger z20 value, suggesting a potential increase in volatility. The mechanism driving this move is likely related to the upcoming inflation data and bank earnings, which may impact the Federal Reserve's monetary policy decisions.
- **Gap**: No gap: the current move in US equities is largely priced in, with small resid_z values indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react to the US market developments, particularly if the VIX increases, leading to a risk-off sentiment. However, the dxy_inr_channel is weak, suggesting that the transmission mechanism from US markets to INR is not strong at present.
- Watch next: nasdaq_100 (up) — not yet - watch; historically leads the S&P 500 by 5 days
- Source: Week Ahead: Wall Street braces for inflation data, big bank earnings and Middle East developments — Mint Markets, 2026-07-12. https://www.livemint.com/market/stock-market-news/week-ahead-wall-street-braces-for-inflation-data-big-bank-earnings-and-middle-east-developments-11783868386079.html
- Source: TRUMP: STRAIT OF HORMUZ OPEN TO COMMERCIAL SHIPPING U.S. President Donald Trump said the Strait of Hormuz remains open to commercial traffic. However, continued U.S.–Iran attacks are raising safety concerns along one of the world’s most critical oil shipping routes. Trump made — DeItaone, 2026-07-12. https://t.me/walter_bloomberg/33560
- Source: KALSHI WORLD CUP BETS COULD GET A TAX BREAK Americans betting on the World Cup through prediction markets could face lower taxes than sportsbook users. Because event contracts are structured as investments, traders may claim broader loss deductions—and potentially lower tax — DeItaone, 2026-07-12. https://t.me/walter_bloomberg/33558
- Historical analogues: 2024-10-17 (d=0.41), 2026-05-22 (d=0.54), 2025-10-24 (d=0.58)

### [RED 5.59] natgas ↓
- natgas [COMMODITIES]: last 2.94, z20 -3.59, zc -0.57, resid-z -0.91 [quiet], 1d -2.39%, |z20|=3.59
- **Mechanism**: The decline in natural gas demand in India, driven by the West Asia conflict and the closure of the Strait of Hormuz, has led to a decrease in natgas prices. This move is largely priced, given the small resid_z value of -0.91, indicating that the decline is largely explained by factor exposures. The VALID metal_copper_channel and gold_silver_comove channels may also influence the price movement, but the primary driver is the decline in demand.
- **Gap**: No gap: the decline in natgas prices is largely explained by factor exposures, with a small resid_z value, indicating that the move is priced
- **India take**: The decline in natural gas demand in India is likely to be expressed through a decrease in the prices of Indian natural gas companies, such as GAIL or ONGC, which have not yet reacted to the news.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment from the decline in natgas prices may lead to a decrease in nifty_50
- Source: India’s natural gas demand likely to decline by 8% in 2026 — BusinessLine Mkts, 2026-07-11. https://www.thehindubusinessline.com/markets/commodities/indias-natural-gas-demand-likely-to-decline-by-8-in-2026/article71210886.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 5.49] commodities · 3 series ↑
- wheat [COMMODITIES]: last 640.25, z20 4.17, zc 3.08, resid-z 2.42 [unexplained], 1d 4.74%, |z20|=4.17; 1y-pct=96
- corn [COMMODITIES]: last 461.00, z20 4.04, zc 6.25, resid-z 5.54 [unexplained], 1d 7.77%, |z20|=4.04
- soybeans [COMMODITIES]: last 1190.75, z20 2.01, zc 0.92, resid-z 1.00 [quiet], 1d 0.93%, |z20|=2.01
- **Mechanism**: The recent surge in commodities, particularly wheat, corn, and soybeans, is driven by unexplained factors, as indicated by their high resid_z values. This move is not fully priced in, given the low r2 values for these commodities. The valid gold_silver_comove channel suggests that monetary metals are co-moving, which may be influencing the commodity prices.
- **Gap**: No gap: the high resid_z values for wheat, corn, and soybeans indicate that the current price move is not fully explained by factors, but the low r2 values suggest that the move is not entirely unexpected
- **India take**: The Indian instrument dyn_adanient_bo, which has a negative correlation with soybeans, has already reacted to the commodity price move. Further reaction in Indian metal equities can be expected via the valid metal_copper_channel.
- Watch next: wheat (up) — unexplained; high resid_z value
- **India receivers**: dyn_adanient_bo (rho -0.373, z 1.25)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.68] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.60, z20 1.68, zc n/a, resid-z n/a [quiet], 1d 0.35%, 52-wk extreme (pct=97); |z20|=1.68; 1y-pct=97
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z-score of 1.64, indicating a potential mean reversion. This ratio is derived from the relative performance of midcap and largecap stocks, and its extreme value may signal a reversal in the market trend. The historical analogues suggest a mixed outcome for various assets, with the S&P 500 showing a positive median return, while the high-yield OAS shows a negative median return.
- **Gap**: No gap: the nifty_midcap_100 has already reacted to the extreme midcap_largecap_ratio, with a z-score of 1.59, indicating that the Indian market has likely priced in the event
- **India take**: The Nifty Midcap 100 index, with a correlation of 0.516 with the midcap_largecap_ratio, has likely expressed this move and may be due for a correction. The Indian market may see a pullback in midcap stocks, as indicated by the high z-score of the nifty_midcap_100
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.518, z 1.6); dyn_swiggy_ns (rho 0.374, z 2.06); dyn_kalyankjil_ns (rho 0.368, z 5.7); dyn_indianb_ns (rho 0.357, z 1.35)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.09] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.25, z20 -2.09, zc -0.80, resid-z 0.84 [quiet], 1d -6.45%, |z20|=2.09
- **Mechanism**: The decline in dyn_qessf is attributed to the announcement of Apollo Micro Systems' plans to raise ₹3,322 crore through fresh equity issuance, which may lead to equity dilution and impact the stock's price. This move is largely priced, given the small resid_z value of 0.84. The valid metal_copper_channel and gold_silver_comove channels do not directly influence this event, but the vix_equity_inverse channel suggests a potential increase in volatility, which may impact the stock's price.
- **Gap**: No gap: the move in dyn_qessf is largely priced, with a small resid_z value indicating that the decline is mostly explained by factor exposures
- **India take**: The Indian instrument that expresses this move is Apollo Micro Systems, which has already reacted to the news with a 2.65% increase in stock price on Friday. However, the stock may experience further volatility due to the planned equity issuance.
- Watch next: Apollo Micro Systems (down) — already moved; equity dilution from fresh issuance
- Source: Multibagger defence stock to raise  ₹3,322 crore through fresh equity issuance — Mint Markets, 2026-07-12. https://www.livemint.com/market/stock-market-news/multibagger-defence-stock-apollo-micro-systems-to-raise-3-322-crore-through-fresh-equity-issuance-11783836726858.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 3.9] bovespa ↑
- bovespa [INDICES]: last 177680.62, z20 3.90, zc 3.11, resid-z 3.20 [unexplained], 1d 2.86%, |z20|=3.90
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-08-13 (z-distance 0.73).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.551 vs bovespa, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.543 vs bovespa, historically leads by 2d
- Historical analogues: 2024-08-13 (d=0.73), 2025-08-12 (d=0.92), 2025-01-30 (d=0.96)

## Watchlist (below surfacing floor)
dyn_atherenerg_ns ↑ (3.89), gold_silver_ratio ↑ (3.77), sofr ↓ (3.64), rates · 4 series ↑ (3.49), cross-asset · 2 series ↑ (2.82), brent_wti_spread ↑ (2.5), dyn_swiggy_ns ↑ (2.06), dyn_cupid_ns ↑ (1.67), eth_usd ↑ (1.54), dyn_adanient_bo ↑ (1.25), dyn_inoxindia_ns ↑ (1.23), usd_cny ↓ (1.06)

## India macro
- nifty_50: 24211.6504 (1d 1.04%, z20 0.82, flag none)
- nifty_midcap_100: 63034.3008 (1d 1.40%, z20 1.60, flag amber)
- usd_inr: 95.3700 (1d -0.51%, z20 0.75, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6035 (1d 0.35%, z20 1.68, flag red)
- Next India prints: India CPI T-1d · NSDL FPI flows T-1d · IMD weekly rainfall T-1d · India WPI T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 30.8 — "Nearly 60% of foreign inflows into India-focused funds withdrawn since 2024 peak: Report"
- HDB (HDFC Bank Limited) score 24.2 — "HDFC Bank, HCL Tech among 143 companies to announce earnings this week"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 23.9 — "HDFC Bank, HCL Tech among 143 companies to announce earnings this week"
- COIN (Coinbase Global, Inc.) score 22.8 — "World’s wealth gap is widening, UBS Global Wealth Report shows"
- INDIANB.NS (INDIAN BANK) score 13.5 — "Q1 results FY27 to US-Iran war: Top five triggers that may dictate the Indian stock market"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 12.4 — "Nomura sees 22% upside in Ather Energy. Here's why it's the brokerage's top EV pick"
- SKHYV (SK hynix Inc. American Deposit) score 9.2 — "AI chip fever returns? SK Hynix  share price surges 13% after blockbuster $26.5 billion US"
- CHKP (Check Point Software Technolog) score 9.1 — "SBI Funds Management IPO: SBI offloads 1.42% stake to 30 investors ahead of issue | Check "
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 7.1 — "F&O Talk: Mid, smallcaps to continue outperformance as Q1 begins, says Sudeep Shah; outlin"
- BOND (PIMCO Active Bond Exchange-Tra) score 6.3 — "PFC raises USD 300 mn via bonds carrying floating interest rates"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.5 — "F&O Talk: Mid, smallcaps to continue outperformance as Q1 begins, says Sudeep Shah; outlin"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.2 — "Multibagger defence stock to raise  ₹3,322 crore through fresh equity issuance"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 4.2 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- MU (Micron Technology, Inc.) score 4.0 — "SK Hynix makes US debut today. Will investors sell Micron to buy the AI memory leader?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 3.9 — "Vedanta Aluminium, Adani Power, 4 other stocks with up to 24% upside. Do you own any?"
- SWIGGY.NS (SWIGGY LIMITED) score 3.8 — "Broker’s call: Swiggy (Reduce)"
- JEF (Jefferies Financial Group Inc.) score 3.4 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- META (Meta) score 3.4 — "Guardian Metal, Montana Mining Association forge US tungsten processing alliance"
- MCAP (MCAP Inc.) score 3.0 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- VT (Vanguard Total World Stock Ind) score 2.9 — "Gold price loses its grip: World’s 50 biggest mining companies shed $228 billion in Q2"
- CUPID.NS (CUPID LIMITED) score 2.4 — "Cupid shares jump 6%, stock skyrockets 900% in one year. Should you buy now?"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 2.3 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.1 — "IC Electricals share price hits 5% upper circuit after blockbuster debut"
- MS (Morgan Stanley) score 2.1 — "Morgan Stanley warns AI chip rally may be running out of steam"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.8 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 1.3 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 1.2 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 1.0 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.9 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
- WULF (TeraWulf Inc.) score 0.7 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"
- BLK (BlackRock, Inc.) score 0.6 — "BlackRock to launch Nasdaq-100 ETF as AI rally pulls investors into tech stocks"

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