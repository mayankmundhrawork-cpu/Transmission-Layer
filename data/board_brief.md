# Transmission Layer — board brief · 2026-08-25 07:07Z

data as of **2026-08-25** · 98 series · 8 red / 35 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.363, 1d in regime; vol-pct 0.226, breadth-off 0.5, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.17, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.11, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.15, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.21, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.33, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0008684598407633359)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2394) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.84] commodities · 2 series ↑
- corn [COMMODITIES]: last 519.75, z20 4.00, zc 4.51, resid-z 1.08 [moved], 1d 5.75%, |z20|=4.00; 1y-pct=100
- wheat [COMMODITIES]: last 703.75, z20 2.67, zc 2.03, resid-z 0.12 [moved], 1d 3.23%, |z20|=2.67; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 6.71] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 80715.33, z20 3.05, zc 0.54, resid-z 0.81 [quiet], 1d 2.16%, |z20|=3.05
- dyn_mrna [EQUITIES]: last 138.89, z20 2.77, zc -0.33, resid-z 0.89 [quiet], 1d -4.30%, |z20|=2.77; 1y-pct=99
- eth_usd [CRYPTO]: last 2509.00, z20 2.48, zc 0.21, resid-z 0.18 [quiet], 1d 0.91%, |z20|=2.48
- dyn_coin [EQUITIES]: last 179.49, z20 2.22, zc -0.69, resid-z 2.03 [unexplained], 1d -3.76%, |z20|=2.22
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.75).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.414 via btc_usd, z 1.31, reacted)
- **India receivers**: nifty_metal (rho 0.414, z 1.31)
- Source: Global Market: Japanese bond yields edge higher as US Treasury yields, oil prices rise — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-edge-higher-as-us-treasury-yields-oil-prices-rise/articleshow/133496737.cms
- Source: Global market: Mainland China stocks slip as metal shares drop, investors await Jackson Hole cues — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-mainland-china-stocks-slip-as-metal-shares-drop-investors-await-jackson-hole-cues/articleshow/133495355.cms
- Source: Global Market: Porsche stock falls as MHP sale, weak revenue keep investors on edge — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-porsche-stock-falls-as-mhp-sale-weak-revenue-keep-investors-on-edge/articleshow/133495008.cms
- Historical analogues: 2025-08-13 (d=0.75), 2024-11-21 (d=1.37), 2026-05-05 (d=1.38)

### [AMBER 5.32] cross-asset · 2 series ↓
- dyn_techm_ns [EQUITIES]: last 1564.50, z20 -2.49, zc -0.81, resid-z -0.01 [quiet], 1d -1.23%, |z20|=2.49
- nifty_it [INDICES]: last 30345.70, z20 -1.53, zc -0.56, resid-z 0.13 [quiet], 1d -0.82%, |z20|=1.53
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.609 via nifty_it, z -1.65, reacted); dyn_tatatech_ns (rho 0.502 via nifty_it, z -0.22, quiet); nifty_50 (rho 0.469 via nifty_it, z -1.06, reacted)
- Watch next: shanghai_comp (inverse) — not yet - watch; rho -0.505 vs dyn_techm_ns, historically leads by 5d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.502 vs nifty_it, historically leads by 3d
- **India receivers**: dyn_tataelxsi_ns (rho 0.609, z -1.65); dyn_tatatech_ns (rho 0.502, z -0.22); nifty_50 (rho 0.469, z -1.06)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Performance Overview — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-livestock-price-today-live-updates-24-aug-2026/liveblog/133450069.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.01] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3222.90, z20 3.01, zc 0.13, resid-z 3.53 [unexplained], 1d 0.43%, |z20|=3.01
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.643 via dyn_muthootfin_ns, z 1.31, reacted); nifty_midcap_100 (rho 0.568 via dyn_muthootfin_ns, z 0.44, quiet); nifty_50 (rho 0.496 via dyn_muthootfin_ns, z -1.06, reacted); dyn_karurvysya_ns (rho 0.476 via dyn_muthootfin_ns, z 2.43, reacted); dyn_idbi_ns (rho 0.398 via dyn_muthootfin_ns, z 2.66, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.568 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.509 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.643, z 1.31); nifty_midcap_100 (rho 0.568, z 0.44); nifty_50 (rho 0.496, z -1.06); dyn_karurvysya_ns (rho 0.476, z 2.43)
- Source: Muthoot Finance among 6 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-among-6-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/133489659.cms
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [AMBER 4.63] rates · 2 series ↑
- ust_10y [RATES]: last 4.74, z20 1.79, zc 1.07, resid-z 1.37 [quiet], 1d 1.07%, |z20|=1.79; 1y-pct=99
- ust_30y [RATES]: last 5.27, z20 1.13, zc 0.90, resid-z 1.12 [quiet], 1d 0.76%, 1y-pct=98
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.768 vs ust_10y, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.952 vs ust_10y
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.853 vs ust_10y
- Watch next: wti (co-move) — not yet - watch; rho 0.559 vs ust_10y, historically leads by 3d
- Watch next: brent (co-move) — not yet - watch; rho 0.591 vs ust_10y
- Source: Global Market: Japanese bond yields edge higher as US Treasury yields, oil prices rise — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-edge-higher-as-us-treasury-yields-oil-prices-rise/articleshow/133496737.cms
- Source: GERMAN FIN. MIN. KLINGBEIL: SURGE IN BOND YIELDS A RESULT OF TRUMP'S WAR — DeItaone, 2026-08-24. https://t.me/walter_bloomberg/34951
- Source: US stock market today: Wall Street futures slip as tech rout, Iran tensions and bond yields weigh — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-slip-as-tech-rout-iran-tensions-and-bond-yields-weigh-11787385929496.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.11), 2025-05-16 (d=0.19)

