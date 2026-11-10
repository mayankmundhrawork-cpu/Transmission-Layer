# Transmission Layer — board brief · 2026-11-10 03:41Z

data as of **2026-11-10** · 97 series · 11 red / 34 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 4d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.555)
- [INVERTED] **safe_haven_gold** — corr20 -0.15, corr60 -0.22, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 0.05, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.33, corr60 0.29, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **9 of 89** scanned series survive multiplicity control (effective p ≤ 0.009054222265934664)
- **SETUP** dax → asx_200: leads 1d (ccf 0.264, β 0.1919, p 0.00445); driver zc -1.71 → expected -0.368%. Type hit-rate 0.819 (n=2148).
- Track record · residual_reversion: hit-rate **0.508** (n=1127) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2148) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.15] cross-asset · 7 series ↑
- nifty_50 [INDICES]: last 25044.65, z20 2.81, zc 1.80, resid-z 2.78 [unexplained], 1d 0.06%, |z20|=2.81
- dyn_muthootfin_ns [EQUITIES]: last 2917.60, z20 2.64, zc 0.28, resid-z -0.76 [quiet], 1d 1.69%, |z20|=2.64
- dyn_bajfinance_ns [EQUITIES]: last 1064.85, z20 2.28, zc 0.74, resid-z -0.69 [quiet], 1d -2.11%, |z20|=2.28
- nifty_metal [INDICES]: last 12664.75, z20 2.22, zc 0.45, resid-z -1.15 [quiet], 1d -0.11%, |z20|=2.22
- dyn_jiofin_bo [EQUITIES]: last 229.95, z20 2.18, zc 0.25, resid-z -1.10 [quiet], 1d -0.28%, |z20|=2.18
- nifty_midcap_100 [INDICES]: last 61018.65, z20 2.09, zc 0.00, resid-z -2.77 [unexplained], 1d 0.66%, |z20|=2.09
- nifty_fmcg [INDICES]: last 46660.10, z20 1.91, zc 0.49, resid-z -1.60 [unexplained], 1d -0.27%, |z20|=1.91
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.733 via nifty_metal, z 1.06, reacted); dyn_indusindbk_bo (rho 0.632 via nifty_midcap_100, z 1.32, reacted); dyn_indianb_ns (rho 0.607 via nifty_midcap_100, z 4.09, reacted); dyn_policybzr_ns (rho 0.527 via nifty_midcap_100, z -1.36, reacted); nifty_it (rho 0.514 via nifty_50, z 0.71, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.514 vs nifty_50, historically leads by 5d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.505 vs dyn_jiofin_bo
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.502 vs dyn_muthootfin_ns
- **India receivers**: dyn_adanient_bo (rho 0.733, z 1.06); dyn_indusindbk_bo (rho 0.632, z 1.32); dyn_indianb_ns (rho 0.607, z 4.09); dyn_policybzr_ns (rho 0.527, z -1.36)
- Source: Promoter holding in Nifty 50 firms falls to 40% — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/promoter-holding-in-nifty-50-firms-falls-to-40/article71683186.ece
- Source: Eternal shares rebound over 70% from March lows, emerge as top Nifty 50 recovery stock; what drove the rally? — Mint Markets, 2026-11-09. https://www.livemint.com/market/eternal-shares-rebound-over-70-from-march-lows-emerge-as-top-nifty-50-recovery-stock-what-drove-the-rally-11794234112702.html
- Source: Nifty holds 25,000 after volatile session; PSU Banks surge 3.7%, IT drags — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/nifty-holds-25000-after-volatile-session-psu-banks-surge-37-it-drags/article71682374.ece
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-11 (d=1.35), 2025-12-23 (d=1.37)

### [RED 7.11] usd_inr ↓
- usd_inr [FX]: last 93.90, z20 -2.11, zc -0.13, resid-z -0.39 [quiet], 1d -0.59%, 20d range extreme; |z20|=2.11; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.381 via usd_inr, z -0.26, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.381, z -0.26)
- Source: Rupee’s 5-day winning streak ends with the currency closing at ₹93.93 — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/forex/rupees-5-day-winning-streak-ends-with-the-currency-closing-at-9393/article71683133.ece
- Source: FPI investments in FAR G-Secs rise nearly ₹8,000 cr as rupee gains, bond yields ease — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/fpi-investments-in-far-g-secs-rise-nearly-8000-cr-as-rupee-gains-bond-yields-ease/article71682301.ece
- Source: Rupee breaks six-day winning streak on state banks' dollar bids — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/forex/indian-rupee-breaks-six-day-winning-streak-on-state-banks-dollar-bids/article71682202.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 5.63] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2110.96, z20 -2.31, zc -0.23, resid-z 0.51 [quiet], 1d -0.92%, |z20|=2.31
- btc_usd [CRYPTO]: last 74416.60, z20 -1.82, zc -0.41, resid-z 0.02 [quiet], 1d -0.98%, |z20|=1.82
- dyn_coin [EQUITIES]: last 136.07, z20 -1.71, zc -0.30, resid-z 0.35 [quiet], 1d 0.97%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.758 vs eth_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.741 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.732 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.505 vs eth_usd, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.657 vs eth_usd
- Source: Global Market Today: Asian stocks rally after US tech surge, oil slump — ET Markets, 2026-11-10. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-rally-after-us-tech-surge-oil-slump/articleshow/135696042.cms
- Source: Global LNG Markets Face a Winter of Extreme Uncertainty — OilPrice, 2026-11-09. https://oilprice.com/Energy/Energy-General/Global-LNG-Markets-Face-a-Winter-of-Extreme-Uncertainty.html
- Source: Indian IT stocks strengthen buoyed by weakness in the global AI trade and attractive valuations — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/indian-it-stocks-strengthen-buoyed-by-weakness-in-the-global-ai-trade-and-attractive-valuations/article71683017.ece
- Historical analogues: 2026-05-22 (d=0.16), 2025-04-10 (d=0.46), 2025-10-16 (d=0.6)

