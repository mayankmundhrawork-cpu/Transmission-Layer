# Transmission Layer — board brief · 2026-10-21 15:13Z

data as of **2026-10-21** · 97 series · 12 red / 32 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.746, 13d in regime; vol-pct 0.727, breadth-off 0.765, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.21, corr60 -0.37, contra nifty_50 corr20=0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.82, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.11, corr60 0.1, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.02, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.2, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.49, corr60 0.22, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.385731695004779e-10)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.5** (n=1127) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=1959) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.3] usd_inr ↓
- usd_inr [FX]: last 94.45, z20 -2.30, zc -1.08, resid-z -1.28 [quiet], 1d -0.57%, 20d range extreme; |z20|=2.30
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.382 via usd_inr, z -1.98, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.382, z -1.98)
- Source: Rupee rises 46 paise to 94.45 on India-US trade deal hopes; oil prices cap gains — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-46-paise-to-94-45-on-india-us-trade-deal-hopes-oil-prices-cap-gains/articleshow/135092741.cms
- Source: Jio Platforms' IPO-linked inflows boost rupee; elevated oil prices spur caution — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/forex/forex-news/jio-platforms-ipo-linked-inflows-boost-rupee-elevated-oil-prices-spur-caution/articleshow/135089592.cms
- Source: IMF advises India to let rupee move as first defence amid oil shock — BusinessLine Mkts, 2026-10-21. https://www.thehindubusinessline.com/economy/imf-advises-india-to-let-rupee-move-as-first-defence-amid-oil-shock/article71607130.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.81] commodities · 2 series ↑
- brent [COMMODITIES]: last 109.21, z20 1.64, zc 0.20, resid-z 0.27 [quiet], 1d 0.39%, |z20|=1.64
- wti [COMMODITIES]: last 97.83, z20 0.97, zc -1.60, resid-z -1.43 [moved], 1d -3.89%, 1-session move -3.89% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.589 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.586 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.575 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.548 vs brent
- Source: EIA Says US Crude Inventories Sink Further — OilPrice, 2026-10-21. https://oilprice.com/Energy/Crude-Oil/EIA-Says-US-Crude-Inventories-Sink-Further.html
- Source: Higher Oil Availability Pressures Middle East Crude Benchmarks — OilPrice, 2026-10-21. https://oilprice.com/Latest-Energy-News/World-News/Higher-Oil-Availability-Pressures-Middle-East-Crude-Benchmarks.html
- Source: Rupee rises 46 paise to 94.45 on India-US trade deal hopes; oil prices cap gains — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-46-paise-to-94-45-on-india-us-trade-deal-hopes-oil-prices-cap-gains/articleshow/135092741.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.63] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1834.70, z20 3.31, zc -0.20, resid-z 0.71 [quiet], 1d 3.13%, |z20|=3.31; 1y-pct=100
- nifty_it [INDICES]: last 32422.50, z20 2.87, zc -0.63, resid-z 0.27 [quiet], 1d 2.88%, |z20|=2.87
- dyn_tataelxsi_ns [EQUITIES]: last 3848.60, z20 2.28, zc -0.61, resid-z 0.38 [quiet], 1d 1.55%, |z20|=2.28
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.521 via dyn_tataelxsi_ns, z -0.02, quiet); dyn_justdial_bo (rho 0.513 via nifty_it, z 4.18, reacted); nifty_fmcg (rho 0.489 via dyn_tataelxsi_ns, z -1.74, reacted); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -3.36, reacted); dyn_tatatech_ns (rho 0.403 via nifty_it, z -1.22, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.514 vs nifty_it
- **India receivers**: nifty_50 (rho 0.521, z -0.02); dyn_justdial_bo (rho 0.513, z 4.18); nifty_fmcg (rho 0.489, z -1.74); midcap_largecap_ratio (rho -0.439, z -3.36)
- Source: Mahindra Finance Q2 net profit surges 55% to Rs 882 crore on volumes, lower credit cost — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-finance-q2-net-profit-surges-55-to-rs-882-crore-on-volumes-lower-credit-cost/articleshow/135094556.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 6.18] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 765.15, z20 4.18, zc 0.82, resid-z 1.21 [quiet], 1d 4.45%, |z20|=4.18
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.513 via dyn_justdial_bo, z 2.87, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.31, reacted); nifty_50 (rho 0.454 via dyn_justdial_bo, z -0.02, quiet); dyn_tataelxsi_ns (rho 0.396 via dyn_justdial_bo, z 2.28, reacted); nifty_midcap_100 (rho 0.351 via dyn_justdial_bo, z -1.79, reacted)
- **India receivers**: nifty_it (rho 0.513, z 2.87); dyn_techm_ns (rho 0.505, z 3.31); nifty_50 (rho 0.454, z -0.02); dyn_tataelxsi_ns (rho 0.396, z 2.28)
- Source: Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss by Anand Rathi's expert — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-short-term-just-dial-bse-orient-hotels-target-price-stop-loss-by-anand-rathis-expert-11792400725179.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [RED 4.88] usd_cny ↓
- usd_cny [FX]: last 6.66, z20 -4.88, zc -4.17, resid-z -6.28 [unexplained], 1d -0.40%, |z20|=4.88; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [RED 4.82] dyn_wit ↑
- dyn_wit [EQUITIES]: last 2.09, z20 2.82, zc 0.50, resid-z -0.06 [quiet], 1d 1.95%, |z20|=2.82
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - Check stop loss, targets — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/top-2-stocks-to-buy-or-sell-for-short-term-wipro-dixon-technologies-by-nagaraj-shetti-check-stop-loss-targets-11792580012562.html
- Source: IT stocks on fire, rally up to 15% today; check performance of TCS, L&T Technology, Wipro, Infosys | Jefferies bullish — Mint Markets, 2026-10-21. https://www.livemint.com/market/stock-market-news/it-stocks-on-fire-rally-up-to-15-today-check-performance-of-tcs-l-t-technology-wipro-infosys-jefferies-bulli-11792559488325.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [RED 4.72] natgas ↓
- natgas [COMMODITIES]: last 2.84, z20 -2.72, zc -1.26, resid-z -1.84 [unexplained], 1d -4.22%, |z20|=2.72
- **Mechanism**: natgas ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.122 vs natgas, historically leads by 4d
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.075 vs natgas, historically leads by 4d
- Source: Asian LNG Prices Surge Past $30 as Middle East Shipping Risks Escalate — OilPrice, 2026-10-20. https://oilprice.com/Latest-Energy-News/World-News/Asian-LNG-Prices-Surge-Past-30-as-Middle-East-Shipping-Risks-Escalate.html
- Source: Qatar Offers Lebanon 2 Gas Plants and 20 Years of LNG Piped Through Syria — OilPrice, 2026-10-19. https://oilprice.com/Latest-Energy-News/World-News/Qatar-Offers-Lebanon-2-Gas-Plants-and-20-Years-of-LNG-Piped-Through-Syria.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 4.55] commodities · 3 series ↓
- wheat [COMMODITIES]: last 625.75, z20 -3.23, zc -1.59, resid-z -1.38 [moved], 1d -2.72%, |z20|=3.23
- soybeans [COMMODITIES]: last 1244.25, z20 -2.18, zc -0.32, resid-z -0.40 [quiet], 1d -0.32%, |z20|=2.18
- corn [COMMODITIES]: last 460.25, z20 -1.81, zc -0.27, resid-z -0.26 [quiet], 1d -0.38%, |z20|=1.81
- **Mechanism**: commodities · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

