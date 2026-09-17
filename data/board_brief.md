# Transmission Layer — board brief · 2026-09-17 22:51Z

data as of **2026-09-17** · 97 series · 10 red / 35 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.553, 1d in regime; vol-pct 0.459, breadth-off 0.647, Markov P(high-vol) 0.031)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.27, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.2, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.08, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.84, last shift 2026-07-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.07, last shift 2026-07-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.28, corr60 0.16, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.551, β 0.6392, p 0.0); driver zc 1.74 → expected 1.098%. Type hit-rate 0.822 (n=2092).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.542, β 0.8506, p 0.0); driver zc 1.53 → expected 0.96%. Type hit-rate 0.822 (n=2092).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.488, β -0.0884, p 0.0); driver zc -1.65 → expected 1.133%. Type hit-rate 0.822 (n=2092).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.464, β 0.2794, p 0.0); driver zc 1.53 → expected 0.315%. Type hit-rate 0.822 (n=2092).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.447, β 0.1985, p 0.0); driver zc 1.74 → expected 0.341%. Type hit-rate 0.822 (n=2092).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.437, β -0.0302, p 0.0); driver zc -1.65 → expected 0.387%. Type hit-rate 0.822 (n=2092).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.43, β -0.2453, p 0.0); driver zc 1.53 → expected -0.277%. Type hit-rate 0.822 (n=2092).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.415, β -0.1746, p 0.0); driver zc 1.74 → expected -0.3%. Type hit-rate 0.822 (n=2092).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.415, β 0.0271, p 0.0); driver zc -1.65 → expected -0.348%. Type hit-rate 0.822 (n=2092).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.407, β 0.6999, p 0.0); driver zc 1.74 → expected 1.202%. Type hit-rate 0.822 (n=2092).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.359, β 0.8318, p 0.0); driver zc 1.53 → expected 0.939%. Type hit-rate 0.822 (n=2092).
- **SETUP** vix → kospi: leads 1d (ccf -0.351, β -0.0941, p 0.0); driver zc -1.65 → expected 1.206%. Type hit-rate 0.822 (n=2092).
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.306, β 0.4345, p 0.0); driver zc 1.8 → expected 0.258%. Type hit-rate 0.822 (n=2092).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.255, β 0.3658, p 3e-05); driver zc 1.8 → expected 0.217%. Type hit-rate 0.822 (n=2092).
- Track record · residual_reversion: hit-rate **0.497** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2092) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.4] cross-asset · 9 series ↑
- tips_10y_real [RATES]: last 2.68, z20 2.77, zc 1.33, resid-z 0.46 [quiet], 1d 2.29%, 1d move +6.0bps ≥ 5bps; |z20|=2.77; 1y-pct=100
- ust_2y [RATES]: last 4.74, z20 2.41, zc 1.15, resid-z 0.04 [quiet], 1d 1.50%, |z20|=2.41; 1y-pct=100
- dyn_ms [EQUITIES]: last 203.48, z20 -2.33, zc 0.28, resid-z -0.58 [quiet], 1d 0.52%, |z20|=2.33
- ust_10y [RATES]: last 5.01, z20 2.12, zc 0.21, resid-z -0.58 [quiet], 1d 0.20%, |z20|=2.12; 1y-pct=100
- dow_jones [INDICES]: last 51776.48, z20 -1.93, zc 0.69, resid-z -0.70 [quiet], 1d 0.61%, |z20|=1.93
- ust_30y [RATES]: last 5.35, z20 1.57, zc -0.24, resid-z -0.64 [quiet], 1d -0.19%, |z20|=1.57; 1y-pct=98
- russell_2000 [INDICES]: last 2875.10, z20 -1.57, zc 0.50, resid-z -0.79 [quiet], 1d 0.57%, |z20|=1.57
- brent [COMMODITIES]: last 104.07, z20 1.11, zc -0.58, resid-z 0.18 [quiet], 1d -1.66%, 1-session move -1.66% ≥ 1.5%
- dyn_bond [EQUITIES]: last 89.08, z20 -1.11, zc 1.80, resid-z 0.19 [priced], 1d 0.59%, 1y-pct=2
- **Mechanism**: cross-asset · 9 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.429 via ust_2y, z -0.3, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.717 vs dyn_ms, historically leads by 4d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.582 vs dyn_ms, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.766 vs dyn_ms
- Watch next: sp500 (co-move) — not yet - watch; rho 0.738 vs dyn_ms
- Watch next: vix (inverse) — not yet - watch; rho -0.646 vs dyn_ms
- **India receivers**: midcap_largecap_ratio (rho -0.429, z -0.3)
- Source: Turkey Bets $108 Billion on Wind and Solar While Expanding Oil and Gas — OilPrice, 2026-09-17. https://oilprice.com/Alternative-Energy/Renewable-Energy/Turkey-Bets-108-Billion-on-Wind-and-Solar-While-Expanding-Oil-and-Gas.html
- Source: The 10-year Treasury is having its worst run in over 100 years. Why investors are buying bonds anyway. — MarketWatch Top, 2026-09-17. https://www.marketwatch.com/story/the-bond-market-is-seeing-trouble-why-investors-are-buying-now-anyway-065a2f9f?mod=mw_rss_topstories
- Source: US stocks today: US stocks rebound as tech rally gains momentum on easing oil, yields — ET Markets, 2026-09-17. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-rebound-as-tech-rally-gains-momentum-on-easing-oil-yields/articleshow/134320980.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.65), 2025-05-12 (d=0.74)

