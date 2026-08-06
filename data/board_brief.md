# Transmission Layer — board brief · 2026-08-06 14:33Z

data as of **2026-08-06** · 98 series · 12 red / 31 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.329, 2d in regime; vol-pct 0.422, breadth-off 0.235, Markov P(high-vol) 0.022)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.42, contra nifty_50 corr20=0.07, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.81, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.33, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.06, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.02, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.32, corr60 -0.26, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.17, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.001472750523107802)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.495, β 0.2704, p 0.0); driver zc -1.53 → expected -0.403%. Type hit-rate 0.829 (n=2684).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.28, β -0.1144, p 0.0); driver zc -1.53 → expected 0.17%. Type hit-rate 0.829 (n=2684).
- Track record · residual_reversion: hit-rate **0.494** (n=1156) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2684) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.25] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4322.20, z20 4.38, zc 0.85, resid-z 1.40 [quiet], 1d 1.80%, |z20|=4.38; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6525.92, z20 2.93, zc 0.84, resid-z 1.19 [quiet], 1d 0.76%, |z20|=2.93; 1y-pct=100
- cac_40 [INDICES]: last 8741.32, z20 2.93, zc 1.06, resid-z 1.53 [unexplained], 1d 0.83%, |z20|=2.93; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.73, z20 2.75, zc 0.19, resid-z 0.37 [quiet], 1d 0.43%, |z20|=2.75; 1y-pct=100; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 54239.52, z20 2.55, zc -0.19, resid-z -0.24 [quiet], 1d -0.20%, |z20|=2.55; 1y-pct=99
- dyn_vt [EQUITIES]: last 160.49, z20 2.28, zc 0.19, resid-z -0.90 [quiet], 1d 0.20%, |z20|=2.28; 1y-pct=100
- comex_silver [COMMODITIES]: last 61.80, z20 2.27, zc -0.17, resid-z -1.71 [unexplained], 1d -0.48%, |z20|=2.27; co-occur[gold_silver] same-direction (channel VALID)
- dax [INDICES]: last 26224.11, z20 2.22, zc 0.46, resid-z 0.63 [quiet], 1d 0.37%, |z20|=2.22; 1y-pct=100
- russell_2000 [INDICES]: last 3030.00, z20 2.20, zc 0.28, resid-z 0.56 [quiet], 1d 0.36%, |z20|=2.20; 1y-pct=99
- sp500 [INDICES]: last 7728.40, z20 2.19, zc 0.06, resid-z 3.71 [unexplained], 1d 0.06%, |z20|=2.19; 1y-pct=99
- dyn_nvda [EQUITIES]: last 219.57, z20 2.05, zc 0.06, resid-z -1.09 [quiet], 1d 0.16%, |z20|=2.05; 1y-pct=96
- **Mechanism**: The current move is driven by a cross-asset event with 11 series showing an upward trend, led by commodities such as gold and copper, and indices like Stoxx 50 and CAC 40. The move is largely priced, with most series having a low resid_z, indicating that the move is explained by factor exposures. However, some series like CAC 40 and S&P 500 have an unexplained component, suggesting potential for further movement.
- **Gap**: No gap: the move is largely priced, with most series having a low resid_z, indicating that the move is explained by factor exposures
- **India take**: The Indian instruments such as Nifty 50, Nifty Midcap 100, and Nifty Metal have already reacted to the global move, with Nifty 50 having a rho of 0.535 with CAC 40. However, Nifty FMCG has not yet reacted, with a rho of -0.525 with Dyn NVDA.
- Watch next: comex_gold (up) — already moved; valid gold_silver_comove channel
- Watch next: stoxx_50 (up) — already moved; 1y-pct=100
- Watch next: cac_40 (up) — already moved; unexplained move with resid_z=1.53
- Watch next: comex_copper (up) — already moved; valid metal_copper_channel
- Watch next: dow_jones (down) — not yet - watch; low resid_z and potential impact from Middle East peace deal
- **India receivers**: nifty_50 (rho 0.535, z 1.73); nifty_fmcg (rho -0.525, z 0.53); nifty_midcap_100 (rho 0.509, z 1.14); nifty_metal (rho 0.47, z 2.31)
- Source: Nasdaq, S&P 500 edge lower as tech shares weigh on markets; investors await Iran deal details — Mint Markets, 2026-08-06. https://www.livemint.com/market/stock-market-news/nasdaq-s-p-500-edge-lower-as-tech-shares-weigh-on-markets-investors-await-iran-deal-details-11786024285864.html
- Source: China Added More Nuclear Power In A Decade Than The Rest Of The World Combined — OilPrice, 2026-08-06. https://oilprice.com/Alternative-Energy/Nuclear-Power/China-Added-More-Nuclear-Power-In-A-Decade-Than-The-Rest-Of-The-World-Combined.html
- Source: US stocks: S&P 500, Nasdaq open lower as tech stocks weigh; MidEast in focus — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-sp-500-nasdaq-open-lower-as-tech-stocks-weigh-mideast-in-focus/articleshow/133007586.cms
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.08), 2025-10-24 (d=1.14)

