# Transmission Layer — board brief · 2026-11-13 19:37Z

data as of **2026-11-13** · 97 series · 12 red / 24 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.638, 3d in regime; vol-pct 0.747, breadth-off 0.529, Markov P(high-vol) 0.038)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.21, contra nifty_50 corr20=0.25, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.12, last shift 2026-09-16. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.34, corr60 0.03, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.91, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.27, corr60 -0.0, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.17, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.37, corr60 0.32, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.477, β 0.2051, p 0.0); driver zc 2.86 → expected 0.765%. Type hit-rate 0.819 (n=2188).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.447, β 0.2336, p 0.0); driver zc 1.9 → expected 0.479%. Type hit-rate 0.819 (n=2188).
- **SETUP** aud_usd → usd_cny: leads 1d (ccf -0.269, β -0.0801, p 0.0); driver zc -1.66 → expected 0.077%. Type hit-rate 0.819 (n=2188).
- Track record · residual_reversion: hit-rate **0.509** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2188) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.32] dxy ↑
- dxy [FX]: last 103.39, z20 3.32, zc 0.57, resid-z 0.95 [quiet], 1d 0.21%, 20d range extreme; |z20|=3.32; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_jef (inverse) — not yet - watch; rho -0.504 vs dxy, historically leads by 5d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 6.23] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 22.11, z20 6.23, zc 3.90, resid-z 0.60 [moved], 1d 10.38%, |z20|=6.23
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.513 vs dyn_301077_sz, historically leads by 1d
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 6.14] cross-asset · 4 series ↓
- comex_copper [COMMODITIES]: last 6.08, z20 -2.47, zc -0.88, resid-z -0.86 [quiet], 1d -1.67%, |z20|=2.47
- comex_gold [COMMODITIES]: last 3882.30, z20 -2.07, zc -0.04, resid-z -1.00 [quiet], 1d -0.08%, |z20|=2.07; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 48.94, z20 -1.65, zc -0.70, resid-z -1.44 [quiet], 1d -2.08%, |z20|=1.65; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 79.34, z20 1.22, zc n/a, resid-z n/a [quiet], 1d 2.04%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.473 via comex_gold, z 1.28, reacted); dyn_karurvysya_ns (rho 0.425 via comex_gold, z 1.91, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.576 vs comex_copper, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.506 vs comex_copper, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.473, z 1.28); dyn_karurvysya_ns (rho 0.425, z 1.91)
- Source: Gold Edges Up, Still On Track for Worst Weekly Slump Since June — Mint Markets, 2026-11-13. https://www.livemint.com/market/gold-edges-up-still-on-track-for-worst-weekly-slump-since-june-11794595223804.html
- Source: Gem, jewellery exports up 34% on growing demand, rise in gold prices — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/gold/gem-jewellery-exports-up-34-on-growing-demand-rise-in-gold-prices/article71697017.ece
- Source: India’s gold imports plunge 62.57% to $5.51 billion in October as prices fall below $4,000/oz — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/gold/indias-gold-imports-plunge-6257-to-551-billion-in-october-as-prices-fall-below-4000oz/article71697565.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 6.07] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 68994.93, z20 -2.75, zc -1.31, resid-z -0.71 [quiet], 1d -3.29%, |z20|=2.75
- eth_usd [CRYPTO]: last 1949.25, z20 -2.52, zc -0.88, resid-z -0.49 [quiet], 1d -3.35%, |z20|=2.52
- dyn_coin [EQUITIES]: last 128.93, z20 -1.55, zc -0.28, resid-z 0.21 [quiet], 1d -1.34%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.55 vs btc_usd, historically leads by 2d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.74 vs btc_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.732 vs btc_usd
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.718 vs btc_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.613 vs btc_usd
- Source: How Global Energy Markets Survived Eight Months of Iran War Disruptions — OilPrice, 2026-11-13. https://oilprice.com/Energy/Energy-General/How-Global-Energy-Markets-Survived-Eight-Months-of-Iran-War-Disruptions.html
- Source: NSEIX Global Access expands offering to seven European markets, adds 11,500 securities — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/nseix-global-access-expands-offering-to-seven-european-markets-adds-11500-securities/article71697970.ece
- Source: Microsoft shares fall nearly 3% in pre-market as global outage hits Outlook, Teams and Copilot; what went wrong? — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/microsoft-shares-fall-nearly-3-in-pre-market-as-global-outage-hits-outlook-teams-and-copilot-what-went-wrong-11794570500283.html
- Historical analogues: 2026-05-22 (d=0.59), 2025-04-10 (d=0.85), 2025-10-16 (d=0.91)

