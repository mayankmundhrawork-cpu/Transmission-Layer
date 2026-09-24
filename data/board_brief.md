# Transmission Layer — board brief · 2026-09-24 23:56Z

data as of **2026-09-24** · 97 series · 10 red / 39 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.586, 5d in regime; vol-pct 0.485, breadth-off 0.688, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.35, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.08, corr60 0.22, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.11, corr60 0.13, last shift 2026-08-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.08, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-08-04. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.17, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **8 of 89** scanned series survive multiplicity control (effective p ≤ 0.008290602722071938)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1096) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2421) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 20.01] cross-asset · 8 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1207.20, z20 -15.51, zc -12.58, resid-z -17.71 [unexplained], 1d -36.00%, |z20|=15.51; 1y-pct=0
- usd_mxn [FX]: last 17.73, z20 5.49, zc 6.05, resid-z 6.60 [unexplained], 1d 2.59%, |z20|=5.49
- aud_usd [FX]: last 0.70, z20 -3.84, zc -3.38, resid-z -3.73 [unexplained], 1d -1.45%, |z20|=3.84
- gbp_usd [FX]: last 1.32, z20 -3.61, zc -2.75, resid-z -3.00 [unexplained], 1d -0.98%, |z20|=3.61
- eur_usd [FX]: last 1.14, z20 -2.88, zc -2.00, resid-z -2.19 [unexplained], 1d -0.60%, |z20|=2.88; 1y-pct=2
- nifty_midcap_100 [INDICES]: last 60992.25, z20 -1.74, zc -3.09, resid-z -2.26 [unexplained], 1d -2.24%, |z20|=1.74
- nifty_50 [INDICES]: last 23063.10, z20 -1.73, zc -3.22, resid-z -2.32 [unexplained], 1d -1.64%, |z20|=1.73; 1y-pct=3
- india_vix [INDICES]: last 12.62, z20 1.44, zc 3.88, resid-z n/a [moved], 1d 21.98%, 1-session move +21.98% ≥ 15.0%
- **Mechanism**: cross-asset · 8 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-06 (z-distance 1.05).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.641 via nifty_50, z -1.0, reacted); midcap_largecap_ratio (rho 0.587 via nifty_midcap_100, z -0.39, quiet); nifty_metal (rho 0.536 via nifty_midcap_100, z -0.49, quiet); nifty_fmcg (rho 0.529 via nifty_50, z -0.21, quiet); dyn_techm_ns (rho 0.524 via nifty_50, z -0.8, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.568 vs aud_usd, historically leads by 3d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.529 vs nifty_50, historically leads by 3d
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.524 vs nifty_50, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.411 vs eur_usd, historically leads by 1d
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.587 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.641, z -1.0); midcap_largecap_ratio (rho 0.587, z -0.39); nifty_metal (rho 0.536, z -0.49); nifty_fmcg (rho 0.529, z -0.21)
- Source: Nifty outlook for tomorrow: Why 23,000 matters after breaking below 4-month support? Resistance, support levels | Friday — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/nifty-outlook-for-tomorrow-why-23-000-matters-after-breaking-below-4-month-support-resistance-support-levels-friday-11790272671999.html
- Source: US yield shock, oil surge hammer equities; Nifty hits lowest since April 7 — BusinessLine Mkts, 2026-09-24. https://www.thehindubusinessline.com/markets/us-yield-shock-oil-surge-hammer-equities-nifty-hits-lowest-since-april-7/article71504358.ece
- Source: HDFC MF bets on PB Fintech, buys stake worth Rs 321 crore as IRDAI reforms trigger 36% stock rout — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-mf-bets-on-pb-fintech-buys-stake-worth-rs-321-crore-as-irdai-reforms-trigger-36-stock-rout/articleshow/134466281.cms
- Historical analogues: 2024-11-06 (d=1.05), 2025-07-21 (d=1.15), 2025-01-31 (d=1.16)

