# Transmission Layer — board brief · 2026-09-15 09:24Z

data as of **2026-09-15** · 97 series · 25 red / 36 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.766, 1d in regime; vol-pct 0.616, breadth-off 0.917, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.56, corr60 -0.31, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 0.09, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.87, corr60 -0.83, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.16, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.13, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.956591173648327e-05)
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.414, β 0.3415, p 0.0); driver zc -2.14 → expected -1.239%. Type hit-rate 0.818 (n=2044).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.259, β 0.0316, p 0.00026); driver zc 1.88 → expected 0.291%. Type hit-rate 0.818 (n=2044).
- Track record · residual_reversion: hit-rate **0.495** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2044) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 12.02] cross-asset · 16 series ↓
- tips_10y_real [RATES]: last 2.60, z20 3.69, zc 1.10, resid-z 1.46 [quiet], 1d 1.96%, 1d move +5.0bps ≥ 5bps; |z20|=3.69; 1y-pct=100
- dyn_ms [EQUITIES]: last 206.60, z20 -3.15, zc -2.14, resid-z -0.11 [priced], 1d -3.63%, |z20|=3.15
- ust_2y [RATES]: last 4.63, z20 3.12, zc 1.16, resid-z 1.39 [quiet], 1d 1.54%, |z20|=3.12; 1y-pct=100
- ust_10y [RATES]: last 4.96, z20 3.00, zc 0.20, resid-z 0.38 [quiet], 1d 0.20%, |z20|=3.00; 1y-pct=100
- stoxx_50 [INDICES]: last 6209.21, z20 -2.96, zc -0.86, resid-z -1.07 [quiet], 1d -0.82%, |z20|=2.96
- vix [INDICES]: last 17.88, z20 2.63, zc 0.51, resid-z n/a [quiet], 1d 4.56%, |z20|=2.63
- dax [INDICES]: last 25229.42, z20 -2.54, zc -0.92, resid-z -0.20 [quiet], 1d -0.83%, |z20|=2.54
- dyn_bond [EQUITIES]: last 88.75, z20 -2.50, zc -0.27, resid-z -0.80 [quiet], 1d -0.10%, |z20|=2.50; 1y-pct=0
- cac_40 [INDICES]: last 8048.68, z20 -2.33, zc -0.95, resid-z -0.62 [quiet], 1d -0.85%, |z20|=2.33
- ust_30y [RATES]: last 5.35, z20 2.27, zc -0.47, resid-z -0.34 [quiet], 1d -0.37%, |z20|=2.27; 1y-pct=99
- wti [COMMODITIES]: last 103.45, z20 2.22, zc 0.69, resid-z 0.31 [quiet], 1d 2.03%, 1-session move +2.03% ≥ 1.5%; |z20|=2.22; 1y-pct=96
- ftse_100 [INDICES]: last 10610.23, z20 -2.18, zc -1.32, resid-z 0.91 [quiet], 1d -0.82%, |z20|=2.18
- dyn_vt [EQUITIES]: last 158.72, z20 -2.12, zc -0.93, resid-z 0.03 [quiet], 1d -0.76%, |z20|=2.12
- russell_2000 [INDICES]: last 2892.41, z20 -1.88, zc -0.33, resid-z 0.28 [quiet], 1d -0.40%, |z20|=1.88
- dow_jones [INDICES]: last 52421.57, z20 -1.65, zc -0.34, resid-z 0.22 [quiet], 1d -0.29%, |z20|=1.65
- brent [COMMODITIES]: last 102.58, z20 1.30, zc -0.99, resid-z 0.16 [quiet], 1d -2.93%, 1-session move -2.93% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: cross-asset · 16 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.507 via ftse_100, z -1.0, quiet); nifty_midcap_100 (rho 0.472 via dax, z -3.99, reacted); dyn_techm_ns (rho 0.412 via ftse_100, z -0.14, quiet); midcap_largecap_ratio (rho -0.397 via ust_2y, z -0.92, quiet); nifty_50 (rho 0.379 via ftse_100, z -2.78, reacted)
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.506 vs cac_40, historically leads by 5d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.507 vs ftse_100
- **India receivers**: nifty_it (rho 0.507, z -1.0); nifty_midcap_100 (rho 0.472, z -3.99); dyn_techm_ns (rho 0.412, z -0.14); midcap_largecap_ratio (rho -0.397, z -0.92)
- Source: Sensex today | Stock Market Live: Sensex down over 520 pts, Nifty slips below 23,280 as Crude, Fed fears drag markets into red — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-15th-september-2026/article71466165.ece
- Source: US 10-year bond yield crosses 5%: Why Warren Buffett once called bonds a terrible investment — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/us-stocks/news/us-10-year-bond-yield-crosses-5-why-warren-buffett-once-called-bonds-a-terrible-investment/articleshow/134256140.cms
- Source: IT stocks couldn’t save Nifty as crude, Fed fears drag markets into red — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/stock-markets/it-stocks-couldnt-save-nifty-as-crude-fed-fears-drag-markets-into-red/article71467100.ece

