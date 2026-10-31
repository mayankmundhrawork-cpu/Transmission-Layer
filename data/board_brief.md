# Transmission Layer — board brief · 2026-10-31 00:55Z

data as of **2026-10-31** · 97 series · 10 red / 40 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.81, 1d in regime; vol-pct 0.797, breadth-off 0.824, Markov P(high-vol) 0.243)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.45, contra nifty_50 corr20=0.28, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.11, last shift 2026-09-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.01, corr60 0.08, last shift 2026-09-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-14. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 -0.0, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.13, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.54, corr60 0.34, last shift 2026-07-28. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.002977997490474893)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.589, β 0.4865, p 0.0); driver zc -1.52 → expected -0.528%. Type hit-rate 0.83 (n=1664).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.566, β 0.4365, p 0.0); driver zc -2.44 → expected -0.788%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.563, β 0.4476, p 0.0); driver zc -2.34 → expected -0.774%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.558, β 0.3433, p 0.0); driver zc -2.34 → expected -0.593%. Type hit-rate 0.83 (n=1664).
- **SETUP** vix → asx_200: leads 1d (ccf -0.496, β -0.0447, p 0.0); driver zc 1.7 → expected -0.582%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.47, β 0.1798, p 0.0); driver zc -2.0 → expected -0.652%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.452, β 0.1289, p 0.0); driver zc -2.44 → expected -0.793%. Type hit-rate 0.83 (n=1664).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.443, β 0.1928, p 0.0); driver zc -2.58 → expected -0.667%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.377, β -2.4907, p 0.00655); driver zc -2.34 → expected 4.304%. Type hit-rate 0.83 (n=1664).
- **SETUP** vix → india_vix: leads 1d (ccf 0.351, β 0.2339, p 0.01084); driver zc 1.7 → expected 3.047%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.349, β 0.5521, p 0.0); driver zc -2.34 → expected -0.954%. Type hit-rate 0.83 (n=1664).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.321, β 0.141, p 1e-05); driver zc -2.34 → expected -0.244%. Type hit-rate 0.83 (n=1664).
- Track record · residual_reversion: hit-rate **0.506** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=1664) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.36] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3884.90, z20 -4.04, zc -3.28, resid-z -0.72 [priced], 1d -3.63%, |z20|=4.04; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 49.13, z20 -2.96, zc -2.54, resid-z 0.07 [priced], 1d -5.86%, |z20|=2.96; 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 79.07, z20 2.63, zc n/a, resid-z n/a [quiet], 1d 2.36%, |z20|=2.63
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.573 vs comex_silver, historically leads by 1d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.54 vs comex_gold
- Source: Why gold plunged to its lowest price in a year despite renewed Iran jitters — MarketWatch Top, 2026-10-30. https://www.marketwatch.com/story/why-gold-plunged-to-its-lowest-price-in-a-year-despite-renewed-iran-jitters-365be0e2?mod=mw_rss_topstories
- Source: Silver price crash deepens as Oct losses hit  ₹45,000/kg; gold falls to 7-month low: Why are precious metals sinking? — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/silver-price-crash-deepens-as-oct-losses-hit-rs-45-000-kg-gold-falls-to-7-month-low-why-are-precious-metals-sinking-11793368770318.html
- Source: SPOT GOLD EXTENDS LOSSES, DOWN 3% TO $3,908.13/OZ — DeItaone, 2026-10-30. https://t.me/walter_bloomberg/37820
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.76] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 143.51, z20 -3.45, zc -2.29, resid-z -0.22 [moved], 1d -10.64%, |z20|=3.45; 1y-pct=1
- btc_usd [CRYPTO]: last 77340.26, z20 -2.27, zc 0.35, resid-z 0.28 [quiet], 1d 0.81%, |z20|=2.27
- eth_usd [CRYPTO]: last 2245.07, z20 -1.79, zc 0.09, resid-z 0.37 [quiet], 1d 0.36%, |z20|=1.79
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.54).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: India flags global energy disruptions caused by sanctions and chokepoints — BusinessLine Mkts, 2026-10-31. https://www.thehindubusinessline.com/news/india-flags-global-energy-disruptions-caused-by-sanctions-and-chokepoints/article71648064.ece
- Source: Intel stock plunges 30% as weak PC demand and AI costs trigger global chip selloff — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/intel-plunges-25-as-weak-pc-demand-and-ai-costs-trigger-global-chip-selloff/articleshow/135371230.cms
- Source: RUSSIA'S NOVAK SAYS ATTACKS ON OIL REFINERIES WILL HAVE NEGATIVE IMPACT ON DIESEL FUEL SUPPLIES TO GLOBAL MARKET — DeItaone, 2026-10-30. https://t.me/walter_bloomberg/37825
- Historical analogues: 2026-05-22 (d=0.54), 2025-10-16 (d=0.56), 2025-04-10 (d=0.66)

