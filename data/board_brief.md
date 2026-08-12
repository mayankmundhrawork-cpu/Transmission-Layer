# Transmission Layer — board brief · 2026-08-12 07:49Z

data as of **2026-08-12** · 98 series · 8 red / 34 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.255, 2d in regime; vol-pct 0.343, breadth-off 0.167, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.32, corr60 0.37, last shift 2026-05-12. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.22, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.08, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.495, β 0.2696, p 0.0); driver zc 1.52 → expected 0.406%. Type hit-rate 0.815 (n=2503).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.393, β 0.2345, p 0.0); driver zc -2.34 → expected -0.606%. Type hit-rate 0.815 (n=2503).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.359, β -0.2161, p 0.0); driver zc -2.34 → expected 0.559%. Type hit-rate 0.815 (n=2503).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.282, β -0.1155, p 0.0); driver zc 1.52 → expected -0.174%. Type hit-rate 0.815 (n=2503).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.275, β -0.1119, p 0.0); driver zc 1.52 → expected -0.168%. Type hit-rate 0.815 (n=2503).
- Track record · residual_reversion: hit-rate **0.491** (n=1135) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2503) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.69] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4464.50, z20 2.84, zc 1.15, resid-z 0.81 [quiet], 1d 1.86%, |z20|=2.84; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 66.21, z20 2.60, zc 0.85, resid-z -0.39 [quiet], 1d 2.22%, |z20|=2.60; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.43, z20 -1.82, zc n/a, resid-z n/a [quiet], 1d -0.36%, GSR<75 (extreme low); |z20|=1.82
- stoxx_50 [INDICES]: last 6553.04, z20 1.73, zc 0.04, resid-z 0.54 [quiet], 1d 0.03%, |z20|=1.73; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.80, z20 1.62, zc -0.11, resid-z 0.13 [quiet], 1d -0.10%, 1y-pct=99
- russell_2000 [INDICES]: last 3026.71, z20 1.58, zc 0.25, resid-z 1.11 [quiet], 1d 0.31%, |z20|=1.58; 1y-pct=99
- dax [INDICES]: last 26415.53, z20 1.58, zc 0.12, resid-z 0.57 [quiet], 1d 0.09%, |z20|=1.58; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.67, z20 1.55, zc 0.39, resid-z 0.46 [quiet], 1d 0.88%, |z20|=1.55; 1y-pct=99
- sp500 [INDICES]: last 7727.41, z20 1.45, zc -0.38, resid-z 0.97 [quiet], 1d -0.33%, 1y-pct=98
- cac_40 [INDICES]: last 8696.02, z20 1.34, zc -0.30, resid-z 0.04 [quiet], 1d -0.22%, 1y-pct=98
- dow_jones [INDICES]: last 53785.19, z20 1.24, zc -0.41, resid-z -0.24 [quiet], 1d -0.35%, 1y-pct=98
- **Mechanism**: The recent move in COMEX gold and silver is driven by persistent geopolitical risk premiums in crude oil prices, which has led to buying interest in these commodities. This move is also reflected in the gold-silver ratio, which is at an extreme low. The channel status indicates that the gold-silver comove channel is valid, suggesting that monetary metals are co-moving. However, the real rates gold inverse channel is weak, which may limit the upside in gold.
- **Gap**: No gap: the move in COMEX gold and silver is largely priced in, with resid_z values of 0.81 and -0.39, respectively, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which has already reacted with a z20 score of 1.37. The Nifty 50 index has not yet reacted, with a z20 score of 0.04.
- Watch next: comex_gold (up) — already moved; geopolitical risk premiums in crude oil prices
- Watch next: comex_silver (up) — already moved; geopolitical risk premiums in crude oil prices
- Watch next: nifty_metal (up) — already moved; co-movement with COMEX silver
- **India receivers**: nifty_midcap_100 (rho 0.516, z 1.23); nifty_50 (rho 0.491, z 0.04); nifty_metal (rho 0.48, z 1.37)
- Source: Gold, silver rates to USD vs INR: Commodity heatmap amid soaring crude oil prices — Mint Markets, 2026-08-12. https://www.livemint.com/market/commodities/gold-silver-rates-to-usd-vs-inr-commodity-heatmap-amid-soaring-crude-oil-prices-11786512599576.html
- Source: Manappuram Finance pushes the pedal on gold loans as other businesses lose sheen — Mint Markets, 2026-08-12. https://www.livemint.com/market/mark-to-market/manappuram-finance-gold-loans-muthoot-finance-nbfc-aum-rbi-loan-growth-asset-quality-11786510821642.html
- Source: Senco Gold shares fall over 8% after Q1 results. What squeezed profitability? — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/senco-gold-shares-fall-over-8-after-q1-results-what-squeezed-profitability/articleshow/133171068.cms
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [AMBER 5.67] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.25, z20 1.74, zc 1.45, resid-z 1.57 [unexplained], 1d 1.16%, |z20|=1.74; 1y-pct=99
- ust_10y [RATES]: last 4.72, z20 1.47, zc 1.52, resid-z 1.47 [moved], 1d 1.51%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.47, z20 -1.11, zc 0.23, resid-z 0.24 [quiet], 1d 0.07%, 1y-pct=1
- tips_10y_real [RATES]: last 2.43, z20 0.88, zc 0.78, resid-z 0.38 [quiet], 1d 1.25%, 1y-pct=97
- ust_2y [RATES]: last 4.25, z20 0.20, zc 1.12, resid-z 0.77 [quiet], 1d 1.43%, 1y-pct=96
- **Mechanism**: The recent move in US Treasury yields, particularly the 10-year and 30-year yields, is driven by the fading hopes of a US-Iran agreement, which has led to a risk-off sentiment in the market. This sentiment is further reinforced by the upcoming July CPI data, which may put pressure on Treasury yields if it comes in higher than expected. The move is also correlated with the price action in other assets, such as brent and wti, which have not moved yet but have a historical lead of 3 days.
- **Gap**: No gap: the big raw move in ust_30y with a resid_z of 1.57 is not an anomaly as it is largely explained by the factor exposures, with an r2 of 0.24, indicating that the move is priced in.
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the move in US Treasury yields through the valid gold_silver_comove and metal_copper_channel. However, the inr_oil_channel is weak, and the dxy_inr_channel is also weak, which may limit the transmission of the move to the Indian market.
- Watch next: ust_10y (up) — already moved; risk-off sentiment and potential for higher CPI data
- Watch next: brent (up) — not yet - watch; historical lead of 3 days and correlation with ust_30y
- Source: US Stock Market: Treasury yields pare gains as Iran comments dampen hopes for Strait of Hormuz deal — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-treasury-yields-pare-gains-as-iran-comments-dampen-hopes-for-strait-of-hormuz-deal/articleshow/133171566.cms
- Source: BARCLAYS SEES TREASURY YIELDS STAYING HIGH Barclays says growing reliance on price-sensitive private investors could keep long-term U.S. Treasury yields near multi-decade highs. Private investors now hold about 73% of the Treasury market, up from roughly 50% a decade ago. With — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34647
- Source: SBI returns to dollar bond market after a year, prices five-year notes 88 bps over US Treasury — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/sbi-returns-to-dollar-bond-market-after-a-year-prices-five-year-notes-88-bps-over-us-treasury/articleshow/133155806.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.31] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 2.31, zc n/a, resid-z n/a [quiet], 1d 0.43%, 52-wk extreme (pct=99); |z20|=2.31; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 2.31, indicating a potential overbought condition. This move is likely priced, given the small resid_z, and may propagate through the metal_copper_channel, which is currently valid. The RISK_ON regime and VALID gold_silver_comove channel also support this mechanism.
- **Gap**: No gap: the move is likely priced, given the small resid_z and the fact that the nifty_midcap_100 and other transmission candidates have already reacted
- **India take**: The Indian instruments that express this move, such as nifty_midcap_100 and dyn_bharatcoal_ns, have already reacted. However, dyn_pcjeweller_ns remains quiet and may be worth watching.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to midcap_largecap_ratio
- Watch next: dyn_bharatcoal_ns (down) — already moved; reacted to midcap_largecap_ratio
- Watch next: dyn_pcjeweller_ns (down) — not yet - watch; quiet despite midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.521, z 1.23); dyn_bharatcoal_ns (rho 0.416, z -1.03); dyn_pcjeweller_ns (rho 0.387, z 0.19); dyn_indianb_ns (rho 0.35, z 2.25)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 5.27] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.58, z20 -3.27, zc -2.79, resid-z -1.30 [moved], 1d -3.82%, |z20|=3.27
- **Mechanism**: The dyn_ohi decline is driven by a risk-off sentiment, as evidenced by the RISK_ON regime with P(high-vol)=0.012, and the VALID vix_equity_inverse channel indicating a vol spike leading to equity drawdown. The metal_copper_channel also suggests a potential transmission to Indian metal equities.
- **Gap**: No gap: the dyn_ohi move is largely priced, with a resid_z of -1.3 indicating that most of the move is explained by factor exposures
- **India take**: The Indian instrument nifty_fmcg has already reacted to the dyn_ohi decline, with a z20 of -2.18. The metal_copper_channel may also lead to a decline in Indian metal equities.
- Watch next: nifty_fmcg (down) — already moved; reacted to dyn_ohi
- **India receivers**: nifty_fmcg (rho 0.374, z -2.18)
- Source: Sensex crashes 600 points, Nifty nears 24,250; investors lose  ₹3 lakh crore; key factors behind market selloff explained — Mint Markets, 2026-08-12. https://www.livemint.com/market/stock-market-news/sensex-crashes-600-points-nifty-near-24-250-investors-lose-3-lakh-crore-key-factors-behind-market-selloff-explained-11786516924623.html
- Source: Global Market: Japan stocks muted as investors await US CPI report — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-muted-as-investors-await-us-cpi-report/articleshow/133169643.cms
- Source: Global Investors Favor Taiwan Over Korea Stocks After AI Selloff — Mint Markets, 2026-08-11. https://www.livemint.com/market/global-investors-favor-taiwan-over-korea-stocks-after-ai-selloff-11786490631027.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [AMBER 4.31] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1562.80, z20 2.31, zc 0.75, resid-z 0.40 [quiet], 1d 2.45%, |z20|=2.31; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's shares is driven by the government's extension of subsidies for electric two-wheelers until FY28, which has improved sentiment towards the sector. This move is likely to propagate through the metal_copper_channel, as global copper leads Indian metal equities. The VALID gold_silver_comove channel also suggests a potential co-move with other monetary metals.
- **Gap**: No gap: the move in dyn_atherenerg_ns is largely priced, given its resid_z of 0.4, which is relatively small compared to its z20 level of 2.31
- **India take**: The Indian instrument that expresses this move is Tata Motors, which has a significant stake in the electric vehicle market. It has not reacted yet, but may follow suit given the improved sentiment towards the sector.
- Watch next: ola_electric_ns (up) — not yet - watch; similar business model to Ather Energy
- Source: Ola Electric, Ather Energy shares surge up to 5% as EV subsidies extended to FY28 — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/ola-electric-ather-energy-shares-surge-up-to-5-as-ev-subsidies-extended-to-fy28-11786439521082.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.22] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.00, z20 2.22, zc 0.15, resid-z 1.16 [quiet], 1d 0.22%, |z20|=2.22; 1y-pct=100
- **Mechanism**: The recent increase in dyn_bac, despite being a big raw move, is priced with a small resid_z, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is a valid channel, may propagate this move, potentially influencing Indian metal equities. However, the lack of a clear unexplained component and the absence of a strong channel to transmit the move to Indian markets limits the potential for a significant gap.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and no clear unexplained component
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.36 via dyn_bac, limiting the potential for a significant gap in Indian markets. The metal_copper_channel may still influence Indian metal equities, but the impact is likely to be limited.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.357, z 2.81)
- Source: S&P 500 EARNINGS BOOM MAY SET UP A TOUGHER 2027 S&P 500 EPS is tracking roughly 32% growth in Q2, after 30% in Q1 — a historically rare back-to-back surge. Bank of America warns growth could slow below 20% by Q1 2027 and to the mid-teens for the full year. That matters because — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34608
- Source: STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a faster pace. Labor participation among people aged 55+ has dropped from above 40% pre-pandemic to 36.9% in July. Bank of America economists point to rising wealth as a key driver. With the — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34605
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 4.03] bovespa ↓
- bovespa [INDICES]: last 167728.12, z20 -4.03, zc -2.34, resid-z -2.28 [unexplained], 1d -2.59%, |z20|=4.03
- **Mechanism**: bovespa ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

