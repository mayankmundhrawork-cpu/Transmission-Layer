# Transmission Layer — board brief · 2026-10-30 18:00Z

data as of **2026-10-30** · 97 series · 13 red / 37 amber · 8 events surfaced (34 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.852, 2d in regime; vol-pct 0.88, breadth-off 0.824, Markov P(high-vol) 0.444)
- [INVERTED] **safe_haven_gold** — corr20 -0.58, corr60 -0.48, contra nifty_50 corr20=0.29, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.12, last shift 2026-09-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.02, corr60 0.08, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.94, corr60 -0.79, last shift 2026-09-11. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 -0.0, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.08, corr60 -0.14, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.55, corr60 0.36, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.0020015649532281188)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.566, β 0.4351, p 0.0); driver zc -2.73 → expected -0.879%. Type hit-rate 0.838 (n=1605).
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.564, β 0.3307, p 0.0); driver zc -1.86 → expected -0.692%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.563, β 0.4471, p 0.0); driver zc -2.72 → expected -0.897%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.557, β 0.3414, p 0.0); driver zc -2.72 → expected -0.685%. Type hit-rate 0.838 (n=1605).
- **SETUP** vix → asx_200: leads 1d (ccf -0.496, β -0.0447, p 0.0); driver zc 3.09 → expected -1.057%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.471, β 0.1801, p 0.0); driver zc -2.6 → expected -0.845%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.453, β 0.129, p 0.0); driver zc -2.58 → expected -0.839%. Type hit-rate 0.838 (n=1605).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.441, β 0.1914, p 0.0); driver zc -2.91 → expected -0.745%. Type hit-rate 0.838 (n=1605).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.431, β -0.0293, p 0.0); driver zc 3.09 → expected -0.694%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.377, β -2.4837, p 0.00637); driver zc -2.72 → expected 4.984%. Type hit-rate 0.838 (n=1605).
- **SETUP** vix → india_vix: leads 1d (ccf 0.352, β 0.2335, p 0.0105); driver zc 3.09 → expected 5.526%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.346, β 0.5454, p 1e-05); driver zc -2.72 → expected -1.094%. Type hit-rate 0.838 (n=1605).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.324, β 0.1419, p 1e-05); driver zc -2.72 → expected -0.285%. Type hit-rate 0.838 (n=1605).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.307, β 0.4733, p 0.00039); driver zc -2.73 → expected -0.956%. Type hit-rate 0.838 (n=1605).
- **SETUP** vix → nifty_metal: leads 1d (ccf -0.299, β -0.0475, p 0.00062); driver zc 3.09 → expected -1.124%. Type hit-rate 0.838 (n=1605).
- **SETUP** russell_2000 → india_vix: leads 1d (ccf -0.276, β -1.282, p 0.00218); driver zc -1.86 → expected 2.682%. Type hit-rate 0.838 (n=1605).
- **SETUP** russell_2000 → nifty_50: leads 1d (ccf 0.252, β 0.1599, p 7e-05); driver zc -1.86 → expected -0.335%. Type hit-rate 0.838 (n=1605).
- Track record · residual_reversion: hit-rate **0.506** (n=1122) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.838** (n=1605) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.52] cross-asset · 4 series ↓
- sp500 [INDICES]: last 7564.41, z20 -3.14, zc -2.73, resid-z 0.23 [priced], 1d -2.02%, |z20|=3.14
- vix [INDICES]: last 21.27, z20 2.85, zc 3.09, resid-z n/a [moved], 1d 23.66%, 1-session move +23.66% ≥ 15.0%; |z20|=2.85
- dyn_vt [EQUITIES]: last 154.80, z20 -2.71, zc -2.72, resid-z 0.60 [priced], 1d -2.01%, |z20|=2.71
- nasdaq_100 [INDICES]: last 28258.73, z20 -2.41, zc -2.91, resid-z -0.14 [priced], 1d -3.89%, |z20|=2.41
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.736 vs sp500, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.86 vs sp500
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.716 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.53 vs sp500
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.515 vs nasdaq_100
- Source: Japan to Overtake China As World’s Top LNG Importer This Year — OilPrice, 2026-10-30. https://oilprice.com/Latest-Energy-News/World-News/Japan-to-Overtake-China-As-Worlds-Top-LNG-Importer-This-Year.html
- Source: US stocks today: Nasdaq sinks 2.2% as Amazon, Intel fuel fresh fears over AI spending — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-tumbles-over-2-sp-1-at-open-as-amazon-intel-add-to-ai-spending-woes/articleshow/135364444.cms
- Source: Big dividends, bigger losses? The hidden risk in Wall Street's highest-yielding stocks — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/big-dividends-bigger-losses-the-hidden-risk-in-wall-streets-highest-yielding-stocks/articleshow/135362488.cms
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 7.38] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 138.14, z20 -4.06, zc -3.02, resid-z 0.07 [moved], 1d -13.98%, |z20|=4.06; 1y-pct=0
- btc_usd [CRYPTO]: last 77030.79, z20 -2.92, zc -0.40, resid-z 0.39 [quiet], 1d -0.96%, |z20|=2.92
- eth_usd [CRYPTO]: last 2240.88, z20 -1.92, zc -0.10, resid-z 0.62 [quiet], 1d -0.38%, |z20|=1.92
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Intel stock plunges 30% as weak PC demand and AI costs trigger global chip selloff — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/intel-plunges-25-as-weak-pc-demand-and-ai-costs-trigger-global-chip-selloff/articleshow/135371230.cms
- Source: Global Market: European blue-chips set for strongest earnings in four years — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-blue-chips-set-for-strongest-earnings-in-four-years/articleshow/135356294.cms
- Source: Global Market: European automakers get earnings boost as Chinese competition weighs on recovery — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-european-automakers-get-earnings-boost-as-chinese-competition-weighs-on-recovery/articleshow/135352780.cms
- Historical analogues: 2026-05-22 (d=0.78), 2025-10-16 (d=0.85), 2025-04-10 (d=0.94)

