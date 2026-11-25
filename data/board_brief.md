# Transmission Layer — board brief · 2026-11-25 00:39Z

data as of **2026-11-25** · 97 series · 6 red / 40 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 1.0, 8d in regime; vol-pct None, breadth-off 1.0, Markov P(high-vol) 0.588)
- [WEAK] **safe_haven_gold** — corr20 -0.15, corr60 -0.26, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.21, corr60 0.05, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.19, corr60 -0.01, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.31, corr60 0.35, last shift 2026-10-07. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **10 of 89** scanned series survive multiplicity control (effective p ≤ 0.009880031515541177)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.483, β 0.2082, p 0.0); driver zc -2.02 → expected -0.569%. Type hit-rate 0.819 (n=2126).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.458, β 0.2397, p 0.0); driver zc -2.21 → expected -0.571%. Type hit-rate 0.819 (n=2126).
- Track record · residual_reversion: hit-rate **0.506** (n=1152) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2126) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.6] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 87.23, z20 2.29, zc n/a, resid-z n/a [quiet], 1d 0.03%, GSR>85 (extreme high); |z20|=2.29; 1y-pct=100
- comex_silver [COMMODITIES]: last 40.58, z20 -2.09, zc -0.00, resid-z -0.96 [quiet], 1d -0.01%, |z20|=2.09; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3539.60, z20 -1.99, zc 0.01, resid-z -3.12 [unexplained], 1d 0.02%, |z20|=1.99; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.583 via comex_gold, z -0.51, quiet); dyn_karurvysya_ns (rho 0.491 via comex_gold, z 1.03, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.572 vs comex_silver, historically leads by 4d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.519 vs gold_silver_ratio, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.583, z -0.51); dyn_karurvysya_ns (rho 0.491, z 1.03)
- Source: Gold Slips as Investors Weigh Fed Outlook, US Tariff Plans — Mint Markets, 2026-11-24. https://www.livemint.com/market/gold-slips-as-investors-weigh-fed-outlook-us-tariff-plans-11795564730725.html
- Source: Explained: Why Gold prices gained and extended a rebound from a 14-month low - 3 reasons — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/explained-why-gold-prices-gained-and-extended-a-rebound-from-a-14-month-low-3-reasons-11795514651749.html
- Source: How will the AI boom impact gold prices? 4 key factors investors should watch, explains World Gold Council strategist — Mint Markets, 2026-11-24. https://www.livemint.com/market/how-will-the-ai-boom-impact-gold-prices-4-key-factors-investors-should-watch-explains-world-gold-council-strategist-11795519705028.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 6.28] cross-asset · 5 series ↓
- dyn_ms [EQUITIES]: last 168.80, z20 -2.35, zc -0.81, resid-z 0.74 [quiet], 1d -2.20%, |z20|=2.35
- dyn_gs [EQUITIES]: last 806.15, z20 -2.34, zc -0.75, resid-z -0.65 [quiet], 1d -2.12%, |z20|=2.34
- dax [INDICES]: last 25008.07, z20 -2.02, zc -0.87, resid-z -1.24 [quiet], 1d -1.30%, |z20|=2.02
- stoxx_50 [INDICES]: last 6003.93, z20 -1.84, zc -0.81, resid-z -0.74 [quiet], 1d -1.16%, |z20|=1.84
- ftse_100 [INDICES]: last 10467.51, z20 -1.63, zc -0.13, resid-z -0.18 [quiet], 1d -0.13%, |z20|=1.63
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-01 (z-distance 0.89).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.486 via dax, z -0.51, quiet); dyn_kaynes_ns (rho 0.424 via ftse_100, z -2.03, reacted); dyn_tataelxsi_ns (rho 0.355 via ftse_100, z 0.54, quiet)
- Watch next: vix (inverse) — not yet - watch; rho -0.765 vs dyn_gs, historically leads by 5d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.907 vs dax
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.644 vs dyn_gs, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.486, z -0.51); dyn_kaynes_ns (rho 0.424, z -2.03); dyn_tataelxsi_ns (rho 0.355, z 0.54)
- Source: SPY $QQQ - GOLDMAN SAYS MARKET POSITIONING SIGNALS ABOVE-AVERAGE S&P 500 RETURNS Goldman Sachs says its sentiment and positioning indicator has fallen to the 36th percentile, its lowest since Liberation Day, historically a favorable level for future equity returns. Strategist Christian Mueller-Gliss — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39115
- Source: Rupee retreats, Goldman calls it a 'port of stability' in AI storm — ET Markets, 2026-11-23. https://economictimes.indiatimes.com/markets/forex/rupee-retreats-goldman-calls-it-a-port-of-stability-in-ai-storm/articleshow/136092977.cms
- Historical analogues: 2026-04-01 (d=0.89), 2025-10-31 (d=1.63), 2025-10-24 (d=1.77)

