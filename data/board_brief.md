# Transmission Layer — board brief · 2026-08-21 13:09Z

data as of **2026-08-21** · 98 series · 15 red / 25 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.234, 2d in regime; vol-pct 0.217, breadth-off 0.25, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.4, contra nifty_50 corr20=0.04, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.87, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.37, last shift 2026-07-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.13, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.69, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.04, corr60 -0.13, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.21, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.26, corr60 0.19, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.593, β 0.4867, p 0.0); driver zc -1.88 → expected -0.628%. Type hit-rate 0.819 (n=2302).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.489, β 0.1961, p 0.0); driver zc -1.84 → expected -0.616%. Type hit-rate 0.819 (n=2302).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.466, β 0.7864, p 0.0); driver zc -1.88 → expected -1.014%. Type hit-rate 0.819 (n=2302).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.422, β 0.7091, p 0.0); driver zc -1.88 → expected -0.914%. Type hit-rate 0.819 (n=2302).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.416, β 0.3441, p 0.0); driver zc -1.84 → expected -1.081%. Type hit-rate 0.819 (n=2302).
- **SETUP** tips_10y_real → usd_jpy: leads 1d (ccf 0.409, β 0.1225, p 0.0); driver zc -1.66 → expected -0.305%. Type hit-rate 0.819 (n=2302).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.407, β -0.3502, p 0.0); driver zc -1.88 → expected 0.452%. Type hit-rate 0.819 (n=2302).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.395, β 0.2592, p 1e-05); driver zc -1.88 → expected -0.334%. Type hit-rate 0.819 (n=2302).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.391, β 0.3216, p 0.0); driver zc -1.84 → expected -1.01%. Type hit-rate 0.819 (n=2302).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.363, β -0.2362, p 0.0); driver zc -1.88 → expected 0.304%. Type hit-rate 0.819 (n=2302).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.309, β 0.0866, p 0.0); driver zc 1.53 → expected 0.494%. Type hit-rate 0.819 (n=2302).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.274, β 0.0877, p 0.00313); driver zc -1.84 → expected -0.275%. Type hit-rate 0.819 (n=2302).
- Track record · residual_reversion: hit-rate **0.491** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2302) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.47] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 133.34, z20 7.81, zc 5.86, resid-z 11.29 [unexplained], 1d 35.87%, |z20|=7.81; 1y-pct=100
- btc_usd [CRYPTO]: last 77197.21, z20 5.37, zc 1.53, resid-z 3.02 [unexplained], 1d 5.70%, |z20|=5.37
- eth_usd [CRYPTO]: last 2390.05, z20 3.77, zc 0.54, resid-z 1.49 [quiet], 1d 2.74%, |z20|=3.77
- dyn_coin [EQUITIES]: last 172.46, z20 2.62, zc 1.52, resid-z 2.13 [unexplained], 1d 7.65%, |z20|=2.62
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.384 via btc_usd, z 0.91, quiet)
- Watch next: vix (inverse) — not yet - watch; rho -0.584 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.512 vs eth_usd
- **India receivers**: nifty_metal (rho 0.384, z 0.91)
- Source: Bitcoin on track for best week in more than two years. Can this mean the next crypto bull market has arrived? — MarketWatch Top, 2026-08-21. https://www.marketwatch.com/story/bitcoin-on-track-for-best-week-in-more-than-two-years-has-the-next-crypto-bull-market-arrived-0181180c?mod=mw_rss_topstories
- Source: Global Market: European shares little changed as bond yields rise and gulf tensions lift oil — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-little-changed-as-bond-yields-rise-and-gulf-tensions-lift-oil/articleshow/133399383.cms
- Source: CRYPTO STOCKS SURGE AS BITCOIN RALLY ACCELERATES Crypto-linked U.S. stocks climbed sharply in premarket trading as Bitcoin jumped 6.6% to nearly $77,800 and Ethereum gained 2.7%. Investors are growing more confident about a favorable U.S. regulatory environment for crypto. — DeItaone, 2026-08-21. https://t.me/walter_bloomberg/34877
- Historical analogues: 2025-08-13 (d=1.14), 2025-05-09 (d=2.07), 2024-11-21 (d=2.32)