### [RED 8.85] cross-asset · 4 series ↓
- india_vix [INDICES]: last 13.46, z20 5.19, zc 0.74, resid-z n/a [quiet], 1d 9.54%, |z20|=5.19
- nifty_midcap_100 [INDICES]: last 61007.25, z20 -3.99, zc -0.40, resid-z -0.44 [quiet], 1d -1.91%, |z20|=3.99
- nifty_50 [INDICES]: last 23181.80, z20 -2.78, zc -0.61, resid-z -0.80 [quiet], 1d -0.92%, |z20|=2.78
- dyn_jiofin_bo [EQUITIES]: last 227.20, z20 -2.27, zc -0.35, resid-z 0.41 [quiet], 1d -1.22%, |z20|=2.27; 1y-pct=1
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.622 via nifty_50, z -1.61, reacted); dyn_indianb_ns (rho 0.554 via nifty_midcap_100, z -3.25, reacted); nifty_it (rho 0.51 via nifty_50, z -1.0, quiet); dyn_indusindbk_bo (rho 0.464 via nifty_50, z -3.12, reacted); dyn_techm_ns (rho 0.463 via nifty_50, z -0.14, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.51 vs nifty_50, historically leads by 3d
- **India receivers**: nifty_fmcg (rho 0.622, z -1.61); dyn_indianb_ns (rho 0.554, z -3.25); nifty_it (rho 0.51, z -1.0); dyn_indusindbk_bo (rho 0.464, z -3.12)
- Source: Sensex today | Stock Market Live: Sensex down over 520 pts, Nifty slips below 23,280 as Crude, Fed fears drag markets into red — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-15th-september-2026/article71466165.ece
- Source: Sensex, Nifty today: Why is stock market down today? Top 3 factors driving the selloff explained — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/sensex-nifty-today-why-is-stock-market-down-today-top-3-factors-driving-the-selloff-explained-11789460084552.html
- Source: Shriram Finance, Hindustan Aeronautics, Siemens Energy shares fall nearly 4%, among top Nifty 100 laggards — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/shriram-finance-hindustan-aeronautics-siemens-energy-shares-fall-nearly-4-among-top-nifty-100-laggards-11789459288755.html
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 7.63] cross-asset · 4 series ↓
- comex_silver [COMMODITIES]: last 63.28, z20 -1.81, zc -0.14, resid-z 0.86 [quiet], 1d -0.37%, |z20|=1.81; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.38, z20 -1.70, zc 0.36, resid-z -0.77 [quiet], 1d 0.80%, |z20|=1.70; co-occur[metal_copper] suppressed: channel WEAK
- comex_gold [COMMODITIES]: last 4304.50, z20 -1.68, zc -0.78, resid-z 0.15 [quiet], 1d -1.09%, |z20|=1.68; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.02, z20 0.96, zc n/a, resid-z n/a [quiet], 1d -0.72%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho -0.369 via gold_silver_ratio, z -3.42, reacted)
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.646 vs comex_gold, historically leads by 5d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.621 vs comex_silver, historically leads by 5d
- **India receivers**: nifty_metal (rho -0.369, z -3.42)
- Source: Kerala gold trade sector pins hopes on proposed jewellery park — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/commodities/kerala-gold-trade-sector-pins-hopes-on-proposed-jewellery-park/article71466974.ece
- Source: Positive inflows into gold ETFs continues for eighth week in a row — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/gold/positive-inflows-into-gold-etfs-continues-for-eighth-week-in-a-row/article71466928.ece
- Source: Gold prices at Rs 1.52 lakh/10 grams, silver down Rs 3,300/kg in 2 days ahead of US Fed decision. Key levels to track — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-at-rs-1-52-lakh/10-grams-silver-down-rs-3300/kg-in-2-days-ahead-of-us-fed-decision-key-levels-to-track/articleshow/134251599.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 7.0] brent_wti_spread ↓
- brent_wti_spread [DERIVED]: last -0.87, z20 -7.00, zc n/a, resid-z n/a [quiet], 1d -120.28%, |z20|=7.00; 1y-pct=2
- **Mechanism**: brent_wti_spread ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho -0.39 via brent_wti_spread, z 0.22, quiet)
- **India receivers**: eur_inr (rho -0.39, z 0.22)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-04 (d=0.0), 2026-05-06 (d=0.01)

