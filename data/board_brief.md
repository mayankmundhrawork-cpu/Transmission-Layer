# Transmission Layer — board brief · 2026-09-22 19:44Z

data as of **2026-09-22** · 97 series · 15 red / 37 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.378, 3d in regime; vol-pct 0.131, breadth-off 0.625, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.51, corr60 -0.28, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.86, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.28, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.1, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.08, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.41, corr60 0.18, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 1.5093029581692008e-06)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.493, β 0.1976, p 0.0); driver zc -1.55 → expected -0.547%. Type hit-rate 0.818 (n=2242).
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.472, β 0.2313, p 0.0); driver zc -1.61 → expected -0.579%. Type hit-rate 0.818 (n=2242).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.415, β 0.3415, p 0.0); driver zc -1.55 → expected -0.945%. Type hit-rate 0.818 (n=2242).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.389, β 0.3188, p 0.0); driver zc -1.55 → expected -0.882%. Type hit-rate 0.818 (n=2242).
- **SETUP** comex_copper → aud_usd: leads 1d (ccf 0.389, β 0.1137, p 0.00043); driver zc 1.69 → expected 0.395%. Type hit-rate 0.818 (n=2242).
- **SETUP** comex_copper → usd_mxn: leads 1d (ccf -0.29, β -0.0803, p 0.00083); driver zc 1.69 → expected -0.279%. Type hit-rate 0.818 (n=2242).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.282, β 0.0893, p 0.0023); driver zc -1.55 → expected -0.247%. Type hit-rate 0.818 (n=2242).
- Track record · residual_reversion: hit-rate **0.5** (n=1093) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2242) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.02] natgas ↑
- natgas [COMMODITIES]: last 3.16, z20 5.02, zc 4.19, resid-z 4.81 [unexplained], 1d 11.28%, 1-session move +11.28% ≥ 5.0%; |z20|=5.02
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho -0.357 via natgas, z -2.03, reacted)
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.062 vs natgas, historically leads by 4d
- **India receivers**: dyn_voltas_ns (rho -0.357, z -2.03)
- Source: Public companies produce most U.S. crude oil and natural gas — EIA Today in Energy, 2026-09-22. https://www.eia.gov/todayinenergy/detail.php?id=68184
- Source: Qatar’s LNG Loss Revives Projects From Argentina to Timor-Leste — OilPrice, 2026-09-22. https://oilprice.com/Energy/Natural-Gas/Qatars-LNG-Loss-Revives-Projects-From-Argentina-to-Timor-Leste.html
- Source: Hormuz Blockage Puts Qatar's $83 Billion LNG Bet at Risk — OilPrice, 2026-09-21. https://oilprice.com/Latest-Energy-News/World-News/Hormuz-Blockage-Puts-Qatars-83-Billion-LNG-Bet-at-Risk.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 8.99] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.68, z20 2.06, zc 1.47, resid-z 1.75 [unexplained], 1d 2.68%, 1d move +7.0bps ≥ 5bps; |z20|=2.06; 1y-pct=99
- ust_2y [RATES]: last 4.76, z20 1.96, zc 1.47, resid-z 1.50 [unexplained], 1d 1.93%, |z20|=1.96; 1y-pct=100
- ust_10y [RATES]: last 5.01, z20 1.71, zc 1.46, resid-z 1.48 [quiet], 1d 1.42%, |z20|=1.71; 1y-pct=99
- ust_30y [RATES]: last 5.34, z20 1.23, zc 1.23, resid-z 1.24 [quiet], 1d 0.95%, 1y-pct=98
- dyn_bond [EQUITIES]: last 89.07, z20 -0.79, zc 0.29, resid-z -0.08 [quiet], 1d 0.10%, 1y-pct=3
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.378 via ust_2y, z 0.64, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.608 vs ust_10y
- Watch next: wti (co-move) — not yet - watch; rho 0.544 vs ust_10y
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.53 vs ust_10y
- **India receivers**: midcap_largecap_ratio (rho -0.378, z 0.64)
- Source: The bond market is flashing a warning for stocks. These sectors are already wobbling. — MarketWatch Top, 2026-09-22. https://www.marketwatch.com/story/the-bond-market-is-flashing-a-warning-for-stocks-these-sectors-are-already-wobbling-015dc707?mod=mw_rss_topstories
- Source: SoftBank draws over $20 billion of early interest in junk bond — Mint Markets, 2026-09-22. https://www.livemint.com/market/bonds/softbank-draws-over-20-billion-of-early-interest-in-junk-bond-11790076505828.html
- Source: RBI bond sales, FX intervention help halve India's cash overhang — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/bonds/rbi-bond-sales-fx-intervention-help-halve-indias-cash-overhang/articleshow/134408593.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.74] cross-asset · 4 series ↑
- nasdaq_100 [INDICES]: last 30734.61, z20 4.08, zc 0.56, resid-z 0.72 [quiet], 1d 0.83%, |z20|=4.08; 1y-pct=100
- sp500 [INDICES]: last 7774.46, z20 2.09, zc 0.14, resid-z -0.11 [quiet], 1d 0.13%, |z20|=2.09; 1y-pct=99
- vix [INDICES]: last 14.20, z20 -1.36, zc -0.57, resid-z n/a [quiet], 1d -4.51%, 1y-pct=2
- dyn_vt [EQUITIES]: last 161.47, z20 1.18, zc 0.38, resid-z -2.25 [unexplained], 1d 0.36%, 1y-pct=97
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.635 vs sp500, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.604 vs sp500, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.759 vs nasdaq_100
- Watch next: dax (co-move) — not yet - watch; rho 0.606 vs dyn_vt
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.569 vs nasdaq_100
- Source: Wall Street extends gains as oil prices retreat on hopes of US-Iran breakthrough — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/wall-street-extends-gains-as-oil-prices-retreat-on-hopes-of-us-iran-breakthrough-11790085064437.html
- Source: Wall Street mixed as oil prices retreat on hopes of US-Iran breakthrough — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/wall-street-extends-gains-as-oil-prices-retreat-on-hopes-of-us-iran-breakthrough-11790085064437.html
- Source: US stocks: Nasdaq hits intraday record as tech stocks regain momentum — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-nasdaq-hits-intraday-record-high-as-tech-stocks-regain-footing/articleshow/134414070.cms
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 6.6] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 86373.68, z20 3.28, zc -0.07, resid-z -0.30 [quiet], 1d -0.26%, |z20|=3.28
- eth_usd [CRYPTO]: last 2752.96, z20 3.22, zc -0.19, resid-z -0.48 [quiet], 1d -0.85%, |z20|=3.22
- dyn_coin [EQUITIES]: last 201.15, z20 2.16, zc 0.01, resid-z 2.88 [unexplained], 1d 0.05%, |z20|=2.16
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.51).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.404 via eth_usd, z -1.54, reacted); midcap_largecap_ratio (rho 0.387 via dyn_coin, z 0.64, quiet)
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.58 vs btc_usd
- **India receivers**: dyn_cartrade_ns (rho 0.404, z -1.54); midcap_largecap_ratio (rho 0.387, z 0.64)
- Source: Yemen Escalation Raises New Risks for Global Oil Markets — OilPrice, 2026-09-22. https://oilprice.com/Geopolitics/Middle-East/Yemen-Escalation-Raises-New-Risks-for-Global-Oil-Markets.html
- Source: $3 trillion crypto comeback: Can Bitcoin bulls reclaim $100K and push higher? — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/3-trillion-crypto-comeback-can-bitcoin-bulls-reclaim-100k-and-push-higher/articleshow/134412450.cms
- Source: CATHIE WOOD SHRUGS OFF FED RATE-HIKE FEARS ARK Invest CEO Cathie Wood says higher interest rates won’t derail the technology boom, arguing rapid innovation will drive stronger economic growth. Wood expects the current tech revolution to reduce inflation while pushing global growth above its historic — DeItaone, 2026-09-22. https://t.me/walter_bloomberg/35988
- Historical analogues: 2025-08-13 (d=0.51), 2025-05-09 (d=1.51), 2024-11-21 (d=1.77)

