# Transmission Layer — board brief · 2026-10-12 21:16Z

data as of **2026-10-12** · 97 series · 7 red / 34 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.753, 6d in regime; vol-pct 0.706, breadth-off 0.8, Markov P(high-vol) 0.015)
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
- Track record · transmission_follow: hit-rate **0.828** (n=2114) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
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
- Source: Market wrap: ITC, Apollo Hospital, Dr Reddy's Labs, Bajaj Auto top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-itc-apollo-hospital-dr-reddys-labs-bajaj-auto-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/134892529.cms
- Source: Rupee gains 96 paise, but Nifty falls 157 points on crude, FII outflows — BusinessLine Mkts, 2026-10-12. https://www.thehindubusinessline.com/markets/rupee-gains-96-paise-but-nifty-falls-157-points-on-crude-fii-outflows/article71574872.ece
- Source: Sensex today | Stock Market Highlights: Stock markets tumble on oil price spike, foreign fund outflows; Sensex drops 548 points — BusinessLine Mkts, 2026-10-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-12-october-2026/article71571162.ece
- Historical analogues: 2025-07-14 (d=0.64), 2025-07-21 (d=0.65), 2025-07-31 (d=1.1)

### [RED 4.89] dyn_techm_ns ↓
- dyn_techm_ns [EQUITIES]: last 1471.00, z20 -2.89, zc 0.80, resid-z -0.03 [quiet], 1d -2.85%, |z20|=2.89
- **Mechanism**: dyn_techm_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.831 via dyn_techm_ns, z -0.18, quiet); dyn_tataelxsi_ns (rho 0.476 via dyn_techm_ns, z 0.47, quiet); dyn_justdial_bo (rho 0.433 via dyn_techm_ns, z -0.72, quiet); dyn_tatatech_ns (rho 0.402 via dyn_techm_ns, z -0.03, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.831 vs dyn_techm_ns
- **India receivers**: nifty_it (rho 0.831, z -0.18); dyn_tataelxsi_ns (rho 0.476, z 0.47); dyn_justdial_bo (rho 0.433, z -0.72); dyn_tatatech_ns (rho 0.402, z -0.03)
- Source: Tech Mahindra, TCS, Oracle shares fall up to 3% today - Is it the right time to buy IT stocks? — Mint Markets, 2026-10-12. https://www.livemint.com/market/stock-market-news/tech-mahindra-tcs-oracle-shares-fall-up-to-3-today-is-it-the-right-time-to-buy-it-stocks-11791805096158.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [RED 4.67] dxy ↑
- dxy [FX]: last 102.58, z20 1.67, zc 0.20, resid-z -0.13 [quiet], 1d 0.36%, 20d range extreme; |z20|=1.67; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.508 vs dxy, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [AMBER 4.62] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.60, z20 0.95, zc -1.74, resid-z -2.34 [unexplained], 1d -1.23%, 1y-pct=97
- dyn_bond [EQUITIES]: last 86.95, z20 -0.75, zc 0.10, resid-z 0.58 [quiet], 1d 0.00%, 1y-pct=2
- tips_10y_real [RATES]: last 2.87, z20 0.73, zc -0.90, resid-z -1.52 [unexplained], 1d -1.71%, 1y-pct=96
- ust_10y [RATES]: last 5.22, z20 0.72, zc -1.12, resid-z -1.95 [unexplained], 1d -1.14%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 1d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.507 vs ust_10y, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.586 vs dyn_bond
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.535 vs ust_30y
- Source: SEBI’s Credit Risk-o-Meter may make bond risks easier to compare — BusinessLine Mkts, 2026-10-12. https://www.thehindubusinessline.com/markets/sebis-credit-risk-o-meter-may-make-bond-risks-easier-to-compare/article71575750.ece
- Source: India benchmark bond posts worst day in six months on RBI measures — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/bonds/india-benchmark-bond-posts-worst-day-in-six-months-on-rbi-measures/articleshow/134893334.cms
- Source: The bond market is doing the Fed’s job, and that could be good news for stocks, says Morgan Stanley strategist — MarketWatch Top, 2026-10-12. https://www.marketwatch.com/story/the-bond-market-is-doing-the-feds-job-and-that-could-be-good-news-for-stocks-says-morgan-stanley-strategist-ec57b81a?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.22] indices · 2 series ↑
- sp500 [INDICES]: last 7807.79, z20 1.39, zc 0.84, resid-z -1.45 [quiet], 1d -0.05%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30669.27, z20 0.51, zc 0.48, resid-z -0.78 [quiet], 1d -0.69%, 1y-pct=97
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.952 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.724 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.86 vs sp500
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.607 vs sp500
- Source: US stocks: Nasdaq ends lower as oil prices surge ahead of earnings, economic data — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-nasdaq-ends-lower-as-oil-prices-surge-ahead-of-earnings-economic-data/articleshow/134902064.cms
- Source: $4,000 Gold Could Be Wall Street's Next Big Buying Opportunity — OilPrice, 2026-10-12. https://oilprice.com/Metals/Gold/4000-Gold-Could-Be-Wall-Streets-Next-Big-Buying-Opportunity.html
- Source: Wall Street bets big on India as IPO boom draws global financial giants — BusinessLine Mkts, 2026-10-12. https://www.thehindubusinessline.com/markets/wall-street-bets-big-on-india-as-ipo-boom-draws-global-financial-giants/article71576048.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

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

### [AMBER 3.92] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 69.27, z20 0.92, zc n/a, resid-z n/a [quiet], 1d -0.32%, GSR<75 (extreme low)
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.365 via gold_silver_ratio, z -0.16, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.84 vs gold_silver_ratio
- **India receivers**: midcap_largecap_ratio (rho -0.365, z -0.16)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (3.88), dyn_cartrade_ns ↑ (3.72), kospi ↓ (3.39), dyn_tech ↑ (3.26), dyn_rs ↑ (3.14), dyn_karurvysya_ns ↑ (3.03), usd_cny ↓ (2.97), commodities · 2 series ↓ (2.81), dyn_meta ↑ (2.78), dyn_coalindia_ns ↓ (2.59), bovespa ↑ (2.34), nifty_metal ↓ (2.16)

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
- COALINDIA.NS (COAL INDIA LTD) score 73.2 — "India benchmark bond posts worst day in six months on RBI measures"
- INOXINDIA.NS (INOX INDIA LIMITED) score 70.9 — "India benchmark bond posts worst day in six months on RBI measures"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 68.7 — "India benchmark bond posts worst day in six months on RBI measures"
- INDIANB.NS (INDIAN BANK) score 57.0 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- BAC (Bank of America Corporation) score 51.1 — "TRUMP’S RUSSIAN DIESEL DEAL SPARKS REPUBLICAN REVOLT Republican Senator Thom Tillis warns "
- HDB (HDFC Bank Limited) score 44.9 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.1 — "HCL Tech Q2 Results: Profit jumps 21% YoY to Rs 5,132 crore; co declares Rs 12/share divid"
- IDBI.NS (IDBI BANK LIMITED) score 42.8 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.8 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.8 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.5 — "HCL Tech Q2 Results: Profit jumps 21% YoY to Rs 5,132 crore; co declares Rs 12/share divid"
- TECH (Bio-Techne Corp) score 41.5 — "HCL Tech Q2 Results: Profit jumps 21% YoY to Rs 5,132 crore; co declares Rs 12/share divid"
- COIN (Coinbase Global, Inc.) score 40.4 — "Goldman upgrades global equities on earnings optimism"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.2 — "TRUMP ANNOUNCES IMMEDIATE RUSSIA-UKRAINE ENERGY CEASEFIRE Trump says Russia and Ukraine ha"
- OHI (Omega Healthcare Investors, In) score 32.7 — "Top stocks in focus tomorrow: Investors must watch HCL Tech, RBL Bank, Azad Engineering sh"
- BOND (PIMCO Active Bond Exchange-Tra) score 32.7 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- LTH (Life Time Group Holdings, Inc.) score 27.4 — "TRUMP: TIME FOR UKRAINE TO GET A NEW PRESIDENT"
- TGT (Target Corporation) score 27.3 — "Zetwerk targets  ₹25,583 crore valuation in  ₹5,012 crore IPO"
- CHKP (Check Point Software Technolog) score 23.0 — "POPE LEO TO UNDERGO LUNG SURGERY THIS WEEK Pope Leo, 71, says doctors discovered a small g"
- 301077.SZ (CHINASTARS) score 19.0 — "Nvidia, Micron, SK Hynix shares slump up to 5% as China's CXMT steps up challenge to globa"
- SEPN (Septerna, Inc.) score 19.0 — "Small-cap, mid-cap funds grab 44% of equity MF inflows in September"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 16.6 — "RIL shares: Reliance Industries stock slides 6% in a month, can Jio Platforms IPO aid the "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.1 — "Stocks to Watch, Oct 12: Lenskart, Everyday Ind, SJS, Authum, Adani enterprise, M&M"
- JIOFIN.BO (Jio Financial Services Limited) score 10.1 — "Wall Street bets big on India as IPO boom draws global financial giants"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.7 — "FORMER U.S. DEFENSE SECRETARY WARNS IRAN WAR HAS “NO EASY WAY OUT” Former Defense Secretar"
- JEF (Jefferies Financial Group Inc.) score 8.4 — "Will RBI’s CRR hike to 99% hit HDFC, SBI and other bank stocks? Here’s what Jefferies says"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.4 — "TRUMP'S RUSSIAN DIESEL DEAL UNLIKELY TO BRING PRICES DOWN Trump says Russia will release 4"
- GS (Goldman Sachs Group, Inc. (The) score 8.2 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.9 — "Top 2 stocks to buy for tomorrow: PNB Housing Finance, TVS Motor Company by Chandan Tapari"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.6 — "Tata Steel slips marginally as draft steel policy 2047 puts sector in focus"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.6 — "Tata Steel slips marginally as draft steel policy 2047 puts sector in focus"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 7.6 — "Market wrap: ITC, Apollo Hospital, Dr Reddy's Labs, Bajaj Auto top gainers and losers on N"
- VT (Vanguard Total World Stock Ind) score 7.6 — "Trump’s ‘energy ceasefire’ collides with real-world problems of dwindling fuel supplies"
- RS (Reliance, Inc.) score 6.5 — "RIL shares: Reliance Industries stock slides 6% in a month, can Jio Platforms IPO aid the "
- META (Meta) score 6.1 — "Meta is back on the AI leaderboard with its new family of Wonder models"
- NVDA (NVIDIA Corporation) score 5.5 — "Nvidia, Micron, SK Hynix shares slump up to 5% as China's CXMT steps up challenge to globa"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.6 — "Retail stocks to buy before Q2 results: Metro Brands, Campus Activewear, Vishal Mega Mart "
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.1 — "Nomura becomes latest brokerage to cut PB Fintech share price target by 31%, lists 2 scena"
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