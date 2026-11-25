# Transmission Layer — board brief · 2026-11-25 04:23Z

data as of **2026-11-25** · 97 series · 6 red / 42 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.766, 8d in regime; vol-pct 0.783, breadth-off 0.75, Markov P(high-vol) 0.588)
- [WEAK] **safe_haven_gold** — corr20 -0.15, corr60 -0.26, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.12, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.0, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.19, corr60 -0.01, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.3, corr60 0.35, last shift 2026-10-07. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **10 of 89** scanned series survive multiplicity control (effective p ≤ 0.009880031515541177)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.483, β 0.2082, p 0.0); driver zc -2.02 → expected -0.569%. Type hit-rate 0.819 (n=2154).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.458, β 0.2397, p 0.0); driver zc -2.21 → expected -0.571%. Type hit-rate 0.819 (n=2154).
- Track record · residual_reversion: hit-rate **0.507** (n=1153) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2154) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.64] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 87.41, z20 2.32, zc n/a, resid-z n/a [quiet], 1d -0.08%, GSR>85 (extreme high); |z20|=2.32; 1y-pct=99
- comex_silver [COMMODITIES]: last 40.60, z20 -2.09, zc 0.03, resid-z -1.30 [quiet], 1d 0.14%, |z20|=2.09; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3548.40, z20 -1.95, zc 0.02, resid-z -3.12 [unexplained], 1d 0.05%, |z20|=1.95; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.586 via comex_gold, z -0.52, quiet); dyn_karurvysya_ns (rho 0.493 via comex_gold, z 0.7, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.571 vs comex_silver, historically leads by 4d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.521 vs gold_silver_ratio, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.586, z -0.52); dyn_karurvysya_ns (rho 0.493, z 0.7)
- Source: Gold rate today under pressure after dead-cat bounce from 14-month low;  ₹1 lakh or  ₹1.5 lakh? 3 dates to remember — Mint Markets, 2026-11-25. https://www.livemint.com/market/commodities/gold-rate-today-under-pressure-after-dead-cat-bounce-from-14-month-low-rs-1-lakh-or-rs-1-5-lakh-3-dates-to-remember-11795577248684.html
- Source: Gold Silver Rates Live Updates: Gold falls over 2% as rate hike bets rise; silver edges lower — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/stocks/live-blog/live-updates-gold-rate-today-25th-november-24k-22k-20k-18-carat-mcx-gold-silver-price-in-delhi-hyderabad-chennai-bengaluru-citywise/liveblog/136146334.cms
- Source: Gold ticks lower ahead of US inflation data — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/commodities/news/gold-ticks-lower-ahead-of-us-inflation-data/articleshow/136145643.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.18] usd_inr ↓
- usd_inr [FX]: last 92.55, z20 -2.18, zc -0.95, resid-z 0.62 [quiet], 1d -0.39%, 20d range extreme; |z20|=2.18
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.444 via usd_inr, z 0.68, quiet); dyn_havells_ns (rho -0.424 via usd_inr, z 1.1, reacted); nifty_it (rho -0.422 via usd_inr, z 0.53, quiet); dyn_tataelxsi_ns (rho -0.374 via usd_inr, z 1.04, reacted); dyn_inoxindia_ns (rho -0.362 via usd_inr, z 1.86, reacted)
- **India receivers**: dyn_indianb_ns (rho -0.444, z 0.68); dyn_havells_ns (rho -0.424, z 1.1); nifty_it (rho -0.422, z 0.53); dyn_tataelxsi_ns (rho -0.374, z 1.04)
- Source: Rupee to resume rally on positive flow backdrop, turn in market sentiment — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/forex/rupee-to-resume-rally-on-positive-flow-backdrop-turn-in-market-sentiment/article71740950.ece
- Source: India’s rupee has become an accidental carry star — ET Markets, 2026-11-24. https://economictimes.indiatimes.com/markets/stocks/news/indias-rupee-has-become-an-accidental-carry-star/articleshow/136117132.cms
- Source: Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/banks-sell-off-ends-four-week-rally-nifty-slumps-175-rupee-weakens/article71734774.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.28] cross-asset · 5 series ↓
- dyn_ms [EQUITIES]: last 168.80, z20 -2.35, zc -0.81, resid-z 0.74 [quiet], 1d -2.20%, |z20|=2.35
- dyn_gs [EQUITIES]: last 806.15, z20 -2.34, zc -0.75, resid-z -0.65 [quiet], 1d -2.12%, |z20|=2.34
- dax [INDICES]: last 25008.07, z20 -2.02, zc -0.87, resid-z -1.36 [quiet], 1d -1.30%, |z20|=2.02
- stoxx_50 [INDICES]: last 6003.93, z20 -1.84, zc -0.81, resid-z -0.92 [quiet], 1d -1.16%, |z20|=1.84
- ftse_100 [INDICES]: last 10467.51, z20 -1.63, zc -0.13, resid-z -0.17 [quiet], 1d -0.13%, |z20|=1.63
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-01 (z-distance 0.89).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.486 via dax, z -0.52, quiet); dyn_kaynes_ns (rho 0.424 via ftse_100, z -2.1, reacted); dyn_tataelxsi_ns (rho 0.355 via ftse_100, z 1.04, reacted)
- Watch next: vix (inverse) — not yet - watch; rho -0.765 vs dyn_gs, historically leads by 5d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.907 vs dax
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.644 vs dyn_gs, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.486, z -0.52); dyn_kaynes_ns (rho 0.424, z -2.1); dyn_tataelxsi_ns (rho 0.355, z 1.04)
- Source: Goldman Sachs, SocGen buy Rs 920 crore stake in Lenskart — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/stocks/news/goldman-sachs-socgen-buy-rs-920-crore-stake-in-lenskart/articleshow/136145273.cms
- Source: SPY $QQQ - GOLDMAN SAYS MARKET POSITIONING SIGNALS ABOVE-AVERAGE S&P 500 RETURNS Goldman Sachs says its sentiment and positioning indicator has fallen to the 36th percentile, its lowest since Liberation Day, historically a favorable level for future equity returns. Strategist Christian Mueller-Gliss — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39115
- Source: Rupee retreats, Goldman calls it a 'port of stability' in AI storm — ET Markets, 2026-11-23. https://economictimes.indiatimes.com/markets/forex/rupee-retreats-goldman-calls-it-a-port-of-stability-in-ai-storm/articleshow/136092977.cms
- Historical analogues: 2026-04-01 (d=0.89), 2025-10-31 (d=1.63), 2025-10-24 (d=1.77)