## Watchlist (below surfacing floor)
dow_jones ↑ (4.46), dyn_4417_t ↑ (4.1), dyn_bajfinance_ns ↓ (4.1), gold_silver_ratio ↑ (3.99), dyn_rs ↑ (3.86), gbp_usd ↑ (3.38), tips_10y_real ↓ (3.36), midcap_largecap_ratio ↓ (3.36), hy_oas ↑ (3.31), dyn_jiofin_bo ↓ (3.21), cross-asset · 3 series ↓ (3.11), dyn_inoxindia_ns ↓ (3.08)

## India macro
- nifty_50: 22811.3496 (1d -0.34%, z20 -0.02, flag none)
- nifty_midcap_100: 57568.7500 (1d -1.56%, z20 -1.79, flag amber)
- usd_inr: 94.4500 (1d -0.57%, z20 -2.30, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5237 (1d -1.23%, z20 -3.36, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 88.9 — "From Dhirubhai to Akash Ambani, Reliance made stocks popular with Indians"
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.4 — "From Dhirubhai to Akash Ambani, Reliance made stocks popular with Indians"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.1 — "From Dhirubhai to Akash Ambani, Reliance made stocks popular with Indians"
- INDIANB.NS (INDIAN BANK) score 83.5 — "From Dhirubhai to Akash Ambani, Reliance made stocks popular with Indians"
- BAC (Bank of America Corporation) score 71.6 — "Want exposure to India's biggest banks? Zerodha launches new ETF"
- HDB (HDFC Bank Limited) score 66.2 — "Want exposure to India's biggest banks? Zerodha launches new ETF"
- IDBI.NS (IDBI BANK LIMITED) score 63.8 — "Want exposure to India's biggest banks? Zerodha launches new ETF"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 63.8 — "Want exposure to India's biggest banks? Zerodha launches new ETF"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 63.8 — "Want exposure to India's biggest banks? Zerodha launches new ETF"
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.5 — "Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.0 — "Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - "
- TECH (Bio-Techne Corp) score 55.0 — "Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - "
- COIN (Coinbase Global, Inc.) score 53.5 — "Global Market: UK inflation rises to 3.5% in September, boosting rate hike bets"
- OHI (Omega Healthcare Investors, In) score 51.3 — "CITADEL’S KEN GRIFFIN: WE’RE ALMOST CERTAINLY IN AN AI BUBBLE Billionaire Ken Griffin warn"
- CHKP (Check Point Software Technolog) score 42.1 — "Jio IPO Day 1: Issue subscribed 3 times on strong QIB push; retail portion booked 68%. Che"
- TGT (Target Corporation) score 39.0 — "Acme Solar vs NTPC Green: Renewable stocks in focus - Check what Nomura prefers | Share pr"
- RS (Reliance, Inc.) score 33.5 — "From Dhirubhai to Akash Ambani, Reliance made stocks popular with Indians"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.4 — "Global Market: Eurozone bond yields rise as French unrest fuels fiscal concerns"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.5 — "UK Approves Jackdaw Gas Field as Energy Crisis Deepens"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.4 — "Eternal shares: Will Deepinder Goyal's Temple device and Dark AI venture impact Zomato sto"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.5 — "Market wrap: Infosys, HCL Tech, Bajaj Finance, BSE top gainers and losers on Nifty and Sen"
- 301077.SZ (CHINASTARS) score 22.2 — "How Bad Would It Get If China Blocks Rare Earths to America?"
- LTH (Life Time Group Holdings, Inc.) score 21.5 — "Jio IPO Day 1: Issue subscribed 3 times on strong QIB push; retail portion booked 68%. Che"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 18.6 — "Market wrap: Infosys, HCL Tech, Bajaj Finance, BSE top gainers and losers on Nifty and Sen"
- JIOFIN.BO (Jio Financial Services Limited) score 15.4 — "Jio IPO strengthens Reliance’s financial flexibility; capex funding remains key: Moody’s"
- SEPN (Septerna, Inc.) score 13.3 — "Global Market: UK inflation rises to 3.5% in September, boosting rate hike bets"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "Paras Healthcare IPO: Can higher occupancy deliver lasting profit?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.3 — "RIL's stock climbs 2% as Jio Platforms IPO achieves full subscription in just 100 minutes"
- GS (Goldman Sachs Group, Inc. (The) score 12.0 — "Goldman Sachs Warns of New Oil Price Shock as Tanker Rates Soar"
- META (Meta) score 11.1 — "Meta’s AI spending spree has investors taking a page from the financial-crisis playbook"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.9 — "IHCL Q2 Results: Tata Group-owned hotel chain's net profit jumps 19% to Rs 379 crore"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.9 — "IHCL Q2 Results: Tata Group-owned hotel chain's net profit jumps 19% to Rs 379 crore"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.2 — "Adani Green Q2 Results: Profit rises 15% YoY to Rs 673 crore; revenue jumps 39%"
- JEF (Jefferies Financial Group Inc.) score 9.1 — "UltraTech Cement shares jump 3% as brokerages revise target prices after Q2 results. What "
- VT (Vanguard Total World Stock Ind) score 6.1 — "In charts: How one of the world's biggest economies got trapped by debt"
- NVDA (NVIDIA Corporation) score 4.6 — "DEEPSEEK AND HUAWEI ARE COLLABORATING ON NEW AI CHIP DESIGNS TO CHALLENGE NVIDIA - THE IN "
- WIT (Wipro Limited) score 4.5 — "Top 2 stocks to buy or sell for short-term: Wipro, Dixon Technologies by Nagaraj Shetti - "
- DELL (Dell Technologies Inc.) score 1.6 — "Super Micro’s stock soars after surprise update — with Dell and HPE shares joining the ral"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.6 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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