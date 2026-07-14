# Transmission Layer — board brief · 2026-07-14 08:32Z

data as of **2026-07-14** · 92 series · 10 red / 30 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.456, 6d in regime; vol-pct 0.662, breadth-off 0.25, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.23, corr60 -0.44, contra nifty_50 corr20=0.4, last shift 2026-05-19. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.47, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 0.01, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.25, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 82** scanned series survive multiplicity control (effective p ≤ 0.0009001744811842904)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.569, β -0.447, p 0.0); driver zc 3.23 → expected -1.326%. Type hit-rate 0.815 (n=2399).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.4, β 0.2426, p 0.0); driver zc 3.23 → expected 0.719%. Type hit-rate 0.815 (n=2399).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.367, β -0.2446, p 0.0); driver zc 3.23 → expected -0.725%. Type hit-rate 0.815 (n=2399).
- Track record · residual_reversion: hit-rate **0.481** (n=1085) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2399) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.04] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 764.65, z20 7.04, zc 5.91, resid-z 12.22 [unexplained], 1d 12.86%, |z20|=7.04
- **Mechanism**: The surge in Just Dial's stock price is driven by its strong Q1 FY27 earnings report, which has prompted brokerages to turn bullish, citing revenue growth, healthy cash reserves, and improving business fundamentals. This has led to a significant increase in the stock's price, with some brokerages seeing up to 62% upside. The move is unexplained by factor exposures, with a high resid_z of 12.22, indicating that the stock's price movement is not fully accounted for by its underlying factors.
- **Gap**: No gap: the big raw move in Just Dial's stock price is largely priced in, given the strong earnings report and bullish brokerage views
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react negatively to the risk-off sentiment, although it has not yet done so. The metal_copper_channel, which is a valid channel, may also be impacted, given the global copper leads Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in the Nifty 50
- Source: Just Dial shares rocket 36% in two days! Why Citi, Kotak, others think Reliance-backed stock can rally up to 62%? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-36-in-two-days-why-citi-kotak-others-think-reliance-backed-stock-can-rally-up-to-62/articleshow/132382158.cms
- Source: Just Dial share price skyrockets 17% on strong Q1 results, new CEO, CFO announcement. Do you own? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/just-dial-share-price-skyrockets-17-on-strong-q1-results-new-ceo-cfo-announcement-do-you-own-11783922394287.html
- Source: Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-14-as-profit-rises-to-rs-166-crore-revenue-grows-10-yoy/articleshow/132356592.cms
- Historical analogues: 2026-06-18 (d=0.19), 2025-06-30 (d=0.52), 2026-01-07 (d=0.52)