### [RED 5.18] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 165.90, z20 3.18, zc 0.14, resid-z 0.20 [quiet], 1d 4.73%, |z20|=3.18; 1y-pct=99
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.646 vs dyn_tgt, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.506 vs dyn_tgt
- Source: Top 3 stocks to buy this week: Union Bank, Ather Energy, Laurus Labs by market expert; check stop-loss, target price — Mint Markets, 2026-11-09. https://www.livemint.com/market/stock-market-news/top-3-stocks-to-buy-this-week-union-bank-ather-energy-laurus-labs-by-market-expert-check-stop-loss-target-price-11794224157187.html
- Source: Top PSU stock to buy: Brokerage sees 50% upside! Gujarat Energy shares gain 2% as profit surges 26% - Check target price — Mint Markets, 2026-11-09. https://www.livemint.com/market/stock-market-news/top-psu-stock-to-buy-brokerage-sees-50-upside-gujarat-energy-shares-gain-2-as-profit-surges-26-check-target-price-11794218975640.html
- Source: GOLDMAN SACHS DEFENDS NVIDIA WITH $300 PRICE TARGET Goldman Sachs reiterates its Buy rating on Nvidia ($NVDA ) with a $300 price target, calling the stock's risk/reward attractive following the recent AI-sector selloff. Analyst James Schneider expects Nvidia's near-term fundamentals to exceed Wall S — DeItaone, 2026-11-09. https://t.me/walter_bloomberg/38215
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [AMBER 5.03] commodities · 2 series ↓
- wti [COMMODITIES]: last 85.97, z20 -2.20, zc 0.02, resid-z 0.27 [quiet], 1d 0.07%, |z20|=2.20
- brent [COMMODITIES]: last 91.73, z20 -2.18, zc 0.00, resid-z 0.08 [quiet], 1d 0.00%, |z20|=2.18; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.495 via wti, z 2.64, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.556 vs brent, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.624 vs brent
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.555 vs brent
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.551 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.509 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.495, z 2.64)
- Source: Oil falls as Trump downplays prospect of escalation with Iran — ET Markets, 2026-11-10. https://economictimes.indiatimes.com/markets/commodities/news/oil-falls-as-trump-downplays-prospect-of-escalation-with-iran/articleshow/135696497.cms
- Source: Global Market Today: Asian stocks rally after US tech surge, oil slump — ET Markets, 2026-11-10. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-rally-after-us-tech-surge-oil-slump/articleshow/135696042.cms
- Source: Scientists Develop Cheap Filter That Could Slash Oil Refining Energy Use by 32% — OilPrice, 2026-11-09. https://oilprice.com/Energy/Energy-General/Scientists-Develop-Cheap-Filter-That-Could-Slash-Oil-Refining-Energy-Use-by-32.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 4.92] equities · 2 series ↑
- dyn_indianb_ns [EQUITIES]: last 933.70, z20 4.09, zc 0.51, resid-z -0.16 [quiet], 1d 3.51%, |z20|=4.09
- dyn_karurvysya_ns [EQUITIES]: last 370.00, z20 2.01, zc 1.01, resid-z 0.92 [quiet], 1d -0.01%, |z20|=2.01; 1y-pct=99
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.607 via dyn_indianb_ns, z 2.09, reacted); dyn_jiofin_bo (rho 0.578 via dyn_indianb_ns, z 2.18, reacted); dyn_bajfinance_ns (rho 0.519 via dyn_indianb_ns, z 2.28, reacted); nifty_50 (rho 0.496 via dyn_indianb_ns, z 2.81, reacted); dyn_muthootfin_ns (rho 0.491 via dyn_indianb_ns, z 2.64, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.607, z 2.09); dyn_jiofin_bo (rho 0.578, z 2.18); dyn_bajfinance_ns (rho 0.519, z 2.28); nifty_50 (rho 0.496, z 2.81)
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-04 (d=0.46), 2025-02-01 (d=0.51)

