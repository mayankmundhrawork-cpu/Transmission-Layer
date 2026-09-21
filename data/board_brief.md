# Transmission Layer — board brief · 2026-09-21 09:54Z

data as of **2026-09-21** · 97 series · 10 red / 33 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.449, 2d in regime; vol-pct 0.17, breadth-off 0.727, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.26, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.09, corr60 0.28, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.09, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.83, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.04, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.07, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.41, corr60 0.14, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0)
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.304, β 0.0862, p 0.0); driver zc 1.5 → expected 0.4%. Type hit-rate 0.817 (n=2076).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.262, β 0.0315, p 0.00019); driver zc 2.58 → expected 0.368%. Type hit-rate 0.817 (n=2076).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.261, β -0.0575, p 1e-05); driver zc 1.5 → expected -0.267%. Type hit-rate 0.817 (n=2076).
- Track record · residual_reversion: hit-rate **0.499** (n=1096) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2076) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 12.75] sofr ↑
- sofr [RATES]: last 3.85, z20 12.75, zc 9.87, resid-z 9.91 [unexplained], 1d 6.35%, |z20|=12.75
- **Mechanism**: sofr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-06 (d=0.0), 2025-04-17 (d=0.0)

### [RED 8.49] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.67, z20 1.64, zc -1.13, resid-z -1.31 [quiet], 1d -1.48%, |z20|=1.64; 1y-pct=99
- tips_10y_real [RATES]: last 2.61, z20 1.56, zc -1.48, resid-z -1.82 [unexplained], 1d -2.61%, 1d move -7.0bps ≥ 5bps; |z20|=1.56; 1y-pct=99
- dyn_bond [EQUITIES]: last 88.72, z20 -1.45, zc -1.20, resid-z 1.01 [quiet], 1d -0.42%, 1y-pct=1
- ust_10y [RATES]: last 4.94, z20 1.23, zc -1.46, resid-z -1.30 [quiet], 1d -1.40%, 1y-pct=98
- ust_30y [RATES]: last 5.29, z20 0.45, zc -1.49, resid-z -1.16 [quiet], 1d -1.12%, 1y-pct=97
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.445 via ust_2y, z 0.15, quiet)
- Watch next: brent (inverse) — not yet - watch; rho -0.62 vs dyn_bond, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.609 vs dyn_bond, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.54 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.445, z 0.15)
- Source: US Market Outlook: Treasury Yields eye higher — BusinessLine Mkts, 2026-09-19. https://www.thehindubusinessline.com/portfolio/technical-analysis/us-market-outlook-yields-eye-higher/article71483837.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.28] cross-asset · 6 series ↓
- dyn_bac [EQUITIES]: last 57.71, z20 -2.58, zc -0.47, resid-z -0.34 [quiet], 1d -0.81%, |z20|=2.58
- dyn_gs [EQUITIES]: last 941.74, z20 -2.46, zc -0.43, resid-z -0.40 [quiet], 1d -1.02%, |z20|=2.46
- dyn_ms [EQUITIES]: last 202.52, z20 -2.19, zc -0.27, resid-z -0.45 [quiet], 1d -0.49%, |z20|=2.19
- dow_jones [INDICES]: last 51656.25, z20 -1.87, zc -0.27, resid-z -1.03 [quiet], 1d -0.24%, |z20|=1.87
- russell_2000 [INDICES]: last 2859.95, z20 -1.72, zc -0.45, resid-z -0.93 [quiet], 1d -0.51%, |z20|=1.72
- wti [COMMODITIES]: last 94.12, z20 0.13, zc -2.20, resid-z -0.52 [moved], 1d -6.16%, 1-session move -6.16% ≥ 1.5%
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.737 vs dyn_ms, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.664 vs dow_jones, historically leads by 3d
- Watch next: vix (inverse) — not yet - watch; rho -0.647 vs dyn_ms, historically leads by 4d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.526 vs dyn_ms, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.604 vs wti
- Source: Global Market: European shares rise as oil slide boosts risk appetite — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-rise-as-oil-slide-boosts-risk-appetite/articleshow/134381804.cms
- Source: US Market:  Equity funds see fourth straight week of outflows as oil, rate hike concerns mount — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-equity-funds-see-fourth-straight-week-of-outflows-as-oil-rate-hike-concerns-mount/articleshow/134384599.cms
- Source: Strait of Hormuz Shipping Traffic Falls Further as Saudi Oil Flows Rise — OilPrice, 2026-09-21. https://oilprice.com/Latest-Energy-News/World-News/Strait-of-Hormuz-Shipping-Traffic-Falls-Further-as-Saudi-Oil-Flows-Rise.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.68), 2025-05-08 (d=1.07)

