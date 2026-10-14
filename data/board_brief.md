# Transmission Layer — board brief · 2026-10-14 09:29Z

data as of **2026-10-14** · 97 series · 6 red / 34 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.763, 8d in regime; vol-pct 0.693, breadth-off 0.833, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, contra nifty_50 corr20=0.17, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.23, corr60 0.21, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 0.15, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.06, corr60 -0.06, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.27, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.62, corr60 0.15, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.00016324754740537628)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2178) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.96] usd_inr ↓
- usd_inr [FX]: last 95.09, z20 -2.96, zc -1.34, resid-z -1.34 [quiet], 1d -0.72%, 20d range extreme; |z20|=2.96
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.428 via usd_inr, z 5.03, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.428, z 5.03)
- Source: Rupee rises 44 paise to 94.92 against US dollar in early trade — BusinessLine Mkts, 2026-10-14. https://www.thehindubusinessline.com/markets/forex/rupee-rises-44-paise-to-9492-against-us-dollar-in-early-trade/article71582257.ece
- Source: RBI intervention bolsters rupee, traders say — BusinessLine Mkts, 2026-10-14. https://www.thehindubusinessline.com/markets/forex/rbi-intervention-bolsters-rupee-traders-say/article71582224.ece
- Source: Rupee gains 145 paise in two trading sessions, but disquiet sets in forex market — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/money-and-banking/rupee-gains-145-paise-in-two-trading-sessions-but-disquiet-sets-in-forex-market/article71579835.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 7.03] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 91.80, z20 5.03, zc 4.50, resid-z 3.77 [unexplained], 1d 10.68%, |z20|=5.03
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho -0.428 via dyn_idbi_ns, z -2.96, reacted)
- **India receivers**: usd_inr (rho -0.428, z -2.96)
- Source: IDBI Bank shares rally 13%, market value swells by Rs 11,460 crore amid muted market. What lies ahead? — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/stocks/news/idbi-bank-shares-rally-13-market-value-swells-by-rs-11460-crore-amid-muted-market-what-lies-ahead/articleshow/134934298.cms
- Source: IDBI Bank shares surge 13% today in a weak market - Q2 results expectations, share price trend — Mint Markets, 2026-10-14. https://www.livemint.com/market/stock-market-news/idbi-bank-shares-surge-13-today-in-a-weak-market-q2-results-expectations-share-price-trend-11791953348353.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

### [RED 6.81] cross-asset · 2 series ↑
- dyn_tataelxsi_ns [EQUITIES]: last 3635.60, z20 3.98, zc 2.77, resid-z 3.92 [unexplained], 1d 6.10%, |z20|=3.98
- nifty_it [INDICES]: last 30242.65, z20 3.02, zc 0.58, resid-z 1.22 [quiet], 1d 1.38%, |z20|=3.02
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-31 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho 0.862 via nifty_it, z 1.86, reacted); nifty_fmcg (rho 0.541 via dyn_tataelxsi_ns, z 0.05, quiet); dyn_justdial_bo (rho 0.539 via nifty_it, z 1.24, reacted); dyn_tatatech_ns (rho 0.482 via nifty_it, z 1.5, reacted); nifty_50 (rho 0.479 via dyn_tataelxsi_ns, z -0.72, quiet)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.541 vs dyn_tataelxsi_ns
- **India receivers**: dyn_techm_ns (rho 0.862, z 1.86); nifty_fmcg (rho 0.541, z 0.05); dyn_justdial_bo (rho 0.539, z 1.24); dyn_tatatech_ns (rho 0.482, z 1.5)
- Source: Tata Elxsi stock rebounds as growth improves in Q2. Can it continue? — Mint Markets, 2026-10-14. https://www.livemint.com/market/mark-to-market/tata-elxsi-q2-results-stock-recovery-ai-growth-outlook-11791957021978.html
- Source: Tata Elxsi Q2 results impact: IT stock soars 7%- Buy, sell, or hold? Check highlights, target price, share price trend — Mint Markets, 2026-10-14. https://www.livemint.com/market/stock-market-news/tata-elxsi-q2-results-impact-it-stock-soars-7-buy-sell-or-hold-check-highlights-target-price-share-price-trend-11791906874922.html
- Source: Tata Elxsi shares jump 7% after Q2 results, but Morgan Stanley, Motilal Oswal reiterate bearish calls — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/stocks/news/tata-elxsi-shares-jump-7-after-q2-results-but-morgan-stanley-motilal-oswal-reiterate-bearish-calls/articleshow/134931786.cms
- Historical analogues: 2025-07-31 (d=0.34), 2025-01-30 (d=0.36), 2025-07-09 (d=0.4)

