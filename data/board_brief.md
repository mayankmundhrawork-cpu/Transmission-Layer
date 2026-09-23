# Transmission Layer — board brief · 2026-09-23 09:17Z

data as of **2026-09-23** · 97 series · 13 red / 36 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.405, 4d in regime; vol-pct 0.083, breadth-off 0.727, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.36, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.12, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.07, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.06, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.39, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0015243893761345273)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.491, β 0.1964, p 0.0); driver zc -1.6 → expected -0.563%. Type hit-rate 0.816 (n=2207).
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.469, β 0.2292, p 0.0); driver zc -1.93 → expected -0.688%. Type hit-rate 0.816 (n=2207).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.415, β 0.3415, p 0.0); driver zc -1.6 → expected -0.979%. Type hit-rate 0.816 (n=2207).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.387, β 0.3162, p 0.0); driver zc -1.6 → expected -0.907%. Type hit-rate 0.816 (n=2207).
- Track record · residual_reversion: hit-rate **0.495** (n=1097) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2207) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.84] natgas ↑
- natgas [COMMODITIES]: last 3.18, z20 5.84, zc 2.21, resid-z 1.75 [unexplained], 1d 7.12%, 1-session move +7.12% ≥ 5.0%; |z20|=5.84
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.075 vs natgas, historically leads by 4d
- Source: Washington Needs This LNG Deal More Than Beijing Does — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Washington-Needs-This-LNG-Deal-More-Than-Beijing-Does.html
- Source: Public companies produce most U.S. crude oil and natural gas — EIA Today in Energy, 2026-09-22. https://www.eia.gov/todayinenergy/detail.php?id=68184
- Source: Qatar’s LNG Loss Revives Projects From Argentina to Timor-Leste — OilPrice, 2026-09-22. https://oilprice.com/Energy/Natural-Gas/Qatars-LNG-Loss-Revives-Projects-From-Argentina-to-Timor-Leste.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 8.18] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.76, z20 1.72, zc 0.00, resid-z 0.00 [quiet], 1d 0.00%, |z20|=1.72; 1y-pct=99
- tips_10y_real [RATES]: last 2.62, z20 1.25, zc -1.19, resid-z -1.38 [quiet], 1d -2.24%, 1d move -6.0bps ≥ 5bps; 1y-pct=98
- ust_10y [RATES]: last 4.96, z20 1.11, zc -1.02, resid-z -0.67 [quiet], 1d -1.00%, 1y-pct=98
- dyn_bond [EQUITIES]: last 89.05, z20 -0.81, zc 0.23, resid-z -0.26 [quiet], 1d 0.08%, 1y-pct=3
- ust_30y [RATES]: last 5.29, z20 0.28, zc -1.21, resid-z -0.83 [quiet], 1d -0.94%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.381 via ust_2y, z 1.06, reacted)
- Watch next: wti (co-move) — not yet - watch; rho 0.607 vs ust_10y, historically leads by 3d
- Watch next: brent (co-move) — not yet - watch; rho 0.641 vs ust_10y
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.54 vs ust_10y
- Watch next: dyn_tna (inverse) — not yet - watch; rho -0.534 vs ust_10y
- **India receivers**: midcap_largecap_ratio (rho -0.381, z 1.06)
- Source: Softbank’s mega junk-bond deal shows capital for the AI race is getting more expensive — MarketWatch Top, 2026-09-23. https://www.marketwatch.com/story/softbanks-mega-junk-bond-deal-shows-capital-for-the-ai-race-is-getting-more-expensive-9eb3fa28?mod=mw_rss_topstories
- Source: Vietnam raises $1 billion in government bond auction, highest volume this year — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/bonds/vietnam-raises-1-billion-in-government-bond-auction-highest-volume-this-year/articleshow/134426711.cms
- Source: US Market: Financial stocks slide as AI disruption, bond curve weigh on banks — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/stocks/news/us-market-financial-stocks-slide-as-ai-disruption-bond-curve-weigh-on-banks/articleshow/134425549.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.99] cross-asset · 5 series ↑
- nasdaq_100 [INDICES]: last 30728.40, z20 4.06, zc 0.55, resid-z -0.03 [quiet], 1d 0.81%, |z20|=4.06; 1y-pct=100
- sp500 [INDICES]: last 7764.27, z20 1.90, zc -0.01, resid-z 3.24 [unexplained], 1d -0.01%, |z20|=1.90; 1y-pct=98
- dyn_nvda [EQUITIES]: last 228.83, z20 1.43, zc 0.25, resid-z -0.10 [quiet], 1d 0.64%, 1y-pct=99
- vix [INDICES]: last 14.13, z20 -1.31, zc -0.07, resid-z n/a [quiet], 1d -0.56%, 1y-pct=2
- dyn_vt [EQUITIES]: last 161.26, z20 1.01, zc 0.24, resid-z 0.32 [quiet], 1d 0.23%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-04 (z-distance 0.22).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.631 vs sp500, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.62 vs sp500, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.769 vs nasdaq_100
- Watch next: dyn_tna (co-move) — not yet - watch; rho 0.768 vs nasdaq_100
- Watch next: dax (co-move) — not yet - watch; rho 0.638 vs dyn_vt
- Source: This oil giant has lagged its leading rivals through two energy crises. Now one Wall Street giant says it’s time to buy. — MarketWatch Top, 2026-09-23. https://www.marketwatch.com/story/this-oil-giant-has-lagged-its-leading-rivals-through-two-energy-crises-now-one-wall-street-giant-says-its-time-to-buy-987838c3?mod=mw_rss_topstories
- Source: The Nasdaq’s rapid rise to a record is sending a message to investors: Don’t wait for a pullback to buy — MarketWatch Top, 2026-09-22. https://www.marketwatch.com/story/the-nasdaqs-rapid-rise-to-a-record-is-sending-a-message-to-investors-dont-wait-for-a-pullback-to-buy-5f533ed8?mod=mw_rss_topstories
- Source: Why Apple could soon join Nvidia in the exclusive $5 trillion club — MarketWatch Top, 2026-09-22. https://www.marketwatch.com/story/why-apple-could-soon-join-nvidia-in-the-exclusive-5-trillion-club-4e7724e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-04 (d=0.22), 2025-10-23 (d=0.29), 2025-08-28 (d=0.29)

