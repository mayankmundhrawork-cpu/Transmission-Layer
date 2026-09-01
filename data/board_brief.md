# Transmission Layer — board brief · 2026-09-01 00:43Z

data as of **2026-09-01** · 98 series · 12 red / 25 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 1d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.014)
- [WEAK] **safe_haven_gold** — corr20 -0.17, corr60 -0.39, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.02, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.34, corr60 -0.83, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.21, corr60 -0.14, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.28, corr60 0.2, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.0006496287948376533)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.49, β 0.2162, p 0.0); driver zc 2.79 → expected 0.721%. Type hit-rate 0.825 (n=2041).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.351, β -0.1179, p 0.0); driver zc 2.79 → expected -0.393%. Type hit-rate 0.825 (n=2041).
- Track record · residual_reversion: hit-rate **0.497** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.825** (n=2041) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.69] cross-asset · 4 series ↑
- ust_2y [RATES]: last 4.34, z20 4.03, zc 2.79, resid-z 2.28 [unexplained], 1d 3.33%, |z20|=4.03; 1y-pct=99
- ust_10y [RATES]: last 4.73, z20 1.35, zc 1.32, resid-z 0.99 [quiet], 1d 1.28%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.44, z20 -1.06, zc -1.45, resid-z 0.00 [quiet], 1d -0.09%, 1y-pct=1
- tips_10y_real [RATES]: last 2.42, z20 0.58, zc 2.13, resid-z 1.76 [unexplained], 1d 3.42%, 1d move +8.0bps ≥ 5bps; 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.898 vs ust_10y
- Watch next: brent (co-move) — not yet - watch; rho 0.592 vs ust_10y
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.338 vs ust_2y, historically leads by 1d
- Source: With Warsh running the Fed, should bond investors be worried? — MarketWatch Top, 2026-08-31. https://www.marketwatch.com/story/should-bond-investors-worry-with-warsh-running-the-fed-0a99c5ac?mod=mw_rss_topstories
- Source: US 10-year Treasury yield tops 19-month high as oil prices fuel rate-hike bets — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-10-year-treasury-yield-tops-19-month-high-as-oil-prices-fuel-rate-hike-bets/articleshow/133661626.cms
- Source: Longer-dated US Treasury yields climb as Iran and US restart military attacks — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/us-stocks/news/longer-dated-us-treasury-yields-climb-as-iran-and-us-restart-military-attacks/articleshow/133660629.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.31), 2025-05-23 (d=0.52)

