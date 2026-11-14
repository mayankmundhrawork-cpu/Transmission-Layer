# Transmission Layer — board brief · 2026-11-14 00:53Z

data as of **2026-11-14** · 97 series · 13 red / 24 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.645, 3d in regime; vol-pct 0.76, breadth-off 0.529, Markov P(high-vol) 0.034)
- [WEAK] **safe_haven_gold** — corr20 -0.09, corr60 -0.21, contra nifty_50 corr20=0.25, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.13, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.33, corr60 0.04, last shift 2026-09-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-21. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 0.0, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.17, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-17. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.476, β 0.2044, p 0.0); driver zc 2.85 → expected 0.762%. Type hit-rate 0.82 (n=2126).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.449, β 0.2339, p 0.0); driver zc 1.9 → expected 0.479%. Type hit-rate 0.82 (n=2126).
- **SETUP** aud_usd → usd_cny: leads 1d (ccf -0.268, β -0.0799, p 0.0); driver zc -1.73 → expected 0.08%. Type hit-rate 0.82 (n=2126).
- Track record · residual_reversion: hit-rate **0.509** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2126) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.38] dxy ↑
- dxy [FX]: last 103.41, z20 3.38, zc 0.64, resid-z 0.95 [quiet], 1d 0.23%, 20d range extreme; |z20|=3.38; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_jef (inverse) — not yet - watch; rho -0.505 vs dxy, historically leads by 5d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 6.25] cross-asset · 4 series ↓
- comex_copper [COMMODITIES]: last 6.06, z20 -2.58, zc -0.90, resid-z -1.14 [quiet], 1d -1.92%, |z20|=2.58
- comex_gold [COMMODITIES]: last 3887.60, z20 -2.00, zc 0.03, resid-z -1.00 [quiet], 1d 0.06%, |z20|=2.00; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 48.65, z20 -1.76, zc -0.90, resid-z -2.04 [unexplained], 1d -2.65%, |z20|=1.76; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 79.91, z20 1.46, zc n/a, resid-z n/a [quiet], 1d 2.78%, 1y-pct=97
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.469 via comex_gold, z 1.28, reacted); dyn_karurvysya_ns (rho 0.425 via comex_gold, z 1.91, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.575 vs comex_copper, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.504 vs comex_copper, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.469, z 1.28); dyn_karurvysya_ns (rho 0.425, z 1.91)
- Source: Rate-hike bets keep gold on track for worst week in four months — Mint Markets, 2026-11-13. https://www.livemint.com/market/ratehike-bets-keep-gold-on-track-for-worst-week-in-four-months-11794598496469.html
- Source: Gold Edges Up, Still On Track for Worst Weekly Slump Since June — Mint Markets, 2026-11-13. https://www.livemint.com/market/gold-edges-up-still-on-track-for-worst-weekly-slump-since-june-11794595223804.html
- Source: Gem, jewellery exports up 34% on growing demand, rise in gold prices — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/gold/gem-jewellery-exports-up-34-on-growing-demand-rise-in-gold-prices/article71697017.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 6.23] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 22.11, z20 6.23, zc 3.90, resid-z 0.60 [moved], 1d 10.38%, |z20|=6.23
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.513 vs dyn_301077_sz, historically leads by 1d
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 6.2] rates · 2 series ↑
- tips_10y_real [RATES]: last 2.86, z20 2.37, zc 2.64, resid-z 1.60 [unexplained], 1d 2.88%, 1d move +8.0bps ≥ 5bps; |z20|=2.37; 1y-pct=95
- ust_2y [RATES]: last 4.86, z20 1.94, zc 2.85, resid-z 2.05 [unexplained], 1d 2.75%, |z20|=1.94; 1y-pct=98
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.932 vs tips_10y_real, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-05-14 (d=0.45)