### [AMBER 5.06] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 102.38, z20 -1.74, zc -1.25, resid-z 1.63 [unexplained], 1d -5.88%, 1y-pct=0
- btc_usd [CRYPTO]: last 59166.44, z20 -1.45, zc -0.85, resid-z -0.12 [quiet], 1d -2.15%, 1y-pct=1
- eth_usd [CRYPTO]: last 1660.71, z20 -1.31, zc -0.55, resid-z -0.23 [quiet], 1d -2.09%, 1y-pct=4
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.22).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.502 vs dyn_coin, historically leads by 2d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.595 vs btc_usd
- Source: Sensex today | Stock Market Live: Sensex jumps 1,500 pts in early trade, Nifty crosses 25,750 defying global weakness — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-25-november-2026/article71734420.ece
- Source: Global Market Today: Asian stocks fall as AI trade doubts resurface — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-fall-as-ai-trade-doubts-resurface/articleshow/136145030.cms
- Source: Bitcoin Surrenders Most Gains Amid Sustained ETF Outflows — Mint Markets, 2026-11-24. https://www.livemint.com/market/bitcoin-surrenders-most-gains-amid-sustained-etf-outflows-11795554238437.html
- Historical analogues: 2025-10-22 (d=0.22), 2025-10-30 (d=0.3), 2025-03-31 (d=0.36)

