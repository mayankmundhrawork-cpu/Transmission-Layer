# Transmission Layer — board brief · 2026-08-21 07:05Z

data as of **2026-08-21** · 98 series · 13 red / 24 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.29, 2d in regime; vol-pct 0.204, breadth-off 0.375, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.41, contra nifty_50 corr20=0.03, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.87, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.37, last shift 2026-07-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.13, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.69, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.04, corr60 -0.13, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.21, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.25, corr60 0.22, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.593, β 0.4867, p 0.0); driver zc -1.88 → expected -0.628%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.489, β 0.1961, p 0.0); driver zc -1.84 → expected -0.616%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.466, β 0.7864, p 0.0); driver zc -1.88 → expected -1.014%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.422, β 0.7091, p 0.0); driver zc -1.88 → expected -0.914%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.416, β 0.3441, p 0.0); driver zc -1.84 → expected -1.081%. Type hit-rate 0.821 (n=2333).
- **SETUP** tips_10y_real → usd_jpy: leads 1d (ccf 0.409, β 0.1225, p 0.0); driver zc -1.66 → expected -0.305%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.396, β 0.2601, p 1e-05); driver zc -1.88 → expected -0.335%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.391, β 0.3216, p 0.0); driver zc -1.84 → expected -1.01%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.363, β -0.2363, p 0.0); driver zc -1.88 → expected 0.305%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.275, β 0.0882, p 0.00294); driver zc -1.84 → expected -0.277%. Type hit-rate 0.821 (n=2333).
- Track record · residual_reversion: hit-rate **0.491** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2333) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.81] dyn_mrna ↑
- dyn_mrna [EQUITIES]: last 133.34, z20 7.81, zc 5.86, resid-z 11.29 [unexplained], 1d 35.87%, |z20|=7.81; 1y-pct=100
- **Mechanism**: dyn_mrna ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may also be overhyped — MarketWatch Top, 2026-08-20. https://www.marketwatch.com/story/modernas-personalized-mrna-shot-could-reshape-the-fight-against-skin-cancer-but-it-may-also-be-overhyped-a6f1bc88?mod=mw_rss_topstories
- Source: Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/modernas-cancer-vaccine-breakthrough-what-it-means-for-the-stock/slideshow/133367426.cms
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.01), 2025-08-20 (d=0.01)

### [RED 8.17] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 75672.61, z20 4.85, zc 1.13, resid-z 2.80 [unexplained], 1d 4.08%, |z20|=4.85
- eth_usd [CRYPTO]: last 2373.06, z20 3.67, zc 0.47, resid-z 1.39 [quiet], 1d 2.35%, |z20|=3.67
- dyn_coin [EQUITIES]: last 172.46, z20 2.62, zc 1.52, resid-z 2.13 [unexplained], 1d 7.65%, |z20|=2.62
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.02).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.588 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.514 vs eth_usd
- Source: Nifty’s higher highs offer a bullish signal amid global turmoil — Mint Markets, 2026-08-21. https://www.livemint.com/market/stock-market-news/niftys-higher-highs-offer-a-bullish-signal-amid-global-turmoil-11787283025704.html
- Source: Bitcoin on Track for Biggest Weekly Gain in More Than Two Years — Mint Markets, 2026-08-21. https://www.livemint.com/market/bitcoin-on-track-for-biggest-weekly-gain-in-more-than-two-years-11787292175301.html
- Source: Global Market: China stocks hold steady as investors await fiscal support — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-hold-steady-as-investors-await-fiscal-support/articleshow/133394857.cms
- Historical analogues: 2025-08-13 (d=1.02), 2025-05-09 (d=2.1), 2024-11-13 (d=2.26)