### [AMBER 6.44] commodities · 2 series ↓
- wti [COMMODITIES]: last 90.08, z20 -0.61, zc -1.65, resid-z -0.42 [moved], 1d -4.77%, 1-session move -4.77% ≥ 1.5%
- brent [COMMODITIES]: last 95.74, z20 -0.49, zc -1.45, resid-z -0.39 [quiet], 1d -3.54%, 1-session move -3.54% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.5 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.632 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.611 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.536 vs wti
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.503 vs wti
- Source: $100 Brent Keeping China's Oil Buying in Check, Goldman Says — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/100-Brent-Keeping-Chinas-Oil-Buying-in-Check-Goldman-Says.html
- Source: This oil giant has lagged its leading rivals through two energy crises. Now one Wall Street giant says it’s time to buy. — MarketWatch Top, 2026-09-23. https://www.marketwatch.com/story/this-oil-giant-has-lagged-its-leading-rivals-through-two-energy-crises-now-one-wall-street-giant-says-its-time-to-buy-987838c3?mod=mw_rss_topstories
- Source: Metals lead Nifty higher; crude slide, geopolitical uncertainty cap gains — BusinessLine Mkts, 2026-09-23. https://www.thehindubusinessline.com/markets/stock-markets/metals-lead-nifty-higher-crude-slide-geopolitical-uncertainty-cap-gains/article71498873.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [AMBER 5.75] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 85967.01, z20 2.43, zc -0.05, resid-z -0.40 [quiet], 1d -0.19%, |z20|=2.43
- eth_usd [CRYPTO]: last 2741.47, z20 2.41, zc -0.08, resid-z -0.49 [quiet], 1d -0.32%, |z20|=2.41
- dyn_coin [EQUITIES]: last 201.06, z20 2.15, zc 0.00, resid-z -0.07 [quiet], 1d 0.00%, |z20|=2.15
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 0.98).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.41 via dyn_coin, z 1.06, reacted); dyn_cartrade_ns (rho 0.386 via eth_usd, z -0.24, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.527 vs btc_usd, historically leads by 1d
- **India receivers**: midcap_largecap_ratio (rho 0.41, z 1.06); dyn_cartrade_ns (rho 0.386, z -0.24)
- Source: Global Market: Grab executives buy over $30 million in shares after stock slump — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-grab-executives-buy-over-30-million-in-shares-after-stock-slump/articleshow/134429891.cms
- Source: Global Market: Singapore core inflation hits nearly two-year high in August — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-singapore-core-inflation-hits-nearly-two-year-high-in-august/articleshow/134428523.cms
- Source: Global Market: China, Hong Kong stocks fall as investors temper Trump-Xi meeting hopes; property shares gain — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-hong-kong-stocks-fall-as-investors-temper-trump-xi-meeting-hopes-property-shares-gain/articleshow/134427229.cms
- Historical analogues: 2025-08-11 (d=0.98), 2024-11-21 (d=1.42), 2026-05-05 (d=1.47)

### [RED 5.6] fx · 2 series ↓
- gbp_usd [FX]: last 1.33, z20 -2.77, zc -1.58, resid-z -1.41 [moved], 1d -0.57%, |z20|=2.77
- eur_usd [FX]: last 1.14, z20 -2.60, zc -1.36, resid-z -0.90 [quiet], 1d -0.42%, |z20|=2.60
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.413 via gbp_usd, z -0.28, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.565 vs eur_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.327 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_icicigi_bo (rho -0.413, z -0.28)
- Source: Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic and global orders — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/stocks/news/sterling-and-wilson-renewable-energy-shares-rally-8-after-securing-rs-985-crore-domestic-and-global-orders/articleshow/134402652.cms
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.42] dxy ↑
- dxy [FX]: last 100.83, z20 2.42, zc 0.87, resid-z 1.14 [quiet], 1d 0.29%, 20d range extreme; |z20|=2.42
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.40 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.366 via dyn_4417_t, z 0.79, quiet)
- **India receivers**: dyn_justdial_bo (rho 0.366, z 0.79)
- Source: Sebi board is set to grow. Experts say it's missing one safeguard it needs most — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/sebi-board-expansion-securities-markets-code-2025-appointmentprocess-11788844688106.html
- Source: How to invest amid heightened uncertainty? Look at multi-asset allocation funds, say experts — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/how-to-invest-amid-heightened-uncertainty-look-at-multi-asset-allocation-funds-say-experts-11790078842845.html
- Source: Vedanta Aluminium stock jumps 4% days after hitting 52-week low! Can it reclaim demerger level? Experts decode outlook — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/vedanta-aluminium-stock-jumps-4-days-after-hitting-52-week-low-can-it-reclaim-demerger-level-experts-decode-outlook-11790062916085.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_lth ↓ (4.76), dyn_bac ↓ (4.66), gold_silver_ratio ↓ (4.64), dyn_meta ↑ (4.31), dyn_ms ↓ (4.3), dyn_tech ↑ (4.23), comex_copper ↑ (4.14), midcap_largecap_ratio ↑ (4.06), fx · 2 series ↑ (3.89), dyn_sepn ↑ (3.38), dyn_voltas_ns ↓ (2.99), sofr ↑ (2.91)

