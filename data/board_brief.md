# Transmission Layer — board brief · 2026-09-16 22:55Z

data as of **2026-09-16** · 97 series · 19 red / 40 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.689, 5d in regime; vol-pct 0.555, breadth-off 0.824, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.55, corr60 -0.32, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.32, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.11, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.84, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.33, corr60 -0.08, last shift 2026-07-23. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.15, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.475, β 0.2327, p 0.0); driver zc -1.52 → expected -0.637%. Type hit-rate 0.823 (n=2057).
- Track record · residual_reversion: hit-rate **0.495** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2057) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.85] cross-asset · 15 series ↓
- dyn_ms [EQUITIES]: last 202.46, z20 -3.33, zc -1.00, resid-z 0.41 [quiet], 1d -1.85%, |z20|=3.33
- dow_jones [INDICES]: last 51477.73, z20 -3.08, zc -1.48, resid-z -2.81 [unexplained], 1d -1.18%, |z20|=3.08
- dyn_vt [EQUITIES]: last 157.43, z20 -2.84, zc -0.48, resid-z 0.26 [quiet], 1d -0.38%, |z20|=2.84
- sp500 [INDICES]: last 7553.33, z20 -2.73, zc -0.57, resid-z -0.73 [quiet], 1d -0.43%, |z20|=2.73
- tips_10y_real [RATES]: last 2.62, z20 2.48, zc 0.44, resid-z -0.10 [quiet], 1d 0.77%, |z20|=2.48; 1y-pct=100
- ust_10y [RATES]: last 5.00, z20 2.43, zc 0.61, resid-z 0.14 [quiet], 1d 0.60%, |z20|=2.43; 1y-pct=100
- ust_2y [RATES]: last 4.67, z20 2.32, zc 0.33, resid-z -0.22 [quiet], 1d 0.43%, |z20|=2.32; 1y-pct=100
- vix [INDICES]: last 17.71, z20 2.19, zc 0.37, resid-z n/a [quiet], 1d 2.97%, |z20|=2.19
- russell_2000 [INDICES]: last 2859.05, z20 -2.18, zc -0.34, resid-z -0.22 [quiet], 1d -0.39%, |z20|=2.18
- dyn_bond [EQUITIES]: last 88.53, z20 -2.06, zc -0.44, resid-z 0.95 [quiet], 1d -0.15%, |z20|=2.06; 1y-pct=0
- ust_30y [RATES]: last 5.36, z20 1.91, zc 0.48, resid-z 0.14 [quiet], 1d 0.37%, |z20|=1.91; 1y-pct=99
- nasdaq_100 [INDICES]: last 28953.02, z20 -1.84, zc 0.05, resid-z 0.37 [quiet], 1d 0.05%, |z20|=1.84
- stoxx_50 [INDICES]: last 6271.93, z20 -1.63, zc 0.64, resid-z 0.74 [quiet], 1d 0.57%, |z20|=1.63
- wti [COMMODITIES]: last 101.95, z20 1.60, zc -1.15, resid-z -1.41 [quiet], 1d -3.67%, 1-session move -3.67% ≥ 1.5%; |z20|=1.60
- brent [COMMODITIES]: last 105.52, z20 1.50, zc -1.01, resid-z -1.21 [quiet], 1d -2.97%, 1-session move -2.97% ≥ 1.5%; |z20|=1.50; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: cross-asset · 15 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.404 via ust_2y, z -1.69, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.58 vs dyn_ms, historically leads by 4d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.579 vs stoxx_50, historically leads by 2d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.56 vs dyn_vt
- **India receivers**: midcap_largecap_ratio (rho -0.404, z -1.69)
- Source: Oil Above $100 Pushes U.S. Fuel Prices to New Records — OilPrice, 2026-09-16. https://oilprice.com/Energy/Energy-General/Oil-Above-100-Pushes-US-Fuel-Prices-to-New-Records.html
- Source: Shale Oil Now Makes Up 72% of Argentina's Crude Output, Data Shows — OilPrice, 2026-09-16. https://oilprice.com/Energy/Crude-Oil/Shale-Oil-Now-Makes-Up-72-of-Argentinas-Crude-Output-Data-Shows.html
- Source: Why optical stocks Lumentum and Coherent were the day’s biggest S&P 500 gainers — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/why-optical-stocks-lumentum-and-coherent-were-the-days-biggest-gainers-051af440?mod=mw_rss_topstories

