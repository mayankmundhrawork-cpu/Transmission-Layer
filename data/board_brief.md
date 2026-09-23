# Transmission Layer — board brief · 2026-09-23 14:59Z

data as of **2026-09-23** · 97 series · 10 red / 36 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.354, 4d in regime; vol-pct 0.083, breadth-off 0.625, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.51, corr60 -0.36, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.08, corr60 0.28, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.12, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.07, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.06, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.39, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0015243893761345273)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1098) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2333) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.93] natgas ↑
- natgas [COMMODITIES]: last 3.13, z20 4.93, zc 1.76, resid-z 2.50 [unexplained], 1d 5.67%, 1-session move +5.67% ≥ 5.0%; |z20|=4.93
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.103 vs natgas, historically leads by 4d
- Source: TotalEnergies to Develop Offshore Gas Field to Boost Nigeria LNG Supply — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-to-Develop-Offshore-Gas-Field-to-Boost-Nigeria-LNG-Supply.html
- Source: Washington Needs This LNG Deal More Than Beijing Does — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Washington-Needs-This-LNG-Deal-More-Than-Beijing-Does.html
- Source: Public companies produce most U.S. crude oil and natural gas — EIA Today in Energy, 2026-09-22. https://www.eia.gov/todayinenergy/detail.php?id=68184
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 8.18] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.76, z20 1.72, zc 0.00, resid-z 0.00 [quiet], 1d 0.00%, |z20|=1.72; 1y-pct=99
- dyn_bond [EQUITIES]: last 88.43, z20 -1.49, zc -2.07, resid-z -0.26 [priced], 1d -0.70%, 1y-pct=0
- tips_10y_real [RATES]: last 2.62, z20 1.25, zc -1.19, resid-z -1.38 [quiet], 1d -2.24%, 1d move -6.0bps ≥ 5bps; 1y-pct=98
- ust_10y [RATES]: last 4.96, z20 1.11, zc -1.02, resid-z -0.67 [quiet], 1d -1.00%, 1y-pct=98
- ust_30y [RATES]: last 5.29, z20 0.28, zc -1.21, resid-z -0.83 [quiet], 1d -0.94%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.381 via ust_2y, z 0.98, quiet)
- Watch next: brent (inverse) — not yet - watch; rho -0.591 vs dyn_bond, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.564 vs dyn_bond, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.589 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.381, z 0.98)
- Source: 10-year US Treasury yields surges over 5.05% to 19-year high — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/10-year-us-treasury-yields-surges-over-5-05-to-19-year-high/articleshow/134441042.cms
- Source: Wall Street slips as oil and bond yields rise, Trump-Xi meet in focus — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/wall-street-slips-as-oil-and-bond-yields-rise-trump-xi-meet-in-focus-11790171977214.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US 10-year Treasury yield tops 5% for first time since 2007; Nasdaq slumps over 1% — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.6] fx · 4 series ↓
- usd_mxn [FX]: last 17.47, z20 3.94, zc 3.53, resid-z 3.42 [unexplained], 1d 1.50%, |z20|=3.94
- gbp_usd [FX]: last 1.33, z20 -3.18, zc -2.23, resid-z -2.04 [unexplained], 1d -0.80%, |z20|=3.18
- aud_usd [FX]: last 0.70, z20 -3.03, zc -2.28, resid-z -2.23 [unexplained], 1d -0.99%, |z20|=3.03
- eur_usd [FX]: last 1.14, z20 -2.80, zc -1.73, resid-z -1.23 [moved], 1d -0.53%, |z20|=2.80; 1y-pct=4
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.419 via gbp_usd, z -0.18, quiet); dyn_muthootfin_ns (rho 0.409 via aud_usd, z -0.31, quiet); dyn_inoxindia_ns (rho 0.358 via aud_usd, z 0.3, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.549 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.419, z -0.18); dyn_muthootfin_ns (rho 0.409, z -0.31); dyn_inoxindia_ns (rho 0.358, z 0.3)
- Source: Almost ten million people took part in ECB survey on new euro banknotes — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260923~6ebddaf01e.en.html
- Source: Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic and global orders — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/stocks/news/sterling-and-wilson-renewable-energy-shares-rally-8-after-securing-rs-985-crore-domestic-and-global-orders/articleshow/134402652.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.15] commodities · 2 series ↓
- wti [COMMODITIES]: last 92.06, z20 -0.32, zc -0.92, resid-z -1.03 [quiet], 1d -2.67%, 1-session move -2.67% ≥ 1.5%
- brent [COMMODITIES]: last 97.63, z20 -0.19, zc -0.67, resid-z -0.76 [quiet], 1d -1.63%, 1-session move -1.63% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.624 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.534 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.531 vs wti
- Source: EIA Reports 3M Barrel Crude Build as Distillate Stocks Fall 12% Below Average — OilPrice, 2026-09-23. https://oilprice.com/Energy/Energy-General/EIA-Reports-3M-Barrel-Crude-Build-as-Distillate-Stocks-Fall-12-Below-Average.html
- Source: Climate Startup Signs CO2 Deals With Three U.S. Oil Producers — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/Climate-Startup-Signs-CO2-Deals-With-Three-US-Oil-Producers.html
- Source: Wall Street slips as oil and bond yields rise, Trump-Xi meet in focus — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/wall-street-slips-as-oil-and-bond-yields-rise-trump-xi-meet-in-focus-11790171977214.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 5.87] dxy ↑
- dxy [FX]: last 101.07, z20 2.87, zc 1.60, resid-z 1.14 [moved], 1d 0.52%, 20d range extreme; |z20|=2.87
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.77] cross-asset · 3 series ↑
- nasdaq_100 [INDICES]: last 30524.63, z20 2.45, zc -0.47, resid-z -0.03 [quiet], 1d -0.66%, |z20|=2.45; 1y-pct=98
- sp500 [INDICES]: last 7731.30, z20 1.09, zc -0.49, resid-z 3.24 [unexplained], 1d -0.42%, 1y-pct=96
- dyn_nvda [EQUITIES]: last 226.12, z20 0.89, zc -0.48, resid-z -0.10 [quiet], 1d -1.18%, 1y-pct=97
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.93 vs nasdaq_100, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.658 vs nasdaq_100, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.618 vs sp500, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.607 vs sp500, historically leads by 2d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.607 vs nasdaq_100
- Source: Wall Street slips as oil and bond yields rise, Trump-Xi meet in focus — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/wall-street-slips-as-oil-and-bond-yields-rise-trump-xi-meet-in-focus-11790171977214.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US 10-year Treasury yield tops 5% for first time since 2007; Nasdaq slumps over 1% — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: This oil giant has lagged its leading rivals through two energy crises. Now one Wall Street giant says it’s time to buy. — MarketWatch Top, 2026-09-23. https://www.marketwatch.com/story/this-oil-giant-has-lagged-its-leading-rivals-through-two-energy-crises-now-one-wall-street-giant-says-its-time-to-buy-987838c3?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.18), 2025-08-28 (d=0.22)

