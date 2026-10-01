# Transmission Layer — board brief · 2026-10-01 18:25Z

data as of **2026-10-01** · 97 series · 18 red / 39 amber · 8 events surfaced (36 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.68, 6d in regime; vol-pct 0.694, breadth-off 0.667, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.43, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.03, corr60 0.15, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.02, corr60 0.11, last shift 2026-08-18. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.76, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.08, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.15, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.43, corr60 0.21, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0032821224683141637)
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.728, β -0.7736, p 0.0); driver zc 2.13 → expected -0.541%. Type hit-rate 0.826 (n=2310).
- Track record · residual_reversion: hit-rate **0.502** (n=1126) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2310) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.65] cross-asset · 3 series ↓
- comex_silver [COMMODITIES]: last 60.96, z20 -1.74, zc 0.77, resid-z 0.58 [quiet], 1d 1.43%, |z20|=1.74; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4201.40, z20 -1.69, zc 0.39, resid-z 0.43 [quiet], 1d 0.35%, |z20|=1.69; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.92, z20 1.33, zc n/a, resid-z n/a [quiet], 1d -1.07%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.351 via gold_silver_ratio, z -1.57, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.589 vs comex_silver, historically leads by 1d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.5 vs comex_silver, historically leads by 5d
- **India receivers**: midcap_largecap_ratio (rho -0.351, z -1.57)
- Source: Gold futures rise to ₹1.50 lakh/10 gm on firm spot demand — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/gold/gold-futures-rise-to-150-lakh10-gm-on-firm-spot-demand/article71532369.ece
- Source: Today’s Gold Rate in India October 1: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-1-2026/article71531990.ece
- Source: Today’s Gold Rate in India October 1: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-1-2026/article71531991.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.89] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.59, z20 2.96, zc 0.66, resid-z 0.33 [quiet], 1d 0.54%, |z20|=2.96; 1y-pct=100
- ust_10y [RATES]: last 5.26, z20 2.17, zc 0.36, resid-z -0.10 [quiet], 1d 0.38%, |z20|=2.17; 1y-pct=100
- tips_10y_real [RATES]: last 2.91, z20 2.11, zc 0.16, resid-z -0.39 [quiet], 1d 0.34%, |z20|=2.11; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.78, z20 -1.99, zc -0.62, resid-z -0.95 [quiet], 1d -0.24%, 1y-pct=0
- ust_2y [RATES]: last 4.89, z20 1.46, zc -0.46, resid-z -1.09 [quiet], 1d -0.61%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.659 vs ust_30y, historically leads by 3d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.504 vs ust_10y, historically leads by 4d
- Watch next: wti (co-move) — not yet - watch; rho 0.503 vs ust_30y, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.538 vs dyn_bond
- Source: This silent alarm in the bond market tells you which stocks to buy and which to avoid — MarketWatch Top, 2026-10-01. https://www.marketwatch.com/story/this-silent-alarm-in-the-bond-market-tells-you-which-stocks-to-buy-and-which-to-avoid-4568ac53?mod=mw_rss_topstories
- Source: Why are world bond markets selling off again? — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/why-are-world-bond-markets-selling-off-again/articleshow/134625028.cms
- Source: FPIs pull out  ₹36,000 cr from Indian equities in Sept as high oil, bond yields weigh — should retail investors worry? — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/fpis-pull-out-rs-36-000-cr-from-indian-equities-in-sept-as-high-oil-bond-yields-weigh-should-retail-investors-worry-11790863175864.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.73] indices · 2 series ↑
- nikkei_225 [INDICES]: last 68986.97, z20 3.89, zc 2.33, resid-z 1.25 [moved], 1d 3.35%, |z20|=3.89
- taiwan_weighted [INDICES]: last 48281.21, z20 1.69, zc 0.67, resid-z -0.15 [quiet], 1d 0.71%, |z20|=1.69; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.423 via taiwan_weighted, z -0.79, quiet); dyn_techm_ns (rho -0.415 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.815 vs nikkei_225
- **India receivers**: nifty_it (rho -0.423, z -0.79); dyn_techm_ns (rho -0.415, z -0.73)
- Source: Global Market: Japan’s Nikkei hits six-week high as chip stocks rally on AI optimism — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-hits-six-week-high-as-chip-stocks-rally-on-ai-optimism/articleshow/134609469.cms
- Source: Global Market: Japan’s Nikkei rises as AI stocks track US chip gains — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-rises-as-ai-stocks-track-us-chip-gains/articleshow/134581624.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 6.72] fx · 4 series ↓
- usd_mxn [FX]: last 18.34, z20 3.06, zc 2.11, resid-z 3.40 [unexplained], 1d 1.64%, |z20|=3.06
- eur_usd [FX]: last 1.12, z20 -2.72, zc -2.90, resid-z -2.94 [unexplained], 1d -0.92%, |z20|=2.72; 1y-pct=0
- aud_usd [FX]: last 0.69, z20 -2.64, zc -1.79, resid-z -2.57 [unexplained], 1d -0.92%, |z20|=2.64
- gbp_usd [FX]: last 1.32, z20 -1.82, zc -0.85, resid-z -0.82 [quiet], 1d -0.32%, |z20|=1.82
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.514 via usd_mxn, z -2.24, reacted); dyn_icicigi_bo (rho -0.502 via gbp_usd, z 1.68, reacted); dyn_muthootfin_ns (rho 0.477 via aud_usd, z -2.12, reacted); nifty_metal (rho 0.449 via aud_usd, z -2.95, reacted); nifty_midcap_100 (rho -0.424 via usd_mxn, z -2.52, reacted)
- **India receivers**: dyn_policybzr_ns (rho -0.514, z -2.24); dyn_icicigi_bo (rho -0.502, z 1.68); dyn_muthootfin_ns (rho 0.477, z -2.12); nifty_metal (rho 0.449, z -2.95)
- Source: UK pound falls to three-month lows as investors fret over rates, oil — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/uk-pound-falls-to-three-month-lows-as-investors-fret-over-rates-oil/articleshow/134621868.cms
- Source: EURO SLIDE CONTINUES; LAST DOWN 0.55% AT $1.127 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36444
- Source: FOREX-Euro slides to 17-month low, hit by rates and inflation cocktail — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/forex-euro-slides-to-17-month-low-hit-by-rates-and-inflation-cocktail/articleshow/134613639.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.37] usd_inr ↑
- usd_inr [FX]: last 96.31, z20 1.37, zc 0.49, resid-z 0.69 [quiet], 1d 0.26%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.355 via usd_inr, z 0.81, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.355, z 0.81)
- Source: RBI set for 50–75 bps rate hike as Rupee, Oil and Global risks mount, says Bandhan Life — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/rbi-set-for-5075-bps-rate-hike-as-rupee-oil-and-global-risks-mount-says-bandhan-life/article71532861.ece
- Source: Rupee drops to two-month low as global bond rout deepens, oil jumps — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-drops-to-two-month-low-as-global-bond-rout-deepens-oil-jumps/articleshow/134615636.cms
- Source: Rupee drops to two-month low of 96.31/$ as global bond rout deepens, oil jumps — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/forex/rupee-drops-to-two-month-low-of-9631-as-global-bond-rout-deepens-oil-jumps/article71532379.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.19] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 22421.95, z20 -2.53, zc -1.36, resid-z -1.21 [quiet], 1d -0.88%, |z20|=2.53; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 58731.25, z20 -2.52, zc -1.06, resid-z -0.50 [quiet], 1d -1.00%, |z20|=2.52
- india_vix [INDICES]: last 14.44, z20 2.46, zc 1.19, resid-z n/a [quiet], 1d 7.01%, |z20|=2.46
- dyn_policybzr_ns [EQUITIES]: last 980.00, z20 -2.24, zc -1.16, resid-z -0.93 [quiet], 1d -7.89%, |z20|=2.24; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.603 via nifty_midcap_100, z -1.57, reacted); nifty_fmcg (rho 0.589 via nifty_50, z -3.71, reacted); dyn_jiofin_bo (rho 0.588 via nifty_50, z -2.93, reacted); nifty_metal (rho 0.525 via nifty_midcap_100, z -2.95, reacted); dyn_indusindbk_bo (rho 0.485 via nifty_midcap_100, z -2.15, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.603, z -1.57); nifty_fmcg (rho 0.589, z -3.71); dyn_jiofin_bo (rho 0.588, z -2.93); nifty_metal (rho 0.525, z -2.95)
- Source: 50% of Nifty stocks slip into bear territory, down up to 40% - What should investors do now? Experts view — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/50-of-nifty-stocks-slip-into-bear-territory-down-up-to-40-what-should-investors-do-now-experts-view-11790873814742.html
- Source: Nifty IT crashes 11% in September: TCS, Infosys, Wipro among top losers — Can Q2 earnings spark a rebound? — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/nifty-it-crashes-11-in-september-tcs-infosys-wipro-among-top-losers-can-q2-earnings-spark-a-rebound-11790851695743.html
- Source: Market wrap: Infosys, HDFC Bank, Bajaj Auto, Maruti Suzuki among top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-infosys-hdfc-bank-bajaj-auto-maruti-suzuki-among-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134617786.cms
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 5.91] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.37, z20 -3.91, zc -1.59, resid-z -0.39 [moved], 1d -2.03%, |z20|=3.91
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: 50% of Nifty stocks slip into bear territory, down up to 40% - What should investors do now? Experts view — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/50-of-nifty-stocks-slip-into-bear-territory-down-up-to-40-what-should-investors-do-now-experts-view-11790873814742.html
- Source: FPIs pull out  ₹36,000 cr from Indian equities in Sept as high oil, bond yields weigh — should retail investors worry? — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/fpis-pull-out-rs-36-000-cr-from-indian-equities-in-sept-as-high-oil-bond-yields-weigh-should-retail-investors-worry-11790863175864.html
- Source: UK pound falls to three-month lows as investors fret over rates, oil — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/uk-pound-falls-to-three-month-lows-as-investors-fret-over-rates-oil/articleshow/134621868.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 5.64] wti ↓
- wti [COMMODITIES]: last 92.98, z20 -0.64, zc 1.05, resid-z 1.64 [unexplained], 1d 2.83%, 1-session move +2.83% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.914 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.562 vs wti
- Source: BLM Opens 35,000 California Acres to December Oil and Gas Lease Sale — OilPrice, 2026-10-01. https://oilprice.com/Latest-Energy-News/World-News/BLM-Opens-35000-California-Acres-to-December-Oil-and-Gas-Lease-Sale.html
- Source: FPIs pull out  ₹36,000 cr from Indian equities in Sept as high oil, bond yields weigh — should retail investors worry? — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/fpis-pull-out-rs-36-000-cr-from-indian-equities-in-sept-as-high-oil-bond-yields-weigh-should-retail-investors-worry-11790863175864.html
- Source: Canada Fast-Tracks 1 Million-Bpd Pacific Link Oil Pipeline to Asia — OilPrice, 2026-10-01. https://oilprice.com/Latest-Energy-News/World-News/Canada-Fast-Tracks-1-Million-Bpd-Pacific-Link-Oil-Pipeline-to-Asia.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

