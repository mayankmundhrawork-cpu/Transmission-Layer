# Transmission Layer — board brief · 2026-10-12 11:54Z

data as of **2026-10-12** · 97 series · 6 red / 37 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.808, 6d in regime; vol-pct 0.706, breadth-off 0.909, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.41, contra nifty_50 corr20=0.27, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.22, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.07, corr60 0.13, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.11, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.29, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.67, corr60 0.17, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1136) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2058) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 5.42] cross-asset · 4 series ↓
- india_vix [INDICES]: last 15.24, z20 1.76, zc -0.99, resid-z n/a [quiet], 1d 6.02%, |z20|=1.76
- nifty_fmcg [INDICES]: last 44112.75, z20 -1.61, zc 2.25, resid-z 1.59 [unexplained], 1d -1.68%, |z20|=1.61; 1y-pct=1
- nifty_50 [INDICES]: last 22363.35, z20 -1.58, zc 1.55, resid-z 2.23 [unexplained], 1d -0.70%, |z20|=1.58; 1y-pct=1
- dyn_policybzr_ns [EQUITIES]: last 1047.00, z20 -0.83, zc 0.38, resid-z -0.68 [quiet], 1d 3.46%, 1y-pct=3
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-14 (z-distance 0.64).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.782 via nifty_50, z -1.21, reacted); dyn_jiofin_bo (rho 0.61 via nifty_50, z -1.38, reacted); nifty_metal (rho 0.583 via nifty_50, z -2.16, reacted); dyn_bajfinance_ns (rho -0.527 via india_vix, z -1.05, reacted); dyn_justdial_bo (rho 0.52 via nifty_50, z -0.72, quiet)
- Watch next: dyn_justdial_bo (co-move) — not yet - watch; rho 0.52 vs nifty_50
- Watch next: ig_oas (inverse) — not yet - watch; rho -0.511 vs dyn_policybzr_ns
- **India receivers**: nifty_midcap_100 (rho 0.782, z -1.21); dyn_jiofin_bo (rho 0.61, z -1.38); nifty_metal (rho 0.583, z -2.16); dyn_bajfinance_ns (rho -0.527, z -1.05)
- Source: Sensex today | Stock Market Highlights: Stock markets tumble on oil price spike, foreign fund outflows; Sensex drops 548 points — BusinessLine Mkts, 2026-10-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-12-october-2026/article71571162.ece
- Source: Stock market prediction for tomorrow: Sensex, Nifty outlook for Tuesday | Kospi, Taiwan cues to watch | 13 Oct 2026 — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/stock-market-prediction-for-tomorrow-sensex-nifty-outlook-for-tuesday-kospi-taiwan-cues-to-watch-13-oct-2026-11791799942402.html
- Source: Q2 results 2026: Can corporate earnings halt Sensex, Nifty sell-off? Experts decode — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/q2-results-2026-can-corporate-earnings-halt-sensex-nifty-sell-off-experts-decode-11791796933685.html
- Historical analogues: 2025-07-14 (d=0.64), 2025-07-21 (d=0.65), 2025-07-31 (d=1.1)

### [RED 5.14] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -5.14, zc -0.33, resid-z -0.11 [quiet], 1d -0.30%, |z20|=5.14; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.363 via usd_cny, z -0.83, quiet)
- **India receivers**: dyn_policybzr_ns (rho -0.363, z -0.83)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.94] cross-asset · 3 series ↑
- sp500 [INDICES]: last 7811.09, z20 1.62, zc 0.83, resid-z -1.45 [quiet], 1d 0.59%, |z20|=1.62; 1y-pct=99
- nasdaq_100 [INDICES]: last 30881.86, z20 0.91, zc 0.47, resid-z -0.78 [quiet], 1d 0.51%, 1y-pct=98
- dyn_nvda [EQUITIES]: last 229.34, z20 0.39, zc -0.23, resid-z -1.26 [quiet], 1d -0.49%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.952 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.724 vs sp500, historically leads by 4d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.887 vs sp500
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.86 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.637 vs sp500
- Source: Nifty holds flat at open despite Wall Street gains; FII selling streak hits 11 sessions — BusinessLine Mkts, 2026-10-12. https://www.thehindubusinessline.com/markets/nifty-holds-flat-at-open-despite-wall-street-gains-fii-selling-streak-hits-11-sessions/article71573720.ece
- Source: Wall Street’s rate shock spreads beneath AI-fueled market rally — BusinessLine Mkts, 2026-10-10. https://www.thehindubusinessline.com/markets/wall-streets-rate-shock-spreads-beneath-ai-fueled-market-rally/article71568541.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.18), 2025-08-28 (d=0.22)