### [RED 6.5] cross-asset · 4 series ↓
- sp500 [INDICES]: last 7580.95, z20 -2.84, zc -2.44, resid-z -0.95 [priced], 1d -1.81%, |z20|=2.84
- dyn_vt [EQUITIES]: last 155.24, z20 -2.37, zc -2.34, resid-z 0.24 [priced], 1d -1.73%, |z20|=2.37
- nasdaq_100 [INDICES]: last 28385.75, z20 -2.24, zc -2.58, resid-z -1.07 [moved], 1d -3.46%, |z20|=2.24
- vix [INDICES]: last 19.44, z20 1.69, zc 1.70, resid-z n/a [moved], 1d 13.02%, |z20|=1.69
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.744 vs sp500, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.842 vs sp500
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.529 vs nasdaq_100, historically leads by 3d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.702 vs sp500
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.56 vs dyn_vt
- Source: Has the tech bubble burst? Why the Nasdaq’s rough ride looks eerily like 2000. — MarketWatch Top, 2026-10-30. https://www.marketwatch.com/story/has-the-tech-bubble-burst-why-the-nasdaqs-rough-ride-looks-eerily-like-2000-5bcefcb2?mod=mw_rss_topstories
- Source: This cybersecurity stock will be the next to join the S&P 500 — MarketWatch Top, 2026-10-30. https://www.marketwatch.com/story/this-cybersecurity-stock-will-be-the-next-to-join-the-s-p-500-dc976803?mod=mw_rss_topstories
- Source: Microsoft is winning the cloud wars and becoming Wall Street’s new golden child — MarketWatch Top, 2026-10-30. https://www.marketwatch.com/story/microsoft-is-winning-the-cloud-wars-and-becoming-wall-streets-new-golden-child-62eecbbd?mod=mw_rss_topstories
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 6.27] cross-asset · 4 series ↓
- ust_2y [RATES]: last 4.61, z20 -2.61, zc -1.00, resid-z -0.99 [quiet], 1d -1.28%, |z20|=2.61
- dyn_schd [EQUITIES]: last 35.79, z20 1.71, zc 0.56, resid-z 0.92 [quiet], 1d 0.51%, 1y-pct=100
- tips_10y_real [RATES]: last 2.63, z20 -1.67, zc -0.82, resid-z -0.85 [quiet], 1d -1.50%, |z20|=1.67
- ust_10y [RATES]: last 4.98, z20 -1.60, zc -1.30, resid-z -1.45 [quiet], 1d -1.39%, |z20|=1.60
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.512 vs dyn_schd, historically leads by 4d
- Watch next: dyn_tgt (co-move) — not yet - watch; rho 0.592 vs dyn_schd
- Watch next: kospi (inverse) — not yet - watch; rho -0.587 vs dyn_schd
- Source: Dividend stocks alert: Record date Mon 2 Nov: Colgate Palmolive vs Pitti Engineering vs Route Mobile vs Tanla Platforms — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/dividend-stocks-alert-record-date-mon-2-nov-colgate-palmolive-vs-pitti-engineering-vs-route-mobile-vs-tanla-platforms-11793377023477.html
- Source: NALCO shares: Up 242% in 3 years, is there more rally left in this Navratna PSU? Check Q2 results date, dividend history — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/nalco-shares-up-242-in-3-years-is-there-more-rally-left-in-this-navratna-psu-check-q2-results-date-dividend-history-11793346545175.html
- Source: India's 10-year bond heads for first weekly gain in 11 weeks, set to end record losing run — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/indias-10-year-bond-heads-for-first-weekly-gain-in-11-weeks-set-to-end-record-losing-run/article71644234.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.57), 2025-05-19 (d=1.16)

