# Transmission Layer — board brief · 2026-11-02 12:19Z

data as of **2026-11-02** · 97 series · 9 red / 35 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.724, 2d in regime; vol-pct 0.782, breadth-off 0.667, Markov P(high-vol) 0.256)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.44, contra nifty_50 corr20=0.3, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.12, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 0.07, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.13, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.56, corr60 0.35, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.588, β 0.4859, p 0.0); driver zc -1.52 → expected -0.528%. Type hit-rate 0.829 (n=1681).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.565, β 0.436, p 0.0); driver zc -2.44 → expected -0.787%. Type hit-rate 0.829 (n=1681).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.562, β 0.4472, p 0.0); driver zc -2.34 → expected -0.773%. Type hit-rate 0.829 (n=1681).
- **SETUP** vix → asx_200: leads 1d (ccf -0.495, β -0.0446, p 0.0); driver zc 1.69 → expected -0.576%. Type hit-rate 0.829 (n=1681).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.47, β 0.1797, p 0.0); driver zc -2.0 → expected -0.652%. Type hit-rate 0.829 (n=1681).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.452, β 0.1288, p 0.0); driver zc -2.4 → expected -0.793%. Type hit-rate 0.829 (n=1681).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.378, β -2.4982, p 0.00637); driver zc -2.34 → expected 4.317%. Type hit-rate 0.829 (n=1681).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.353, β 0.5549, p 0.0); driver zc -2.34 → expected -0.959%. Type hit-rate 0.829 (n=1681).
- **SETUP** vix → india_vix: leads 1d (ccf 0.353, β 0.2351, p 0.01051); driver zc 1.69 → expected 3.034%. Type hit-rate 0.829 (n=1681).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.321, β 0.1408, p 1e-05); driver zc -2.34 → expected -0.243%. Type hit-rate 0.829 (n=1681).
- Track record · residual_reversion: hit-rate **0.506** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=1681) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.28] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 143.51, z20 -3.45, zc -2.32, resid-z -0.22 [moved], 1d -10.64%, |z20|=3.45; 1y-pct=1
- btc_usd [CRYPTO]: last 77912.49, z20 -1.83, zc 0.28, resid-z 0.47 [quiet], 1d 0.62%, |z20|=1.83
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.07).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Bitcoin holds steady near $78,000 as investors assess Binance security breach. Here is what experts say — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-steady-near-78000-as-investors-assess-binance-security-breach-here-is-what-experts-say/articleshow/135459441.cms
- Source: Global investors slash dollar-hedging ratio to lowest since 2014 — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/forex/global-investors-slash-dollar-hedging-ratio-to-lowest-since-2014/article71656208.ece
- Source: Global Market: French bond yields hold steady despite Fitch downgrade warning — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-french-bond-yields-hold-steady-despite-fitch-downgrade-warning/articleshow/135454878.cms
- Historical analogues: 2026-05-22 (d=0.07), 2026-04-02 (d=0.27), 2025-08-19 (d=0.32)

### [RED 6.27] cross-asset · 4 series ↓
- ust_2y [RATES]: last 4.61, z20 -2.61, zc -1.00, resid-z -0.99 [quiet], 1d -1.28%, |z20|=2.61
- dyn_schd [EQUITIES]: last 35.79, z20 1.71, zc 0.56, resid-z 0.92 [quiet], 1d 0.51%, 1y-pct=100
- tips_10y_real [RATES]: last 2.63, z20 -1.67, zc -0.82, resid-z -0.85 [quiet], 1d -1.50%, |z20|=1.67
- ust_10y [RATES]: last 4.98, z20 -1.60, zc -1.30, resid-z -1.45 [quiet], 1d -1.39%, |z20|=1.60
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: kospi (inverse) — not yet - watch; rho -0.6 vs dyn_schd
- Watch next: dyn_tgt (co-move) — not yet - watch; rho 0.595 vs dyn_schd
- Source: Global Market: French bond yields hold steady despite Fitch downgrade warning — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-french-bond-yields-hold-steady-despite-fitch-downgrade-warning/articleshow/135454878.cms
- Source: Japan bond yields edge higher ahead of key JGB auctions; 10-year yield holds at 2.77% — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/us-stocks/news/japan-bond-yields-edge-higher-ahead-of-key-jgb-auctions-10-year-yield-holds-at-2-77/articleshow/135453773.cms
- Source: Infosys dividend 2026: Record date tomorrow | Know dividend payout, yield, history, returns — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/infosys-dividend-2026-record-date-tomorrow-know-dividend-payout-yield-history-returns-11793585489373.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.57), 2025-05-19 (d=1.16)

