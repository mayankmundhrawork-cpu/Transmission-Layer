# Transmission Layer — board brief · 2026-10-28 10:32Z

data as of **2026-10-28** · 97 series · 9 red / 38 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.782, 18d in regime; vol-pct 0.731, breadth-off 0.833, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.39, contra nifty_50 corr20=0.44, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.13, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.1, corr60 0.06, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.29, corr60 -0.02, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.1, corr60 -0.15, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.51, corr60 0.28, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 1.0825087815469203e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.503** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.833** (n=1696) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.04] commodities · 2 series ↑
- wti [COMMODITIES]: last 101.71, z20 1.20, zc 0.68, resid-z -0.04 [quiet], 1d 1.81%, 1-session move +1.81% ≥ 1.5%
- brent [COMMODITIES]: last 111.21, z20 0.87, zc -1.05, resid-z -0.03 [quiet], 1d -2.34%, 1-session move -2.34% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.439 via wti, z -1.11, reacted)
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.407 vs wti, historically leads by 4d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.59 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.54 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.535 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.529 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.439, z -1.11)
- Source: Global shares are mixed after US stock rally, and oil prices gain more than 1% — BusinessLine Mkts, 2026-10-28. https://www.thehindubusinessline.com/markets/global-shares-are-mixed-after-us-stock-rally-and-oil-prices-gain-more-than-1/article71635343.ece
- Source: Indian stocks may rebound in November, but high crude prices pose a risk — BusinessLine Mkts, 2026-10-28. https://www.thehindubusinessline.com/markets/indian-stocks-may-rebound-in-november-but-high-crude-prices-pose-a-risk/article71635188.ece
- Source: Equinor Profits Triple as Oil and Gas Prices Surge — OilPrice, 2026-10-28. https://oilprice.com/Latest-Energy-News/World-News/Equinor-Profits-Triple-as-Oil-and-Gas-Prices-Surge.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 5.98] cross-asset · 5 series ↓
- tips_10y_real [RATES]: last 2.66, z20 -2.05, zc 0.00, resid-z -0.36 [quiet], 1d 0.00%, |z20|=2.05
- ust_30y [RATES]: last 5.31, z20 -2.00, zc -0.43, resid-z -0.44 [quiet], 1d -0.38%, |z20|=2.00
- ust_10y [RATES]: last 5.00, z20 -1.99, zc 0.00, resid-z -0.15 [quiet], 1d 0.00%, |z20|=1.99
- ust_2y [RATES]: last 4.68, z20 -1.86, zc -0.16, resid-z -0.52 [quiet], 1d -0.21%, |z20|=1.86
- dyn_schd [EQUITIES]: last 35.12, z20 1.50, zc -0.56, resid-z 0.09 [quiet], 1d -0.50%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.553 vs dyn_schd, historically leads by 5d
- Watch next: nikkei_225 (inverse) — not yet - watch; rho -0.557 vs dyn_schd
- Watch next: kospi (inverse) — not yet - watch; rho -0.553 vs dyn_schd
- Source: Naukri brand parent Info Edge shares dip after  ₹3 per share dividend move | Check payment, record date, history, yield — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/naukri-brand-parent-info-edge-shares-dip-after-rs-3-per-share-dividend-move-check-payment-record-date-history-yield-11793178605612.html
- Source: US Market: Rising Treasury yields put US banks under pressure over bond losses — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-rising-treasury-yields-put-us-banks-under-pressure-over-bond-losses/articleshow/135260352.cms
- Source: US Market: Treasury yields face pressure despite expected Fed rate pause — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-treasury-yields-face-pressure-despite-expected-fed-rate-pause/articleshow/135256143.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.63), 2025-05-19 (d=1.06)

