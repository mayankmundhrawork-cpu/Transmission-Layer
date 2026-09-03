# Transmission Layer — board brief · 2026-09-03 08:55Z

data as of **2026-09-03** · 98 series · 7 red / 40 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.388, 3d in regime; vol-pct 0.192, breadth-off 0.583, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.4, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.88, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.04, corr60 0.33, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.04, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.19, corr60 -0.1, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.08, corr60 0.21, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 2.2351978664403305e-05)
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.365, β -0.2079, p 0.0); driver zc 2.83 → expected -0.619%. Type hit-rate 0.826 (n=2001).
- **SETUP** dyn_dell → taiwan_weighted: leads 1d (ccf 0.364, β 0.1466, p 1e-05); driver zc 3.68 → expected 2.317%. Type hit-rate 0.826 (n=2001).
- Track record · residual_reversion: hit-rate **0.5** (n=1126) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2001) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.647** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.48] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.39, z20 3.55, zc 0.89, resid-z 0.39 [quiet], 1d 1.15%, |z20|=3.55; 1y-pct=100
- ust_10y [RATES]: last 4.79, z20 2.88, zc 0.85, resid-z 0.46 [quiet], 1d 0.84%, |z20|=2.88; 1y-pct=100
- dyn_bond [EQUITIES]: last 89.89, z20 -2.56, zc 0.41, resid-z -4.24 [unexplained], 1d 0.14%, |z20|=2.56; 1y-pct=0
- tips_10y_real [RATES]: last 2.44, z20 1.24, zc 0.00, resid-z -0.71 [quiet], 1d 0.00%, 1y-pct=98
- ust_30y [RATES]: last 5.27, z20 1.23, zc 0.47, resid-z 0.20 [quiet], 1d 0.38%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.377 vs ust_2y, historically leads by 1d
- Source: Rising Treasury yields emerge as key risk to Wall Street’s record rally — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/rising-treasury-yields-emerge-as-key-risk-to-wall-streets-record-rally/articleshow/133728756.cms
- Source: Global Market: Japan’s Nikkei struggles for direction as chip stocks weigh, bond yields fall — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-struggles-for-direction-as-chip-stocks-weigh-bond-yields-fall/articleshow/133724941.cms
- Source: Gold and silver prices jump 1% on MCX amid a decline in US dollar, bond yields; experts highlight key levels to watch — Mint Markets, 2026-09-03. https://www.livemint.com/market/commodities/gold-and-silver-prices-jump-1-on-mcx-amid-a-decline-in-us-dollar-bond-yields-experts-highlight-key-levels-to-watch-11788407087556.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.04] usd_jpy ↓
- usd_jpy [FX]: last 156.53, z20 -4.04, zc -4.94, resid-z -6.14 [unexplained], 1d -2.29%, |z20|=4.04
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.514 vs usd_jpy
- Source: Yen Surge Keeps Traders on Alert for Further Official Action — Mint Markets, 2026-09-02. https://www.livemint.com/market/yen-surge-keeps-traders-on-alert-for-further-official-action-11788381875091.html
- Source: YEN SURGES MORE THAN 1% WITH TRADERS ON ALERT FOR INTERVENTION — DeItaone, 2026-09-02. https://t.me/walter_bloomberg/35394
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 5.01] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1517.95, z20 -3.01, zc -0.81, resid-z -0.50 [quiet], 1d -1.20%, |z20|=3.01; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Explained: What $127 billion FCNR(B) inflows mean for ICICI Bank, HDFC Bank, other bank stocks — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/explained-what-127-billion-fcnrb-inflows-mean-for-icici-bank-hdfc-bank-other-bank-stocks/articleshow/133725930.cms
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Source: ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/stock-markets/icici-bank-slips-056-as-fcnr-deposit-data-reveals-1788-billion-mobilisation/article71418374.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [AMBER 4.87] commodities · 2 series ↑
- wti [COMMODITIES]: last 90.84, z20 2.04, zc -0.07, resid-z 0.34 [quiet], 1d -0.19%, |z20|=2.04
- brent [COMMODITIES]: last 95.34, z20 1.65, zc -0.12, resid-z 0.41 [quiet], 1d -0.30%, |z20|=1.65
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Chinese Refiners Pay Record Premiums for Russian ESPO Crude — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/Chinese-Refiners-Pay-Record-Premiums-for-Russian-ESPO-Crude.html
- Source: Asian Oil Buying Spree Sends Dubai Crude Toward $100 — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/Asian-Oil-Buying-Spree-Sends-Dubai-Crude-Toward-100.html
- Source: Inox Wind shares rise 2% after bagging Rs 755 crore turnkey order from Indian Oil — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/inox-wind-shares-rise-2-after-bagging-rs-755-crore-turnkey-order-from-indian-oil/articleshow/133725602.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.78] dyn_heromotoco_ns ↓
- dyn_heromotoco_ns [EQUITIES]: last 5287.50, z20 -2.78, zc -0.13, resid-z -0.16 [quiet], 1d -0.24%, |z20|=2.78
- **Mechanism**: dyn_heromotoco_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowdown — Mint Markets, 2026-09-02. https://www.livemint.com/market/mark-to-market/august-auto-sales-maruti-tata-mahindra-tvs-motor-11788333468302.html
- Source: Hero MotoCorp, Eicher Motors fall despite strong August sales — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/hero-motocorp-eicher-motors-fall-despite-strong-august-sales/article71418612.ece
- Source: Why Hero MotoCorp shares fell 5% despite record dispatches — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/stock-markets/hero-motocorp-shares-slide-5-as-retail-data-disappoints-despite-record-dispatch-numbers/article71418322.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [AMBER 4.74] indices · 2 series ↓
- nifty_midcap_100 [INDICES]: last 63149.10, z20 -1.90, zc 0.30, resid-z 0.53 [quiet], 1d 0.23%, |z20|=1.90
- nifty_50 [INDICES]: last 23914.55, z20 -1.90, zc 0.00, resid-z -0.85 [quiet], 1d 0.00%, |z20|=1.90
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.721 via nifty_50, z -1.16, reacted); nifty_fmcg (rho 0.607 via nifty_50, z -1.82, reacted); dyn_indianb_ns (rho 0.558 via nifty_midcap_100, z 1.05, reacted); nifty_it (rho 0.534 via nifty_50, z -0.27, quiet); dyn_adanient_bo (rho 0.5 via nifty_midcap_100, z -1.5, reacted)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.534 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.692 vs nifty_midcap_100
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.616 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.721, z -1.16); nifty_fmcg (rho 0.607, z -1.82); dyn_indianb_ns (rho 0.558, z 1.05); nifty_it (rho 0.534, z -0.27)
- Source: Sensex today | Stock Market Live Updates: Markets shed morning gains; Sensex up 113 pts, Nifty trades below 24,000 — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-3rd-september-2026/article71420222.ece
- Source: Sensex, Nifty trim morning gains by midday; Banking holds firm as IT, Pharma, Consumer stocks weigh — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/sensex-nifty-trim-morning-gains-by-midday-banking-holds-firm-as-it-pharma-consumer-stocks-weigh/article71422838.ece
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Historical analogues: 2025-07-21 (d=0.6), 2024-11-07 (d=0.84), 2025-07-14 (d=0.96)