## India macro
- nifty_50: 23431.1992 (1d 0.44%, z20 -0.73, flag none)
- nifty_midcap_100: 62374.0508 (1d 0.67%, z20 -0.39, flag none)
- usd_inr: 95.7125 (1d 0.00%, z20 0.78, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6620 (1d 0.23%, z20 1.06, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 70.6 — "CCI clears Fairfax India’s proposal to acquire additional stake in IIFL Capital Services"
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.7 — "CCI clears Fairfax India’s proposal to acquire additional stake in IIFL Capital Services"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 67.9 — "CCI clears Fairfax India’s proposal to acquire additional stake in IIFL Capital Services"
- COIN (Coinbase Global, Inc.) score 54.0 — "ETMarkets Smart Talk | Anthropic, SpaceX, US stocks: Viram Shah on how Indian investors ca"
- INDIANB.NS (INDIAN BANK) score 53.9 — "Sensex, Nifty 50 prediction today: How Asian markets, crude will impact Indian markets? Gi"
- OHI (Omega Healthcare Investors, In) score 47.2 — "Trump’s 100% tariff threat: What Indian investors should do now"
- BAC (Bank of America Corporation) score 46.9 — "RBL Bank among 4 stocks showing White Marubozu Pattern"
- HDB (HDFC Bank Limited) score 43.2 — "RBL Bank among 4 stocks showing White Marubozu Pattern"
- CHKP (Check Point Software Technolog) score 41.1 — "Elevate Campuses’ Rs 2,100 cr IPO opens for subscription. Check GMP, other details"
- IDBI.NS (IDBI BANK LIMITED) score 40.1 — "RBL Bank among 4 stocks showing White Marubozu Pattern"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.1 — "RBL Bank among 4 stocks showing White Marubozu Pattern"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.1 — "RBL Bank among 4 stocks showing White Marubozu Pattern"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.0 — "India bond rally likely to extend marginally as Brent slips below $100/barrel"
- SEPN (Septerna, Inc.) score 26.2 — "Dividend record date 23 Sept alert: Last call for investors today! Buy Arfin India, Engine"
- LTH (Life Time Group Holdings, Inc.) score 26.2 — "Gold lacklustre as higher-for-longer rate outlook weighs on sentiment"
- TECHM.NS (TECH MAHINDRA LIMITED) score 25.7 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Price Analysis"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 25.7 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Price Analysis"
- TECH (Bio-Techne Corp) score 25.7 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Price Analysis"
- 301077.SZ (CHINASTARS) score 22.3 — "Goldman Sees China Oil Imports Staying Subdued in Fourth Quarter"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.9 — "Noel Tata's latest proposal offers alternative to Tata Sons' listing but Shapoorji Pallonj"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 20.9 — "Noel Tata's latest proposal offers alternative to Tata Sons' listing but Shapoorji Pallonj"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.3 — "Ather Energy among 4 F&O stocks with a sharp rise in futures open interest"
- JIOFIN.BO (Jio Financial Services Limited) score 17.6 — "CCI clears Fairfax India’s proposal to acquire additional stake in IIFL Capital Services"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.6 — "Dividend record date 23 Sept alert: Last call for investors today! Buy Arfin India, Engine"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.3 — "IPO listings today: SS Retail vs Hero Motors vs Jindal Supreme - Bumper listing and flop s"
- META (Meta) score 10.2 — "Gold vs Silver: Which metal to invest in for maximum profit amid ongoing US-Iran war and o"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.1 — "The real estate portfolio of Zendaya and Tom Holland, plus her plans for a room just for h"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.4 — "Sebi board is set to grow. Experts say it's missing one safeguard it needs most"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.2 — "5 Adani group stocks in focus as firms settle Sebi proceedings linked to Hindenburg report"
- PINELABS.NS (PINE LABS LIMITED) score 6.8 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.8 — "Bajaj Finance shares jump 3% after UBS upgrades to Neutral, hikes target price while Jeffe"
- MS (Morgan Stanley) score 5.5 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- GS (Goldman Sachs Group, Inc. (The) score 5.2 — "Goldman Sees China Oil Imports Staying Subdued in Fourth Quarter"
- VT (Vanguard Total World Stock Ind) score 5.0 — "U.S. Threatens to Ground Iranian Airlines Worldwide"
- TNA (Direxion Small Cap Bull 3X ETF) score 4.9 — "Small-cap stocks trade at nearly twice Nifty 50 valuation, says VK Vijayakumar"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.6 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 4.0 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.6 — "Action Construction share price jumps 50% in 6 months - ICICI Direct sees it rising furthe"
- VOLTAS.NS (VOLTAS LTD) score 1.3 — "Voltas share price: Nuvama upgrades rating but Jefferies cuts target price after analyst m"
- DELL (Dell Technologies Inc.) score 0.1 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"

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