### [AMBER 4.62] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.60, z20 0.95, zc -1.74, resid-z -2.34 [unexplained], 1d -1.23%, 1y-pct=97
- dyn_bond [EQUITIES]: last 86.93, z20 -0.86, zc 0.02, resid-z 0.58 [quiet], 1d 0.01%, 1y-pct=2
- tips_10y_real [RATES]: last 2.87, z20 0.73, zc -0.90, resid-z -1.52 [unexplained], 1d -1.71%, 1y-pct=96
- ust_10y [RATES]: last 5.22, z20 0.72, zc -1.12, resid-z -1.95 [unexplained], 1d -1.14%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 1d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.585 vs dyn_bond
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.535 vs ust_30y
- Source: The bond market is doing the Fed’s job, and that could be good news for stocks, says Morgan Stanley strategist — MarketWatch Top, 2026-10-12. https://www.marketwatch.com/story/the-bond-market-is-doing-the-feds-job-and-that-could-be-good-news-for-stocks-says-morgan-stanley-strategist-ec57b81a?mod=mw_rss_topstories
- Source: US Market: Four warning signs that bond selling could intensify — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-market-four-warning-signs-that-bond-selling-could-intensify/articleshow/134886417.cms
- Source: Global Market: Eurozone bond yields ease as Russia-Ukraine energy truce lifts sentiment — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-ease-as-russia-ukraine-energy-truce-lifts-sentiment/articleshow/134886214.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.48] dxy ↑
- dxy [FX]: last 102.42, z20 1.48, zc 0.20, resid-z -0.13 [quiet], 1d 0.21%, 20d range extreme; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.508 vs dxy, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [AMBER 4.14] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2631.00, z20 -2.14, zc 0.43, resid-z -0.18 [quiet], 1d -0.08%, |z20|=2.14
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.556 via dyn_adanient_bo, z -2.16, reacted); nifty_50 (rho 0.383 via dyn_adanient_bo, z -1.58, reacted); nifty_midcap_100 (rho 0.373 via dyn_adanient_bo, z -1.21, reacted)
- **India receivers**: nifty_metal (rho 0.556, z -2.16); nifty_50 (rho 0.383, z -1.58); nifty_midcap_100 (rho 0.373, z -1.21)
- Source: Elara initiates coverage on Adani Power, sees  up to 17% upside as expansion plans gather pace — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/stocks/news/elara-initiates-coverage-on-adani-power-sees-up-to-17-upside-as-expansion-plans-gather-pace/articleshow/134890260.cms
- Source: Jefferies sees 35% upside in Adani Green shares, flags demand and execution triggers — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-sees-35-upside-in-adani-green-shares-flags-demand-and-execution-triggers/articleshow/134889828.cms
- Source: Adani Green Energy shares up 16% in 6 months, Jefferies sees 35% more upside in Gautam Adani-owned stock | Target price — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/adani-green-energy-shares-up-16-in-6-months-jefferies-sees-35-more-upside-in-gautam-adani-owned-stock-target-price-11791785755069.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.08] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3794.60, z20 -2.08, zc 0.07, resid-z -0.29 [quiet], 1d -0.50%, |z20|=2.08; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.406 via shanghai_comp, z -0.06, quiet)
- **India receivers**: dyn_inoxindia_ns (rho 0.406, z -0.06)
- Source: Global Market: China stocks fall as global yields, geopolitical tensions weigh on sentiment — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-global-yields-geopolitical-tensions-weigh-on-sentiment/articleshow/134884757.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [AMBER 3.88] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 6580.00, z20 1.88, zc -0.07, resid-z 2.45 [unexplained], 1d -0.45%, 1y-pct=99
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Q2 results 2026: Can corporate earnings halt Sensex, Nifty sell-off? Experts decode — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/q2-results-2026-can-corporate-earnings-halt-sensex-nifty-sell-off-experts-decode-11791796933685.html
- Source: IFCI share price jumps 14% in 3 sessions - Can the stock rise further? Tech experts decode? — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/ifci-share-price-jumps-14-in-3-sessions-can-the-stock-rise-further-tech-experts-decode-11791781850755.html
- Source: RIL shares: Reliance Industries stock slides 6% in a month, can Jio Platforms IPO aid the bounce back? Experts' views — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/ril-shares-reliance-industries-stock-slides-6-in-a-month-can-jio-platforms-ipo-aid-the-bounce-back-experts-views-11791781439943.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_cartrade_ns ↑ (3.72), gold_silver_ratio ↑ (3.53), dyn_rs ↑ (3.5), kospi ↓ (3.39), dyn_karurvysya_ns ↑ (3.03), commodities · 2 series ↓ (3.0), dyn_hdb ↓ (2.98), dyn_techm_ns ↓ (2.89), dyn_coalindia_ns ↓ (2.59), bovespa ↑ (2.34), dyn_tech ↑ (2.21), nifty_metal ↓ (2.16)