### [AMBER 4.22] natgas ↑
- natgas [COMMODITIES]: last 2.99, z20 2.22, zc 0.34, resid-z 0.48 [quiet], 1d 1.01%, |z20|=2.22
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.1 vs natgas, historically leads by 4d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.055 vs natgas, historically leads by 4d
- Source: Asian LNG Prices Surge to Highest Since 2022 as Iran War Escalates — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/Asian-LNG-Prices-Surge-to-Highest-Since-2022-as-Iran-War-Escalates.html
- Source: Qatar and UAE Turn to Rare LNG Ship Transfers as Hormuz Crisis Drags On — OilPrice, 2026-09-02. https://oilprice.com/Latest-Energy-News/World-News/Qatar-and-UAE-Turn-to-Rare-LNG-Ship-Transfers-as-Hormuz-Crisis-Drags-On.html
- Source: Pakistan Rejects Costly LNG Cargo as Blackout Risk Deepens — OilPrice, 2026-09-02. https://oilprice.com/Latest-Energy-News/World-News/Pakistan-Rejects-Costly-LNG-Cargo-as-Blackout-Risk-Deepens.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.2] dyn_coalindia_ns ↑
- dyn_coalindia_ns [EQUITIES]: last 418.70, z20 2.20, zc 0.15, resid-z 0.32 [quiet], 1d 0.20%, |z20|=2.20
- **Mechanism**: dyn_coalindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PTC India, Coal India among 10 stocks offering dividend yields of up to 10% — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/ptc-india-coal-india-among-10-stocks-offering-dividend-yields-of-up-to-10/slideshow/133730231.cms
- Source: Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/mahanadi-coalfields-files-drhp-with-sebi-for-ipo-coal-india-plans-to-sell-10-stake/article71420575.ece
- Source: Coal India arm Mahanadi Coalfields files IPO papers, plans OFS of up to 66 cr shares — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/ipos/fpos/coal-india-arm-mahanadi-coalfields-files-drhp-for-ipo-ofs-up-to-66-18-crore-shares/articleshow/133705532.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