### [RED 8.59] commodities · 2 series ↑
- brent [COMMODITIES]: last 85.91, z20 2.76, zc 1.24, resid-z 0.01 [quiet], 1d 3.13%, 1-session move +3.13% ≥ 1.5%; |z20|=2.76; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 80.11, z20 2.16, zc 1.03, resid-z -0.13 [quiet], 1d 2.52%, 1-session move +2.52% ≥ 1.5%; |z20|=2.16
- **Mechanism**: The recent surge in oil prices, driven by geopolitical tensions and supply disruptions, has led to a rise in Brent and WTI prices, with both commodities experiencing quiet moves despite significant 1-session gains of +3.13% and +2.52%, respectively. The small resid_z values of 0.01 and -0.13 for Brent and WTI, respectively, indicate that the moves are largely priced in, given the current factor exposures. The valid metal_copper_channel and gold_silver_comove channels may facilitate the transmission of this move to Indian metal equities and other correlated instruments.
- **Gap**: No gap: the small resid_z values indicate that the oil price moves are largely priced in, given the current factor exposures.
- **India take**: The Indian instrument nifty_midcap_100 has already reacted to the WTI price surge, and further moves in Indian metal equities may be influenced by the valid metal_copper_channel. The rise in oil prices may also impact India's inflation and interest rate risks, as reflected in the decline of Indian government bonds.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price surge
- **India receivers**: nifty_midcap_100 (rho -0.516, z 1.18)
- Source: Iran Sneaks 12 Million Barrels Past Renewed U.S. Oil Blockade — OilPrice, 2026-07-14. https://oilprice.com/Latest-Energy-News/World-News/Iran-Sneaks-12-Million-Barrels-Past-Renewed-US-Oil-Blockade.html
- Source: China’s Crude Oil Imports Crash to Decade Low as Hormuz Crisis Bites — OilPrice, 2026-07-14. https://oilprice.com/Latest-Energy-News/World-News/Chinas-Crude-Oil-Imports-Crash-to-Decade-Low-as-Hormuz-Crisis-Bites.html
- Source: India bonds join global rout after Mideast escalation jolts oil higher — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/india-bonds-join-global-rout-after-mideast-escalation-jolts-oil-higher/articleshow/132382258.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.43] usd_inr ↑
- usd_inr [FX]: last 96.14, z20 2.43, zc 1.83, resid-z 1.23 [moved], 1d 0.85%, 20d range extreme; |z20|=2.43; 1y-pct=98; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The USD-INR move is driven by the recent escalation of US-Iran tensions, which has led to a surge in crude oil prices, putting pressure on the Indian rupee. This is reflected in the weak inr_oil_channel, which is normally expected to transmit oil price shocks to the rupee. However, the current move is largely priced, given the relatively small resid_z of 1.23, indicating that the move is mostly explained by factor exposures.
- **Gap**: No gap: The current USD-INR move is largely priced, with a small resid_z and a high z20 level, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the EUR-INR, which has already reacted with a rho of 0.381 via USD-INR. The Nifty 50 has also responded to the risk-off sentiment, with a decline in its value.
- Watch next: nifty_50 (down) — already moved; Risk-off sentiment due to US-Iran tensions
- **India receivers**: eur_inr (rho 0.381, z 1.29)
- Source: Iran jitters, Rupee slide keep Sensex, Nifty under pressure; HCL Tech, HDFC Life lead losses — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/stock-markets/iran-jitters-rupee-slide-keep-sensex-nifty-under-pressure-hcl-tech-hdfc-life-lead-losses/article71220380.ece
- Source: Rupee breaches 96 as Trump’s Iran escalation sends crude soaring — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/forex/rupee-breaches-96-as-trumps-iran-escalation-sends-crude-soaring/article71219940.ece
- Source: Rupee drops past 96 as oil prices climb on renewed US-Iran tensions — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/forex/rupee-drops-past-96-per-dollar-as-oil-prices-climb-on-renewed-us-iran-tensions/article71219838.ece
- Historical analogues: 2024-11-06 (d=0.01), 2024-10-24 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.45] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 90.93, z20 -2.52, zc -0.27, resid-z 0.14 [quiet], 1d -0.40%, |z20|=2.52; 1y-pct=1
- tips_10y_real [RATES]: last 2.32, z20 1.79, zc 0.24, resid-z 0.27 [quiet], 1d 0.43%, |z20|=1.79; 1y-pct=100
- ust_30y [RATES]: last 5.06, z20 1.74, zc 0.27, resid-z 0.32 [quiet], 1d 0.20%, |z20|=1.74; 1y-pct=97
- ust_10y [RATES]: last 4.56, z20 1.64, zc 0.44, resid-z 0.56 [quiet], 1d 0.44%, |z20|=1.64; 1y-pct=96
- ust_2y [RATES]: last 4.21, z20 1.40, zc 0.93, resid-z 1.21 [quiet], 1d 1.20%, 1y-pct=99
- **Mechanism**: The recent rise in global bond yields, driven by Middle East tensions and inflation concerns, is transmitting to the Indian market through the global duration channel. This is evident from the increase in yields of US Treasury bonds, such as ust_30y and ust_10y, which are correlated with the Indian government bond yields. The rise in bond yields is also influencing monetary policy expectations, leading to a potential increase in borrowing costs for businesses and individuals.
- **Gap**: No gap: The current move in bond yields is largely priced in, with low resid_z values for dyn_bond and other correlated instruments.
- **India take**: The Indian 10-year government bond yield is likely to increase in response to the global bond yield rise, which may impact the Indian stock market, particularly the Nifty and Sensex. However, the Indian market has not yet reacted significantly to this development.
- Watch next: dyn_bond (down) — not yet - watch; The dyn_bond has a low resid_z of 0.14, indicating that the current move is largely priced in.
- Watch next: tips_10y_real (up) — already moved; The tips_10y_real has a high z20 score of 1.79, indicating a significant move.
- Source: SBI raises $200 million through bond tap in — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/sbi-raises-200-million-through-bond-tap-in/articleshow/132385450.cms
- Source: Global Market: UK bond yields hit one-month high as Middle East tensions boost rate-hike expectations — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-uk-bond-yields-hit-one-month-high-as-middle-east-tensions-boost-rate-hike-expectations/articleshow/132383109.cms
- Source: Global Market: Eurozone bond yields climb as Middle East tensions rekindle inflation concerns — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-climb-as-middle-east-tensions-rekindle-inflation-concerns/articleshow/132362710.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.6] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 527.05, z20 3.60, zc 0.37, resid-z 1.19 [quiet], 1d 3.21%, |z20|=3.60
- **Mechanism**: dyn_kalyankjil_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-07 (z-distance 1.76).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.56 via dyn_kalyankjil_ns, z 1.18, reacted); dyn_indianb_ns (rho 0.485 via dyn_kalyankjil_ns, z -0.03, quiet); dyn_pcjeweller_ns (rho 0.444 via dyn_kalyankjil_ns, z 1.3, reacted); nifty_50 (rho 0.403 via dyn_kalyankjil_ns, z -0.04, quiet); dyn_swiggy_ns (rho 0.389 via dyn_kalyankjil_ns, z 0.52, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.56, z 1.18); dyn_indianb_ns (rho 0.485, z -0.03); dyn_pcjeweller_ns (rho 0.444, z 1.3); nifty_50 (rho 0.403, z -0.04)
- Source: Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. Time to buy or book profits? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/kalyan-jewellers-shares-skyrocket-50-in-5-days-market-value-swells-by-rs-18200-crore-time-to-buy-or-book-profits/articleshow/132382065.cms
- Source: Top Gainers & Losers on 13 July: Newgen Software, Kalyan Jewellers, TCS, Voltas, Paytm, Bajaj Auto among top gainers — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-13-july-newgen-software-kalyan-jewellers-tcs-voltas-paytm-bajaj-auto-among-top-gainers-11783936105519.html
- Source: Kalyan Jewellers shares surge 12%, jump 50% in just 4 sessions; is there more steam left? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/kalyan-jewellers-shares-surge-almost-10-jump-47-in-just-4-sessions-is-there-more-steam-left-11783922565597.html
- Historical analogues: 2026-01-07 (d=1.76), 2026-06-15 (d=1.78), 2025-07-02 (d=2.84)

