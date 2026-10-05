# Transmission Layer — board brief · 2026-10-05 20:44Z

data as of **2026-10-05** · 97 series · 6 red / 41 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.684, 1d in regime; vol-pct 0.7, breadth-off 0.667, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.42, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.19, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.03, corr60 0.12, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.25, corr60 -0.09, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.587, β -0.4304, p 0.0); driver zc 2.61 → expected -1.131%. Type hit-rate 0.817 (n=2334).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.384, β 0.2222, p 0.0); driver zc 2.61 → expected 0.584%. Type hit-rate 0.817 (n=2334).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.37, β -0.2069, p 0.0); driver zc 2.61 → expected -0.543%. Type hit-rate 0.817 (n=2334).
- Track record · residual_reversion: hit-rate **0.496** (n=1128) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2334) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.81] bovespa ↑
- bovespa [INDICES]: last 207190.44, z20 10.81, zc 2.61, resid-z 2.06 [unexplained], 1d 7.85%, |z20|=10.81; 1y-pct=100
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_stylebaaza_ns (rho -0.433 via bovespa, z -2.39, reacted)
- **India receivers**: dyn_stylebaaza_ns (rho -0.433, z -2.39)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

### [AMBER 7.29] commodities · 2 series ↓
- wti [COMMODITIES]: last 89.19, z20 -1.46, zc -0.70, resid-z -0.36 [quiet], 1d -2.11%, 1-session move -2.11% ≥ 1.5%
- brent [COMMODITIES]: last 100.20, z20 -1.06, zc -0.03, resid-z 0.37 [quiet], 1d -2.00%, 1-session move -2.00% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dax (inverse) — not yet - watch; rho -0.519 vs wti, historically leads by 1d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.599 vs wti
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.51 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.508 vs wti
- Source: Southeast Asia’s Oil and Gas M&A Market Is Heating Up — OilPrice, 2026-10-05. https://oilprice.com/Energy/Energy-General/Southeast-Asias-Oil-and-Gas-MA-Market-Is-Heating-Up.html
- Source: Saudi Aramco’s CEO may be too downbeat about the road to restocking global oil supplies — MarketWatch Top, 2026-10-05. https://www.marketwatch.com/story/saudi-aramcos-ceo-may-be-too-downbeat-about-the-road-to-restocking-global-oil-supplies-1fdbb70b?mod=mw_rss_topstories
- Source: Iran’s Oil Minister Resigns as U.S. Blockade Chokes Crude Exports — OilPrice, 2026-10-05. https://oilprice.com/Latest-Energy-News/World-News/Irans-Oil-Minister-Resigns-as-US-Blockade-Chokes-Crude-Exports.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 6.25] usd_inr ↑
- usd_inr [FX]: last 96.30, z20 1.25, zc 0.58, resid-z 0.31 [quiet], 1d 0.08%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.396 via usd_inr, z 0.96, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.396, z 0.96)
- Source: Rupee edges higher as traders await RBI policy decision on rates — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-edges-higher-as-traders-await-rbi-policy-decision-on-rates/articleshow/134707753.cms
- Source: Rupee ends flat, anchored by RBI intervention in face of global strains — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-ends-flat-anchored-by-rbi-intervention-in-face-of-global-strains/articleshow/134700361.cms
- Source: Gap-Up fades as IT and HDFC Bank drag Nifty to near-flat; crude, Rupee weigh — BusinessLine Mkts, 2026-10-05. https://www.thehindubusinessline.com/markets/gap-up-fades-as-it-and-hdfc-bank-drag-nifty-to-near-flat-crude-rupee-weigh/article71546207.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.03] indices · 2 series ↑
- nikkei_225 [INDICES]: last 69928.05, z20 3.20, zc -0.47, resid-z -0.82 [quiet], 1d 2.37%, |z20|=3.20; 1y-pct=97
- taiwan_weighted [INDICES]: last 49666.41, z20 2.84, zc 0.23, resid-z -0.28 [quiet], 1d 2.46%, |z20|=2.84; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.544 via taiwan_weighted, z -1.41, reacted); nifty_it (rho -0.374 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.842 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.544, z -1.41); nifty_it (rho -0.374, z -0.73)
- Source: Global Market: Japan’s Nikkei jumps 2.5% to 3-month high as AI stocks rally — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-jumps-2-5-to-3-month-high-as-ai-stocks-rally/articleshow/134685851.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [AMBER 5.96] cross-asset · 4 series ↓
- india_vix [INDICES]: last 14.71, z20 2.30, zc 1.21, resid-z n/a [quiet], 1d 1.73%, |z20|=2.30
- dyn_policybzr_ns [EQUITIES]: last 976.20, z20 -1.92, zc -1.18, resid-z -0.96 [quiet], 1d -0.39%, 1y-pct=0
- nifty_50 [INDICES]: last 22555.75, z20 -1.82, zc -1.36, resid-z -1.34 [quiet], 1d 0.60%, |z20|=1.82; 1y-pct=1
- nifty_midcap_100 [INDICES]: last 59127.45, z20 -1.81, zc -1.06, resid-z -0.70 [quiet], 1d 0.67%, |z20|=1.81
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.634 via nifty_midcap_100, z -1.32, reacted); nifty_fmcg (rho 0.573 via nifty_50, z -1.43, reacted); dyn_bajfinance_ns (rho -0.572 via india_vix, z -1.41, reacted); dyn_jiofin_bo (rho 0.537 via nifty_50, z -2.5, reacted); nifty_metal (rho 0.521 via nifty_midcap_100, z -2.21, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.634, z -1.32); nifty_fmcg (rho 0.573, z -1.43); dyn_bajfinance_ns (rho -0.572, z -1.41); dyn_jiofin_bo (rho 0.537, z -2.5)
- Source: Nifty prediction: RSI still hints at weak momentum | Resistance, support, LG Electronics India stock to watch — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/nifty-prediction-rsi-still-hints-at-weak-momentum-resistance-support-lg-electronics-india-stock-to-watch-11791221648017.html
- Source: Top 3 stock picks by Vaishali Parekh: ITC, MRPL, KEI Industries | Target, stop-loss, Nifty, Bank Nifty outlook — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/top-3-stock-picks-by-vaishali-parekh-itc-mrpl-kei-industries-target-stop-loss-nifty-bank-nifty-outlook-11791213624948.html
- Source: Hindustan Unilever, PB Fintech among 7 stocks that hit 52-week lows and slipped up to 47% in a month — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-unilever-pb-fintech-among-7-stocks-that-hit-52-week-lows-and-slipped-up-to-47-in-a-month/slideshow/134705609.cms
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.88] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.63, z20 1.95, zc 0.44, resid-z 0.65 [quiet], 1d 0.36%, |z20|=1.95; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.38, z20 -1.91, zc -0.58, resid-z -0.41 [quiet], 1d -0.18%, 1y-pct=0
- ust_10y [RATES]: last 5.28, z20 1.61, zc 0.72, resid-z 1.07 [quiet], 1d 0.76%, |z20|=1.61; 1y-pct=99
- tips_10y_real [RATES]: last 2.92, z20 1.52, zc 0.69, resid-z 1.03 [quiet], 1d 1.39%, |z20|=1.52; 1y-pct=99
- ust_2y [RATES]: last 4.83, z20 0.82, zc 0.78, resid-z 1.10 [quiet], 1d 1.05%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.529 vs ust_10y, historically leads by 4d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.528 vs ust_30y
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.521 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.507 vs ust_30y
- Source: Investors see big opportunity in ferocious 2026 bond-market rout — MarketWatch Top, 2026-10-05. https://www.marketwatch.com/story/investors-see-big-opportunity-in-ferocious-2026-bond-market-rout-e5cc94f3?mod=mw_rss_topstories
- Source: French bond contagion fears are rattling the euro — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/french-bond-contagion-fears-are-rattling-the-euro/articleshow/134714445.cms
- Source: Indian State Firm BPCL Readies $3-Billion Bond to Fund Brazil oil Project — OilPrice, 2026-10-05. https://oilprice.com/Latest-Energy-News/World-News/Indian-State-Firm-BPCL-Readies-3-Billion-Bond-to-Fund-Brazil-oil-Project.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 4.74] dxy ↑
- dxy [FX]: last 102.15, z20 1.74, zc -0.47, resid-z -0.40 [quiet], 1d 0.22%, 20d range extreme; |z20|=1.74; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [AMBER 4.73] rates · 2 series ↑
- ig_oas [RATES]: last 0.85, z20 1.89, zc -0.69, resid-z -0.96 [quiet], 1d -1.16%, |z20|=1.89
- hy_oas [RATES]: last 3.10, z20 1.75, zc -1.61, resid-z -2.96 [unexplained], 1d -4.32%, |z20|=1.75
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.425 via ig_oas, z -2.31, reacted); nifty_midcap_100 (rho -0.414 via ig_oas, z -2.37, reacted)
- **India receivers**: dyn_policybzr_ns (rho -0.479, z -1.92); nifty_midcap_100 (rho -0.464, z -1.81); nifty_50 (rho -0.357, z -1.82)