### [RED 7.37] commodities · 2 series ↑
- wti [COMMODITIES]: last 104.68, z20 1.54, zc 1.03, resid-z -1.21 [quiet], 1d 2.63%, 1-session move +2.63% ≥ 1.5%; |z20|=1.54; 1y-pct=96
- brent [COMMODITIES]: last 113.89, z20 1.09, zc -0.43, resid-z -3.28 [unexplained], 1d -0.86%, 1y-pct=96
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.446 via wti, z -0.92, quiet)
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.419 vs wti, historically leads by 4d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.538 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.446, z -0.92)
- Source: U.S. Oil, Gas Drillers Still on Hold — OilPrice, 2026-10-30. https://oilprice.com/Energy/Energy-General/US-Oil-Gas-Drillers-Still-on-Hold.html
- Source: RIL diversifies crude sourcing, redirects exports amid Middle East disruptions — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/commodities/ril-diversifies-crude-sourcing-redirects-exports-amid-middle-east-disruptions/article71646507.ece
- Source: Oil Traders Brace for a Wild Week as Brent Approaches $120 — OilPrice, 2026-10-30. https://oilprice.com/Energy/Oil-Prices/Oil-Traders-Brace-for-a-Wild-Week-as-Brent-Approaches-120.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.25] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3891.80, z20 -3.93, zc -3.13, resid-z -0.99 [priced], 1d -3.46%, |z20|=3.93; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 49.15, z20 -2.95, zc -2.53, resid-z 0.17 [priced], 1d -5.82%, |z20|=2.95; 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 79.17, z20 2.67, zc n/a, resid-z n/a [quiet], 1d 2.50%, |z20|=2.67
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.563 vs comex_gold
- Source: Silver price crash deepens as Oct losses hit  ₹45,000/kg; gold falls to 7-month low: Why are precious metals sinking? — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/silver-price-crash-deepens-as-oct-losses-hit-rs-45-000-kg-gold-falls-to-7-month-low-why-are-precious-metals-sinking-11793368770318.html
- Source: India gold price, October 30: MCX rate crashes below  ₹1.42 lakh ahead of Dhanteras - What's triggering sell-off? — Mint Markets, 2026-10-30. https://www.livemint.com/market/commodities/india-gold-price-october-30-mcx-rate-crashes-below-rs-1-42-lakh-ahead-of-dhanteras-whats-triggering-selloff-11793360090751.html
- Source: NSE's electronic gold receipts could generate ₹1,260 crore revenue by FY30, says Jefferies — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/nses-electronic-gold-receipts-could-generate-1260-crore-revenue-by-fy30-says-jefferies/article71644103.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.53] dyn_cartrade_ns ↓
- dyn_cartrade_ns [EQUITIES]: last 2173.00, z20 -3.53, zc -1.83, resid-z -2.12 [unexplained], 1d -6.54%, |z20|=3.53
- **Mechanism**: dyn_cartrade_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3,377. Here’s why — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/cartrade-tech-shares-tank-over-6-after-q2-results-but-nomura-raises-target-price-to-rs-3377-heres-why/articleshow/135290221.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 4.35] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.92, z20 2.35, zc -0.31, resid-z -0.99 [quiet], 1d -0.94%, |z20|=2.35; 1y-pct=96
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: European Gas Tops 101 Euros for First Time Since 2022 — OilPrice, 2026-10-30. https://oilprice.com/Latest-Energy-News/World-News/European-Gas-Tops-101-Euros-for-First-Time-Since-2022.html
- Source: Borosil shares skyrocket 16% after strong Q2 results | Is it time to book profits? Target price, stop loss here — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/borosil-shares-skyrocket-16-after-strong-q2-results-is-it-time-to-book-profits-target-price-stop-loss-here-11793335910559.html
- Source: ITC, RIL, HDFC Bank among top laggards as Nifty falls over 12% in 2026: Time to buy beaten-down stocks or wait for a recovery? — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/itc-ril-hdfc-bank-among-top-laggards-as-nifty-falls-over-12-in-2026-time-to-buy-beaten-down-stocks-or-wait-for-a-recovery/articleshow/135345201.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [AMBER 4.23] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 389.00, z20 -2.23, zc -0.77, resid-z -0.93 [quiet], 1d -1.04%, |z20|=2.23
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India shares fall 3% after Q2 results; Jefferies, Motilal Oswal, others cut target price — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/coal-india-shares-fall-3-after-q2-results-jefferies-motilal-oswal-others-cut-target-price/articleshow/135349282.cms
- Source: Why Coal India shares fell 2% despite strong Q2 revenue growth — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/stock-markets/coal-india-shares-slip-2-after-q2-ebitda-misses-despite-strong-revenue-beat/article71643744.ece
- Source: Q2 October dividend champions: Infosys, Colgate, HUL, CPCL, Coal India | Big payouts - amount, record date — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/october-dividend-champions-infosys-colgate-hul-chennai-petro-coal-india-announce-big-payouts-check-amount-record-11793286004751.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