### [RED 4.92] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 70.84, z20 1.92, zc n/a, resid-z n/a [quiet], 1d 0.32%, GSR<75 (extreme low); |z20|=1.92
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.39 via gold_silver_ratio, z -0.41, quiet)
- **India receivers**: midcap_largecap_ratio (rho -0.39, z -0.41)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [AMBER 4.89] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.91, z20 0.95, zc 0.74, resid-z 0.80 [quiet], 1d 1.39%, 1y-pct=97
- ust_30y [RATES]: last 5.60, z20 0.87, zc 0.00, resid-z 0.11 [quiet], 1d 0.00%, 1y-pct=97
- ust_10y [RATES]: last 5.24, z20 0.79, zc 0.38, resid-z 0.49 [quiet], 1d 0.38%, 1y-pct=96
- dyn_bond [EQUITIES]: last 87.08, z20 -0.54, zc 0.38, resid-z 1.21 [quiet], 1d 0.13%, 1y-pct=4
- ust_2y [RATES]: last 4.80, z20 0.26, zc 0.81, resid-z 0.85 [quiet], 1d 1.05%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.643 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.527 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.504 vs ust_30y
- Source: Global Market: Asian investors pour money into hedge funds as bond markets falter — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-asian-investors-pour-money-into-hedge-funds-as-bond-markets-falter/articleshow/134937550.cms
- Source: Global Market: Japan five-year bond yield steady after strong demand at auction — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-five-year-bond-yield-steady-after-strong-demand-at-auction/articleshow/134934716.cms
- Source: U.S. TREASURY YIELDS FALL FOLLOWING FED'S WILLIAMS COMMENTS U.S. Treasury yields moved lower after New York Fed President John Williams signaled one more rate hike in 2026 may be sufficient, with no further increases currently anticipated in 2027. 30-year yield: 5.565% (-3.42 bps) 10-year yield: 5.2 — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37025
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 4.27] dyn_301077_sz ↓
- dyn_301077_sz [EQUITIES]: last 20.40, z20 -2.27, zc -0.98, resid-z -0.36 [quiet], 1d -2.58%, |z20|=2.27
- **Mechanism**: dyn_301077_sz ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Source: China sentences 3 more Myanmar crime bosses to death in scam centre crackdown — SCMP Economy, 2026-10-13. https://www.scmp.com/news/china/politics/article/3370757/china-sentences-3-more-myanmar-crime-bosses-death-scam-centre-crackdown?utm_source=rss_feed
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [AMBER 4.17] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 3149.00, z20 2.17, zc -0.04, resid-z -0.13 [quiet], 1d -0.12%, |z20|=2.17; 1y-pct=96
- **Mechanism**: dyn_cartrade_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: UBS says CarTrade Tech’s OLX buy can deliver 5x revenue in five years. Here’s why — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/stocks/news/ubs-says-cartrade-techs-olx-buy-can-deliver-5x-revenue-in-five-years-heres-why/articleshow/134934907.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 4.11] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3768.06, z20 -2.11, zc -1.23, resid-z 0.81 [quiet], 1d -0.86%, |z20|=2.11; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.375 via shanghai_comp, z -0.39, quiet)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.53 vs shanghai_comp, historically leads by 2d
- **India receivers**: dyn_inoxindia_ns (rho 0.375, z -0.39)
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

## Watchlist (below surfacing floor)
indices · 2 series ↑ (4.06), natgas ↑ (3.79), comex_copper ↑ (3.64), dyn_4417_t ↑ (3.48), dyn_rs ↑ (3.48), dyn_meta ↑ (3.38), kospi ↓ (3.34), nifty_50 ↓ (2.72), dyn_policybzr_ns ↓ (2.63), commodities · 2 series ↓ (2.55), dyn_tech ↑ (2.4), dyn_jiofin_bo ↓ (2.39)