### [AMBER 6.36] usd_inr ↑
- usd_inr [FX]: last 95.94, z20 1.36, zc 1.65, resid-z 2.11 [unexplained], 1d 0.95%, 20d range extreme; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: RBI likely intervened to shield rupee as oil prices climb, traders say — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rbi-likely-intervened-to-shield-rupee-as-oil-prices-climb-traders-say/article71466683.ece
- Source: Rupee falls 30 paise to 95.84 against US dollar in early trade — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rupee-falls-30-paise-to-9584-against-us-dollar-in-early-trade/article71466720.ece
- Source: Rupee, bonds under pressure as oil stays above $100 and Fed hike looms — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rupee-bonds-under-pressure-as-oil-stays-above-100-and-fed-hike-looms/article71466545.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 6.08] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5360.00, z20 4.08, zc 1.56, resid-z -0.59 [moved], 1d 8.83%, |z20|=4.08; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: From VBL, Power Grid to Paytm - 6 stocks experts recommend buying for the short term; do you own any? — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/from-vbl-power-grid-to-paytm-6-stocks-experts-recommend-buying-for-the-short-term-do-you-own-any-11789451473678.html
- Source: HDFC Bank share price jumps over 6% in 3 days | Experts see 15% more upside, check target price — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-jumps-over-6-in-3-days-experts-see-15-more-upside-check-target-price-11789444548891.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 5.9] dyn_bac ↓
- dyn_bac [EQUITIES]: last 59.47, z20 -3.90, zc -3.69, resid-z -0.35 [moved], 1d -5.14%, |z20|=3.90
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho 0.366 via dyn_bac, z 0.22, quiet)
- **India receivers**: eur_inr (rho 0.366, z 0.22)
- Source: The 10 most overvalued housing markets in America — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-10-most-overvalued-housing-markets-in-america-6d28efdf?mod=mw_rss_topstories
- Source: TRUMP: “DON’T KILL THE GOLDEN GOOSE” President Trump says America’s AI and data center boom is happening because the U.S. holds a commanding global lead. He urged against measures that could slow the industry’s expansion, warning policymakers: “Don’t kill the Golden Goose!” — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35759
- Source: BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7,400 from 7,100, signaling increased confidence in the equity rally. BofA also introduced a 12-month target of 7,800, pointing to further upside for U.S. stocks beyond year-end. — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35746
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 5.47] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -2.64, zc -1.67, resid-z -1.41 [moved], 1d -0.49%, |z20|=2.64
- gbp_usd [FX]: last 1.35, z20 -1.87, zc -1.03, resid-z -1.18 [quiet], 1d -0.40%, |z20|=1.87
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.394 via gbp_usd, z -1.8, reacted)
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.367 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_muthootfin_ns (rho 0.394, z -1.8)
- Source: Piero Cipollone: The future of euro cash: trusted today, designed for tomorrow — ECB press, 2026-09-14. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260914_1~91d3436449.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

## Watchlist (below surfacing floor)
usd_mxn ↑ (4.86), indices · 2 series ↓ (4.85), dyn_jef ↓ (4.71), dyn_tatatech_ns ↓ (4.32), dyn_icicigi_bo ↓ (4.06), nifty_metal ↓ (3.42), dyn_indianb_ns ↓ (3.25), dyn_indusindbk_bo ↓ (3.12), dyn_lenskart_ns ↑ (3.02), asx_200 ↓ (2.86), hang_seng ↓ (2.66), ust_2s10s ↓ (2.63)