### [RED 4.84] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 178.60, z20 -2.84, zc 0.60, resid-z 0.97 [quiet], 1d -4.31%, |z20|=2.84
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.699 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.662 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.653 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.648 vs dyn_nvda, historically leads by 4d
- Source: The short seller who saw signs of Nvidia’s China scandal months ago claims Megaspeed isn’t the only company helping China access chips — MarketWatch Top, 2026-11-10. https://www.marketwatch.com/story/the-short-seller-who-saw-signs-of-nvidias-china-scandal-months-ago-claims-megaspeed-isnt-the-ony-company-helping-china-access-chips-9877f544?mod=mw_rss_topstories
- Source: TRUMP SAYS ' WAS AMAZED' ABOUT NVIDIA CEO'S ALLEGATIONS — DeItaone, 2026-11-09. https://t.me/walter_bloomberg/38280
- Source: As Nvidia’s stock falls, here’s what Wall Street has to say about the Jensen Huang scandal — MarketWatch Top, 2026-11-09. https://www.marketwatch.com/story/how-wall-street-is-reacting-to-the-news-of-nvidias-jensen-huang-investigation-into-spy-claims-d8c839ab?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

### [AMBER 4.7] rates · 2 series ↓
- ust_2y [RATES]: last 4.51, z20 -1.87, zc 0.86, resid-z -0.77 [quiet], 1d 1.12%, |z20|=1.87
- ust_10y [RATES]: last 4.86, z20 -1.64, zc 0.38, resid-z -1.13 [quiet], 1d 0.41%, |z20|=1.64
- **Mechanism**: rates · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.831 vs ust_2y
- Watch next: dyn_schd (inverse) — not yet - watch; rho -0.593 vs ust_10y, historically leads by 2d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.029 vs ust_2y, historically leads by 1d
- Source: FPI investments in FAR G-Secs rise nearly ₹8,000 cr as rupee gains, bond yields ease — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/fpi-investments-in-far-g-secs-rise-nearly-8000-cr-as-rupee-gains-bond-yields-ease/article71682301.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.18), 2025-05-15 (d=0.36)

## Watchlist (below surfacing floor)
eur_inr ↓ (4.47), dyn_tech ↑ (4.38), dyn_ohi ↑ (4.08), indices · 3 series ↑ (3.98), dyn_atherenerg_ns ↑ (3.74), vix ↑ (3.34), asx_200 ↑ (3.31), dyn_4417_t ↑ (3.12), dyn_hdb ↑ (2.94), dyn_schd ↑ (2.89), cross-asset · 2 series ↑ (2.84), dyn_havells_ns ↑ (2.52)

