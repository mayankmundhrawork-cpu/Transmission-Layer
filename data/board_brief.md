# Transmission Layer — board brief · 2026-09-25 09:35Z

data as of **2026-09-25** · 97 series · 7 red / 41 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.665, 1d in regime; vol-pct 0.441, breadth-off 0.889, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.24, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.0, corr60 0.11, last shift 2026-08-12. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-08-05. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.41, corr60 0.21, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.182475943819263e-05)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.481, β 0.2126, p 0.0); driver zc 2.28 → expected 0.632%. Type hit-rate 0.828 (n=2451).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.474, β 0.2528, p 0.0); driver zc 3.12 → expected 0.765%. Type hit-rate 0.828 (n=2451).
- **SETUP** dyn_bond → usd_jpy: leads 1d (ccf -0.415, β -0.7709, p 0.0); driver zc -1.64 → expected 0.499%. Type hit-rate 0.828 (n=2451).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.359, β -0.1201, p 0.0); driver zc 2.28 → expected -0.357%. Type hit-rate 0.828 (n=2451).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.273, β -0.1104, p 0.0); driver zc 3.12 → expected -0.334%. Type hit-rate 0.828 (n=2451).
- Track record · residual_reversion: hit-rate **0.497** (n=1100) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2451) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.17] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 87.56, z20 -2.39, zc -1.64, resid-z -0.15 [priced], 1d -0.65%, |z20|=2.39; 1y-pct=0
- tips_10y_real [RATES]: last 2.76, z20 2.24, zc 2.66, resid-z 2.36 [unexplained], 1d 4.94%, 1d move +13.0bps ≥ 5bps; |z20|=2.24; 1y-pct=100
- ust_10y [RATES]: last 5.11, z20 2.13, zc 3.12, resid-z 2.64 [unexplained], 1d 3.02%, |z20|=2.13; 1y-pct=100
- ust_30y [RATES]: last 5.40, z20 2.07, zc 2.73, resid-z 2.34 [unexplained], 1d 2.08%, |z20|=2.07; 1y-pct=100
- ust_2y [RATES]: last 4.85, z20 1.87, zc 2.28, resid-z 1.49 [moved], 1d 2.97%, |z20|=1.87; 1y-pct=100
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.621 vs dyn_bond, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.525 vs dyn_bond, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.596 vs dyn_bond
- Watch next: sp500 (co-move) — not yet - watch; rho 0.544 vs dyn_bond
- Source: Indian 10-year bond hits 4-month low on US debt rout — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/bonds/indian-10-year-bond-hits-4-month-low-on-us-debt-rout/articleshow/134479074.cms
- Source: US Market: Bond fund managers turn cautious as yields, AI debt raise risks — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-bond-fund-managers-turn-cautious-as-yields-ai-debt-raise-risks/articleshow/134475249.cms
- Source: Global Market: Japanese investors eye home assets as rising bond yields alter returns — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japanese-investors-eye-home-assets-as-rising-bond-yields-alter-returns/articleshow/134474944.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.25] fx · 4 series ↓
- usd_mxn [FX]: last 17.66, z20 3.58, zc 1.05, resid-z 1.21 [quiet], 1d 0.68%, |z20|=3.58
- gbp_usd [FX]: last 1.32, z20 -2.62, zc -0.09, resid-z -0.07 [quiet], 1d -0.04%, |z20|=2.62
- aud_usd [FX]: last 0.70, z20 -2.54, zc -0.04, resid-z 0.16 [quiet], 1d -0.03%, |z20|=2.54
- eur_usd [FX]: last 1.14, z20 -2.17, zc 0.30, resid-z 0.66 [quiet], 1d 0.10%, |z20|=2.17; 1y-pct=4
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.504 via usd_mxn, z -4.51, reacted); dyn_icicigi_bo (rho -0.493 via gbp_usd, z 1.05, reacted); dyn_muthootfin_ns (rho 0.467 via aud_usd, z -0.39, quiet); dyn_inoxindia_ns (rho 0.44 via aud_usd, z 0.13, quiet); nifty_50 (rho 0.385 via eur_usd, z -1.43, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.545 vs aud_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.412 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_policybzr_ns (rho -0.504, z -4.51); dyn_icicigi_bo (rho -0.493, z 1.05); dyn_muthootfin_ns (rho 0.467, z -0.39); dyn_inoxindia_ns (rho 0.44, z 0.13)
- Source: Philip R. Lane: The Outlook for the Euro Area Economy — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260923_1~ac21bf46e3.en.pdf
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.51] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 1161.90, z20 -4.51, zc -0.13, resid-z -1.17 [quiet], 1d -3.75%, |z20|=4.51; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.602 via dyn_policybzr_ns, z -1.73, reacted); nifty_50 (rho 0.481 via dyn_policybzr_ns, z -1.43, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.715 vs dyn_policybzr_ns
- **India receivers**: nifty_midcap_100 (rho 0.602, z -1.73); nifty_50 (rho 0.481, z -1.43)
- Source: How to trade PB Fintech shares after falling 12% from day’s high? This technical analyst explains — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/news/how-to-trade-pb-fintech-shares-after-falling-12-from-days-high-this-technical-analyst-explains/articleshow/134477427.cms
- Source: PB Fintech's 36% bloodbath rattles market, but Jefferies stays bullish. What does it see in Policybazaar parent? — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/news/pb-fintechs-36-bloodbath-rattles-market-but-jefferies-stays-bullish-what-does-it-see-in-policybazaar-parent/articleshow/134475050.cms
- Source: PB Fintech shares slump 40% in two sessions| What Jefferies, Morgan Stanley, BofA say on the stock — Mint Markets, 2026-09-25. https://www.livemint.com/market/stock-market-news/pb-fintech-shares-slump-40-in-two-sessions-what-jefferies-morgan-stanley-bofa-say-on-the-stock-11790308344209.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [AMBER 6.26] commodities · 2 series ↓
- wti [COMMODITIES]: last 92.86, z20 -0.42, zc -0.65, resid-z 0.83 [quiet], 1d -1.85%, 1-session move -1.85% ≥ 1.5%
- brent [COMMODITIES]: last 98.63, z20 -0.33, zc -2.62, resid-z 0.98 [priced], 1d -7.48%, 1-session move -7.48% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dax (inverse) — not yet - watch; rho -0.554 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.582 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.545 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.506 vs wti
- Source: JPMorgan CEO Jamie Dimon warns Trump against punishing India; gives this advice on Russian oil imports — Mint Markets, 2026-09-25. https://www.livemint.com/market/stock-market-news/jpmorgan-ceo-jamie-dimon-warns-trump-against-punishing-india-gives-this-advice-on-russian-oil-imports-11790326652038.html
- Source: Global Market: European shares rise as oil prices ease; Middle East tensions keep investors cautious — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-rise-as-oil-prices-ease-middle-east-tensions-keep-investors-cautious/articleshow/134480611.cms
- Source: Brent crude price falls below $106 as US-Iran deal talks emerge — BusinessLine Mkts, 2026-09-25. https://www.thehindubusinessline.com/markets/commodities/brent-crude-falls-below-106-as-us-iran-deal-talks-emerge/article71507075.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [AMBER 5.63] cross-asset · 3 series ↓
- dyn_ms [EQUITIES]: last 196.23, z20 -2.31, zc -0.59, resid-z 0.12 [quiet], 1d -1.09%, |z20|=2.31
- dow_jones [INDICES]: last 51349.18, z20 -1.68, zc -0.40, resid-z 0.03 [quiet], 1d -0.32%, |z20|=1.68
- russell_2000 [INDICES]: last 2835.78, z20 -1.66, zc -0.08, resid-z 0.26 [quiet], 1d -0.10%, |z20|=1.66
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.743 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.721 vs dyn_ms, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.641 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.621 vs dow_jones, historically leads by 2d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.618 vs dyn_ms, historically leads by 2d
- Source: PB Fintech shares slump 40% in two sessions| What Jefferies, Morgan Stanley, BofA say on the stock — Mint Markets, 2026-09-25. https://www.livemint.com/market/stock-market-news/pb-fintech-shares-slump-40-in-two-sessions-what-jefferies-morgan-stanley-bofa-say-on-the-stock-11790308344209.html
- Source: Here’s how to position your portfolio for the next AI wave, according to Morgan Stanley — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/heres-how-to-position-your-portfolio-for-the-next-ai-wave-according-to-morgan-stanley-ac8f8a4a?mod=mw_rss_topstories
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks edge lower as crude gains on Mideast uncertainty, eyes on Trump-Xi talks — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-trump-xi-china-talks-iran-war-hormuz-brent-crude-oil-inflation-fed-rate-treasury-yields-meta-apple-tesla-amazon-ai-chip-stock-price-news-24th-september-2026/liveblog/134462304.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-27 (d=0.32), 2026-05-14 (d=0.54)

### [RED 5.34] natgas ↑
- natgas [COMMODITIES]: last 3.26, z20 3.34, zc -0.23, resid-z 4.16 [unexplained], 1d -1.12%, |z20|=3.34
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.447 via natgas, z -4.51, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.082 vs natgas, historically leads by 4d
- **India receivers**: dyn_policybzr_ns (rho -0.447, z -4.51)
- Source: U.S. to Back Argentina’s First LNG Export Project With $6 Billion Loan — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/US-to-Back-Argentinas-First-LNG-Export-Project-With-6-Billion-Loan.html
- Source: Southeast Asia Keeps Building Gas Plants Despite Hormuz LNG Shock — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Southeast-Asia-Keeps-Building-Gas-Plants-Despite-Hormuz-LNG-Shock.html
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 4.63] dyn_indusindbk_bo ↓
- dyn_indusindbk_bo [EQUITIES]: last 914.65, z20 -2.63, zc -0.20, resid-z -0.90 [quiet], 1d -0.60%, |z20|=2.63
- **Mechanism**: dyn_indusindbk_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.459 via dyn_indusindbk_bo, z -1.73, reacted); nifty_50 (rho 0.427 via dyn_indusindbk_bo, z -1.43, reacted); nifty_metal (rho 0.375 via dyn_indusindbk_bo, z -0.24, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.459, z -1.73); nifty_50 (rho 0.427, z -1.43); nifty_metal (rho 0.375, z -0.24)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank News — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-today-live-25-sep-2026/liveblog/134474146.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