### [RED 12.04] natgas ↑
- natgas [COMMODITIES]: last 3.28, z20 7.04, zc 2.65, resid-z 3.86 [unexplained], 1d 8.37%, 1-session move +8.37% ≥ 5.0%; |z20|=7.04
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.426 via natgas, z -15.51, reacted)
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.054 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.017 vs natgas, historically leads by 4d
- **India receivers**: dyn_policybzr_ns (rho -0.426, z -15.51)
- Source: U.S. to Back Argentina’s First LNG Export Project With $6 Billion Loan — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/US-to-Back-Argentinas-First-LNG-Export-Project-With-6-Billion-Loan.html
- Source: Southeast Asia Keeps Building Gas Plants Despite Hormuz LNG Shock — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Southeast-Asia-Keeps-Building-Gas-Plants-Despite-Hormuz-LNG-Shock.html
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 9.87] cross-asset · 9 series ↑
- dyn_bond [EQUITIES]: last 87.56, z20 -2.39, zc -1.64, resid-z -0.15 [priced], 1d -0.65%, |z20|=2.39; 1y-pct=0
- dyn_ms [EQUITIES]: last 196.23, z20 -2.31, zc -0.59, resid-z 0.12 [quiet], 1d -1.09%, |z20|=2.31
- tips_10y_real [RATES]: last 2.76, z20 2.24, zc 2.66, resid-z 2.36 [unexplained], 1d 4.94%, 1d move +13.0bps ≥ 5bps; |z20|=2.24; 1y-pct=100
- ust_10y [RATES]: last 5.11, z20 2.13, zc 3.12, resid-z 2.64 [unexplained], 1d 3.02%, |z20|=2.13; 1y-pct=100
- ust_30y [RATES]: last 5.40, z20 2.07, zc 2.73, resid-z 2.34 [unexplained], 1d 2.08%, |z20|=2.07; 1y-pct=100
- ust_2y [RATES]: last 4.85, z20 1.87, zc 2.28, resid-z 1.49 [moved], 1d 2.97%, |z20|=1.87; 1y-pct=100
- dow_jones [INDICES]: last 51349.18, z20 -1.68, zc -0.40, resid-z -0.08 [quiet], 1d -0.32%, |z20|=1.68
- russell_2000 [INDICES]: last 2835.78, z20 -1.66, zc -0.08, resid-z 0.24 [quiet], 1d -0.10%, |z20|=1.66
- brent [COMMODITIES]: last 106.07, z20 1.12, zc 1.06, resid-z 0.79 [quiet], 1d 2.90%, 1-session move +2.90% ≥ 1.5%
- **Mechanism**: cross-asset · 9 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.613 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.586 vs dyn_ms, historically leads by 4d
- Watch next: wti (inverse) — not yet - watch; rho -0.514 vs dyn_bond, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.595 vs dyn_bond
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.593 vs dow_jones
- Source: Soaring Freight Costs Make Japan’s Crude Imports the World’s Most Expensive — OilPrice, 2026-09-24. https://oilprice.com/Energy/Crude-Oil/Soaring-Freight-Costs-Make-Japans-Crude-Imports-the-Worlds-Most-Expensive.html
- Source: Why investors aren’t buying yet another attempt by the Treasury to calm the rattled bond market — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/why-investors-arent-buying-yet-another-attempt-by-the-treasury-to-calm-the-rattled-bond-market-b168cac3?mod=mw_rss_topstories
- Source: Oil jump sends 30-year yields to two-decade high — Mint Markets, 2026-09-24. https://www.livemint.com/market/oil-jump-sends-30-year-yields-to-two-decade-high-11790284055527.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.65), 2025-05-12 (d=0.74)

