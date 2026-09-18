# Transmission Layer — board brief · 2026-09-18 19:03Z

data as of **2026-09-18** · 97 series · 11 red / 36 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.435, 2d in regime; vol-pct 0.223, breadth-off 0.647, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.25, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.87, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.34, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 0.1, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.83, last shift 2026-07-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.07, last shift 2026-07-28. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.4, corr60 0.15, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **7 of 89** scanned series survive multiplicity control (effective p ≤ 0.0063334325547157455)
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.305, β 0.0869, p 0.0); driver zc 2.72 → expected 0.511%. Type hit-rate 0.819 (n=2014).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.273, β 0.278, p 0.02151); driver zc -1.81 → expected -0.416%. Type hit-rate 0.819 (n=2014).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.263, β -0.058, p 1e-05); driver zc 2.72 → expected -0.341%. Type hit-rate 0.819 (n=2014).
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.262, β 0.1962, p 0.00745); driver zc -1.66 → expected -0.287%. Type hit-rate 0.819 (n=2014).
- **SETUP** dax → asx_200: leads 1d (ccf 0.259, β 0.1869, p 0.00502); driver zc -1.96 → expected -0.304%. Type hit-rate 0.819 (n=2014).
- Track record · residual_reversion: hit-rate **0.499** (n=1101) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2014) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 12.75] sofr ↑
- sofr [RATES]: last 3.85, z20 12.75, zc 9.57, resid-z 9.91 [unexplained], 1d 6.35%, |z20|=12.75
- **Mechanism**: sofr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-06 (d=0.0), 2025-04-17 (d=0.0)

### [RED 9.7] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.68, z20 2.77, zc 1.33, resid-z 0.46 [quiet], 1d 2.29%, 1d move +6.0bps ≥ 5bps; |z20|=2.77; 1y-pct=100
- ust_2y [RATES]: last 4.74, z20 2.41, zc 1.15, resid-z 0.04 [quiet], 1d 1.50%, |z20|=2.41; 1y-pct=100
- ust_10y [RATES]: last 5.01, z20 2.12, zc 0.21, resid-z -0.58 [quiet], 1d 0.20%, |z20|=2.12; 1y-pct=100
- ust_30y [RATES]: last 5.35, z20 1.57, zc -0.24, resid-z -0.64 [quiet], 1d -0.19%, |z20|=1.57; 1y-pct=98
- dyn_bond [EQUITIES]: last 88.75, z20 -1.42, zc -1.12, resid-z 0.19 [quiet], 1d -0.39%, 1y-pct=1
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.423 via ust_2y, z 1.41, reacted)
- Watch next: brent (co-move) — not yet - watch; rho 0.637 vs ust_10y
- Watch next: wti (co-move) — not yet - watch; rho 0.619 vs ust_10y
- Watch next: sp500 (co-move) — not yet - watch; rho 0.544 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.423, z 1.41)
- Source: Global Markets: French bond spread at highest since 2012 as default insurance spikes — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-french-bond-spread-at-highest-since-2012-as-default-insurance-spikes/articleshow/134338977.cms
- Source: US Treasury yields rise as investors weigh outlook for rate hikes — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/news/us-treasury-yields-rise-as-investors-weigh-outlook-for-rate-hikes/articleshow/134338963.cms
- Source: Wall Street mixed amid lower oil prices and higher Treasury yields — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/wall-street-mixed-amid-lower-oil-prices-and-higher-treasury-yields-11789740109962.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.83] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2613.33, z20 4.00, zc 1.74, resid-z 1.91 [unexplained], 1d 6.79%, |z20|=4.00
- btc_usd [CRYPTO]: last 80898.78, z20 2.00, zc 2.72, resid-z 2.57 [unexplained], 1d 5.88%, |z20|=2.00
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-05-09 (z-distance 0.11).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.483 via btc_usd, z -0.73, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.615 vs btc_usd
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.599 vs eth_usd
- **India receivers**: dyn_cartrade_ns (rho 0.483, z -0.73)
- Source: Bitcoin vs Ethereum vs Solana: Which crypto asset is best positioned for the next bull run? — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-vs-ethereum-vs-solana-which-crypto-asset-is-best-positioned-for-the-next-bull-run/articleshow/134336948.cms
- Source: Bitcoin holds near $77K despite hawkish Fed, CLARITY Act setback and weak ETF demand. Here is what experts say — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-77k-despite-hawkish-fed-clarity-act-setback-and-weak-etf-demand-here-is-what-experts-say/articleshow/134330927.cms
- Source: BITCOIN COULD GET MORE SUPPORT THAN GOLD JPMorgan says Bitcoin could benefit more than gold if ETF hedging demand eases. Short interest in IBIT remains near yearly highs, while its put-to-call ratio is also higher than GLD’s — signaling heavier Bitcoin hedging. If those hedges unwind, JPMorgan sees  — DeItaone, 2026-09-17. https://t.me/walter_bloomberg/35890
- Historical analogues: 2025-05-09 (d=0.11), 2025-08-12 (d=0.24), 2025-07-16 (d=0.42)

