# Transmission Layer — board brief · 2026-08-12 05:45Z

data as of **2026-08-12** · 98 series · 8 red / 34 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.31, 2d in regime; vol-pct 0.37, breadth-off 0.25, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.32, corr60 0.37, last shift 2026-05-12. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.22, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.01, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

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

### [RED 9.03] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4452.30, z20 2.74, zc 0.98, resid-z 0.81 [quiet], 1d 1.58%, |z20|=2.74; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.28, z20 2.25, zc 0.30, resid-z -0.62 [quiet], 1d 0.79%, |z20|=2.25; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6553.86, z20 2.01, zc 0.35, resid-z 0.59 [quiet], 1d 0.28%, |z20|=2.01; 1y-pct=100
- dax [INDICES]: last 26392.05, z20 1.74, zc 0.34, resid-z 0.57 [quiet], 1d 0.26%, |z20|=1.74; 1y-pct=100
- cac_40 [INDICES]: last 8717.47, z20 1.67, zc -0.13, resid-z 0.08 [quiet], 1d -0.10%, |z20|=1.67; 1y-pct=99
- dyn_vt [EQUITIES]: last 160.80, z20 1.62, zc -0.11, resid-z 0.13 [quiet], 1d -0.10%, 1y-pct=99
- russell_2000 [INDICES]: last 3026.71, z20 1.58, zc 0.25, resid-z 1.11 [quiet], 1d 0.31%, |z20|=1.58; 1y-pct=99
- sp500 [INDICES]: last 7727.41, z20 1.45, zc -0.38, resid-z 0.97 [quiet], 1d -0.33%, 1y-pct=98
- comex_copper [COMMODITIES]: last 6.65, z20 1.39, zc 0.23, resid-z 0.46 [quiet], 1d 0.51%, 1y-pct=98
- dow_jones [INDICES]: last 53785.19, z20 1.24, zc -0.41, resid-z -0.24 [quiet], 1d -0.35%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.20, z20 -1.15, zc n/a, resid-z n/a [quiet], 1d 0.79%, GSR<75 (extreme low)
- **Mechanism**: The current move is driven by reduced bets on Federal Reserve tightening next month, as investors await key U.S. inflation data. This has led to a rise in gold prices, which in turn has triggered a co-movement in other monetary metals, such as silver, and has influenced equity markets. The gold-silver ratio, which is at an extreme low, also suggests a rotation towards silver.
- **Gap**: No gap: The big raw move in gold prices is largely priced in, with a resid_z of 0.81, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instruments that express this move are the Nifty Metal index, which has reacted, and the Nifty Midcap 100 index, which has also reacted. The Nifty 50 index has not yet reacted.
- Watch next: comex_gold (up) — already moved; Reduced bets on Federal Reserve tightening
- Watch next: comex_silver (up) — already moved; Co-movement with gold
- Watch next: stoxx_50 (up) — already moved; Influence of gold price on equity markets
- **India receivers**: nifty_midcap_100 (rho 0.52, z 1.18); nifty_50 (rho 0.487, z 0.05); nifty_metal (rho 0.478, z 1.36)
- Source: Senco Gold shares fall over 8% after Q1 results. What squeezed profitability? — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/senco-gold-shares-fall-over-8-after-q1-results-what-squeezed-profitability/articleshow/133171068.cms
- Source: Gold rebounds towards 10-week high as markets brace for US CPI data — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/gold/gold-rebounds-towards-10-week-high-as-markets-brace-for-us-cpi-data/article71335003.ece
- Source: Gold prices rise Rs 1,200/10g; silver jumps Rs 2,612/kg as traders eye US inflation data. Check key levels — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-rise-rs-1200/10g-silver-jumps-rs-2612/kg-as-traders-eye-us-inflation-data-check-key-levels/articleshow/133169568.cms
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