### [AMBER 5.93] brent ↓
- brent [COMMODITIES]: last 80.88, z20 -0.93, zc 0.49, resid-z 0.61 [quiet], 1d 1.80%, 1-session move +1.80% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The decline in Brent crude oil prices is driven by the discovery of new offshore oil and gas reserves in Angola, which may increase global oil supply and reduce prices. However, the ongoing geopolitical risks in the Middle East, such as the Iran-Oman shipping talks and attacks on Saudi oil tankers, are keeping supply risks high and supporting oil prices. The RISK_ON regime and the VALID metal_copper_channel and gold_silver_comove channels suggest that the oil price move may propagate through the commodities complex.
- **Gap**: No gap: the big raw move in Brent has a relatively small resid_z of 0.61, indicating that the move is largely priced in by factor exposures
- **India take**: The Indian instruments that express this move, such as nifty_midcap_100, dyn_hdbfs_bo, and midcap_largecap_ratio, have already reacted to the decline in Brent crude oil prices. Further moves in these instruments will depend on the ongoing geopolitical developments in the Middle East and their impact on global oil prices.
- Watch next: wti (down) — not yet - watch; historically leads Brent by 5d
- **India receivers**: nifty_midcap_100 (rho -0.451, z 1.14); dyn_hdbfs_bo (rho -0.387, z -1.21); midcap_largecap_ratio (rho -0.378, z -1.66)
- Source: Angola Confirms New Offshore Oil and Gas Reserves With Katambi-2 Well — OilPrice, 2026-08-06. https://oilprice.com/Latest-Energy-News/World-News/Angola-Confirms-New-Offshore-Oil-and-Gas-Reserves-With-Katambi-2-Well.html
- Source: Brent crude tops $80 per barrel  as Hormuz talks, tanker attacks keep supply risks high — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/brent-crude-tops-80-per-barrel-as-hormuz-talks-tanker-attacks-keep-supply-risks-high/articleshow/133007593.cms
- Source: Q1 Results Today Live: LIC, Trent, Apollo Tyres, Emcure Pharma log Q1 PAT growth, Blue Star profit declines, Hero MotoCorp, Lupin, Britannia, Siemens Energy, BOSCH, Kirloskar Oil Engines, Premier Energies to announce Q1 results — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-trent-britannia-siemens-energy-hero-motocorp-lupin-lic-kirloskar-oil-engines-bosch-aegis-logistics-premier-energies-emcure-pharma-blue-star-results-06-august-2026/article71312019.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [AMBER 5.41] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.00, z20 2.09, zc 0.45, resid-z 0.41 [quiet], 1d 0.96%, |z20|=2.09
- nifty_50 [INDICES]: last 24636.00, z20 1.73, zc 0.07, resid-z 0.23 [quiet], 1d 0.05%, |z20|=1.73
- nifty_midcap_100 [INDICES]: last 63324.85, z20 1.14, zc -0.58, resid-z -0.97 [quiet], 1d -0.43%, 1y-pct=98
- **Mechanism**: The move in Indian benchmark indices, led by Reliance Industries and SBI, is driven by easing crude oil prices and the Reserve Bank of India's steady policy stance, which has resulted in selective buying in heavyweight stocks. This move is further supported by the VALID metal_copper_channel and vix_equity_inverse channels. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which may limit the upside. The low resid_z values for nifty_50 and nifty_midcap_100 indicate that the move is largely priced in.
- **Gap**: No gap: the low resid_z values for nifty_50 and nifty_midcap_100 indicate that the move is largely priced in, with no significant unexplained component.
- **India take**: The Indian instruments that express this move are dyn_muthootfin_ns, dyn_bharatcoal_ns, and nifty_metal, which have already reacted to the easing crude oil prices and the Reserve Bank of India's steady policy stance. However, dyn_indusindbk_bo remains quiet and may be worth watching.
- Watch next: dyn_jiofin_bo (up) — already moved; z20 level is high at 2.09
- Watch next: nifty_50 (up) — already moved; z20 level is high at 1.73
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -1.76); dyn_bharatcoal_ns (rho 0.649, z -1.0); dyn_indusindbk_bo (rho 0.625, z -0.6); dyn_indianb_ns (rho 0.6, z 2.61)
- Source: Nifty CAS gap narrows as markets adapt to new system — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/nifty-cas-gap-narrows-as-markets-adapt-to-new-system/article71313875.ece
- Source: Market wrap: Reliance Industries, SBI, Power Grid among top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-reliance-industries-sbi-power-grid-among-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133002408.cms
- Source: Sensex today | Stock Market Highlights: Sensex climbs 374 pts; Nifty ends above 24,600 on RBI, crude oil cues — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-6-august-2026/article71309748.ece
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [AMBER 4.71] cross-asset · 2 series ↑
- usd_jpy [FX]: last 158.18, z20 -1.88, zc 0.60, resid-z 0.63 [quiet], 1d 0.31%, |z20|=1.88
- dyn_amzn [EQUITIES]: last 273.73, z20 1.57, zc 0.19, resid-z -1.63 [unexplained], 1d 0.40%, 1y-pct=98
- **Mechanism**: The recent strengthening of the yen, driven by Japanese investors' return to overseas bonds and foreign investors' return to Japanese long-term bonds, has led to a move in usd_jpy. This, in turn, has correlated with a move in dyn_amzn, potentially due to transmission through global markets. However, the resid_z values suggest that the move in usd_jpy is largely priced, while the move in dyn_amzn is unexplained by factors.
- **Gap**: No gap: the move in usd_jpy is largely priced, and the correlated move in dyn_amzn is unexplained but does not represent a significant event-to-price gap
- **India take**: The Indian transmission candidates, such as dyn_muthootfin_ns and dyn_thangamayl_ns, have already reacted to the move in usd_jpy, while dyn_cartrade_ns remains quiet. Further reaction in Indian markets may be limited due to the priced nature of the usd_jpy move.
- Watch next: dyn_amzn (up) — not yet - watch; unexplained move with high historical hit-rate-up
- **India receivers**: dyn_muthootfin_ns (rho -0.503, z -1.76); dyn_cartrade_ns (rho -0.359, z -0.12); dyn_thangamayl_ns (rho -0.35, z -1.52)
- Source: Japanese investors return to overseas bonds as stronger yen, higher yields boost demand — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/bonds/japanese-investors-return-to-overseas-bonds-as-stronger-yen-higher-yields-boost-demand/articleshow/132980557.cms
- Source: Yen firms after landmark intervention, dollar near lows on optimism over Iran talks — Mint Markets, 2026-08-05. https://www.livemint.com/market/yen-firms-after-landmark-intervention-dollar-near-lows-on-optimism-over-iran-talks-11785963413851.html
- Source: BOFA ANTICIPATE STRONGER JAPANESE YEN FOLLOWING INTERVENTION, CHANGE YEAR END DOLLAR/YEN FORECAST TO 149 FROM 152 - CURRENTLY TRADES AT 157.7 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34369
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [AMBER 4.56] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.18, z20 0.89, zc -1.20, resid-z -0.09 [quiet], 1d -0.96%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.71, z20 -0.66, zc -0.56, resid-z 1.91 [unexplained], 1d -0.17%, 1y-pct=2
- tips_10y_real [RATES]: last 2.40, z20 0.53, zc -0.74, resid-z 0.20 [quiet], 1d -1.23%, 1y-pct=96
- ust_10y [RATES]: last 4.63, z20 0.13, zc -1.53, resid-z -0.59 [priced], 1d -1.49%, 1y-pct=96
- **Mechanism**: The recent move in Indian government bonds, driven by the Reserve Bank of India's dovish stance and falling oil prices, has created a priced move in the 10-year US Treasury yield, which is now transmitting to other assets. The valid gold_silver_comove and metal_copper_channel are indicating a potential rotation into monetary metals and Indian metal equities. However, the weak inr_oil_channel and dxy_inr_channel are limiting the transmission to the Indian rupee and other emerging market currencies.
- **Gap**: No gap: the move in Indian government bonds is largely priced in, with the 10-year yield having decreased by nearly seven basis points since early August.
- **India take**: The Indian 10-year government bond yield is likely to remain stable, with the Reserve Bank of India's dovish stance and falling oil prices supporting the bond market. The Nifty 50 index may see a potential rotation into Indian equities, driven by the transmission from the US Treasury yield.
- Watch next: nifty_50 (up) — not yet - watch; potential rotation into Indian equities
- Source: Profit-taking, debt supply stall India bond rally — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/bonds/profit-taking-debt-supply-stall-india-bond-rally/articleshow/133003162.cms
- Source: RBI policy-led India bond rally continues; Friday's debt sale in focus — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/bonds/rbi-policy-led-india-bond-rally-continues-fridays-debt-sale-in-focus/articleshow/132993202.cms
- Source: Global Market: Japanese bond yields fall as lower oil prices ease inflation concerns — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-fall-as-lower-oil-prices-ease-inflation-concerns/articleshow/132991673.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.46] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1445.00, z20 2.46, zc -0.53, resid-z -0.66 [quiet], 1d -1.75%, |z20|=2.46; 1y-pct=99
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.44] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 157.47, z20 2.44, zc -0.12, resid-z 8.43 [unexplained], 1d -0.61%, |z20|=2.44
- **Mechanism**: dyn_pltr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho 0.394 via dyn_pltr, z 2.46, reacted)
- **India receivers**: dyn_atherenerg_ns (rho 0.394, z 2.46)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [AMBER 4.17] dyn_msft ↑
- dyn_msft [EQUITIES]: last 495.68, z20 2.17, zc 0.45, resid-z 0.46 [quiet], 1d 1.69%, |z20|=2.17
- **Mechanism**: dyn_msft ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_thangamayl_ns (rho -0.379 via dyn_msft, z -1.52, reacted)
- **India receivers**: dyn_thangamayl_ns (rho -0.379, z -1.52)
- Source: OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billion in AI revenue from OpenAI in the year ended June, suggesting the ChatGPT maker accounts for more than half—and possibly around 70%—of its AI business. The figures highlight Microsoft's — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34422
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