### [AMBER 4.96] rates · 2 series ↑
- ig_oas [RATES]: last 0.97, z20 2.13, zc 2.78, resid-z 0.71 [priced], 1d -1.02%, |z20|=2.13; 1y-pct=99
- hy_oas [RATES]: last 3.63, z20 1.94, zc 3.00, resid-z 0.45 [priced], 1d -3.46%, |z20|=1.94; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.481 via ig_oas, z -1.74, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.585 vs hy_oas, historically leads by 5d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.515 vs hy_oas, historically leads by 2d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.507 vs hy_oas, historically leads by 3d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.546 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.481, z -1.74)
- Source: Dividend vs fixed deposits: 5 high yield stocks generating better income than FDs - CyberTech, Majestic Auto, to Premco — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/dividend-vs-fixed-deposits-5-high-yield-stocks-generating-better-income-than-fds-cybertech-majestic-auto-to-premco-11795463444218.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [RED 4.84] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 176.01, z20 2.84, zc 2.29, resid-z -2.28 [unexplained], 1d 4.65%, |z20|=2.84; 1y-pct=100
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.537 vs dyn_tgt, historically leads by 3d
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.519 vs dyn_tgt, historically leads by 4d
- Source: MSFT - MICROSOFT HAS DECLARED "CODE RED" FOR M365 CORE SERVICE HEALTH AFTER NOV 12 OUTAGE -INTERNAL MEMOS SHOW MICROSOFT SETS TARGET FOR WORLDWIDE MITIGATION IN UNDER AN HOUR FOR FUTURE INCIDENTS -MEMO — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39133
- Source: ANT - WEDBUSH INITIATES ANTHROPIC AT OUTPERFORM, SEES 37% UPSIDE Wedbush Securities initiated coverage of Anthropic with an Outperform rating and $120 price target, implying approximately 37% upside from Monday's close. Analyst Ygal Arounian sees Anthropic as a major beneficiary of the expanding AI  — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39106
- Source: TSLA - SEAPORT INITIATES TESLA AT BUY, $475 TARGET Seaport Global Securities initiated Tesla at Buy with a $475 price target, citing accelerating Robotaxi deployment. The firm forecasts $3–4 billion in Robotaxi annual recurring revenue by the end of 2027 and sees a multi-trillion-dollar market oppor — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39105
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [AMBER 4.56] indices · 2 series ↓
- nikkei_225 [INDICES]: last 57006.68, z20 -1.72, zc -1.07, resid-z -2.00 [unexplained], 1d -2.79%, |z20|=1.72
- kospi [INDICES]: last 4720.36, z20 -1.64, zc -1.39, resid-z 2.82 [unexplained], 1d -5.71%, |z20|=1.64
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.429 via nikkei_225, z 0.94, quiet); nifty_metal (rho 0.353 via nikkei_225, z -1.62, reacted)
- Watch next: dyn_2545_tw (co-move) — not yet - watch; rho 0.572 vs kospi, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.429, z 0.94); nifty_metal (rho 0.353, z -1.62)
- Source: Stock market outlook today,25 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-25. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-25-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11795566965791.html
- Source: Asian markets follow Wall Street: Nikkei, Kospi jump up to 8% as Jensen Huang’s return sparks rally in AI stocks — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/asian-markets-follow-wall-street-nikkei-kospi-jump-up-to-8-as-jensen-huang-s-return-sparks-rally-in-ai-stocks-11795485047635.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-07-02 (d=0.5), 2025-04-21 (d=1.1)

### [AMBER 4.49] natgas ↑
- natgas [COMMODITIES]: last 3.69, z20 2.49, zc 0.01, resid-z 4.96 [unexplained], 1d 0.05%, |z20|=2.49
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Iran Faces a Deepening Natural Gas Crisis Ahead of Winter — OilPrice, 2026-11-24. https://oilprice.com/Energy/Energy-General/Iran-Faces-a-Deepening-Natural-Gas-Crisis-Ahead-of-Winter.html
- Source: PNGRB proposes 14% assured returns to attract investment in natural gas pipelines — BusinessLine Mkts, 2026-11-24. https://www.thehindubusinessline.com/markets/commodities/pngrb-proposes-14-assured-returns-to-attract-investment-in-natural-gas-pipelines/article71738560.ece
- Source: Japan Poised to Ramp Up LNG Buying as Power Prices Surge — OilPrice, 2026-11-24. https://oilprice.com/Latest-Energy-News/World-News/Japan-Poised-to-Ramp-Up-LNG-Buying-as-Power-Prices-Surge.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
comex_copper ↓ (3.84), usd_mxn ↑ (3.67), dyn_301077_sz ↓ (3.55), dyn_crwv ↓ (3.44), dyn_tech ↑ (3.4), dyn_lth ↑ (3.25), dyn_atherenerg_ns ↑ (3.08), dyn_nvda ↓ (2.92), dyn_2545_tw ↓ (2.71), dyn_4417_t ↑ (2.51), cross-asset · 2 series ↓ (2.45), dyn_techm_ns ↑ (2.35)

