# Transmission Layer — board brief · 2026-09-18 14:29Z

data as of **2026-09-18** · 97 series · 13 red / 34 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.435, 2d in regime; vol-pct 0.223, breadth-off 0.647, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.25, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.33, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 0.1, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.83, last shift 2026-07-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.07, last shift 2026-07-28. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.37, corr60 0.14, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.305, β 0.0869, p 0.0); driver zc 2.62 → expected 0.492%. Type hit-rate 0.815 (n=2075).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.263, β -0.058, p 1e-05); driver zc 2.62 → expected -0.329%. Type hit-rate 0.815 (n=2075).
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.262, β 0.1962, p 0.00745); driver zc -1.5 → expected -0.26%. Type hit-rate 0.815 (n=2075).
- **SETUP** dax → asx_200: leads 1d (ccf 0.259, β 0.1869, p 0.00502); driver zc -1.7 → expected -0.263%. Type hit-rate 0.815 (n=2075).
- Track record · residual_reversion: hit-rate **0.499** (n=1101) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2075) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
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
- dyn_bond [EQUITIES]: last 88.74, z20 -1.44, zc -1.15, resid-z 0.19 [quiet], 1d -0.40%, 1y-pct=1
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.423 via ust_2y, z 1.41, reacted)
- Watch next: brent (co-move) — not yet - watch; rho 0.648 vs ust_10y
- Watch next: wti (co-move) — not yet - watch; rho 0.641 vs ust_10y
- Watch next: sp500 (co-move) — not yet - watch; rho 0.55 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.423, z 1.41)
- Source: Wall Street mixed amid lower oil prices and higher Treasury yields — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/wall-street-mixed-amid-lower-oil-prices-and-higher-treasury-yields-11789740109962.html
- Source: Expert view: Elevated bond yields to put pressure on Nifty PE, says Wealthy's head of research — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/expert-view-elevated-bond-yields-to-put-pressure-on-nifty-pe-says-wealthys-head-of-research-11789729062189.html
- Source: Global Market: Eurozone bond yields set for weekly decline as ECB hike bets ease — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-set-for-weekly-decline-as-ecb-hike-bets-ease/articleshow/134333302.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 6.57] commodities · 2 series ↑
- wti [COMMODITIES]: last 97.99, z20 0.74, zc -1.31, resid-z -1.37 [quiet], 1d -3.85%, 1-session move -3.85% ≥ 1.5%
- brent [COMMODITIES]: last 100.09, z20 0.40, zc -1.72, resid-z -1.63 [unexplained], 1d -4.51%, 1-session move -4.51% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.593 vs wti
- Source: Wall Street mixed amid lower oil prices and higher Treasury yields — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/wall-street-mixed-amid-lower-oil-prices-and-higher-treasury-yields-11789740109962.html
- Source: The Oil Market’s Backup Plan Is Breaking Down — OilPrice, 2026-09-18. https://oilprice.com/Energy/Energy-General/The-Oil-Markets-Backup-Plan-Is-Breaking-Down.html
- Source: US stocks today: S&P 500, Nasdaq open higher as oil prices fall — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-sp-500-nasdaq-open-higher-as-oil-prices-fall/articleshow/134337081.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.83] dxy ↑
- dxy [FX]: last 100.51, z20 2.83, zc 0.84, resid-z 2.15 [unexplained], 1d 0.29%, 20d range extreme; |z20|=2.83
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 5.69] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2570.34, z20 2.86, zc 1.29, resid-z 1.92 [unexplained], 1d 5.04%, |z20|=2.86
- btc_usd [CRYPTO]: last 80730.00, z20 1.88, zc 2.62, resid-z 2.94 [unexplained], 1d 5.66%, |z20|=1.88
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.483 via btc_usd, z -0.73, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.607 vs btc_usd
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.591 vs eth_usd
- **India receivers**: dyn_cartrade_ns (rho 0.483, z -0.73)
- Source: Bitcoin vs Ethereum vs Solana: Which crypto asset is best positioned for the next bull run? — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-vs-ethereum-vs-solana-which-crypto-asset-is-best-positioned-for-the-next-bull-run/articleshow/134336948.cms
- Source: Bitcoin holds near $77K despite hawkish Fed, CLARITY Act setback and weak ETF demand. Here is what experts say — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-77k-despite-hawkish-fed-clarity-act-setback-and-weak-etf-demand-here-is-what-experts-say/articleshow/134330927.cms
- Source: BITCOIN COULD GET MORE SUPPORT THAN GOLD JPMorgan says Bitcoin could benefit more than gold if ETF hedging demand eases. Short interest in IBIT remains near yearly highs, while its put-to-call ratio is also higher than GLD’s — signaling heavier Bitcoin hedging. If those hedges unwind, JPMorgan sees  — DeItaone, 2026-09-17. https://t.me/walter_bloomberg/35890
- Historical analogues: 2025-07-17 (d=0.08), 2026-03-17 (d=0.13), 2026-04-13 (d=0.31)