## India macro
- nifty_50: 22612.6504 (1d -0.48%, z20 -0.72, flag amber)
- nifty_midcap_100: 59340.0000 (1d -0.20%, z20 -0.66, flag none)
- usd_inr: 95.0900 (1d -0.72%, z20 -2.96, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6242 (1d 0.28%, z20 -0.41, flag none)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-1d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.1 — "Stock recommendations for 14 October from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.7 — "Stock recommendations for 14 October from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 81.9 — "Indian shares on track for muted open as oil prices, foreign outflows weigh"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.2 — "Stock recommendations for 14 October from MarketSmith India"
- BAC (Bank of America Corporation) score 73.1 — "RBL Bank among 4 F&O stocks with a sharp rise in futures open interest"
- HDB (HDFC Bank Limited) score 66.9 — "RBL Bank among 4 F&O stocks with a sharp rise in futures open interest"
- IDBI.NS (IDBI BANK LIMITED) score 65.4 — "RBL Bank among 4 F&O stocks with a sharp rise in futures open interest"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.4 — "RBL Bank among 4 F&O stocks with a sharp rise in futures open interest"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 65.4 — "RBL Bank among 4 F&O stocks with a sharp rise in futures open interest"
- COIN (Coinbase Global, Inc.) score 56.4 — "Global Market: South Korean shares rebound as chipmakers recover after five-day losing str"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.0 — "LIVE: Canara Bank Q2 quarterly results announced, share price jumps - All eyes on BHEL, Gr"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.1 — "LIVE: Canara Bank Q2 quarterly results announced, share price jumps - All eyes on BHEL, Gr"
- TECH (Bio-Techne Corp) score 54.1 — "LIVE: Canara Bank Q2 quarterly results announced, share price jumps - All eyes on BHEL, Gr"
- OHI (Omega Healthcare Investors, In) score 48.2 — "Durga's many arms: Why diversification is not dilution for investors this Navratri"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.0 — "Indian bonds slip on higher oil, hawkish RBI governor comments"
- TGT (Target Corporation) score 35.3 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.5 — "Global Market | European companies better positioned to withstand energy price shock than "
- CHKP (Check Point Software Technolog) score 31.4 — "IPO GMP comparison: HD Fire Protect vs Fusion CX vs Tonbo Imaging India | Check listing sh"
- LTH (Life Time Group Holdings, Inc.) score 28.1 — "LTCG, STT: Is it opportune time for FM Sitharaman to relook at taxation to contain FIIs se"
- 301077.SZ (CHINASTARS) score 22.3 — "Global Market: China’s yuan firms as investors await US CPI data, assess inflation"
- SEPN (Septerna, Inc.) score 18.6 — "TCS share price rebounds 14% from September low: Can the rally extend further?"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.5 — "Vedanta Power shares jump 13% today after a 5-day loss - Can a rebound in the stock sustai"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.7 — "Tata Elxsi shares jump 7% after Q2 results, but Morgan Stanley, Motilal Oswal reiterate be"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.7 — "Tata Elxsi shares jump 7% after Q2 results, but Morgan Stanley, Motilal Oswal reiterate be"
- JIOFIN.BO (Jio Financial Services Limited) score 13.3 — "Q2 Results Today Live: Canara Bank, CEAT gain; HDB Financial falls nearly 3%, BHEL, Groww,"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.6 — "Buzzing stocks: Watch out for these 16 stocks including Adani Enterprises, Polycab, ICICI "
- BZ=F (Brent Crude Oil Last Day Finan) score 10.5 — "Multibagger chemical stock Himadri Speciality up 40% in last 6 months- should investors bu"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.2 — "Indian families keep just 14% abroad, global peers 30-40%: Prithipal Singh on going global"
- VT (Vanguard Total World Stock Ind) score 9.5 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- RS (Reliance, Inc.) score 9.0 — "A Jigsaw Puzzle: Why Reliance Jio's IPO buzz isn’t saving RIL stock from a painful year?"
- JEF (Jefferies Financial Group Inc.) score 8.5 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.2 — "Down 24% in 3 months, Choice sees 48% upside in this housing finance stock, initiates with"
- GS (Goldman Sachs Group, Inc. (The) score 7.6 — "GOLDMAN SACHS ($GS ) Q3 EARNINGS BEAT ESTIMATES Results * EPS: $17.01 vs. $13.02 est. (+30"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.4 — "Down 24% in 3 months, Choice sees 48% upside in this housing finance stock, initiates with"
- NVDA (NVIDIA Corporation) score 6.4 — "NVDA - NVIDIA TO ANNOUNCE $2 BILLION IN NEW EUROPEAN AI INVESTMENTS Nvidia CEO Jensen Huan"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.0 — "SS Retail shares: Up 95% from IPO price, newly listed stock soars over 19% today on strong"
- META (Meta) score 4.3 — "Meta is back on the AI leaderboard with its new family of Wonder models"
- POLICYBZR.NS (PB FINTECH LIMITED) score 3.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.3 — "Piero Cipollone: Interview with Corriere della Sera"
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