## Watchlist (below surfacing floor)
indices · 2 series ↑ (4.67), dyn_jiofin_bo ↓ (4.5), dyn_nvda ↑ (4.45), dyn_stylebaaza_ns ↓ (4.39), dyn_ohi ↓ (4.37), hang_seng ↓ (4.22), eur_usd ↓ (4.22), usd_brl ↓ (3.77), comex_gold ↓ (3.68), dyn_4417_t ↑ (3.63), dyn_tech ↑ (3.51), dyn_hdb ↓ (3.41)

## India macro
- nifty_50: 22555.7500 (1d 0.60%, z20 -1.82, flag amber)
- nifty_midcap_100: 59127.4492 (1d 0.67%, z20 -1.81, flag amber)
- usd_inr: 96.3000 (1d 0.08%, z20 1.25, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6214 (1d 0.08%, z20 -1.32, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI MPC decision T-2d · AMFI SIP / MF flows T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 73.6 — "Broker’s call: Vesuvius India (Buy)"
- COALINDIA.NS (COAL INDIA LTD) score 71.1 — "Broker’s call: Vesuvius India (Buy)"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 70.0 — "Broker’s call: Vesuvius India (Buy)"
- INDIANB.NS (INDIAN BANK) score 64.7 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- BAC (Bank of America Corporation) score 46.9 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- BOND (PIMCO Active Bond Exchange-Tra) score 45.3 — "JPMORGAN: BOND YIELD SPIKE WON’T DERAIL STOCKS JPMorgan says the recent surge in bond yiel"
- COIN (Coinbase Global, Inc.) score 45.1 — "U.S.-RUSSIA UKRAINE TALKS EXPAND TO MULTIBILLION-DOLLAR OIL DEAL Trump administration talk"
- HDB (HDFC Bank Limited) score 44.7 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- IDBI.NS (IDBI BANK LIMITED) score 42.1 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.1 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.1 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- OHI (Omega Healthcare Investors, In) score 41.8 — "SEBI chairman warns investors against anonymous tips, finfluencers; launches Project Jagro"
- TECHM.NS (TECH MAHINDRA LIMITED) score 34.8 — "ALTMAN: WORLD SHOULD ACCEPT SOME AI RISKS OpenAI CEO Sam Altman says “the world should acc"
- CHKP (Check Point Software Technolog) score 33.0 — "TRUMP PROMISES $5,000 PAYMENTS IF GOP WINS MIDTERMS President Trump says he would give eve"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.4 — "ALTMAN: WORLD SHOULD ACCEPT SOME AI RISKS OpenAI CEO Sam Altman says “the world should acc"
- TECH (Bio-Techne Corp) score 30.4 — "ALTMAN: WORLD SHOULD ACCEPT SOME AI RISKS OpenAI CEO Sam Altman says “the world should acc"
- TGT (Target Corporation) score 29.9 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- LTH (Life Time Group Holdings, Inc.) score 28.0 — "MUSK TO RENAME SPACEXAI AS “SPACEXSI” Elon Musk says he will rename SpaceXAI to SpaceXSI, "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.9 — "Nayara Energy hikes petrol by ₹5, diesel by ₹3"
- SEPN (Septerna, Inc.) score 23.0 — "COIN - BOFA RAISES COINBASE TARGET TO $203 BofA raised its Coinbase price target to $203 f"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 16.2 — "AI stock Nvidia stock gets target upgrade from BNP Paribas; 47% further upside seen by exp"
- 301077.SZ (CHINASTARS) score 14.0 — "China returns to top 100 in gender parity ranking for first time since 2016"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.4 — "JPMORGAN: BOND YIELD SPIKE WON’T DERAIL STOCKS JPMorgan says the recent surge in bond yiel"
- JIOFIN.BO (Jio Financial Services Limited) score 10.6 — "WHAT TO WATCH TODAY — U.S. MARKETS 🔸 9:20 AM ET — 🇺🇸 NY Fed Bill Purchases, 4–12 months 🔸 "
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.5 — "BOFA: ACTIVE FUNDS STRUGGLE AS MEGACAPS DOMINATE Just 44% of large-cap active funds beat t"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.7 — "Piramal Finance directors okay ₹1,750-cr preferential allotment of warrants to promoter gr"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.1 — "Adani Energy Solutions share price rally: From  ₹990 to  ₹1,350 in just 6 months: Know why"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.7 — "Value retail stocks slide on cautious consumer spending"
- JEF (Jefferies Financial Group Inc.) score 6.2 — "Bajaj Finance shares jump 5% after Q2 business update. Why Jefferies sees 35% upside in it"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 6.0 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 6.0 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.6 — "Hindustan Unilever, PB Fintech among 7 stocks that hit 52-week lows and slipped up to 47% "
- NVDA (NVIDIA Corporation) score 5.6 — "AI stock Nvidia stock gets target upgrade from BNP Paribas; 47% further upside seen by exp"
- VT (Vanguard Total World Stock Ind) score 4.8 — "ALTMAN: WORLD SHOULD ACCEPT SOME AI RISKS OpenAI CEO Sam Altman says “the world should acc"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 4.7 — "Piramal Finance directors okay ₹1,750-cr preferential allotment of warrants to promoter gr"
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "U.S. Diesel Export Ban Would Hit Latin America Hardest: Goldman"
- META (Meta) score 4.3 — "META PARTS WAYS WITH VIRTUE AI - SEMAFOR"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.9 — "20 Stocks to watch today: HDFC Bank, ICICI life, Wipro, DLF, Ola Electric & Gland Pharma"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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