### [AMBER 3.67] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 849.30, z20 1.67, zc -0.58, resid-z -0.72 [quiet], 1d -1.84%, 1y-pct=98
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.478 via dyn_tatatech_ns, z 0.74, quiet); dyn_tataelxsi_ns (rho 0.476 via dyn_tatatech_ns, z 0.72, quiet)
- **India receivers**: nifty_it (rho 0.478, z 0.74); dyn_tataelxsi_ns (rho 0.476, z 0.72)
- Source: Q1 Results Today Live: Marksans Pharma PAT rises 43.6% y-o-y, Tata Motors, Apollo Hospitals, HAL, Grasim, GMR Airports, Lenskart, Abbott, VA Tech, IRCON, AIA, IRCTC, Sun TV, EID Parry to announce Q1 results — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-hal-grasim-ind-tata-motors-apollo-hospitals-gmr-airports-lenskart-gic-abbott-aia-engg-irctc-sun-tv-eid-parry-va-tech-ircon-titagarh-results-12-august-2026/article71332017.ece
- Source: Sensex today | Stock Market Live: Sensex falls over 600 points, Nifty drops below 24,300; Tata stocks tumble — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-august-2026/article71332253.ece
- Source: Tata Group stocks fall up to 5% after Tata Sons Chairman Chandrasekaran resigns — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/indias-tata-group-stocks-fall-by-4-after-report-tata-sons-chairman-has-quit/article71335270.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
shanghai_comp ↑ (3.59), fx · 2 series ↑ (3.52), dyn_coin ↓ (3.18), dyn_tech ↑ (3.09), dyn_cupid_ns ↑ (2.81), dyn_hdb ↓ (2.81), usd_brl ↑ (2.39), dyn_lth ↑ (2.32), dyn_idbi_ns ↓ (2.26), dyn_indianb_ns ↑ (2.25), dyn_pltr ↑ (2.23), nifty_fmcg ↓ (2.18)

