# Transmission Layer — board brief · 2026-09-03 19:18Z

data as of **2026-09-03** · 98 series · 7 red / 44 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.33, 1d in regime; vol-pct 0.249, breadth-off 0.412, Markov P(high-vol) 0.027)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.41, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.88, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.0, corr60 0.34, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.04, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.09, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.22, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 2.2351978664403305e-05)
- **SETUP** dxy → eur_usd: leads 1d (ccf -0.836, β -0.904, p 0.0); driver zc -1.86 → expected 0.573%. Type hit-rate 0.831 (n=1936).
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.726, β -0.7802, p 0.0); driver zc -1.86 → expected 0.495%. Type hit-rate 0.831 (n=1936).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.543, β 0.8519, p 0.0); driver zc 1.51 → expected 0.927%. Type hit-rate 0.831 (n=1936).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.523, β 0.8315, p 0.0); driver zc 1.51 → expected 0.905%. Type hit-rate 0.831 (n=1936).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.468, β 0.7926, p 0.0); driver zc 1.51 → expected 0.898%. Type hit-rate 0.831 (n=1936).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.42, β 0.7079, p 0.0); driver zc 1.51 → expected 0.802%. Type hit-rate 0.831 (n=1936).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.364, β 0.8356, p 0.0); driver zc 1.51 → expected 0.909%. Type hit-rate 0.831 (n=1936).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.298, β 0.4584, p 0.00068); driver zc 1.51 → expected 0.499%. Type hit-rate 0.831 (n=1936).
- Track record · residual_reversion: hit-rate **0.5** (n=1128) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.831** (n=1936) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.647** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.48] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.39, z20 3.55, zc 0.89, resid-z 0.39 [quiet], 1d 1.15%, |z20|=3.55; 1y-pct=100
- ust_10y [RATES]: last 4.79, z20 2.88, zc 0.85, resid-z 0.46 [quiet], 1d 0.84%, |z20|=2.88; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.06, z20 -1.59, zc 0.57, resid-z -4.24 [unexplained], 1d 0.19%, 1y-pct=1
- tips_10y_real [RATES]: last 2.44, z20 1.24, zc 0.00, resid-z -0.71 [quiet], 1d 0.00%, 1y-pct=98
- ust_30y [RATES]: last 5.27, z20 1.23, zc 0.47, resid-z 0.20 [quiet], 1d 0.38%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.374 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.511 vs dyn_bond
- Source: Wall Street is betting on Fed Chair Kevin Warsh to keep a manic bond market from unraveling — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/wall-street-is-betting-on-fed-chair-kevin-warsh-to-keep-a-manic-bond-market-from-unraveling-03bbd093?mod=mw_rss_topstories
- Source: HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the Fed outlook turns more hawkish. The bank still expects rates to remain unchanged, but now sees a near-even chance of a 25bp September hike. HSBC forecasts 2-year yields at 4.20% and 10-year yields at 4.65% by en — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35422
- Source: Global Market: European stocks rise as bond selloff eases; investors await U.S. jobs data — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-stocks-rise-as-bond-selloff-eases-investors-await-u-s-jobs-data/articleshow/133732839.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.34] usd_jpy ↓
- usd_jpy [FX]: last 155.70, z20 -5.34, zc -6.06, resid-z -7.45 [unexplained], 1d -2.81%, |z20|=5.34
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.529 vs usd_jpy
- Source: YEN EXTENDS GAINS TO 2% VERSUS DOLLAR, STRONGEST SINCE AUG. 3 — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35430
- Source: DOLLAR/YEN EXTENDS FALL, NOW DOWN 1.75% AT 155.9 — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35426
- Source: Yen Surge Keeps Traders on Alert for Further Official Action — Mint Markets, 2026-09-02. https://www.livemint.com/market/yen-surge-keeps-traders-on-alert-for-further-official-action-11788381875091.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 5.13] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1514.00, z20 -3.13, zc -0.98, resid-z -0.57 [quiet], 1d -1.46%, |z20|=3.13; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Explained: What $127 billion FCNR(B) inflows mean for ICICI Bank, HDFC Bank, other bank stocks — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/explained-what-127-billion-fcnrb-inflows-mean-for-icici-bank-hdfc-bank-other-bank-stocks/articleshow/133725930.cms
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Source: ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/stock-markets/icici-bank-slips-056-as-fcnr-deposit-data-reveals-1788-billion-mobilisation/article71418374.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [AMBER 5.1] commodities · 2 series ↑
- wti [COMMODITIES]: last 91.60, z20 2.27, zc 0.25, resid-z 0.46 [quiet], 1d 0.65%, |z20|=2.27
- brent [COMMODITIES]: last 95.68, z20 1.76, zc 0.02, resid-z 0.31 [quiet], 1d 0.05%, |z20|=1.76
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.67 vs wti
- Source: High Oil Prices Speed Up China’s Shift Away From Crude — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/High-Oil-Prices-Speed-Up-Chinas-Shift-Away-From-Crude.html
- Source: Machado Backs U.S. Oil Partnership but Questions Venezuela Deal — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/Machado-Backs-US-Oil-Partnership-but-Questions-Venezuela-Deal.html
- Source: UK Borrowing Costs Surge as Oil Shock Rattles Global Markets — OilPrice, 2026-09-03. https://oilprice.com/Energy/Energy-General/UK-Borrowing-Costs-Surge-as-Oil-Shock-Rattles-Global-Markets.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.03] cross-asset · 4 series ↑
- vix [INDICES]: last 14.42, z20 -1.36, zc -0.61, resid-z n/a [quiet], 1d -5.13%, 1y-pct=3
- dyn_vt [EQUITIES]: last 161.76, z20 1.15, zc 1.43, resid-z 0.22 [quiet], 1d 1.03%, 1y-pct=98
- sp500 [INDICES]: last 7750.04, z20 0.90, zc 1.51, resid-z 0.25 [priced], 1d 1.09%, 1y-pct=98
- dow_jones [INDICES]: last 53663.12, z20 0.47, zc 1.51, resid-z 0.58 [priced], 1d 1.13%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-17 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.647 vs vix, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.639 vs dyn_vt, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.542 vs dyn_vt, historically leads by 1d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.511 vs dow_jones, historically leads by 2d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.509 vs dyn_vt
- Source: Wall Street is betting on Fed Chair Kevin Warsh to keep a manic bond market from unraveling — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/wall-street-is-betting-on-fed-chair-kevin-warsh-to-keep-a-manic-bond-market-from-unraveling-03bbd093?mod=mw_rss_topstories
- Source: As Broadcom’s stock falls, Wall Street focuses on the company’s forecast — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/broadcom-stock-fall-as-investors-weigh-guidance-heres-what-wall-street-analysts-are-saying-9048c0e6?mod=mw_rss_topstories
- Source: US stocks today: NaS&P 500 rise as Fed's Waller signals openness to holding rates steady — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-higher-after-feds-waller-signals-patience-on-rate-policy/articleshow/133737976.cms
- Historical analogues: 2024-10-17 (d=0.46), 2025-10-21 (d=0.48), 2025-08-27 (d=0.53)

