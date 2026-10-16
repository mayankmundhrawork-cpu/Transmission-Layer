# Transmission Layer — board brief · 2026-10-16 22:49Z

data as of **2026-10-16** · 97 series · 17 red / 28 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.816, 10d in regime; vol-pct 0.808, breadth-off 0.824, Markov P(high-vol) 0.049)
- [INVERTED] **safe_haven_gold** — corr20 -0.24, corr60 -0.39, contra nifty_50 corr20=0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.27, corr60 0.21, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 0.13, last shift 2026-08-26. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.02, last shift 2026-08-12. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.15, corr60 -0.26, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.49, corr60 0.23, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 8.99588777714122e-06)
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.556, β 0.642, p 0.0); driver zc -2.18 → expected -1.602%. Type hit-rate 0.814 (n=2052).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.552, β 0.6392, p 0.0); driver zc -2.18 → expected -1.595%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → asx_200: leads 1d (ccf -0.503, β -0.046, p 0.0); driver zc 2.68 → expected -0.984%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.483, β -0.0878, p 0.0); driver zc 2.68 → expected -1.878%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.441, β -0.0817, p 0.0); driver zc 2.68 → expected -1.748%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.433, β 0.0284, p 0.0); driver zc 2.68 → expected 0.608%. Type hit-rate 0.814 (n=2052).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.428, β -0.179, p 0.0); driver zc -2.18 → expected 0.447%. Type hit-rate 0.814 (n=2052).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.411, β 0.716, p 0.0); driver zc -2.18 → expected -1.787%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → kospi: leads 1d (ccf -0.354, β -0.0968, p 0.0); driver zc 2.68 → expected -2.07%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → india_vix: leads 1d (ccf 0.339, β 0.227, p 0.01469); driver zc 2.68 → expected 4.854%. Type hit-rate 0.814 (n=2052).
- **SETUP** vix → nifty_metal: leads 1d (ccf -0.287, β -0.0463, p 0.00103); driver zc 2.68 → expected -0.991%. Type hit-rate 0.814 (n=2052).
- Track record · residual_reversion: hit-rate **0.501** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.814** (n=2052) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 13.39] cross-asset · 4 series ↓
- vix [INDICES]: last 19.98, z20 6.72, zc 2.68, resid-z n/a [moved], 1d 21.39%, 1-session move +21.39% ≥ 15.0%; |z20|=6.72
- nasdaq_100 [INDICES]: last 29188.64, z20 -3.46, zc -2.18, resid-z -0.68 [priced], 1d -2.50%, |z20|=3.46
- russell_2000 [INDICES]: last 2721.87, z20 -2.61, zc -1.28, resid-z -0.91 [quiet], 1d -1.64%, |z20|=2.61
- dyn_vt [EQUITIES]: last 156.81, z20 -2.46, zc -1.16, resid-z -0.35 [quiet], 1d -0.95%, |z20|=2.46
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-05-06 (z-distance 0.18).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.542 vs russell_2000, historically leads by 1d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.523 vs russell_2000, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.585 vs dyn_vt
- Source: CBOE VOLATILITY INDEX JUMPS TO OVER FOUR-MONTH HIGH, LAST UP 4.97 POINTS AT 21.41 — DeItaone, 2026-10-16. https://t.me/walter_bloomberg/37256
- Source: NASDAQ 100 INDEX EXTENDS DECLINE TO 2% — DeItaone, 2026-10-16. https://t.me/walter_bloomberg/37250
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market subdued as AI stocks weigh on traders’ risk appetite — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-rate-yield-earnings-tesla-nvidia-nebius-coreweave-varonis-systems-ai-chip-stock-price-news-16th-october-2026/liveblog/134994983.cms
- Historical analogues: 2025-05-06 (d=0.18), 2025-08-18 (d=0.25), 2025-04-29 (d=0.26)