## Watchlist (below surfacing floor)
fx · 3 series ↑ (4.01), natgas ↓ (4.01), dyn_bac ↑ (3.82), dyn_coin ↓ (3.53), usd_inr ↓ (3.51), dyn_cupid_ns ↑ (3.48), gold_silver_ratio ↑ (3.26), asx_200 ↑ (2.95), dyn_lth ↑ (2.94), dyn_tech ↑ (2.89), usd_cny ↓ (2.7), dyn_indianb_ns ↑ (2.61)

## India macro
- nifty_50: 24636.0000 (1d 0.05%, z20 1.73, flag amber)
- nifty_midcap_100: 63324.8516 (1d -0.43%, z20 1.14, flag amber)
- usd_inr: 95.2100 (1d 0.12%, z20 -1.51, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5704 (1d -0.47%, z20 -1.66, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-1d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 93.3 — "Profit-taking, debt supply stall India bond rally"
- COALINDIA.NS (COAL INDIA LTD) score 91.4 — "Profit-taking, debt supply stall India bond rally"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.7 — "Profit-taking, debt supply stall India bond rally"
- INDIANB.NS (INDIAN BANK) score 65.6 — "Indian Refiners Continue West Africa Crude Buying Spree"
- COIN (Coinbase Global, Inc.) score 57.2 — "Sensex, Nifty open flat as RBI holds rates, global cues stay mixed"
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.0 — "Dow Jones| Nasdaq | US Stock Market Today | Live: S&P 500, Nasdaq open lower as tech stock"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 56.0 — "Dow Jones| Nasdaq | US Stock Market Today | Live: S&P 500, Nasdaq open lower as tech stock"
- TECH (Bio-Techne Corp) score 52.2 — "Dow Jones| Nasdaq | US Stock Market Today | Live: S&P 500, Nasdaq open lower as tech stock"
- OHI (Omega Healthcare Investors, In) score 51.2 — "Datadog’s stock slides after earnings. This is what’s nagging at investors."
- BAC (Bank of America Corporation) score 44.5 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- HDB (HDFC Bank Limited) score 43.6 — "HDFC Securities initiates coverage on Sona BLW with 'Add'; sees upside on EV-led growth"
- IDBI.NS (IDBI BANK LIMITED) score 41.5 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.5 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.2 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.2 — "MV Electrosystems close 47% over IPO price, Juniper Green Energy settles with 15% listing "
- LTH (Life Time Group Holdings, Inc.) score 34.4 — "Quote of the day by Peter Lynch: "Maybe you’re right 5 or 6 times out of 10. But if your w"
- CHKP (Check Point Software Technolog) score 31.8 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 6"
- 301077.SZ (CHINASTARS) score 28.2 — "China Added More Nuclear Power In A Decade Than The Rest Of The World Combined"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.5 — "Profit-taking, debt supply stall India bond rally"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.2 — "Swiggy shares jump nearly 3% as company targets Rs 10,000 crore adjusted EBITDA by FY31"
- MS (Morgan Stanley) score 14.0 — "Somebody will disrupt the market! Why JPMorgan CEO Jamie Dimon is raising alarm over high "
- JIOFIN.BO (Jio Financial Services Limited) score 13.6 — "Can Tips Music's Rs 44 crore share buyback boost its share price? Here's what JM Financial"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.3 — "Can Tata Sons stay unlisted? Here's what RBI Governor Sanjay Malhotra said"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.9 — "Can Tips Music's Rs 44 crore share buyback boost its share price? Here's what JM Financial"
- VT (Vanguard Total World Stock Ind) score 8.9 — "China Added More Nuclear Power In A Decade Than The Rest Of The World Combined"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.6 — "Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.4 — "Top Gainers & Losers on 6 August: Navin Fluorine, Tata Tech, HAL, Pine Labs, Kalyan Jewell"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Trading Status"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.9 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- PLTR (Palantir Technologies Inc.) score 7.1 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 7.1 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- NVDA (NVIDIA Corporation) score 6.5 — "NVDA - NVIDIA SHARES HIT HIGHEST IN OVER TWO MONTHS, LAST UP 4.3%"
- META (Meta) score 6.1 — "META AI MODEL ACCESSED INTERNET, HACKED A COMPANY: INFORMATION"
- MSFT (Microsoft Corporation) score 5.8 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.6 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- AAPL (Apple Inc.) score 5.3 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- INFY (Infosys Limited) score 4.7 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "GOLDMAN STICKS TO PAYROLL FORECAST Goldman Sachs maintained its 75,000 July nonfarm payrol"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.2 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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