# Transmission Layer — board brief · 2026-08-25 10:48Z

data as of **2026-08-25** · 98 series · 8 red / 36 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.223, 2d in regime; vol-pct 0.196, breadth-off 0.25, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.16, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.27, corr60 -0.08, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.18, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.21, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.3, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2394) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.45] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 79465.12, z20 2.79, zc 0.16, resid-z 0.79 [quiet], 1d 0.63%, |z20|=2.79
- dyn_mrna [EQUITIES]: last 138.89, z20 2.77, zc -0.33, resid-z 0.89 [quiet], 1d -4.30%, |z20|=2.77; 1y-pct=99
- eth_usd [CRYPTO]: last 2483.89, z20 2.37, zc 0.02, resid-z 0.12 [quiet], 1d 0.08%, |z20|=2.37
- dyn_coin [EQUITIES]: last 179.49, z20 2.22, zc -0.69, resid-z 2.03 [unexplained], 1d -3.76%, |z20|=2.22
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.424 via btc_usd, z 1.59, reacted)
- **India receivers**: nifty_metal (rho 0.424, z 1.59)
- Source: Global Market: Japanese businesses turn to currency hedging as weak Yen drives up import costs — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japanese-businesses-turn-to-currency-hedging-as-weak-yen-drives-up-import-costs/articleshow/133505126.cms
- Source: Global Market: European markets gain as investors assess impact of Iran sanctions — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-markets-gain-as-investors-assess-impact-of-iran-sanctions/articleshow/133501875.cms
- Source: Bitcoin has beaten stocks and gold over six months. Now it’s crossed the $80,000 mark. — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/bitcoin-has-beaten-stocks-and-gold-over-six-months-now-its-closing-in-on-80-000-b8aa48f9?mod=mw_rss_topstories
- Historical analogues: 2025-08-13 (d=0.82), 2024-11-21 (d=1.31), 2026-05-05 (d=1.32)

### [AMBER 5.86] commodities · 2 series ↑
- brent [COMMODITIES]: last 87.99, z20 0.03, zc -2.12, resid-z -0.76 [moved], 1d -4.54%, 1-session move -4.54% ≥ 1.5%
- wti [COMMODITIES]: last 82.36, z20 0.01, zc -1.36, resid-z -0.66 [quiet], 1d -3.12%, 1-session move -3.12% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.573 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.679 vs brent
- Source: Oil prices decline as investors brush aside Bessent’s ‘economic D-Day’ for Iran — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/oil-prices-decline-as-investors-brush-aside-bessents-economic-d-day-for-iran-f318b614?mod=mw_rss_topstories
- Source: Oil fall lifts rupee to over one-week high after central bank keeps lid on losses — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/forex/oil-fall-lifts-rupee-to-over-one-week-high-after-central-bank-keeps-lid-on-losses/articleshow/133505392.cms
- Source: India’s Crude Import Bill Surges as Hormuz Shipping Rates Soar — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/Indias-Crude-Import-Bill-Surges-as-Hormuz-Shipping-Rates-Soar.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.67] corn ↑
- corn [COMMODITIES]: last 514.25, z20 3.67, zc 3.63, resid-z 1.08 [moved], 1d 4.63%, |z20|=3.67; 1y-pct=100
- **Mechanism**: corn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.01), 2025-12-31 (d=0.02)