### [RED 5.06] dyn_lth ↓
- dyn_lth [EQUITIES]: last 37.17, z20 -3.06, zc -0.98, resid-z -1.49 [quiet], 1d -2.75%, |z20|=3.06
- **Mechanism**: dyn_lth ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US 10-year Treasury yield tops 5% for first time since 2007; Nasdaq slumps over 1% — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: This oil giant has lagged its leading rivals through two energy crises. Now one Wall Street giant says it’s time to buy. — MarketWatch Top, 2026-09-23. https://www.marketwatch.com/story/this-oil-giant-has-lagged-its-leading-rivals-through-two-energy-crises-now-one-wall-street-giant-says-its-time-to-buy-987838c3?mod=mw_rss_topstories
- Source: Taiwan index rises to near all-time peak as Asian stocks ride AI wave — BusinessLine Mkts, 2026-09-23. https://www.thehindubusinessline.com/markets/taiwan-index-rises-to-near-all-time-peak-as-asian-stocks-ride-ai-wave/article71498652.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.40 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.366 via dyn_4417_t, z 0.69, quiet)
- **India receivers**: dyn_justdial_bo (rho 0.366, z 0.69)
- Source: Sebi board is set to grow. Experts say it's missing one safeguard it needs most — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/sebi-board-expansion-securities-markets-code-2025-appointmentprocess-11788844688106.html
- Source: How to invest amid heightened uncertainty? Look at multi-asset allocation funds, say experts — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/how-to-invest-amid-heightened-uncertainty-look-at-multi-asset-allocation-funds-say-experts-11790078842845.html
- Source: Vedanta Aluminium stock jumps 4% days after hitting 52-week low! Can it reclaim demerger level? Experts decode outlook — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/vedanta-aluminium-stock-jumps-4-days-after-hitting-52-week-low-can-it-reclaim-demerger-level-experts-decode-outlook-11790062916085.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
crypto · 2 series ↑ (4.75), dyn_bac ↓ (4.26), dyn_meta ↑ (4.25), gold_silver_ratio ↓ (4.2), dyn_ms ↓ (4.01), midcap_largecap_ratio ↑ (3.98), comex_gold ↓ (3.64), dyn_tech ↑ (3.64), comex_copper ↑ (3.46), dyn_voltas_ns ↓ (2.99), ust_2s10s ↓ (2.68), sofr ↑ (2.6)