### [AMBER 5.47] cross-asset · 3 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1117.00, z20 2.15, zc 0.08, resid-z 0.68 [quiet], 1d 0.18%, |z20|=2.15; 1y-pct=98
- nifty_midcap_100 [INDICES]: last 61881.90, z20 1.84, zc -0.22, resid-z 0.49 [quiet], 1d -0.25%, |z20|=1.84
- nifty_50 [INDICES]: last 25144.30, z20 1.71, zc -0.53, resid-z -0.85 [quiet], 1d -0.61%, |z20|=1.71
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.814 via nifty_midcap_100, z 1.16, reacted); nifty_metal (rho 0.717 via nifty_midcap_100, z 1.34, reacted); dyn_muthootfin_ns (rho 0.713 via nifty_midcap_100, z 1.28, reacted); dyn_indusindbk_bo (rho 0.667 via nifty_midcap_100, z 1.83, reacted); nifty_fmcg (rho 0.644 via nifty_midcap_100, z 1.41, reacted)
- Watch next: dyn_adanient_bo (co-move) — not yet - watch; rho 0.536 vs nifty_midcap_100, historically leads by 5d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.522 vs nifty_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.507 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.52 vs nifty_midcap_100
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.514 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.814, z 1.16); nifty_metal (rho 0.717, z 1.34); dyn_muthootfin_ns (rho 0.713, z 1.28); dyn_indusindbk_bo (rho 0.667, z 1.83)
- Source: Sensex, Nifty edge down on profit taking, inflation worries — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/sensex-nifty-edge-down-on-profit-taking-inflation-worries/article71698030.ece
- Source: Pulse of the Street: Dalal Street’s winning streak faces an inflation test — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/pulse-of-the-street-dalal-street-s-winning-streak-faces-an-inflation-test-11794572591011.html
- Source: Diwali gains often last. Will this year’s Sensex rally hold? — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/diwali-gains-this-year-sensex-rally-muhurat-11794459314013.html
- Historical analogues: 2025-07-21 (d=0.59), 2025-09-25 (d=1.13), 2025-07-11 (d=1.19)

### [RED 5.07] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -4.24, zc -1.58, resid-z -1.84 [unexplained], 1d -0.60%, |z20|=4.24; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.86, zc -1.26, resid-z -1.54 [unexplained], 1d -0.49%, |z20|=2.86
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.055 vs eur_usd, historically leads by 1d
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.65] usd_jpy ↑
- usd_jpy [FX]: last 159.74, z20 2.65, zc 0.01, resid-z -0.06 [quiet], 1d 0.01%, |z20|=2.65
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.411 via usd_jpy, z -0.07, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.411, z -0.07)
- Source: Yen Falls to Cusp of 160 Level, Fanning Intervention Risk — Mint Markets, 2026-11-12. https://www.livemint.com/market/yen-falls-to-cusp-of-160-level-fanning-intervention-risk-11794521542082.html
- Source: The Yen Is Becoming Too Hard for Some Investors to Trade — Mint Markets, 2026-11-12. https://www.livemint.com/market/the-yen-is-becoming-too-hard-for-some-investors-to-trade-11794520064240.html
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [AMBER 4.19] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 162.38, z20 -2.19, zc -0.56, resid-z -2.56 [unexplained], 1d -2.29%, |z20|=2.19; 1y-pct=0
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.815 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.741 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.692 vs dyn_nvda
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.685 vs dyn_nvda
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.623 vs dyn_nvda
- Source: The scandal at Nvidia is exactly what’s wrong with the S&P 500 — MarketWatch Top, 2026-11-13. https://www.marketwatch.com/story/the-scandal-at-nvidia-is-exactly-whats-wrong-with-the-s-p-500-7307457e?mod=mw_rss_topstories
- Source: Washington’s efforts to block Beijing’s access to Nvidia chips could spark a ‘short-lived U.S.-China trade war’ that rattles markets — MarketWatch Top, 2026-11-13. https://www.marketwatch.com/story/washingtons-efforts-to-block-beijings-access-to-nvidia-chips-could-spark-a-short-lived-u-s-china-trade-war-that-rattles-markets-83078d84?mod=mw_rss_topstories
- Source: Bessent blames Lutnick’s Commerce as he slams Nvidia chip ‘leakage’ to China — CNBC Economy, 2026-11-13. https://www.cnbc.com/2026/11/13/us-inflation-outlook-federal-reserve-rate-hike.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
indices · 4 series ↑ (4.14), tips_10y_real ↑ (4.06), dyn_schd ↑ (3.27), dyn_tech ↑ (3.21), aud_usd ↓ (3.04), ust_2s10s ↓ (2.92), dyn_4417_t ↑ (2.9), dyn_lth ↑ (2.87), eur_inr ↓ (2.82), dyn_cochinship_ns ↓ (2.64), dyn_crwv ↓ (2.52), dyn_rs ↑ (2.04)