### [AMBER 4.35] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.35, zc n/a, resid-z n/a [quiet], 1d 0.02%, 52-wk extreme (pct=100); 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.483 via midcap_largecap_ratio, z 0.44, quiet); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 0.8, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.483, z 0.44); dyn_fincables_ns (rho 0.355, z 0.8)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.12] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 668.20, z20 2.12, zc 1.25, resid-z -0.67 [quiet], 1d 2.02%, |z20|=2.12; 1y-pct=100
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.366 via dyn_lenskart_ns, z 0.69, quiet)
- **India receivers**: dyn_adanient_bo (rho 0.366, z 0.69)
- Source: From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s vision — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/from-ipo-mockery-to-rs-1-lakh-crore-m-cap-why-investors-are-still-betting-on-lenskarts-vision/articleshow/133494107.cms
- Source: SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/softbank-pares-nearly-2-6-stake-in-lenskart-for-rs-2888-crore/articleshow/133472713.cms
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 20% in a month — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-20-in-a-month/slideshow/133468092.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [AMBER 4.06] comex_gold ↑
- comex_gold [COMMODITIES]: last 4696.30, z20 2.06, zc 0.75, resid-z 1.19 [quiet], 1d 1.20%, |z20|=2.06
- **Mechanism**: comex_gold ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.445 via comex_gold, z 1.31, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.635 vs comex_gold, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.535 vs comex_gold, historically leads by 4d
- **India receivers**: nifty_metal (rho 0.445, z 1.31)
- Source: Gold futures decline to ₹1,63,109/10gm — BusinessLine Mkts, 2026-08-25. https://www.thehindubusinessline.com/markets/gold/gold-futures-decline-to-16310910gm/article71387451.ece
- Source: Gold Rate Today, Aug 25: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-25. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-25-2026/article71387306.ece
- Source: Gold prices fall after 4 days; silver dips Rs 4,300/kg ahead of inflation data, Warsh speech at Jackson Hole — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-fall-after-4-days-silver-dips-rs-4300/kg-ahead-of-inflation-data-warsh-speech-at-jackson-hole/articleshow/133491244.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-15 (d=0.0), 2024-11-18 (d=0.1)

## Watchlist (below surfacing floor)
dyn_lth ↑ (3.43), dyn_tech ↑ (3.4), gold_silver_ratio ↑ (3.39), dyn_icicigi_bo ↓ (3.39), dyn_pcjeweller_ns ↑ (3.33), cross-asset · 2 series ↑ (3.15), dyn_cartrade_ns ↑ (3.07), comex_copper ↑ (2.68), dyn_idbi_ns ↑ (2.66), fx · 2 series ↑ (2.61), ftse_100 ↑ (2.44), dyn_karurvysya_ns ↑ (2.43)