### [RED 6.16] cross-asset · 3 series ↓
- sp500 [INDICES]: last 7580.95, z20 -2.84, zc -2.44, resid-z -0.95 [priced], 1d -1.81%, |z20|=2.84
- dyn_vt [EQUITIES]: last 155.24, z20 -2.37, zc -2.34, resid-z 0.24 [priced], 1d -1.73%, |z20|=2.37
- nasdaq_100 [INDICES]: last 28385.75, z20 -2.24, zc -2.58, resid-z -1.07 [moved], 1d -3.46%, |z20|=2.24
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.744 vs sp500, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.834 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.578 vs sp500, historically leads by 2d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.535 vs nasdaq_100, historically leads by 3d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.71 vs sp500
- Source: Retired World Series champ Matt Holliday lists $11.6 million Arizona estate he bought months ago — MarketWatch Top, 2026-11-02. https://www.marketwatch.com/story/retired-world-series-champ-matt-holliday-lists-11-6-million-arizona-estate-he-bought-months-ago-a48b6a9b?mod=mw_rss_topstories
- Source: Boris Vujčić: Integrated, open and resilient: Europe’s strengths in a fragmenting world — ECB press, 2026-11-02. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp.261102~70003226e9.en.html
- Source: World's energy supply buffers have been eroded, ADNOC CEO says — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/commodities/worlds-energy-supply-buffers-have-been-eroded-adnoc-ceo-says/article71655703.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2025-05-07 (d=0.08)

### [RED 5.96] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3910.20, z20 -2.64, zc -2.98, resid-z -0.72 [priced], 1d 0.29%, |z20|=2.64; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 50.20, z20 -2.04, zc -2.58, resid-z -0.37 [priced], 1d 2.25%, |z20|=2.04; 1y-pct=3; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 77.89, z20 1.75, zc n/a, resid-z n/a [quiet], 1d -1.91%, |z20|=1.75
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.593 vs comex_silver, historically leads by 1d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.53 vs comex_gold
- Source: Today’s Gold Rate in India November 2: Gold prices see mixed trend in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-2-2026/article71655881.ece
- Source: Today’s Gold Rate in India November 2: Gold prices see mixed trend in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-2-2026/article71655882.ece
- Source: Gold rises on softer oil; markets parse Fed signals — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/gold/gold-rises-on-softer-oil-markets-parse-fed-signals/article71655715.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.47] wti ↑
- wti [COMMODITIES]: last 99.86, z20 0.47, zc 0.82, resid-z -1.33 [quiet], 1d -4.09%, 1-session move -4.09% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.44 via wti, z -0.22, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.796 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.534 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.44, z -0.22)
- Source: How oil prices could average $130 per barrel next year, according to Goldman Sachs — MarketWatch Top, 2026-11-02. https://www.marketwatch.com/story/how-oil-prices-could-average-130-per-barrel-next-year-according-to-goldman-sachs-235ce32b?mod=mw_rss_topstories
- Source: Rupee ends little changed as traders stay cautious despite oil, dollar drop — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/forex/rupee-ends-little-changed-as-traders-stay-cautious-despite-oil-dollar-drop/articleshow/135455769.cms
- Source: Iraq's Oil Exports via Turkey Surge to 500,000 Bpd — OilPrice, 2026-11-02. https://oilprice.com/Latest-Energy-News/World-News/Iraqs-Oil-Exports-via-Turkey-Surge-to-500000-Bpd.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.26] nifty_50 ↑
- nifty_50 [INDICES]: last 23440.80, z20 3.26, zc 0.60, resid-z 0.94 [quiet], 1d 1.68%, |z20|=3.26
- **Mechanism**: nifty_50 ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.684 via nifty_50, z -0.22, quiet); nifty_fmcg (rho 0.661 via nifty_50, z -0.06, quiet); dyn_jiofin_bo (rho 0.636 via nifty_50, z 0.22, quiet); dyn_bajfinance_ns (rho 0.607 via nifty_50, z 0.5, quiet); nifty_metal (rho 0.564 via nifty_50, z 0.58, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.684 vs nifty_50, historically leads by 3d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.636 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.746 vs nifty_50
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.542 vs nifty_50, historically leads by 2d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.661 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.684, z -0.22); nifty_fmcg (rho 0.661, z -0.06); dyn_jiofin_bo (rho 0.636, z 0.22); dyn_bajfinance_ns (rho 0.607, z 0.5)
- Source: Reliance fuels Nifty’s best single-day jump in months; Sensex reclaims 75,600 — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/reliance-fuels-niftys-best-single-day-jump-in-months-sensex-reclaims-75600/article71656555.ece
- Source: Sensex today | Stock Market Highlights: Sensex surges 1,233 pts, Nifty ends above 23,400; Reliance, Tata Steel top gainers — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-2nd-november-2026/article71653748.ece
- Source: FIIs increase stake: 11 Nifty stocks rally up to 50% in FY27 so far — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/fiis-increase-stake-11-nifty-stocks-rally-up-to-50-in-fy27-so-far/slideshow/135452650.cms
- Historical analogues: 2026-01-14 (d=0.0), 2025-07-18 (d=0.05), 2025-01-27 (d=0.11)