### [AMBER 4.21] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3596.61, z20 -2.21, zc -1.83, resid-z -0.23 [moved], 1d -1.50%, |z20|=2.21; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: kospi (co-move) — not yet - watch; rho 0.557 vs shanghai_comp
- Source: Global Market: China stocks extend losing streak to 12 weeks as global AI selloff hits tech shares — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-extend-losing-streak-to-12-weeks-as-global-ai-selloff-hits-tech-shares/articleshow/135346469.cms
- Source: Global Market: China stocks fall as tech selloff deepens despite Fed rate pause — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-tech-selloff-deepens-despite-fed-rate-pause/articleshow/135295671.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (4.21), dyn_301077_sz ↓ (4.1), dyn_jiofin_bo ↓ (3.8), dyn_rs ↑ (3.75), nifty_50 ↑ (3.74), dyn_schd ↑ (3.73), dyn_sepn ↑ (3.7), eur_usd ↓ (3.65), dyn_tech ↑ (3.65), usd_cny ↓ (3.51), dyn_4417_t ↑ (3.46), dyn_atherenerg_ns ↑ (3.16)

## India macro
- nifty_50: 23053.0996 (1d 0.51%, z20 1.74, flag amber)
- nifty_midcap_100: 57304.4492 (1d -0.92%, z20 -0.92, flag none)
- usd_inr: 94.9400 (1d -0.28%, z20 -0.74, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4858 (1d -1.42%, z20 -1.59, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 100.7 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- COALINDIA.NS (COAL INDIA LTD) score 100.5 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 99.1 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- INDIANB.NS (INDIAN BANK) score 77.1 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- BAC (Bank of America Corporation) score 68.5 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- TGT (Target Corporation) score 63.9 — "Diwali 2026 Top Stocks To Buy: Apollo Hospitals, GE Vernova, TARIL, TD Power, Jindal Steel"
- HDB (HDFC Bank Limited) score 60.0 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- COIN (Coinbase Global, Inc.) score 59.0 — "Intel stock plunges 30% as weak PC demand and AI costs trigger global chip selloff"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.7 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- IDBI.NS (IDBI BANK LIMITED) score 58.5 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 58.5 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- OHI (Omega Healthcare Investors, In) score 54.8 — "Record earnings! 5 big takeaways from RIL Q2 results investors should watch for Monday tra"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.9 — "Amazon, Intel shares crash up to 25% in premarket trade as AI spending concerns trigger te"
- CHKP (Check Point Software Technolog) score 43.6 — "After IPO listing, Jio Platforms Q2 results 2026 announced: Check ARPU, profit, revenue, E"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.8 — "Amazon, Intel shares crash up to 25% in premarket trade as AI spending concerns trigger te"
- TECH (Bio-Techne Corp) score 38.8 — "Amazon, Intel shares crash up to 25% in premarket trade as AI spending concerns trigger te"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 37.2 — "NTPC Green Energy Q2 Results: Profit jumps 56% YoY to Rs 137 crore, revenue rises 53%"
- RS (Reliance, Inc.) score 36.1 — "Reliance Industries Q2 Results 2026 Live: RIL Q2 profit jumps 41% YoY to Rs 25,548 crore; "
- LTH (Life Time Group Holdings, Inc.) score 29.4 — "European Gas Tops 101 Euros for First Time Since 2022"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.7 — "India bonds buckle for fourth straight month on oil's climb"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.6 — "Reliance Industries Q2 results 2026 today: Preview, should you buy, sell or hold ahead of "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 22.0 — "Tata Capital among 4 Nifty500 stocks closing above VWAP"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 22.0 — "Tata Capital among 4 Nifty500 stocks closing above VWAP"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.9 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- 301077.SZ (CHINASTARS) score 20.5 — "Japan to Overtake China As World’s Top LNG Importer This Year"
- SCHD (Schwab US Dividend Equity ETF) score 16.2 — "Big dividends, bigger losses? The hidden risk in Wall Street's highest-yielding stocks"
- JEF (Jefferies Financial Group Inc.) score 15.8 — "Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages af"
- JIOFIN.BO (Jio Financial Services Limited) score 15.0 — "Jio Financial Services promoter holding rises to 50.98% after 25 crore share allotment"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.2 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.1 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.3 — "Nifty reclaims 23,000 on Oct’s last trading day; IT, Pharma stocks lead"
- SEPN (Septerna, Inc.) score 11.7 — "Q2 results impact: 2 Vedanta stocks rally up to 14% after Sept quarter earnings. How have "
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.8 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- META (Meta) score 8.5 — "Silver price crash deepens as Oct losses hit  ₹45,000/kg; gold falls to 7-month low: Why a"
- VT (Vanguard Total World Stock Ind) score 7.6 — "Japan to Overtake China As World’s Top LNG Importer This Year"
- INFY (Infosys Limited) score 6.6 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- GS (Goldman Sachs Group, Inc. (The) score 5.8 — "Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages af"
- SWIGGY.NS (SWIGGY LIMITED) score 2.0 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.6 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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