### [AMBER 5.06] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 102.38, z20 -1.74, zc -1.25, resid-z 1.63 [unexplained], 1d -5.88%, 1y-pct=0
- btc_usd [CRYPTO]: last 59449.77, z20 -1.41, zc -0.67, resid-z -0.30 [quiet], 1d -1.68%, 1y-pct=1
- eth_usd [CRYPTO]: last 1667.75, z20 -1.28, zc -0.44, resid-z -0.43 [quiet], 1d -1.67%, 1y-pct=5
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.22).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.502 vs dyn_coin, historically leads by 2d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.596 vs btc_usd
- Source: Bitcoin Surrenders Most Gains Amid Sustained ETF Outflows — Mint Markets, 2026-11-24. https://www.livemint.com/market/bitcoin-surrenders-most-gains-amid-sustained-etf-outflows-11795554238437.html
- Source: BITCOIN FALLS BELOW $60,000 — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39113
- Source: TSLA - SEAPORT INITIATES TESLA AT BUY, $475 TARGET Seaport Global Securities initiated Tesla at Buy with a $475 price target, citing accelerating Robotaxi deployment. The firm forecasts $3–4 billion in Robotaxi annual recurring revenue by the end of 2027 and sees a multi-trillion-dollar market oppor — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39105
- Historical analogues: 2025-10-22 (d=0.22), 2025-10-30 (d=0.27), 2025-03-31 (d=0.35)

### [AMBER 4.96] rates · 2 series ↑
- ig_oas [RATES]: last 0.97, z20 2.13, zc 2.78, resid-z 0.71 [priced], 1d -1.02%, |z20|=2.13; 1y-pct=99
- hy_oas [RATES]: last 3.63, z20 1.94, zc 3.00, resid-z 0.45 [priced], 1d -3.46%, |z20|=1.94; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.481 via ig_oas, z -1.13, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.585 vs hy_oas, historically leads by 5d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.515 vs hy_oas, historically leads by 2d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.507 vs hy_oas, historically leads by 3d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.546 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.481, z -1.13)
- Source: Dividend vs fixed deposits: 5 high yield stocks generating better income than FDs - CyberTech, Majestic Auto, to Premco — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/dividend-vs-fixed-deposits-5-high-yield-stocks-generating-better-income-than-fds-cybertech-majestic-auto-to-premco-11795463444218.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [RED 4.84] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 176.01, z20 2.84, zc 2.29, resid-z -2.28 [unexplained], 1d 4.65%, |z20|=2.84; 1y-pct=100
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.537 vs dyn_tgt, historically leads by 3d
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.519 vs dyn_tgt, historically leads by 4d
- Source: ANT - WEDBUSH INITIATES ANTHROPIC AT OUTPERFORM, SEES 37% UPSIDE Wedbush Securities initiated coverage of Anthropic with an Outperform rating and $120 price target, implying approximately 37% upside from Monday's close. Analyst Ygal Arounian sees Anthropic as a major beneficiary of the expanding AI  — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39106
- Source: TSLA - SEAPORT INITIATES TESLA AT BUY, $475 TARGET Seaport Global Securities initiated Tesla at Buy with a $475 price target, citing accelerating Robotaxi deployment. The firm forecasts $3–4 billion in Robotaxi annual recurring revenue by the end of 2027 and sees a multi-trillion-dollar market oppor — DeItaone, 2026-11-24. https://t.me/walter_bloomberg/39105
- Source: Poonawalla Fincorp share price: After 25% jump in 1 month, JM Financial sees 21% further upside, raises target — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/poonawalla-fincorp-share-price-after-25-jump-in-1-month-jm-financial-sees-21-further-upside-raises-target-11795515723611.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 4.5] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 382.00, z20 -2.50, zc -0.29, resid-z -0.11 [quiet], 1d -2.05%, |z20|=2.50
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India unit Mahanadi's IPO fully subscribed on final day, led by institutional investors — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/coal-india-unit-mahanadis-ipo-fully-subscribed-on-final-day-led-by-institutional-investors/article71734460.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