### [AMBER 5.79] brent ↑
- brent [COMMODITIES]: last 112.33, z20 0.79, zc -1.11, resid-z -3.56 [unexplained], 1d -2.22%, 1-session move -2.22% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.366 via brent, z -0.92, quiet)
- **India receivers**: nifty_midcap_100 (rho -0.366, z -0.92)
- Source: Europe Is Now Seriously Rethinking Its Oil Refinery Phase Down — OilPrice, 2026-10-30. https://oilprice.com/Energy/Crude-Oil/Europe-Is-Now-Seriously-Rethinking-Its-Oil-Refinery-Phase-Down.html
- Source: Gasoline Up 34% and Heating Oil Up 74% as Voters Head to the Midterms — OilPrice, 2026-10-30. https://oilprice.com/Energy/Gas-Prices/Gasoline-Up-34-and-Heating-Oil-Up-74-as-Voters-Head-to-the-Midterms.html
- Source: U.S. Oil, Gas Drillers Still on Hold — OilPrice, 2026-10-30. https://oilprice.com/Energy/Energy-General/US-Oil-Gas-Drillers-Still-on-Hold.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.53] dyn_cartrade_ns ↓
- dyn_cartrade_ns [EQUITIES]: last 2173.00, z20 -3.53, zc -1.83, resid-z -2.16 [unexplained], 1d -6.54%, |z20|=3.53
- **Mechanism**: dyn_cartrade_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3,377. Here’s why — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/cartrade-tech-shares-tank-over-6-after-q2-results-but-nomura-raises-target-price-to-rs-3377-heres-why/articleshow/135290221.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 4.47] dyn_lth ↑
- dyn_lth [EQUITIES]: last 45.10, z20 2.47, zc -0.18, resid-z 2.10 [unexplained], 1d -0.55%, |z20|=2.47; 1y-pct=96
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CBOE VOLATILITY INDEX RISES ABOVE 20 POINTS FOR FIRST TIME IN A WEEK — DeItaone, 2026-10-30. https://t.me/walter_bloomberg/37832
- Source: European Gas Tops 101 Euros for First Time Since 2022 — OilPrice, 2026-10-30. https://oilprice.com/Latest-Energy-News/World-News/European-Gas-Tops-101-Euros-for-First-Time-Since-2022.html
- Source: Borosil shares skyrocket 16% after strong Q2 results | Is it time to book profits? Target price, stop loss here — Mint Markets, 2026-10-30. https://www.livemint.com/market/stock-market-news/borosil-shares-skyrocket-16-after-strong-q2-results-is-it-time-to-book-profits-target-price-stop-loss-here-11793335910559.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [AMBER 4.23] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 389.00, z20 -2.23, zc -0.77, resid-z -0.86 [quiet], 1d -1.04%, |z20|=2.23
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India shares fall 3% after Q2 results; Jefferies, Motilal Oswal, others cut target price — ET Markets, 2026-10-30. https://economictimes.indiatimes.com/markets/stocks/news/coal-india-shares-fall-3-after-q2-results-jefferies-motilal-oswal-others-cut-target-price/articleshow/135349282.cms
- Source: Why Coal India shares fell 2% despite strong Q2 revenue growth — BusinessLine Mkts, 2026-10-30. https://www.thehindubusinessline.com/markets/stock-markets/coal-india-shares-slip-2-after-q2-ebitda-misses-despite-strong-revenue-beat/article71643744.ece
- Source: Q2 October dividend champions: Infosys, Colgate, HUL, CPCL, Coal India | Big payouts - amount, record date — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/october-dividend-champions-infosys-colgate-hul-chennai-petro-coal-india-announce-big-payouts-check-amount-record-11793286004751.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

## Watchlist (below surfacing floor)
shanghai_comp ↓ (4.21), dyn_301077_sz ↓ (4.1), dyn_rs ↑ (3.94), dyn_jiofin_bo ↓ (3.8), nifty_50 ↑ (3.74), dyn_sepn ↑ (3.73), dyn_tech ↑ (3.59), dyn_4417_t ↑ (3.46), eur_usd ↓ (3.34), dyn_atherenerg_ns ↑ (3.16), dyn_techm_ns ↑ (3.02), usd_cny ↓ (2.81)

