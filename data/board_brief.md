# Transmission Layer — board brief · 2026-08-24 21:51Z

data as of **2026-08-24** · 98 series · 12 red / 32 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.313, 1d in regime; vol-pct 0.274, breadth-off 0.353, Markov P(high-vol) 0.014)
- [WEAK] **safe_haven_gold** — corr20 -0.24, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.75, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.17, corr60 0.4, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 -0.1, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.21, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.28, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.002288413662045352)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1113) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2455) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.32] commodities · 2 series ↑
- corn [COMMODITIES]: last 515.00, z20 4.49, zc 5.08, resid-z 4.06 [unexplained], 1d 6.46%, |z20|=4.49; 1y-pct=100
- wheat [COMMODITIES]: last 700.75, z20 2.70, zc 1.70, resid-z 1.51 [unexplained], 1d 2.82%, |z20|=2.70; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 7.27] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 79008.11, z20 3.61, zc 0.19, resid-z 0.79 [quiet], 1d 0.86%, |z20|=3.61
- eth_usd [CRYPTO]: last 2486.48, z20 2.98, zc -0.23, resid-z 0.15 [quiet], 1d -1.15%, |z20|=2.98
- dyn_mrna [EQUITIES]: last 138.89, z20 2.77, zc -0.33, resid-z 0.89 [quiet], 1d -4.30%, |z20|=2.77; 1y-pct=99
- dyn_coin [EQUITIES]: last 179.49, z20 2.22, zc -0.69, resid-z 2.03 [unexplained], 1d -3.76%, |z20|=2.22
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.57).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Bitcoin has beaten stocks and gold over six months. Now it’s closing in on $80,000. — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/bitcoin-has-beaten-stocks-and-gold-over-six-months-now-its-closing-in-on-80-000-b8aa48f9?mod=mw_rss_topstories
- Source: Global oil prices above $90 a barrel ahead of Bessent’s ‘economic D-Day’ announcement on Iran — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/oil-trades-lower-even-as-bessent-promises-economic-d-day-announcement-on-iran-a90d862e?mod=mw_rss_topstories
- Source: Global Markets: Fast-fashion giant Shein shrinks value to up to $27 billion in Hong Kong IPO — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-fast-fashion-giant-shein-shrinks-value-to-up-to-27-billion-in-hong-kong-ipo/articleshow/133466240.cms
- Historical analogues: 2025-08-13 (d=0.57), 2025-05-09 (d=1.49), 2024-11-21 (d=1.59)