### [AMBER 4.45] indices · 2 series ↓
- nikkei_225 [INDICES]: last 57225.00, z20 -1.62, zc -0.89, resid-z -2.00 [unexplained], 1d -2.31%, |z20|=1.62
- kospi [INDICES]: last 4757.78, z20 -1.55, zc -1.30, resid-z 3.13 [unexplained], 1d -5.58%, |z20|=1.55
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.43 via nikkei_225, z 0.83, quiet); nifty_metal (rho 0.354 via nikkei_225, z -1.13, reacted)
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.816 vs nikkei_225, historically leads by 2d
- Watch next: dyn_2545_tw (co-move) — not yet - watch; rho 0.548 vs kospi, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.43, z 0.83); nifty_metal (rho 0.354, z -1.13)
- Source: Asian markets follow Wall Street: Nikkei, Kospi jump up to 8% as Jensen Huang’s return sparks rally in AI stocks — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/asian-markets-follow-wall-street-nikkei-kospi-jump-up-to-8-as-jensen-huang-s-return-sparks-rally-in-ai-stocks-11795485047635.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-07-02 (d=0.5), 2025-04-21 (d=1.1)

### [AMBER 4.45] natgas ↑
- natgas [COMMODITIES]: last 3.68, z20 2.45, zc 0.00, resid-z 4.83 [unexplained], 1d 0.00%, |z20|=2.45
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Iran Faces a Deepening Natural Gas Crisis Ahead of Winter — OilPrice, 2026-11-24. https://oilprice.com/Energy/Energy-General/Iran-Faces-a-Deepening-Natural-Gas-Crisis-Ahead-of-Winter.html
- Source: PNGRB proposes 14% assured returns to attract investment in natural gas pipelines — BusinessLine Mkts, 2026-11-24. https://www.thehindubusinessline.com/markets/commodities/pngrb-proposes-14-assured-returns-to-attract-investment-in-natural-gas-pipelines/article71738560.ece
- Source: Japan Poised to Ramp Up LNG Buying as Power Prices Surge — OilPrice, 2026-11-24. https://oilprice.com/Latest-Energy-News/World-News/Japan-Poised-to-Ramp-Up-LNG-Buying-as-Power-Prices-Surge.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
dyn_tatatech_ns ↑ (4.15), usd_inr ↓ (3.88), comex_copper ↓ (3.82), usd_mxn ↑ (3.48), dyn_crwv ↓ (3.44), dyn_tech ↑ (3.4), dyn_atherenerg_ns ↑ (3.28), dyn_lth ↑ (3.25), dyn_301077_sz ↓ (3.11), dyn_nvda ↓ (2.92), dyn_4417_t ↑ (2.51), fx · 2 series ↓ (2.2)