### [RED 5.82] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 68259.32, z20 -2.51, zc -0.40, resid-z -0.73 [quiet], 1d -1.07%, |z20|=2.51
- eth_usd [CRYPTO]: last 1929.48, z20 -2.28, zc -0.26, resid-z -0.47 [quiet], 1d -1.01%, |z20|=2.28
- dyn_coin [EQUITIES]: last 127.62, z20 -1.64, zc -0.50, resid-z 0.21 [quiet], 1d -2.33%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.48).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.74 vs btc_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.728 vs btc_usd
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.717 vs btc_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.609 vs btc_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.552 vs btc_usd
- Source: Global oil supplies are suddenly flowing. Why a crude glut won’t mean cheaper diesel. — MarketWatch Top, 2026-11-13. https://www.marketwatch.com/story/global-oil-supplies-are-suddenly-flowing-why-a-crude-glut-wont-mean-cheaper-diesel-a5fa80c8?mod=mw_rss_topstories
- Source: Bitcoin is now below $69,000 and could fall even further if investors cash out to buy into the Anthropic IPO — MarketWatch Top, 2026-11-13. https://www.marketwatch.com/story/bitcoin-could-fall-even-further-if-investors-cash-out-to-buy-into-the-anthropic-ipo-5a14f46a?mod=mw_rss_topstories
- Source: CRYPTO STOCKS SLIDE AS BITCOIN HITS THREE-MONTH LOW 🔸 Hut 8 ($HUT): −6.0% 🔸 Riot Platforms ($RIOT): −3.9% 🔸 MARA Holdings ($MARA): −3.9% 🔸 Robinhood ($HOOD): −3.2% 🔸 Strategy ($MSTR): −2.1% 🔸 Coinbase ($COIN): −0.5% Bitcoin's weakness is spreading across crypto equities, with mining stocks taking th — DeItaone, 2026-11-13. https://t.me/walter_bloomberg/38522
- Historical analogues: 2026-05-22 (d=0.48), 2025-04-10 (d=0.71), 2025-10-16 (d=0.74)

### [AMBER 5.47] cross-asset · 3 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1117.00, z20 2.15, zc 0.08, resid-z 0.65 [quiet], 1d 0.18%, |z20|=2.15; 1y-pct=98
- nifty_midcap_100 [INDICES]: last 61881.90, z20 1.84, zc -0.22, resid-z 0.51 [quiet], 1d -0.25%, |z20|=1.84
- nifty_50 [INDICES]: last 25144.30, z20 1.71, zc -0.53, resid-z -0.84 [quiet], 1d -0.61%, |z20|=1.71
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

### [RED 5.1] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -4.27, zc -1.61, resid-z -1.88 [unexplained], 1d -0.61%, |z20|=4.27; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.91, zc -1.32, resid-z -1.62 [unexplained], 1d -0.51%, |z20|=2.91; 1y-pct=4
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.055 vs eur_usd, historically leads by 1d
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.57] usd_jpy ↑
- usd_jpy [FX]: last 159.69, z20 2.57, zc -0.05, resid-z -0.10 [quiet], 1d -0.03%, |z20|=2.57
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.411 via usd_jpy, z -0.07, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.411, z -0.07)
- Source: Yen Falls to Cusp of 160 Level, Fanning Intervention Risk — Mint Markets, 2026-11-12. https://www.livemint.com/market/yen-falls-to-cusp-of-160-level-fanning-intervention-risk-11794521542082.html
- Source: The Yen Is Becoming Too Hard for Some Investors to Trade — Mint Markets, 2026-11-12. https://www.livemint.com/market/the-yen-is-becoming-too-hard-for-some-investors-to-trade-11794520064240.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

## Watchlist (below surfacing floor)
dyn_nvda ↓ (4.16), indices · 4 series ↑ (4.14), dyn_schd ↑ (3.38), dyn_tech ↑ (3.15), aud_usd ↓ (3.08), dyn_4417_t ↑ (2.9), dyn_lth ↑ (2.88), eur_inr ↓ (2.87), ust_2s10s ↓ (2.85), dyn_cochinship_ns ↓ (2.64), dyn_crwv ↓ (2.51), dyn_rs ↑ (2.04)