### [AMBER 5.47] cross-asset · 3 series ↓
- dyn_ms [EQUITIES]: last 202.67, z20 -2.15, zc -0.23, resid-z -0.58 [quiet], 1d -0.42%, |z20|=2.15
- dow_jones [INDICES]: last 51594.15, z20 -1.96, zc -0.41, resid-z -1.46 [quiet], 1d -0.36%, |z20|=1.96
- russell_2000 [INDICES]: last 2850.33, z20 -1.91, zc -0.74, resid-z -1.19 [quiet], 1d -0.85%, |z20|=1.91
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.717 vs dyn_ms, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.665 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.653 vs dow_jones, historically leads by 2d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.582 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.738 vs dyn_ms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: S&P 500, Nasdaq open higher as oil prices fall — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-xenon-pharmaceuticals-berkshire-hathaway-alphabet-apple-stock-price-news-18th-september-2026/liveblog/134335091.cms
- Source: US Market: Nike’s position in Dow Jones index comes under pressure — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-nikes-position-in-dow-jones-index-comes-under-pressure/articleshow/134329444.cms
- Source: Global Market: J.P. Morgan sees BoE rates rising amid renewed inflation risks — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-j-p-morgan-sees-boe-rates-rising-amid-renewed-inflation-risks/articleshow/134326027.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-27 (d=0.32), 2024-10-18 (d=0.52)