### [RED 7.49] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4621.30, z20 2.23, zc 1.49, resid-z 0.72 [quiet], 1d 2.32%, |z20|=2.23; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 68.90, z20 1.98, zc 0.49, resid-z 1.92 [unexplained], 1d 1.29%, |z20|=1.98; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.07, z20 -1.17, zc n/a, resid-z n/a [quiet], 1d 1.02%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.53 via comex_silver, z 0.78, quiet); dyn_stylebaaza_ns (rho -0.398 via gold_silver_ratio, z 2.0, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.662 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.57 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.533 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.53 vs comex_silver, historically leads by 4d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.505 vs comex_silver
- **India receivers**: nifty_metal (rho 0.53, z 0.78); dyn_stylebaaza_ns (rho -0.398, z 2.0)
- Source: Where is gold heading? Jefferies turns bullish as US, Japan face fiscal strain — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/gold/where-is-gold-heading-jefferies-turns-bullish-as-us-japan-face-fiscal-strain/article71372425.ece
- Source: Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 gm — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-manappuram-finance-shares-jump-up-to-7-in-2-days-as-gold-crosses-rs-1-6-lakh/10-gm/articleshow/133394594.cms
- Source: Gold prices rise Rs 6,400/10g in 3 days; silver jumps Rs 13,000/kg despite Middle East tensions. Big rally brewing? — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-rise-rs-6400/10g-in-3-days-silver-jumps-rs-13000/kg-despite-middle-east-tensions-big-rally-brewing/articleshow/133393150.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.69] tips_10y_real ↓
- tips_10y_real [RATES]: last 2.35, z20 -3.69, zc -1.66, resid-z -1.10 [moved], 1d -2.49%, 1d move -6.0bps ≥ 5bps; |z20|=3.69
- **Mechanism**: tips_10y_real ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.866 vs tips_10y_real, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.864 vs tips_10y_real, historically leads by 1d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.759 vs tips_10y_real, historically leads by 1d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.725 vs tips_10y_real
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.517 vs tips_10y_real
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-10 (d=0.0), 2025-05-22 (d=0.07)

### [AMBER 6.13] wti ↑
- wti [COMMODITIES]: last 86.42, z20 1.13, zc -0.67, resid-z 0.35 [quiet], 1d -1.61%, 1-session move -1.61% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.351 via wti, z 0.63, quiet)
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.628 vs wti
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.506 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.504 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.351, z 0.63)
- Source: Indian govt bonds hang tight before supply as oil stalls — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/indian-govt-bonds-hang-tight-before-supply-as-oil-stalls/article71372342.ece
- Source: Oil Prices Head for Second Straight Weekly Gain as Iran Risks Mount — OilPrice, 2026-08-21. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Head-for-Second-Straight-Weekly-Gain-as-Iran-Risks-Mount.html
- Source: China Keeps Oil Buying in Check as Crude Prices Stay Above $90 — Mint Markets, 2026-08-21. https://www.livemint.com/market/china-keeps-oil-buying-in-check-as-crude-prices-stay-above-90-11787289773942.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 6.1] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.44, zc 0.65, resid-z 2.57 [unexplained], 1d 0.25%, |z20|=2.44
- aud_usd [FX]: last 0.72, z20 2.43, zc 0.58, resid-z 1.25 [quiet], 1d 0.36%, |z20|=2.43
- gbp_usd [FX]: last 1.37, z20 2.25, zc 0.88, resid-z 1.11 [quiet], 1d 0.38%, |z20|=2.25; 1y-pct=96
- usd_mxn [FX]: last 16.92, z20 -1.77, zc -0.48, resid-z -1.37 [quiet], 1d -0.19%, |z20|=1.77; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.583 via usd_mxn, z 1.61, reacted); nifty_midcap_100 (rho 0.43 via aud_usd, z 0.63, quiet); dyn_icicigi_bo (rho -0.408 via gbp_usd, z -1.15, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.545 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.525 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.583, z 1.61); nifty_midcap_100 (rho 0.43, z 0.63); dyn_icicigi_bo (rho -0.408, z -1.15)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 4.81] commodities · 2 series ↑
- corn [COMMODITIES]: last 500.50, z20 3.98, zc 3.54, resid-z 0.65 [moved], 1d 4.54%, |z20|=3.98; 1y-pct=100
- wheat [COMMODITIES]: last 702.75, z20 2.87, zc 1.69, resid-z 0.12 [moved], 1d 2.93%, |z20|=2.87; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.8] dxy ↓
- dxy [FX]: last 98.73, z20 -1.80, zc -0.49, resid-z -2.52 [unexplained], 1d -0.17%, 20d range extreme; |z20|=1.80
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
dyn_cartrade_ns ↑ (4.42), dyn_lenskart_ns ↑ (4.35), midcap_largecap_ratio ↑ (4.28), dyn_jef ↓ (4.21), dyn_bharatcoal_ns ↑ (4.2), dyn_stylebaaza_ns ↑ (4.0), dyn_icicigi_bo ↓ (3.15), dyn_tech ↑ (2.92), usd_cny ↓ (2.75), eur_inr ↑ (2.55), dyn_lth ↑ (2.44), dyn_tatatech_ns ↑ (2.33)