### [RED 6.91] dxy ↑
- dxy [FX]: last 100.34, z20 3.91, zc 2.09, resid-z 0.53 [moved], 1d 0.69%, 20d range extreme; |z20|=3.91
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 6.78] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4311.00, z20 -1.95, zc -0.43, resid-z -0.02 [quiet], 1d -0.50%, |z20|=1.95; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 63.47, z20 -1.63, zc 0.15, resid-z 0.89 [quiet], 1d 0.38%, |z20|=1.63; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.92, z20 0.46, zc n/a, resid-z n/a [quiet], 1d -0.88%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.52 vs comex_gold, historically leads by 1d
- Source: Gold Swings Lower as Fed Tilts Hawkish After Raising Rates — Mint Markets, 2026-09-16. https://www.livemint.com/market/gold-swings-lower-as-fed-tilts-hawkish-after-raising-rates-11789590473862.html
- Source: Gold falls more than 1% after Fed hikes interest rates — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/us-stocks/news/gold-falls-more-than-1-after-fed-hikes-interest-rates/articleshow/134296279.cms
- Source: US Fed rate hike impact on gold: FOMC outcome on yellow metal decoded — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/us-fed-rate-hike-impact-on-gold-fomc-outcome-on-yellow-metal-decoded-11789580961438.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.61] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 60879.15, z20 -2.95, zc 0.01, resid-z -0.60 [quiet], 1d 0.01%, |z20|=2.95
- india_vix [INDICES]: last 13.14, z20 2.79, zc -0.38, resid-z n/a [quiet], 1d -2.16%, |z20|=2.79
- dyn_jiofin_bo [EQUITIES]: last 225.00, z20 -2.40, zc -0.32, resid-z -1.18 [quiet], 1d -0.44%, |z20|=2.40; 1y-pct=0
- nifty_50 [INDICES]: last 23217.60, z20 -2.11, zc 0.78, resid-z 0.36 [quiet], 1d 0.43%, |z20|=2.11
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.617 via nifty_50, z -0.92, quiet); dyn_indianb_ns (rho 0.559 via nifty_midcap_100, z -2.16, reacted); nifty_it (rho 0.53 via nifty_50, z -1.64, reacted); dyn_techm_ns (rho 0.516 via nifty_50, z -0.8, quiet); midcap_largecap_ratio (rho -0.437 via nifty_50, z -1.69, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.617 vs nifty_50, historically leads by 3d
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.516 vs nifty_50, historically leads by 3d
- **India receivers**: nifty_fmcg (rho 0.617, z -0.92); dyn_indianb_ns (rho 0.559, z -2.16); nifty_it (rho 0.53, z -1.64); dyn_techm_ns (rho 0.516, z -0.8)
- Source: US Fed rate hike impact on Indian stock market - Sensex, Nifty, Bank Nifty, Nifty IT — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/us-fed-rate-hike-impact-on-indian-stock-market-sensex-nifty-bank-nifty-nifty-it-11789581995860.html
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Thu | Kospi, Taiwan Index, Nikkei cues to watch | 17 Sept — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-thu-kospi-taiwan-index-nikkei-cues-to-watch-17-sept-11789567603146.html
- Source: Fed watch freezes Dalal Street; Nifty ekes out modest gains after brutal sell-off — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/fed-watch-freezes-dalal-street-nifty-ekes-out-modest-gains-after-brutal-sell-off/article71472309.ece
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 6.58] fx · 4 series ↓
- usd_mxn [FX]: last 17.24, z20 4.92, zc 1.60, resid-z 1.56 [unexplained], 1d 0.70%, |z20|=4.92
- eur_usd [FX]: last 1.15, z20 -4.17, zc -2.23, resid-z -1.65 [unexplained], 1d -0.69%, |z20|=4.17
- gbp_usd [FX]: last 1.34, z20 -3.51, zc -2.30, resid-z -2.26 [unexplained], 1d -0.89%, |z20|=3.51
- aud_usd [FX]: last 0.71, z20 -2.21, zc -1.45, resid-z -1.51 [unexplained], 1d -0.69%, |z20|=2.21
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.424 via aud_usd, z -1.37, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.603 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_muthootfin_ns (rho 0.424, z -1.37)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.34] usd_inr ↑
- usd_inr [FX]: last 95.94, z20 1.34, zc 0.19, resid-z 0.42 [quiet], 1d 0.11%, 20d range extreme; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Rupee languishes at six-week low ahead of Fed outcome, RBI limits losses — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/forex/rupee-languishes-at-six-week-low-ahead-of-fed-outcome-rbi-limits-losses/articleshow/134284941.cms
- Source: Rupee falls 3 paise to 95.91 against US dollar in early trade — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/forex/rupee-falls-3-paise-to-9591-against-us-dollar-in-early-trade/article71471039.ece
- Source: Rupee expected to stay under pressure with likely Fed rate hike adding to strain from high oil prices — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/forex/rupee-expected-to-stay-under-pressure-with-likely-fed-rate-hike-adding-to-strain-from-high-oil-prices/article71470982.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 5.97] dyn_bac ↓
- dyn_bac [EQUITIES]: last 57.89, z20 -3.97, zc -1.52, resid-z -0.02 [moved], 1d -2.74%, |z20|=3.97
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho 0.382 via dyn_bac, z -0.33, quiet)
- **India receivers**: eur_inr (rho 0.382, z -0.33)
- Source: 5% Treasury yields mean America’s debt bill just got a lot bigger — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/5-treasury-yields-mean-americas-debt-bill-just-got-a-lot-bigger-8a5702b0?mod=mw_rss_topstories
- Source: WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expects the Federal Reserve to raise rates in September, according to a WSJ survey. Most forecast 50 basis points of total tightening in 2026, while Bank of America, Deutsche Bank and RBC see 75bps. Market angle: exp — DeItaone, 2026-09-15. https://t.me/walter_bloomberg/35811
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 5.44] dyn_jef ↓
- dyn_jef [EQUITIES]: last 47.33, z20 -3.44, zc -1.12, resid-z -0.71 [quiet], 1d -3.07%, |z20|=3.44
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Solar Industries’ defence share may fall to 22-25% by FY30 after Omnia deal: Jefferies — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-defence-share-may-fall-to-22-25-by-fy30-after-omnia-deal-jefferies/articleshow/134280191.cms
- Source: Solar Industries shares plunge 17% in 2 days. Why Jefferies, Nuvama still see up to 46% upside — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-shares-plunge-17-in-2-days-why-jefferies-nuvama-still-see-up-to-46-upside/articleshow/134279133.cms
- Source: Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estimates after new UPI charges — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-jump-7-as-jefferies-other-brokerages-raise-target-prices-and-earnings-estimates-after-new-upi-charges/articleshow/134278132.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (5.27), dyn_tatatech_ns ↓ (4.37), dyn_stylebaaza_ns ↓ (4.13), hy_oas ↑ (4.05), dyn_icicigi_bo ↓ (3.7), nikkei_225 ↓ (3.57), dyn_indusindbk_bo ↓ (3.45), soybeans ↑ (3.42), dyn_hdb ↓ (3.23), usd_cny ↓ (2.92), commodities · 2 series ↑ (2.49), dyn_lenskart_ns ↑ (2.4)

