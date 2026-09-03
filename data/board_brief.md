# Transmission Layer — board brief · 2026-09-03 22:32Z

data as of **2026-09-03** · 98 series · 6 red / 45 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.33, 1d in regime; vol-pct 0.249, breadth-off 0.412, Markov P(high-vol) 0.026)
- [INVERTED] **safe_haven_gold** — corr20 -0.44, corr60 -0.41, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.88, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.0, corr60 0.34, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.04, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.15, corr60 -0.09, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.23, corr60 -0.14, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.05, corr60 0.22, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 7.500666754367558e-13)
- **SETUP** dxy → eur_usd: leads 1d (ccf -0.836, β -0.9039, p 0.0); driver zc -1.64 → expected 0.506%. Type hit-rate 0.829 (n=1971).
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.726, β -0.7802, p 0.0); driver zc -1.64 → expected 0.436%. Type hit-rate 0.829 (n=1971).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.468, β 0.7926, p 0.0); driver zc 1.57 → expected 0.935%. Type hit-rate 0.829 (n=1971).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.42, β 0.7079, p 0.0); driver zc 1.57 → expected 0.835%. Type hit-rate 0.829 (n=1971).
- Track record · residual_reversion: hit-rate **0.5** (n=1128) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=1971) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.647** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.07] usd_jpy ↓
- usd_jpy [FX]: last 155.88, z20 -5.07, zc -5.83, resid-z -7.17 [unexplained], 1d -2.70%, |z20|=5.07
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.527 vs usd_jpy
- Source: YEN EXTENDS GAINS TO 2% VERSUS DOLLAR, STRONGEST SINCE AUG. 3 — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35430
- Source: DOLLAR/YEN EXTENDS FALL, NOW DOWN 1.75% AT 155.9 — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35426
- Source: Yen Surge Keeps Traders on Alert for Further Official Action — Mint Markets, 2026-09-02. https://www.livemint.com/market/yen-surge-keeps-traders-on-alert-for-further-official-action-11788381875091.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 6.59] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.39, z20 2.66, zc 0.00, resid-z 0.16 [quiet], 1d 0.00%, |z20|=2.66; 1y-pct=99
- ust_10y [RATES]: last 4.79, z20 2.37, zc 0.00, resid-z 0.12 [quiet], 1d 0.00%, |z20|=2.37; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.04, z20 -1.64, zc 0.52, resid-z 0.94 [quiet], 1d 0.17%, 1y-pct=1
- tips_10y_real [RATES]: last 2.45, z20 1.41, zc 0.24, resid-z 0.43 [quiet], 1d 0.41%, 1y-pct=99
- ust_30y [RATES]: last 5.27, z20 1.11, zc 0.00, resid-z 0.06 [quiet], 1d 0.00%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.372 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.51 vs dyn_bond
- Source: Wall Street is betting on Fed Chair Kevin Warsh to keep a manic bond market from unraveling — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/wall-street-is-betting-on-fed-chair-kevin-warsh-to-keep-a-manic-bond-market-from-unraveling-03bbd093?mod=mw_rss_topstories
- Source: HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the Fed outlook turns more hawkish. The bank still expects rates to remain unchanged, but now sees a near-even chance of a 25bp September hike. HSBC forecasts 2-year yields at 4.20% and 10-year yields at 4.65% by en — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35422
- Source: Global Market: European stocks rise as bond selloff eases; investors await U.S. jobs data — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-stocks-rise-as-bond-selloff-eases-investors-await-u-s-jobs-data/articleshow/133732839.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 5.23] cross-asset · 4 series ↑
- vix [INDICES]: last 14.31, z20 -1.57, zc -0.69, resid-z n/a [quiet], 1d -5.86%, |z20|=1.57; 1y-pct=2
- dyn_vt [EQUITIES]: last 161.75, z20 1.14, zc 1.42, resid-z -0.03 [quiet], 1d 1.02%, 1y-pct=98
- sp500 [INDICES]: last 7747.80, z20 0.85, zc 1.47, resid-z -0.24 [quiet], 1d 1.06%, 1y-pct=98
- dow_jones [INDICES]: last 53687.54, z20 0.54, zc 1.57, resid-z 0.78 [priced], 1d 1.18%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-17 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.648 vs vix, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.64 vs dyn_vt, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.542 vs dyn_vt, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.509 vs dyn_vt
- Source: Wall Street ends sharply higher as Waller remarks ease rate hike fears — Mint Markets, 2026-09-03. https://www.livemint.com/market/wall-street-ends-sharply-higher-as-waller-remarks-ease-rate-hike-fears-11788465720251.html
- Source: Wall Street is betting on Fed Chair Kevin Warsh to keep a manic bond market from unraveling — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/wall-street-is-betting-on-fed-chair-kevin-warsh-to-keep-a-manic-bond-market-from-unraveling-03bbd093?mod=mw_rss_topstories
- Source: U.S. STOCKS EXTEND GAINS, S&P 500 UP 1.00 PCT — DeItaone, 2026-09-03. https://t.me/walter_bloomberg/35446
- Historical analogues: 2024-10-17 (d=0.46), 2025-10-21 (d=0.48), 2025-08-27 (d=0.53)