### [RED 5.27] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.58, z20 -3.27, zc -2.79, resid-z -1.30 [moved], 1d -3.82%, |z20|=3.27
- **Mechanism**: The decline in dyn_ohi is driven by a combination of factors, including a potential shift in risk appetite ahead of the US CPI report and ongoing tensions in the Middle East. The valid vix_equity_inverse channel suggests that the vol spike is leading to an equity drawdown. However, the weak dxy_inr_channel and inr_oil_channel imply that the transmission to Indian markets may be muted.
- **Gap**: No gap: the big raw move in dyn_ohi has a relatively small resid_z of -1.3, indicating that the move is largely priced in by factors
- **India take**: The Indian instrument nifty_fmcg has already reacted to the decline in dyn_ohi, with a z20 of -2.17. Further downside in nifty_fmcg is possible if the risk-off sentiment persists.
- Watch next: nifty_fmcg (down) — already moved; reacted to dyn_ohi decline
- **India receivers**: nifty_fmcg (rho 0.374, z -2.17)
- Source: Global Market: Japan stocks muted as investors await US CPI report — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-muted-as-investors-await-us-cpi-report/articleshow/133169643.cms
- Source: Global Investors Favor Taiwan Over Korea Stocks After AI Selloff — Mint Markets, 2026-08-11. https://www.livemint.com/market/global-investors-favor-taiwan-over-korea-stocks-after-ai-selloff-11786490631027.html
- Source: ETHEREUM BUYERS ACCUMULATE AHEAD OF CPI Investors are accumulating Ethereum ahead of Wednesday’s U.S. CPI report, according to Nansen. Managed money is reportedly buying ETH on spot markets at 7.2 times its normal pace. Meanwhile, sophisticated traders remain net short Bitcoin — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34648
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [RED 5.19] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 2.19, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=99); |z20|=2.19; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, indicating a potential rotation in market sentiment. However, with a resid_z of None, this move appears to be largely priced in. The RISK_ON regime and VALID vix_equity_inverse channel suggest that equity markets are likely to remain volatile.
- **Gap**: No gap: The midcap_largecap_ratio move is largely priced in, with resid_z=None and a high 52-week extreme percentage.
- **India take**: Indian midcap stocks, such as those in the nifty_midcap_100 index, have already reacted to the midcap_largecap_ratio move. However, specific stocks like dyn_pcjeweller_ns remain quiet and are worth watching.
- Watch next: nifty_midcap_100 (down) — already moved; Reacted to midcap_largecap_ratio with rho=0.522
- Watch next: dyn_bharatcoal_ns (down) — already moved; Reacted to midcap_largecap_ratio with rho=0.417
- Watch next: dyn_pcjeweller_ns (down) — not yet - watch; Quiet despite rho=0.391 to midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.522, z 1.18); dyn_bharatcoal_ns (rho 0.417, z -1.03); dyn_pcjeweller_ns (rho 0.391, z 0.24)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.22] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.00, z20 2.22, zc 0.15, resid-z 1.16 [quiet], 1d 0.22%, |z20|=2.22; 1y-pct=100
- **Mechanism**: The recent increase in dyn_bac, despite being a big raw move, is priced with a small resid_z, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is a valid channel, may propagate this move, potentially influencing Indian metal equities. However, the lack of a clear unexplained component and the absence of a strong channel to transmit the move to Indian markets limits the potential for a significant gap.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and no clear unexplained component
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.36 via dyn_bac, limiting the potential for a significant gap in Indian markets. The metal_copper_channel may still influence Indian metal equities, but the impact is likely to be limited.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.358, z 2.72)
- Source: S&P 500 EARNINGS BOOM MAY SET UP A TOUGHER 2027 S&P 500 EPS is tracking roughly 32% growth in Q2, after 30% in Q1 — a historically rare back-to-back surge. Bank of America warns growth could slow below 20% by Q1 2027 and to the mid-teens for the full year. That matters because — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34608
- Source: STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a faster pace. Labor participation among people aged 55+ has dropped from above 40% pre-pandemic to 36.9% in July. Bank of America economists point to rising wealth as a key driver. With the — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34605
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.07] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1537.60, z20 2.07, zc 0.25, resid-z 0.96 [quiet], 1d 0.80%, |z20|=2.07; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ola Electric, Ather Energy shares surge up to 5% as EV subsidies extended to FY28 — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/ola-electric-ather-energy-shares-surge-up-to-5-as-ev-subsidies-extended-to-fy28-11786439521082.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 4.03] bovespa ↓
- bovespa [INDICES]: last 167728.12, z20 -4.03, zc -2.34, resid-z -2.28 [unexplained], 1d -2.59%, |z20|=4.03
- **Mechanism**: bovespa ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

### [AMBER 3.79] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 855.15, z20 1.79, zc -0.37, resid-z -0.66 [quiet], 1d -1.16%, 1y-pct=98
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.474 via dyn_tatatech_ns, z 0.77, quiet); dyn_tataelxsi_ns (rho 0.471 via dyn_tatatech_ns, z 0.99, quiet)
- **India receivers**: nifty_it (rho 0.474, z 0.77); dyn_tataelxsi_ns (rho 0.471, z 0.99)
- Source: Q1 Results Today Live: Tata Motors, Apollo Hospitals, HAL, Grasim GMR Airports, Lenskart, Abbott, VA Tech, IRCON, AIA, IRCTC, Sun TV, EID Parry to announce Q1 results, NBCC, Siemens, RVNL, Kalpataru, MRF, Zydus Lifesciences, KPI Green, Manappuram Finance in focus, TD Power Systems, Finolex shares hit 52-week high — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-hal-grasim-ind-tata-motors-apollo-hospitals-gmr-airports-lenskart-gic-abbott-aia-engg-irctc-sun-tv-eid-parry-va-tech-ircon-titagarh-results-12-august-2026/article71332017.ece
- Source: Tata Sons’ IPO can take a page from a Hong Kong titan — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/ipos/fpos/tata-sons-ipo-can-take-a-page-from-a-hong-kong-titan/articleshow/133169095.cms
- Source: Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-consumer-share-price-live-updates-11-aug-2026/liveblog/133140823.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
fx · 2 series ↑ (3.52), dyn_coin ↓ (3.18), dyn_tech ↑ (3.09), dyn_hdb ↓ (2.81), usd_cny ↓ (2.79), dyn_cupid_ns ↑ (2.72), dyn_indianb_ns ↑ (2.34), dyn_lth ↑ (2.32), usd_brl ↑ (2.28), dyn_pltr ↑ (2.23), nifty_fmcg ↓ (2.17), dyn_icicigi_bo ↓ (2.09)