### [RED 5.6] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3106.50, z20 3.60, zc 2.78, resid-z 1.86 [unexplained], 1d 4.24%, |z20|=3.60
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.489 via dyn_adanient_bo, z -0.23, quiet); nifty_midcap_100 (rho 0.453 via dyn_adanient_bo, z 1.48, reacted); dyn_indusindbk_bo (rho 0.439 via dyn_adanient_bo, z 0.09, quiet)
- **India receivers**: nifty_50 (rho 0.489, z -0.23); nifty_midcap_100 (rho 0.453, z 1.48); dyn_indusindbk_bo (rho 0.439, z 0.09)
- Source: Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance Snapshot — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ent-share-price-today-live-25-aug-2026/liveblog/133487865.cms
- Source: Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tata-steel-hcl-tech-bajaj-finance-adani-ports-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/133463103.cms
- Source: SEBI rejects settlement bids by Adani-linked funds — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sebi-rejects-settlement-bids-by-adani-linked-funds/article71383108.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 4.77] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3201.00, z20 2.77, zc -0.07, resid-z -0.51 [quiet], 1d -0.25%, |z20|=2.77
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.645 via dyn_muthootfin_ns, z 1.59, reacted); nifty_midcap_100 (rho 0.563 via dyn_muthootfin_ns, z 1.48, reacted); nifty_50 (rho 0.491 via dyn_muthootfin_ns, z -0.23, quiet); dyn_karurvysya_ns (rho 0.472 via dyn_muthootfin_ns, z 2.09, reacted); dyn_idbi_ns (rho 0.398 via dyn_muthootfin_ns, z 3.01, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.51 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.645, z 1.59); nifty_midcap_100 (rho 0.563, z 1.48); nifty_50 (rho 0.491, z -0.23); dyn_karurvysya_ns (rho 0.472, z 2.09)
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
- Watch next: wti (co-move) — not yet - watch; rho 0.553 vs ust_10y, historically leads by 3d
- Watch next: brent (co-move) — not yet - watch; rho 0.578 vs ust_10y
- Source: Global market: Eurozone bond yields steady as oil prices ease, traders assess Iran sanctions — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-steady-as-oil-prices-ease-traders-assess-iran-sanctions/articleshow/133500147.cms
- Source: Global Market: Japanese bond yields edge higher as US Treasury yields, oil prices rise — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-edge-higher-as-us-treasury-yields-oil-prices-rise/articleshow/133496737.cms
- Source: GERMAN FIN. MIN. KLINGBEIL: SURGE IN BOND YIELDS A RESULT OF TRUMP'S WAR — DeItaone, 2026-08-24. https://t.me/walter_bloomberg/34951
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.11), 2025-05-16 (d=0.19)

### [AMBER 4.4] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.40, zc n/a, resid-z n/a [quiet], 1d 0.07%, 52-wk extreme (pct=100); 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.483 via midcap_largecap_ratio, z 1.48, reacted); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 0.84, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.483, z 1.48); dyn_fincables_ns (rho 0.355, z 0.84)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.26] cross-asset · 3 series ↑
- comex_copper [COMMODITIES]: last 6.64, z20 0.94, zc 0.29, resid-z 0.59 [quiet], 1d 0.64%, 1y-pct=98; co-occur[metal_copper] suppressed: channel WEAK
- dax [INDICES]: last 26328.82, z20 0.85, zc 1.15, resid-z -0.06 [quiet], 1d 0.85%, 1y-pct=98
- stoxx_50 [INDICES]: last 6487.54, z20 0.36, zc 0.78, resid-z -0.43 [quiet], 1d 0.61%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-25 (z-distance 0.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.465 via dax, z 1.48, reacted)
- Watch next: vix (inverse) — not yet - watch; rho -0.603 vs stoxx_50, historically leads by 5d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.597 vs dax, historically leads by 4d
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.596 vs comex_copper, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.584 vs stoxx_50, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.558 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.465, z 1.48)
- Source: Multibagger stocks: Ather Energy, Hind Copper, MCX among stocks which surged up to 250% in one year — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/multibagger-stocks-ather-energy-hind-copper-mcx-among-stocks-which-surged-up-to-250-in-one-year/slideshow/133506231.cms
- Source: Hindustan Copper share price: Stock plunges 7% - Here's why — Mint Markets, 2026-08-25. https://www.livemint.com/market/stock-market-news/hindustan-copper-share-price-stock-plunges-7-heres-why-11787638180391.html
- Source: 9 Stocks to Watch Today: Hind Copper, TCS, Ecofinity, IDFC First Bank, Axis Bank, Fujiyama, Coromandel, Ceigall, Afcons — BusinessLine Mkts, 2026-08-25. https://www.thehindubusinessline.com/markets/buzzing-stocks-hind-copper-tcs-ecofinity-idfc-first-bank-axis-bank-fujiyama-coromandel-ceigall-afcons/article71387102.ece
- Historical analogues: 2025-07-25 (d=0.44), 2025-10-14 (d=0.48), 2024-10-03 (d=0.55)

## Watchlist (below surfacing floor)
comex_gold ↑ (4.03), wheat ↑ (3.92), dyn_lenskart_ns ↑ (3.77), gold_silver_ratio ↑ (3.73), dyn_icicigi_bo ↓ (3.7), fx · 4 series ↑ (3.58), dyn_lth ↑ (3.43), dyn_tech ↑ (3.4), cross-asset · 2 series ↑ (3.15), dyn_idbi_ns ↑ (3.01), dyn_cartrade_ns ↑ (2.89), dyn_pcjeweller_ns ↑ (2.78)

