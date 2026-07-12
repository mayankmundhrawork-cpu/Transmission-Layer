# Transmission Layer — board brief · 2026-07-12 18:53Z

data as of **2026-07-11** · 87 series · 8 red / 23 amber · 8 events surfaced (18 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.149, 1d in regime; vol-pct 0.11, breadth-off 0.188, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.28, corr60 -0.45, contra nifty_50 corr20=0.43, last shift 2025-07-14. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.83, last shift 2025-05-05. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.44, corr60 0.37, last shift 2025-03-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 -0.03, last shift 2026-01-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.78, last shift 2025-04-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 0.01, last shift 2025-08-20. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2025-08-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.19, corr60 0.25, last shift 2025-04-04. Channel: gold/silver ratio rises under monetary stress

## Events (ranked)

### [RED 5.82] dyn_meta ↑
- dyn_meta [EQUITIES]: last 669.31, z20 3.82, zc 2.00, resid-z 1.39 [moved], 1d 5.99%, |z20|=3.82
- **Mechanism**: The surge in Meta stock due to plans for AI chip production and potential Tencent investment in AI startup Manus may propagate through the technology sector, influencing Indian equities with similar exposures. This move may be transmitted through the correlation between Meta and Indian stocks, such as dyn_indianb_ns, nifty_midcap_100, and dyn_swiggy_ns. The historical analogues of dyn_meta's z-score suggest a potential positive impact on the S&P 500 and a mixed impact on other assets.
- **Gap**: No gap: the event is already priced in, with dyn_meta surging 7.5% on the news and Indian transmission candidates reacting accordingly
- **India take**: Indian equities such as dyn_indianb_ns, nifty_midcap_100, and dyn_swiggy_ns have already reacted to the move in dyn_meta, with z-scores of 1.35, 1.59, and 2.06, respectively. These stocks may continue to be influenced by further developments in the AI and technology sectors.
- Watch next: dyn_meta (up) — already moved; 7.5% surge on AI chip production news
- **India receivers**: dyn_indianb_ns (rho 0.413, z 1.35); dyn_swiggy_ns (rho 0.393, z 2.06); nifty_midcap_100 (rho 0.391, z 1.59)
- Source: Meta’s stock roars back to life as it notches its best week in years — MarketWatch Top, 2026-07-10. https://www.marketwatch.com/story/metas-stock-roars-back-to-life-as-it-heads-for-its-best-week-in-years-0ff0fa7d?mod=mw_rss_topstories
- Source: Meta stock surges 7.5% as report says AI chip production could begin this year — Mint Markets, 2026-07-10. https://www.livemint.com/market/stock-market-news/meta-stock-surges-12-as-report-says-ai-chip-production-could-begin-this-year-11783690729013.html
- Source: Global Market | Tencent explores stake in AI Startup Manus after China challenges Meta deal: Reports — ET Markets, 2026-07-10. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-tencent-explores-stake-in-ai-startup-manus-after-china-challenges-meta-deal-reports/articleshow/132306230.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [RED 5.7] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 480.20, z20 5.70, zc 0.90, resid-z 1.63 [unexplained], 1d 8.40%, |z20|=5.70
- **Mechanism**: The surge in Kalyan Jewellers' stock price is driven by strong buying momentum following a robust first-quarter business update, which reported 38% consolidated revenue growth. This growth, despite a challenging period for gold purchases, has led to a bullish stance among analysts. The rally is further supported by expansion strategies and industry formalisation. The mechanism of transmission to other Indian instruments is through correlation, with Nifty Midcap 100, PC Jeweller, and IndusInd Bank being among the affected stocks.
- **Gap**: No gap: the stock price of Kalyan Jewellers has already jumped over 36% in three days, reflecting the strong buying momentum and positive business update.
- **India take**: The Indian instruments that express this move are Nifty Midcap 100, PC Jeweller, and IndusInd Bank, which have already reacted to the surge in Kalyan Jewellers' stock price. The Nifty 50, although correlated, has remained relatively quiet with a z20 score of 0.82.
- Watch next: nifty_midcap_100 (up) — reacted; rho=0.548 via dyn_kalyankjil_ns
- **India receivers**: nifty_midcap_100 (rho 0.58, z 1.59); dyn_indianb_ns (rho 0.515, z 1.35); dyn_pcjeweller_ns (rho 0.439, z 1.89); nifty_50 (rho 0.408, z 0.82)
- Source: Top Gainers & Losers on 10 July: Godrej Industries, Indian Bank, Kalyan Jewellers, Paytm, CDSL among top gainers — Mint Markets, 2026-07-10. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-10-july-godrej-industries-indian-bank-kalyan-jewellers-paytm-cdsl-among-top-gainers-11783676501893.html
- Source: Kalyan Jewellers India share price jumps over 36% in three days. Buy, sell or hold? — Mint Markets, 2026-07-10. https://www.livemint.com/market/stock-market-news/kalyan-jewellers-india-share-price-jumps-over-36-in-three-days-buy-sell-or-hold-11783666796874.html
- Source: Kalyan Jewellers jumps 9%, m-cap swells by Rs 13,280 crore in 3 days. What's next? — ET Markets, 2026-07-10. https://economictimes.indiatimes.com/markets/stocks/news/kalyan-jewellers-jumps-9-extends-3-day-rally-to-36-whats-next/articleshow/132303291.cms
- Historical analogues: 2026-01-07 (d=1.99), 2026-06-15 (d=2.01), 2025-07-02 (d=3.07)

### [RED 5.4] commodities · 3 series ↑
- wheat [COMMODITIES]: last 639.25, z20 4.08, zc 2.97, resid-z 2.34 [unexplained], 1d 4.58%, |z20|=4.08; 1y-pct=96
- corn [COMMODITIES]: last 460.25, z20 3.97, zc 6.11, resid-z 5.41 [unexplained], 1d 7.60%, |z20|=3.97
- soybeans [COMMODITIES]: last 1189.50, z20 1.97, zc 0.81, resid-z 0.89 [quiet], 1d 0.83%, |z20|=1.97
- **Mechanism**: The recent surge in global commodity prices, particularly in wheat, corn, and soybeans, is likely to propagate through the Indian markets due to the country's dependence on these commodities. The increase in soybean prices, which are currently above the minimum support price levels, is expected to lead to an increase in soybean acreage in India. This, in turn, may impact the prices of related Indian instruments.
- **Gap**: No gap: the Indian instrument dyn_adanient_bo has already reacted to the surge in soybean prices, given its negative correlation
- **India take**: The Indian instrument dyn_adanient_bo, which has a negative correlation with soybeans, has already reacted to the surge in soybean prices. However, other related Indian instruments may still be affected by the increase in soybean acreage and prices.
- Watch next: dyn_adanient_bo (down) — already moved; negatively correlated with soybeans
- **India receivers**: dyn_adanient_bo (rho -0.375, z 1.25)
- Source: India’s soybean acreage seen rising 5-7 per cent on favourable prices — BusinessLine Mkts, 2026-07-09. https://www.thehindubusinessline.com/economy/agri-business/indias-soybean-acreage-seen-rising-5-7-per-cent-on-favourable-prices/article71203124.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [AMBER 5.35] cross-asset · 4 series ↑
- sp500 [INDICES]: last 7575.38, z20 1.69, zc 0.52, resid-z 0.11 [quiet], 1d 0.42%, |z20|=1.69; 1y-pct=98
- vix [INDICES]: last 15.04, z20 -1.56, zc -0.60, resid-z n/a [quiet], 1d -5.05%, |z20|=1.56
- dow_jones [INDICES]: last 52640.31, z20 1.01, zc 0.36, resid-z -0.05 [quiet], 1d 0.29%, 1y-pct=98
- dyn_ms [EQUITIES]: last 222.28, z20 0.76, zc 0.04, resid-z 0.51 [quiet], 1d 0.07%, 1y-pct=98
- **Mechanism**: The recent surge in US equities, as seen in the S&P 500, Dow Jones, and Dyn MS, is driven by a combination of strong earnings expectations and geopolitical tensions, which have also led to a decline in the VIX. This move is likely to propagate through correlated instruments that have not yet moved, such as the Nasdaq 100 and Russell 2000, due to their historical lead-lag relationships with the S&P 500.
- **Gap**: No gap: the recent move in US equities is largely driven by fundamentals and has been reflected in the prices of the S&P 500, Dow Jones, and Dyn MS, leaving little room for a significant event-to-price gap.
- **India take**: The Indian market is likely to react to this global trend, with the Nifty and Sensex potentially following the lead of the S&P 500 and Dow Jones. However, the reaction may be muted due to domestic factors and the already strong performance of the Indian market.
- Watch next: nasdaq_100 (up) — not yet - watch; historically leads by 5d
- Watch next: russell_2000 (up) — not yet - watch; historically leads by 3d
- Source: Wall Street Week Ahead: Investors to grapple with packed week of earnings, CPI, Iran headlines — ET Markets, 2026-07-11. https://economictimes.indiatimes.com/markets/us-stocks/news/wall-st-week-ahead-investors-to-grapple-with-packed-week-of-earnings-cpi-iran-headlines/articleshow/132324249.cms
- Source: Morgan Stanley warns AI chip rally may be running out of steam — ET Markets, 2026-07-10. https://economictimes.indiatimes.com/markets/us-stocks/news/morgan-stanley-warns-ai-chip-rally-may-be-running-out-of-steam/articleshow/132315698.cms
- Source: Wall Street banks rule on staff betting on prediction markets, sources say — ET Markets, 2026-07-10. https://economictimes.indiatimes.com/markets/us-stocks/news/wall-street-banks-rule-on-staff-betting-on-prediction-markets-sources-say/articleshow/132314792.cms
- Historical analogues: 2024-10-17 (d=0.46), 2025-10-24 (d=0.54), 2026-05-22 (d=0.6)

### [RED 4.64] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.60, z20 1.64, zc n/a, resid-z n/a [quiet], 1d 0.25%, 52-wk extreme (pct=97); |z20|=1.64; 1y-pct=97
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z-score of 1.64, indicating a potential mean reversion. This ratio is derived from the relative performance of midcap and largecap stocks, and its extreme value may signal a reversal in the market trend. The historical analogues suggest a mixed outcome for various assets, with the S&P 500 showing a positive median return, while the high-yield OAS shows a negative median return.
- **Gap**: No gap: the nifty_midcap_100 has already reacted to the extreme midcap_largecap_ratio, with a z-score of 1.59, indicating that the Indian market has likely priced in the event
- **India take**: The Nifty Midcap 100 index, with a correlation of 0.516 with the midcap_largecap_ratio, has likely expressed this move and may be due for a correction. The Indian market may see a pullback in midcap stocks, as indicated by the high z-score of the nifty_midcap_100
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.506, z 1.59); dyn_kalyankjil_ns (rho 0.368, z 5.7); dyn_swiggy_ns (rho 0.352, z 2.06)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 3.9] bovespa ↑
- bovespa [INDICES]: last 177680.62, z20 3.90, zc 3.11, resid-z 3.19 [unexplained], 1d 2.86%, |z20|=3.90

