# Transmission Layer — board brief · 2026-10-22 23:20Z

data as of **2026-10-22** · 97 series · 22 red / 38 amber · 8 events surfaced (46 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.794, 14d in regime; vol-pct 0.765, breadth-off 0.824, Markov P(high-vol) 0.053)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.41, contra nifty_50 corr20=0.4, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.21, last shift 2026-08-27. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.12, corr60 0.09, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.25, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.54, corr60 0.25, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0008081156037280657)
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.557, β 0.343, p 0.0); driver zc -1.7 → expected -0.446%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.512, β -0.4072, p 0.0); driver zc -1.7 → expected 0.529%. Type hit-rate 0.823 (n=1848).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.465, β 0.2773, p 0.0); driver zc -1.6 → expected -0.335%. Type hit-rate 0.823 (n=1848).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.446, β -0.3432, p 0.0); driver zc -1.6 → expected 0.415%. Type hit-rate 0.823 (n=1848).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.441, β 0.1925, p 0.0); driver zc -2.26 → expected -0.555%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.432, β -0.0295, p 0.0); driver zc 1.71 → expected -0.417%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → usd_brl: leads 1d (ccf 0.427, β 0.0377, p 0.0); driver zc 1.71 → expected 0.534%. Type hit-rate 0.823 (n=1848).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.422, β -0.2379, p 0.0); driver zc -2.26 → expected 0.686%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.368, β -2.4319, p 0.00818); driver zc -1.7 → expected 3.159%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.345, β 0.0771, p 0.0); driver zc -1.99 → expected -0.336%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → india_vix: leads 1d (ccf 0.343, β 0.2279, p 0.01301); driver zc 1.71 → expected 3.224%. Type hit-rate 0.823 (n=1848).
- **SETUP** sp500 → india_vix: leads 1d (ccf -0.335, β -2.1617, p 0.01751); driver zc -1.6 → expected 2.612%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.329, β 0.145, p 1e-05); driver zc -1.7 → expected -0.188%. Type hit-rate 0.823 (n=1848).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.287, β 0.063, p 0.0); driver zc -1.75 → expected -0.209%. Type hit-rate 0.823 (n=1848).
- Track record · residual_reversion: hit-rate **0.494** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=1848) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.54] commodities · 2 series ↑
- brent [COMMODITIES]: last 112.80, z20 2.71, zc 1.99, resid-z -0.34 [priced], 1d 3.66%, 1-session move +3.66% ≥ 1.5%; |z20|=2.71; 1y-pct=98
- wti [COMMODITIES]: last 99.04, z20 1.19, zc 0.69, resid-z -0.86 [quiet], 1d 1.95%, 1-session move +1.95% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.542 vs brent, historically leads by 5d
- Source: Rising Crude Oil Imports Reduce China’s Need to Draw from Stocks — OilPrice, 2026-10-22. https://oilprice.com/Energy/Energy-General/Rising-Crude-Oil-Imports-Reduce-Chinas-Need-to-Draw-from-Stocks.html
- Source: EU’s Arctic Strategy Excludes Oil and Gas — OilPrice, 2026-10-22. https://oilprice.com/Energy/Natural-Gas/EUs-Arctic-Strategy-Excludes-Oil-and-Gas.html
- Source: Oil Tankers Sailing the US-China Route Are Commanding $60 Million and It’s Crushing Demand — Mint Markets, 2026-10-22. https://www.livemint.com/market/oil-tankers-sailing-the-us-china-route-are-commanding-60-million-and-it-s-crushing-demand-11792703194471.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 8.17] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4040.30, z20 -2.95, zc -2.63, resid-z -0.07 [priced], 1d -2.64%, |z20|=2.95; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.67, z20 -2.30, zc -2.14, resid-z -0.61 [priced], 1d -4.80%, |z20|=2.30; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 73.91, z20 1.85, zc n/a, resid-z n/a [quiet], 1d 2.27%, GSR<75 (extreme low); |z20|=1.85
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.5 vs comex_gold
- Source: TSX falls 1% as tech and gold mining shares slide — Mint Markets, 2026-10-22. https://www.livemint.com/market/tsx-falls-1-as-tech-and-gold-mining-shares-slide-11792700912983.html
- Source: SPOT SILVER EXTENDS LOSSES, DOWN NEARLY 5% AT $55.17/OZ — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37441
- Source: Silver crashes  ₹8,590/kg to a 7-month low; gold hits 2-month low. What’s driving the selloff in precious metals — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/silver-crashes-rs-8-590-per-kilo-to-7-month-low-gold-hits-2-month-low-what-s-driving-the-selloff-in-precious-metals-11792676479559.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.27] usd_inr ↓
- usd_inr [FX]: last 94.31, z20 -2.27, zc -0.81, resid-z -0.27 [quiet], 1d -0.43%, 20d range extreme; |z20|=2.27
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.378 via usd_inr, z -2.03, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.378, z -2.03)
- Source: Rupee snaps eight-day run, crude tops $112 as Nifty falls for third straight day — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/rupee-snaps-eight-day-run-crude-tops-112-as-nifty-falls-for-third-straight-day/article71611785.ece
- Source: Rupee snaps eight-day rally as oil climbs to highest since May — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-snaps-eight-day-rally-as-oil-climbs-to-highest-since-may/articleshow/135115702.cms
- Source: Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/jio-platforms-ipo-impact-on-rupee-11792645448827.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.21] cross-asset · 4 series ↓
- nasdaq_100 [INDICES]: last 28962.86, z20 -2.55, zc -2.26, resid-z 0.40 [priced], 1d -2.88%, |z20|=2.55
- vix [INDICES]: last 19.04, z20 2.31, zc 1.71, resid-z n/a [moved], 1d 14.15%, |z20|=2.31
- dyn_vt [EQUITIES]: last 156.53, z20 -2.17, zc -1.70, resid-z -0.15 [priced], 1d -1.30%, |z20|=2.17
- dyn_nvda [EQUITIES]: last 212.28, z20 -2.03, zc -1.99, resid-z 0.74 [priced], 1d -4.36%, |z20|=2.03
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-04 (z-distance 0.21).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho 0.391 via dyn_nvda, z -2.27, reacted)
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.601 vs nasdaq_100, historically leads by 2d
- Watch next: dax (co-move) — not yet - watch; rho 0.617 vs dyn_vt
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.575 vs nasdaq_100
- **India receivers**: usd_inr (rho 0.391, z -2.27)
- Source: US stocks today: Nasdaq slumps 2.5%, S&P 1% as revived AI doubts ignite tech selloff — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-slumps-2-5-sp-1-as-revived-ai-doubts-ignite-tech-selloff/articleshow/135127224.cms
- Source: US stocks today: US stocks slide as AI spending jitters hit Nasdaq, oil prices rebound — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-lower-as-ai-jitters-return-oil-rises/articleshow/135120582.cms
- Source: U.S. STOCKS EXTEND FALL, NASDAQ DOWN 1.55% — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37431
- Historical analogues: 2026-05-04 (d=0.21), 2025-04-28 (d=0.28), 2025-08-28 (d=0.3)

