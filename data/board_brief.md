# Transmission Layer — board brief · 2026-11-02 22:47Z

data as of **2026-11-02** · 97 series · 13 red / 36 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.784, 2d in regime; vol-pct 0.88, breadth-off 0.688, Markov P(high-vol) 0.264)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.44, contra nifty_50 corr20=0.3, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.12, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 0.07, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.13, corr60 -0.11, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.56, corr60 0.35, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0011540500847815327)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.588, β 0.4859, p 0.0); driver zc -1.53 → expected -0.531%. Type hit-rate 0.829 (n=1674).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.565, β 0.436, p 0.0); driver zc -2.46 → expected -0.792%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.562, β 0.4472, p 0.0); driver zc -2.26 → expected -0.747%. Type hit-rate 0.829 (n=1674).
- **SETUP** vix → asx_200: leads 1d (ccf -0.495, β -0.0446, p 0.0); driver zc 1.69 → expected -0.576%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.47, β 0.1797, p 0.0); driver zc -1.97 → expected -0.643%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.452, β 0.1288, p 0.0); driver zc -2.41 → expected -0.794%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.378, β -2.4982, p 0.00637); driver zc -2.26 → expected 4.175%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.353, β 0.5549, p 0.0); driver zc -2.26 → expected -0.927%. Type hit-rate 0.829 (n=1674).
- **SETUP** vix → india_vix: leads 1d (ccf 0.353, β 0.2351, p 0.01051); driver zc 1.69 → expected 3.034%. Type hit-rate 0.829 (n=1674).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.321, β 0.1408, p 1e-05); driver zc -2.26 → expected -0.235%. Type hit-rate 0.829 (n=1674).
- **SETUP** vix → dyn_4417_t: leads 1d (ccf -0.26, β -0.1069, p 1e-05); driver zc 1.69 → expected -1.379%. Type hit-rate 0.829 (n=1674).
- Track record · residual_reversion: hit-rate **0.507** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=1674) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.72] cross-asset · 4 series ↓
- ust_2y [RATES]: last 4.56, z20 -3.06, zc -0.84, resid-z -0.81 [quiet], 1d -1.08%, |z20|=3.06
- ust_10y [RATES]: last 4.94, z20 -1.79, zc -0.75, resid-z -1.16 [quiet], 1d -0.80%, |z20|=1.79
- tips_10y_real [RATES]: last 2.60, z20 -1.76, zc -0.63, resid-z -0.61 [quiet], 1d -1.14%, |z20|=1.76
- dyn_schd [EQUITIES]: last 35.88, z20 1.62, zc 0.53, resid-z -0.68 [quiet], 1d 0.29%, 1y-pct=100
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: kospi (inverse) — not yet - watch; rho -0.599 vs dyn_schd
- Source: Treasury Yields Extend Past Month’s Slide as Oil Prices Drop — Mint Markets, 2026-11-02. https://www.livemint.com/market/treasury-yields-extend-past-month-s-slide-as-oil-prices-drop-11793656834005.html
- Source: Dividend, bonus issue: Last chance to buy today — Godrej Consumer, Coal India, Asian Paints and others — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/dividend-bonus-issue-last-chance-to-buy-today-godrej-consumer-coal-india-asian-paints-and-others-11793640245000.html
- Source: High-yield US stocks: 10 companies offering dividend yields of up to 16.65% — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/high-yield-us-stocks-10-companies-offering-dividend-yields-of-up-to-16-65/articleshow/135464561.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.57), 2025-05-19 (d=1.16)