### [RED 4.73] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.24, z20 -2.73, zc 0.30, resid-z 0.18 [quiet], 1d -10.51%, |z20|=2.73
- **Mechanism**: dyn_qessf ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho -0.366 via dyn_qessf, z 0.99, quiet)
- **India receivers**: dyn_atherenerg_ns (rho -0.366, z 0.99)
- Source: FRANCE'S MACRON: UKRAINE HAS AGREED TO BUY SAMP-T AIR DEFENCE SYSTEM — DeItaone, 2026-07-13. https://t.me/walter_bloomberg/33611
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 4.69] natgas ↓
- natgas [COMMODITIES]: last 2.88, z20 -2.69, zc -0.13, resid-z -0.91 [quiet], 1d -0.52%, |z20|=2.69
- **Mechanism**: The decline in natgas prices may propagate through the metal_copper_channel, as a decrease in energy costs can lead to an increase in industrial activity, which in turn can drive up demand for copper and other metals. However, the current move in natgas is largely priced, with a resid_z of -0.91, indicating that the unexplained component is relatively small. The valid gold_silver_comove channel may also play a role, as a decrease in energy costs can lead to a decrease in production costs for gold and silver, potentially driving up their prices.
- **Gap**: No gap: the current move in natgas is largely priced, with a small resid_z and a low r2 value, indicating that the price move is mostly explained by factor exposures
- **India take**: The Indian instrument that expresses this move is likely to be the copper futures contract on the MCX, which may react positively to the decrease in energy costs. However, the reaction has not yet occurred, and the market is still watching for a potential move.
- Watch next: copper (up) — not yet - watch; decrease in energy costs can drive up demand for copper
- Source: Why the UAE Is Taking a Bigger Piece of America’s LNG Crown Jewel — OilPrice, 2026-07-13. https://oilprice.com/Energy/Natural-Gas/Why-the-UAE-Is-Taking-a-Bigger-Piece-of-Americas-LNG-Crown-Jewel.html
- Source: EU's Russian LNG Imports Hit Record High Ahead of 2027 Ban — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/EUs-Russian-LNG-Imports-Hit-Record-High-Ahead-of-2027-Ban.html
- Source: U.S. POWER COSTS SURGE TO MULTI-YEAR HIGHS Natural gas power costs hit $90 per megawatt-hour in 2026—the highest level in at least 17 years—as data-center demand accelerates. Solar and onshore wind costs also jumped more than 10%, reaching their highest levels since at least — DeItaone, 2026-07-13. https://t.me/walter_bloomberg/33579
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.43] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.43, zc n/a, resid-z n/a [quiet], 1d 0.02%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z-score of 1.64, indicating a potential mean reversion. This ratio is derived from the relative performance of midcap and largecap stocks, and its extreme value may signal a reversal in the market trend. The historical analogues suggest a mixed outcome for various assets, with the S&P 500 showing a positive median return, while the high-yield OAS shows a negative median return.
- **Gap**: No gap: the nifty_midcap_100 has already reacted to the extreme midcap_largecap_ratio, with a z-score of 1.59, indicating that the Indian market has likely priced in the event
- **India take**: The Nifty Midcap 100 index, with a correlation of 0.516 with the midcap_largecap_ratio, has likely expressed this move and may be due for a correction. The Indian market may see a pullback in midcap stocks, as indicated by the high z-score of the nifty_midcap_100
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.54, z 1.18); dyn_kalyankjil_ns (rho 0.38, z 3.6); dyn_indianb_ns (rho 0.361, z -0.03); dyn_swiggy_ns (rho 0.358, z 0.52)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_meta ↑ (4.37), dyn_cartrade_ns ↑ (4.18), commodities · 2 series ↑ (3.97), gold_silver_ratio ↑ (3.83), cross-asset · 2 series ↑ (3.63), dyn_cupid_ns ↑ (3.51), dyn_adanient_bo ↑ (3.46), brent_wti_spread ↑ (3.32), eur_usd ↓ (2.47), dxy ↑ (2.4), dyn_coin ↓ (2.24), sofr ↓ (2.19)