## India macro
- nifty_50: 24297.8496 (1d -0.71%, z20 0.04, flag none)
- nifty_midcap_100: 63668.3984 (1d -0.28%, z20 1.23, flag amber)
- usd_inr: 95.4025 (1d 0.01%, z20 -0.88, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6203 (1d 0.43%, z20 2.31, flag red)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · India WPI T-2d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 93.1 — "Russia Imports Indian Fuel as Refinery Crisis Deepens"
- INOXINDIA.NS (INOX INDIA LIMITED) score 92.7 — "Russia Imports Indian Fuel as Refinery Crisis Deepens"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 92.0 — "Russia Imports Indian Fuel as Refinery Crisis Deepens"
- INDIANB.NS (INDIAN BANK) score 68.5 — "Russia Imports Indian Fuel as Refinery Crisis Deepens"
- BAC (Bank of America Corporation) score 54.2 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.1 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis"
- TECH (Bio-Techne Corp) score 52.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis"
- HDB (HDFC Bank Limited) score 50.0 — "HDFC Life Share Price Live Updates: HDFC Life's Current Valuation"
- COIN (Coinbase Global, Inc.) score 47.7 — "Global Market: China stocks rise as tech shares lead gains ahead of US CPI"
- OHI (Omega Healthcare Investors, In) score 47.0 — "Sensex crashes 600 points, Nifty nears 24,250; investors lose  ₹3 lakh crore; key factors "
- IDBI.NS (IDBI BANK LIMITED) score 45.3 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.3 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- CHKP (Check Point Software Technolog) score 45.0 — "Dhoot Transmission IPO day 3: Issue subscribed 8 times so far; check latest GMP, issue rev"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.0 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.6 — "U.S. SAYS HORMUZ OIL FLOWS ARE RECOVERING Energy Secretary Chris Wright says nearly 9 mill"
- LTH (Life Time Group Holdings, Inc.) score 33.2 — "Dhoot Transmission IPO day 3: Issue subscribed 8 times so far; check latest GMP, issue rev"
- 301077.SZ (CHINASTARS) score 23.2 — "Global Market: China stocks rise as tech shares lead gains ahead of US CPI"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.0 — "India bonds hemmed in by oil worries ahead of inflation data"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 20.2 — "Manappuram Finance pushes the pedal on gold loans as other businesses lose sheen"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.2 — "TCS, other Tata stocks fall up to 4% as N Chandrasekaran resigns"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.4 — "Curry Dish, Not Big Mac, Captures Just How Weak Yen Is, BNY Says"
- JIOFIN.BO (Jio Financial Services Limited) score 13.9 — "ideaForge Technology shares drop over 9% in two days. JM Financial downgrades rating"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 13.0 — "China's Coal-to-Gas Industry Set to Triple by 2030, Rystad Says"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.3 — "ideaForge Technology shares drop over 9% in two days. JM Financial downgrades rating"
- MS (Morgan Stanley) score 11.9 — "Manappuram Finance shares jump 3% after Q1 profit soars 4x. Why Jefferies, Morgan Stanley "
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.9 — "Lalithaa Jewellery’s ₹1,700 crore IPO opens August 17; price band fixed at ₹190-201"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.6 — "TCS, other Tata stocks fall up to 4% as N Chandrasekaran resigns"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 9.6 — "ideaForge Technology shares drop over 9% in two days. JM Financial downgrades rating"
- NVDA (NVIDIA Corporation) score 9.6 — "NVDA - NVIDIA’S $500 BILLION AI FINANCING PLAN DIVIDES WALL STREET Nvidia unveiled partner"
- AAPL (Apple Inc.) score 7.5 — "Apple shares fall amid confusion over 2027 ‘all-glass’ iPhone plans; company clarifies, ‘d"
- META (Meta) score 6.5 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.1 — "QIP fundraising hits one-year high, Adani firms dominate"
- VT (Vanguard Total World Stock Ind) score 6.0 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- INTC (Intel Corporation) score 4.8 — "Intel’s $15 billion stock sale. Why shares fell despite AI boom"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.0 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- GOOGL (Alphabet) score 2.9 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- PLTR (Palantir Technologies Inc.) score 2.6 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- AMZN (Amazon.com, Inc.) score 1.9 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 1.7 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"

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