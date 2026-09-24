# Transmission Layer — board brief · 2026-09-24 19:59Z

data as of **2026-09-24** · 97 series · 9 red / 40 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.586, 5d in regime; vol-pct 0.485, breadth-off 0.688, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.35, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.08, corr60 0.22, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.13, corr60 0.14, last shift 2026-08-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.08, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.04, last shift 2026-08-04. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.17, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **8 of 89** scanned series survive multiplicity control (effective p ≤ 0.0043719229098264645)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1096) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2450) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 20.01] cross-asset · 8 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1207.20, z20 -15.51, zc -12.58, resid-z -17.64 [unexplained], 1d -36.00%, |z20|=15.51; 1y-pct=0
- usd_mxn [FX]: last 17.72, z20 5.39, zc 5.87, resid-z 6.51 [unexplained], 1d 2.51%, |z20|=5.39
- aud_usd [FX]: last 0.70, z20 -3.65, zc -3.14, resid-z -3.53 [unexplained], 1d -1.34%, |z20|=3.65
- gbp_usd [FX]: last 1.32, z20 -3.52, zc -2.60, resid-z -2.85 [unexplained], 1d -0.93%, |z20|=3.52
- eur_usd [FX]: last 1.14, z20 -2.86, zc -1.96, resid-z -2.25 [unexplained], 1d -0.59%, |z20|=2.86; 1y-pct=2
- nifty_midcap_100 [INDICES]: last 60992.25, z20 -1.74, zc -3.09, resid-z -2.30 [unexplained], 1d -2.24%, |z20|=1.74
- nifty_50 [INDICES]: last 23063.10, z20 -1.73, zc -3.22, resid-z -2.23 [unexplained], 1d -1.64%, |z20|=1.73; 1y-pct=3
- india_vix [INDICES]: last 12.62, z20 1.44, zc 3.88, resid-z n/a [moved], 1d 21.98%, 1-session move +21.98% ≥ 15.0%
- **Mechanism**: cross-asset · 8 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-06 (z-distance 1.05).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.641 via nifty_50, z -1.0, reacted); midcap_largecap_ratio (rho 0.587 via nifty_midcap_100, z -0.39, quiet); nifty_metal (rho 0.536 via nifty_midcap_100, z -0.49, quiet); nifty_fmcg (rho 0.529 via nifty_50, z -0.21, quiet); dyn_techm_ns (rho 0.524 via nifty_50, z -0.8, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.575 vs aud_usd, historically leads by 3d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.529 vs nifty_50, historically leads by 3d
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.524 vs nifty_50, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.415 vs eur_usd, historically leads by 1d
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.587 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.641, z -1.0); midcap_largecap_ratio (rho 0.587, z -0.39); nifty_metal (rho 0.536, z -0.49); nifty_fmcg (rho 0.529, z -0.21)
- Source: Nifty outlook for tomorrow: Why 23,000 matters after breaking below 4-month support? Resistance, support levels | Friday — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/nifty-outlook-for-tomorrow-why-23-000-matters-after-breaking-below-4-month-support-resistance-support-levels-friday-11790272671999.html
- Source: US yield shock, oil surge hammer equities; Nifty hits lowest since April 7 — BusinessLine Mkts, 2026-09-24. https://www.thehindubusinessline.com/markets/us-yield-shock-oil-surge-hammer-equities-nifty-hits-lowest-since-april-7/article71504358.ece
- Source: HDFC MF bets on PB Fintech, buys stake worth Rs 321 crore as IRDAI reforms trigger 36% stock rout — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-mf-bets-on-pb-fintech-buys-stake-worth-rs-321-crore-as-irdai-reforms-trigger-36-stock-rout/articleshow/134466281.cms
- Historical analogues: 2024-11-06 (d=1.05), 2025-07-21 (d=1.15), 2025-01-31 (d=1.16)