## India macro
- nifty_50: 24244.3008 (1d 0.05%, z20 -0.40, flag none)
- nifty_midcap_100: 63713.2500 (1d 0.07%, z20 0.63, flag amber)
- usd_inr: 95.7450 (1d 0.26%, z20 0.38, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6280 (1d 0.02%, z20 1.28, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 106.9 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- INOXINDIA.NS (INOX INDIA LIMITED) score 104.1 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 103.5 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- INDIANB.NS (INDIAN BANK) score 97.4 — "Kotak Bank Share Price Live Updates: Kotak Bank Sees Positive Movement Today"
- BOND (PIMCO Active Bond Exchange-Tra) score 81.8 — "HDFC Bank shares gain after record $1.75 billion overseas bond raise. What lies ahead?"
- BAC (Bank of America Corporation) score 77.6 — "Kotak Bank Share Price Live Updates: Kotak Bank Sees Positive Movement Today"
- HDB (HDFC Bank Limited) score 71.7 — "Kotak Bank Share Price Live Updates: Kotak Bank Sees Positive Movement Today"
- IDBI.NS (IDBI BANK LIMITED) score 67.0 — "Kotak Bank Share Price Live Updates: Kotak Bank Sees Positive Movement Today"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 67.0 — "Kotak Bank Share Price Live Updates: Kotak Bank Sees Positive Movement Today"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 66.9 — "Kotak Bank Share Price Live Updates: Kotak Bank Sees Positive Movement Today"
- COIN (Coinbase Global, Inc.) score 57.9 — "Global Market: Nikkei slips as rising oil prices, bond yields weigh on Japanese stocks"
- OHI (Omega Healthcare Investors, In) score 49.2 — "Rs 30,000 cr loss in 3 months: Why BSE stock is failing investors and should you buy now?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.0 — "Sensex today | Stock Market Live: Sensex rises 100 pts after flattish opening, Nifty trade"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 46.7 — "General Atlantic sells 8.75% stake in KFin Technologies for ₹1,400 crore"
- TECH (Bio-Techne Corp) score 46.6 — "General Atlantic sells 8.75% stake in KFin Technologies for ₹1,400 crore"
- CHKP (Check Point Software Technolog) score 41.6 — "Sunshine Pictures IPO GMP signals 20% listing pop. Here's how to check allotment status on"
- LTH (Life Time Group Holdings, Inc.) score 37.6 — "Gaja Alternative Asset Management IPO Day 3: Issue subscribed nearly 2.5 times; GMP at 11%"
- 301077.SZ (CHINASTARS) score 22.4 — "China Keeps Oil Buying in Check as Crude Prices Stay Above $90"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.7 — "These three copper stocks are riding India’s energy expansion. Should you invest?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 21.5 — "Shankesh Jewellers IPO allotment to be finalised today. Latest GMP, step-by-step guide to "
- JIOFIN.BO (Jio Financial Services Limited) score 20.6 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.6 — "Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 16.1 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.3 — "RailTel shares rise 4% after securing Rs 165 crore order from Western Coalfields"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.9 — "Stocks to watch: HAL, RailTel, Tata Motors PV among shares in focus today; check list here"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.9 — "88% retail investors lost money in F&O trading in FY26: Sebi"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.1 — "Stocks to watch: HAL, RailTel, Tata Motors PV among shares in focus today; check list here"
- MS (Morgan Stanley) score 12.0 — "SEBI’s swift ban on JPMorgan unit seen as warning to traders"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.6 — "Adani Power share price: 70% rally in 1 year - What's next for the stock after favourable "
- MRNA (Moderna, Inc.) score 10.1 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- JEF (Jefferies Financial Group Inc.) score 10.0 — "Jefferies initiates coverage on Anthem Biosciences with a Rs 1,050 target"
- META (Meta) score 8.8 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.7 — "Goldman Sachs starts coverage on 14 banks with up to 37% upside potential; ICICI Bank, Kot"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.4 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- VT (Vanguard Total World Stock Ind) score 7.9 — "Beijing Bets on Fossil Fuels Even as It Leads the World in Renewables"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.8 — "Coforge shares jump 3% after IT major launches private equity unit"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.1 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.2 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.4 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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