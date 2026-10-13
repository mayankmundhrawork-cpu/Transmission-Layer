# Transmission Layer — board brief · 2026-10-13 11:43Z

data as of **2026-10-13** · 97 series · 6 red / 35 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.7, 7d in regime; vol-pct 0.649, breadth-off 0.75, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.32, corr60 -0.4, contra nifty_50 corr20=0.28, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.28, corr60 0.23, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.06, corr60 0.15, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.14, corr60 -0.09, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.29, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.59, corr60 0.14, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2126) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.49] usd_inr ↓
- usd_inr [FX]: last 95.28, z20 -2.49, zc -0.98, resid-z -0.86 [quiet], 1d -0.50%, 20d range extreme; |z20|=2.49
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.406 via usd_inr, z -0.63, quiet); dyn_karurvysya_ns (rho -0.374 via usd_inr, z 3.56, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.406, z -0.63); dyn_karurvysya_ns (rho -0.374, z 3.56)
- Source: RBI to continue efforts to curb rupee volatility; external factors driving currency fall: FM — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/stocks/news/rbi-to-continue-efforts-to-curb-rupee-volatility-external-factors-driving-currency-fall-fm/articleshow/134915932.cms
- Source: Rupee jumps 40 paise to close at 95.38 against US dollar — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/forex/rupee-jumps-40-paise-to-close-at-9538-against-us-dollar/article71578987.ece
- Source: Rupee outpaces Asian peers on fresh FX curbs, RBI intervention — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/forex/rupee-outpaces-asian-peers-on-fresh-fx-curbs-rbi-intervention/articleshow/134915016.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.59] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 29830.10, z20 2.76, zc 3.54, resid-z 2.49 [unexplained], 1d 5.22%, |z20|=2.76
- dyn_tataelxsi_ns [EQUITIES]: last 3426.70, z20 2.07, zc 2.62, resid-z 1.99 [unexplained], 1d 5.21%, |z20|=2.07
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-31 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho 0.878 via nifty_it, z 0.42, quiet); nifty_50 (rho 0.591 via dyn_tataelxsi_ns, z -0.5, quiet); dyn_justdial_bo (rho 0.525 via nifty_it, z 0.7, quiet); dyn_tatatech_ns (rho 0.522 via nifty_it, z 1.48, reacted); nifty_fmcg (rho 0.508 via dyn_tataelxsi_ns, z -0.54, quiet)
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.878 vs nifty_it, historically leads by 3d
- Watch next: dyn_justdial_bo (co-move) — not yet - watch; rho 0.525 vs nifty_it, historically leads by 4d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.591 vs dyn_tataelxsi_ns
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.508 vs dyn_tataelxsi_ns
- **India receivers**: dyn_techm_ns (rho 0.878, z 0.42); nifty_50 (rho 0.591, z -0.5); dyn_justdial_bo (rho 0.525, z 0.7); dyn_tatatech_ns (rho 0.522, z 1.48)
- Source: Q2 Results Today Live: Q2 Results Today Live: Tata Elxsi, ICICI Pru Life, Hero Motors shares trade mixed; PNB Gilts jumps 8% — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-hero-motors-icici-pru-tata-elxsi-ss-retail-anand-rathi-share-company-results-13-october-2026/article71577900.ece
- Source: Dividend comparison: TCS, Tata Elxsi, Trent - Which Tata stock paid highest amount in FY26? What 9 firms disbursed — Mint Markets, 2026-10-13. https://www.livemint.com/market/stock-market-news/dividend-comparison-tcs-tata-elxsi-trent-which-tata-stock-paid-highest-amount-in-fy26-what-9-firms-disbursed-11791875007417.html
- Historical analogues: 2025-07-31 (d=0.34), 2025-01-30 (d=0.36), 2025-07-09 (d=0.4)