### [RED 10.35] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1790.00, z20 7.03, zc 4.43, resid-z 4.44 [unexplained], 1d 8.48%, |z20|=7.03; 1y-pct=100
- nifty_it [INDICES]: last 31924.10, z20 4.13, zc 2.32, resid-z 1.95 [unexplained], 1d 3.92%, |z20|=4.13
- dyn_tataelxsi_ns [EQUITIES]: last 3850.10, z20 3.62, zc 1.66, resid-z 1.07 [moved], 1d 4.06%, |z20|=3.62
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.559 via nifty_it, z 3.24, reacted); nifty_50 (rho 0.512 via dyn_tataelxsi_ns, z 0.82, quiet); nifty_fmcg (rho 0.468 via dyn_tataelxsi_ns, z -0.66, quiet); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -3.57, reacted); dyn_tatatech_ns (rho 0.392 via nifty_it, z 0.68, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.512 vs dyn_tataelxsi_ns
- **India receivers**: dyn_justdial_bo (rho 0.559, z 3.24); nifty_50 (rho 0.512, z 0.82); nifty_fmcg (rho 0.468, z -0.66); midcap_largecap_ratio (rho -0.439, z -3.57)
- Source: Kotak Mahindra Bank among 5 stocks that hit 52-week highs & rallied up to 15% in a month — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/kotak-mahindra-bank-among-5-stocks-that-hit-52-week-highs-amp-rallied-up-to-15-in-a-month/slideshow/134995212.cms
- Source: Worst over for IT stocks? Experts analyse Q2 results of TCS, HCL, Tech Mahindra and others, suggest top picks — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/worst-over-for-it-stocks-experts-analyse-q2-results-of-tcs-hcl-tech-mahindra-and-others-suggest-top-picks-11792149864702.html
- Source: Market wrap: Tech Mahindra, TCS, InterGlobe, BSE top gainers and losers on Nifty and Sensex on Friday — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tech-mahindra-tcs-interglobe-bse-top-gainers-and-losers-on-nifty-and-sensex-on-friday/articleshow/134992216.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 8.59] commodities · 2 series ↑
- brent [COMMODITIES]: last 109.69, z20 2.76, zc 1.99, resid-z -0.44 [priced], 1d 3.56%, 1-session move +3.56% ≥ 1.5%; |z20|=2.76
- wti [COMMODITIES]: last 99.04, z20 2.10, zc 0.47, resid-z -1.28 [quiet], 1d 1.09%, |z20|=2.10
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.608 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.573 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.56 vs brent
- Source: US stocks: US market ends down sharply; worries about AI trade and high oil prices weigh — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-down-sharply-worries-about-ai-trade-and-high-oil-prices-weigh/articleshow/135003266.cms
- Source: Norway's Untapped Oil and Gas Frontier Is Drawing Renewed Interest — OilPrice, 2026-10-16. https://oilprice.com/Energy/Crude-Oil/Norways-Untapped-Oil-and-Gas-Frontier-Is-Drawing-Renewed-Interest.html
- Source: U.S. Oil Drillers Back Off Even As Prices Soar — OilPrice, 2026-10-16. https://oilprice.com/Energy/Energy-General/US-Oil-Drillers-Back-Off-Even-As-Prices-Soar.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.46] usd_inr ↓
- usd_inr [FX]: last 94.95, z20 -2.46, zc -0.40, resid-z 0.28 [quiet], 1d -0.21%, 20d range extreme; |z20|=2.46
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.371 via usd_inr, z -0.09, quiet); dyn_karurvysya_ns (rho -0.366 via usd_inr, z 2.99, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.371, z -0.09); dyn_karurvysya_ns (rho -0.366, z 2.99)
- Source: Sitharaman pitches rupee mechanism to bridge global forex crunch, trade disruptions — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/economy/sitharaman-pitches-rupee-mechanism-to-bridge-global-forex-crunch-trade-disruptions/article71592229.ece
- Source: Rupee rises 1.9% in a week, closes below 95 per dollar — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-1-9-in-a-week-closes-below-95-per-dollar/articleshow/134996292.cms
- Source: Rupee posts best week in seven months, fundamentals key for lasting turnaround — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/forex/rupee-posts-best-week-in-seven-months-fundamentals-key-for-lasting-turnaround/articleshow/134991672.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.86] dyn_dell ↓
- dyn_dell [EQUITIES]: last 451.60, z20 -3.86, zc -0.78, resid-z -1.69 [unexplained], 1d -4.60%, |z20|=3.86
- **Mechanism**: dyn_dell ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: MICHAEL DELL REVEALS HOW HIS COMPANY COULD SURVIVE AN AI BUST Dell Technologies ($DELL ) is positioning itself to withstand a potential AI downturn through just-in-time manufacturing and a negative cash conversion cycle. Unlike heavily indebted AI infrastructure providers, Dell largely builds server — DeItaone, 2026-10-16. https://t.me/walter_bloomberg/37241
- Source: Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Boom Collapses Dell Says He Expects Memory Crunch to Get Worse — DeItaone, 2026-10-16. https://t.me/walter_bloomberg/37240
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