### [AMBER 6.24] commodities · 2 series ↑
- wti [COMMODITIES]: last 95.51, z20 0.41, zc -2.13, resid-z -2.15 [unexplained], 1d -6.28%, 1-session move -6.28% ≥ 1.5%
- brent [COMMODITIES]: last 98.70, z20 0.19, zc -2.22, resid-z -2.02 [unexplained], 1d -5.84%, 1-session move -5.84% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.584 vs wti
- Source: Gold rises to one-week high, heads for weekly gain on easing oil prices — Mint Markets, 2026-09-18. https://www.livemint.com/market/gold-rises-to-one-week-high-heads-for-weekly-gain-on-easing-oil-prices-11789756221619.html
- Source: Saudi Arabia Cuts Europe Off From October Crude as Gulf Exports Surge — OilPrice, 2026-09-18. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Cuts-Europe-Off-From-October-Crude-as-Gulf-Exports-Surge.html
- Source: U.S. Oil, Gas Rig Count Creeps Up With Strong Prices — OilPrice, 2026-09-18. https://oilprice.com/Energy/Energy-General/US-Oil-Gas-Rig-Count-Creeps-Up-With-Strong-Prices.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.51] cross-asset · 3 series ↓
- dyn_ms [EQUITIES]: last 202.48, z20 -2.20, zc -0.28, resid-z -0.58 [quiet], 1d -0.51%, |z20|=2.20
- russell_2000 [INDICES]: last 2855.28, z20 -1.81, zc -0.59, resid-z -1.23 [quiet], 1d -0.67%, |z20|=1.81
- dow_jones [INDICES]: last 51702.66, z20 -1.80, zc -0.17, resid-z -1.77 [unexplained], 1d -0.15%, |z20|=1.80
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.664 vs dow_jones, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.639 vs dow_jones, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.738 vs dyn_ms
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.527 vs dyn_ms, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.643 vs dyn_ms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: S&P 500, Nasdaq open higher as oil prices fall — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-xenon-pharmaceuticals-berkshire-hathaway-alphabet-apple-stock-price-news-18th-september-2026/liveblog/134335091.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks slip as higher Treasury yields weigh on sentiment — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-xenon-pharmaceuticals-berkshire-hathaway-alphabet-apple-stock-price-news-18th-september-2026/liveblog/134335091.cms
- Source: JP MORGAN EXPECTS ECB TO DELIVER ANOTHER 25 BP INTEREST RATE HIKE IN MARCH 2027 AFTER A DECEMBER HIKE VS PRIOR FORECAST OF RATES ON HOLD IN 2027 — DeItaone, 2026-09-18. https://t.me/walter_bloomberg/35894
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-27 (d=0.32), 2024-10-18 (d=0.52)