## India macro
- nifty_50: 24167.7500 (1d -0.21%, z20 -1.06, flag none)
- nifty_midcap_100: 63695.5508 (1d -0.19%, z20 0.44, flag amber)
- usd_inr: 95.7000 (1d -0.00%, z20 0.98, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6356 (1d 0.02%, z20 1.35, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.4 — "Palm Conversations International India calls for broader understanding of palm oil"
- COALINDIA.NS (COAL INDIA LTD) score 81.0 — "Palm Conversations International India calls for broader understanding of palm oil"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.2 — "Palm Conversations International India calls for broader understanding of palm oil"
- INDIANB.NS (INDIAN BANK) score 75.8 — "HDFC Bank shares today: What is driving the stock lower"
- BAC (Bank of America Corporation) score 64.7 — "HDFC Bank shares today: What is driving the stock lower"
- BOND (PIMCO Active Bond Exchange-Tra) score 61.8 — "Global Market: Japanese bond yields edge higher as US Treasury yields, oil prices rise"
- HDB (HDFC Bank Limited) score 60.2 — "HDFC Bank shares today: What is driving the stock lower"
- IDBI.NS (IDBI BANK LIMITED) score 56.5 — "HDFC Bank shares today: What is driving the stock lower"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.5 — "HDFC Bank shares today: What is driving the stock lower"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.5 — "HDFC Bank shares today: What is driving the stock lower"
- TECHM.NS (TECH MAHINDRA LIMITED) score 50.0 — "Netweb Technologies shares fall 4% after raising Rs 1,200 crore through QIP"
- COIN (Coinbase Global, Inc.) score 48.9 — "Global Market: SK Hynix workers reject pay deal amid bonus dispute"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.7 — "Netweb Technologies shares fall 4% after raising Rs 1,200 crore through QIP"
- TECH (Bio-Techne Corp) score 48.6 — "Netweb Technologies shares fall 4% after raising Rs 1,200 crore through QIP"
- OHI (Omega Healthcare Investors, In) score 35.3 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- CHKP (Check Point Software Technolog) score 34.3 — "Annu Projects IPO opens: Check GMP, price band, and key dates. Should you subscribe?"
- LTH (Life Time Group Holdings, Inc.) score 30.6 — "Bitcoin tops $80,000 for the first time since mid-May"
- 301077.SZ (CHINASTARS) score 23.1 — "Global market: Mainland China stocks slip as metal shares drop, investors await Jackson Ho"
- JIOFIN.BO (Jio Financial Services Limited) score 21.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- PCJEWELLER.NS (PC JEWELLER LTD) score 19.1 — "Shankesh Jewellers, Sunshine Pictures make modest debut, trade below listing prices"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.3 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 15.0 — "ONTARIO PREMIER FORD: NEED TO RESTRICT ENERGY, POTASH, ELECTRICITY SHIPMENTS TO U.S."
- MS (Morgan Stanley) score 12.6 — "TCS-Porsche deal: Why Morgan Stanley, Citi, other brokerages still see up to 20% downside "
- NVDA (NVIDIA Corporation) score 12.2 — "Global Market: Kospi drops 2% as chip stocks tumble ahead of Nvidia earnings"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.0 — "Piramal Finance  ₹2,100 crore QIP: Check key dates, indicative issue price, purpose behind"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.5 — "Shein IPO: Fast fashion retailer eyes $27 billion price tag in long-awaited Hong Kong list"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.3 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.0 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- VT (Vanguard Total World Stock Ind) score 8.6 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- META (Meta) score 7.9 — "Global market: Mainland China stocks slip as metal shares drop, investors await Jackson Ho"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.6 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.3 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.2 — "Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance Snapshot"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.5 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.0 — "20 MILLION TO SHIP OIL THROUGH HORMUZ Shipping a supertanker through the Strait of Hormuz "
- JEF (Jefferies Financial Group Inc.) score 4.8 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- MRNA (Moderna, Inc.) score 4.0 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 0.9 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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