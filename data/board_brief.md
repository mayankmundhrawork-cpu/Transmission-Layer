# Transmission Layer — board brief · 2026-07-27 23:49Z

data as of **2026-07-27** · 98 series · 7 red / 37 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.55, 2d in regime; vol-pct 0.688, breadth-off 0.412, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.45, contra nifty_50 corr20=0.13, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 -0.05, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.489** (n=1147) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3209) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 6.53] commodities · 2 series ↑
- wti [COMMODITIES]: last 82.10, z20 0.70, zc -0.97, resid-z -0.93 [quiet], 1d -8.07%, 1-session move -8.07% ≥ 1.5%
- brent [COMMODITIES]: last 87.93, z20 0.69, zc -1.03, resid-z -1.22 [quiet], 1d -9.14%, 1-session move -9.14% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent decline in crude oil prices, led by a 9.14% drop in Brent and an 8.07% drop in WTI, is attributed to the pause in US-Iran hostilities, which has eased inflation concerns and led to a decrease in US Treasury yields. This move is largely priced, with resid_z values of -0.93 and -1.22 for WTI and Brent, respectively, indicating that the majority of the move can be explained by factor exposures.
- **Gap**: No gap: the decline in oil prices is largely priced, with resid_z values indicating that the majority of the move can be explained by factor exposures
- **India take**: The Indian instruments that express this move are the Nifty Midcap 100 and Nifty 50, which have a negative correlation with WTI and Brent, respectively. These indices have not yet reacted to the decline in oil prices.
- Watch next: nifty_midcap_100 (up) — not yet - watch; negative correlation with WTI
- Watch next: nifty_50 (up) — not yet - watch; negative correlation with Brent
- **India receivers**: nifty_midcap_100 (rho -0.618, z -0.07); nifty_50 (rho -0.461, z -0.51); dyn_jiofin_bo (rho -0.456, z -0.46)
- Source: $100 Oil Puts Big Tech’s $725 Billion AI Bet at Risk — OilPrice, 2026-07-27. https://oilprice.com/Energy/Energy-General/100-Oil-Puts-Big-Techs-725-Billion-AI-Bet-at-Risk.html
- Source: Dollar eases as oil prices fall on pause in Middle East conflict — Mint Markets, 2026-07-27. https://www.livemint.com/market/dollar-eases-as-oil-prices-fall-on-pause-in-middle-east-conflict-11785181650901.html
- Source: US yields decline as oil plunges — Mint Markets, 2026-07-27. https://www.livemint.com/market/us-yields-decline-as-oil-plunges-11785179752035.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.96] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.33, z20 2.03, zc -0.71, resid-z -1.16 [quiet], 1d -0.92%, |z20|=2.03; 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 1.85, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, |z20|=1.85; 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.72, zc -0.44, resid-z -0.72 [quiet], 1d -0.42%, |z20|=1.72; 1y-pct=99
- ust_30y [RATES]: last 5.16, z20 1.38, zc -0.30, resid-z -0.44 [quiet], 1d -0.19%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.79, z20 -1.09, zc 0.45, resid-z 0.09 [quiet], 1d 0.25%, 1y-pct=2
- **Mechanism**: The recent surge in US interest rates and uncertainty about Fed policy outlook have led to a rise in demand for swaptions, indicating growing apprehensions among bond investors. This has resulted in a priced move in US Treasury yields, with the 2-year, 10-year, and 30-year yields increasing. The move is largely explained by factor exposures, with small resid_z values indicating that the move is priced in.
- **Gap**: No gap: The move in US Treasury yields is largely explained by factor exposures, with small resid_z values indicating that the move is priced in.
- **India take**: The Indian 10-year bond yield has logged its biggest plunge in 2 months as the oil rally falters, and may react further to the priced move in US Treasury yields. Indian instruments such as the 10-year GoI bond may see increased demand due to the uncertainty about Fed policy outlook.
- Watch next: ust_2y (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Watch next: tips_10y_real (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Watch next: ust_10y (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Watch next: ust_30y (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Source: JPMORGAN TURNS BULLISH ON STOCKS JPMorgan said its tactical positioning monitor is flashing a buy signal, pointing to further upside for the S&P 500. The bank expects lower bond yields, a weaker dollar, steady Fed policy, and strong earnings to support equities, while warning — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33969
- Source: Bond investors, unsure about Fed policy outlook, hedge against US rate shock — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/bond-investors-unsure-about-fed-policy-outlook-hedge-against-us-rate-shock/articleshow/132665831.cms
- Source: India 10-year bond yield logs biggest plunge in 2 months as oil rally falters — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/india-10-year-bond-yield-logs-biggest-plunge-in-2-months-as-oil-rally-falters/articleshow/132661306.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.65] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 2980.00, z20 3.65, zc -0.39, resid-z -0.87 [quiet], 1d 12.18%, |z20|=3.65
- **Mechanism**: The recent move in dyn_cartrade_ns is likely priced, given its small resid_z of -0.86, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is currently valid, may be a contributing factor to the move, as global copper prices can influence Indian metal equities. However, the lack of a strong correlation between dyn_cartrade_ns and other instruments, such as dow_jones, suggests that the move may be specific to the Indian market.
- **Gap**: No gap: the move in dyn_cartrade_ns is largely explained by factor exposures, with a small resid_z of -0.86, indicating that the price move is priced in.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has already reacted with a 1% gain, snapping a five-session losing streak. Other Indian metal equities, such as those in the metal_copper_channel, may also be affected.
- Watch next: nifty_50 (up) — already moved; broader market momentum
- Source: Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant Raj among top gainers — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-27-july-cartrade-tech-laurus-labs-infosys-atul-tbo-tek-anant-raj-among-top-gainers-11785144447038.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 5.18] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 28036.41, z20 -2.35, zc -0.79, resid-z -1.60 [unexplained], 1d -0.33%, |z20|=2.35
- vix [INDICES]: last 18.67, z20 1.53, zc -0.06, resid-z n/a [quiet], 1d 0.48%, |z20|=1.53
- **Mechanism**: The Nasdaq 100's unexplained move is driven by easing US-Iran tensions, which have improved investor risk appetite, as evidenced by the sharp increase in US stock futures. This risk-on sentiment is likely to propagate through the valid vix_equity_inverse channel, where a vol spike typically leads to an equity drawdown, but in this case, the vol spike is absent, and equities are rising. The metal_copper_channel may also play a role, as global copper leads Indian metal equities, and the improved risk appetite could boost copper prices, which in turn could support Indian metal equities.
- **Gap**: No gap: The Nasdaq 100's move is largely priced, with a resid_z of -1.6, indicating that the majority of the move can be explained by factor exposures, and the remaining unexplained component is not unusually large.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react positively to the improved risk appetite and potential boost to copper prices. However, it has not yet reacted, and its response is worth watching.
- Watch next: nifty_50 (up) — not yet - watch; Improved risk appetite and potential boost to copper prices
- Source: US stock market today: S&P 500, Nasdaq futures jump up to 1.7% as oil prices tumble on easing US-Iran tensions — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-jump-up-to-1-7-as-oil-prices-tumble-on-easing-us-iran-tensions-11785151956723.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market opens higher as pause in US-Iran hostilities lifts sentiment — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market edges lower as chip stocks tumble ahead of earnings session — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Historical analogues: 2026-05-04 (d=0.12), 2025-10-23 (d=0.14), 2026-05-20 (d=0.14)

### [RED 5.18] dyn_lth ↑
- dyn_lth [EQUITIES]: last 43.75, z20 3.18, zc 0.45, resid-z -0.11 [quiet], 1d 3.35%, |z20|=3.18; 1y-pct=100
- **Mechanism**: The recent increase in dyn_lth, a measure of long-term market sentiment, has not been accompanied by a significant unexplained component, as evidenced by a resid_z of -0.11, suggesting that the move is largely priced in. The valid vix_equity_inverse channel indicates that a vol spike would lead to an equity drawdown, but the current regime is neutral, which may limit the impact of this channel. The metal_copper_channel, which is also valid, could potentially influence Indian metal equities.
- **Gap**: No gap: the move in dyn_lth is largely explained by its factor exposures, with a small resid_z indicating that the price move is priced in
- **India take**: The Indian instrument that may express this move is the Nifty 50, which has not yet reacted. The metal_copper_channel could also influence Indian metal equities such as Hindalco or Tata Steel.
- Watch next: nifty_50 (down) — not yet - watch; potential risk-off sentiment
- Source: ‘Time will tell whether that was a good bet’: My adviser got me a full SpaceX IPO allocation. Was I lucky? — MarketWatch Top, 2026-07-27. https://www.marketwatch.com/story/time-will-tell-whether-that-was-a-good-bet-my-adviser-got-me-a-full-spacex-ipo-allocation-was-i-lucky-7f319645?mod=mw_rss_topstories
- Source: Trump: I have a lot of patience, plenty of time — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33953
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 4.95] dxy ↑
- dxy [FX]: last 101.51, z20 1.95, zc 0.12, resid-z 0.23 [quiet], 1d 0.04%, 20d range extreme; |z20|=1.95; 1y-pct=99
- **Mechanism**: The recent surge in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a decline in gold prices. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which could support gold prices. The VALID metal_copper_channel may also influence Indian metal equities.
- **Gap**: No gap: The DXY move is largely priced, with a small resid_z of -0.69, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that may express this move is the MCX Gold, which may decline if the gold_silver_comove channel dominates. However, the reaction is yet to be seen.
- Watch next: comex_gold (down) — not yet - watch; Historically leads DXY by 3 days
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.48] dyn_infy ↑
- dyn_infy [EQUITIES]: last 11.75, z20 2.48, zc 1.47, resid-z 1.60 [unexplained], 1d 5.76%, |z20|=2.48
- **Mechanism**: dyn_infy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.561 via dyn_infy, leads 1d, z 1.49, reacted); dyn_techm_ns (rho 0.542 via dyn_infy, leads 1d, z 1.45, reacted); dyn_tataelxsi_ns (rho 0.384 via dyn_infy, z -0.48, quiet)
- **India receivers**: nifty_it (rho 0.561, z 1.49); dyn_techm_ns (rho 0.542, z 1.45); dyn_tataelxsi_ns (rho 0.384, z -0.48)
- Source: Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-hdfc-bank-infosys-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132660092.cms
- Source: Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant Raj among top gainers — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-27-july-cartrade-tech-laurus-labs-infosys-atul-tbo-tek-anant-raj-among-top-gainers-11785144447038.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

