# Transmission Layer — board brief · 2026-08-24 16:54Z

data as of **2026-08-24** · 98 series · 14 red / 31 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.313, 2d in regime; vol-pct 0.274, breadth-off 0.353, Markov P(high-vol) 0.013)
- [WEAK] **safe_haven_gold** — corr20 -0.24, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.73, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.41, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.21, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.29, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.002288413662045352)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1113) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2454) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.81] commodities · 2 series ↑
- corn [COMMODITIES]: last 521.75, z20 4.97, zc 6.17, resid-z 4.90 [unexplained], 1d 7.86%, |z20|=4.97; 1y-pct=100
- wheat [COMMODITIES]: last 706.25, z20 3.03, zc 2.19, resid-z 1.90 [unexplained], 1d 3.63%, |z20|=3.03; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 7.3] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 79125.49, z20 3.64, zc 0.22, resid-z 0.81 [quiet], 1d 1.01%, |z20|=3.64
- eth_usd [CRYPTO]: last 2484.89, z20 2.97, zc -0.24, resid-z 0.08 [quiet], 1d -1.21%, |z20|=2.97
- dyn_mrna [EQUITIES]: last 137.01, z20 2.70, zc -0.42, resid-z 4.54 [unexplained], 1d -5.59%, |z20|=2.70; 1y-pct=99
- dyn_coin [EQUITIES]: last 184.56, z20 2.70, zc -0.19, resid-z 2.63 [unexplained], 1d -1.03%, |z20|=2.70
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.58).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global oil prices above $90 a barrel ahead of Bessent’s ‘economic D-Day’ announcement on Iran — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/oil-trades-lower-even-as-bessent-promises-economic-d-day-announcement-on-iran-a90d862e?mod=mw_rss_topstories
- Source: Global Markets: Fast-fashion giant Shein shrinks value to up to $27 billion in Hong Kong IPO — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-fast-fashion-giant-shein-shrinks-value-to-up-to-27-billion-in-hong-kong-ipo/articleshow/133466240.cms
- Source: MSTR - STRATEGY BUILDS $1.6 BILLION WAR CHEST Strategy has created a new $1.59 billion USD Cash pool, giving it more flexibility to buy Bitcoin, repurchase shares or manage debt. The company also holds a $5.1 billion USD Reserve. Strategy raised roughly $2 billion by selling — DeItaone, 2026-08-24. https://t.me/walter_bloomberg/34932
- Historical analogues: 2025-08-13 (d=0.58), 2025-05-09 (d=1.5), 2024-11-21 (d=1.59)

### [AMBER 7.03] commodities · 2 series ↑
- brent [COMMODITIES]: last 92.69, z20 1.19, zc -0.88, resid-z -0.56 [quiet], 1d -1.80%, 1-session move -1.80% ≥ 1.5%
- wti [COMMODITIES]: last 85.36, z20 0.91, zc -0.87, resid-z -0.52 [quiet], 1d -1.95%, 1-session move -1.95% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.598 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.581 vs brent, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.55 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.688 vs brent
- Source: Global oil prices above $90 a barrel ahead of Bessent’s ‘economic D-Day’ announcement on Iran — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/oil-trades-lower-even-as-bessent-promises-economic-d-day-announcement-on-iran-a90d862e?mod=mw_rss_topstories
- Source: Oil trades lower even as Bessent promises ‘economic D-Day’ announcement on Iran — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/oil-trades-lower-even-as-bessent-promises-economic-d-day-announcement-on-iran-a90d862e?mod=mw_rss_topstories
- Source: MRPL says no single geography, supplier or route decisive for crude sourcing — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/commodities/mrpl-says-no-single-geography-supplier-or-route-decisive-for-crude-sourcing/article71384527.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.77] commodities · 3 series ↑
- comex_gold [COMMODITIES]: last 4718.20, z20 2.45, zc 1.14, resid-z 0.88 [quiet], 1d 2.03%, |z20|=2.45; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 68.82, z20 1.67, zc -0.36, resid-z -2.65 [unexplained], 1d -0.93%, |z20|=1.67; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.62, z20 0.79, zc 0.26, resid-z 0.71 [quiet], 1d 0.58%, 1y-pct=98; co-occur[metal_copper] suppressed: channel WEAK
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.48 via comex_silver, z 1.73, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.86 vs comex_silver, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.56 vs comex_silver, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.535 vs comex_copper, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.521 vs comex_gold, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.501 vs comex_copper, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.48, z 1.73)
- Source: Hindustan Copper OFS: Government to sell up to 6% stake at  ₹514 per share, 10% below market price — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/hindustan-copper-ofs-government-to-sell-up-to-6-stake-at-rs-514-per-share-10-below-market-price-11787579800581.html
- Source: Govt to sell up to 6% stake in Hindustan Copper via OFS; floor price at 10% discount — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/govt-to-sell-up-to-6-stake-in-hindustan-copper-via-ofs-floor-price-at-10-discount/articleshow/133469842.cms
- Source: Positive investments in gold ETFs continue for the fifth week in a row — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/gold/positive-investments-in-gold-etfs-continue-for-the-fifth-week-in-a-row/article71384933.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.17), 2025-07-30 (d=0.3)