### [RED 5.16] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 73.28, z20 2.16, zc n/a, resid-z n/a [quiet], 1d -0.13%, GSR<75 (extreme low); |z20|=2.16
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.526 vs gold_silver_ratio, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 5.01] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7380.00, z20 3.01, zc 4.54, resid-z -0.92 [moved], 1d 15.67%, |z20|=3.01; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Worst over for IT stocks? Experts analyse Q2 results of TCS, HCL, Tech Mahindra and others, suggest top picks — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/worst-over-for-it-stocks-experts-analyse-q2-results-of-tcs-hcl-tech-mahindra-and-others-suggest-top-picks-11792149864702.html
- Source: Stock to buy after SEBI CAS new rule: Experts bullish on Groww brand parent Billionbrains Garage Ventures shares; target — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/stock-to-buy-after-sebi-cas-new-rule-experts-bullish-on-groww-brand-parent-billionbrains-garage-ventures-shares-target-11792143458424.html
- Source: Gold vs silver vs platinum: Which metal saw biggest rally since last Dussehra? Experts explain outlook — Mint Markets, 2026-10-16. https://www.livemint.com/market/commodities/gold-vs-silver-vs-platinum-which-metal-saw-biggest-rally-since-last-dussehra-experts-explain-outlook-11792142307625.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.99] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 355.65, z20 2.99, zc 1.49, resid-z 1.53 [unexplained], 1d 2.89%, |z20|=2.99; 1y-pct=100
- **Mechanism**: dyn_karurvysya_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho 0.453 via dyn_karurvysya_ns, z 1.77, reacted); dyn_muthootfin_ns (rho 0.389 via dyn_karurvysya_ns, z -1.25, reacted); nifty_50 (rho 0.378 via dyn_karurvysya_ns, z 0.82, quiet); usd_inr (rho -0.366 via dyn_karurvysya_ns, z -2.46, reacted)
- **India receivers**: dyn_indianb_ns (rho 0.453, z 1.77); dyn_muthootfin_ns (rho 0.389, z -1.25); nifty_50 (rho 0.378, z 0.82); usd_inr (rho -0.366, z -2.46)
- Source: Karur Vysya Bank shares jump 6% to hit a 52-week high after Q2 results - Should you buy? Rationale, target price — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/karur-vysya-bank-shares-jump-6-to-hit-a-52-week-high-after-q2-results-should-you-buy-rationale-target-price-11792125152481.html
- Source: Karur Vysya Bank shares rally 6% after Q2 profit jumps 37% YoY — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/karur-vysya-bank-shares-rally-6-after-q2-profit-jumps-37-yoy/articleshow/134982900.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

## Watchlist (below surfacing floor)
dyn_wit ↑ (4.66), dyn_nvda ↓ (4.63), crypto · 2 series ↓ (4.52), dyn_hdb ↑ (4.45), shanghai_comp ↓ (4.3), dyn_bac ↓ (4.08), dyn_rs ↑ (3.96), usd_cny ↓ (3.85), midcap_largecap_ratio ↓ (3.57), tips_10y_real ↓ (3.39), commodities · 3 series ↓ (3.39), dyn_muthootfin_ns ↓ (3.25)