### [RED 14.1] natgas ↑
- natgas [COMMODITIES]: last 3.38, z20 9.10, zc 3.77, resid-z 5.31 [unexplained], 1d 11.91%, 1-session move +11.91% ≥ 5.0%; |z20|=9.10
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.557 via natgas, z -15.51, reacted)
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.051 vs natgas, historically leads by 4d
- **India receivers**: dyn_policybzr_ns (rho -0.557, z -15.51)
- Source: U.S. to Back Argentina’s First LNG Export Project With $6 Billion Loan — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/US-to-Back-Argentinas-First-LNG-Export-Project-With-6-Billion-Loan.html
- Source: Southeast Asia Keeps Building Gas Plants Despite Hormuz LNG Shock — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Southeast-Asia-Keeps-Building-Gas-Plants-Despite-Hormuz-LNG-Shock.html
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 9.1] cross-asset · 10 series ↑
- dyn_bond [EQUITIES]: last 87.61, z20 -2.34, zc -1.50, resid-z 0.59 [priced], 1d -0.59%, |z20|=2.34; 1y-pct=0
- dyn_ms [EQUITIES]: last 196.14, z20 -2.32, zc -0.62, resid-z -1.67 [unexplained], 1d -1.13%, |z20|=2.32
- dow_jones [INDICES]: last 51341.75, z20 -1.69, zc -0.42, resid-z 0.12 [quiet], 1d -0.33%, |z20|=1.69
- russell_2000 [INDICES]: last 2835.71, z20 -1.66, zc -0.08, resid-z 0.26 [quiet], 1d -0.10%, |z20|=1.66
- brent [COMMODITIES]: last 107.36, z20 1.34, zc 1.52, resid-z 1.26 [moved], 1d 4.15%, 1-session move +4.15% ≥ 1.5%
- ust_2y [RATES]: last 4.71, z20 1.27, zc -0.80, resid-z -1.41 [quiet], 1d -1.05%, 1y-pct=98
- tips_10y_real [RATES]: last 2.63, z20 1.22, zc 0.20, resid-z -0.25 [quiet], 1d 0.38%, 1y-pct=99
- ust_10y [RATES]: last 4.96, z20 1.00, zc 0.00, resid-z -0.34 [quiet], 1d 0.00%, 1y-pct=97
- ust_30y [RATES]: last 5.29, z20 0.26, zc 0.00, resid-z -0.16 [quiet], 1d 0.00%, 1y-pct=96
- wti [COMMODITIES]: last 95.23, z20 0.07, zc 1.17, resid-z 1.07 [quiet], 1d 3.33%, 1-session move +3.33% ≥ 1.5%
- **Mechanism**: cross-asset · 10 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.613 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.585 vs dyn_ms, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.597 vs dyn_bond
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.594 vs dow_jones
- Watch next: sp500 (co-move) — not yet - watch; rho 0.544 vs dyn_bond
- Source: Surging Treasury yields pose a brand new problem for Kevin Warsh and the Fed — CNBC Economy, 2026-09-24. https://www.cnbc.com/2026/09/24/surging-treasury-yields-are-posing-a-brand-new-problem-for-kevin-warsh-and-the-fed.html
- Source: Saudi Oil Export Costs Surge as Red Sea Risks Mount — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Oil-Export-Costs-Surge-as-Red-Sea-Risks-Mount.html
- Source: Here are 3 alternatives for investors looking to dodge the bond-market beatdown — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/here-are-3-alternatives-for-investors-looking-to-dodge-the-bond-market-beatdown-ec8fda43?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.79), 2025-05-15 (d=0.79)