### [AMBER 3.81] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 68.47, z20 0.81, zc n/a, resid-z n/a [quiet], 1d 0.09%, GSR<75 (extreme low)
- **Mechanism**: The gold-silver ratio has increased, which may propagate through the commodities market, affecting prices of correlated instruments such as COMEX copper, silver, and gold. This move could be driven by changes in industrial demand or investor sentiment. The historically leading relationships between these instruments and the gold-silver ratio suggest potential follow-through moves.
- **Gap**: No gap: The correlated instruments have not moved significantly yet, and the historical analogues do not show a consistent pattern of price movement after a similar increase in the gold-silver ratio.
- **India take**: Indian investors can express this view through instruments such as MCX Copper, MCX Silver, and MCX Gold, which are likely to be affected by the movement in COMEX copper, silver, and gold. However, these instruments have not reacted significantly yet.
- Watch next: comex_copper (down) — not yet - watch; Historical lead of 3 days
- Watch next: comex_silver (down) — not yet - watch; High negative correlation
- Watch next: comex_gold (down) — not yet - watch; Historical lead of 4 days

### [RED 3.64] sofr ↓
- sofr [RATES]: last 3.53, z20 -3.64, zc -1.15, resid-z -2.14 [unexplained], 1d -1.40%, |z20|=3.64; 1y-pct=1

