# Transmission Layer — board brief · 2026-11-11 19:33Z

data as of **2026-11-11** · 97 series · 13 red / 32 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.601, 5d in regime; vol-pct 0.79, breadth-off 0.412, Markov P(high-vol) 0.262)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.2, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.21, corr60 0.04, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 -0.02, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.512** (n=1140) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2101) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.79] usd_inr ↓
- usd_inr [FX]: last 93.68, z20 -2.79, zc -0.63, resid-z -0.93 [quiet], 1d -0.28%, 20d range extreme; |z20|=2.79; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.416 via usd_inr, z 2.05, reacted); dyn_indusindbk_bo (rho -0.373 via usd_inr, z 1.6, reacted)
- **India receivers**: dyn_havells_ns (rho -0.416, z 2.05); dyn_indusindbk_bo (rho -0.373, z 1.6)
- Source: Rupee closes at seven-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-closes-at-seven-month-high-of-9369-as-fpi-inflows-lower-crude-prices-boost-sentiment/article71689839.ece
- Source: Rupee rises 7 paise to close at 93.70 against US dollar — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9370-against-us-dollar/article71689281.ece
- Source: Rupee touches strongest since April as foreign inflows offset firm dollar — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-touches-strongest-since-april-as-foreign-inflows-offset-firm-dollar/articleshow/135734005.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 7.55] commodities · 2 series ↓
- wti [COMMODITIES]: last 87.02, z20 -1.78, zc 0.37, resid-z 1.39 [quiet], 1d 1.14%, |z20|=1.78
- brent [COMMODITIES]: last 93.21, z20 -1.71, zc 0.59, resid-z 1.71 [unexplained], 1d 1.88%, 1-session move +1.88% ≥ 1.5%; |z20|=1.71; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.499 via wti, z 2.09, reacted); nifty_midcap_100 (rho -0.461 via wti, z 2.18, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.535 vs brent, historically leads by 1d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.588 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.576 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.519 vs brent
- **India receivers**: dyn_muthootfin_ns (rho -0.499, z 2.09); nifty_midcap_100 (rho -0.461, z 2.18)
- Source: Murphy Oil Draws Boycott Call Over Israeli Gas Licenses — OilPrice, 2026-11-11. https://oilprice.com/Latest-Energy-News/World-News/Murphy-Oil-Draws-Boycott-Call-Over-Israeli-Gas-Licenses.html
- Source: Vitol’s Venezuela Oil Windfall Traced to Trader’s Ties to JD Vance — OilPrice, 2026-11-11. https://oilprice.com/Latest-Energy-News/World-News/Vitols-Venezuela-Oil-Windfall-Traced-to-Traders-Ties-to-JD-Vance.html
- Source: Crude Is Back at 80% in the Gulf, but Refined Products Are Stuck at 35% — OilPrice, 2026-11-11. https://oilprice.com/Energy/Energy-General/Crude-Is-Back-at-80-in-the-Gulf-but-Refined-Products-Are-Stuck-at-35.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.7] cross-asset · 6 series ↑
- nifty_50 [INDICES]: last 25255.05, z20 2.55, zc 1.80, resid-z 2.78 [unexplained], 1d 0.84%, |z20|=2.55
- nifty_metal [INDICES]: last 12787.40, z20 2.28, zc 0.45, resid-z -1.15 [quiet], 1d 0.97%, |z20|=2.28
- dyn_bajfinance_ns [EQUITIES]: last 1078.80, z20 2.22, zc 0.74, resid-z -0.69 [quiet], 1d 1.31%, |z20|=2.22
- nifty_midcap_100 [INDICES]: last 61515.05, z20 2.18, zc 0.00, resid-z -2.77 [unexplained], 1d 0.81%, |z20|=2.18
- nifty_fmcg [INDICES]: last 47188.90, z20 2.10, zc 0.49, resid-z -1.60 [unexplained], 1d 1.13%, |z20|=2.10
- dyn_muthootfin_ns [EQUITIES]: last 2900.00, z20 2.09, zc 0.28, resid-z -0.76 [quiet], 1d -0.60%, |z20|=2.09
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.818 via nifty_midcap_100, z 1.76, reacted); dyn_adanient_bo (rho 0.735 via nifty_metal, z 1.02, reacted); dyn_indusindbk_bo (rho 0.634 via nifty_midcap_100, z 1.6, reacted); dyn_indianb_ns (rho 0.612 via nifty_midcap_100, z 2.99, reacted); dyn_policybzr_ns (rho 0.53 via nifty_midcap_100, z -0.74, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.506 vs nifty_50, historically leads by 5d
- Watch next: dyn_policybzr_ns (co-move) — not yet - watch; rho 0.524 vs dyn_bajfinance_ns
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.512 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.818, z 1.76); dyn_adanient_bo (rho 0.735, z 1.02); dyn_indusindbk_bo (rho 0.634, z 1.6); dyn_indianb_ns (rho 0.612, z 2.99)
- Source: Bajaj Finance launches ₹11,700-crore share sale, sets floor price at ₹992.25 — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/bajaj-finance-launches-11700-crore-share-sale-sets-floor-price-at-99225/article71690436.ece
- Source: Nifty 50 target: Index in sweet spot? 28,000 soon? HSBC, Citi and Bernstein raise targets after sharp 13.5% recovery — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/nifty-50-target-index-in-sweet-spot-28-000-soon-hsbc-citi-and-bernstein-raise-targets-after-sharp-13-5-recovery-11794402943483.html
- Source: Nifty closes 0.84% higher, cooling off from intraday highs — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/nifty-closes-084-higher-cooling-off-from-intraday-highs/article71689484.ece
- Historical analogues: 2025-07-21 (d=1.09), 2025-12-23 (d=1.43), 2025-07-11 (d=1.45)