### [AMBER 4.5] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2710.99, z20 1.67, zc 0.22, resid-z 0.21 [quiet], 1d 0.88%, |z20|=1.67
- btc_usd [CRYPTO]: last 84723.61, z20 1.59, zc 0.14, resid-z 0.02 [quiet], 1d 0.41%, |z20|=1.59
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-22 (z-distance 0.12).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.353 via btc_usd, z -0.08, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.543 vs btc_usd, historically leads by 1d
- **India receivers**: dyn_cartrade_ns (rho 0.353, z -0.08)
- Source: What Bitcoin’s $16 billion options expiry means for investors — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/cryptocurrency/what-bitcoins-16-billion-options-expiry-means-for-investors/articleshow/134453599.cms
- Source: Cryptocurrency future: Bitcoin prices trading above $80k - What's behind the rally? What lies ahead? — Mint Markets, 2026-09-24. https://www.livemint.com/market/cryptocurrency/cryptocurrency-future-bitcoin-prices-trading-above-80k-whats-behind-the-rally-what-lies-ahead-11790218140136.html
- Source: Bitcoin holds near $86,000 as spot Bitcoin ETF inflows hit 11-month high of $999 million — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-86000-as-spot-bitcoin-etf-inflows-hit-11-month-high-of-999-million/articleshow/134432852.cms
- Historical analogues: 2026-07-22 (d=0.12), 2025-06-09 (d=0.14), 2026-04-14 (d=0.17)