## Watchlist (below surfacing floor)
indices · 4 series ↓ (5.52), dxy ↑ (5.26), commodities · 3 series ↓ (5.2), dyn_jiofin_bo ↓ (4.93), cross-asset · 2 series ↓ (4.92), dyn_stylebaaza_ns ↓ (4.11), rates · 2 series ↑ (3.97), nifty_fmcg ↓ (3.71), dyn_nvda ↑ (3.37), nasdaq_100 ↑ (3.24), dyn_4417_t ↑ (3.1), nifty_metal ↓ (2.95)

## India macro
- nifty_50: 22421.9492 (1d -0.88%, z20 -2.53, flag red)
- nifty_midcap_100: 58731.2500 (1d -1.00%, z20 -2.52, flag red)
- usd_inr: 96.3050 (1d 0.26%, z20 1.37, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6194 (1d -0.12%, z20 -1.57, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 103.1 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- COALINDIA.NS (COAL INDIA LTD) score 97.8 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 96.1 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- INDIANB.NS (INDIAN BANK) score 72.2 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- BOND (PIMCO Active Bond Exchange-Tra) score 63.3 — "FRENCH 5-YEAR CDS HIT 71.6 BPS, HIGHEST SINCE JULY 2013, AS BONDS SELL OFF"
- COIN (Coinbase Global, Inc.) score 57.6 — "U.S. PRESSURES FRANCE AND GERMANY TO RELEASE DIESEL RESERVES The Trump administration has "
- OHI (Omega Healthcare Investors, In) score 52.1 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- TECHM.NS (TECH MAHINDRA LIMITED) score 50.8 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- BAC (Bank of America Corporation) score 50.2 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- HDB (HDFC Bank Limited) score 49.6 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 46.9 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- TECH (Bio-Techne Corp) score 46.9 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- IDBI.NS (IDBI BANK LIMITED) score 45.2 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.2 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.2 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- CHKP (Check Point Software Technolog) score 41.6 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- SEPN (Septerna, Inc.) score 39.7 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.6 — "EU COORDINATES POSSIBLE ENERGY RESERVE RELEASE WITH U.S. The European Commission says it i"
- LTH (Life Time Group Holdings, Inc.) score 35.1 — "SYRIAN OFFICIALS AND HEZBOLLAH MET IN TURKEY LAST MONTH IN FIRST KNOWN MEETING BETWEEN LON"
- TGT (Target Corporation) score 26.2 — "Azad Engineering share price: Up 86% in 6 months! Is more steam left in this defence stock"
- 301077.SZ (CHINASTARS) score 25.9 — "TRUMP ADMINISTRATION HAS BEEN TAKING STEPS TO TURN CHINA'S DEPENDENCE ON US AVIATION SUPPL"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.3 — "Azad Engineering share price: Up 86% in 6 months! Is more steam left in this defence stock"
- BZ=F (Brent Crude Oil Last Day Finan) score 18.6 — "CBOE VOLATILITY INDEX HITS OVER TWO-WEEK HIGH; LAST UP 0.5 POINTS AT 16.86"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.4 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.4 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.8 — "Adani Group has Rs 2.6 lakh crore projects completed or under execution in Maharashtra: Pr"
- JIOFIN.BO (Jio Financial Services Limited) score 12.9 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.1 — "10 microcap stocks slumped up to 32% in just one month. Were they in your portfolio?"
- POLICYBZR.NS (PB FINTECH LIMITED) score 10.9 — "PB Fintech shares crash 48% in 6 sessions; stock back to IPO price - Should investors chan"
- GS (Goldman Sachs Group, Inc. (The) score 10.4 — "GOLDMAN REFRESHES TOP U.S. STOCK PICKS Goldman Sachs added Amazon ($AMZN), Burlington Stor"
- VT (Vanguard Total World Stock Ind) score 9.8 — "Jio Platforms IPO in final stages after concluding worldwide roadshows"
- META (Meta) score 8.6 — "Gold price future roadmap: What led to 6% yellow metal fall in Sept 2026? Will Diwali help"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.7 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- JEF (Jefferies Financial Group Inc.) score 6.5 — "Jefferies is bearish TCS, Wipro, 6 other IT stocks ahead of Q2 results. How many do you ow"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.3 — "FPIs pull out  ₹36,000 cr from Indian equities in Sept as high oil, bond yields weigh — sh"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.9 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- NVDA (NVIDIA Corporation) score 5.8 — "NVIDIA'S HUANG: WE'RE GOING TO ADVANCE THIS RESPONSIBLY AND SAFELY"
- MS (Morgan Stanley) score 4.3 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.2 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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