### [RED 5.24] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.84, z20 -2.24, zc n/a, resid-z n/a [quiet], 1d -2.03%, GSR<75 (extreme low); |z20|=2.24
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.394 via gold_silver_ratio, z -0.82, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.862 vs gold_silver_ratio
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.62 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.394, z -0.82)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 4.91] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 722.45, z20 -2.91, zc -2.53, resid-z -2.08 [unexplained], 1d -4.78%, |z20|=2.91
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.495 via dyn_tatatech_ns, z -1.61, reacted); dyn_tataelxsi_ns (rho 0.473 via dyn_tatatech_ns, z -2.28, reacted); dyn_techm_ns (rho 0.397 via dyn_tatatech_ns, z -1.3, reacted)
- **India receivers**: nifty_it (rho 0.495, z -1.61); dyn_tataelxsi_ns (rho 0.473, z -2.28); dyn_techm_ns (rho 0.397, z -1.3)
- Source: TCS, Tata Chemicals, Tata Steel to Tata Motors PV — Tata Group stock lost 46,600 crores in a single day — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tcs-tata-chemicals-tata-steel-to-tata-motors-pv-tata-group-stock-lost-46-600-crores-in-a-single-day-11789728923950.html
- Source: Sensex, Nifty extend losses to 6th week, crude moderation offers little relief, IT & Tata group stocks weigh — BusinessLine Mkts, 2026-09-18. https://www.thehindubusinessline.com/markets/sensex-nifty-extend-losses-to-6th-week-crude-moderation-offers-little-relief-it-tata-group-stocks-weigh/article71480356.ece
- Source: Tata Sons listing: Tata Chemicals vs Tata Steel vs Tata Power — Which Tata Group stocks may benefit most? Experts decode — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tata-sons-listing-tata-chemicals-vs-tata-steel-vs-tata-power-which-tata-group-stocks-may-benefit-most-experts-decode-11789722802716.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (4.87), midcap_largecap_ratio ↑ (4.41), dyn_bac ↓ (4.31), dyn_tataelxsi_ns ↓ (4.28), usd_cny ↓ (4.17), dyn_jef ↓ (4.1), dyn_lenskart_ns ↑ (4.07), dyn_voltas_ns ↓ (3.93), commodities · 2 series ↑ (3.84), fx · 2 series ↓ (3.83), fx · 2 series ↑ (3.37), indices · 3 series ↓ (3.12)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.9 — "Nestle India shares slip nearly 3% after FSSAI initiates legal action over infant nutritio"
- COALINDIA.NS (COAL INDIA LTD) score 77.8 — "Nestle India shares slip nearly 3% after FSSAI initiates legal action over infant nutritio"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.5 — "Nestle India shares slip nearly 3% after FSSAI initiates legal action over infant nutritio"
- INDIANB.NS (INDIAN BANK) score 63.3 — "From GIFT City to Europe: India INX GA to launch tax-efficient UCITS for Indian investors"
- COIN (Coinbase Global, Inc.) score 57.9 — "Global Market: European shares edge lower as telecom stocks weigh"
- BAC (Bank of America Corporation) score 56.4 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- OHI (Omega Healthcare Investors, In) score 52.7 — "Nifty prediction, target 2026: Bulls to help investors for 27,000 in 2026? What experts sa"
- HDB (HDFC Bank Limited) score 49.2 — "This newly listed stock more than doubled investors' money in less than 2 months; HDFC Sec"
- BOND (PIMCO Active Bond Exchange-Tra) score 45.6 — "Global Market: Foreign investors sell Asian bonds in August as global debt rout weighs"
- IDBI.NS (IDBI BANK LIMITED) score 45.0 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.0 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.0 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- CHKP (Check Point Software Technolog) score 40.9 — "IPO GMP comparison:  NSE vs Hero Motors vs SS Retail vs Jindal Supreme - Check which has w"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 31.8 — "Adani Energy vs CESC vs Tata Power vs NTPC vs Power Grid: Which stock has more upside? Tar"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 31.8 — "Adani Energy vs CESC vs Tata Power vs NTPC vs Power Grid: Which stock has more upside? Tar"
- TECHM.NS (TECH MAHINDRA LIMITED) score 30.6 — "Hi-Tech Flow Solutions files DHRP for IPO, to raises Rs 300 cr via fresh issue"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.6 — "Hi-Tech Flow Solutions files DHRP for IPO, to raises Rs 300 cr via fresh issue"
- TECH (Bio-Techne Corp) score 30.6 — "Hi-Tech Flow Solutions files DHRP for IPO, to raises Rs 300 cr via fresh issue"
- SEPN (Septerna, Inc.) score 29.8 — "Elevate Campuses IPO price band set at Rs 343–362; Rs 2,100 crore issue opens September 23"
- LTH (Life Time Group Holdings, Inc.) score 26.7 — "Quote of the day by Fred C. Kelly: "Vanity makes men sell good stocks and keep poor ones i"
- 301077.SZ (CHINASTARS) score 23.8 — "Global Market: China stocks rally 1% as Trump-Xi meeting raises trade hopes"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.9 — "Adani Energy vs CESC vs Tata Power vs NTPC vs Power Grid: Which stock has more upside? Tar"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 16.4 — "IPO GMP comparison:  NSE vs Hero Motors vs SS Retail vs Jindal Supreme - Check which has w"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "Japan's Refiners Have Enough Crude to Last Through November, Industry Body Says"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.3 — "Nifty prediction, target 2026: Bulls to help investors for 27,000 in 2026? What experts sa"
- MS (Morgan Stanley) score 10.4 — "Global Market: J.P. Morgan sees BoE rates rising amid renewed inflation risks"
- JIOFIN.BO (Jio Financial Services Limited) score 10.4 — "Skyways Air Services share price surges 15% after Q1 results, dividend announcements | All"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "Up over 65% from IPO price in just 3 days! What is driving Glass Wall Systems share price?"
- VT (Vanguard Total World Stock Ind) score 9.0 — "The Race to Build a World Beyond Hormuz"
- JEF (Jefferies Financial Group Inc.) score 7.8 — "Adani stocks soar up to 12% after Jefferies sees up to 53% upside in Adani Energy and othe"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.7 — "Adani Energy vs CESC vs Tata Power vs NTPC vs Power Grid: Which stock has more upside? Tar"
- NVDA (NVIDIA Corporation) score 7.3 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.0 — "Gold jewellery sector seeks MDR exemption on high-value UPI transactions"
- META (Meta) score 6.6 — "Metal stocks to buy: Tata Steel, JSW Steel among Motilal Oswal’s top picks, up to 17% upsi"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.9 — "PNB Housing Finance among 4 F&O stocks with a sharp rise in futures open interest"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.9 — "HDFC Bank is winning the mutual fund vote over ICICI Bank. Can the shift last?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.7 — "Lenskart Solutions block deal: ADIA-backed investor likely to offload 1.7% stake: Report"
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