### [RED 8.55] cross-asset · 6 series ↑
- comex_gold [COMMODITIES]: last 4632.70, z20 2.30, zc 1.65, resid-z 0.72 [priced], 1d 2.58%, |z20|=2.30; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.36, z20 2.11, zc 0.75, resid-z -1.20 [quiet], 1d 1.97%, |z20|=2.11; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 66.79, z20 -1.40, zc n/a, resid-z n/a [quiet], 1d 0.60%, GSR<75 (extreme low)
- comex_copper [COMMODITIES]: last 6.60, z20 0.69, zc 0.96, resid-z 0.46 [quiet], 1d 2.14%, 1y-pct=96
- dax [INDICES]: last 26093.14, z20 0.27, zc 0.56, resid-z 0.04 [quiet], 1d 0.42%, 1y-pct=95
- stoxx_50 [INDICES]: last 6451.79, z20 0.12, zc 0.59, resid-z 0.18 [quiet], 1d 0.46%, 1y-pct=95
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-30 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.533 via comex_silver, z 0.91, quiet); nifty_midcap_100 (rho 0.477 via dax, z 0.66, quiet); dyn_stylebaaza_ns (rho -0.391 via gold_silver_ratio, z 1.7, reacted)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.813 vs dax, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.605 vs comex_copper, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.593 vs dax, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.58 vs comex_copper, historically leads by 3d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.574 vs comex_copper, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.533, z 0.91); nifty_midcap_100 (rho 0.477, z 0.66); dyn_stylebaaza_ns (rho -0.391, z 1.7)
- Source: Shanti Gold among 7 consumer discretionary stocks that hit 52-week highs and surged up to 37% in a month — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/stocks/news/shanti-gold-among-7-consumer-discretionary-stocks-that-hit-52-week-highs-and-surged-up-to-37-in-a-month/slideshow/133404296.cms
- Source: Tata MF lifts curbs on investment in gold ETFs — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/tata-mf-lifts-curbs-on-investment-in-gold-etfs/article71372919.ece
- Source: Gold climbs to near three-month peak after US Treasury move — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/gold/gold-climbs-to-near-three-month-peak-after-us-treasury-move/article71372830.ece
- Historical analogues: 2025-07-30 (d=0.59), 2026-04-02 (d=0.67), 2024-11-07 (d=0.8)

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

### [RED 5.61] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 3072.90, z20 3.61, zc 1.79, resid-z 1.85 [unexplained], 1d 6.14%, |z20|=3.61
- **Mechanism**: dyn_cartrade_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top Gainers & Losers on 21 Aug: Welspun Corp, Jindal Saw, Urban Company, Vedanta, CarTrade Tech among top gainers — Mint Markets, 2026-08-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-21-aug-welspun-corp-jindal-saw-urban-company-vedanta-cartrade-tech-among-top-gainers-11787305625058.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [RED 5.07] commodities · 2 series ↑
- corn [COMMODITIES]: last 503.75, z20 4.24, zc 4.07, resid-z 0.65 [moved], 1d 5.22%, |z20|=4.24; 1y-pct=100
- wheat [COMMODITIES]: last 697.50, z20 2.55, zc 1.24, resid-z 0.12 [quiet], 1d 2.16%, |z20|=2.55; 1y-pct=99
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

### [RED 4.47] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.81, zc 0.98, resid-z 1.28 [quiet], 1d 0.60%, |z20|=2.81
- eur_usd [FX]: last 1.17, z20 2.26, zc 0.34, resid-z 0.34 [quiet], 1d 0.13%, |z20|=2.26
- gbp_usd [FX]: last 1.36, z20 2.11, zc 0.66, resid-z 0.64 [quiet], 1d 0.29%, |z20|=2.11
- usd_mxn [FX]: last 16.91, z20 -1.80, zc -0.56, resid-z -0.47 [quiet], 1d -0.22%, |z20|=1.80; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.586 via usd_mxn, z 1.26, reacted); nifty_midcap_100 (rho 0.427 via aud_usd, z 0.66, quiet); dyn_icicigi_bo (rho -0.409 via gbp_usd, z -1.23, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.632 vs aud_usd, historically leads by 4d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.555 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.522 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.586, z 1.26); nifty_midcap_100 (rho 0.427, z 0.66); dyn_icicigi_bo (rho -0.409, z -1.23)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.28] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.28, zc n/a, resid-z n/a [quiet], 1d 0.02%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.492 via midcap_largecap_ratio, z 0.66, quiet); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 1.05, reacted); dyn_bharatcoal_ns (rho 0.351 via midcap_largecap_ratio, z 1.7, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.492, z 0.66); dyn_fincables_ns (rho 0.355, z 1.05); dyn_bharatcoal_ns (rho 0.351, z 1.7)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_jef ↓ (4.21), soybeans ↑ (3.85), dyn_stylebaaza_ns ↑ (3.7), usd_cny ↓ (3.68), dyn_icicigi_bo ↓ (3.23), dyn_tech ↑ (2.92), dyn_lenskart_ns ↑ (2.66), eur_inr ↑ (2.62), dyn_pcjeweller_ns ↑ (2.49), dyn_lth ↑ (2.44), dyn_tatatech_ns ↑ (2.32), nifty_fmcg ↓ (2.08)