## Watchlist (below surfacing floor)
dyn_meta ↑ (4.45), gold_silver_ratio ↓ (4.11), nasdaq_100 ↑ (3.97), dyn_tech ↑ (3.84), hang_seng ↓ (3.8), comex_copper ↑ (3.46), nifty_50 ↓ (3.43), dyn_jiofin_bo ↓ (3.41), dyn_voltas_ns ↓ (3.32), dyn_4417_t ↑ (3.31), commodities · 2 series ↓ (2.79), sofr ↑ (2.14)

## India macro
- nifty_50: 23110.5000 (1d 0.21%, z20 -1.43, flag amber)
- nifty_midcap_100: 60836.0508 (1d -0.26%, z20 -1.73, flag amber)
- usd_inr: 95.8475 (1d 0.11%, z20 0.95, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6324 (1d -0.46%, z20 -1.33, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 90.4 — "Stock recommendations for 25 September from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.1 — "Stock recommendations for 25 September from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.6 — "Stock recommendations for 25 September from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 62.2 — "IndusInd Bank Share Price Live Updates: IndusInd Bank News"
- COIN (Coinbase Global, Inc.) score 53.3 — "Global Market: Japanese shares rise on AI stocks, dividend buying; Nikkei up 1.2%"
- OHI (Omega Healthcare Investors, In) score 53.2 — "Axiom Gas Engineering SME IPO shares to list today: Key details investors should know"
- HDB (HDFC Bank Limited) score 49.3 — "IndusInd Bank Share Price Live Updates: IndusInd Bank News"
- BAC (Bank of America Corporation) score 47.1 — "IndusInd Bank Share Price Live Updates: IndusInd Bank News"
- CHKP (Check Point Software Technolog) score 46.5 — "Gold price outlook: Gold set for a weekly loss, but can it rebound? Check 2026 forecast"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.9 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.9 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- TECH (Bio-Techne Corp) score 42.9 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- IDBI.NS (IDBI BANK LIMITED) score 40.4 — "IndusInd Bank Share Price Live Updates: IndusInd Bank News"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.4 — "IndusInd Bank Share Price Live Updates: IndusInd Bank News"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.4 — "IndusInd Bank Share Price Live Updates: IndusInd Bank News"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.9 — "Global Market: Japanese investors eye home assets as rising bond yields alter returns"
- 301077.SZ (CHINASTARS) score 35.6 — "XI TOLD TRUMP CHINA'S POSITION ON SAFEGUARDING ITS NATIONAL UNITY AND TERRITORIAL INTEGRIT"
- SEPN (Septerna, Inc.) score 34.4 — "Stock recommendations for 25 September from MarketSmith India"
- LTH (Life Time Group Holdings, Inc.) score 30.2 — "800% gains, 106 multibaggers in 3 years; now every second Nifty 500 stock is down in 2026."
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.9 — "5 Energy Stocks Positioned for a Prolonged Iran War"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.6 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.6 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- JIOFIN.BO (Jio Financial Services Limited) score 18.9 — "Financial stocks lead correction as insurance overhaul plan sparks fears"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.2 — "Bonus issue record date today: Last chance to buy Aastha Spintex shares as deadline approa"
- POLICYBZR.NS (PB FINTECH LIMITED) score 15.0 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- META (Meta) score 12.9 — "Meta stock jumps 36% in September as Muse AI fuels rally"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.1 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.2 — "Just One Commodity Vessel Left the Strait of Hormuz on Wednesday"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.2 — "Embassy REIT raises ₹1,000 cr via debentures to refinance debt"
- MS (Morgan Stanley) score 8.7 — "PB Fintech shares slump 40% in two sessions| What Jefferies, Morgan Stanley, BofA say on t"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.6 — "ICICI Lombard General Insurance among 3 stocks showing White Marubozu Pattern"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.3 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- VT (Vanguard Total World Stock Ind) score 8.2 — "Beyond high-profile wars, a worldwide battle for critical minerals"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.2 — "Retail investors raise stakes in 10 smallcaps; 3 turn multibaggers in 3 months"
- GS (Goldman Sachs Group, Inc. (The) score 5.1 — "Goldman Sachs buys stake in Firstcry brand parent owner Brainbees Solutions | Check price,"
- PINELABS.NS (PINE LABS LIMITED) score 4.3 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- NVDA (NVIDIA Corporation) score 3.4 — "FORMER OPENAI DATA CENTER CHIEF CHRIS MALONE IS NOW AT NVIDIA - THE INFORMATION"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.9 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- VOLTAS.NS (VOLTAS LTD) score 1.6 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.9 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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