## India macro
- nifty_50: 25144.3008 (1d -0.61%, z20 1.71, flag amber)
- nifty_midcap_100: 61881.8984 (1d -0.25%, z20 1.84, flag amber)
- usd_inr: 94.2300 (1d 0.57%, z20 -0.89, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4611 (1d 0.36%, z20 -0.75, flag none)
- Next India prints: India WPI T-2d · NSDL FPI flows T-2d · India trade / CAD data T-2d · IMD weekly rainfall T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 84.4 — "Nvidia’s woes attract Indian investors, trading surges on overseas investing platforms"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.0 — "Nvidia’s woes attract Indian investors, trading surges on overseas investing platforms"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.9 — "Nvidia’s woes attract Indian investors, trading surges on overseas investing platforms"
- NVDA (NVIDIA Corporation) score 79.9 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- INDIANB.NS (INDIAN BANK) score 60.0 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- BAC (Bank of America Corporation) score 54.4 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- HDB (HDFC Bank Limited) score 46.3 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.9 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- IDBI.NS (IDBI BANK LIMITED) score 41.9 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.9 — "LUTNICK AGREES TO TESTIFY BEFORE SENATE OVER NVIDIA Commerce Secretary Howard Lutnick has "
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.0 — "NVIDIA CEO RACE: IAN BUCK PULLS AHEAD Following Jensen Huang's departure, Nvidia executive"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.2 — "NVIDIA CEO RACE: IAN BUCK PULLS AHEAD Following Jensen Huang's departure, Nvidia executive"
- TECH (Bio-Techne Corp) score 39.2 — "NVIDIA CEO RACE: IAN BUCK PULLS AHEAD Following Jensen Huang's departure, Nvidia executive"
- TGT (Target Corporation) score 39.0 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- CHKP (Check Point Software Technolog) score 34.9 — "ideaForge Technology shares: Drone stock gains 53% in a year, but should you buy now? Chec"
- OHI (Omega Healthcare Investors, In) score 32.3 — "Nvidia’s woes attract Indian investors, trading surges on overseas investing platforms"
- 301077.SZ (CHINASTARS) score 30.0 — "ANTHROPIC IPO IS SAID TO EXCLUDE CHINA, HK-BASED INVESTORS"
- COIN (Coinbase Global, Inc.) score 24.5 — "BOFA GLOBAL RESEARCH ADDS 25 BP FED RATE HIKE IN JANUARY 2027 TO ITS FORECAST; NOW EXPECTS"
- LTH (Life Time Group Holdings, Inc.) score 23.2 — "12.5 MILLION AMERICAN GAMERS PLAN TO TAKE TIME OFF FOR GTA 6 An estimated 12.5 million US "
- BOND (PIMCO Active Bond Exchange-Tra) score 21.7 — "India 10-year bond yield reverses half of last week's drop on elevated inflation"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.9 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.5 — "FED'S GOOLSBEE SAYS ON CNBC INFLATION HAS SPREAD INTO CATEGORIES WHERE PRICES ARE NOT BEIN"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.0 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.0 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.5 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 15.4 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.1 — "NVIDIA SHARES EXTEND LOSSES, LAST DOWN 4.1%"
- JIOFIN.BO (Jio Financial Services Limited) score 14.4 — "AI risks are the biggest threat to the financial system, Fed survey finds"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.9 — "Anthropic IPO oversubscribed nearly six times; can AI firm become new NVIDIA amid stock cr"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.6 — "12.5 MILLION AMERICAN GAMERS PLAN TO TAKE TIME OFF FOR GTA 6 An estimated 12.5 million US "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.9 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- CRWV (CoreWeave, Inc.) score 6.7 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- RS (Reliance, Inc.) score 5.6 — "Reliance Industries shares rebound 15% in November, add  ₹2.38 lakh crore in market value;"
- META (Meta) score 4.6 — "India ETFs draw ₹35,120 crore in Q3 as large-cap, precious metals lead inflows"
- DEMZ (Democratic Large Cap Core ETF) score 4.4 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- BLLN (BillionToOne, Inc.) score 4.0 — "Germany Eyes €4 Billion Buyout of RWE and E.ON’s Urenco Stake"
- JEF (Jefferies Financial Group Inc.) score 3.9 — "FIIs are back! Jefferies lists 11 stocks that can be the biggest beneficiaries"
- GS (Goldman Sachs Group, Inc. (The) score 3.8 — "Earnings growth is set to peter out — but not the bull market, says Goldman Sachs. Here’s "
- MSFT (Microsoft Corporation) score 3.7 — "Microsoft shares fall nearly 3% in pre-market as global outage hits Outlook, Teams and Cop"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 2.8 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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