### [AMBER 6.69] commodities · 2 series ↓
- brent [COMMODITIES]: last 104.23, z20 -0.86, zc 1.21, resid-z -1.52 [unexplained], 1d -11.40%, 1-session move -11.40% ≥ 1.5%
- wti [COMMODITIES]: last 96.26, z20 -0.23, zc 0.82, resid-z -1.34 [quiet], 1d -7.55%, 1-session move -7.55% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.44 via wti, z -0.22, quiet)
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.534 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.44, z -0.22)
- Source: Treasury Yields Extend Past Month’s Slide as Oil Prices Drop — Mint Markets, 2026-11-02. https://www.livemint.com/market/treasury-yields-extend-past-month-s-slide-as-oil-prices-drop-11793656834005.html
- Source: TSX rebounds as oil pullback boosts industrials, mining shares — Mint Markets, 2026-11-02. https://www.livemint.com/market/tsx-rebounds-as-oil-pullback-boosts-industrials-mining-shares-11793655587408.html
- Source: Trump’s Trillion-Dollar Oil Play: A Trap For Big Oil? — OilPrice, 2026-11-02. https://oilprice.com/Energy/Crude-Oil/Trumps-Trillion-Dollar-Oil-Play-A-Trap-For-Big-Oil.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.56] cross-asset · 4 series ↓
- sp500 [INDICES]: last 7542.33, z20 -2.90, zc -2.46, resid-z -2.23 [unexplained], 1d -0.50%, |z20|=2.90
- vix [INDICES]: last 21.17, z20 2.56, zc 1.69, resid-z n/a [moved], 1d 9.01%, |z20|=2.56
- nasdaq_100 [INDICES]: last 27996.29, z20 -2.40, zc -2.59, resid-z -0.35 [priced], 1d -1.37%, |z20|=2.40
- dyn_vt [EQUITIES]: last 155.12, z20 -2.10, zc -2.26, resid-z 0.41 [priced], 1d -0.14%, |z20|=2.10
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.744 vs sp500, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.833 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.577 vs sp500, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.71 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.621 vs dyn_vt
- Source: Nasdaq 100 Enters Correction as Megacap Results Amplify AI Fears — Mint Markets, 2026-11-02. https://www.livemint.com/market/nasdaq-100-enters-correction-as-megacap-results-amplify-ai-fears-11793658450748.html
- Source: Traders rushing into a leveraged ETF to make a bullish bet on the Nasdaq-100 just got burned — MarketWatch Top, 2026-11-02. https://www.marketwatch.com/story/traders-rushing-into-a-leveraged-etf-to-make-a-bullish-bet-on-the-nasdaq-100-just-got-burned-d6775191?mod=mw_rss_topstories
- Source: Wall Street’s most hated stocks are faring far better than its favorites — MarketWatch Top, 2026-11-02. https://www.marketwatch.com/story/wall-streets-most-hated-stocks-are-faring-far-better-than-its-favorites-4c1d6c68?mod=mw_rss_topstories
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 6.49] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 137.87, z20 -3.17, zc -2.31, resid-z -1.49 [moved], 1d -3.95%, |z20|=3.17; 1y-pct=0
- btc_usd [CRYPTO]: last 76700.00, z20 -2.48, zc -0.43, resid-z 0.48 [quiet], 1d -0.95%, |z20|=2.48
- eth_usd [CRYPTO]: last 2248.26, z20 -1.79, zc -0.05, resid-z 0.34 [quiet], 1d -0.20%, |z20|=1.79
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.62).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: MIZUHO REITERATES $165 TARGET ON STRATEGY ($MSTR ) Mizuho maintained its Outperform rating and $165 price target on Strategy following its Q3 2026 earnings call. Analyst Dan Dolev highlighted a stronger balance sheet, with 848,517 BTC held, net leverage falling to 2.4% from 8.4%, and $5.1 billion in — DeItaone, 2026-11-02. https://t.me/walter_bloomberg/37879
- Source: TRUMP SAYS US COULD SOON CONTROL 50% OF GLOBAL CHIP BUSINESS — DeItaone, 2026-11-02. https://t.me/walter_bloomberg/37877
- Source: Bitcoin holds steady near $78,000 as investors assess Binance security breach. Here is what experts say — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-steady-near-78000-as-investors-assess-binance-security-breach-here-is-what-experts-say/articleshow/135459441.cms
- Historical analogues: 2026-05-22 (d=0.62), 2025-10-16 (d=0.64), 2025-04-10 (d=0.75)