## India macro
- nifty_50: 24067.1992 (1d -0.59%, z20 -0.04, flag none)
- nifty_midcap_100: 62698.1016 (1d -0.58%, z20 1.18, flag amber)
- usd_inr: 96.1400 (1d 0.85%, z20 2.43, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6051 (1d 0.02%, z20 1.43, flag amber)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-1d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 37.6 — "India to invest in foreign uranium mines"
- COIN (Coinbase Global, Inc.) score 37.0 — "Global Market Update | SK Hynix set to gain as South Korea eases capital-raising rules"
- HDB (HDFC Bank Limited) score 28.8 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Market Movement"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 26.8 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Market Movement"
- INDIANB.NS (INDIAN BANK) score 25.9 — "Gift Nifty, US-Iran war, crude oil prices to India inflation: 10 things that changed for I"
- CHKP (Check Point Software Technolog) score 18.2 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 1"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 13.2 — "Stocks to watch: Tata Elxsi, HCL Tech, BEL among shares in focus today; check list here"
- SKHYV (SK hynix Inc. American Deposit) score 12.5 — "Global Market Update | SK Hynix set to gain as South Korea eases capital-raising rules"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 12.1 — "Global Emissions Hit Another Record High Despite Clean Energy Boom"
- BOND (PIMCO Active Bond Exchange-Tra) score 11.9 — "ETMarkets Smart Talk | Equity, mutual funds, bonds or property: Tax rules every NRI should"
- VT (Vanguard Total World Stock Ind) score 9.4 — "Fifa World Cup semi-finalists Argentina pledge donations to China flood victims"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.2 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 8.5 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- META (Meta) score 5.1 — "Rekha Jhunjhunwala likely exits this smallcap metal stock after 90% rally in 1 year. Do yo"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.7 — "FRANCE'S MACRON: UKRAINE HAS AGREED TO BUY SAMP-T AIR DEFENCE SYSTEM"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.7 — "The great Adani trade is back with Rs 1.4 lakh crore bang! Why Adani Enterprises is Nifty’"
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.7 — "Why Vijay Kedia just bet on this small-cap mining stock"
- MU (Micron Technology, Inc.) score 3.6 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- CUPID.NS (CUPID LIMITED) score 3.5 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- SWIGGY.NS (SWIGGY LIMITED) score 3.5 — "Swiggy shares slide over 2% after FSSAI issues 9 notices over consumer complaints"
- MS (Morgan Stanley) score 3.2 — "MORGAN STANLEY EXPECTS US HYPERSCALER CAPEX TO REACH $1.2 TRLN BY 2027 MORGAN STANLEY EXPE"
- GS (Goldman Sachs Group, Inc. (The) score 3.1 — "Goldman Sachs stock picks! RIL, HDFC Bank, Adani Power, among 14 names brokerage is bullis"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 2.9 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- JEF (Jefferies Financial Group Inc.) score 2.4 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.3 — "GE Vernova, Atlanta Electricals among top beneficiaries of India's transmission expansion"
- MCAP (MCAP Inc.) score 2.1 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.6 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- BLK (BlackRock, Inc.) score 1.3 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.3 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 0.9 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 0.8 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 0.7 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.6 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
- WULF (TeraWulf Inc.) score 0.5 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"

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