## India macro
- nifty_50: 23181.8008 (1d -0.92%, z20 -2.78, flag red)
- nifty_midcap_100: 61007.2500 (1d -1.91%, z20 -3.99, flag red)
- usd_inr: 95.9375 (1d 0.95%, z20 1.36, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6317 (1d -1.00%, z20 -0.92, flag none)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 60.0 — "NSE IPO threatens to hollow out India’s unlisted shadow market"
- COALINDIA.NS (COAL INDIA LTD) score 59.5 — "NSE IPO threatens to hollow out India’s unlisted shadow market"
- INDIANB.NS (INDIAN BANK) score 58.8 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 58.4 — "NSE IPO threatens to hollow out India’s unlisted shadow market"
- BAC (Bank of America Corporation) score 51.8 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- COIN (Coinbase Global, Inc.) score 49.7 — "What Saudi Arabia’s East-West pipeline closure means for global energy markets"
- HDB (HDFC Bank Limited) score 44.7 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- IDBI.NS (IDBI BANK LIMITED) score 42.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- OHI (Omega Healthcare Investors, In) score 37.9 — "Wealthy Investors Flock To Oil & Gas Assets Amid Energy Crisis"
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- TECH (Bio-Techne Corp) score 35.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- CHKP (Check Point Software Technolog) score 33.8 — "Rentomojo IPO: Allotment today; check status online | 72.88x subscription - GMP signals 39"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.5 — "Rupee, bonds under pressure as oil stays above $100 and Fed hike looms"
- 301077.SZ (CHINASTARS) score 23.1 — "LNG Demand in China and India Could Surge When Prices Normalize"
- LTH (Life Time Group Holdings, Inc.) score 21.3 — "Infosys, HCLTech, TCS, other IT stocks soar up to 6%; Nifty IT rallies 5% as global AI slo"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.0 — "Wealthy Investors Flock To Oil & Gas Assets Amid Energy Crisis"
- SEPN (Septerna, Inc.) score 18.7 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.8 — "From TCS, Tata Chemicals to Tata Motors PV- Tata Group stocks surge up to 20%- What is dri"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.8 — "From TCS, Tata Chemicals to Tata Motors PV- Tata Group stocks surge up to 20%- What is dri"
- NVDA (NVIDIA Corporation) score 9.5 — "NVIDIA, Palantir and Booz Allen Hamilton will limit use of ANTHROPIC models"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.0 — "Saudi Arabia may be just days away from not being able to export much oil"
- JIOFIN.BO (Jio Financial Services Limited) score 8.1 — "EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services;"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.5 — "Can SS Retail IPO deliver long-term growth for high-risk investors?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.3 — "All that glitters... in jewellers’ IPO boom"
- JEF (Jefferies Financial Group Inc.) score 6.6 — "HDFC Bank share price target: What are Jefferies, 3 other foreign brokerages saying as CEO"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.5 — "Tech picks: Adani Ports, Data Patterns among 5 stocks that could give up to 23% returns in"
- VT (Vanguard Total World Stock Ind) score 6.5 — "3 SME IPOs open today: Vama Wovenfab, Shakti Polytarp and Quanto Agroworld. Check GMP and "
- MS (Morgan Stanley) score 6.2 — "GOLDMAN, JPMORGAN NOW EXPECT FED TO HIKE THIS WEEK Goldman Sachs and JPMorgan have shifted"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.0 — "LIC Housing Finance among 5 F&O stocks with sharp rise in futures open interest"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 5.2 — "HDFC Bank share price jumps over 6% in 3 days | Experts see 15% more upside, check target "
- META (Meta) score 4.6 — "Gold and silver prices crash up to 2% on MCX- What is driving precious metals down?"
- BZ=F (Brent Crude Oil Last Day Finan) score 4.4 — "Dividend record date alert: Last chance to buy today for cash reward; Hindustan Copper, Ba"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.9 — "ICICI Securities says buy this NBFC stock, sees 59% upside after an 80% jump in 6 months -"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.4 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.8 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.1 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
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