## India macro
- nifty_50: 25044.6504 (1d 0.06%, z20 2.81, flag red)
- nifty_midcap_100: 61018.6484 (1d 0.66%, z20 2.09, flag amber)
- usd_inr: 93.9030 (1d -0.59%, z20 -2.11, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4364 (1d 0.60%, z20 -1.50, flag none)
- Next India prints: NSDL FPI flows T-0d · India CPI T-2d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 69.7 — "Stock recommendations for 11 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 69.4 — "Stock recommendations for 11 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 69.1 — "Stock recommendations for 11 November from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 47.8 — "RBI said to query bank valuations of some bond derivative trades"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.2 — "Global Market Today: Asian stocks rally after US tech surge, oil slump"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.4 — "Global Market Today: Asian stocks rally after US tech surge, oil slump"
- TECH (Bio-Techne Corp) score 38.4 — "Global Market Today: Asian stocks rally after US tech surge, oil slump"
- 301077.SZ (CHINASTARS) score 34.5 — "JEFFRIES: THERE ARE REAL CONCERNS THAT NEED TO BE ADDRESSED WITH RESPECT TO THE NVIDIA SIT"
- BAC (Bank of America Corporation) score 32.8 — "RBI said to query bank valuations of some bond derivative trades"
- TGT (Target Corporation) score 30.6 — "NVDA - NVIDIA BOARD LAUNCHES ESPIONAGE PROBE INVOLVING CEO JENSEN HUANG Nvidia IS launchin"
- HDB (HDFC Bank Limited) score 29.8 — "RBI said to query bank valuations of some bond derivative trades"
- COIN (Coinbase Global, Inc.) score 28.5 — "Global Market Today: Asian stocks rally after US tech surge, oil slump"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.1 — "RBI said to query bank valuations of some bond derivative trades"
- IDBI.NS (IDBI BANK LIMITED) score 28.0 — "RBI said to query bank valuations of some bond derivative trades"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.0 — "RBI said to query bank valuations of some bond derivative trades"
- OHI (Omega Healthcare Investors, In) score 26.9 — "Upcoming IPO: Veritas Finance gets Sebi nod to launch public issue – Top things for invest"
- NVDA (NVIDIA Corporation) score 24.5 — "NVDA - JEFFRIES: CLEARLY CONGRESS NEEDS MORE INFORMATION ABOUT NVIDIA SITUATION"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.8 — "TRUMP TELLS REUTERS AFTER TALKS WITH QATARI LEADER THAT QATAR WOULD RATHER SEE A PEACEFUL "
- CHKP (Check Point Software Technolog) score 20.2 — "Crude Check: Bears make their move"
- BOND (PIMCO Active Bond Exchange-Tra) score 19.3 — "RBI said to query bank valuations of some bond derivative trades"
- LTH (Life Time Group Holdings, Inc.) score 14.7 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.6 — "Upcoming IPO: Veritas Finance gets Sebi nod to launch public issue – Top things for invest"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.4 — "Pearl Global shares hit 52-week high ahead of dividend record date; will the rally continu"
- JIOFIN.BO (Jio Financial Services Limited) score 11.5 — "NVDA - NVIDIA DOWNGRADED TO HOLD AS $165 BILLION AI FINANCING EXPOSURE RAISES CONCERNS Ale"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.7 — "Upcoming IPO: Veritas Finance gets Sebi nod to launch public issue – Top things for invest"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.6 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.6 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 10.1 — "Four stocks with high dividend payout ratios to watch"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.7 — "US OCTOBER CPI REPORT TO OMIT ANNUAL INFLATION FIGURES The Bureau of Labor Statistics will"
- META (Meta) score 9.3 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.5 — "Stocks in focus: SBI, L&T, Alkem Lab, Adani Enterprises, BEL, GRSE, BHEL, Waaree Renewable"
- RS (Reliance, Inc.) score 7.3 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- DEMZ (Democratic Large Cap Core ETF) score 6.4 — "Democratic Win Set to Reshuffle U.S. Energy Policy"
- JEF (Jefferies Financial Group Inc.) score 4.2 — "HSBC upgrades India to Overweight, cuts China to Neutral; Citi, Jefferies also favour Indi"
- SEPN (Septerna, Inc.) score 4.0 — "DEMOCRATS SWEEP CONGRESS. FED HIKE BETS RETREAT. Following the midterm results, December F"
- GS (Goldman Sachs Group, Inc. (The) score 3.7 — "GOLDMAN SACHS DEFENDS NVIDIA WITH $300 PRICE TARGET Goldman Sachs reiterates its Buy ratin"
- JUSTDIAL.BO (JUST DIAL LTD.) score 3.7 — "₹13 to  ₹82: This multibagger small-cap stock turns  ₹1 lakh into 6.5 lakh in just 10 mont"
- VT (Vanguard Total World Stock Ind) score 3.6 — "JENSEN HUANG IS SCHEDULED TO ATTEND SEMAFOR’S SILICON VALLEY & THE WORLD, SOURCE SAYS"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.4 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.2 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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