## Watchlist (below surfacing floor)
rates · 4 series ↑ (3.49), natgas ↓ (3.48), cross-asset · 2 series ↑ (2.82), brent_wti_spread ↑ (2.3), dyn_qessf ↓ (2.09), dyn_swiggy_ns ↑ (2.06), dyn_atherenerg_ns ↑ (1.89), dyn_cupid_ns ↑ (1.67), dyn_adanient_bo ↑ (1.25), dyn_inoxindia_ns ↑ (1.23), usd_cny ↓ (1.06), eur_usd ↓ (0.42)

## India macro
- nifty_50: 24211.6504 (1d 1.04%, z20 0.82, flag none)
- nifty_midcap_100: 63034.3008 (1d 1.29%, z20 1.59, flag amber)
- usd_inr: 95.3700 (1d -0.51%, z20 0.75, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6035 (1d 0.25%, z20 1.64, flag red)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India WPI T-1d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 38.2 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- COIN (Coinbase Global, Inc.) score 29.7 — "Global Markets: Chinese fast fashion retailer Shein finally wins approval for Hong Kong IP"
- HDB (HDFC Bank Limited) score 24.5 — "Bank credit growth at two-year high at 18.6% as debt market turns costlier"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 24.2 — "Bank credit growth at two-year high at 18.6% as debt market turns costlier"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 13.4 — "Bureaucracy Is Strangling America's Clean Energy Buildout"
- SKHYV (SK hynix Inc. American Deposit) score 11.7 — "SK Hynix shares jump in marquee US debut as AI euphoria persists"
- BOND (PIMCO Active Bond Exchange-Tra) score 9.0 — "PFC raises USD 300 mn via bonds carrying floating interest rates"
- CHKP (Check Point Software Technolog) score 7.3 — "Reliance Industries, Jio Financial announce Q1 earnings dates. Check details"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 7.3 — "Kalyan Jewellers stock to double from here? Why analysts are bullish"
- INDIANB.NS (INDIAN BANK) score 6.5 — "Bank credit growth at two-year high at 18.6% as debt market turns costlier"
- MU (Micron Technology, Inc.) score 5.6 — "SK Hynix makes US debut today. Will investors sell Micron to buy the AI memory leader?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.5 — "Vedanta Aluminium, Adani Power, 4 other stocks with up to 24% upside. Do you own any?"
- SWIGGY.NS (SWIGGY LIMITED) score 5.4 — "Broker’s call: Swiggy (Reduce)"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.0 — "Kalyan Jewellers stock to double from here? Why analysts are bullish"
- JEF (Jefferies Financial Group Inc.) score 4.9 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.6 — "Sebi approves IPOs of defence electronics maker Tonbo Imaging and 3 others"
- CUPID.NS (CUPID LIMITED) score 3.4 — "Cupid shares jump 6%, stock skyrockets 900% in one year. Should you buy now?"
- META (Meta) score 3.4 — "Meta’s stock roars back to life as it notches its best week in years"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 3.2 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.1 — "IC Electricals share price hits 5% upper circuit after blockbuster debut"
- MS (Morgan Stanley) score 3.0 — "Morgan Stanley warns AI chip rally may be running out of steam"
- KNACK.BO (KNACK PACKAGING LIMITED) score 2.6 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 1.8 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 1.7 — "Bharti Airtel declares record date for the payment of final dividend in FY26. Details here"
- HLIO (Helios Technologies, Inc.) score 1.7 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 1.4 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.3 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
- WULF (TeraWulf Inc.) score 1.1 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"
- BLK (BlackRock, Inc.) score 0.9 — "BlackRock to launch Nasdaq-100 ETF as AI rally pulls investors into tech stocks"

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