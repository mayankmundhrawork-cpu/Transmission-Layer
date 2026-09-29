# Transmission Layer — board brief · 2026-09-29 18:05Z

data as of **2026-09-29** · 97 series · 16 red / 31 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.643, 4d in regime; vol-pct 0.581, breadth-off 0.706, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.56, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.05, corr60 0.14, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.09, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.76, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.07, corr60 -0.09, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.15, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.44, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **8 of 89** scanned series survive multiplicity control (effective p ≤ 0.008049177085516668)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.5** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2378) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.37] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4175.40, z20 -2.68, zc 0.58, resid-z -0.30 [quiet], 1d 0.59%, |z20|=2.68; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.10, z20 -2.55, zc -0.10, resid-z -0.93 [quiet], 1d -0.20%, |z20|=2.55; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.34, z20 1.05, zc n/a, resid-z n/a [quiet], 1d 0.80%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.597 vs comex_silver, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.587 vs comex_gold
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.585 vs comex_gold
- Source: Shanti Gold vs Sky Gold: Which jewellery stock has more upside? Check share price targets by BOB Capital — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/shanti-gold-vs-sky-gold-which-jewellery-stock-has-more-upside-check-share-price-targets-by-bob-capital-11790677887897.html
- Source: Gold traders to protest on Oct 15 against MDR on UPI dealings — BusinessLine Mkts, 2026-09-29. https://www.thehindubusinessline.com/markets/gold/gold-traders-to-protest-on-oct-15-against-mdr-on-upi-dealings/article71523296.ece
- Source: Gold edges up from 7-week low; all eyes on West Asia, US economic data — BusinessLine Mkts, 2026-09-29. https://www.thehindubusinessline.com/markets/gold/gold-edges-up-from-7-week-low-all-eyes-on-west-asia-us-economic-data/article71522988.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.36] fx · 4 series ↓
- usd_mxn [FX]: last 18.10, z20 3.70, zc 2.66, resid-z 4.29 [unexplained], 1d 1.95%, |z20|=3.70
- aud_usd [FX]: last 0.70, z20 -2.50, zc -0.72, resid-z -1.28 [quiet], 1d -0.45%, |z20|=2.50
- eur_usd [FX]: last 1.13, z20 -2.28, zc -1.28, resid-z -1.05 [quiet], 1d -0.42%, |z20|=2.28; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -1.97, zc -0.21, resid-z -0.16 [quiet], 1d -0.08%, |z20|=1.97
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.482 via usd_mxn, z -2.76, reacted); dyn_icicigi_bo (rho -0.479 via gbp_usd, z 0.23, quiet); dyn_muthootfin_ns (rho 0.464 via aud_usd, z -1.75, reacted); dyn_inoxindia_ns (rho 0.405 via aud_usd, z -0.81, quiet); nifty_midcap_100 (rho -0.397 via usd_mxn, z -2.74, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.541 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_policybzr_ns (rho -0.482, z -2.76); dyn_icicigi_bo (rho -0.479, z 0.23); dyn_muthootfin_ns (rho 0.464, z -1.75); dyn_inoxindia_ns (rho 0.405, z -0.81)
- Source: Euro zone bond selloff hits pause, yields fall from multi-year highs — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-selloff-hits-pause-yields-fall-from-multi-year-highs/articleshow/134563785.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 7.1] commodities · 2 series ↓
- wti [COMMODITIES]: last 90.14, z20 -1.27, zc -0.96, resid-z -0.95 [quiet], 1d -2.66%, 1-session move -2.66% ≥ 1.5%
- brent [COMMODITIES]: last 96.72, z20 -1.19, zc -2.97, resid-z -3.11 [unexplained], 1d -8.13%, 1-session move -8.13% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.566 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.543 vs wti
- Source: Iran Talks Take the Heat Out of the Oil Rally — OilPrice, 2026-09-29. https://oilprice.com/Energy/Crude-Oil/Iran-Talks-Take-the-Heat-Out-of-the-Oil-Rally.html
- Source: Global Markets: Tech stocks gain on Anthropic IPO optimism, offsetting high oil, yields — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-tech-stocks-gain-on-anthropic-ipo-optimism-offsetting-high-oil-yields/articleshow/134568836.cms
- Source: Rupee breaches 96 per dollar as oil surge stokes pressure; RBI intervention limits fall — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-breaches-96-per-dollar-as-oil-surge-stokes-pressure-rbi-intervention-limits-fall/articleshow/134565213.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 6.87] hy_oas ↑
- hy_oas [RATES]: last 3.02, z20 4.87, zc 2.51, resid-z 4.08 [unexplained], 1d 3.07%, |z20|=4.87
- **Mechanism**: hy_oas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S. high-yield debt issuance is straining investor demand, pushing junk-bond spreads to their widest since April. September issuance has reached $38.5 billion, while CCC spreads have surged to their highest since — DeItaone, 2026-09-28. https://t.me/walter_bloomberg/36264
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-25 (d=0.0), 2025-07-31 (d=0.01)