### [RED 5.66] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.10, z20 3.66, zc 0.19, resid-z 2.40 [unexplained], 1d 0.55%, |z20|=3.66
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US Fed meeting October 2026 today: Expectations, date and time, when & where to watch Kevin Warsh's speech — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/us-fed-meeting-october-2026-today-expectations-date-and-time-when-where-to-watch-kevin-warshs-speech-11793175022190.html
- Source: US Fed Meeting LIVE: Expectations, time, where to watch Kevin Warsh's speech? How rate decision may impact gold, markets — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/us-fed-meeting-live-expectations-time-where-to-watch-kevin-warshs-speech-how-rate-decision-may-impact-gold-markets-11793157523493.html
- Source: Gold, silver prices crash up to 53% from January peak. Time to buy before Dhanteras, festive season? — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-prices-crash-up-to-53-from-january-peak-time-to-buy-before-dhanteras-festive-season/articleshow/135253262.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 5.47] dyn_sepn ↑
- dyn_sepn [EQUITIES]: last 44.09, z20 3.47, zc 1.66, resid-z 0.24 [moved], 1d 6.55%, |z20|=3.47; 1y-pct=98
- **Mechanism**: dyn_sepn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US OCT CONSUMER CONFIDENCE INDEX 91.7 (CONSENSUS 81.0) VS SEPT REVISED 84.2 (PREVIOUS 81.9) - CONFERENCE BOARD — DeItaone, 2026-10-27. https://t.me/walter_bloomberg/37609
- Source: India’s crude steel output rises 5.6% in Jan-Sept even as global production dips — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/commodities/indias-crude-steel-output-rises-56-in-jan-sept-even-as-global-production-dips/article71620869.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [AMBER 5.18] natgas ↑
- natgas [COMMODITIES]: last 3.05, z20 0.18, zc 3.44, resid-z 1.44 [moved], 1d 13.20%, 1-session move +13.20% ≥ 5.0%
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Alleged Russian Funding Prompts Executive Exodus at U.S. LNG Firm — OilPrice, 2026-10-26. https://oilprice.com/Energy/Natural-Gas/Alleged-Russian-Funding-Prompts-Executive-Exodus-at-US-LNG-Firm.html
- Source: The Iran War Just Added $39 Billion to the World's LNG Bill — OilPrice, 2026-10-26. https://oilprice.com/Energy/Natural-Gas/The-Iran-War-Just-Added-39-Billion-to-the-Worlds-LNG-Bill.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 4.91] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1650.00, z20 2.91, zc -0.44, resid-z -0.60 [quiet], 1d -1.43%, |z20|=2.91; 1y-pct=97
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.413 via dyn_atherenerg_ns, z -1.11, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.413, z -1.11)
- Source: Ather Energy shares: 125% YTD returns! Experts give 'portfolio stock' tag after Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/ather-energy-shares-125-ytd-returns-experts-give-portfolio-stock-tag-after-q2-results-2026-target-stoploss-11793080902497.html
- Source: Ather achieves profitability milestone, supply ramp-up to pave the road ahead — Mint Markets, 2026-10-27. https://www.livemint.com/market/mark-to-market/ather-energy-q2-results-net-profit-revenue-growth-11793081766549.html
- Source: Ather Energy shares jump 5%, extend rally to 20% in two days after Q2 results. Can the run continue? — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-jump-5-extend-rally-to-20-in-two-days-after-q2-results-can-the-run-continue/articleshow/135225009.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 4.76] dyn_tgt ↓
- dyn_tgt [EQUITIES]: last 148.00, z20 -2.76, zc -0.19, resid-z -1.60 [unexplained], 1d -0.36%, |z20|=2.76
- **Mechanism**: dyn_tgt ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho -0.36 via dyn_tgt, z -1.56, reacted)
- **India receivers**: dyn_adanient_bo (rho -0.36, z -1.56)
- Source: Morgan Stanley turns bullish on Paytm, raises target 35% to ₹1,950 on earnings upside — BusinessLine Mkts, 2026-10-28. https://www.thehindubusinessline.com/markets/morgan-stanley-turns-bullish-on-paytm-raises-target-35-to-1950-on-earnings-upside/article71634940.ece
- Source: Multibagger defence stock Raymond retraces after jumping 7% amid weak trends on D-Street | Check target, upside — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/multibagger-defence-stock-raymond-retraces-after-jumping-7-amid-weak-trends-on-d-street-check-target-upside-11793168220033.html
- Source: Maruti Suzuki shares see target price cuts by Jefferies, Nomura, other brokerages after Q2 net profit drops 26% YoY. What’s ahead? — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/stocks/news/maruti-suzuki-shares-see-target-price-cuts-by-jefferies-nomura-other-brokerages-after-q2-net-profit-drops-26-yoy-whats-ahead/articleshow/135254335.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [AMBER 4.71] commodities · 2 series ↓
- wheat [COMMODITIES]: last 611.00, z20 -1.88, zc 0.08, resid-z -0.46 [quiet], 1d 0.12%, |z20|=1.88
- corn [COMMODITIES]: last 450.50, z20 -1.62, zc 0.29, resid-z -0.89 [quiet], 1d 0.39%, |z20|=1.62
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn drops on US harvest pressure, wheat near 3-1/2-month low — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/commodities/corn-drops-on-us-harvest-pressure-wheat-near-3-12-month-low/article71629668.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.35), 2025-08-28 (d=0.36)

## Watchlist (below surfacing floor)
dyn_meta ↓ (4.7), cross-asset · 2 series ↑ (4.64), dyn_rs ↑ (4.61), dyn_coalindia_ns ↓ (4.47), dyn_chkp ↑ (4.41), dyn_hdb ↓ (4.41), dyn_cartrade_ns ↓ (4.36), eur_usd ↓ (4.34), dyn_tatatech_ns ↓ (4.12), dyn_gs ↑ (4.04), dyn_jiofin_bo ↓ (3.94), dyn_4417_t ↑ (3.67)