### [RED 3.99] indices · 3 series ↑
- ftse_100 [INDICES]: last 10801.15, z20 2.68, zc 1.14, resid-z 0.74 [quiet], 1d 0.60%, |z20|=2.68; 1y-pct=98
- dax [INDICES]: last 25426.61, z20 1.01, zc 1.32, resid-z 1.09 [quiet], 1d 1.31%, 1y-pct=98
- stoxx_50 [INDICES]: last 6297.21, z20 0.18, zc 1.08, resid-z 0.75 [quiet], 1d 0.26%, 1y-pct=96
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.588 via stoxx_50, z -0.07, quiet); nifty_50 (rho 0.566 via dax, z -0.51, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.684 vs ftse_100, historically leads by 3d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.6 vs dax, historically leads by 5d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.535 vs ftse_100, historically leads by 5d
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.573 vs dax
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.566 vs dax
- **India receivers**: nifty_midcap_100 (rho 0.588, z -0.07); nifty_50 (rho 0.566, z -0.51)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2025-12-01 (d=0.45)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (3.93), dyn_hdb ↓ (3.75), nikkei_225 ↓ (3.66), natgas ↓ (3.63), dyn_bac ↑ (3.55), dyn_301077_sz ↓ (3.39), gold_silver_ratio ↑ (3.27), usd_inr ↑ (3.08), commodities · 2 series ↑ (2.95), dyn_tech ↑ (2.8), asx_200 ↑ (2.74), dyn_hdbfs_bo ↓ (2.55)

## India macro
- nifty_50: 24003.6504 (1d 0.99%, z20 -0.51, flag none)
- nifty_midcap_100: 62286.1484 (1d 0.98%, z20 -0.07, flag none)
- usd_inr: 96.5673 (1d -0.32%, z20 1.08, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5949 (1d -0.01%, z20 0.47, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 66.7 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- INOXINDIA.NS (INOX INDIA LIMITED) score 58.1 — "Crude tumbles as US-Iran pause eases pressure, but risks to India’s oil supply remain"
- BAC (Bank of America Corporation) score 57.1 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- HDB (HDFC Bank Limited) score 56.2 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 53.7 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- IDBI.NS (IDBI BANK LIMITED) score 51.2 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 46.1 — "Crude tumbles as US-Iran pause eases pressure, but risks to India’s oil supply remain"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.4 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends mixed as investors focus "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.0 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.0 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends mixed as investors focus "
- COIN (Coinbase Global, Inc.) score 38.8 — "AMZN - AMAZON: LEO WILL PARTNER WITH MOBILE NETWORK OPERATORS TO EXTEND MOBILE CONNECTIVIT"
- COALINDIA.NS (COAL INDIA LTD) score 36.9 — "Crude tumbles as US-Iran pause eases pressure, but risks to India’s oil supply remain"
- OHI (Omega Healthcare Investors, In) score 25.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends mixed as investors focus "
- BOND (PIMCO Active Bond Exchange-Tra) score 22.5 — "JPMORGAN TURNS BULLISH ON STOCKS JPMorgan said its tactical positioning monitor is flashin"
- LTH (Life Time Group Holdings, Inc.) score 19.6 — "Trump: I have a lot of patience, plenty of time"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.8 — "MACQUARIE SEES CHINA TAPPING OIL STOCKPILES Macquarie said China's state-owned refiners co"
- CHKP (Check Point Software Technolog) score 13.8 — "Cube Highways Trust InvIT IPO: Focus shifts to allotment date. Latest GMP, step-by-step gu"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.0 — "Tata Power board okays raising Rs 4,500 cr via NCDs"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.0 — "Global markets: Shein will struggle to justify up to $50 billion Hong Kong IPO valuation"
- INFY (Infosys Limited) score 9.8 — "Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant"
- VT (Vanguard Total World Stock Ind) score 8.4 — "TRUMP ON FED: WE SHOULD HAVE WORLD'S LOWEST INTEREST RATE"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.3 — "Adani Energy launches Rs 3,500 crore QIP, sets floor price at Rs 1,698 per share"
- JIOFIN.BO (Jio Financial Services Limited) score 8.3 — "AMZN - AMAZON: LEO WILL PARTNER WITH MOBILE NETWORK OPERATORS TO EXTEND MOBILE CONNECTIVIT"
- MS (Morgan Stanley) score 7.5 — "MORGAN STANLEY RAISES ISM FORECAST Morgan Stanley lifted its July ISM Manufacturing PMI fo"
- TECH (Bio-Techne Corp) score 7.3 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends mixed as investors focus "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.1 — "Q1 Results Today Highlights: BEL & Canara Bank Q1 PAT up, P N Gadgil PAT jumps 51%, HUDCO "
- META (Meta) score 6.8 — "More cracks emerge in AI-related bonds as Meta, Microsoft earnings loom"
- GS (Goldman Sachs Group, Inc. (The) score 6.7 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.4 — "From financials to industrials: Here's how Nifty 500 composition has shifted over the year"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.9 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- NVDA (NVIDIA Corporation) score 4.9 — "Nvidia’s potential new deal with OpenAI would revive a spooky tech-bubble habit, analyst w"
- ETERNAL.NS (ETERNAL LIMITED) score 3.9 — "Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex "
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.9 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- PCJEWELLER.NS (PC JEWELLER LTD) score 3.1 — "Sebi clears IPOs of Intellius Recode, Nityas Gems & Jewellery"
- 301077.SZ (CHINASTARS) score 2.9 — "MACQUARIE SEES CHINA TAPPING OIL STOCKPILES Macquarie said China's state-owned refiners co"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 2.7 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- AAPL (Apple Inc.) score 1.7 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 1.6 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.5 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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