## India macro
- nifty_50: 24300.8008 (1d -0.70%, z20 0.05, flag none)
- nifty_midcap_100: 63637.9492 (1d -0.33%, z20 1.18, flag amber)
- usd_inr: 95.4225 (1d 0.03%, z20 -0.84, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6188 (1d 0.37%, z20 2.19, flag red)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · India WPI T-2d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 89.9 — "India’s crude oil imports from the US likely to hit record low in August"
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.5 — "India’s crude oil imports from the US likely to hit record low in August"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.8 — "India’s crude oil imports from the US likely to hit record low in August"
- INDIANB.NS (INDIAN BANK) score 67.9 — "From Gift Nifty to US-Iran war, crude oil prices: 7 key things that changed for Indian sto"
- BAC (Bank of America Corporation) score 55.2 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- HDB (HDFC Bank Limited) score 50.0 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.0 — "HCL Tech Share Price Live Updates: HCL Tech's Trading Performance"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.1 — "HCL Tech Share Price Live Updates: HCL Tech's Trading Performance"
- OHI (Omega Healthcare Investors, In) score 46.9 — "Global Investors Favor Taiwan Over Korea Stocks After AI Selloff"
- COIN (Coinbase Global, Inc.) score 46.6 — "Global Investors Favor Taiwan Over Korea Stocks After AI Selloff"
- IDBI.NS (IDBI BANK LIMITED) score 46.3 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 46.3 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- TECH (Bio-Techne Corp) score 46.1 — "HCL Tech Share Price Live Updates: HCL Tech's Trading Performance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.9 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Stock Details"
- CHKP (Check Point Software Technolog) score 40.8 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 1"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 36.3 — "U.S. SAYS HORMUZ OIL FLOWS ARE RECOVERING Energy Secretary Chris Wright says nearly 9 mill"
- LTH (Life Time Group Holdings, Inc.) score 32.8 — "Dhoot Transmission IPO day 3: Issue subscribed 4 times so far; check latest GMP, issue rev"
- 301077.SZ (CHINASTARS) score 22.7 — "China prepares to mark Jiang Zemin centenary with full commemorative honours"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.4 — "U.S. TREASURY YIELDS SET TO EASE A Reuters poll sees Treasury yields declining over the ne"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.6 — "Manappuram Finance shares jump 3% after Q1 profit soars 4x. Why Jefferies, Morgan Stanley "
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.7 — "Curry Dish, Not Big Mac, Captures Just How Weak Yen Is, BNY Says"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 13.3 — "China's Coal-to-Gas Industry Set to Triple by 2030, Rystad Says"
- JIOFIN.BO (Jio Financial Services Limited) score 13.1 — "Jio Financial Services Share Price Live Updates: Jio Financial Services experiences a mino"
- MS (Morgan Stanley) score 12.1 — "Manappuram Finance shares jump 3% after Q1 profit soars 4x. Why Jefferies, Morgan Stanley "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 11.5 — "Jio Financial Services Share Price Live Updates: Jio Financial Services experiences a mino"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.4 — "Tata Sons’ IPO can take a page from a Hong Kong titan"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.2 — "Lalithaa Jewellery’s ₹1,700 crore IPO opens August 17; price band fixed at ₹190-201"
- NVDA (NVIDIA Corporation) score 9.8 — "NVDA - NVIDIA’S $500 BILLION AI FINANCING PLAN DIVIDES WALL STREET Nvidia unveiled partner"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.8 — "ideaForge Technology shares slide 5% after Q1 gross profit margin falls 49%"
- AAPL (Apple Inc.) score 7.7 — "Apple shares fall amid confusion over 2027 ‘all-glass’ iPhone plans; company clarifies, ‘d"
- META (Meta) score 6.6 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.3 — "QIP fundraising hits one-year high, Adani firms dominate"
- VT (Vanguard Total World Stock Ind) score 6.1 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- INTC (Intel Corporation) score 4.9 — "Intel’s $15 billion stock sale. Why shares fell despite AI boom"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 4.7 — "Tata Sons’ IPO can take a page from a Hong Kong titan"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.1 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- GOOGL (Alphabet) score 3.0 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- PLTR (Palantir Technologies Inc.) score 2.7 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
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