## India macro
- nifty_50: 24334.5508 (1d 0.48%, z20 -0.23, flag none)
- nifty_midcap_100: 64163.3516 (1d 0.54%, z20 1.48, flag amber)
- usd_inr: 95.4100 (1d -0.30%, z20 -0.33, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6367 (1d 0.07%, z20 1.40, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.5 — "Samudra Manthan: India prepares year-wise drilling, rig deployment roadmap"
- COALINDIA.NS (COAL INDIA LTD) score 83.1 — "Samudra Manthan: India prepares year-wise drilling, rig deployment roadmap"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.4 — "Samudra Manthan: India prepares year-wise drilling, rig deployment roadmap"
- INDIANB.NS (INDIAN BANK) score 76.1 — "Oil fall lifts rupee to over one-week high after central bank keeps lid on losses"
- BAC (Bank of America Corporation) score 65.4 — "Oil fall lifts rupee to over one-week high after central bank keeps lid on losses"
- BOND (PIMCO Active Bond Exchange-Tra) score 63.5 — "India bonds flat as oil prices shrug off US curbs on Iran"
- HDB (HDFC Bank Limited) score 61.1 — "Oil fall lifts rupee to over one-week high after central bank keeps lid on losses"
- IDBI.NS (IDBI BANK LIMITED) score 57.5 — "Oil fall lifts rupee to over one-week high after central bank keeps lid on losses"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.5 — "Oil fall lifts rupee to over one-week high after central bank keeps lid on losses"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 57.5 — "Oil fall lifts rupee to over one-week high after central bank keeps lid on losses"
- COIN (Coinbase Global, Inc.) score 51.2 — "Global Market: Japanese businesses turn to currency hedging as weak Yen drives up import c"
- TECHM.NS (TECH MAHINDRA LIMITED) score 50.2 — "Sensex today | Stock Market Live: Sensex up 16 points, Nifty touches 24,199; HCL Tech lead"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.0 — "Sensex today | Stock Market Live: Sensex up 16 points, Nifty touches 24,199; HCL Tech lead"
- TECH (Bio-Techne Corp) score 48.9 — "Sensex today | Stock Market Live: Sensex up 16 points, Nifty touches 24,199; HCL Tech lead"
- OHI (Omega Healthcare Investors, In) score 39.0 — "Oil prices decline as investors brush aside Bessent’s ‘economic D-Day’ for Iran"
- CHKP (Check Point Software Technolog) score 34.1 — "Mukul Agrawal-backed ESDS Software Solution sets price band for Rs 720 crore IPO. Check ke"
- LTH (Life Time Group Holdings, Inc.) score 30.5 — "One Wall Street measure of market fragility just hit its highest possible level. The last "
- 301077.SZ (CHINASTARS) score 22.3 — "Global market: Mainland China stocks slip as metal shares drop, investors await Jackson Ho"
- JIOFIN.BO (Jio Financial Services Limited) score 22.1 — "SEBI drops case against Max Financial, Max Life, Axis entities in ₹3,911 crore case"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.4 — "Shankesh Jewellers, Sunshine Pictures make modest debut, trade below listing prices"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.7 — "SEBI drops case against Max Financial, Max Life, Axis entities in ₹3,911 crore case"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 15.5 — "Multibagger stocks: Ather Energy, Hind Copper, MCX among stocks which surged up to 250% in"
- MS (Morgan Stanley) score 14.2 — "He once mentored Scott Bessent. Now Stanley Druckenmiller is criticizing the treasury secr"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.6 — "IIFL Finance shares drop 8% as IIFL Home Finance gets Rs 963 crore tax demand"
- NVDA (NVIDIA Corporation) score 11.8 — "Global Market: Kospi drops 2% as chip stocks tumble ahead of Nvidia earnings"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.1 — "Pernia's parent Purple Style Labs to launch ₹680 cr IPO on Aug 31"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.0 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.7 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- VT (Vanguard Total World Stock Ind) score 8.3 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- META (Meta) score 7.6 — "Global market: Mainland China stocks slip as metal shares drop, investors await Jackson Ho"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.3 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.0 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.0 — "Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance Snapshot"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.9 — "Xi’s 13-year corruption campaign just keeps accelerating"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.3 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- JEF (Jefferies Financial Group Inc.) score 4.6 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- MRNA (Moderna, Inc.) score 3.9 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 0.8 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
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