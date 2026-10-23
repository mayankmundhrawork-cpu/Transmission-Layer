# Transmission Layer — board brief · 2026-10-23 00:03Z

data as of **2026-10-23** · 97 series · 23 red / 36 amber · 8 events surfaced (45 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.794, 14d in regime; vol-pct 0.765, breadth-off 0.824, Markov P(high-vol) 0.054)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.41, contra nifty_50 corr20=0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.21, last shift 2026-08-28. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.12, corr60 0.09, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.78, last shift 2026-09-02. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.25, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.54, corr60 0.26, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0027897744709846073)
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.556, β 0.3414, p 0.0); driver zc -1.7 → expected -0.443%. Type hit-rate 0.822 (n=1907).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.513, β -0.408, p 0.0); driver zc -1.7 → expected 0.53%. Type hit-rate 0.822 (n=1907).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.464, β 0.276, p 0.0); driver zc -1.59 → expected -0.333%. Type hit-rate 0.822 (n=1907).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.446, β -0.344, p 0.0); driver zc -1.59 → expected 0.416%. Type hit-rate 0.822 (n=1907).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.438, β 0.1906, p 0.0); driver zc -2.25 → expected -0.549%. Type hit-rate 0.822 (n=1907).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.431, β -0.0293, p 0.0); driver zc 1.71 → expected -0.415%. Type hit-rate 0.822 (n=1907).
- **SETUP** vix → usd_brl: leads 1d (ccf 0.427, β 0.0378, p 0.0); driver zc 1.71 → expected 0.534%. Type hit-rate 0.822 (n=1907).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.424, β -0.1767, p 0.0); driver zc -2.25 → expected 0.509%. Type hit-rate 0.822 (n=1907).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.423, β -0.2388, p 0.0); driver zc -2.25 → expected 0.688%. Type hit-rate 0.822 (n=1907).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.371, β -2.4509, p 0.00768); driver zc -1.7 → expected 3.184%. Type hit-rate 0.822 (n=1907).
- **SETUP** vix → india_vix: leads 1d (ccf 0.344, β 0.2288, p 0.0127); driver zc 1.71 → expected 3.237%. Type hit-rate 0.822 (n=1907).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.343, β 0.0765, p 0.0); driver zc -1.98 → expected -0.334%. Type hit-rate 0.822 (n=1907).
- **SETUP** sp500 → india_vix: leads 1d (ccf -0.338, β -2.1804, p 0.01657); driver zc -1.59 → expected 2.634%. Type hit-rate 0.822 (n=1907).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.326, β 0.1433, p 1e-05); driver zc -1.7 → expected -0.186%. Type hit-rate 0.822 (n=1907).
- Track record · residual_reversion: hit-rate **0.495** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=1907) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.69] commodities · 2 series ↑
- brent [COMMODITIES]: last 113.23, z20 2.86, zc 2.21, resid-z -0.21 [priced], 1d 4.05%, 1-session move +4.05% ≥ 1.5%; |z20|=2.86; 1y-pct=98
- wti [COMMODITIES]: last 99.32, z20 1.25, zc 0.79, resid-z -0.78 [quiet], 1d 2.23%, 1-session move +2.23% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.539 vs brent, historically leads by 5d
- Source: Rising Crude Oil Imports Reduce China’s Need to Draw from Stocks — OilPrice, 2026-10-22. https://oilprice.com/Energy/Energy-General/Rising-Crude-Oil-Imports-Reduce-Chinas-Need-to-Draw-from-Stocks.html
- Source: EU’s Arctic Strategy Excludes Oil and Gas — OilPrice, 2026-10-22. https://oilprice.com/Energy/Natural-Gas/EUs-Arctic-Strategy-Excludes-Oil-and-Gas.html
- Source: Oil Tankers Sailing the US-China Route Are Commanding $60 Million and It’s Crushing Demand — Mint Markets, 2026-10-22. https://www.livemint.com/market/oil-tankers-sailing-the-us-china-route-are-commanding-60-million-and-it-s-crushing-demand-11792703194471.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 8.2] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4037.80, z20 -3.00, zc -2.69, resid-z -0.07 [priced], 1d -2.70%, |z20|=3.00; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.58, z20 -2.33, zc -2.19, resid-z -0.65 [priced], 1d -4.94%, |z20|=2.33; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 73.97, z20 1.88, zc n/a, resid-z n/a [quiet], 1d 2.35%, GSR<75 (extreme low); |z20|=1.88
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: TSX falls 1% as tech and gold mining shares slide — Mint Markets, 2026-10-22. https://www.livemint.com/market/tsx-falls-1-as-tech-and-gold-mining-shares-slide-11792700912983.html
- Source: SPOT SILVER EXTENDS LOSSES, DOWN NEARLY 5% AT $55.17/OZ — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37441
- Source: Silver crashes  ₹8,590/kg to a 7-month low; gold hits 2-month low. What’s driving the selloff in precious metals — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/silver-crashes-rs-8-590-per-kilo-to-7-month-low-gold-hits-2-month-low-what-s-driving-the-selloff-in-precious-metals-11792676479559.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.27] usd_inr ↓
- usd_inr [FX]: last 94.31, z20 -2.27, zc -0.81, resid-z -0.30 [quiet], 1d -0.43%, 20d range extreme; |z20|=2.27
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.38 via usd_inr, z -2.03, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.38, z -2.03)
- Source: Rupee snaps eight-day run, crude tops $112 as Nifty falls for third straight day — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/rupee-snaps-eight-day-run-crude-tops-112-as-nifty-falls-for-third-straight-day/article71611785.ece
- Source: Rupee snaps eight-day rally as oil climbs to highest since May — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-snaps-eight-day-rally-as-oil-climbs-to-highest-since-may/articleshow/135115702.cms
- Source: Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/jio-platforms-ipo-impact-on-rupee-11792645448827.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.34] usd_jpy ↓
- usd_jpy [FX]: last 156.37, z20 -4.34, zc -2.43, resid-z 0.27 [moved], 1d -1.11%, |z20|=4.34
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Yen jumps as oil, AI and France worries rattle markets — Mint Markets, 2026-10-22. https://www.livemint.com/market/yen-jumps-as-oil-ai-and-france-worries-rattle-markets-11792694662480.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [RED 6.21] cross-asset · 4 series ↓
- nasdaq_100 [INDICES]: last 28962.86, z20 -2.55, zc -2.25, resid-z 0.40 [priced], 1d -2.88%, |z20|=2.55
- vix [INDICES]: last 19.04, z20 2.31, zc 1.71, resid-z n/a [moved], 1d 14.15%, |z20|=2.31
- dyn_vt [EQUITIES]: last 156.53, z20 -2.17, zc -1.70, resid-z -0.15 [priced], 1d -1.30%, |z20|=2.17
- dyn_nvda [EQUITIES]: last 212.28, z20 -2.03, zc -1.98, resid-z 0.74 [priced], 1d -4.36%, |z20|=2.03
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-04 (z-distance 0.21).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho 0.414 via dyn_nvda, z -2.27, reacted)
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.598 vs nasdaq_100, historically leads by 2d
- Watch next: dax (co-move) — not yet - watch; rho 0.617 vs dyn_vt
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.597 vs nasdaq_100
- **India receivers**: usd_inr (rho 0.414, z -2.27)
- Source: US stocks today: Nasdaq slumps 2.5%, S&P 1% as revived AI doubts ignite tech selloff — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-slumps-2-5-sp-1-as-revived-ai-doubts-ignite-tech-selloff/articleshow/135127224.cms
- Source: US stocks today: US stocks slide as AI spending jitters hit Nasdaq, oil prices rebound — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-lower-as-ai-jitters-return-oil-rises/articleshow/135120582.cms
- Source: U.S. STOCKS EXTEND FALL, NASDAQ DOWN 1.55% — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37431
- Historical analogues: 2026-05-04 (d=0.21), 2025-04-28 (d=0.28), 2025-08-28 (d=0.3)