### [AMBER 5.49] brent ↑
- brent [COMMODITIES]: last 104.68, z20 0.49, zc -0.84, resid-z 0.56 [quiet], 1d -1.85%, 1-session move -1.85% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.898 vs brent, historically leads by 5d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.642 vs brent, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.648 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.636 vs brent
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.609 vs brent
- Source: Japan to Compensate Oil Importers for High Shipping Costs — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Japan-to-Compensate-Oil-Importers-for-High-Shipping-Costs.html
- Source: Saudi Arabia Plans Massive Expansion of Oil Pipeline to Bypass Hormuz — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Plans-Massive-Expansion-of-Oil-Pipeline-to-Bypass-Hormuz.html
- Source: Gold ticks up as oil eases; spotlight on US inflation data — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/gold/gold-ticks-up-as-oil-eases-spotlight-on-us-inflation-data/article71578314.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [AMBER 5.42] wti ↓
- wti [COMMODITIES]: last 92.03, z20 -0.42, zc -0.76, resid-z 0.57 [quiet], 1d -1.82%, 1-session move -1.82% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.898 vs wti
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.56 vs wti
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.543 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.51 vs wti
- Source: Japan to Compensate Oil Importers for High Shipping Costs — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Japan-to-Compensate-Oil-Importers-for-High-Shipping-Costs.html
- Source: Saudi Arabia Plans Massive Expansion of Oil Pipeline to Bypass Hormuz — OilPrice, 2026-10-13. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Plans-Massive-Expansion-of-Oil-Pipeline-to-Bypass-Hormuz.html
- Source: Gold ticks up as oil eases; spotlight on US inflation data — BusinessLine Mkts, 2026-10-13. https://www.thehindubusinessline.com/markets/gold/gold-ticks-up-as-oil-eases-spotlight-on-us-inflation-data/article71578314.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 4.83] kospi ↓
- kospi [INDICES]: last 6005.98, z20 -4.83, zc -3.10, resid-z -0.52 [moved], 1d -5.92%, |z20|=4.83
- **Mechanism**: kospi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.479 via kospi, z 2.76, reacted); dyn_bajfinance_ns (rho 0.467 via kospi, z -0.09, quiet); dyn_techm_ns (rho -0.412 via kospi, z 0.42, quiet)
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.943 vs kospi, historically leads by 2d
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.841 vs kospi, historically leads by 2d
- **India receivers**: nifty_it (rho -0.479, z 2.76); dyn_bajfinance_ns (rho 0.467, z -0.09); dyn_techm_ns (rho -0.412, z 0.42)
- Historical analogues: 2026-07-10 (d=0.0), 2026-04-02 (d=0.01), 2025-04-01 (d=0.04)