## India macro
- nifty_50: 23217.5996 (1d 0.43%, z20 -2.11, flag amber)
- nifty_midcap_100: 60879.1484 (1d 0.01%, z20 -2.95, flag red)
- usd_inr: 95.9400 (1d 0.11%, z20 1.34, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6221 (1d -0.42%, z20 -1.69, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 64.5 — "FED: WHAT WALL STREET EXPECTS FROM WARSH TODAY Major banks are focused on how Kevin Warsh "
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.1 — "US Fed rate hike impact on Indian economy: FOMC outcome effect decoded"
- COALINDIA.NS (COAL INDIA LTD) score 62.7 — "US Fed rate hike impact on Indian economy: FOMC outcome effect decoded"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 62.0 — "US Fed rate hike impact on Indian economy: FOMC outcome effect decoded"
- COIN (Coinbase Global, Inc.) score 52.9 — "Export Constraints Curb Kazakhstan’s Ability to Offset the Global Oil Shortage"
- BAC (Bank of America Corporation) score 52.1 — "FED: WHAT WALL STREET EXPECTS FROM WARSH TODAY Major banks are focused on how Kevin Warsh "
- OHI (Omega Healthcare Investors, In) score 47.0 — "NSE IPO all set to open; co raises Rs 6,746 crore from anchor investors including LIC, Gol"
- HDB (HDFC Bank Limited) score 46.1 — "FED: WHAT WALL STREET EXPECTS FROM WARSH TODAY Major banks are focused on how Kevin Warsh "
- BOND (PIMCO Active Bond Exchange-Tra) score 43.4 — "Fed rate hike fails to calm troubled markets as Dow falls 600 points. Expect more sharp sw"
- IDBI.NS (IDBI BANK LIMITED) score 42.6 — "FED: WHAT WALL STREET EXPECTS FROM WARSH TODAY Major banks are focused on how Kevin Warsh "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.6 — "FED: WHAT WALL STREET EXPECTS FROM WARSH TODAY Major banks are focused on how Kevin Warsh "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.6 — "FED: WHAT WALL STREET EXPECTS FROM WARSH TODAY Major banks are focused on how Kevin Warsh "
- CHKP (Check Point Software Technolog) score 35.9 — "Fortis Healthcare shares outlook by Nomura: Rating neutral and target price remains  ₹1030"
- TECHM.NS (TECH MAHINDRA LIMITED) score 30.4 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.4 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- TECH (Bio-Techne Corp) score 30.4 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- LTH (Life Time Group Holdings, Inc.) score 25.8 — "FED: RATE HIKE WILL SUPPORT `TIMELIER' RETURN TO 2% INFLATION"
- SEPN (Septerna, Inc.) score 25.3 — "Stock Market prediction tomorrow: Sensex, Nifty outlook for Thu | Kospi, Taiwan Index, Nik"
- 301077.SZ (CHINASTARS) score 24.8 — "China Could Curb Fuel Exports as Diesel and Gasoline Stocks Sink"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.0 — "MARKETS MAY BE PRICING TOO MANY RATE HIKES Markets now expect four 25bp Fed hikes over the"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.3 — "ATLANTA FED GDPNOW SURGES ABOVE 5% The Atlanta Fed’s GDPNow estimate for Q3 growth jumped "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.3 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.3 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.2 — "SAUDI PIPELINE COULD RESTORE HALF ITS CAPACITY WITHIN DAYS Saudi Arabia is working to rest"
- JIOFIN.BO (Jio Financial Services Limited) score 9.2 — "JM Financial sees up to 28% upside in Dr Reddy’s and Aurobindo Pharma. Should you buy?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.7 — "5% Treasury yields mean America’s debt bill just got a lot bigger"
- MS (Morgan Stanley) score 8.7 — "LIC, Morgan Stanley, Goldman Sachs among anchor investors as NSE raises Rs 6,746 crore ahe"
- NVDA (NVIDIA Corporation) score 8.2 — "BESSENT: TRUMP COMPLETELY ALIGNED WITH NVIDIA'S JENSEN HUANG"
- VT (Vanguard Total World Stock Ind) score 8.0 — "IRANIAN ATTACK HITS U.S.-CONTRACTED VESSEL NEAR HORMUZ An Iranian drone and missile attack"
- JEF (Jefferies Financial Group Inc.) score 7.2 — "Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estim"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.9 — "GRT Jewellers launches ₹431 crore open offer for remaining TBZ stake"
- META (Meta) score 6.8 — "US Fed rate hike impact on gold: FOMC outcome on yellow metal decoded"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 6.3 — "Borosil Renewables' entry into the solar rooftop sector a significant positive, shares may"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.8 — "Indonesia's new finance minister faces an uphill battle on fiscal credibility"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.4 — "Suzlon Energy, Adani Power share prices fall: Check 1-week, 1-year and 5-year returns"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.5 — "ICICI Prudential MF, Kotak MF top buyers in SS Retail's Rs 146 crore anchor round before I"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.0 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.5 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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