## India macro
- nifty_50: 25366.4004 (1d -1.68%, z20 0.97, flag none)
- nifty_midcap_100: 61403.8516 (1d -1.00%, z20 0.83, flag none)
- usd_inr: 92.9152 (1d 0.26%, z20 -1.88, flag amber)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4207 (1d 0.70%, z20 -1.13, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- NVDA (NVIDIA Corporation) score 65.0 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- COALINDIA.NS (COAL INDIA LTD) score 61.0 — "Stock recommendations for 25 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 56.7 — "Stock recommendations for 25 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 56.4 — "Stock recommendations for 25 November from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 43.6 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- OHI (Omega Healthcare Investors, In) score 36.4 — "Nasdaq, S&P 500 end lower as investors assess Jensen Huang's return to Nvidia: US Stock Ma"
- BAC (Bank of America Corporation) score 34.9 — "How much more are richest Americans spending on the holidays compared to everyone else?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 31.6 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- TGT (Target Corporation) score 30.1 — "TSLA - SEAPORT INITIATES TESLA AT BUY, $475 TARGET Seaport Global Securities initiated Tes"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 29.9 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- TECH (Bio-Techne Corp) score 29.9 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- HDB (HDFC Bank Limited) score 29.9 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.6 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- IDBI.NS (IDBI BANK LIMITED) score 28.6 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.6 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.2 — "How does EIA compare different types of energy?"
- BLLN (BillionToOne, Inc.) score 23.0 — "TSLA - SEAPORT INITIATES TESLA AT BUY, $475 TARGET Seaport Global Securities initiated Tes"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 22.7 — "Nasdaq, S&P 500 end lower as investors assess Jensen Huang's return to Nvidia: US Stock Ma"
- 301077.SZ (CHINASTARS) score 20.7 — "U.S. PREPARES TO RAISE TARIFFS ON CHINA AND OTHER COUNTRIES -- WSJ"
- CHKP (Check Point Software Technolog) score 18.8 — "Top defence stocks to buy: Apollo Micro Systems, BEL, Data Patterns, GRSE, Zen Technologie"
- COIN (Coinbase Global, Inc.) score 17.0 — "TSLA - SEAPORT INITIATES TESLA AT BUY, $475 TARGET Seaport Global Securities initiated Tes"
- LTH (Life Time Group Holdings, Inc.) score 16.9 — "SPY $QQQ - GOLDMAN SAYS MARKET POSITIONING SIGNALS ABOVE-AVERAGE S&P 500 RETURNS Goldman S"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.4 — "Beware! Fraudsters impersonating as Sebi-registered intermediaries: How can investors avoi"
- BOND (PIMCO Active Bond Exchange-Tra) score 11.7 — "Japanese bond yields fall as lower oil prices ease inflation concerns"
- JIOFIN.BO (Jio Financial Services Limited) score 10.4 — "Canada’s Oilfield Services Sector Is Gearing Up for a Stronger 2027"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Valuation, debt worries overshadow Tata Steel-APL Apollo deal’s strategic gains"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Valuation, debt worries overshadow Tata Steel-APL Apollo deal’s strategic gains"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.5 — "ANT - ANTHROPIC SHARES DOWN 5.6% AFTER FALLING FOR THE LAST TWO SESSIONS"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.1 — "Climate Finance Dispute Derails COP31 Negotiations"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.7 — "A 66-year-old nurse is facing down retirement with just $500 saved. Who’s to blame?"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.6 — "Climate Finance Dispute Derails COP31 Negotiations"
- META (Meta) score 6.2 — "The Energy Transition Needs More Metals but Less Extraction"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.1 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- GS (Goldman Sachs Group, Inc. (The) score 3.7 — "SPY $QQQ - GOLDMAN SAYS MARKET POSITIONING SIGNALS ABOVE-AVERAGE S&P 500 RETURNS Goldman S"
- CRWV (CoreWeave, Inc.) score 3.2 — "AI STOCKS PULL BACK IN PREMARKET AFTER MONDAY'S MASSIVE RALLY U.S. technology and semicond"
- MS (Morgan Stanley) score 3.0 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- MU (Micron Technology, Inc.) score 2.8 — "Micron’s stock falls as an analyst warns about a future supply glut"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.5 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
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