### [RED 5.13] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.92, z20 -2.13, zc n/a, resid-z n/a [quiet], 1d -1.90%, GSR<75 (extreme low); |z20|=2.13
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.391 via gold_silver_ratio, z -0.82, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.866 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.391, z -0.82)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 4.91] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 722.45, z20 -2.91, zc -2.53, resid-z -2.09 [unexplained], 1d -4.78%, |z20|=2.91
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.495 via dyn_tatatech_ns, z -1.61, reacted); dyn_tataelxsi_ns (rho 0.473 via dyn_tatatech_ns, z -2.28, reacted); dyn_techm_ns (rho 0.397 via dyn_tatatech_ns, z -1.3, reacted)
- **India receivers**: nifty_it (rho 0.495, z -1.61); dyn_tataelxsi_ns (rho 0.473, z -2.28); dyn_techm_ns (rho 0.397, z -1.3)
- Source: Tata feud wipes  ₹52,154 crore off listed companies’ market value — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tata-feud-wipes-52-154-crore-off-listed-companies-market-value-11789737927529.html
- Source: TCS, Tata Chemicals, Tata Steel to Tata Motors PV — Tata Group stock lost 46,600 crores in a single day — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tcs-tata-chemicals-tata-steel-to-tata-motors-pv-tata-group-stock-lost-46-600-crores-in-a-single-day-11789728923950.html
- Source: Sensex, Nifty extend losses to 6th week, crude moderation offers little relief, IT & Tata group stocks weigh — BusinessLine Mkts, 2026-09-18. https://www.thehindubusinessline.com/markets/sensex-nifty-extend-losses-to-6th-week-crude-moderation-offers-little-relief-it-tata-group-stocks-weigh/article71480356.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.28 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Tata Sons listing: Tata Chemicals vs Tata Steel vs Tata Power — Which Tata Group stocks may benefit most? Experts decode — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tata-sons-listing-tata-chemicals-vs-tata-steel-vs-tata-power-which-tata-group-stocks-may-benefit-most-experts-decode-11789722802716.html
- Source: Bitcoin holds near $77K despite hawkish Fed, CLARITY Act setback and weak ETF demand. Here is what experts say — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-77k-despite-hawkish-fed-clarity-act-setback-and-weak-etf-demand-here-is-what-experts-say/articleshow/134330927.cms
- Source: Nifty prediction, target 2026: Bulls to help investors for 27,000 in 2026? What experts said — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/stock-market-prediction-bulls-may-fancy-nifty-50-hitting-27-000-in-cy2026-heres-how-11789712187213.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_bac ↓ (4.54), midcap_largecap_ratio ↑ (4.41), dyn_tataelxsi_ns ↓ (4.28), dyn_jef ↓ (4.2), usd_cny ↓ (4.18), dyn_lenskart_ns ↑ (4.07), dyn_voltas_ns ↓ (3.93), fx · 2 series ↓ (3.31), indices · 3 series ↓ (3.23), comex_copper ↑ (3.11), usd_mxn ↑ (2.78), dyn_tech ↑ (2.76)