### [RED 5.75] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3209.00, z20 3.75, zc 2.81, resid-z 3.51 [unexplained], 1d 6.19%, |z20|=3.75
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.687 via dyn_muthootfin_ns, z 1.73, reacted); nifty_midcap_100 (rho 0.614 via dyn_muthootfin_ns, z 0.77, quiet); nifty_50 (rho 0.537 via dyn_muthootfin_ns, z -0.7, quiet); dyn_karurvysya_ns (rho 0.429 via dyn_muthootfin_ns, z 0.13, quiet); dyn_bharatcoal_ns (rho 0.425 via dyn_muthootfin_ns, z 1.67, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.614 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.537 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.59 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.687, z 1.73); nifty_midcap_100 (rho 0.614, z 0.77); nifty_50 (rho 0.537, z -0.7); dyn_karurvysya_ns (rho 0.429, z 0.13)
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 5.09] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 11.05, z20 5.09, zc 2.35, resid-z 3.05 [unexplained], 1d 8.12%, |z20|=5.09
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.401 via dyn_pcjeweller_ns, z 3.75, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.401, z 3.75)
- Historical analogues: 2026-07-10 (d=0.0), 2024-10-01 (d=0.19), 2026-01-07 (d=0.32)

### [AMBER 4.48] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.48, zc n/a, resid-z n/a [quiet], 1d 0.26%, 52-wk extreme (pct=100); 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.491 via midcap_largecap_ratio, z 0.77, quiet); dyn_fincables_ns (rho 0.37 via midcap_largecap_ratio, z 1.18, reacted); dyn_bharatcoal_ns (rho 0.356 via midcap_largecap_ratio, z 1.67, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.491, z 0.77); dyn_fincables_ns (rho 0.37, z 1.18); dyn_bharatcoal_ns (rho 0.356, z 1.67)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.09] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 88.50, z20 4.09, zc 3.54, resid-z 2.61 [unexplained], 1d 7.61%, |z20|=4.09
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.408 via dyn_idbi_ns, z 3.75, reacted); dyn_voltas_ns (rho 0.391 via dyn_idbi_ns, z -1.33, reacted); nifty_metal (rho 0.372 via dyn_idbi_ns, z 1.73, reacted); nifty_midcap_100 (rho 0.371 via dyn_idbi_ns, z 0.77, quiet); dyn_bharatcoal_ns (rho 0.36 via dyn_idbi_ns, z 1.67, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.408, z 3.75); dyn_voltas_ns (rho 0.391, z -1.33); nifty_metal (rho 0.372, z 1.73); nifty_midcap_100 (rho 0.371, z 0.77)
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