### [RED 6.75] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.49, z20 2.82, zc 0.44, resid-z 0.60 [quiet], 1d 0.37%, |z20|=2.82; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.97, z20 -2.34, zc -0.85, resid-z 0.13 [quiet], 1d -0.34%, |z20|=2.34; 1y-pct=0
- tips_10y_real [RATES]: last 2.83, z20 2.13, zc -0.31, resid-z -0.18 [quiet], 1d -0.70%, |z20|=2.13; 1y-pct=99
- ust_10y [RATES]: last 5.17, z20 2.05, zc -0.18, resid-z -0.02 [quiet], 1d -0.19%, |z20|=2.05; 1y-pct=99
- ust_2y [RATES]: last 4.81, z20 1.31, zc -0.92, resid-z -0.78 [quiet], 1d -1.23%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.55 vs dyn_bond
- Source: US 30-year Treasury yield tops 5.6%, reaching highest level since 2002 — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-30-year-treasury-yield-tops-5-6-reaching-highest-level-since-2002/articleshow/134570770.cms
- Source: The hidden messages the bond market is sending about the AI boom and the stock market — MarketWatch Top, 2026-09-29. https://www.marketwatch.com/story/the-hidden-messages-the-bond-market-is-sending-about-the-ai-boom-and-the-stock-market-5c9495ba?mod=mw_rss_topstories
- Source: US stocks: US market slips as rising Treasury yields offset AI-driven tech gains — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-sp-nasdaq-open-higher-on-oil-retreat-tech-optimism/articleshow/134568670.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.42] cross-asset · 4 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1081.00, z20 -2.76, zc -0.35, resid-z -1.30 [quiet], 1d -6.11%, |z20|=2.76; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 59321.25, z20 -2.74, zc -1.00, resid-z -1.47 [quiet], 1d -0.99%, |z20|=2.74
- nifty_50 [INDICES]: last 22716.20, z20 -2.21, zc -0.41, resid-z -1.06 [quiet], 1d -0.28%, |z20|=2.21; 1y-pct=2
- india_vix [INDICES]: last 13.34, z20 1.76, zc -0.37, resid-z n/a [quiet], 1d -2.22%, |z20|=1.76
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.605 via nifty_midcap_100, z -2.58, reacted); dyn_jiofin_bo (rho 0.583 via nifty_50, z -2.82, reacted); nifty_fmcg (rho 0.557 via nifty_50, z -2.17, reacted); dyn_techm_ns (rho 0.494 via nifty_50, z -1.65, reacted); dyn_indusindbk_bo (rho 0.482 via nifty_midcap_100, z -2.77, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.605, z -2.58); dyn_jiofin_bo (rho 0.583, z -2.82); nifty_fmcg (rho 0.557, z -2.17); dyn_techm_ns (rho 0.494, z -1.65)
- Source: Nifty 50 down 13.5% in 2026, set for worst year in 15 years: Key factors weighing on market sentiment — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/nifty-50-down-13-5-in-2026-set-for-worst-year-in-15-years-key-factors-weighing-on-market-sentiment-11790688426677.html
- Source: Nifty 50 falls 6.3% in September, worst monthly series in 25 years; what triggered the sell-off? — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/nifty-50-falls-6-3-in-september-worst-monthly-series-in-25-years-what-triggered-the-selloff-11790689288980.html
- Source: Nifty sees worst September series in 25 years. What does October hold? — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/stocks/news/nifty-sees-worst-september-series-in-25-years-what-does-october-hold/articleshow/134569275.cms
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 5.08] dxy ↑
- dxy [FX]: last 101.59, z20 2.08, zc 1.14, resid-z -0.82 [quiet], 1d 0.39%, 20d range extreme; |z20|=2.08; 1y-pct=99
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [RED 5.04] dyn_chkp ↓
- dyn_chkp [EQUITIES]: last 125.89, z20 -3.04, zc -1.13, resid-z -1.27 [quiet], 1d -2.61%, |z20|=3.04
- **Mechanism**: dyn_chkp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.367 via dyn_chkp, z -1.99, reacted)
- **India receivers**: dyn_tatatech_ns (rho 0.367, z -1.99)
- Source: Maruti Suzuki vs TVS Motor vs Mahindra: Which auto stock to buy ahead of festive season? Check target price — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/maruti-suzuki-vs-tvs-motor-vs-mahindra-which-auto-stock-to-buy-ahead-of-festive-season-check-target-price-11790698377129.html
- Source: Vedanta's demerger report card: Vedanta Iron to Vedanta Power - Who gained, who lagged since listing? Check real winner — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/vedantas-demerger-report-card-vedanta-iron-to-vedanta-power-who-gained-who-lagged-since-listing-check-real-winner-11790681601033.html
- Source: Shanti Gold vs Sky Gold: Which jewellery stock has more upside? Check share price targets by BOB Capital — Mint Markets, 2026-09-29. https://www.livemint.com/market/stock-market-news/shanti-gold-vs-sky-gold-which-jewellery-stock-has-more-upside-check-share-price-targets-by-bob-capital-11790677887897.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