### [RED 5.76] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1717.70, z20 3.76, zc 2.53, resid-z 2.38 [unexplained], 1d 6.27%, |z20|=3.76; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy share price hits lifetime high | Delivers 423% returns from IPO price — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-hits-lifetime-high-delivers-423-returns-from-ipo-price-11788162211726.html
- Source: Ather Energy shares rally 4% after launch of Konarc electric scooter at Rs 99,999. Buy, sell or hold the stock? — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-rally-4-after-launch-of-konarc-electric-scooter-at-rs-99999-buy-sell-or-hold-the-stock/articleshow/133643336.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 5.52] commodities · 3 series ↑
- wheat [COMMODITIES]: last 770.50, z20 2.20, zc 0.00, resid-z 1.56 [unexplained], 1d 0.00%, |z20|=2.20; 1y-pct=99
- corn [COMMODITIES]: last 535.50, z20 2.14, zc 0.00, resid-z -0.15 [quiet], 1d 0.00%, |z20|=2.14; 1y-pct=99
- soybeans [COMMODITIES]: last 1293.00, z20 2.09, zc 0.04, resid-z 1.30 [quiet], 1d 0.04%, |z20|=2.09; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho -0.357 via corn, z -1.21, reacted)
- **India receivers**: dyn_coalindia_ns (rho -0.357, z -1.21)
- Source: Australia Raises Wheat Crop Forecast as Export Demand Picks Up — Mint Markets, 2026-08-31. https://www.livemint.com/market/australia-raises-wheat-crop-forecast-as-export-demand-picks-up-11788215862266.html
- Source: Chicago wheat falls on selling pressure after recent highs — Mint Markets, 2026-08-31. https://www.livemint.com/market/chicago-wheat-falls-on-selling-pressure-after-recent-highs-11788203489599.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.1] dyn_lth ↓
- dyn_lth [EQUITIES]: last 42.01, z20 -3.10, zc -0.85, resid-z -0.94 [quiet], 1d -3.45%, |z20|=3.10
- **Mechanism**: dyn_lth ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Stocks to watch and why on September 1: PVR INOX, E2E Networks, NCC, Brigade Enterprises, Time Technoplast and more — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/stocks-to-watch-and-why-on-september-1-pvr-inox-e2e-networks-ncc-brigade-enterprises-indegene-and-more-11788197253602.html
- Source: BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent defended his U.S. bond-market intervention after criticism from Stanley Druckenmiller. Bessent suggested the veteran investor “lost money” around the time he submitted his critical op-ed. He also defended Treasur — DeItaone, 2026-08-31. https://t.me/walter_bloomberg/35250
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 4.91] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.67, z20 1.91, zc n/a, resid-z n/a [quiet], 1d 0.64%, 52-wk extreme (pct=100); |z20|=1.91; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.483 via midcap_largecap_ratio, z -1.48, reacted); dyn_inoxindia_ns (rho 0.405 via midcap_largecap_ratio, z 2.81, reacted); nifty_fmcg (rho -0.395 via midcap_largecap_ratio, z -2.48, reacted); nifty_it (rho -0.366 via midcap_largecap_ratio, z 0.3, quiet); dyn_techm_ns (rho -0.364 via midcap_largecap_ratio, z 0.41, quiet)
- **India receivers**: nifty_50 (rho -0.483, z -1.48); dyn_inoxindia_ns (rho 0.405, z 2.81); nifty_fmcg (rho -0.395, z -2.48); nifty_it (rho -0.366, z 0.3)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.64] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 138.94, z20 2.64, zc 1.38, resid-z 1.58 [unexplained], 1d 0.45%, |z20|=2.64
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.383 via dyn_chkp, z 1.44, reacted)
- **India receivers**: dyn_karurvysya_ns (rho -0.383, z 1.44)
- Source: Sebi slaps Rs 25 lakh fine on Citrus Check Inns directors — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/sebi-slaps-rs-25-lakh-fine-on-citrus-check-inns-directors/articleshow/133655536.cms
- Source: Nomura initiates coverage on Clean Max Enviro with Buy call. Check upside potential, key reasons — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/nomura-initiates-coverage-on-clean-max-enviro-with-buy-call-check-upside-potential-key-reasons/articleshow/133643047.cms
- Source: Annu Projects IPO allotment likely today; Here's how to check your status — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/ipos/fpos/annu-projects-ipo-allotment-likely-today-heres-how-to-check-your-status/articleshow/133641219.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2024-10-18 (d=0.02)