### [AMBER 6.43] commodities · 2 series ↓
- wti [COMMODITIES]: last 89.25, z20 -0.60, zc -2.22, resid-z -2.24 [unexplained], 1d -6.82%, 1-session move -6.82% ≥ 1.5%
- brent [COMMODITIES]: last 97.95, z20 -0.05, zc -0.91, resid-z -0.76 [quiet], 1d -2.38%, 1-session move -2.38% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dax (inverse) — not yet - watch; rho -0.519 vs wti, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.627 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.558 vs wti
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.531 vs wti
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.507 vs wti
- Source: India’s Russian Oil Imports Slide as Refiners Hunt for Alternatives — OilPrice, 2026-09-22. https://oilprice.com/Latest-Energy-News/World-News/Indias-Russian-Oil-Imports-Slide-as-Refiners-Hunt-for-Alternatives.html
- Source: Saudi Pipeline Restart Fails to End Oil Market Tightness — OilPrice, 2026-09-22. https://oilprice.com/Energy/Crude-Oil/Saudi-Pipeline-Restart-Fails-to-End-Oil-Market-Tightness.html
- Source: Saudi Arabia Restarts East-West Oil Pipeline — OilPrice, 2026-09-22. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Restarts-East-West-Oil-Pipeline.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 6.35] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 64.81, z20 -3.35, zc n/a, resid-z n/a [quiet], 1d -2.69%, GSR<75 (extreme low); |z20|=3.35
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.357 via gold_silver_ratio, z -0.89, quiet)
- **India receivers**: nifty_midcap_100 (rho -0.357, z -0.89)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 5.17] dxy ↑
- dxy [FX]: last 100.53, z20 2.17, zc 0.30, resid-z -0.11 [quiet], 1d 0.10%, 20d range extreme; |z20|=2.17
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.14] fx · 2 series ↓
- gbp_usd [FX]: last 1.33, z20 -2.30, zc -0.76, resid-z -0.68 [quiet], 1d -0.31%, |z20|=2.30
- eur_usd [FX]: last 1.15, z20 -2.28, zc -0.66, resid-z -0.37 [quiet], 1d -0.21%, |z20|=2.28
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.399 via gbp_usd, z -0.65, quiet); nifty_50 (rho 0.362 via eur_usd, z -1.11, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.56 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.399, z -0.65); nifty_50 (rho 0.362, z -1.11)
- Source: Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic and global orders — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/stocks/news/sterling-and-wilson-renewable-energy-shares-rally-8-after-securing-rs-985-crore-domestic-and-global-orders/articleshow/134402652.cms
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