### [AMBER 6.86] commodities · 2 series ↑
- brent [COMMODITIES]: last 91.99, z20 1.03, zc -1.24, resid-z -0.83 [quiet], 1d -2.54%, 1-session move -2.54% ≥ 1.5%
- wti [COMMODITIES]: last 84.98, z20 0.81, zc -1.06, resid-z -0.68 [quiet], 1d -2.39%, 1-session move -2.39% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.581 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.687 vs brent
- Source: Houthis Target Saudi Oil Tanker in Red Sea Missile and Drone Attack — OilPrice, 2026-08-24. https://oilprice.com/Geopolitics/Middle-East/Houthis-Target-Saudi-Oil-Tanker-in-Red-Sea-Missile-and-Drone-Attack.html
- Source: Bessent’s sweeping sanctions against Iran send oil prices to their biggest drop in 3 weeks, while fueling hopes of de-escalation — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/oil-trades-lower-even-as-bessent-promises-economic-d-day-announcement-on-iran-a90d862e?mod=mw_rss_topstories
- Source: Norway Warns Oil and Gas Output Could Collapse After 2030 — OilPrice, 2026-08-24. https://oilprice.com/Energy/Crude-Oil/Norway-Warns-Oil-and-Gas-Output-Could-Collapse-After-2030.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.7] cross-asset · 4 series ↑
- comex_gold [COMMODITIES]: last 4710.00, z20 2.41, zc 1.04, resid-z 1.19 [quiet], 1d 1.86%, |z20|=2.41; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 68.96, z20 1.71, zc -0.28, resid-z -2.31 [unexplained], 1d -0.72%, |z20|=1.71; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.61, z20 0.69, zc 0.18, resid-z 0.65 [quiet], 1d 0.40%, 1y-pct=97; co-occur[metal_copper] suppressed: channel WEAK
- gold_silver_ratio [DERIVED]: last 68.30, z20 -0.04, zc n/a, resid-z n/a [quiet], 1d 2.60%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.483 via comex_silver, z 1.73, reacted); dyn_stylebaaza_ns (rho -0.425 via gold_silver_ratio, z 1.14, reacted)
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.56 vs comex_silver, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.537 vs comex_copper, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.522 vs comex_gold, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.501 vs comex_copper, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.483, z 1.73); dyn_stylebaaza_ns (rho -0.425, z 1.14)
- Source: Bitcoin has beaten stocks and gold over six months. Now it’s closing in on $80,000. — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/bitcoin-has-beaten-stocks-and-gold-over-six-months-now-its-closing-in-on-80-000-b8aa48f9?mod=mw_rss_topstories
- Source: Gold rallies past three-month high as Treasury buyback and weak dollar boost demand — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-rallies-past-three-month-high-as-treasury-buyback-and-weak-dollar-boost-demand/articleshow/133473806.cms
- Source: Hindustan Copper OFS: Government to sell up to 6% stake at  ₹514 per share, 10% below market price — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/hindustan-copper-ofs-government-to-sell-up-to-6-stake-at-rs-514-per-share-10-below-market-price-11787579800581.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 5.75] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3209.00, z20 3.75, zc 2.81, resid-z 3.52 [unexplained], 1d 6.19%, |z20|=3.75
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.687 via dyn_muthootfin_ns, z 1.73, reacted); nifty_midcap_100 (rho 0.614 via dyn_muthootfin_ns, z 0.77, quiet); nifty_50 (rho 0.537 via dyn_muthootfin_ns, z -0.7, quiet); dyn_karurvysya_ns (rho 0.429 via dyn_muthootfin_ns, z 0.13, quiet); dyn_bharatcoal_ns (rho 0.425 via dyn_muthootfin_ns, z 1.67, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.614 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.537 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.579 vs dyn_muthootfin_ns
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

### [AMBER 4.63] rates · 2 series ↑
- ust_10y [RATES]: last 4.74, z20 1.79, zc 1.07, resid-z 1.37 [quiet], 1d 1.07%, |z20|=1.79; 1y-pct=99
- ust_30y [RATES]: last 5.27, z20 1.13, zc 0.90, resid-z 1.12 [quiet], 1d 0.76%, 1y-pct=98
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.765 vs ust_10y, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.951 vs ust_10y
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.852 vs ust_10y
- Watch next: wti (co-move) — not yet - watch; rho 0.554 vs ust_10y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.509 vs ust_10y
- Source: GERMAN FIN. MIN. KLINGBEIL: SURGE IN BOND YIELDS A RESULT OF TRUMP'S WAR — DeItaone, 2026-08-24. https://t.me/walter_bloomberg/34951
- Source: US stock market today: Wall Street futures slip as tech rout, Iran tensions and bond yields weigh — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-slip-as-tech-rout-iran-tensions-and-bond-yields-weigh-11787385929496.html
- Source: This market shift resembles the post–World War II era — and bond yields could have room to go higher, says Morgan Stanley — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/the-post-world-war-ii-market-shift-is-here-and-bond-yields-could-have-higher-to-go-says-morgan-stanley-9381532c?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.11), 2025-05-16 (d=0.19)

### [AMBER 4.48] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.48, zc n/a, resid-z n/a [quiet], 1d 0.26%, 52-wk extreme (pct=100); 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.491 via midcap_largecap_ratio, z 0.77, quiet); dyn_fincables_ns (rho 0.37 via midcap_largecap_ratio, z 1.18, reacted); dyn_bharatcoal_ns (rho 0.356 via midcap_largecap_ratio, z 1.67, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.491, z 0.77); dyn_fincables_ns (rho 0.37, z 1.18); dyn_bharatcoal_ns (rho 0.356, z 1.67)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_idbi_ns ↑ (4.09), dyn_lenskart_ns ↑ (4.01), dyn_cartrade_ns ↑ (3.69), dyn_lth ↑ (3.43), dyn_tech ↑ (3.4), dyn_icicigi_bo ↓ (3.29), cross-asset · 2 series ↑ (3.15), fx · 2 series ↑ (3.13), usd_cny ↓ (3.06), fx · 2 series ↑ (2.68), dyn_indusindbk_bo ↑ (2.52), ftse_100 ↑ (2.5)