### [RED 6.62] dxy ↑
- dxy [FX]: last 102.91, z20 3.62, zc 1.90, resid-z 2.61 [unexplained], 1d 0.67%, 20d range extreme; |z20|=3.62; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.561 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 5.9] usd_jpy ↑
- usd_jpy [FX]: last 159.84, z20 3.90, zc 2.46, resid-z 2.37 [unexplained], 1d 1.18%, |z20|=3.90
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.381 via usd_jpy, z -0.33, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.381, z -0.33)
- Source: Top Yen Forecaster Predicts 147 Per Dollar as Rate Gap Narrows — Mint Markets, 2026-11-09. https://www.livemint.com/market/top-yen-forecaster-predicts-147-per-dollar-as-rate-gap-narrows-11794259355721.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [AMBER 5.47] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2076.91, z20 -2.15, zc 0.33, resid-z 0.43 [quiet], 1d 1.30%, |z20|=2.15
- btc_usd [CRYPTO]: last 74270.25, z20 -1.62, zc 0.31, resid-z -0.26 [quiet], 1d 0.75%, |z20|=1.62
- dyn_coin [EQUITIES]: last 137.23, z20 -1.27, zc 0.81, resid-z 0.35 [quiet], 1d 3.86%, 1y-pct=2
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.25).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.738 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.536 vs eth_usd, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.695 vs eth_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.662 vs eth_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.585 vs eth_usd
- Source: How a Super El Niño Could Reshape Global Coal Markets — OilPrice, 2026-11-11. https://oilprice.com/Energy/Energy-General/How-a-Super-El-Nio-Could-Reshape-Global-Coal-Markets.html
- Source: U.S. Midterm Shake-Up Could Reshape Global Oil and Gas Markets — OilPrice, 2026-11-10. https://oilprice.com/Energy/Energy-General/US-Midterm-Shake-Up-Could-Reshape-Global-Oil-and-Gas-Markets.html
- Source: Iran War Set to Drive A Drop in Global Fossil Fuel Emissions in 2026 — OilPrice, 2026-11-10. https://oilprice.com/Latest-Energy-News/World-News/Iran-War-Set-to-Drive-A-Drop-in-Global-Fossil-Fuel-Emissions-in-2026.html
- Historical analogues: 2026-05-22 (d=0.25), 2025-04-10 (d=0.42), 2025-03-31 (d=0.48)

### [RED 4.68] indices · 3 series ↑
- stoxx_50 [INDICES]: last 6392.53, z20 3.36, zc 1.06, resid-z 0.93 [quiet], 1d 1.02%, |z20|=3.36
- cac_40 [INDICES]: last 8330.49, z20 2.38, zc 0.72, resid-z 1.26 [quiet], 1d 0.63%, |z20|=2.38
- dax [INDICES]: last 26644.39, z20 2.37, zc 0.99, resid-z 1.60 [unexplained], 1d 1.13%, |z20|=2.37; 1y-pct=100
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.539 via cac_40, z 2.09, reacted); nifty_fmcg (rho 0.499 via cac_40, z 2.1, reacted); nifty_midcap_100 (rho 0.495 via dax, z 2.18, reacted); dyn_jiofin_bo (rho 0.467 via cac_40, z 1.76, reacted); dyn_tataelxsi_ns (rho 0.439 via cac_40, z 0.83, quiet)
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.511 vs stoxx_50, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.539, z 2.09); nifty_fmcg (rho 0.499, z 2.1); nifty_midcap_100 (rho 0.495, z 2.18); dyn_jiofin_bo (rho 0.467, z 1.76)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [RED 4.64] eur_inr ↓
- eur_inr [FX]: last 103.91, z20 -4.64, zc -1.82, resid-z -1.45 [moved], 1d -1.35%, |z20|=4.64; 1y-pct=4
- **Mechanism**: eur_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-08 (d=0.0), 2025-08-26 (d=0.0)