### [AMBER 5.15] commodities · 2 series ↑
- wti [COMMODITIES]: last 91.77, z20 2.32, zc 0.32, resid-z 0.51 [quiet], 1d 0.84%, |z20|=2.32
- brent [COMMODITIES]: last 95.82, z20 1.80, zc 0.08, resid-z 0.35 [quiet], 1d 0.20%, |z20|=1.80
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.666 vs wti
- Source: High Oil Prices Speed Up China’s Shift Away From Crude — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/High-Oil-Prices-Speed-Up-Chinas-Shift-Away-From-Crude.html
- Source: Machado Backs U.S. Oil Partnership but Questions Venezuela Deal — OilPrice, 2026-09-03. https://oilprice.com/Latest-Energy-News/World-News/Machado-Backs-US-Oil-Partnership-but-Questions-Venezuela-Deal.html
- Source: UK Borrowing Costs Surge as Oil Shock Rattles Global Markets — OilPrice, 2026-09-03. https://oilprice.com/Energy/Energy-General/UK-Borrowing-Costs-Surge-as-Oil-Shock-Rattles-Global-Markets.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.13] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1514.00, z20 -3.13, zc -0.98, resid-z -0.56 [quiet], 1d -1.46%, |z20|=3.13; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Explained: What $127 billion FCNR(B) inflows mean for ICICI Bank, HDFC Bank, other bank stocks — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/explained-what-127-billion-fcnrb-inflows-mean-for-icici-bank-hdfc-bank-other-bank-stocks/articleshow/133725930.cms
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Source: ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/stock-markets/icici-bank-slips-056-as-fcnr-deposit-data-reveals-1788-billion-mobilisation/article71418374.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 4.73] dyn_dell ↑
- dyn_dell [EQUITIES]: last 515.94, z20 2.73, zc 0.53, resid-z 2.36 [unexplained], 1d 4.82%, |z20|=2.73; 1y-pct=100
- **Mechanism**: dyn_dell ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho 0.473 via dyn_dell, z 2.45, reacted); nifty_it (rho -0.421 via dyn_dell, z -0.32, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.542 vs dyn_dell, historically leads by 5d
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
- dyn_coalindia_ns [EQUITIES]: last 420.05, z20 2.45, zc 0.40, resid-z 0.47 [quiet], 1d 0.53%, |z20|=2.45
- **Mechanism**: dyn_coalindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PTC India, Coal India among 10 stocks offering dividend yields of up to 10% — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/ptc-india-coal-india-among-10-stocks-offering-dividend-yields-of-up-to-10/slideshow/133730231.cms
- Source: Mahanadi Coalfields files DRHP with SEBI for IPO, Coal India plans to sell 10% stake — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/mahanadi-coalfields-files-drhp-with-sebi-for-ipo-coal-india-plans-to-sell-10-stake/article71420575.ece
- Source: Coal India arm Mahanadi Coalfields files IPO papers, plans OFS of up to 66 cr shares — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/ipos/fpos/coal-india-arm-mahanadi-coalfields-files-drhp-for-ipo-ofs-up-to-66-18-crore-shares/articleshow/133705532.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

## Watchlist (below surfacing floor)
nifty_50 ↓ (4.12), midcap_largecap_ratio ↑ (3.97), nikkei_225 ↓ (3.92), usd_inr ↓ (3.83), dyn_nvda ↑ (3.75), gold_silver_ratio ↓ (3.72), dyn_tech ↑ (3.3), dyn_atherenerg_ns ↑ (3.29), bovespa ↑ (2.62), fx · 2 series ↑ (2.59), indices · 2 series ↓ (2.49), brent_wti_spread ↓ (2.45)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.6 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- COALINDIA.NS (COAL INDIA LTD) score 79.9 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.3 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- INDIANB.NS (INDIAN BANK) score 77.0 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- BAC (Bank of America Corporation) score 66.6 — "Oura files for IPO amid Americans’ obsession with tracking their sleep, steps and heart ra"
- HDB (HDFC Bank Limited) score 57.6 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- COIN (Coinbase Global, Inc.) score 56.8 — "UK Borrowing Costs Surge as Oil Shock Rattles Global Markets"
- BOND (PIMCO Active Bond Exchange-Tra) score 56.2 — "Wall Street is betting on Fed Chair Kevin Warsh to keep a manic bond market from unravelin"
- IDBI.NS (IDBI BANK LIMITED) score 55.6 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 55.6 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 55.6 — "HSBC HIKES TREASURY YIELD FORECASTS HSBC raised its U.S. Treasury yield forecasts as the F"
- CHKP (Check Point Software Technolog) score 41.2 — "High conviction picks: Up to 44% upside - 5 large caps, 9 mid and small caps stocks | Chec"
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.7 — "Nvidia takes back control of the AI trade as Big Tech nears record highs"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.3 — "Nvidia takes back control of the AI trade as Big Tech nears record highs"
- TECH (Bio-Techne Corp) score 35.3 — "Nvidia takes back control of the AI trade as Big Tech nears record highs"
- OHI (Omega Healthcare Investors, In) score 35.2 — "This subtle Microsoft change could be a big win for investors"
- LTH (Life Time Group Holdings, Inc.) score 29.4 — "TRUMP’S THURSDAY SCHEDULE 🔸 8:00 AM — Executive Time 🔸 11:00 AM — Intelligence Briefing 🔸 "
- 301077.SZ (CHINASTARS) score 27.0 — "CHINA AND RUSSIA PUSH FOR DEEPER INVESTMENT TIES China is ready to expand investment coope"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.6 — "Indian Energy Exchange records highest-ever monthly electricity volume in August"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.1 — "Deepa Jewellers IPO Day 3: GMP falls to 13%, issue booked 42x"
- NVDA (NVIDIA Corporation) score 17.5 — "Nvidia takes back control of the AI trade as Big Tech nears record highs"
- JIOFIN.BO (Jio Financial Services Limited) score 15.9 — "FED'S WALLER SAYS MORTGAGE RATES, AUTO LOAN RATES ARE NOT LOW FED'S WALLER SAYS 'LOOSE FIN"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.8 — "Retail sugar price drops 3.85% to ₹62.57/kg in a week: Govt data"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.7 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.7 — "PTC India, Coal India among 10 stocks offering dividend yields of up to 10%"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.1 — "TRUMP: I JUST WANT THE WAR ENDED IN UKRAINE"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.8 — "Adani Ports shares rise 2% on record August cargo volumes, brokerages bullish"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.9 — "FED'S WALLER SAYS MORTGAGE RATES, AUTO LOAN RATES ARE NOT LOW FED'S WALLER SAYS 'LOOSE FIN"
- VT (Vanguard Total World Stock Ind) score 7.9 — "Jindal Worldwide stock hits upper circuit - What's behind the share price jump?"
- META (Meta) score 7.2 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.1 — "16% jump in share price of this firm after  ₹100 crore order from Tata Motors PV | Do you "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.0 — "16% jump in share price of this firm after  ₹100 crore order from Tata Motors PV | Do you "
- MS (Morgan Stanley) score 6.6 — "Clean sweep or divided Congress, these are the midterm-elections trades to make, says JPMo"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.7 — "ICICI Bank shares slip 0.56% as FCNR mobilisation hits $17.88 bn"
- DELL (Dell Technologies Inc.) score 4.6 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.6 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.1 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 0.7 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
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