## India macro
- nifty_50: 24252.0000 (1d 0.08%, z20 -0.37, flag none)
- nifty_midcap_100: 63735.6016 (1d 0.11%, z20 0.66, flag amber)
- usd_inr: 95.6850 (1d 0.20%, z20 0.24, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6281 (1d 0.02%, z20 1.28, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 105.8 — "India’s PMS Industry AUM rises 2% in July to Rs 44 lakh crore, client base grows 1.3%: APM"
- INOXINDIA.NS (INOX INDIA LIMITED) score 102.2 — "India’s PMS Industry AUM rises 2% in July to Rs 44 lakh crore, client base grows 1.3%: APM"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 101.6 — "India’s PMS Industry AUM rises 2% in July to Rs 44 lakh crore, client base grows 1.3%: APM"
- INDIANB.NS (INDIAN BANK) score 96.7 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- BOND (PIMCO Active Bond Exchange-Tra) score 85.0 — "LONG-TERM YIELDS END WILD WEEK NEAR DECADE HIGHS Long-term bond yields remain near multi-y"
- BAC (Bank of America Corporation) score 79.1 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- HDB (HDFC Bank Limited) score 72.5 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- IDBI.NS (IDBI BANK LIMITED) score 68.1 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 68.1 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 68.0 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- COIN (Coinbase Global, Inc.) score 59.5 — "Global Market: BOJ's July 2027 meeting could shape Japan's rate path"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.0 — "Market wrap:  Kotak Mahindra Bank, Power Grid, Maruti Suzuki, Trent top gainers and losers"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.9 — "Atomberg Technologies files DRHP for IPO to raise ₹450 crore through fresh issue"
- TECH (Bio-Techne Corp) score 50.8 — "Atomberg Technologies files DRHP for IPO to raise ₹450 crore through fresh issue"
- OHI (Omega Healthcare Investors, In) score 50.3 — "CRYPTO STOCKS SURGE AS BITCOIN RALLY ACCELERATES Crypto-linked U.S. stocks climbed sharply"
- CHKP (Check Point Software Technolog) score 40.2 — "American consumers are delivering a retail reality check as they laser in on bargains"
- LTH (Life Time Group Holdings, Inc.) score 38.4 — "Tempsens Instruments IPO Day 2: Issue booked 21.66 times, GMP signals 90% premium. Apply o"
- 301077.SZ (CHINASTARS) score 26.0 — "TSLA - TESLA TO RECALL 1,956,713 CHINA MADE MODEL 3, Y VEHICLES-CHINA'S MARKET REGULATOR"
- PCJEWELLER.NS (PC JEWELLER LTD) score 21.2 — "Lalithaa Jewellery IPO listing share price prediction: What latest GMP hints at"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.5 — "These three copper stocks are riding India’s energy expansion. Should you invest?"
- JIOFIN.BO (Jio Financial Services Limited) score 19.4 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.6 — "Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.4 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.2 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.1 — "Tata MF lifts curbs on investment in gold ETFs"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.3 — "Tata MF lifts curbs on investment in gold ETFs"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.1 — "American consumers are delivering a retail reality check as they laser in on bargains"
- MS (Morgan Stanley) score 12.3 — "PRICE TARGET RAISED • $ABT: PT raised to $135 from $115 by TD Cowen • $ADSK: PT raised to "
- JEF (Jefferies Financial Group Inc.) score 11.4 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.0 — "Tata Steel, Adani Ports among top 10 stocks downgraded by Motilal Oswal after Q1 results"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 10.2 — "ICICI Bank doubles borrowing from overseas markets to $5 billion"
- MRNA (Moderna, Inc.) score 9.5 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VT (Vanguard Total World Stock Ind) score 8.5 — "Quote of the day by Tom Gayner: "I’ve always said you might as well assume the world is go"
- META (Meta) score 8.3 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.9 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.4 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.0 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.1 — "Voltas reported strong growth in June quarter, but failed to impress"
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