## Watchlist (below surfacing floor)
nikkei_225 ↓ (3.92), usd_inr ↓ (3.83), dyn_dell ↑ (3.79), midcap_largecap_ratio ↑ (3.61), dyn_tataelxsi_ns ↓ (3.51), dyn_atherenerg_ns ↑ (3.27), bovespa ↑ (3.16), indices · 3 series ↓ (3.15), dyn_nvda ↑ (3.06), gold_silver_ratio ↓ (3.03), dyn_havells_ns ↓ (2.45), dyn_tech ↑ (2.36)

## India macro
- nifty_50: 23914.5508 (1d 0.00%, z20 -1.90, flag amber)
- nifty_midcap_100: 63149.1016 (1d 0.23%, z20 -1.90, flag amber)
- usd_inr: 94.4780 (1d -0.50%, z20 -1.83, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6406 (1d 0.23%, z20 0.61, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.8 — "Indian govt bonds on course for stable opening, short-end debt may notch some gains"
- COALINDIA.NS (COAL INDIA LTD) score 87.9 — "Indian govt bonds on course for stable opening, short-end debt may notch some gains"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 86.0 — "Indian govt bonds on course for stable opening, short-end debt may notch some gains"
- INDIANB.NS (INDIAN BANK) score 77.1 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- BAC (Bank of America Corporation) score 66.3 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- BOND (PIMCO Active Bond Exchange-Tra) score 59.8 — "Indian govt bonds on course for stable opening, short-end debt may notch some gains"
- COIN (Coinbase Global, Inc.) score 58.4 — "Swiggy shares fall 2%, down for 3rd session, as MSCI set to remove stock from Global Stand"
- HDB (HDFC Bank Limited) score 57.2 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- IDBI.NS (IDBI BANK LIMITED) score 54.9 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 54.9 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 54.8 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- CHKP (Check Point Software Technolog) score 40.7 — "Asset Reconstruction IPO: Price band set at  ₹132- ₹139 per share; check key dates, issue "
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.3 — "US Market: Tech stocks challenge Wall Street’s traditional bear market definition"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 34.9 — "US Market: Tech stocks challenge Wall Street’s traditional bear market definition"
- TECH (Bio-Techne Corp) score 34.9 — "US Market: Tech stocks challenge Wall Street’s traditional bear market definition"
- OHI (Omega Healthcare Investors, In) score 32.6 — "Oil prices edge lower as investors weigh US-Iran strike risks"
- LTH (Life Time Group Holdings, Inc.) score 28.1 — "There’s a new record number of 401(k) millionaires as retirement savings hold at all-time "
- 301077.SZ (CHINASTARS) score 27.5 — "Unstable Tibetan Plateau risks cascading disasters as glacier losses mount in Nepal, China"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.7 — "Antelopus Selan Energy share price up over 32% up in 3 days - What's behind continuous sto"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.4 — "IPO GMP Live Updates | Lumino Industries stock surges after stellar debut, Deepa Jewellers"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 15.8 — "Small investors, big money! 15 retail-heavy subscribed IPOs of 2026 deliver up to 76% retu"
- NVDA (NVIDIA Corporation) score 15.5 — "Nvidia’s stock is climbing as investors get more confidence in an expanding base of AI cus"
- JIOFIN.BO (Jio Financial Services Limited) score 13.8 — "Stocks to buy: Nagaraj Shetti recommends eClerx Services, UNO Minda shares to buy in the s"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.2 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.2 — "PTC India, Coal India among 10 stocks offering dividend yields of up to 10%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.1 — "Motilal Oswal initiates coverage on Adani Power with Buy call, sees 20% upside. Time to ho"
- META (Meta) score 8.2 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "South Korea's semiconductor exports just tripled year-over-year. Is it too much of a good "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.9 — "JM Financial Asset Management garners Rs 700 crore from maiden pre-IPO fund"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.0 — "Why auto stocks are down today? Eicher, Tata Motors, Hyundai, Bajaj Auto and others - Chec"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.0 — "Why auto stocks are down today? Eicher, Tata Motors, Hyundai, Bajaj Auto and others - Chec"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.5 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- MS (Morgan Stanley) score 6.5 — "JPMORGAN: RISING YIELDS WON’T KILL STOCK RALLY JPMorgan remains bullish on global equities"
- VT (Vanguard Total World Stock Ind) score 5.9 — "What’s behind the selloff in world bond markets?"
- DELL (Dell Technologies Inc.) score 5.3 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.9 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.4 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 0.8 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.6 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas reported strong growth in June quarter, but failed to impress"

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