## Watchlist (below surfacing floor)
dyn_jiofin_bo ↓ (4.82), shanghai_comp ↓ (4.21), dyn_havells_ns ↓ (4.02), dyn_4417_t ↑ (3.16), dyn_nvda ↑ (3.03), usd_brl ↑ (2.97), dyn_indusindbk_bo ↓ (2.77), dyn_indianb_ns ↓ (2.72), dyn_hdb ↓ (2.68), dyn_atherenerg_ns ↓ (2.65), midcap_largecap_ratio ↓ (2.58), commodities · 2 series ↓ (2.47)

## India macro
- nifty_50: 22716.1992 (1d -0.28%, z20 -2.21, flag amber)
- nifty_midcap_100: 59321.2500 (1d -0.99%, z20 -2.74, flag red)
- usd_inr: 95.9700 (1d 0.19%, z20 1.01, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6114 (1d -0.71%, z20 -2.58, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 79.8 — "El Nino effect: India’s coal imports may rise in October-December"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.5 — "El Nino effect: India’s coal imports may rise in October-December"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.4 — "El Nino effect: India’s coal imports may rise in October-December"
- INDIANB.NS (INDIAN BANK) score 50.0 — "Rupee hits two-month low, slips past 96 | What does it mean for the Indian stock market?"
- COIN (Coinbase Global, Inc.) score 46.7 — "Global Markets: Tech stocks gain on Anthropic IPO optimism, offsetting high oil, yields"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.4 — "Top stocks to buy or sell in F&O segment: Alkem Lab, KFin Tech, Amber Ent by Jay Thakkar -"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.4 — "Top stocks to buy or sell in F&O segment: Alkem Lab, KFin Tech, Amber Ent by Jay Thakkar -"
- TECH (Bio-Techne Corp) score 41.4 — "Top stocks to buy or sell in F&O segment: Alkem Lab, KFin Tech, Amber Ent by Jay Thakkar -"
- OHI (Omega Healthcare Investors, In) score 40.8 — "Bitcoin testing highs above $84,000 again, can this rally sustain? Here's what experts say"
- CHKP (Check Point Software Technolog) score 38.0 — "Top stocks to buy or sell in F&O segment: Alkem Lab, KFin Tech, Amber Ent by Jay Thakkar -"
- BOND (PIMCO Active Bond Exchange-Tra) score 37.2 — "Euro zone bond selloff hits pause, yields fall from multi-year highs"
- HDB (HDFC Bank Limited) score 33.7 — "Quote of the day by Irving Fisher: "A chief cause of crises, panics, runs on banks, etc., "
- BAC (Bank of America Corporation) score 32.1 — "Quote of the day by Irving Fisher: "A chief cause of crises, panics, runs on banks, etc., "
- IDBI.NS (IDBI BANK LIMITED) score 29.7 — "Quote of the day by Irving Fisher: "A chief cause of crises, panics, runs on banks, etc., "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 29.7 — "Quote of the day by Irving Fisher: "A chief cause of crises, panics, runs on banks, etc., "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 29.7 — "Quote of the day by Irving Fisher: "A chief cause of crises, panics, runs on banks, etc., "
- SEPN (Septerna, Inc.) score 29.1 — "ABSLAMC launches industry’s first BSE Total Market Index Fund, NFO opens September 30"
- LTH (Life Time Group Holdings, Inc.) score 28.9 — "Oura IPO: Smart ringmaker delays US public issue after 4 times oversubscription"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.8 — "UAE's Next $25 Billion Bet On India Includes Energy Sector"
- 301077.SZ (CHINASTARS) score 26.1 — "China rolls out new measures to bolster its property sector and economy"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.8 — "Market wrap: Adani Enterprises, Adani Ports, Titan Company, Wipro top gainers and losers o"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.6 — "Top stocks in focus tomorrow: Investors must watch Tata Steel, KSB, Power Mech, TCI shares"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.6 — "Top stocks in focus tomorrow: Investors must watch Tata Steel, KSB, Power Mech, TCI shares"
- TGT (Target Corporation) score 14.1 — "IndiGo share price: Goldman Sachs sees over 21% upside | Target price, detailed outlook"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.7 — "IPO Today: Orient Cables, German Green IPOs see strong demand on last day; AceVector, Runw"
- POLICYBZR.NS (PB FINTECH LIMITED) score 11.4 — "PB Fintech shares suffer Rs 37,000 crore shock in 4 days but Jefferies, Bernstein see up t"
- JIOFIN.BO (Jio Financial Services Limited) score 10.3 — "Stocks to buy: JM Financial expects soft Q2 season for IT majors; check target prices for "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 10.1 — "Bitcoin testing highs above $84,000 again, can this rally sustain? Here's what experts say"
- META (Meta) score 9.2 — "Nifty Metal slips 5% in September post 29% 1 yr rally, October comeback ahead? Hindustan Z"
- GS (Goldman Sachs Group, Inc. (The) score 7.7 — "IndiGo share price: Goldman Sachs sees over 21% upside | Target price, detailed outlook"
- VT (Vanguard Total World Stock Ind) score 7.5 — "World's Tallest Dam Project Gets New Life With Fresh World Bank Funding"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.1 — "Auto stocks: Festive demand gets a low-base boost; can earnings justify valuations?"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.5 — "Broker’s Call: Home First Finance (Add)"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.4 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- NVDA (NVIDIA Corporation) score 5.0 — "Nvidia $150 billion share buyback: Should you participate post-record date announcement?"
- MS (Morgan Stanley) score 4.5 — "A month ago, this JPMorgan team urged caution on stocks. Now it’s going all in on tech."
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.5 — "ETMarkets Smart Talk| F&O STT, UPI charges and trading costs: Sandeep Neema on the hidden "
- MU (Micron Technology, Inc.) score 2.9 — "Global Market: South Korean stocks under pressure ahead of trade data, Micron results"
- VOLTAS.NS (VOLTAS LTD) score 0.6 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.3 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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