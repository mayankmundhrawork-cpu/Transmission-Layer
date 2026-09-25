# Transmission Layer — board brief · 2026-09-25 15:14Z

data as of **2026-09-25** · 97 series · 7 red / 35 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.547, 6d in regime; vol-pct 0.38, breadth-off 0.714, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.24, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.02, corr60 0.12, last shift 2026-08-12. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-08-05. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.4, corr60 0.21, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.474, β 0.2528, p 0.0); driver zc 3.12 → expected 0.765%. Type hit-rate 0.831 (n=2224).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.359, β -0.1201, p 0.0); driver zc 2.28 → expected -0.357%. Type hit-rate 0.831 (n=2224).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.273, β -0.1104, p 0.0); driver zc 3.12 → expected -0.334%. Type hit-rate 0.831 (n=2224).
- Track record · residual_reversion: hit-rate **0.496** (n=1102) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.831** (n=2224) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.17] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 87.37, z20 -2.33, zc -0.56, resid-z -0.20 [quiet], 1d -0.23%, |z20|=2.33; 1y-pct=0
- tips_10y_real [RATES]: last 2.76, z20 2.24, zc 2.66, resid-z 2.44 [unexplained], 1d 4.94%, 1d move +13.0bps ≥ 5bps; |z20|=2.24; 1y-pct=100
- ust_10y [RATES]: last 5.11, z20 2.13, zc 3.12, resid-z 2.67 [unexplained], 1d 3.02%, |z20|=2.13; 1y-pct=100
- ust_30y [RATES]: last 5.40, z20 2.07, zc 2.73, resid-z 2.34 [unexplained], 1d 2.08%, |z20|=2.07; 1y-pct=100
- ust_2y [RATES]: last 4.85, z20 1.87, zc 2.28, resid-z 1.58 [unexplained], 1d 2.97%, |z20|=1.87; 1y-pct=100
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.6 vs dyn_bond, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.517 vs dyn_bond, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.592 vs dyn_bond
- Watch next: sp500 (co-move) — not yet - watch; rho 0.541 vs dyn_bond
- Source: Why investors aren’t buying yet another attempt by the Treasury Department to calm the rattled bond market — MarketWatch Top, 2026-09-25. https://www.marketwatch.com/story/why-investors-arent-buying-yet-another-attempt-by-the-treasury-to-calm-the-rattled-bond-market-b168cac3?mod=mw_rss_topstories
- Source: Bitcoin trades around $84,000 after profit booking as rising US Treasury yields pressure crypto markets — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-trades-around-84000-after-profit-booking-as-rising-us-treasury-yields-pressure-crypto-markets/articleshow/134484052.cms
- Source: Japanese investors step up domestic bond purchases as foreign demand drops: JSDA data — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/news/japanese-investors-step-up-domestic-bond-purchases-as-foreign-demand-drops-jsda-data/articleshow/134483644.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.64] fx · 4 series ↓
- usd_mxn [FX]: last 17.73, z20 3.98, zc 1.62, resid-z 2.06 [unexplained], 1d 1.05%, |z20|=3.98
- aud_usd [FX]: last 0.70, z20 -2.69, zc -0.15, resid-z -0.07 [quiet], 1d -0.13%, |z20|=2.69
- gbp_usd [FX]: last 1.32, z20 -2.63, zc -0.10, resid-z -0.12 [quiet], 1d -0.04%, |z20|=2.63
- eur_usd [FX]: last 1.14, z20 -2.09, zc 0.47, resid-z 0.78 [quiet], 1d 0.16%, |z20|=2.09; 1y-pct=4
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.493 via usd_mxn, z -4.48, reacted); dyn_icicigi_bo (rho -0.493 via gbp_usd, z 1.06, reacted); dyn_muthootfin_ns (rho 0.465 via aud_usd, z -0.33, quiet); dyn_inoxindia_ns (rho 0.433 via aud_usd, z 0.13, quiet); nifty_50 (rho 0.388 via eur_usd, z -1.34, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.534 vs aud_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.402 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_policybzr_ns (rho -0.493, z -4.48); dyn_icicigi_bo (rho -0.493, z 1.06); dyn_muthootfin_ns (rho 0.465, z -0.33); dyn_inoxindia_ns (rho 0.433, z 0.13)
- Source: Philip R. Lane: The Outlook for the Euro Area Economy — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260923_1~ac21bf46e3.en.pdf
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.48] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 1166.00, z20 -4.48, zc -0.12, resid-z -1.17 [quiet], 1d -3.41%, |z20|=4.48; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.601 via dyn_policybzr_ns, z -1.66, reacted); nifty_50 (rho 0.477 via dyn_policybzr_ns, z -1.34, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.711 vs dyn_policybzr_ns
- **India receivers**: nifty_midcap_100 (rho 0.601, z -1.66); nifty_50 (rho 0.477, z -1.34)
- Source: How to trade PB Fintech shares after falling 12% from day’s high? This technical analyst explains — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/news/how-to-trade-pb-fintech-shares-after-falling-12-from-days-high-this-technical-analyst-explains/articleshow/134477427.cms
- Source: PB Fintech's 36% bloodbath rattles market, but Jefferies stays bullish. What does it see in Policybazaar parent? — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/news/pb-fintechs-36-bloodbath-rattles-market-but-jefferies-stays-bullish-what-does-it-see-in-policybazaar-parent/articleshow/134475050.cms
- Source: PB Fintech shares slump 40% in two sessions| What Jefferies, Morgan Stanley, BofA say on the stock — Mint Markets, 2026-09-25. https://www.livemint.com/market/stock-market-news/pb-fintech-shares-slump-40-in-two-sessions-what-jefferies-morgan-stanley-bofa-say-on-the-stock-11790308344209.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [AMBER 5.16] brent ↓
- brent [COMMODITIES]: last 99.55, z20 -0.16, zc -2.32, resid-z -2.68 [unexplained], 1d -6.61%, 1-session move -6.61% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.895 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.553 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.605 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.556 vs brent
- Source: Beijing's Iran Oil Trade Draws Fresh Criticism From Capitol Hill — OilPrice, 2026-09-25. https://oilprice.com/Geopolitics/International/Beijings-Iran-Oil-Trade-Draws-Fresh-Criticism-From-Capitol-Hill.html
- Source: The options market is sending a contrarian signal about oil prices — MarketWatch Top, 2026-09-25. https://www.marketwatch.com/story/the-options-market-is-sending-a-contrarian-signal-about-oil-prices-a8812210?mod=mw_rss_topstories
- Source: US stocks trade higher as AI enthusiasm eases worries over higher oil prices, yields — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-open-higher-as-ai-enthusiasm-eases-worries-over-higher-oil-prices-yields/articleshow/134486867.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [RED 4.72] dyn_indusindbk_bo ↓
- dyn_indusindbk_bo [EQUITIES]: last 912.50, z20 -2.72, zc -0.27, resid-z -1.13 [quiet], 1d -0.84%, |z20|=2.72
- **Mechanism**: dyn_indusindbk_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.459 via dyn_indusindbk_bo, z -1.66, reacted); nifty_50 (rho 0.421 via dyn_indusindbk_bo, z -1.34, reacted); nifty_metal (rho 0.374 via dyn_indusindbk_bo, z -0.21, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.459, z -1.66); nifty_50 (rho 0.421, z -1.34); nifty_metal (rho 0.374, z -0.21)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank News — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-today-live-25-sep-2026/liveblog/134474146.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