## India macro
- nifty_50: 25144.3008 (1d -0.61%, z20 1.71, flag amber)
- nifty_midcap_100: 61881.8984 (1d -0.25%, z20 1.84, flag amber)
- usd_inr: 94.2300 (1d 0.57%, z20 -0.89, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4611 (1d 0.36%, z20 -0.75, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India WPI T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 87.7 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.2 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.1 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- NVDA (NVIDIA Corporation) score 73.5 — "Nvidia Spy Scandal Threatens the Gulf’s AI Ambitions"
- INDIANB.NS (INDIAN BANK) score 59.9 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- BAC (Bank of America Corporation) score 53.0 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- HDB (HDFC Bank Limited) score 46.7 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.0 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 42.0 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.0 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- TGT (Target Corporation) score 41.1 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- TECHM.NS (TECH MAHINDRA LIMITED) score 40.0 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.1 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- TECH (Bio-Techne Corp) score 38.1 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- CHKP (Check Point Software Technolog) score 36.7 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- OHI (Omega Healthcare Investors, In) score 30.9 — "YES Bank files SC review plea over AT-1 bonds: What does it mean for investors after stock"
- 301077.SZ (CHINASTARS) score 30.5 — "Anthropic IPO share orders from China are said to be rebuffed"
- COIN (Coinbase Global, Inc.) score 23.6 — "Microsoft shares fall nearly 3% in pre-market as global outage hits Outlook, Teams and Cop"
- LTH (Life Time Group Holdings, Inc.) score 23.4 — "Anthropic IPO oversubscribed nearly six times; can AI firm become new NVIDIA amid stock cr"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.8 — "India 10-year bond yield reverses half of last week's drop on elevated inflation"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.0 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.5 — "How Global Energy Markets Survived Eight Months of Iran War Disruptions"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.0 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.0 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.3 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 16.2 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.6 — "Anthropic IPO oversubscribed nearly six times; can AI firm become new NVIDIA amid stock cr"
- JIOFIN.BO (Jio Financial Services Limited) score 14.1 — "Edelweiss Financial Services Q2 net profit rises 50% to ₹193 crore"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.8 — "India 10-year bond yield reverses half of last week's drop on elevated inflation"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.2 — "Titan Company Share Price Live Updates: Titan Company Sees Price Adjustment"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.5 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- CRWV (CoreWeave, Inc.) score 7.0 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- RS (Reliance, Inc.) score 5.9 — "Reliance Industries shares rebound 15% in November, add  ₹2.38 lakh crore in market value;"
- META (Meta) score 4.8 — "India ETFs draw ₹35,120 crore in Q3 as large-cap, precious metals lead inflows"
- DEMZ (Democratic Large Cap Core ETF) score 4.6 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- BLLN (BillionToOne, Inc.) score 4.3 — "Germany Eyes €4 Billion Buyout of RWE and E.ON’s Urenco Stake"
- JEF (Jefferies Financial Group Inc.) score 4.1 — "FIIs are back! Jefferies lists 11 stocks that can be the biggest beneficiaries"
- GS (Goldman Sachs Group, Inc. (The) score 4.0 — "Earnings growth is set to peter out — but not the bull market, says Goldman Sachs. Here’s "
- MSFT (Microsoft Corporation) score 3.9 — "Microsoft shares fall nearly 3% in pre-market as global outage hits Outlook, Teams and Cop"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 2.9 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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