### [RED 5.62] dxy ↑
- dxy [FX]: last 101.27, z20 2.62, zc 0.49, resid-z 0.54 [quiet], 1d 0.17%, 20d range extreme; |z20|=2.62; 1y-pct=96
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.53] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2692.35, z20 1.70, zc 0.07, resid-z 0.20 [quiet], 1d 0.29%, |z20|=1.70
- btc_usd [CRYPTO]: last 84303.32, z20 1.65, zc -0.03, resid-z -0.04 [quiet], 1d -0.09%, |z20|=1.65
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-06-09 (z-distance 0.12).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.356 via btc_usd, z -0.03, quiet)
- **India receivers**: dyn_cartrade_ns (rho 0.356, z -0.03)
- Source: What Bitcoin’s $16 billion options expiry means for investors — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/cryptocurrency/what-bitcoins-16-billion-options-expiry-means-for-investors/articleshow/134453599.cms
- Source: Cryptocurrency future: Bitcoin prices trading above $80k - What's behind the rally? What lies ahead? — Mint Markets, 2026-09-24. https://www.livemint.com/market/cryptocurrency/cryptocurrency-future-bitcoin-prices-trading-above-80k-whats-behind-the-rally-what-lies-ahead-11790218140136.html
- Source: Bitcoin holds near $86,000 as spot Bitcoin ETF inflows hit 11-month high of $999 million — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-86000-as-spot-bitcoin-etf-inflows-hit-11-month-high-of-999-million/articleshow/134432852.cms
- Historical analogues: 2025-06-09 (d=0.12), 2026-04-14 (d=0.12), 2024-11-18 (d=0.15)

### [RED 4.52] brent_wti_spread ↑
- brent_wti_spread [DERIVED]: last 12.13, z20 4.52, zc n/a, resid-z n/a [quiet], 1d 11.08%, |z20|=4.52; 1y-pct=97
- **Mechanism**: brent_wti_spread ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.402 via brent_wti_spread, z -0.21, quiet); nifty_metal (rho 0.368 via brent_wti_spread, z -0.49, quiet)
- **India receivers**: nifty_fmcg (rho 0.402, z -0.21); nifty_metal (rho 0.368, z -0.49)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-04 (d=0.0), 2026-05-06 (d=0.01)

### [AMBER 4.46] dyn_meta ↑
- dyn_meta [EQUITIES]: last 777.75, z20 2.46, zc 1.65, resid-z -0.26 [moved], 1d 4.52%, |z20|=2.46; 1y-pct=100
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.451 via dyn_meta, z -1.05, reacted)
- **India receivers**: dyn_havells_ns (rho -0.451, z -1.05)
- Source: Meta wants to put its Muse AI assistant on your face — but will consumers buy in? — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/meta-gets-price-target-boost-as-jpmorgan-says-muse-agent-has-potential-to-become-the-top-ai-application-since-chatgpt-280ca648?mod=mw_rss_topstories
- Source: Meta gets price-target boost as JPMorgan says Muse agent has potential to become the top AI application since ChatGPT — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/meta-gets-price-target-boost-as-jpmorgan-says-muse-agent-has-potential-to-become-the-top-ai-application-since-chatgpt-280ca648?mod=mw_rss_topstories
- Source: Can Meta’s VR ambitions create a new catalyst for Unity stocks? — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/news/can-metas-vr-ambitions-create-a-new-catalyst-for-unity-stocks/slideshow/134453567.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [AMBER 4.06] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5640.00, z20 2.06, zc 0.65, resid-z 0.25 [quiet], 1d -1.40%, |z20|=2.06; 1y-pct=99
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.369 via dyn_4417_t, z -0.43, quiet)
- **India receivers**: dyn_justdial_bo (rho 0.369, z -0.43)
- Source: IPO reality check! Is GMP a useful signal or just market noise? Here’s what experts think — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/ipos/fpos/ipo-reality-check-is-gmp-a-useful-signal-or-just-market-noise-heres-what-experts-think/articleshow/134452734.cms
- Source: HDFC Bank share price down 25% in 2026 - Opportunity for bottom fishing ahead of new CEO appointment? Experts decode — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-down-25-in-2026-opportunity-for-bottom-fishing-ahead-of-new-ceo-appointment-experts-decode-11790221093029.html
- Source: World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn — CNBC Economy, 2026-09-24. https://www.cnbc.com/2026/09/24/hormuz-blacksea-ukraine-iran-food-security-united-nations-.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↓ (4.03), nasdaq_100 ↑ (3.99), dyn_tech ↑ (3.84), comex_gold ↓ (3.71), comex_copper ↑ (3.57), dyn_voltas_ns ↓ (3.46), gold_silver_ratio ↓ (3.36), dyn_jiofin_bo ↓ (3.0), dyn_indusindbk_bo ↓ (2.98), usd_brl ↑ (2.2), sofr ↑ (2.14), dyn_hdb ↓ (2.05)