### [RED 5.2] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 931.00, z20 -3.20, zc -0.56, resid-z -0.63 [quiet], 1d -6.91%, |z20|=3.20; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.58 via dyn_policybzr_ns, z 0.5, quiet); nifty_midcap_100 (rho 0.527 via dyn_policybzr_ns, z -0.22, quiet); nifty_50 (rho 0.5 via dyn_policybzr_ns, z 3.26, reacted); dyn_indusindbk_bo (rho 0.456 via dyn_policybzr_ns, z -1.43, reacted); nifty_fmcg (rho 0.368 via dyn_policybzr_ns, z -0.06, quiet)
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.58 vs dyn_policybzr_ns, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.724 vs dyn_policybzr_ns
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.527 vs dyn_policybzr_ns
- **India receivers**: dyn_bajfinance_ns (rho 0.58, z 0.5); nifty_midcap_100 (rho 0.527, z -0.22); nifty_50 (rho 0.5, z 3.26); dyn_indusindbk_bo (rho 0.456, z -1.43)
- Source: MobiKwik shares zoom 10% as fintech firm posts record Rs 12 crore profit in Q2 — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/mobikwik-shares-zoom-10-as-fintech-firm-posts-record-rs-12-crore-profit-in-q2/articleshow/135452378.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [AMBER 5.0] brent ↓
- brent [COMMODITIES]: last 108.93, z20 -0.00, zc 1.21, resid-z -1.51 [unexplained], 1d -7.40%, 1-session move -7.40% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.406 via brent, z -0.22, quiet)
- Watch next: wti (co-move) — not yet - watch; rho 0.796 vs brent, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho -0.406, z -0.22)
- Source: How oil prices could average $130 per barrel next year, according to Goldman Sachs — MarketWatch Top, 2026-11-02. https://www.marketwatch.com/story/how-oil-prices-could-average-130-per-barrel-next-year-according-to-goldman-sachs-235ce32b?mod=mw_rss_topstories
- Source: Rupee ends little changed as traders stay cautious despite oil, dollar drop — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/forex/rupee-ends-little-changed-as-traders-stay-cautious-despite-oil-dollar-drop/articleshow/135455769.cms
- Source: Iraq's Oil Exports via Turkey Surge to 500,000 Bpd — OilPrice, 2026-11-02. https://oilprice.com/Latest-Energy-News/World-News/Iraqs-Oil-Exports-via-Turkey-Surge-to-500000-Bpd.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

## Watchlist (below surfacing floor)
dyn_atherenerg_ns ↑ (4.66), dyn_lth ↑ (4.47), dyn_rs ↑ (3.94), dyn_sepn ↑ (3.73), usd_cny ↓ (3.69), dyn_4417_t ↑ (3.65), dyn_tech ↑ (3.59), shanghai_comp ↓ (3.49), indices · 2 series ↑ (2.75), fx · 2 series ↑ (2.65), usd_brl ↑ (2.37), dyn_hdb ↓ (2.36)