## Watchlist (below surfacing floor)
dyn_lth ↓ (4.98), comex_copper ↑ (4.87), dyn_4417_t ↑ (4.87), dyn_bac ↓ (4.5), brent_wti_spread ↑ (4.4), dyn_meta ↑ (4.36), dyn_tatatech_ns ↓ (4.28), dyn_tech ↑ (4.28), dyn_ms ↓ (4.26), dyn_sepn ↑ (3.81), midcap_largecap_ratio ↑ (3.64), ig_oas ↓ (3.27)

## India macro
- nifty_50: 23329.0000 (1d -0.36%, z20 -1.11, flag none)
- nifty_midcap_100: 61957.0000 (1d -0.15%, z20 -0.89, flag none)
- usd_inr: 95.5800 (1d -0.45%, z20 0.58, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6558 (1d 0.22%, z20 0.64, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 66.8 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.6 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 63.7 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- COIN (Coinbase Global, Inc.) score 52.6 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- INDIANB.NS (INDIAN BANK) score 51.2 — "U.S. DIESEL HITS FRESH RECORD AT $6.53 U.S. diesel prices climbed to a record $6.527 per g"
- BAC (Bank of America Corporation) score 46.6 — "U.S. DIESEL HITS FRESH RECORD AT $6.53 U.S. diesel prices climbed to a record $6.527 per g"
- HDB (HDFC Bank Limited) score 42.3 — "U.S. DIESEL HITS FRESH RECORD AT $6.53 U.S. diesel prices climbed to a record $6.527 per g"
- IDBI.NS (IDBI BANK LIMITED) score 38.9 — "U.S. DIESEL HITS FRESH RECORD AT $6.53 U.S. diesel prices climbed to a record $6.527 per g"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.9 — "U.S. DIESEL HITS FRESH RECORD AT $6.53 U.S. diesel prices climbed to a record $6.527 per g"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.9 — "U.S. DIESEL HITS FRESH RECORD AT $6.53 U.S. diesel prices climbed to a record $6.527 per g"
- OHI (Omega Healthcare Investors, In) score 37.9 — "Top stocks in focus today: Investors must watch HCL Tech, Persistent, Adani Group shares o"
- CHKP (Check Point Software Technolog) score 36.6 — "Nifty 50 deep-dive guide for investors: Bearish engulfing candlestick; check resistance, s"
- BOND (PIMCO Active Bond Exchange-Tra) score 30.8 — "The bond market is flashing a warning for stocks. These sectors are already wobbling."
- SEPN (Septerna, Inc.) score 27.6 — "Stock Market prediction today: Sensex, Nifty outlook for Wed | Kospi, Taiwan Index, Nikkei"
- TECHM.NS (TECH MAHINDRA LIMITED) score 27.0 — "CATHIE WOOD SHRUGS OFF FED RATE-HIKE FEARS ARK Invest CEO Cathie Wood says higher interest"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 27.0 — "CATHIE WOOD SHRUGS OFF FED RATE-HIKE FEARS ARK Invest CEO Cathie Wood says higher interest"
- TECH (Bio-Techne Corp) score 27.0 — "CATHIE WOOD SHRUGS OFF FED RATE-HIKE FEARS ARK Invest CEO Cathie Wood says higher interest"
- LTH (Life Time Group Holdings, Inc.) score 24.2 — "Sensex rises 110 points, Nifty above 23,450 as oil prices, bond yields cool down. Time for"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.8 — "Noel Tata's latest proposal offers alternative to Tata Sons' listing but Shapoorji Pallonj"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.8 — "Noel Tata's latest proposal offers alternative to Tata Sons' listing but Shapoorji Pallonj"
- 301077.SZ (CHINASTARS) score 19.8 — "CHINA PROBES DEEPSEEK, MOONSHOT OVER POTENTIAL DATA LEAKS TO ANTHROPIC - THE INFORMATION A"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.6 — "Nuclear Safety Brings America Into Russia's Uzbek Energy Project"
- JIOFIN.BO (Jio Financial Services Limited) score 14.6 — "WHAT TO WATCH TODAY — U.S. MARKETS 🔸 8:15 AM ET — 🇺🇸 ADP Weekly Employment Estimate 🔸 10:0"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.2 — "Quantum stocks are getting hot again after a brutal summer. Can the rally last?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.3 — "U.S. HOME PRICES POST FASTEST GROWTH IN A YEAR U.S. home prices rose 3.7% year-over-year i"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.6 — "How to invest amid heightened uncertainty? Look at multi-asset allocation funds, say exper"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.5 — "‘It doesn’t seem fair’: I’m retired and have plenty of money. Why can’t I qualify for a re"
- META (Meta) score 9.3 — "Could Meta’s viral Muse app be the company’s ChatGPT moment?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.2 — "Top stocks in focus today: Investors must watch HCL Tech, Persistent, Adani Group shares o"
- PINELABS.NS (PINE LABS LIMITED) score 6.6 — "Pine Labs block deal: Why Mastercard Asia-Pacific is selling its entire stake for  ₹890 cr"
- MS (Morgan Stanley) score 6.2 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- VT (Vanguard Total World Stock Ind) score 5.7 — "U.S. Threatens to Ground Iranian Airlines Worldwide"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.2 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.3 — "‘She gave a neighbor $2,000’: Social Security overpaid my mother, 82, by $20,000. What els"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.0 — "Action Construction share price jumps 50% in 6 months - ICICI Direct sees it rising furthe"
- GS (Goldman Sachs Group, Inc. (The) score 3.7 — "Goldman Sachs raises target on a stock that has already surged over 140% this year. Do you"
- NVDA (NVIDIA Corporation) score 3.5 — "NVDA - NVIDIA’S HUANG REJECTS CALLS TO SLOW AI Nvidia CEO Jensen Huang says AI development"
- VOLTAS.NS (VOLTAS LTD) score 0.3 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- DELL (Dell Technologies Inc.) score 0.1 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
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