## India macro
- nifty_50: 23053.0996 (1d 0.51%, z20 1.74, flag amber)
- nifty_midcap_100: 57304.4492 (1d -0.92%, z20 -0.92, flag none)
- usd_inr: 94.9400 (1d -0.28%, z20 -0.74, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4858 (1d -1.42%, z20 -1.59, flag amber)
- Next India prints: NSDL FPI flows T-2d · IMD weekly rainfall T-2d · RBI Weekly Statistical Supplement T-6d · Kharif sowing data T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 95.2 — "India flags global energy disruptions caused by sanctions and chokepoints"
- COALINDIA.NS (COAL INDIA LTD) score 95.0 — "India flags global energy disruptions caused by sanctions and chokepoints"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 93.7 — "India flags global energy disruptions caused by sanctions and chokepoints"
- INDIANB.NS (INDIAN BANK) score 72.1 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- BAC (Bank of America Corporation) score 64.1 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- TGT (Target Corporation) score 61.7 — "F - *FORD CEO TARGETS A 20% JUMP IN SALES - SOURCES SAY"
- COIN (Coinbase Global, Inc.) score 57.2 — "India flags global energy disruptions caused by sanctions and chokepoints"
- HDB (HDFC Bank Limited) score 56.1 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 54.9 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- IDBI.NS (IDBI BANK LIMITED) score 54.8 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 54.8 — "Sebi issues final order against Axis Capital, imposes regulatory censure; Axis Bank shares"
- OHI (Omega Healthcare Investors, In) score 53.2 — "ANTHROPIC MAY NOT SECURE INVESTMENT-GRADE RATING AFTER IPO, BLACKSTONE TELLS INVESTORS - F"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.0 — "Has the tech bubble burst? Why the Nasdaq’s rough ride looks eerily like 2000."
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.1 — "Has the tech bubble burst? Why the Nasdaq’s rough ride looks eerily like 2000."
- TECH (Bio-Techne Corp) score 43.1 — "Has the tech bubble burst? Why the Nasdaq’s rough ride looks eerily like 2000."
- CHKP (Check Point Software Technolog) score 40.8 — "After IPO listing, Jio Platforms Q2 results 2026 announced: Check ARPU, profit, revenue, E"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.8 — "India flags global energy disruptions caused by sanctions and chokepoints"
- RS (Reliance, Inc.) score 33.7 — "Reliance Industries Q2 Results 2026 Live: RIL Q2 profit jumps 41% YoY to Rs 25,548 crore; "
- LTH (Life Time Group Holdings, Inc.) score 29.5 — "CBOE VOLATILITY INDEX RISES ABOVE 20 POINTS FOR FIRST TIME IN A WEEK"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.0 — "India bonds buckle for fourth straight month on oil's climb"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 23.1 — "Reliance Industries Q2 results 2026 today: Preview, should you buy, sell or hold ahead of "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.5 — "Tata Capital among 4 Nifty500 stocks closing above VWAP"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 20.5 — "Tata Capital among 4 Nifty500 stocks closing above VWAP"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.6 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- 301077.SZ (CHINASTARS) score 19.2 — "Japan to Overtake China As World’s Top LNG Importer This Year"
- SCHD (Schwab US Dividend Equity ETF) score 15.1 — "Big dividends, bigger losses? The hidden risk in Wall Street's highest-yielding stocks"
- JIOFIN.BO (Jio Financial Services Limited) score 15.0 — "ANT - ANTHROPIC FACES JUNK CREDIT RATING RISK DESPITE PLANNED MEGA-IPO Blackstone has warn"
- JEF (Jefferies Financial Group Inc.) score 14.8 — "Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages af"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.4 — "Reddit’s stock logs its biggest one-day drop ever. It’s not the last of the bad news, anal"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.3 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.2 — "Market wrap:  Shriram Finance, Nestle India, Trent, InterGlobe top gainers and losers on N"
- SEPN (Septerna, Inc.) score 10.9 — "Q2 results impact: 2 Vedanta stocks rally up to 14% after Sept quarter earnings. How have "
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.1 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- META (Meta) score 9.0 — "TECH STOCK SELLOFF: BIGGEST NAMES FALL SHARPLY FROM THEIR PEAKS Down 20% or more: 🔸 $AVGO "
- VT (Vanguard Total World Stock Ind) score 7.1 — "Japan to Overtake China As World’s Top LNG Importer This Year"
- INFY (Infosys Limited) score 6.2 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- GS (Goldman Sachs Group, Inc. (The) score 5.4 — "Asian Paints shares see target price cuts by Jefferies, Goldman Sachs, other brokerages af"
- SWIGGY.NS (SWIGGY LIMITED) score 1.8 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.5 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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