## India macro
- nifty_50: 23440.8008 (1d 1.68%, z20 3.26, flag red)
- nifty_midcap_100: 57985.2500 (1d 1.19%, z20 -0.22, flag none)
- usd_inr: 94.9000 (1d -0.27%, z20 -0.74, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4737 (1d -0.49%, z20 -1.63, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 74.7 — "Amid price rise, Indian govt doubles weekly wheat auction quantity"
- COALINDIA.NS (COAL INDIA LTD) score 73.6 — "Amid price rise, Indian govt doubles weekly wheat auction quantity"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.9 — "Amid price rise, Indian govt doubles weekly wheat auction quantity"
- INDIANB.NS (INDIAN BANK) score 50.7 — "Amid price rise, Indian govt doubles weekly wheat auction quantity"
- OHI (Omega Healthcare Investors, In) score 44.0 — "Why gold has become a strategic asset for Indian investors"
- BAC (Bank of America Corporation) score 43.2 — "Why Is This Rare Earth Metal 346 Times More Expensive In America Than in China?"
- TGT (Target Corporation) score 42.9 — "China’s fifth plenum: ‘unwritten rules’ newest target in Communist Party’s corruption figh"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.1 — "Tech Query: Sundram Fasteners, HDB Financial Services, Sterlite Technologies, Techno Elect"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.3 — "Tech Query: Sundram Fasteners, HDB Financial Services, Sterlite Technologies, Techno Elect"
- TECH (Bio-Techne Corp) score 38.3 — "Tech Query: Sundram Fasteners, HDB Financial Services, Sterlite Technologies, Techno Elect"
- HDB (HDFC Bank Limited) score 37.7 — "China Reportedly Discusses Ways to Support Stocks With Banks"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.0 — "China Reportedly Discusses Ways to Support Stocks With Banks"
- IDBI.NS (IDBI BANK LIMITED) score 36.9 — "China Reportedly Discusses Ways to Support Stocks With Banks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.9 — "China Reportedly Discusses Ways to Support Stocks With Banks"
- COIN (Coinbase Global, Inc.) score 36.3 — "China’s global initiatives offer ray of hope in a turbulent world"
- RS (Reliance, Inc.) score 32.0 — "Top stocks to watch today: Reliance Industries, Jio Platforms, NTPC, ITC shares in focus o"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.2 — "Senegal’s Ambitious Plan to Slash Electricity Costs and Boost Energy Security"
- CHKP (Check Point Software Technolog) score 29.0 — "Crude Check: Rally may take a breather"
- 301077.SZ (CHINASTARS) score 25.9 — "China’s fifth plenum: ‘unwritten rules’ newest target in Communist Party’s corruption figh"
- LTH (Life Time Group Holdings, Inc.) score 24.6 — "Beijing ramps up maritime patrols around Taiwan, prompting Taipei to shadow ships"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.6 — "India bonds poised to gain as oil slips; US midterms in focus"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 16.0 — "HPCL vs BPCL, IOCL vs ONGC: Which OMC stock to buy as $110/bbl crude oil price becomes a n"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.6 — "Markets open higher as AI selloff boosts anti-tech trade; Reliance, Tata Steel lead gains"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.6 — "Markets open higher as AI selloff boosts anti-tech trade; Reliance, Tata Steel lead gains"
- JIOFIN.BO (Jio Financial Services Limited) score 12.5 — "Tech Query: Sundram Fasteners, HDB Financial Services, Sterlite Technologies, Techno Elect"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 11.1 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- VT (Vanguard Total World Stock Ind) score 10.0 — "China’s global initiatives offer ray of hope in a turbulent world"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.6 — "FPIs pull out ₹34,843 cr from equities in Oct, turn net buyers last week"
- SCHD (Schwab US Dividend Equity ETF) score 9.5 — "Infosys dividend 2026: Record date tomorrow | Know dividend payout, yield, history, return"
- JEF (Jefferies Financial Group Inc.) score 9.4 — "Delhivery shares soar 6% after Q2 results; JPMorgan, Jefferies, Kotak, Citi maintain buy c"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.5 — "Muthoot’s solid gold loan AUM loses sheen amid asset quality stress, stiff competition"
- GS (Goldman Sachs Group, Inc. (The) score 8.1 — "Goldman hikes oil-price forecasts on ‘substantial’ supply risks"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.5 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- SEPN (Septerna, Inc.) score 7.2 — "Nifty holds Sept highs at midday; Reliance surges 7.4%, IT stocks drag"
- META (Meta) score 7.1 — "Why Is This Rare Earth Metal 346 Times More Expensive In America Than in China?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.7 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- INFY (Infosys Limited) score 5.5 — "Infosys dividend 2026: Record date tomorrow | Know dividend payout, yield, history, return"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.3 — "MobiKwik shares zoom 10% as fintech firm posts record Rs 12 crore profit in Q2"
- SWIGGY.NS (SWIGGY LIMITED) score 1.0 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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