## India macro
- nifty_50: 23063.0996 (1d -1.64%, z20 -1.73, flag amber)
- nifty_midcap_100: 60992.2500 (1d -2.24%, z20 -1.74, flag amber)
- usd_inr: 95.9450 (1d 0.27%, z20 1.17, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6446 (1d -0.62%, z20 -0.39, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 82.5 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.1 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.5 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- INDIANB.NS (INDIAN BANK) score 61.8 — "Iran Warns U.S. Strikes Could Push War Into Indian Ocean"
- COIN (Coinbase Global, Inc.) score 51.9 — "Global Market: European shares edge lower as Middle East tensions, US-China talks in focus"
- OHI (Omega Healthcare Investors, In) score 50.8 — "Dow Jones| Nasdaq | US Stock Market Today | Live:  US markets dip as investors focus on ph"
- HDB (HDFC Bank Limited) score 50.5 — "HDFC MF bets on PB Fintech, buys stake worth Rs 321 crore as IRDAI reforms trigger 36% sto"
- BAC (Bank of America Corporation) score 45.9 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- CHKP (Check Point Software Technolog) score 42.7 — "Top stocks to buy today: GAIL, Texmaco, HBL Engineering by Vaishali Parekh, check stop-los"
- IDBI.NS (IDBI BANK LIMITED) score 40.3 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.3 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.3 — "I’m afraid of ‘starving to death.’ Social Security stopped our checks due to a hacked bank"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.8 — "TRUMP SAYS HE AND XI WILL DISCUSS SECURITY, TECHNOLOGY AND ARTIFICIAL INTELLIGENCE"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.8 — "TRUMP SAYS HE AND XI WILL DISCUSS SECURITY, TECHNOLOGY AND ARTIFICIAL INTELLIGENCE"
- TECH (Bio-Techne Corp) score 39.8 — "TRUMP SAYS HE AND XI WILL DISCUSS SECURITY, TECHNOLOGY AND ARTIFICIAL INTELLIGENCE"
- 301077.SZ (CHINASTARS) score 36.5 — "TRUMP SAYS HE AND CHINA'S XI HAVE FORGED TRULY GREAT FRIENDSHIP"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.4 — "Here are 3 alternatives for investors looking to dodge the bond-market beatdown"
- SEPN (Septerna, Inc.) score 30.1 — "Stock market prediction for today: Sensex, Nifty outlook for Friday | Kospi, Taiwan cues t"
- LTH (Life Time Group Holdings, Inc.) score 29.9 — "I spend my time and money caring for my aging mother — yet she gave my brother $100,000. S"
- JIOFIN.BO (Jio Financial Services Limited) score 21.6 — "Financial stocks lead correction as insurance overhaul plan sparks fears"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.9 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.9 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.0 — "Dividend, stock split record date alert: Last chance to buy today - Noble Polymers, Naturi"
- META (Meta) score 12.5 — "Meta wants to put its Muse AI assistant on your face — but will consumers buy in?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.7 — "Just One Commodity Vessel Left the Strait of Hormuz on Wednesday"
- POLICYBZR.NS (PB FINTECH LIMITED) score 10.2 — "HDFC MF bets on PB Fintech, buys stake worth Rs 321 crore as IRDAI reforms trigger 36% sto"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.4 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.3 — "Can IRDAI’s insurance reforms impact NBFCs? Jefferies warns L&T Finance, Piramal Finance, "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.7 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.2 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- MS (Morgan Stanley) score 6.6 — "Morgan Stanley employee accidentally leaks bank’s Asia investment pipeline details"
- VT (Vanguard Total World Stock Ind) score 6.2 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- PINELABS.NS (PINE LABS LIMITED) score 4.9 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- GS (Goldman Sachs Group, Inc. (The) score 4.7 — "Goldman Sachs buys stake in small-cap stock that has surged 50% in less than two months"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.3 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 2.9 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- VOLTAS.NS (VOLTAS LTD) score 1.8 — "Voltas’s market share is growing. Will margins follow?"
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