### [RED 6.12] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 152.00, z20 4.12, zc 2.64, resid-z 0.74 [moved], 1d 5.98%, |z20|=4.12
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.407 via dyn_chkp, z -1.32, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.407, z -1.32)
- Source: Reliance Jio IPO subscription status day 1, day 2: Check QIB, NII, Retail, Employee, RIL Shareholders wise data details — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/reliance-jio-ipo-subscription-status-day-1-day-2-check-qib-nii-retail-employee-ril-shareholders-wise-data-details-11792681049708.html
- Source: Coal India Q2 results 2026 date, dividend announcement news: Check Maharatna PSU's earnings schedule, preview, yield — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/coal-india-q2-results-2026-date-dividend-announcement-news-check-maharatna-psus-earnings-schedule-preview-yield-11792676595483.html
- Source: 163% return in 3 years! This AMC declares  ₹9.50 dividend despite 6% profit dip- Do you own? Check record date — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/163-return-in-3-years-this-amc-declares-rs-9-50-dividend-despite-6-profit-dip-do-you-own-check-record-date-11792672553645.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [RED 6.09] dyn_lth ↑
- dyn_lth [EQUITIES]: last 41.98, z20 4.09, zc 1.36, resid-z -0.53 [quiet], 1d 2.99%, |z20|=4.09
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN 14.97 BASIS POINTS AT 4.996% — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37445
- Source: FRENCH 5-YEAR CDS RISE ABOVE 100 BPS, FIRST TIME SINCE OCTOBER 2012, LAST AT 97.75 BPS, LSEG DATA SHOWS — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37440
- Source: META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS - MARKIT DATA — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37429
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 5.97] dyn_meta ↓
- dyn_meta [EQUITIES]: last 648.91, z20 -3.97, zc -2.87, resid-z -0.12 [moved], 1d -6.97%, |z20|=3.97
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta share price: Stock slumps 7.5% despite upbeat Q3 results; why is Facebook parent falling? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/meta-share-price-stock-slumps-7-5-despite-upbeat-q3-results-why-is-facebook-parent-falling-11792689825393.html
- Source: Zuckerberg’s California tax move is a win for Meta — and for him — MarketWatch Top, 2026-10-22. https://www.marketwatch.com/story/zuckerbergs-california-tax-move-is-a-win-for-meta-and-for-him-aa049c94?mod=mw_rss_topstories
- Source: META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS - MARKIT DATA — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37429
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [RED 5.82] usd_jpy ↓
- usd_jpy [FX]: last 156.57, z20 -3.82, zc -2.26, resid-z -1.60 [unexplained], 1d -1.08%, |z20|=3.82
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Yen jumps as oil, AI and France worries rattle markets — Mint Markets, 2026-10-22. https://www.livemint.com/market/yen-jumps-as-oil-ai-and-france-worries-rattle-markets-11792694662480.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