### [RED 5.89] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2720.20, z20 5.06, zc 0.98, resid-z 1.85 [unexplained], 1d 4.17%, |z20|=5.06
- btc_usd [CRYPTO]: last 84655.55, z20 4.30, zc 1.50, resid-z 2.52 [unexplained], 1d 4.64%, |z20|=4.30
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-10 (z-distance 0.45).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.423 via btc_usd, z -1.49, reacted)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.602 vs btc_usd, historically leads by 1d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.585 vs eth_usd
- **India receivers**: dyn_cartrade_ns (rho 0.423, z -1.49)
- Historical analogues: 2025-07-10 (d=0.45), 2026-03-16 (d=0.87), 2026-08-21 (d=1.11)

### [RED 5.33] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.76, z20 -2.33, zc n/a, resid-z n/a [quiet], 1d -1.10%, GSR<75 (extreme low); |z20|=2.33
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.374 via gold_silver_ratio, z -0.88, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.859 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.374, z -0.88)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 5.07] dxy ↑
- dxy [FX]: last 100.31, z20 2.07, zc 0.28, resid-z 0.52 [quiet], 1d 0.09%, 20d range extreme; |z20|=2.07
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.04] brent ↓
- brent [COMMODITIES]: last 97.62, z20 -0.04, zc -2.48, resid-z -0.30 [moved], 1d -6.02%, 1-session move -6.02% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.981 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.606 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.563 vs brent, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.64 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.597 vs brent
- Source: Global Market: European shares rise as oil slide boosts risk appetite — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-rise-as-oil-slide-boosts-risk-appetite/articleshow/134381804.cms
- Source: US Market:  Equity funds see fourth straight week of outflows as oil, rate hike concerns mount — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-equity-funds-see-fourth-straight-week-of-outflows-as-oil-rate-hike-concerns-mount/articleshow/134384599.cms
- Source: Strait of Hormuz Shipping Traffic Falls Further as Saudi Oil Flows Rise — OilPrice, 2026-09-21. https://oilprice.com/Latest-Energy-News/World-News/Strait-of-Hormuz-Shipping-Traffic-Falls-Further-as-Saudi-Oil-Flows-Rise.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.48 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Knowledge Marine shares jump 5% then drop 2% despite this work order update - What next? Tech experts decode — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/knowledge-marine-shares-jump-5-then-drop-2-despite-this-work-order-update-what-next-tech-experts-decode-11789968774263.html
- Source: NSE IPO: Will there be a negative listing? But, should you still apply — if yes, then why | What experts suggest — Mint Markets, 2026-09-21. https://www.livemint.com/market/ipo/nse-ipo-will-there-be-a-negative-listing-but-should-you-still-apply-if-yes-then-why-what-experts-suggest-11789965511769.html
- Source: Xi Jinping US visit: Trump to weigh on rare-earth magnet | Experts bet high on Vedanta, GMDC, Ather Energy, other stocks — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/xi-jinping-us-visit-trump-to-weigh-on-rare-earth-magnet-experts-bet-high-on-vedanta-gmdc-ather-energy-other-stocks-11789959864197.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_tatatech_ns ↓ (4.27), comex_copper ↑ (3.81), midcap_largecap_ratio ↑ (3.15), usd_cny ↓ (3.0), fx · 2 series ↓ (2.98), dyn_jiofin_bo ↓ (2.86), dyn_tech ↑ (2.86), ig_oas ↓ (2.62), dyn_lenskart_ns ↑ (2.51), commodities · 2 series ↑ (2.35), ust_2s10s ↓ (2.32), dyn_icicigi_bo ↓ (2.32)