### [AMBER 4.62] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.60, z20 0.95, zc -1.74, resid-z -2.34 [unexplained], 1d -1.23%, 1y-pct=97
- dyn_bond [EQUITIES]: last 86.95, z20 -0.75, zc 0.10, resid-z 0.58 [quiet], 1d 0.00%, 1y-pct=2
- tips_10y_real [RATES]: last 2.87, z20 0.73, zc -0.90, resid-z -1.52 [unexplained], 1d -1.71%, 1y-pct=96
- ust_10y [RATES]: last 5.22, z20 0.72, zc -1.12, resid-z -1.95 [unexplained], 1d -1.14%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.648 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 1d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.512 vs ust_10y, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.586 vs dyn_bond
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.535 vs ust_30y
- Source: Global Market: Eurozone bond yields fall as tech stock selloff boosts safe-haven demand — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-fall-as-tech-stock-selloff-boosts-safe-haven-demand/articleshow/134915060.cms
- Source: Surging bond yields wreak havoc on Dalal Street, but IMF sees more pain ahead. Why AI is one of the culprits — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/stocks/news/surging-bond-yields-wreak-havoc-on-dalal-street-but-imf-sees-more-pain-ahead-why-ai-is-one-of-the-culprits/articleshow/134911842.cms
- Source: India bonds rise as investors see value after 10-year yield nears 7.40% — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/bonds/india-bonds-rise-as-investors-see-value-after-10-year-yield-nears-7-40/articleshow/134908753.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 4.33] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -4.33, zc -1.48, resid-z -2.01 [unexplained], 1d -0.16%, |z20|=4.33; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.366 via usd_cny, z -0.69, quiet); dyn_bajfinance_ns (rho -0.354 via usd_cny, z -0.09, quiet)
- **India receivers**: dyn_policybzr_ns (rho -0.366, z -0.69); dyn_bajfinance_ns (rho -0.354, z -0.09)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.22] indices · 2 series ↑
- sp500 [INDICES]: last 7807.79, z20 1.39, zc 0.84, resid-z -1.45 [quiet], 1d -0.05%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30669.27, z20 0.51, zc 0.48, resid-z -0.78 [quiet], 1d -0.69%, 1y-pct=97
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.952 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.73 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.86 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.629 vs sp500, historically leads by 2d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.607 vs sp500
- Source: SpaceX Stock: Why Wall Street sees more upside ahead — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/us-stocks/news/spacex-stock-why-wall-street-sees-more-upside-ahead/slideshow/134908990.cms
- Source: Stock market outlook today, 13 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-10-13. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-13-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11791851924757.html
- Source: US stocks: Nasdaq ends lower as oil prices surge ahead of earnings, economic data — ET Markets, 2026-10-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-nasdaq-ends-lower-as-oil-prices-surge-ahead-of-earnings-economic-data/articleshow/134902064.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (3.91), dyn_4417_t ↑ (3.91), shanghai_comp ↓ (3.71), dyn_karurvysya_ns ↑ (3.56), indices · 2 series ↓ (3.37), dyn_tech ↑ (3.26), dyn_rs ↑ (3.14), dyn_meta ↑ (2.78), commodities · 2 series ↓ (2.62), dyn_cartrade_ns ↑ (2.61), dyn_jiofin_bo ↓ (2.58), bovespa ↑ (2.34)