### [RED 4.97] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5560.00, z20 2.97, zc 0.75, resid-z 0.28 [quiet], 1d 2.77%, |z20|=2.97; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Apollo Micro Systems share price jumps 3.5% after recent fall | technical experts flag key levels — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/apollo-micro-systems-share-price-jumps-3-5-after-recent-fall-technical-experts-flag-key-levels-11789626185762.html
- Source: NSE IPO buzz lifts New India Assurance, IFCI up to 9% | What do technical experts say? — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/nse-ipo-buzz-lifts-new-india-assurance-ifci-up-to-9-what-do-technical-experts-say-11789623090580.html
- Source: Sensex, Nifty soar despite Fed rate hike — Is it NSE IPO impact and 6 listings today? Experts decode stock market rise — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/sensex-nifty-soar-despite-fed-rate-hike-is-it-nse-ipo-impact-and-6-listings-today-experts-decode-stock-market-rise-11789621059076.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.78] dyn_bac ↓
- dyn_bac [EQUITIES]: last 58.17, z20 -2.78, zc 0.25, resid-z -2.13 [unexplained], 1d 0.47%, |z20|=2.78
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho 0.35 via dyn_bac, z -0.23, quiet)
- **India receivers**: eur_inr (rho 0.35, z -0.23)
- Source: America Is Paying a Lot for Fuel, Not Running Out of Gasoline — OilPrice, 2026-09-17. https://oilprice.com/Latest-Energy-News/World-News/America-Is-Paying-a-Lot-for-Fuel-Not-Running-Out-of-Gasoline.html
- Source: TRUMP: LOWER INTEREST RATES FOR UNITED STATES OF AMERICA, AND FAST — DeItaone, 2026-09-16. https://t.me/walter_bloomberg/35874
- Source: TRUMP DEMANDS U.S. INTEREST RATES AT 1% OR LOWER President Trump is calling for U.S. interest rates to be cut to 1% or below, arguing America’s credit strength and booming investment justify dramatically cheaper borrowing. He also criticized U.S. trade deficits, claiming the country is effectively “ — DeItaone, 2026-09-16. https://t.me/walter_bloomberg/35872
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.5] cross-asset · 2 series ↓
- nifty_50 [INDICES]: last 23270.60, z20 -1.67, zc 0.42, resid-z 0.23 [quiet], 1d 0.23%, |z20|=1.67
- dyn_jiofin_bo [EQUITIES]: last 229.50, z20 -1.28, zc 1.47, resid-z 1.35 [quiet], 1d 2.00%, 1y-pct=2
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-06 (z-distance 0.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.617 via nifty_50, z -1.77, reacted); nifty_fmcg (rho 0.608 via nifty_50, z -0.82, quiet); nifty_it (rho 0.501 via nifty_50, z -1.39, reacted); dyn_techm_ns (rho 0.483 via nifty_50, z -0.65, quiet); dyn_indianb_ns (rho 0.465 via dyn_jiofin_bo, z -1.83, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.608 vs nifty_50, historically leads by 3d
- **India receivers**: nifty_midcap_100 (rho 0.617, z -1.77); nifty_fmcg (rho 0.608, z -0.82); nifty_it (rho 0.501, z -1.39); dyn_techm_ns (rho 0.483, z -0.65)
- Source: Nifty faces a crucial test on Friday: Will recovery continue or support levels give way? — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/nifty-faces-a-crucial-test-on-friday-will-recovery-continue-or-support-levels-give-way-11789658462453.html
- Source: Market wrap:  HDFC Life, Tata Motors PV, BEL, HDFC Bank, ONGC top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-09-17. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-hdfc-life-tata-motors-pv-bel-hdfc-bank-ongc-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134310473.cms
- Source: Sensex today | Stock Market Highlights: Nifty, Sensex close flat as high crude price concerns offset value buying — BusinessLine Mkts, 2026-09-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-17th-september-2026/article71472777.ece
- Historical analogues: 2025-08-06 (d=0.09), 2025-07-29 (d=0.53), 2025-07-18 (d=0.65)

### [RED 4.46] fx · 2 series ↓
- gbp_usd [FX]: last 1.34, z20 -3.63, zc -2.39, resid-z -2.24 [unexplained], 1d -0.84%, |z20|=3.63
- eur_usd [FX]: last 1.15, z20 -3.48, zc -1.63, resid-z -1.55 [unexplained], 1d -0.49%, |z20|=3.48
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.39 via gbp_usd, z -0.93, quiet); nifty_50 (rho 0.387 via eur_usd, z -1.67, reacted); dyn_muthootfin_ns (rho 0.361 via gbp_usd, z -1.28, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.574 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.39, z -0.93); nifty_50 (rho 0.387, z -1.67); dyn_muthootfin_ns (rho 0.361, z -1.28)
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 4.35] dyn_jef ↓
- dyn_jef [EQUITIES]: last 47.87, z20 -2.35, zc 0.39, resid-z -0.65 [quiet], 1d 1.10%, |z20|=2.35
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Solar Industries’ defence share may fall to 22-25% by FY30 after Omnia deal: Jefferies — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-defence-share-may-fall-to-22-25-by-fy30-after-omnia-deal-jefferies/articleshow/134280191.cms
- Source: Solar Industries shares plunge 17% in 2 days. Why Jefferies, Nuvama still see up to 46% upside — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-shares-plunge-17-in-2-days-why-jefferies-nuvama-still-see-up-to-46-upside/articleshow/134279133.cms
- Source: Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estimates after new UPI charges — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-jump-7-as-jefferies-other-brokerages-raise-target-prices-and-earnings-estimates-after-new-upi-charges/articleshow/134278132.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [AMBER 4.14] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 66.61, z20 -1.14, zc n/a, resid-z n/a [quiet], 1d -2.40%, GSR<75 (extreme low)
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.359 via gold_silver_ratio, z -1.77, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.867 vs gold_silver_ratio
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.638 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.359, z -1.77)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 3.84] fx · 2 series ↑
- usd_mxn [FX]: last 17.17, z20 3.01, zc 0.29, resid-z 0.42 [quiet], 1d 0.12%, |z20|=3.01
- aud_usd [FX]: last 0.71, z20 -1.83, zc -0.41, resid-z -0.36 [quiet], 1d -0.18%, |z20|=1.83
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.481 via aud_usd, z -1.28, reacted); dyn_karurvysya_ns (rho -0.358 via usd_mxn, z -1.41, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.539 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_muthootfin_ns (rho 0.481, z -1.28); dyn_karurvysya_ns (rho -0.358, z -1.41)
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-25 (d=0.08), 2025-01-31 (d=0.11)

## Watchlist (below surfacing floor)
ig_oas ↓ (3.45), dyn_voltas_ns ↓ (3.4), midcap_largecap_ratio ↓ (3.3), usd_cny ↓ (3.27), soybeans ↑ (3.26), dyn_tech ↑ (2.98), dyn_icicigi_bo ↓ (2.93), ust_2s10s ↓ (2.74), dxy ↑ (2.62), dyn_hdb ↓ (2.58), commodities · 2 series ↑ (2.25), dyn_dell ↑ (2.15)

## India macro
- nifty_50: 23270.5996 (1d 0.23%, z20 -1.67, flag amber)
- nifty_midcap_100: 61433.7500 (1d 0.91%, z20 -1.77, flag amber)
- usd_inr: 95.9200 (1d -0.08%, z20 1.27, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6400 (1d 0.68%, z20 -0.30, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.5 — "India’s basmati acreage dips, production poised to fall"
- COALINDIA.NS (COAL INDIA LTD) score 72.4 — "India’s basmati acreage dips, production poised to fall"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 70.9 — "India’s basmati acreage dips, production poised to fall"
- INDIANB.NS (INDIAN BANK) score 65.8 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- BAC (Bank of America Corporation) score 57.8 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- OHI (Omega Healthcare Investors, In) score 52.1 — "Tesla’s upcoming product frenzy could leave investors disappointed"
- COIN (Coinbase Global, Inc.) score 51.8 — "Global Market: European shares advance as investors await Bank of England decision"
- HDB (HDFC Bank Limited) score 49.4 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- IDBI.NS (IDBI BANK LIMITED) score 45.7 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.7 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.7 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- BOND (PIMCO Active Bond Exchange-Tra) score 42.7 — "The 10-year Treasury is having its worst run in over 100 years. Why investors are buying b"
- CHKP (Check Point Software Technolog) score 36.5 — "Small-cap under  ₹100: Textile stock jumps 4% following this order update | Check details"
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.4 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Tech leads Wall St to hig"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 33.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Tech leads Wall St to hig"
- TECH (Bio-Techne Corp) score 33.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Tech leads Wall St to hig"
- SEPN (Septerna, Inc.) score 30.3 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- LTH (Life Time Group Holdings, Inc.) score 28.8 — "Wall Street is betting Trump backs down on Iran — but what if the ‘TACO’ trade fails this "
- 301077.SZ (CHINASTARS) score 24.4 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.0 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.1 — "Noel Tata tables ₹25,000 cr SP Group share monetisation plan for Tata Sons"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.1 — "Noel Tata tables ₹25,000 cr SP Group share monetisation plan for Tata Sons"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.8 — "Russian Fuel Exports Rebound in August But Still Down 50% From Last Year"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.3 — "SS Retail IPO Day 2; GMP at 19%, subscribed 1.44 times; Check key details"
- JIOFIN.BO (Jio Financial Services Limited) score 10.9 — "SEBI bars Kore Digital from fundraising, alleges financial manipulation"
- MS (Morgan Stanley) score 9.9 — "WALL STREET RETHINKS “ONE-AND-DONE” FED HIKE The Fed’s hawkish September meeting is pushin"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.6 — "‘I just want out’: Why Jeffrey Gundlach is moving his money as far from AI as possible — a"
- NVDA (NVIDIA Corporation) score 8.5 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.5 — "Tata Sons Listing: 1st board meeting after RBI directive — Only 3 options, one is IPO, che"
- VT (Vanguard Total World Stock Ind) score 8.2 — "World stocks rebound, Treasury yields retreat after Fed, BoE decisions"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.1 — "Gold jewellery sector seeks MDR exemption on high-value UPI transactions"
- JEF (Jefferies Financial Group Inc.) score 5.8 — "Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estim"
- META (Meta) score 5.4 — "US Fed rate hike impact on gold: FOMC outcome on yellow metal decoded"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.6 — "Indonesia's new finance minister faces an uphill battle on fiscal credibility"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.5 — "HDFC Bank is winning the mutual fund vote over ICICI Bank. Can the shift last?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.3 — "Suzlon Energy, Adani Power share prices fall: Check 1-week, 1-year and 5-year returns"
- VOLTAS.NS (VOLTAS LTD) score 0.9 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.8 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
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