## Watchlist (below surfacing floor)
dyn_nvda ↓ (4.07), dyn_hdb ↑ (4.05), equities · 2 series ↑ (3.94), commodities · 2 series ↓ (3.88), dyn_lth ↑ (3.45), eur_usd ↓ (3.38), dyn_schd ↑ (3.22), dyn_tech ↑ (3.12), dyn_4417_t ↑ (3.03), cross-asset · 2 series ↑ (2.7), asx_200 ↑ (2.64), aud_usd ↓ (2.43)

## India macro
- nifty_50: 25255.0508 (1d 0.84%, z20 2.55, flag red)
- nifty_midcap_100: 61515.0508 (1d 0.81%, z20 2.18, flag amber)
- usd_inr: 93.6800 (1d -0.28%, z20 -2.79, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4358 (1d -0.03%, z20 -1.37, flag none)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 79.3 — "US Treasury rout hands India's 10-year bond its worst day in a month"
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.6 — "US Treasury rout hands India's 10-year bond its worst day in a month"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 76.4 — "US Treasury rout hands India's 10-year bond its worst day in a month"
- INDIANB.NS (INDIAN BANK) score 54.2 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- BAC (Bank of America Corporation) score 48.1 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- HDB (HDFC Bank Limited) score 40.6 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- TGT (Target Corporation) score 40.6 — "BAIRD SLASHES NVIDIA PRICE TARGET 60%, WARNS OF AI SLOWDOWN Baird downgraded Nvidia ($NVDA"
- NVDA (NVIDIA Corporation) score 39.2 — "BAIRD SLASHES NVIDIA PRICE TARGET 60%, WARNS OF AI SLOWDOWN Baird downgraded Nvidia ($NVDA"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.8 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.2 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- TECH (Bio-Techne Corp) score 38.2 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.5 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 37.5 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.5 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- 301077.SZ (CHINASTARS) score 35.3 — "Baird downgrades Nvidia on China curbs, AI demand worries"
- OHI (Omega Healthcare Investors, In) score 28.9 — "Market angst is driving investors into low-volatility stocks as AI trade stumbles"
- CHKP (Check Point Software Technolog) score 24.9 — "Top 2 stocks to buy for short-term: Canara Bank, Pine Labs by Nagaraj Shetti - Check stop "
- COIN (Coinbase Global, Inc.) score 24.2 — "How a Super El Niño Could Reshape Global Coal Markets"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.3 — "US Treasury rout hands India's 10-year bond its worst day in a month"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "China Expands Its Central Asian Footprint Through Aviation, Energy, and Trade"
- LTH (Life Time Group Holdings, Inc.) score 19.4 — "Protean eGov shares surge 7.4% as Yubi partnership boosts sentiment"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.1 — "Fairfax Financial likely to exit IIFL Finance, sources say"
- SCHD (Schwab US Dividend Equity ETF) score 14.6 — "Edelweiss Alternatives’ H1FY27 profit rises 35% to ₹169 crore; declares ₹7 interim dividen"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.6 — "Tata Steel Share Price Highlights: Tata Steel Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.6 — "Tata Steel Share Price Highlights: Tata Steel Stock Price History"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.5 — "Fairfax Financial likely to exit IIFL Finance, sources say"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.4 — "Trump says Iran war ‘effectively over’: How's it likely to impact Sensex, Nifty, gold and "
- BZ=F (Brent Crude Oil Last Day Finan) score 9.9 — "ONGC dividend 2026: Last day to buy today | Check dividend payout, record date, history, y"
- JIOFIN.BO (Jio Financial Services Limited) score 9.8 — "Fairfax Financial likely to exit IIFL Finance, sources say"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.9 — "Adani Ent Share Price Highlights: Adani Ent. Stock Price History"
- RS (Reliance, Inc.) score 6.5 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- META (Meta) score 6.4 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- DEMZ (Democratic Large Cap Core ETF) score 6.0 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- JEF (Jefferies Financial Group Inc.) score 5.3 — "RIL, HDFC, Axis Bank, IndiGo, more: List of 12 stocks from Jefferies; shares to gain as FP"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.2 — "CoreWeave just gave a shot in the arm to Micron, Lumentum and the rest of the AI trade"
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast"
- CRWV (CoreWeave, Inc.) score 4.8 — "Nasdaq futures rise nearly 2% as CoreWeave earnings calm AI spending fears"
- SEPN (Septerna, Inc.) score 3.5 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.3 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.1 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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