### [RED 5.62] dxy ↑
- dxy [FX]: last 101.27, z20 2.62, zc 0.49, resid-z 0.94 [quiet], 1d 0.17%, 20d range extreme; |z20|=2.62; 1y-pct=96
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.13] wti ↓
- wti [COMMODITIES]: last 93.96, z20 -0.13, zc 0.69, resid-z 0.57 [quiet], 1d 1.95%, 1-session move +1.95% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.584 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.529 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.507 vs wti
- Source: Soaring Freight Costs Make Japan’s Crude Imports the World’s Most Expensive — OilPrice, 2026-09-24. https://oilprice.com/Energy/Crude-Oil/Soaring-Freight-Costs-Make-Japans-Crude-Imports-the-Worlds-Most-Expensive.html
- Source: Oil jump sends 30-year yields to two-decade high — Mint Markets, 2026-09-24. https://www.livemint.com/market/oil-jump-sends-30-year-yields-to-two-decade-high-11790284055527.html
- Source: SOME 60 COMMERCIAL VESSELS TRANSITED THE STRAIT OF HORMUZ ON WEDNESDAY CARRYING THE HIGHEST DAILY VOLUME OF CRUDE SINCE EARLY JULY, US DEFENSE OFFICIAL TELLS REUTERS — DeItaone, 2026-09-24. https://t.me/walter_bloomberg/36162
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 4.5] crypto · 2 series ↑
- btc_usd [CRYPTO]: last 84376.90, z20 1.67, zc -0.00, resid-z -0.01 [quiet], 1d -0.01%, |z20|=1.67
- eth_usd [CRYPTO]: last 2687.33, z20 1.65, zc 0.02, resid-z 0.19 [quiet], 1d 0.10%, |z20|=1.65
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-06-09 (z-distance 0.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.357 via btc_usd, z -0.03, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.544 vs btc_usd, historically leads by 1d
- **India receivers**: dyn_cartrade_ns (rho 0.357, z -0.03)
- Source: What Bitcoin’s $16 billion options expiry means for investors — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/cryptocurrency/what-bitcoins-16-billion-options-expiry-means-for-investors/articleshow/134453599.cms
- Source: Cryptocurrency future: Bitcoin prices trading above $80k - What's behind the rally? What lies ahead? — Mint Markets, 2026-09-24. https://www.livemint.com/market/cryptocurrency/cryptocurrency-future-bitcoin-prices-trading-above-80k-whats-behind-the-rally-what-lies-ahead-11790218140136.html
- Source: Bitcoin holds near $86,000 as spot Bitcoin ETF inflows hit 11-month high of $999 million — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-86000-as-spot-bitcoin-etf-inflows-hit-11-month-high-of-999-million/articleshow/134432852.cms
- Historical analogues: 2025-06-09 (d=0.08), 2024-11-18 (d=0.11), 2026-07-22 (d=0.14)

### [RED 4.5] brent_wti_spread ↑
- brent_wti_spread [DERIVED]: last 12.11, z20 4.50, zc n/a, resid-z n/a [quiet], 1d 10.90%, |z20|=4.50; 1y-pct=97
- **Mechanism**: brent_wti_spread ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.402 via brent_wti_spread, z -0.21, quiet); nifty_metal (rho 0.369 via brent_wti_spread, z -0.49, quiet)
- **India receivers**: nifty_fmcg (rho 0.402, z -0.21); nifty_metal (rho 0.369, z -0.49)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-04 (d=0.0), 2026-05-06 (d=0.01)

### [AMBER 4.45] dyn_meta ↑
- dyn_meta [EQUITIES]: last 777.44, z20 2.45, zc 1.63, resid-z 0.39 [moved], 1d 4.48%, |z20|=2.45; 1y-pct=100
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.451 via dyn_meta, z -1.05, reacted)
- **India receivers**: dyn_havells_ns (rho -0.451, z -1.05)
- Source: Meta wants to put its Muse AI assistant on your face — but will consumers buy in? — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/meta-gets-price-target-boost-as-jpmorgan-says-muse-agent-has-potential-to-become-the-top-ai-application-since-chatgpt-280ca648?mod=mw_rss_topstories
- Source: Meta gets price-target boost as JPMorgan says Muse agent has potential to become the top AI application since ChatGPT — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/meta-gets-price-target-boost-as-jpmorgan-says-muse-agent-has-potential-to-become-the-top-ai-application-since-chatgpt-280ca648?mod=mw_rss_topstories
- Source: Can Meta’s VR ambitions create a new catalyst for Unity stocks? — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/news/can-metas-vr-ambitions-create-a-new-catalyst-for-unity-stocks/slideshow/134453567.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (4.06), dyn_stylebaaza_ns ↓ (4.03), nasdaq_100 ↑ (3.97), dyn_tech ↑ (3.84), comex_gold ↓ (3.72), comex_copper ↑ (3.57), dyn_voltas_ns ↓ (3.46), gold_silver_ratio ↓ (3.38), dyn_jiofin_bo ↓ (3.0), dyn_indusindbk_bo ↓ (2.98), sofr ↑ (2.14), dyn_hdb ↓ (2.03)