## India macro
- nifty_50: 22721.9492 (1d 1.60%, z20 -0.50, flag amber)
- nifty_midcap_100: 59458.4492 (1d 1.04%, z20 -0.65, flag none)
- usd_inr: 95.2800 (1d -0.50%, z20 -2.49, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6168 (1d -0.56%, z20 -0.95, flag none)
- Next India prints: NSDL FPI flows T-0d · India WPI T-1d · India trade / CAD data T-2d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 79.1 — "Stocks to Watch Today: HCL Tech, Nazara, BOI, TD Power, Juniper Green, Airflow Rail, Globu"
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.2 — "Stocks to Watch Today: HCL Tech, Nazara, BOI, TD Power, Juniper Green, Airflow Rail, Globu"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.3 — "Stocks to Watch Today: HCL Tech, Nazara, BOI, TD Power, Juniper Green, Airflow Rail, Globu"
- INDIANB.NS (INDIAN BANK) score 66.8 — "RBL Bank shares plunge 8% despite 170% jump in Q2 profit. Should you buy, sell or hold?"
- BAC (Bank of America Corporation) score 59.8 — "RBL Bank shares plunge 8% despite 170% jump in Q2 profit. Should you buy, sell or hold?"
- HDB (HDFC Bank Limited) score 54.4 — "RBL Bank shares plunge 8% despite 170% jump in Q2 profit. Should you buy, sell or hold?"
- COIN (Coinbase Global, Inc.) score 53.6 — "IMF sees milder global slowdown as AI boom offsets war hit — warns resilience is nearing l"
- TECHM.NS (TECH MAHINDRA LIMITED) score 52.9 — "Qualcomm sells nearly 1% stake in Shadowfax Technologies for ₹157 cr"
- IDBI.NS (IDBI BANK LIMITED) score 52.5 — "RBL Bank shares plunge 8% despite 170% jump in Q2 profit. Should you buy, sell or hold?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.5 — "RBL Bank shares plunge 8% despite 170% jump in Q2 profit. Should you buy, sell or hold?"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 52.5 — "RBL Bank shares plunge 8% despite 170% jump in Q2 profit. Should you buy, sell or hold?"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.6 — "Qualcomm sells nearly 1% stake in Shadowfax Technologies for ₹157 cr"
- TECH (Bio-Techne Corp) score 50.6 — "Qualcomm sells nearly 1% stake in Shadowfax Technologies for ₹157 cr"
- OHI (Omega Healthcare Investors, In) score 42.0 — "HD Fire Protect raises ₹213 cr from anchor investors ahead of IPO"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.3 — "Global Market: Japan bond yields diverge as investors weigh inflation, BOJ outlook"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.3 — "Hitachi Energy, E2E Networks, Anant Raj, other AI-linked stocks slide up to 5% as global A"
- TGT (Target Corporation) score 31.6 — "ICICI Prudential AMC shares rise 2% as Jefferies, other brokerages revise target prices af"
- CHKP (Check Point Software Technolog) score 28.0 — "2,000% returns in 10 yrs! This multibagger chemical stock jumps 16% amid huge trading volu"
- LTH (Life Time Group Holdings, Inc.) score 25.8 — "Bitcoin trades near $83,000 as macro headwinds and US political uncertainty weigh on senti"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.4 — "RBL Bank share price crashes 8% after Q2 results - Should investors buy, sell, or hold the"
- 301077.SZ (CHINASTARS) score 19.5 — "Global Market: China's yuan holds near 3-year high despite strong dollar; PBOC fixing supp"
- SEPN (Septerna, Inc.) score 19.4 — "Unique Picks: 10 stocks held by a single MF scheme in September; rally up to 225% in FY27 "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.6 — "Stocks to Watch, Oct 12: Lenskart, Everyday Ind, SJS, Authum, Adani enterprise, M&M"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.2 — "My wife says we can’t afford to retire. We have $4 million. Do I just keep working?"
- JIOFIN.BO (Jio Financial Services Limited) score 9.8 — "Bandhan Bank shares jump 7% as Abu Dhabi’s IHC explores stake in promoter Bandhan Financia"
- VT (Vanguard Total World Stock Ind) score 9.6 — "In charts: How one of the world's biggest economies got trapped by debt"
- JEF (Jefferies Financial Group Inc.) score 9.3 — "ICICI Prudential AMC shares rise 2% as Jefferies, other brokerages revise target prices af"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.6 — "Dividend comparison: TCS, Tata Elxsi, Trent - Which Tata stock paid highest amount in FY26"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.6 — "Dividend comparison: TCS, Tata Elxsi, Trent - Which Tata stock paid highest amount in FY26"
- BZ=F (Brent Crude Oil Last Day Finan) score 8.4 — "FORMER U.S. DEFENSE SECRETARY WARNS IRAN WAR HAS “NO EASY WAY OUT” Former Defense Secretar"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.9 — "RBI to curb rupee volatility amid external pressures, says Finance Minister Sitharaman"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 7.6 — "RBI to curb rupee volatility amid external pressures, says Finance Minister Sitharaman"
- RS (Reliance, Inc.) score 7.6 — "Jio IPO may trigger Reliance’s next big re-rating. Why Religare sees 47% upside"
- GS (Goldman Sachs Group, Inc. (The) score 7.2 — "GOLDMAN SACHS TURNS BULLISH ON STOCKS AND BONDS Goldman Sachs has upgraded equities to ove"
- NVDA (NVIDIA Corporation) score 6.7 — "Nvidia’s share of China AI chip market falls to 34% as Huawei gains ground"
- META (Meta) score 5.3 — "Meta is back on the AI leaderboard with its new family of Wonder models"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.0 — "CKK Retail Mart to issue 5:1 bonus, enhance share capital"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.8 — "Nomura becomes latest brokerage to cut PB Fintech share price target by 31%, lists 2 scena"
- DELL (Dell Technologies Inc.) score 0.3 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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