## India macro
- nifty_50: 23146.1504 (1d 0.65%, z20 0.82, flag none)
- nifty_midcap_100: 59130.8516 (1d -0.10%, z20 -0.70, flag none)
- usd_inr: 94.9500 (1d -0.21%, z20 -2.46, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5547 (1d -0.75%, z20 -3.57, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 109.9 — "US Fed rate hike: US inflation heats up — experts decode impact on Indian stock market, go"
- INDIANB.NS (INDIAN BANK) score 109.6 — "US Fed rate hike: US inflation heats up — experts decode impact on Indian stock market, go"
- INOXINDIA.NS (INOX INDIA LIMITED) score 104.9 — "US Fed rate hike: US inflation heats up — experts decode impact on Indian stock market, go"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 104.0 — "US Fed rate hike: US inflation heats up — experts decode impact on Indian stock market, go"
- BAC (Bank of America Corporation) score 99.3 — "BOJ'S UEDA SIGNALS FURTHER RATE HIKES AS INFLATION NEARS 2% Bank of Japan Governor Kazuo U"
- HDB (HDFC Bank Limited) score 93.2 — "BOJ'S UEDA SIGNALS FURTHER RATE HIKES AS INFLATION NEARS 2% Bank of Japan Governor Kazuo U"
- IDBI.NS (IDBI BANK LIMITED) score 88.7 — "BOJ'S UEDA SIGNALS FURTHER RATE HIKES AS INFLATION NEARS 2% Bank of Japan Governor Kazuo U"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 88.7 — "BOJ'S UEDA SIGNALS FURTHER RATE HIKES AS INFLATION NEARS 2% Bank of Japan Governor Kazuo U"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 88.7 — "BOJ'S UEDA SIGNALS FURTHER RATE HIKES AS INFLATION NEARS 2% Bank of Japan Governor Kazuo U"
- TECHM.NS (TECH MAHINDRA LIMITED) score 85.1 — "MICHAEL DELL REVEALS HOW HIS COMPANY COULD SURVIVE AN AI BUST Dell Technologies ($DELL ) i"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 82.3 — "MICHAEL DELL REVEALS HOW HIS COMPANY COULD SURVIVE AN AI BUST Dell Technologies ($DELL ) i"
- TECH (Bio-Techne Corp) score 82.3 — "MICHAEL DELL REVEALS HOW HIS COMPANY COULD SURVIVE AN AI BUST Dell Technologies ($DELL ) i"
- COIN (Coinbase Global, Inc.) score 69.5 — "Global Energy Import Dependence Set to Peak by 2034, Rystad Says"
- OHI (Omega Healthcare Investors, In) score 63.3 — "The bond market shrugged off two inflation shocks. Why stock investors should pay attentio"
- CHKP (Check Point Software Technolog) score 45.9 — "Cult.fit IPO alert: Fitness major receives SEBI nod for proposed IPO - Check OFS, fresh is"
- TGT (Target Corporation) score 45.7 — "BOJ'S UEDA SIGNALS FURTHER RATE HIKES AS INFLATION NEARS 2% Bank of Japan Governor Kazuo U"
- BOND (PIMCO Active Bond Exchange-Tra) score 41.6 — "The bond market shrugged off two inflation shocks. Why stock investors should pay attentio"
- RS (Reliance, Inc.) score 31.1 — "Reliance-backed Jio Platforms IPO:  ₹1 lakh crore gains for Meta, Google in  ₹30,213 cr is"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 28.7 — "Global Energy Import Dependence Set to Peak by 2034, Rystad Says"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 28.0 — "US Fed rate hike: US inflation heats up — experts decode impact on Indian stock market, go"
- LTH (Life Time Group Holdings, Inc.) score 27.6 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- SEPN (Septerna, Inc.) score 25.5 — "US CRUDE FUTURES RISE OVER $3 TO SESSION HIGH OF $101.02, MOST SINCE SEPT 21"
- 301077.SZ (CHINASTARS) score 24.0 — "TRUMP: WILL GET A DEAL ON NUCLEAR ARMS WITH RUSSIA AND CHINA"
- JIOFIN.BO (Jio Financial Services Limited) score 23.4 — "China's central bank to boost support for global investors in financial markets"
- BZ=F (Brent Crude Oil Last Day Finan) score 19.4 — "CBOE VOLATILITY INDEX JUMPS TO OVER FOUR-MONTH HIGH, LAST UP 4.97 POINTS AT 21.41"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 18.9 — "Top 3 stocks to buy: Bajaj Finance, Dr Reddy's Lab, Grasim Industries by Sumeet Bagadia | "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.4 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Details"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.4 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Details"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.4 — "Top 3 stocks to buy: Bajaj Finance, Dr Reddy's Lab, Grasim Industries by Sumeet Bagadia | "
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.4 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.6 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- NVDA (NVIDIA Corporation) score 9.6 — "GERMANY PLANS MAJOR AI PARTNERSHIP WITH NVIDIA — HANDELSBLATT German Chancellor Friedrich "
- META (Meta) score 8.7 — "Reliance-backed Jio Platforms IPO:  ₹1 lakh crore gains for Meta, Google in  ₹30,213 cr is"
- VT (Vanguard Total World Stock Ind) score 8.0 — "U.S. Wants World Bank to Drop Ban on Upstream Oil and Gas Funding"
- GS (Goldman Sachs Group, Inc. (The) score 8.0 — "Wipro shares rise over 2% as Q2 revenue grows 9% YoY. What are Nomura, Goldman Sachs analy"
- JEF (Jefferies Financial Group Inc.) score 6.5 — "Jefferies technical analyst finds an encouraging development in Thursday rebound, setting "
- WIT (Wipro Limited) score 5.9 — "Wipro shares rise 5%, up 15% so far in October - Should you buy this IT stock after Q2 res"
- DELL (Dell Technologies Inc.) score 2.1 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.8 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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