## India macro
- nifty_50: 23063.0996 (1d -1.64%, z20 -1.73, flag amber)
- nifty_midcap_100: 60992.2500 (1d -2.24%, z20 -1.74, flag amber)
- usd_inr: 95.7412 (1d 0.05%, z20 0.80, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6446 (1d -0.62%, z20 -0.39, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 79.4 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.1 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.5 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- INDIANB.NS (INDIAN BANK) score 59.5 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- OHI (Omega Healthcare Investors, In) score 52.9 — "Costco’s results beat expectations. Here’s why investors are still cautious."
- COIN (Coinbase Global, Inc.) score 51.9 — "FED MAY BE LOSING CONTROL OF LONG-TERM YIELDS CIFC says long-term Treasury yields are incr"
- HDB (HDFC Bank Limited) score 48.6 — "HDFC MF bets on PB Fintech, buys stake worth Rs 321 crore as IRDAI reforms trigger 36% sto"
- BAC (Bank of America Corporation) score 46.2 — "IRANIAN PRESIDENT WHEN ASKED IF WAR COULD END BEFORE END OF YEAR: IT'S AMERICA THAT MUST C"
- CHKP (Check Point Software Technolog) score 41.1 — "Top stocks to buy today: GAIL, Texmaco, HBL Engineering by Vaishali Parekh, check stop-los"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.4 — "The S&P 500’s newest tech stock is now its best performer"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "The S&P 500’s newest tech stock is now its best performer"
- TECH (Bio-Techne Corp) score 39.4 — "The S&P 500’s newest tech stock is now its best performer"
- 301077.SZ (CHINASTARS) score 39.1 — "XI TOLD TRUMP CHINA'S POSITION ON SAFEGUARDING ITS NATIONAL UNITY AND TERRITORIAL INTEGRIT"
- IDBI.NS (IDBI BANK LIMITED) score 38.8 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.8 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.8 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.1 — "FED MAY BE LOSING CONTROL OF LONG-TERM YIELDS CIFC says long-term Treasury yields are incr"
- SEPN (Septerna, Inc.) score 29.0 — "Stock market prediction for today: Sensex, Nifty outlook for Friday | Kospi, Taiwan cues t"
- LTH (Life Time Group Holdings, Inc.) score 28.8 — "I spend my time and money caring for my aging mother — yet she gave my brother $100,000. S"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.9 — "BP EYES $2–5 BILLION U.S. SHALE DEAL BP is evaluating acquisitions to expand its U.S. shal"
- JIOFIN.BO (Jio Financial Services Limited) score 20.8 — "Financial stocks lead correction as insurance overhaul plan sparks fears"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.2 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.2 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.5 — "FED MAY BE LOSING CONTROL OF LONG-TERM YIELDS CIFC says long-term Treasury yields are incr"
- META (Meta) score 12.0 — "Meta wants to put its Muse AI assistant on your face — but will consumers buy in?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.2 — "Just One Commodity Vessel Left the Strait of Hormuz on Wednesday"
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.8 — "HDFC MF bets on PB Fintech, buys stake worth Rs 321 crore as IRDAI reforms trigger 36% sto"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.1 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.0 — "Can IRDAI’s insurance reforms impact NBFCs? Jefferies warns L&T Finance, Piramal Finance, "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.3 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"
- VT (Vanguard Total World Stock Ind) score 7.9 — "Can the World Hit 35% Electrification by 2035?"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.9 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.8 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- MS (Morgan Stanley) score 7.4 — "Here’s how to position your portfolio for the next AI wave, according to Morgan Stanley"
- PINELABS.NS (PINE LABS LIMITED) score 4.7 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "Goldman Sachs buys stake in small-cap stock that has surged 50% in less than two months"
- NVDA (NVIDIA Corporation) score 3.8 — "FORMER OPENAI DATA CENTER CHIEF CHRIS MALONE IS NOW AT NVIDIA - THE INFORMATION"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.1 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- VOLTAS.NS (VOLTAS LTD) score 1.7 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 1.0 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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