## India macro
- nifty_50: 22698.8496 (1d -0.22%, z20 0.10, flag none)
- nifty_midcap_100: 57268.4492 (1d 0.42%, z20 -1.11, flag none)
- usd_inr: 95.2200 (1d 0.03%, z20 -0.49, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5230 (1d 0.64%, z20 -1.10, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 96.8 — "Ambani looks to defy gravity in debut after India-record Jio IPO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 96.0 — "Ambani looks to defy gravity in debut after India-record Jio IPO"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 94.4 — "Ambani looks to defy gravity in debut after India-record Jio IPO"
- INDIANB.NS (INDIAN BANK) score 64.5 — "Indian shares set for lower open as oil rise weighs; Jio market debut in focus"
- BAC (Bank of America Corporation) score 57.7 — "LT Foods H1 FY27 revenue rises 22%, North America drives growth; shares in red"
- TGT (Target Corporation) score 55.9 — "Reliance Industries shares slip 2% amid Jio Platforms IPO listing | Key RIL targets and le"
- COIN (Coinbase Global, Inc.) score 51.1 — "Global Market: South Korean shares surge 6% as SK Hynix earnings fuel AI chip rally"
- OHI (Omega Healthcare Investors, In) score 50.7 — "Jio Platforms IPO listing today: Should investors chase listing gains or hold for the long"
- HDB (HDFC Bank Limited) score 48.8 — "US Market: Rising Treasury yields put US banks under pressure over bond losses"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 48.3 — "US Market: Rising Treasury yields put US banks under pressure over bond losses"
- IDBI.NS (IDBI BANK LIMITED) score 48.0 — "US Market: Rising Treasury yields put US banks under pressure over bond losses"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 48.0 — "US Market: Rising Treasury yields put US banks under pressure over bond losses"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.1 — "Global Market: Japan’s Nikkei jumps over 1% as tech rally on Wall Street lifts sentiment"
- CHKP (Check Point Software Technolog) score 42.7 — "Jio Platforms IPO listing today: Check exact time of shares trading; expected debut stock "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.2 — "Global Market: Japan’s Nikkei jumps over 1% as tech rally on Wall Street lifts sentiment"
- TECH (Bio-Techne Corp) score 40.2 — "Global Market: Japan’s Nikkei jumps over 1% as tech rally on Wall Street lifts sentiment"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.2 — "Q2 Results Today Live: Adani Enterprises & Hyundai Q2 profit down, Adani Ports Q2 con. pro"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 27.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 27.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Today"
- LTH (Life Time Group Holdings, Inc.) score 26.7 — "Jio Platforms IPO listing today: Check exact time of shares trading; expected debut stock "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 26.6 — "Jio Platforms IPO listing today: Should investors chase listing gains or hold for the long"
- RS (Reliance, Inc.) score 26.6 — "Reliance Industries Q2 results 2026 date and time: Mukesh Ambani company's quarterly earni"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.9 — "India bonds sink on oil spike before Fed decision"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.8 — "Bajaj Finserv Share Price Live Updates: Bajaj Finserv's Financial Overview"
- 301077.SZ (CHINASTARS) score 20.7 — "Global Market: China, Hong Kong stocks rebound as SK Hynix earnings lift AI optimism"
- JIOFIN.BO (Jio Financial Services Limited) score 17.6 — "OPENAI REPORTEDLY PLANS TO BUY GOOGLE AI CHIPS OpenAI plans to purchase AI chips from Goog"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.1 — "Housing is flashing warning signs just as the Fed weighs more interest rate hikes"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.9 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.0 — "Top stocks to watch today: Jio Platforms, RIL, HUL, Adani Enterprises shares in focus on W"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "Diwali 2026: Sensex plunged 10,000 points, Nifty dropped 12% since last Diwali. Will Samva"
- JEF (Jefferies Financial Group Inc.) score 12.9 — "L&T shares rally 6% after Q2 net profit jumps 33% YoY. Why Jefferies cut target price?"
- SEPN (Septerna, Inc.) score 12.9 — "Today’s Gold Rate, September 23: Check gold rates in Delhi, Mumbai, Chennai"
- META (Meta) score 11.4 — "AMD $META - AMD AND META ADVANCE STRATEGIC PARTNERSHIP TO POWER META’S SUPERINTELLIGENCE I"
- SCHD (Schwab US Dividend Equity ETF) score 10.5 — "SK Hynix profit beat fuels $45 billion of dividends, buyback"
- INFY (Infosys Limited) score 8.6 — "Infosys, TechM, TCS, other IT stocks plunge up to 5%, extend losses as global AI trade reb"
- VT (Vanguard Total World Stock Ind) score 7.6 — "World Bank's Banga: Availability of capital 'not really an issue' as AI demand drives up b"
- GS (Goldman Sachs Group, Inc. (The) score 7.2 — "Paytm shares rise 2% after Q2 results. What are Jefferies, Goldman Sachs, and others sayin"
- SWIGGY.NS (SWIGGY LIMITED) score 3.4 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.0 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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