## India macro
- nifty_50: 23446.8008 (1d 0.50%, z20 -0.69, flag none)
- nifty_midcap_100: 62391.4492 (1d 0.70%, z20 -0.38, flag none)
- usd_inr: 95.7300 (1d 0.02%, z20 0.81, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6610 (1d 0.20%, z20 0.98, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 72.9 — "NLC India raises ₹500 crore via issuance of commercial papers"
- INOXINDIA.NS (INOX INDIA LIMITED) score 71.0 — "NLC India raises ₹500 crore via issuance of commercial papers"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 70.3 — "NLC India raises ₹500 crore via issuance of commercial papers"
- COIN (Coinbase Global, Inc.) score 55.1 — "Global Market: European shares edge higher as lower oil prices lift sentiment"
- INDIANB.NS (INDIAN BANK) score 54.1 — "Almost ten million people took part in ECB survey on new euro banknotes"
- OHI (Omega Healthcare Investors, In) score 49.7 — "Global Market: Singapore's US stock trading push struggles to attract investors"
- BAC (Bank of America Corporation) score 46.4 — "Almost ten million people took part in ECB survey on new euro banknotes"
- CHKP (Check Point Software Technolog) score 43.0 — "Today’s Gold Rate, Aug 26: Check gold rates in Delhi, Mumbai, Chennai"
- HDB (HDFC Bank Limited) score 42.9 — "Almost ten million people took part in ECB survey on new euro banknotes"
- IDBI.NS (IDBI BANK LIMITED) score 39.0 — "Almost ten million people took part in ECB survey on new euro banknotes"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.0 — "Almost ten million people took part in ECB survey on new euro banknotes"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.0 — "Almost ten million people took part in ECB survey on new euro banknotes"
- BOND (PIMCO Active Bond Exchange-Tra) score 32.2 — "Wall Street slips as oil and bond yields rise, Trump-Xi meet in focus"
- TECHM.NS (TECH MAHINDRA LIMITED) score 28.4 — "Kellton Tech declares fundraise through rights issue; price, record date, other update you"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 28.4 — "Kellton Tech declares fundraise through rights issue; price, record date, other update you"
- TECH (Bio-Techne Corp) score 28.4 — "Kellton Tech declares fundraise through rights issue; price, record date, other update you"
- SEPN (Septerna, Inc.) score 27.8 — "Global Market: UK business growth cools as inflation pressures build in September"
- LTH (Life Time Group Holdings, Inc.) score 26.8 — "Global Market: European shares edge higher as lower oil prices lift sentiment"
- 301077.SZ (CHINASTARS) score 24.1 — "Xi Jinping's US visit: How Trump-China President meeting will impact US stock markets"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 22.8 — "Shapoorji funding squeeze persists amid Tata IPO uncertainty"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 22.8 — "Shapoorji funding squeeze persists amid Tata IPO uncertainty"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.3 — "UK inflation jumps to 3.1% as energy costs soar"
- JIOFIN.BO (Jio Financial Services Limited) score 17.7 — "Broker’s call: M&M Financial (Buy)"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "Dividend record date 23 Sept alert: Last call for investors today! Buy Arfin India, Engine"
- META (Meta) score 11.7 — "Why physical gold sales lost sheen on Ganesha Chaturthi? Will yellow metal regain its glit"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.8 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.7 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "The real estate portfolio of Zendaya and Tom Holland, plus her plans for a room just for h"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.9 — "Sebi board is set to grow. Experts say it's missing one safeguard it needs most"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.5 — "Market wrap: Bajaj Finance, Tata Steel, HCL Tech, Titan Company top gainers and losers on "
- PINELABS.NS (PINE LABS LIMITED) score 6.4 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- VT (Vanguard Total World Stock Ind) score 5.8 — "‘Built for the World in India’: Nippon AMC’s Sikka sees manufacturing opportunity amid glo"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.4 — "Stylam Industries gets BUY from ICICI Direct; 21% upside seen — check price target"
- MS (Morgan Stanley) score 5.2 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "Goldman Sees China Oil Imports Staying Subdued in Fourth Quarter"
- TNA (Direxion Small Cap Bull 3X ETF) score 4.7 — "Small-cap stocks trade at nearly twice Nifty 50 valuation, says VK Vijayakumar"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.3 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 3.8 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- VOLTAS.NS (VOLTAS LTD) score 1.2 — "Voltas share price: Nuvama upgrades rating but Jefferies cuts target price after analyst m"
- DELL (Dell Technologies Inc.) score 0.1 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"

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