### [AMBER 4.08] natgas ↑
- natgas [COMMODITIES]: last 2.93, z20 2.08, zc 0.00, resid-z -0.22 [quiet], 1d 0.00%, |z20|=2.08
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.043 vs natgas, historically leads by 4d
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.002 vs natgas, historically leads by 4d
- Source: China's LNG Imports Set to Drop 18% in August as Prices Soar — OilPrice, 2026-08-31. https://oilprice.com/Latest-Energy-News/World-News/Chinas-LNG-Imports-Set-to-Drop-18-in-August-as-Prices-Soar.html
- Source: China’s August LNG Imports Set to Drop as High Prices Hit Demand — Mint Markets, 2026-08-31. https://www.livemint.com/market/chinas-august-lng-imports-set-to-drop-as-high-prices-hit-demand-11788153975524.html
- Source: Data Centers Are Driving a New U.S. Natural Gas Buildout — OilPrice, 2026-08-30. https://oilprice.com/Energy/Energy-General/Data-Centers-Are-Driving-a-New-US-Natural-Gas-Buildout.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 3.98] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 66.76, z20 -0.98, zc n/a, resid-z n/a [quiet], 1d 0.03%, GSR<75 (extreme low)
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho -0.471 via gold_silver_ratio, z 0.05, quiet); nifty_midcap_100 (rho -0.408 via gold_silver_ratio, z 1.81, reacted); dyn_stylebaaza_ns (rho -0.405 via gold_silver_ratio, z 0.72, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.891 vs gold_silver_ratio
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.576 vs gold_silver_ratio, historically leads by 4d
- **India receivers**: nifty_metal (rho -0.471, z 0.05); nifty_midcap_100 (rho -0.408, z 1.81); dyn_stylebaaza_ns (rho -0.405, z 0.72)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
dyn_hdb ↓ (3.88), dyn_lenskart_ns ↑ (3.47), ust_2s10s ↓ (3.35), brent_wti_spread ↓ (3.02), dyn_inoxindia_ns ↑ (2.81), dyn_icicigi_bo ↓ (2.78), hy_oas ↓ (2.64), dyn_tataelxsi_ns ↓ (2.61), russell_2000 ↓ (2.6), nifty_fmcg ↓ (2.48), dyn_tech ↑ (2.43), usd_cny ↓ (2.21)

## India macro
- nifty_50: 24080.4004 (1d -0.39%, z20 -1.48, flag none)
- nifty_midcap_100: 64226.6992 (1d 0.24%, z20 1.81, flag amber)
- usd_inr: 95.1520 (1d -0.33%, z20 -0.44, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6672 (1d 0.64%, z20 1.91, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.9 — "India’s valuation premium is shrinking. Is the market finally an entry point?"
- COALINDIA.NS (COAL INDIA LTD) score 68.3 — "India’s valuation premium is shrinking. Is the market finally an entry point?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 66.3 — "India’s valuation premium is shrinking. Is the market finally an entry point?"
- INDIANB.NS (INDIAN BANK) score 64.5 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- BAC (Bank of America Corporation) score 59.8 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- HDB (HDFC Bank Limited) score 52.3 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- IDBI.NS (IDBI BANK LIMITED) score 49.7 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 49.7 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 49.7 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- COIN (Coinbase Global, Inc.) score 37.2 — "HORMUZ DISRUPTIONS SEND TANKER RATES TO RECORD HIGHS Tanker freight rates have surged to r"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.1 — "BESSENT: BEST PERFORMING BOND MARKET, 30-YEAR YIELD IS DOWN"
- OHI (Omega Healthcare Investors, In) score 33.2 — "With Warsh running the Fed, should bond investors be worried?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.9 — "New Tech Breakthrough Aims To Solve The World's Plastic Waste Problem"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.2 — "New Tech Breakthrough Aims To Solve The World's Plastic Waste Problem"
- TECH (Bio-Techne Corp) score 32.2 — "New Tech Breakthrough Aims To Solve The World's Plastic Waste Problem"
- LTH (Life Time Group Holdings, Inc.) score 30.0 — "BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent de"
- 301077.SZ (CHINASTARS) score 27.0 — "China warns of ‘major risk’ of glacier collapse as Tibet-Nepal death toll nears 1,000"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.5 — "HORMUZ DISRUPTIONS SEND TANKER RATES TO RECORD HIGHS Tanker freight rates have surged to r"
- CHKP (Check Point Software Technolog) score 20.9 — "Sebi slaps Rs 25 lakh fine on Citrus Check Inns directors"
- NVDA (NVIDIA Corporation) score 19.8 — "E2E Networks bags  ₹1,000 crore NVIDIA Blackwell cloud GPU deal from sovereign AI firm"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.3 — "Muthoot Finance approves Muthoot Money merger to create larger gold loan business"
- JIOFIN.BO (Jio Financial Services Limited) score 13.2 — "EU TIGHTENS DSA RULES ON CHATGPT, REDDIT & ROBLOX The European Commission has designated R"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.9 — "Sebi weighs refining F&O warnings on brokerage apps as retail losses remain high"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.2 — "Titan vs Kalyan Jewellers: Why HSBC favours both stocks amid jewellery sector growth"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.0 — "Adani Power, Adani Enterprises to Adani Energy: Gautam Adani-owned stocks crash up to 8% i"
- MS (Morgan Stanley) score 9.9 — "BESSENT HITS BACK AT DRUCKENMILLER OVER BOND CRITICISM Treasury Secretary Scott Bessent de"
- META (Meta) score 8.9 — "META COULD OVERTAKE GOOGLE SEARCH IN AD REVENUE Meta is on track to surpass Google Search "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.5 — "China Coking Coal Prices Set for Record 46% Monthly Surge"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.4 — "Pace of gold loan expansion slows as banks adjust to new regulations"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.3 — "Tata Steel Share Price Live Updates: Tata Steel's Daily Performance Update"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.3 — "Tata Steel Share Price Live Updates: Tata Steel's Daily Performance Update"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "Milky Mist Q1 Results: After strong IPO debut, profit and revenue surge | What financials "
- VT (Vanguard Total World Stock Ind) score 6.4 — "TRUMP: WE SHOULD PAY THE LOWEST INTEREST RATES IN THE WORLD BY FAR"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.0 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.9 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- DKS (Dick's Sporting Goods Inc) score 1.5 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 1.1 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.2 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.0 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.0 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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