## India macro
- nifty_50: 23429.0000 (1d 0.35%, z20 -0.94, flag none)
- nifty_midcap_100: 62047.9492 (1d -0.23%, z20 -0.88, flag none)
- usd_inr: 95.8000 (1d 0.00%, z20 0.96, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6483 (1d -0.58%, z20 0.15, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 51.7 — "Copper advantage: The missing piece in India’s Viksit Bharat 2047 ambition"
- INOXINDIA.NS (INOX INDIA LIMITED) score 49.8 — "Copper advantage: The missing piece in India’s Viksit Bharat 2047 ambition"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 48.6 — "Copper advantage: The missing piece in India’s Viksit Bharat 2047 ambition"
- INDIANB.NS (INDIAN BANK) score 44.8 — "Australian shares edge lower as banks and miners drag"
- COIN (Coinbase Global, Inc.) score 43.4 — "FPIs turn cautious; withdraw ₹20,974 core from equities in September amid global uncertain"
- BAC (Bank of America Corporation) score 41.2 — "Australian shares edge lower as banks and miners drag"
- HDB (HDFC Bank Limited) score 37.9 — "Australian shares edge lower as banks and miners drag"
- OHI (Omega Healthcare Investors, In) score 35.4 — "Oil slips as investors assess Saudi export recovery"
- CHKP (Check Point Software Technolog) score 34.4 — "Tiger Global-backed Moneyview sets IPO price band for Rs 1,092-crore offer. Check key date"
- IDBI.NS (IDBI BANK LIMITED) score 34.2 — "Australian shares edge lower as banks and miners drag"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.2 — "Australian shares edge lower as banks and miners drag"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.2 — "Australian shares edge lower as banks and miners drag"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.4 — "India bonds calm as oil dip counters US selloff, RBI sales"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 24.2 — "Tata stocks crashed on Friday; investors lost over  ₹52k crore - Will shares bounce back t"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 24.2 — "Tata stocks crashed on Friday; investors lost over  ₹52k crore - Will shares bounce back t"
- LTH (Life Time Group Holdings, Inc.) score 20.2 — "Consumer sentiment is in the dumps despite a solid economy. Goldman Sachs blames 'lower ha"
- TECHM.NS (TECH MAHINDRA LIMITED) score 20.1 — "Knowledge Marine shares jump 5% then drop 2% despite this work order update - What next? T"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 20.1 — "Knowledge Marine shares jump 5% then drop 2% despite this work order update - What next? T"
- TECH (Bio-Techne Corp) score 20.1 — "Knowledge Marine shares jump 5% then drop 2% despite this work order update - What next? T"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.5 — "Britain Faces £150 Billion Grid Overhaul to Power Renewable Energy Boom"
- SEPN (Septerna, Inc.) score 17.6 — "FPIs turn cautious; withdraw ₹20,974 core from equities in September amid global uncertain"
- 301077.SZ (CHINASTARS) score 16.4 — "China is chasing SpaceX and setting its sights on the global space economy"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.8 — "Latest GMP compared: NSE IPO vs Sonaselection India IPO - Last day to apply today | Share "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.6 — "SS Retail IPO allotment likely today: GMP signals 35% listing gain; here's how to check st"
- JIOFIN.BO (Jio Financial Services Limited) score 10.0 — "Apollo Hospital Share Price Live Updates: Apollo Hospital's Financial Snapshot"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.5 — "Xi Jinping US visit: Trump to weigh on rare-earth magnet | Experts bet high on Vedanta, GM"
- VT (Vanguard Total World Stock Ind) score 6.7 — "UN Warns World Must Prepare for Life Beyond 1.5°C"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "Why Adani Total Gas lost 5%, Adani Ports fell 2% despite gains on Sensex, Nifty | Check ho"
- MS (Morgan Stanley) score 6.0 — "JP MORGAN EXPECTS ECB TO DELIVER ANOTHER 25 BP INTEREST RATE HIKE IN MARCH 2027 AFTER A DE"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.8 — "Tata Sons Listing: Even a shareholder having just one Tata Sons share may become a crorepa"
- META (Meta) score 4.4 — "Gold versus industrial metals – Not an “either/or”"
- JEF (Jefferies Financial Group Inc.) score 4.1 — "Adani stocks soar up to 12% after Jefferies sees up to 53% upside in Adani Energy and othe"
- GS (Goldman Sachs Group, Inc. (The) score 3.9 — "Consumer sentiment is in the dumps despite a solid economy. Goldman Sachs blames 'lower ha"
- NVDA (NVIDIA Corporation) score 3.8 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 3.6 — "Bajaj Finance Share Price Live Updates: Bajaj Finance News"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.4 — "Lenskart Solutions share price drops 3% due to a likely  ₹2,047 crore block deal | Details"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.0 — "ICICI Bank Share Price Live Updates: ICICI Bank's Current Market Position"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- DELL (Dell Technologies Inc.) score 0.2 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"

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