## India macro
- nifty_50: 25770.1504 (1d 1.66%, z20 1.26, flag none)
- nifty_midcap_100: 61754.3516 (1d 0.57%, z20 0.94, flag none)
- usd_inr: 92.5500 (1d -0.39%, z20 -2.18, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.3964 (1d -1.07%, z20 -1.74, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- NVDA (NVIDIA Corporation) score 67.7 — "US ATTORNEY GENERAL BLANCHE: NVIDIA IS A GOOD CORPORATE CITIZEN"
- COALINDIA.NS (COAL INDIA LTD) score 62.9 — "Indian shares may open higher as foreign inflows, lower oil prices aid sentiment"
- INOXINDIA.NS (INOX INDIA LIMITED) score 57.7 — "Indian shares may open higher as foreign inflows, lower oil prices aid sentiment"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 57.4 — "Indian shares may open higher as foreign inflows, lower oil prices aid sentiment"
- INDIANB.NS (INDIAN BANK) score 44.0 — "Indian shares may open higher as foreign inflows, lower oil prices aid sentiment"
- OHI (Omega Healthcare Investors, In) score 36.1 — "Big boom in stock market today;  ₹2.2 lakh cr wealth for investors! Sensex up 1,400 points"
- BAC (Bank of America Corporation) score 34.7 — "Markets snap two-day losing streak with sharp gap-up; Banks, IT lead recovery"
- TGT (Target Corporation) score 34.0 — "Aeravti Ventures launches Fund 2; targets corpus of ₹300 crore"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.4 — "Mahanadi Coalfields IPO allotment to be out today; How to check status on KFin Tech, BSE, "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.9 — "Mahanadi Coalfields IPO allotment to be out today; How to check status on KFin Tech, BSE, "
- TECH (Bio-Techne Corp) score 30.9 — "Mahanadi Coalfields IPO allotment to be out today; How to check status on KFin Tech, BSE, "
- HDB (HDFC Bank Limited) score 29.8 — "Markets snap two-day losing streak with sharp gap-up; Banks, IT lead recovery"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.6 — "Markets snap two-day losing streak with sharp gap-up; Banks, IT lead recovery"
- IDBI.NS (IDBI BANK LIMITED) score 28.6 — "Markets snap two-day losing streak with sharp gap-up; Banks, IT lead recovery"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.6 — "Markets snap two-day losing streak with sharp gap-up; Banks, IT lead recovery"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 25.9 — "NVDA - NVIDIA'S HUANG TO HOLD ALL-HANDS MEETING AT 12:30 P.M. PT TODAY"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.3 — "Dollar takes breather ahead of US data on Fed path; Aussie jumps on CPI"
- BLLN (BillionToOne, Inc.) score 23.2 — "CITADEL SECURITIES SMASHES ANNUAL REVENUE RECORD IN JUST NINE MONTHS Citadel Securities ge"
- LTH (Life Time Group Holdings, Inc.) score 21.3 — "CIA AND U.S. INTELLIGENCE CHIEF'S OFFICE HIT BY CYBERSECURITY BREACH — NYT The CIA and Off"
- 301077.SZ (CHINASTARS) score 20.9 — "DEMOCRATIC SENATE LEADER SCHUMER ACCUSES NVIDIA CEO HUANG OF SHIPPING "EXTREMELY ADVANCED "
- CHKP (Check Point Software Technolog) score 19.2 — "Mahanadi Coalfields IPO allotment to be out today; How to check status on KFin Tech, BSE, "
- COIN (Coinbase Global, Inc.) score 18.4 — "Global Market Today: Asian stocks fall as AI trade doubts resurface"
- BOND (PIMCO Active Bond Exchange-Tra) score 12.3 — "India pension funds pivot to bonds as equity exposure nears cap"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.2 — "ANT - ANTHROPIC SHARES EXTEND LOSSES; LAST DOWN 12.7%"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.0 — "Beware! Fraudsters impersonating as Sebi-registered intermediaries: How can investors avoi"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.2 — "Top stocks to watch today: Tata Steel, Lenskart, Adani Enterprises, PhysicsWallah, Hindalc"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.2 — "Top stocks to watch today: Tata Steel, Lenskart, Adani Enterprises, PhysicsWallah, Hindalc"
- JIOFIN.BO (Jio Financial Services Limited) score 10.0 — "Canada’s Oilfield Services Sector Is Gearing Up for a Stronger 2027"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.4 — "CITADEL SECURITIES SMASHES ANNUAL REVENUE RECORD IN JUST NINE MONTHS Citadel Securities ge"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.8 — "Climate Finance Dispute Derails COP31 Negotiations"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.3 — "Climate Finance Dispute Derails COP31 Negotiations"
- META (Meta) score 6.0 — "The Energy Transition Needs More Metals but Less Extraction"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "Top stocks to watch today: Tata Steel, Lenskart, Adani Enterprises, PhysicsWallah, Hindalc"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "Goldman Sachs, SocGen buy Rs 920 crore stake in Lenskart"
- CRWV (CoreWeave, Inc.) score 3.1 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- MS (Morgan Stanley) score 2.9 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- MU (Micron Technology, Inc.) score 2.7 — "Micron’s stock falls as an analyst warns about a future supply glut"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.4 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- ETERNAL.NS (ETERNAL LIMITED) score 1.0 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.9 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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