### [RED 5.36] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3956.60, z20 -2.04, zc -2.98, resid-z -2.77 [unexplained], 1d 1.48%, |z20|=2.04; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 50.71, z20 -1.88, zc -2.58, resid-z -0.37 [priced], 1d 3.29%, |z20|=1.88; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 78.02, z20 1.80, zc n/a, resid-z n/a [quiet], 1d -1.75%, |z20|=1.80
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.593 vs comex_silver, historically leads by 1d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.528 vs comex_gold
- Source: Gold, silver prices rebound from multi-month lows as crude oil retreats; what is driving the recovery? — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/november-2-gold-silver-rates-gold-silver-prices-rebound-from-multi-month-lows-as-crude-oil-retreats-11793635178579.html
- Source: Gold edges up ahead of Diwali on festive demand; silver remains steady in Delhi — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/gold/gold-edges-up-ahead-of-diwali-on-festive-demand-silver-remains-steady-in-delhi/article71656866.ece
- Source: Rates crash: Gold price slips 7%, silver tanks 20% in Oct: Is Dhanteras 2026 right time to buy? What should investors do — Mint Markets, 2026-11-02. https://www.livemint.com/market/commodities/rates-crash-gold-price-slips-7-silver-tanks-20-in-oct-is-dhanteras-2026-right-time-to-buy-what-should-investors-do-11793618175891.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.26] nifty_50 ↑
- nifty_50 [INDICES]: last 23440.80, z20 3.26, zc 0.60, resid-z 0.94 [quiet], 1d 1.68%, |z20|=3.26
- **Mechanism**: nifty_50 ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.684 via nifty_50, z -0.22, quiet); nifty_fmcg (rho 0.661 via nifty_50, z -0.06, quiet); dyn_jiofin_bo (rho 0.636 via nifty_50, z 0.22, quiet); dyn_bajfinance_ns (rho 0.607 via nifty_50, z 0.5, quiet); nifty_metal (rho 0.564 via nifty_50, z 0.58, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.684 vs nifty_50, historically leads by 3d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.636 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.746 vs nifty_50
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.542 vs nifty_50, historically leads by 2d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.661 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.684, z -0.22); nifty_fmcg (rho 0.661, z -0.06); dyn_jiofin_bo (rho 0.636, z 0.22); dyn_bajfinance_ns (rho 0.607, z 0.5)
- Source: Surge in Reliance lifts Sensex by 1.6%; Nifty tops 23,400 — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/surge-in-reliance-lifts-sensex-by-16-nifty-tops-23400/article71657468.ece
- Source: Sensex, Nifty tomorrow 3 Nov: Will stock market jump on Sebi's 12.5% foreign ‌investors LTCG tax removal recommendation? — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/sensex-nifty-tomorrow-3-nov-will-stock-market-jump-on-sebis-12-5-foreign-investors-ltcg-tax-removal-recommendation-11793629514612.html
- Source: Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-ril-tata-steel-infosys-icici-bank-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/135462862.cms
- Historical analogues: 2026-01-14 (d=0.0), 2025-07-18 (d=0.05), 2025-01-27 (d=0.11)

### [RED 5.2] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 931.00, z20 -3.20, zc -0.56, resid-z -0.63 [quiet], 1d -6.91%, |z20|=3.20; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.58 via dyn_policybzr_ns, z 0.5, quiet); nifty_midcap_100 (rho 0.527 via dyn_policybzr_ns, z -0.22, quiet); nifty_50 (rho 0.5 via dyn_policybzr_ns, z 3.26, reacted); dyn_indusindbk_bo (rho 0.456 via dyn_policybzr_ns, z -1.43, reacted); nifty_fmcg (rho 0.368 via dyn_policybzr_ns, z -0.06, quiet)
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.58 vs dyn_policybzr_ns, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.724 vs dyn_policybzr_ns
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.527 vs dyn_policybzr_ns
- **India receivers**: dyn_bajfinance_ns (rho 0.58, z 0.5); nifty_midcap_100 (rho 0.527, z -0.22); nifty_50 (rho 0.5, z 3.26); dyn_indusindbk_bo (rho 0.456, z -1.43)
- Source: Broker’s call: PB Fintech (Buy) — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/brokers-call-pb-fintech-buy/article71656563.ece
- Source: MobiKwik shares zoom 10% as fintech firm posts record Rs 12 crore profit in Q2 — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/mobikwik-shares-zoom-10-as-fintech-firm-posts-record-rs-12-crore-profit-in-q2/articleshow/135452378.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [RED 4.66] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1774.60, z20 2.66, zc 1.71, resid-z 1.27 [moved], 1d 1.06%, |z20|=2.66; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.371 via dyn_atherenerg_ns, z -0.22, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.371, z -0.22)
- Source: Best EV stock to buy: Ather Energy vs Ola Electric Mobility; which is better profit-making deal? Investors guide, target — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/best-ev-stock-to-buy-ather-energy-vs-ola-electric-mobility-which-is-better-profit-making-deal-investors-guide-target-11793608999266.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.51), dyn_jef ↑ (4.42), dyn_tgt ↑ (4.19), rates · 2 series ↑ (3.9), indices · 2 series ↑ (3.68), dyn_4417_t ↑ (3.65), usd_cny ↓ (3.64), shanghai_comp ↓ (3.49), dyn_sepn ↑ (3.28), dyn_tech ↑ (3.27), eur_usd ↓ (2.42), usd_brl ↑ (2.37)