## Watchlist (below surfacing floor)
dyn_lenskart_ns ↑ (4.01), fx · 4 series ↑ (3.97), dyn_lth ↑ (3.84), dyn_cartrade_ns ↑ (3.69), dyn_icicigi_bo ↓ (3.29), usd_cny ↓ (3.24), rates · 2 series ↑ (3.24), cross-asset · 2 series ↑ (3.17), gold_silver_ratio ↑ (3.17), dyn_tech ↑ (2.92), tips_10y_real ↓ (2.88), dyn_indusindbk_bo ↑ (2.52)

## India macro
- nifty_50: 24219.0508 (1d -0.14%, z20 -0.70, flag none)
- nifty_midcap_100: 63816.3984 (1d 0.13%, z20 0.77, flag amber)
- usd_inr: 95.7400 (1d -0.03%, z20 0.66, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6350 (1d 0.26%, z20 1.48, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 80.4 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.7 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.4 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- INDIANB.NS (INDIAN BANK) score 76.0 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- BOND (PIMCO Active Bond Exchange-Tra) score 66.4 — "GERMAN FIN. MIN. KLINGBEIL: SURGE IN BOND YIELDS A RESULT OF TRUMP'S WAR"
- BAC (Bank of America Corporation) score 62.4 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- HDB (HDFC Bank Limited) score 59.2 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- IDBI.NS (IDBI BANK LIMITED) score 56.1 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.1 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.1 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- COIN (Coinbase Global, Inc.) score 48.1 — "Global oil prices above $90 a barrel ahead of Bessent’s ‘economic D-Day’ announcement on I"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.1 — "Paluck Technologies IPO: BSE SME declares IPO opening date, fixes price band at  ₹46 to  ₹"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.7 — "Paluck Technologies IPO: BSE SME declares IPO opening date, fixes price band at  ₹46 to  ₹"
- TECH (Bio-Techne Corp) score 43.6 — "Paluck Technologies IPO: BSE SME declares IPO opening date, fixes price band at  ₹46 to  ₹"
- OHI (Omega Healthcare Investors, In) score 33.6 — "‘Investors need to look beyond trailing returns’"
- LTH (Life Time Group Holdings, Inc.) score 30.7 — "It’s time to bet big on Nvidia’s stock, says this analyst who thinks the market has it all"
- CHKP (Check Point Software Technolog) score 25.7 — "IPO: Share price band  ₹300, GMP  ₹313 - Check last date to apply, allotment and listing d"
- JIOFIN.BO (Jio Financial Services Limited) score 18.7 — "Sebi drops proceedings against Max Financial, Axis Bank in Max Life deal case"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.5 — "Lalithaa Jewellery shares end with 24% listing gains, Horizon Ind ends below ₹60-IPO price"
- 301077.SZ (CHINASTARS) score 17.9 — "BESSENT PUTS IRAN’S TRADING PARTNERS ON NOTICE Treasury Secretary Scott Bessent is threate"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.2 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- MS (Morgan Stanley) score 12.2 — "Y Combinator sells Meesho shares worth Rs 970 crore in block deals; Morgan Stanley, Goldma"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.0 — "Shein IPO: Fast fashion retailer eyes $27 billion price tag in long-awaited Hong Kong list"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 11.1 — "Sebi drops proceedings against Max Financial, Axis Bank in Max Life deal case"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.4 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.6 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.2 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- VT (Vanguard Total World Stock Ind) score 8.8 — "This market shift resembles the post–World War II era — and bond yields could have room to"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.7 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.3 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- NVDA (NVIDIA Corporation) score 7.7 — "Wall Street stocks mostly fall as Iran tensions, Nvidia earnings in focus; Marvell and Mic"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.2 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- META (Meta) score 6.8 — "Stock market today: Sensex falls 170 points, Nifty 50 ends below 24,219; metal stocks shin"
- JEF (Jefferies Financial Group Inc.) score 5.5 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.2 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.8 — "Alibaba shares tumble as investors question whether AI spending splurge is justified"
- MRNA (Moderna, Inc.) score 4.6 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 1.0 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.2 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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