## India macro
- nifty_50: 22363.3496 (1d -0.70%, z20 -1.58, flag amber)
- nifty_midcap_100: 58847.1016 (1d 0.11%, z20 -1.21, flag none)
- usd_inr: 95.7600 (1d -1.10%, z20 -0.71, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6314 (1d 0.82%, z20 -0.16, flag none)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India WPI T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 71.3 — "Today’s Gold Rate in India October 10: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, "
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.8 — "Today’s Gold Rate in India October 10: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 67.5 — "Today’s Gold Rate in India October 10: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, "
- INDIANB.NS (INDIAN BANK) score 55.8 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- BAC (Bank of America Corporation) score 49.4 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- HDB (HDFC Bank Limited) score 44.7 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- IDBI.NS (IDBI BANK LIMITED) score 42.4 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.4 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.4 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- COIN (Coinbase Global, Inc.) score 39.8 — "Global Markets: 5 key triggers to watch out for this week"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.4 — "China’s Zhejiang province calls to limit tech giants’ power over online traffic"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 34.5 — "China’s Zhejiang province calls to limit tech giants’ power over online traffic"
- TECH (Bio-Techne Corp) score 34.5 — "China’s Zhejiang province calls to limit tech giants’ power over online traffic"
- OHI (Omega Healthcare Investors, In) score 33.6 — "Kotak Life, investors Mukul Agrawal, Ashish Kacholia acquire shares in Fusion CX ahead of "
- BOND (PIMCO Active Bond Exchange-Tra) score 32.4 — "Rupee to rally on fresh RBI measures, bonds eye inflation prints"
- LTH (Life Time Group Holdings, Inc.) score 26.7 — "NSE cash market ADTV dips to six month low on bearish market sentiments"
- TGT (Target Corporation) score 26.6 — "Pemex Needs Nearly $110 Billion to Hit Mexico's Output Targets"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.4 — "3 Stocks To Play The Nuclear Energy Boom"
- CHKP (Check Point Software Technolog) score 21.9 — "Zee Entertainment shares extend gains for second session, rises 7% today | Check stock per"
- SEPN (Septerna, Inc.) score 19.7 — "India equity mutual fund inflows hit 5-month high in September despite Nifty slump"
- 301077.SZ (CHINASTARS) score 18.7 — "China’s Zhejiang province calls to limit tech giants’ power over online traffic"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.2 — "RIL shares: Reliance Industries stock slides 6% in a month, can Jio Platforms IPO aid the "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.3 — "Stocks to Watch, Oct 12: Lenskart, Everyday Ind, SJS, Authum, Adani enterprise, M&M"
- JIOFIN.BO (Jio Financial Services Limited) score 9.9 — "‘The prospectus looks impressive’: My financial adviser wants me to invest $350,000 in a U"
- JEF (Jefferies Financial Group Inc.) score 9.2 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.3 — "Tata Steel slips marginally as draft steel policy 2047 puts sector in focus"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.3 — "Tata Steel slips marginally as draft steel policy 2047 puts sector in focus"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "Here’s why Goldman Sachs just flipped bullish on stocks for the rest of the year"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.6 — "Up 50% in 6 months! Small-cap stock Aye Finance rises today despite weak market - Q2 busin"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.3 — "Emergency Oil Releases Risk Draining the World’s Last Supply Cushion"
- VT (Vanguard Total World Stock Ind) score 7.2 — "Emergency Oil Releases Risk Draining the World’s Last Supply Cushion"
- RS (Reliance, Inc.) score 7.1 — "RIL shares: Reliance Industries stock slides 6% in a month, can Jio Platforms IPO aid the "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 6.1 — "Up 50% in 6 months! Small-cap stock Aye Finance rises today despite weak market - Q2 busin"
- META (Meta) score 5.6 — "IPO: Who really owns Jio Platforms? Reliance doesn't own 100%; Meta, Google, 7 others are "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.0 — "Retail stocks to buy before Q2 results: Metro Brands, Campus Activewear, Vishal Mega Mart "
- NVDA (NVIDIA Corporation) score 5.0 — "NVDA - UBS REAFFIRMS NVIDIA BUY RATING WITH $300 PRICE TARGET UBS reiterated its Buy ratin"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "Global Market: Goldman Sachs raises December Brent oil price forecast to $90 on supply ris"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.3 — "Nomura becomes latest brokerage to cut PB Fintech share price target by 31%, lists 2 scena"
- DELL (Dell Technologies Inc.) score 0.4 — "Piero Cipollone: Interview with Corriere della Sera"
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