### [AMBER 4.5] natgas ↑
- natgas [COMMODITIES]: last 3.18, z20 2.50, zc -0.75, resid-z -1.39 [quiet], 1d -3.64%, |z20|=2.50
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.426 via natgas, z -4.48, reacted)
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.145 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.093 vs natgas, historically leads by 4d
- **India receivers**: dyn_policybzr_ns (rho -0.426, z -4.48)
- Source: Henry Hub natural gas prices this summer were 6% lower than last summer — EIA Today in Energy, 2026-09-25. https://www.eia.gov/todayinenergy/detail.php?id=68204
- Source: U.S. to Back Argentina’s First LNG Export Project With $6 Billion Loan — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/US-to-Back-Argentinas-First-LNG-Export-Project-With-6-Billion-Loan.html
- Source: Southeast Asia Keeps Building Gas Plants Despite Hormuz LNG Shock — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Southeast-Asia-Keeps-Building-Gas-Plants-Despite-Hormuz-LNG-Shock.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.19] dyn_ms ↓
- dyn_ms [EQUITIES]: last 194.73, z20 -2.19, zc -0.45, resid-z 0.11 [quiet], 1d -0.81%, |z20|=2.19
- **Mechanism**: dyn_ms ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.74 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.718 vs dyn_ms, historically leads by 4d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.608 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.585 vs dyn_ms, historically leads by 4d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.552 vs dyn_ms
- Source: ‘We were wrong.’ Why Morgan Stanley changed its tune on the U.S. dollar — and what it expects now. — MarketWatch Top, 2026-09-25. https://www.marketwatch.com/story/we-were-wrong-why-morgan-stanley-changed-its-tune-on-the-u-s-dollar-and-what-it-expects-now-7826fb96?mod=mw_rss_topstories
- Source: PB Fintech shares slump 40% in two sessions| What Jefferies, Morgan Stanley, BofA say on the stock — Mint Markets, 2026-09-25. https://www.livemint.com/market/stock-market-news/pb-fintech-shares-slump-40-in-two-sessions-what-jefferies-morgan-stanley-bofa-say-on-the-stock-11790308344209.html
- Source: Here’s how to position your portfolio for the next AI wave, according to Morgan Stanley — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/heres-how-to-position-your-portfolio-for-the-next-ai-wave-according-to-morgan-stanley-ac8f8a4a?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-11 (d=0.04), 2025-08-13 (d=0.09)