### [RED 4.7] dyn_dell ↑
- dyn_dell [EQUITIES]: last 515.33, z20 2.70, zc 0.52, resid-z -1.09 [quiet], 1d 4.70%, |z20|=2.70; 1y-pct=100
- **Mechanism**: dyn_dell ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho 0.473 via dyn_dell, z 2.45, reacted); nifty_it (rho -0.421 via dyn_dell, z -0.32, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.541 vs dyn_dell, historically leads by 5d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.107 vs dyn_dell, historically leads by 1d
- **India receivers**: dyn_coalindia_ns (rho 0.473, z 2.45); nifty_it (rho -0.421, z -0.32)
- Source: Dell’s AI Boom: $95 billion backlog reshapes growth outlook — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/dells-ai-boom-95-billion-backlog-reshapes-growth-outlook/slideshow/133726366.cms
- Source: HPE follows in Dell’s footsteps as it rides the AI server boom to a big earnings beat — MarketWatch Top, 2026-09-02. https://www.marketwatch.com/story/hpe-follows-in-dells-footsteps-as-it-rides-the-ai-server-boom-to-a-big-earnings-beat-ec46eaea?mod=mw_rss_topstories
- Source: Dell stock price news: Shares jump 14% on record Q2 results as AI server demand surges — data details — Mint Markets, 2026-09-02. https://www.livemint.com/market/stock-market-news/dell-stock-price-news-shares-jump-14-on-record-q2-results-as-ai-server-demand-surges-data-details-11788356963938.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

### [RED 4.63] dyn_heromotoco_ns ↓
- dyn_heromotoco_ns [EQUITIES]: last 5308.50, z20 -2.63, zc 0.09, resid-z 0.22 [quiet], 1d 0.16%, |z20|=2.63
- **Mechanism**: dyn_heromotoco_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowdown — Mint Markets, 2026-09-02. https://www.livemint.com/market/mark-to-market/august-auto-sales-maruti-tata-mahindra-tvs-motor-11788333468302.html
- Source: Hero MotoCorp, Eicher Motors fall despite strong August sales — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/hero-motocorp-eicher-motors-fall-despite-strong-august-sales/article71418612.ece
- Source: Why Hero MotoCorp shares fell 5% despite record dispatches — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/stock-markets/hero-motocorp-shares-slide-5-as-retail-data-disappoints-despite-record-dispatch-numbers/article71418322.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [AMBER 4.45] dyn_coalindia_ns ↑
- dyn_coalindia_ns [EQUITIES]: last 420.05, z20 2.45, zc 0.40, resid-z 0.48 [quiet], 1d 0.53%, |z20|=2.45
- **Mechanism**: dyn_coalindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PTC India, Coal India among 10 stocks offering dividend yields of up to 10% — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/ptc-india-coal-india-among-10-stocks-offering-dividend-yields-of-up-to-10/slideshow/133730231.cms
- Source: Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/mahanadi-coalfields-files-drhp-with-sebi-for-ipo-coal-india-plans-to-sell-10-stake/article71420575.ece
- Source: Coal India arm Mahanadi Coalfields files IPO papers, plans OFS of up to 66 cr shares — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/ipos/fpos/coal-india-arm-mahanadi-coalfields-files-drhp-for-ipo-ofs-up-to-66-18-crore-shares/articleshow/133705532.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

## Watchlist (below surfacing floor)
nifty_50 ↓ (4.12), dyn_nvda ↑ (3.98), midcap_largecap_ratio ↑ (3.97), nikkei_225 ↓ (3.92), usd_inr ↓ (3.83), gold_silver_ratio ↓ (3.62), dyn_tech ↑ (3.38), dyn_atherenerg_ns ↑ (3.29), fx · 2 series ↑ (2.64), bovespa ↑ (2.56), indices · 2 series ↓ (2.49), brent_wti_spread ↓ (2.41)

## India macro
- nifty_50: 23873.4492 (1d -0.17%, z20 -2.12, flag amber)
- nifty_midcap_100: 63235.8984 (1d 0.36%, z20 -1.64, flag amber)
- usd_inr: 94.4750 (1d -0.51%, z20 -1.83, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6488 (1d 0.54%, z20 0.97, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.2 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- COALINDIA.NS (COAL INDIA LTD) score 82.4 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.7 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- INDIANB.NS (INDIAN BANK) score 79.4 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- BAC (Bank of America Corporation) score 67.7 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- HDB (HDFC Bank Limited) score 59.4 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- COIN (Coinbase Global, Inc.) score 58.6 — "UK Borrowing Costs Surge as Oil Shock Rattles Global Markets"
- BOND (PIMCO Active Bond Exchange-Tra) score 58.0 — "Wall Street is betting on Fed Chair Kevin Warsh to keep a manic bond market from unravelin"
- IDBI.NS (IDBI BANK LIMITED) score 57.3 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.3 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 57.3 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- CHKP (Check Point Software Technolog) score 42.5 — "High conviction picks: Up to 44% upside - 5 large caps, 9 mid and small caps stocks | Chec"
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.8 — "Broker’s Call: Happiest Minds Tech (Buy)"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.4 — "Broker’s Call: Happiest Minds Tech (Buy)"
- TECH (Bio-Techne Corp) score 35.4 — "Broker’s Call: Happiest Minds Tech (Buy)"
- OHI (Omega Healthcare Investors, In) score 34.3 — "Global Market: European stocks rise as bond selloff eases; investors await U.S. jobs data"
- LTH (Life Time Group Holdings, Inc.) score 30.3 — "TRUMP’S THURSDAY SCHEDULE 🔸 8:00 AM — Executive Time 🔸 11:00 AM — Intelligence Briefing 🔸 "
- 301077.SZ (CHINASTARS) score 27.8 — "CHINA AND RUSSIA PUSH FOR DEEPER INVESTMENT TIES China is ready to expand investment coope"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.4 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.6 — "Deepa Jewellers IPO Day 3: GMP falls to 13%, issue booked 42x"
- NVDA (NVIDIA Corporation) score 17.0 — "NVDA - NVIDIA TO ACQUIRE HUGGING FACE IN $11.9BN DEAL Nvidia has agreed to acquire Hugging"
- JIOFIN.BO (Jio Financial Services Limited) score 16.5 — "FED'S WALLER SAYS MORTGAGE RATES, AUTO LOAN RATES ARE NOT LOW FED'S WALLER SAYS 'LOOSE FIN"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 15.2 — "Retail sugar price drops 3.85% to ₹62.57/kg in a week: Govt data"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.1 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.0 — "PTC India, Coal India among 10 stocks offering dividend yields of up to 10%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.2 — "Adani Ports shares rise 2% on record August cargo volumes, brokerages bullish"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.4 — "FCNRB deposits: Why bank investors should watch RoE, not just NIM"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "FED'S WALLER SAYS MORTGAGE RATES, AUTO LOAN RATES ARE NOT LOW FED'S WALLER SAYS 'LOOSE FIN"
- VT (Vanguard Total World Stock Ind) score 8.2 — "Jindal Worldwide stock hits upper circuit - What's behind the share price jump?"
- META (Meta) score 7.5 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.3 — "16% jump in share price of this firm after  ₹100 crore order from Tata Motors PV | Do you "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.3 — "16% jump in share price of this firm after  ₹100 crore order from Tata Motors PV | Do you "
- MS (Morgan Stanley) score 6.8 — "Clean sweep or divided Congress, these are the midterm-elections trades to make, says JPMo"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.9 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- DELL (Dell Technologies Inc.) score 4.8 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.6 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.2 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
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