## India macro
- nifty_50: 23346.4004 (1d 0.33%, z20 -1.28, flag none)
- nifty_midcap_100: 62189.1016 (1d 1.23%, z20 -0.82, flag none)
- usd_inr: 95.8630 (1d -0.28%, z20 1.06, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6638 (1d 0.90%, z20 1.41, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.6 — "Indian cotton arrivals improve, while buyers turn cautious in easing market"
- COALINDIA.NS (COAL INDIA LTD) score 76.4 — "Indian cotton arrivals improve, while buyers turn cautious in easing market"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.3 — "Indian cotton arrivals improve, while buyers turn cautious in easing market"
- INDIANB.NS (INDIAN BANK) score 65.6 — "US Federal Reserve's Michelle Bowman says changes to bank stress test coming soon"
- BAC (Bank of America Corporation) score 57.0 — "US Federal Reserve's Michelle Bowman says changes to bank stress test coming soon"
- COIN (Coinbase Global, Inc.) score 56.4 — "Global Markets: French bond spread at highest since 2012 as default insurance spikes"
- OHI (Omega Healthcare Investors, In) score 56.4 — "US stocks today: US stocks slip as Treasury yields rise, investors weigh Fed outlook"
- HDB (HDFC Bank Limited) score 51.1 — "US Federal Reserve's Michelle Bowman says changes to bank stress test coming soon"
- IDBI.NS (IDBI BANK LIMITED) score 46.1 — "US Federal Reserve's Michelle Bowman says changes to bank stress test coming soon"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 46.1 — "US Federal Reserve's Michelle Bowman says changes to bank stress test coming soon"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 46.1 — "US Federal Reserve's Michelle Bowman says changes to bank stress test coming soon"
- BOND (PIMCO Active Bond Exchange-Tra) score 44.6 — "Global Markets: French bond spread at highest since 2012 as default insurance spikes"
- CHKP (Check Point Software Technolog) score 39.1 — "IPO GMP comparison:  NSE vs Hero Motors vs SS Retail vs Jindal Supreme - Check which has w"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 31.5 — "Tata feud wipes  ₹52,154 crore off listed companies’ market value"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 31.5 — "Tata feud wipes  ₹52,154 crore off listed companies’ market value"
- TECHM.NS (TECH MAHINDRA LIMITED) score 29.3 — "Hi-Tech Flow Solutions files DHRP for IPO, to raises Rs 300 cr via fresh issue"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 29.3 — "Hi-Tech Flow Solutions files DHRP for IPO, to raises Rs 300 cr via fresh issue"
- TECH (Bio-Techne Corp) score 29.3 — "Hi-Tech Flow Solutions files DHRP for IPO, to raises Rs 300 cr via fresh issue"
- SEPN (Septerna, Inc.) score 28.6 — "Elevate Campuses IPO price band set at Rs 343–362; Rs 2,100 crore issue opens September 23"
- LTH (Life Time Group Holdings, Inc.) score 26.6 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks slip as highe"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.9 — "U.S. COULD RELEASE MORE OIL FROM SPR Energy Secretary Chris Wright says another round of c"
- 301077.SZ (CHINASTARS) score 22.8 — "Global Market: China stocks rally 1% as Trump-Xi meeting raises trade hopes"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 15.7 — "IPO GMP comparison:  NSE vs Hero Motors vs SS Retail vs Jindal Supreme - Check which has w"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.4 — "Japan's Refiners Have Enough Crude to Last Through November, Industry Body Says"
- MS (Morgan Stanley) score 10.9 — "JP MORGAN EXPECTS ECB TO DELIVER ANOTHER 25 BP INTEREST RATE HIKE IN MARCH 2027 AFTER A DE"
- JIOFIN.BO (Jio Financial Services Limited) score 10.9 — "Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, f"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 10.8 — "Nifty prediction, target 2026: Bulls to help investors for 27,000 in 2026? What experts sa"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.8 — "Up over 65% from IPO price in just 3 days! What is driving Glass Wall Systems share price?"
- VT (Vanguard Total World Stock Ind) score 8.6 — "The Race to Build a World Beyond Hormuz"
- JEF (Jefferies Financial Group Inc.) score 7.5 — "Adani stocks soar up to 12% after Jefferies sees up to 53% upside in Adani Energy and othe"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.3 — "Adani Energy vs CESC vs Tata Power vs NTPC vs Power Grid: Which stock has more upside? Tar"
- NVDA (NVIDIA Corporation) score 7.0 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.7 — "Gold jewellery sector seeks MDR exemption on high-value UPI transactions"
- META (Meta) score 6.3 — "Metal stocks to buy: Tata Steel, JSW Steel among Motilal Oswal’s top picks, up to 17% upsi"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.7 — "PNB Housing Finance among 4 F&O stocks with a sharp rise in futures open interest"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.7 — "HDFC Bank is winning the mutual fund vote over ICICI Bank. Can the shift last?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.6 — "Lenskart block deal: Rs 2,047 crore stake sale likely; Platinum Jasmine may offload 1.7% h"
- VOLTAS.NS (VOLTAS LTD) score 0.8 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- DELL (Dell Technologies Inc.) score 0.4 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"

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