## India macro
- nifty_50: 24219.0508 (1d -0.14%, z20 -0.70, flag none)
- nifty_midcap_100: 63816.3984 (1d 0.13%, z20 0.77, flag amber)
- usd_inr: 95.7350 (1d -0.04%, z20 0.65, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6350 (1d 0.26%, z20 1.48, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 76.7 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- INDIANB.NS (INDIAN BANK) score 75.4 — "SEC SUBPOENAS BANKS FOR DETAILS ON SITUATIONAL AWARENESS: NYT"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.0 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.8 — "INDIA FACES WEAKEST MONSOON SINCE 2009 India is likely to record its lowest monsoon rainfa"
- BAC (Bank of America Corporation) score 65.4 — "SEC SUBPOENAS BANKS FOR DETAILS ON SITUATIONAL AWARENESS: NYT"
- BOND (PIMCO Active Bond Exchange-Tra) score 64.3 — "BESSENT: WE HAVEN'T BOUGHT A SINGLE BOND YET, NEXT OPERATION IS SEPT 9"
- HDB (HDFC Bank Limited) score 59.4 — "SEC SUBPOENAS BANKS FOR DETAILS ON SITUATIONAL AWARENESS: NYT"
- IDBI.NS (IDBI BANK LIMITED) score 56.4 — "SEC SUBPOENAS BANKS FOR DETAILS ON SITUATIONAL AWARENESS: NYT"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.4 — "SEC SUBPOENAS BANKS FOR DETAILS ON SITUATIONAL AWARENESS: NYT"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.4 — "SEC SUBPOENAS BANKS FOR DETAILS ON SITUATIONAL AWARENESS: NYT"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.0 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500, Nasdaq decline "
- COIN (Coinbase Global, Inc.) score 45.9 — "Global oil prices above $90 a barrel ahead of Bessent’s ‘economic D-Day’ announcement on I"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.6 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500, Nasdaq decline "
- TECH (Bio-Techne Corp) score 44.5 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500, Nasdaq decline "
- OHI (Omega Healthcare Investors, In) score 32.1 — "‘Investors need to look beyond trailing returns’"
- LTH (Life Time Group Holdings, Inc.) score 31.3 — "BESSENT: WILL NOT SET SPECIFIC TIMELINES FOR CUTTING IRAN TIES, WE DON'T HAVE INFINITE PAT"
- CHKP (Check Point Software Technolog) score 24.5 — "IPO: Share price band  ₹300, GMP  ₹313 - Check last date to apply, allotment and listing d"
- JIOFIN.BO (Jio Financial Services Limited) score 21.8 — "BESSENT: WE ARE LAUNCHING ECONOMIC ONSLAUGHT AGAINST IRAN'S FINANCIAL CONNECTIONS AROUND G"
- 301077.SZ (CHINASTARS) score 20.9 — "BESSENT ON CHINA-IRAN: NO ONE IS ABOVE REACH OF US SANCTIONS"
- PCJEWELLER.NS (PC JEWELLER LTD) score 17.6 — "Lalithaa Jewellery shares end with 24% listing gains, Horizon Ind ends below ₹60-IPO price"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.4 — "ONTARIO PREMIER FORD: NEED TO RESTRICT ENERGY, POTASH, ELECTRICITY SHIPMENTS TO U.S."
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.6 — "BESSENT: WE ARE LAUNCHING ECONOMIC ONSLAUGHT AGAINST IRAN'S FINANCIAL CONNECTIONS AROUND G"
- NVDA (NVIDIA Corporation) score 12.2 — "NVDA - NVIDIA DIPS IN VOLUME SPIKE, LAST OFF 3.2%"
- MS (Morgan Stanley) score 11.6 — "Y Combinator sells Meesho shares worth Rs 970 crore in block deals; Morgan Stanley, Goldma"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.4 — "Shein IPO: Fast fashion retailer eyes $27 billion price tag in long-awaited Hong Kong list"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.9 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- VT (Vanguard Total World Stock Ind) score 9.4 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.2 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.8 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.3 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.9 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.8 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- META (Meta) score 6.4 — "Stock market today: Sensex falls 170 points, Nifty 50 ends below 24,219; metal stocks shin"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.5 — "20 MILLION TO SHIP OIL THROUGH HORMUZ Shipping a supertanker through the Strait of Hormuz "
- JEF (Jefferies Financial Group Inc.) score 5.2 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.0 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- MRNA (Moderna, Inc.) score 4.4 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 1.0 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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