## Watchlist (below surfacing floor)
indices · 3 series ↓ (5.33), cross-asset · 2 series ↑ (5.33), dyn_bond ↑ (5.17), indices · 2 series ↓ (4.91), dyn_wit ↑ (4.81), natgas ↓ (4.62), comex_copper ↓ (4.61), dow_jones ↑ (4.52), dyn_sepn ↑ (4.34), dyn_4417_t ↑ (4.31), dyn_coalindia_ns ↓ (4.21), dyn_301077_sz ↓ (3.9)

## India macro
- nifty_50: 22687.6504 (1d -0.54%, z20 -0.32, flag amber)
- nifty_midcap_100: 57062.1484 (1d -0.88%, z20 -2.08, flag amber)
- usd_inr: 94.3123 (1d -0.43%, z20 -2.27, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5151 (1d -0.34%, z20 -2.85, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 92.7 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 91.1 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.2 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- INDIANB.NS (INDIAN BANK) score 80.3 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- BAC (Bank of America Corporation) score 70.6 — "Americans are having fewer babies — and pampering them with luxury diapers"
- HDB (HDFC Bank Limited) score 62.2 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- IDBI.NS (IDBI BANK LIMITED) score 60.4 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.4 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.4 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- OHI (Omega Healthcare Investors, In) score 57.5 — "Moderna’s cancer vaccine hits its targets, but a data leak rattled investors and the stock"
- COIN (Coinbase Global, Inc.) score 53.4 — "EBAY SHARES UP 1.6% PREMARKET AFTER CO SAYS WILL REDUCE GLOBAL WORKFORCE BY ABOUT 9%"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq slumps 2.5%, S&P 1"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.5 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq slumps 2.5%, S&P 1"
- TECH (Bio-Techne Corp) score 49.5 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq slumps 2.5%, S&P 1"
- TGT (Target Corporation) score 47.4 — "Moderna’s cancer vaccine hits its targets, but a data leak rattled investors and the stock"
- CHKP (Check Point Software Technolog) score 44.2 — "Ola Electric rights issue opens today: Who are the investors applying for 2.39 crore entit"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.4 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq crashes 3% as AI"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.1 — "Oil prices approach Iran-war highs as soaring tanker rates trigger a second energy squeeze"
- RS (Reliance, Inc.) score 28.9 — "Reliance Industries shares: Monarch sees 20% upside in 3–4 months - Reveals buy range, tar"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 27.6 — "Shoppers Stop shares deliver almost no returns in 10 years; Experts decode the road ahead "
- LTH (Life Time Group Holdings, Inc.) score 26.3 — "YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN"
- 301077.SZ (CHINASTARS) score 25.4 — "Oil Tankers Sailing the US-China Route Are Commanding $60 Million and It’s Crushing Demand"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.2 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- META (Meta) score 17.8 — "META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS -"
- JIOFIN.BO (Jio Financial Services Limited) score 17.6 — "Young Americans are giving up their cars. It’s a path to financial freedom, for some."
- BZ=F (Brent Crude Oil Last Day Finan) score 17.4 — "YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.3 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- SEPN (Septerna, Inc.) score 15.4 — "YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.8 — "Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.0 — "Q2 Results Today Highlights: Q2 Results Live: Adani Energy PAT surges 145%, CPCL profit tr"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.6 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.6 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- JEF (Jefferies Financial Group Inc.) score 10.2 — "KEI Industries shares: Down 15% in one month! Jefferies India sees 45% upside after Q2 res"
- GS (Goldman Sachs Group, Inc. (The) score 9.8 — "GOLDMAN SACHS: AI COULD TEMPORARILY DISPLACE 9% OF WORKERS Goldman Sachs estimates that a "
- VT (Vanguard Total World Stock Ind) score 6.1 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- WIT (Wipro Limited) score 5.8 — "IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 "
- NVDA (NVIDIA Corporation) score 5.7 — "NVIDIA MAY ALSO BE A BIDDER FOR AMBARELLA ( $AMBA ) - BETAVILLE"
- ETERNAL.NS (ETERNAL LIMITED) score 5.6 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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