## India macro
- nifty_50: 23440.8008 (1d 1.68%, z20 3.26, flag red)
- nifty_midcap_100: 57985.2500 (1d 1.19%, z20 -0.22, flag none)
- usd_inr: 94.8900 (1d -0.28%, z20 -0.75, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4737 (1d -0.49%, z20 -1.63, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.6 — "LIBERMAN BACKS EISENKOT, RULES OUT COALITION WITH NETANYAHU Israeli opposition leader Avig"
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.6 — "India tax filers shift toward investments and trading, says ClearTax data"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.9 — "India tax filers shift toward investments and trading, says ClearTax data"
- INDIANB.NS (INDIAN BANK) score 47.8 — "Indian R&D laggards underperform market as innovation-focused firms pull ahead"
- OHI (Omega Healthcare Investors, In) score 45.8 — "Rates crash: Gold price slips 7%, silver tanks 20% in Oct: Is Dhanteras 2026 right time to"
- TGT (Target Corporation) score 40.7 — "MIZUHO REITERATES $165 TARGET ON STRATEGY ($MSTR ) Mizuho maintained its Outperform rating"
- BAC (Bank of America Corporation) score 40.1 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.1 — "Broker’s call: PB Fintech (Buy)"
- HDB (HDFC Bank Limited) score 36.1 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.7 — "Broker’s call: PB Fintech (Buy)"
- TECH (Bio-Techne Corp) score 35.7 — "Broker’s call: PB Fintech (Buy)"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.5 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- IDBI.NS (IDBI BANK LIMITED) score 34.4 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.4 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- COIN (Coinbase Global, Inc.) score 33.8 — "TRUMP SAYS US COULD SOON CONTROL 50% OF GLOBAL CHIP BUSINESS"
- RS (Reliance, Inc.) score 30.0 — "Surge in Reliance lifts Sensex by 1.6%; Nifty tops 23,400"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.2 — "4 Energy Stocks for Midterm Elections That Could Go Either Way"
- 301077.SZ (CHINASTARS) score 27.4 — "TRUMP SAYS US LEADS CHINA IN AI SUPERINTELLIGENCE BY WIDE MARGIN"
- CHKP (Check Point Software Technolog) score 27.2 — "Brazil's Data Center Boom Faces a 14-GW Reality Check"
- LTH (Life Time Group Holdings, Inc.) score 23.3 — "Rates crash: Gold price slips 7%, silver tanks 20% in Oct: Is Dhanteras 2026 right time to"
- BOND (PIMCO Active Bond Exchange-Tra) score 19.8 — "Oil slide hands India's 10-year bond its best day since early April"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.5 — "HPCL vs BPCL, IOCL vs ONGC: Which OMC stock to buy as $110/bbl crude oil price becomes a n"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.3 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.3 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 12.0 — "Fusion Finance swings to Rs 86.5 crore profit as asset quality improves"
- JIOFIN.BO (Jio Financial Services Limited) score 11.3 — "Tech Query: Sundram Fasteners, HDB Financial Services, Sterlite Technologies, Techno Elect"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.6 — "Dividend, bonus issue: Last chance to buy today — Godrej Consumer, Coal India, Asian Paint"
- SCHD (Schwab US Dividend Equity ETF) score 10.6 — "High-yield US stocks: 10 companies offering dividend yields of up to 16.65%"
- VT (Vanguard Total World Stock Ind) score 10.0 — "ADNOC Chief Says World Has “Eroded Its Supply Buffers”"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.7 — "Fusion Finance swings to Rs 86.5 crore profit as asset quality improves"
- JEF (Jefferies Financial Group Inc.) score 8.5 — "Delhivery shares soar 6% after Q2 results; JPMorgan, Jefferies, Kotak, Citi maintain buy c"
- META (Meta) score 8.4 — "El Niño likely to pose supply risks in mining and metals sector"
- GS (Goldman Sachs Group, Inc. (The) score 7.3 — "Goldman hikes oil-price forecasts on ‘substantial’ supply risks"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.2 — "How Iran Just Broke the U.S. Oil Shield In Saudi Arabia Yet Again"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.8 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- SEPN (Septerna, Inc.) score 6.5 — "Nifty holds Sept highs at midday; Reliance surges 7.4%, IT stocks drag"
- INFY (Infosys Limited) score 6.0 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.2 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.9 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
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