### [AMBER 3.97] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 66.70, z20 -0.97, zc n/a, resid-z n/a [quiet], 1d -1.52%, GSR<75 (extreme low)
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.845 vs gold_silver_ratio
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
nasdaq_100 ↑ (3.83), hang_seng ↓ (3.8), dyn_tech ↑ (3.72), dyn_meta ↑ (3.69), comex_gold ↓ (3.58), dyn_jiofin_bo ↓ (3.39), hy_oas ↑ (3.38), comex_copper ↑ (3.33), dyn_4417_t ↑ (3.31), dyn_voltas_ns ↓ (3.2), usd_brl ↑ (2.49), dyn_hdb ↑ (2.22)

## India macro
- nifty_50: 23140.5000 (1d 0.34%, z20 -1.34, flag none)
- nifty_midcap_100: 60901.9492 (1d -0.15%, z20 -1.66, flag amber)
- usd_inr: 95.8020 (1d 0.06%, z20 0.87, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6318 (1d -0.48%, z20 -1.37, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 90.6 — "Engineers India among 7 stocks hitting 52-week highs; shares rallied up to 25% in a month"
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.4 — "Engineers India among 7 stocks hitting 52-week highs; shares rallied up to 25% in a month"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.0 — "Engineers India among 7 stocks hitting 52-week highs; shares rallied up to 25% in a month"
- INDIANB.NS (INDIAN BANK) score 61.9 — "Why Japan’s markets flipped the usual script after central bank rate hike"
- COIN (Coinbase Global, Inc.) score 56.5 — "Global Market: VLCC rates hit record as Saudi crude flows jump"
- OHI (Omega Healthcare Investors, In) score 54.4 — "Japanese investors step up domestic bond purchases as foreign demand drops: JSDA data"
- HDB (HDFC Bank Limited) score 48.7 — "Why Japan’s markets flipped the usual script after central bank rate hike"
- BAC (Bank of America Corporation) score 46.6 — "Why Japan’s markets flipped the usual script after central bank rate hike"
- CHKP (Check Point Software Technolog) score 46.0 — "Upcoming dividend stocks: SAIL, IGL, NMDC among 3 PSU stocks with record dates ahead- Chec"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.6 — "ArMee Infotech IPO Day 3: Issue sees 2.44x subscription; GMP at 5%"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.6 — "ArMee Infotech IPO Day 3: Issue sees 2.44x subscription; GMP at 5%"
- TECH (Bio-Techne Corp) score 44.6 — "ArMee Infotech IPO Day 3: Issue sees 2.44x subscription; GMP at 5%"
- IDBI.NS (IDBI BANK LIMITED) score 40.2 — "Why Japan’s markets flipped the usual script after central bank rate hike"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.2 — "Why Japan’s markets flipped the usual script after central bank rate hike"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.2 — "Why Japan’s markets flipped the usual script after central bank rate hike"
- BOND (PIMCO Active Bond Exchange-Tra) score 37.0 — "Japanese investors step up domestic bond purchases as foreign demand drops: JSDA data"
- 301077.SZ (CHINASTARS) score 35.7 — "China saw 'surprise' jump in U.S. orders ahead of Trump-Xi summit, private survey shows"
- SEPN (Septerna, Inc.) score 32.6 — "Stock recommendations for 25 September from MarketSmith India"
- LTH (Life Time Group Holdings, Inc.) score 29.6 — "Xi confirms he will meet Trump 2 more times this year"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.6 — "5 Energy Stocks Positioned for a Prolonged Iran War"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.6 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.6 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- JIOFIN.BO (Jio Financial Services Limited) score 17.9 — "Financial stocks lead correction as insurance overhaul plan sparks fears"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.4 — "Henry Hub natural gas prices this summer were 6% lower than last summer"
- POLICYBZR.NS (PB FINTECH LIMITED) score 14.2 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.5 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- META (Meta) score 12.3 — "Meta stock jumps 36% in September as Muse AI fuels rally"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.7 — "Embassy REIT raises Rs 1,000 cr via debentures to refinance debt"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.7 — "Just One Commodity Vessel Left the Strait of Hormuz on Wednesday"
- MS (Morgan Stanley) score 9.2 — "‘We were wrong.’ Why Morgan Stanley changed its tune on the U.S. dollar — and what it expe"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.2 — "ICICI Lombard General Insurance among 3 stocks showing White Marubozu Pattern"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 7.9 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- VT (Vanguard Total World Stock Ind) score 7.8 — "Beyond high-profile wars, a worldwide battle for critical minerals"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.7 — "Retail investors raise stakes in 10 smallcaps; 3 turn multibaggers in 3 months"
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "Goldman Sachs buys stake in Firstcry brand parent owner Brainbees Solutions | Check price,"
- PINELABS.NS (PINE LABS LIMITED) score 4.0 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- NVDA (NVIDIA Corporation) score 3.2 — "FORMER OPENAI DATA CENTER CHIEF CHRIS MALONE IS NOW AT NVIDIA - THE INFORMATION"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.7 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- VOLTAS.NS (VOLTAS LTD) score 1.5 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.9 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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