### [RED 6.12] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 152.00, z20 4.12, zc 2.65, resid-z 0.74 [moved], 1d 5.98%, |z20|=4.12
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.409 via dyn_chkp, z -1.32, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.409, z -1.32)
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

## Watchlist (below surfacing floor)
cross-asset · 3 series ↓ (5.39), indices · 3 series ↓ (5.33), cross-asset · 2 series ↑ (5.33), dyn_bond ↑ (5.17), dyn_wit ↑ (4.81), comex_copper ↓ (4.65), natgas ↓ (4.63), dow_jones ↑ (4.52), dyn_sepn ↑ (4.34), dyn_4417_t ↑ (4.25), dyn_coalindia_ns ↓ (4.21), dyn_301077_sz ↓ (3.9)

## India macro
- nifty_50: 22687.6504 (1d -0.54%, z20 -0.32, flag amber)
- nifty_midcap_100: 57062.1484 (1d -0.88%, z20 -2.08, flag amber)
- usd_inr: 94.3123 (1d -0.43%, z20 -2.27, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5151 (1d -0.34%, z20 -2.85, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 92.0 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.4 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.6 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- INDIANB.NS (INDIAN BANK) score 79.8 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- BAC (Bank of America Corporation) score 70.1 — "Americans are having fewer babies — and pampering them with luxury diapers"
- HDB (HDFC Bank Limited) score 61.8 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- IDBI.NS (IDBI BANK LIMITED) score 60.0 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.0 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.0 — "Treasury yields log biggest drop since the 2023 banking crisis. Here’s what’s going on."
- OHI (Omega Healthcare Investors, In) score 57.1 — "Moderna’s cancer vaccine hits its targets, but a data leak rattled investors and the stock"
- COIN (Coinbase Global, Inc.) score 53.0 — "EBAY SHARES UP 1.6% PREMARKET AFTER CO SAYS WILL REDUCE GLOBAL WORKFORCE BY ABOUT 9%"
- TECHM.NS (TECH MAHINDRA LIMITED) score 52.8 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq slumps 2.5%, S&P 1"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq slumps 2.5%, S&P 1"
- TECH (Bio-Techne Corp) score 49.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq slumps 2.5%, S&P 1"
- TGT (Target Corporation) score 47.1 — "Moderna’s cancer vaccine hits its targets, but a data leak rattled investors and the stock"
- CHKP (Check Point Software Technolog) score 43.9 — "Ola Electric rights issue opens today: Who are the investors applying for 2.39 crore entit"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq crashes 3% as AI"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.9 — "Oil prices approach Iran-war highs as soaring tanker rates trigger a second energy squeeze"
- RS (Reliance, Inc.) score 28.7 — "Reliance Industries shares: Monarch sees 20% upside in 3–4 months - Reveals buy range, tar"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 27.4 — "Shoppers Stop shares deliver almost no returns in 10 years; Experts decode the road ahead "
- LTH (Life Time Group Holdings, Inc.) score 26.1 — "YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN"
- 301077.SZ (CHINASTARS) score 25.2 — "Oil Tankers Sailing the US-China Route Are Commanding $60 Million and It’s Crushing Demand"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.1 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- META (Meta) score 17.7 — "META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS -"
- JIOFIN.BO (Jio Financial Services Limited) score 17.4 — "Young Americans are giving up their cars. It’s a path to financial freedom, for some."
- BZ=F (Brent Crude Oil Last Day Finan) score 17.3 — "YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.2 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- SEPN (Septerna, Inc.) score 15.3 — "YIELD ON 10-YEAR TREASURY NOTE FALLS BELOW 5% FOR FIRST TIME SINCE SEPTEMBER 23, LAST DOWN"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.7 — "Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.9 — "Q2 Results Today Highlights: Q2 Results Live: Adani Energy PAT surges 145%, CPCL profit tr"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.5 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.5 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- JEF (Jefferies Financial Group Inc.) score 10.1 — "KEI Industries shares: Down 15% in one month! Jefferies India sees 45% upside after Q2 res"
- GS (Goldman Sachs Group, Inc. (The) score 9.7 — "GOLDMAN SACHS: AI COULD TEMPORARILY DISPLACE 9% OF WORKERS Goldman Sachs estimates that a "
- VT (Vanguard Total World Stock Ind) score 6.0 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- WIT (Wipro Limited) score 5.8 — "IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 "
- NVDA (NVIDIA Corporation) score 5.6 — "NVIDIA MAY ALSO BE A BIDDER FOR AMBARELLA ( $AMBA ) - BETAVILLE"
- ETERNAL.NS (ETERNAL LIMITED) score 5.5 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
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