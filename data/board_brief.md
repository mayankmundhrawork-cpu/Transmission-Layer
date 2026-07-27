# Transmission Layer — board brief · 2026-07-27 13:46Z

data as of **2026-07-27** · 98 series · 5 red / 38 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.463, 2d in regime; vol-pct 0.574, breadth-off 0.353, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.45, contra nifty_50 corr20=0.14, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 -0.05, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_infy → nifty_it: leads 1d (ccf 0.441, β 0.3345, p 0.0); driver zc 1.5 → expected 1.411%. Type hit-rate 0.82 (n=3081).
- **SETUP** dyn_infy → dyn_techm_ns: leads 1d (ccf 0.279, β 0.2401, p 0.0); driver zc 1.5 → expected 1.013%. Type hit-rate 0.82 (n=3081).
- Track record · residual_reversion: hit-rate **0.486** (n=1152) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=3081) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.27] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.37, z20 3.34, zc 1.08, resid-z 0.05 [quiet], 1d 1.39%, |z20|=3.34; 1y-pct=100
- ust_10y [RATES]: last 4.71, z20 2.25, zc 0.89, resid-z -0.10 [quiet], 1d 0.86%, |z20|=2.25; 1y-pct=100
- tips_10y_real [RATES]: last 2.43, z20 2.16, zc 0.99, resid-z -0.07 [quiet], 1d 1.67%, |z20|=2.16; 1y-pct=100
- ust_30y [RATES]: last 5.17, z20 1.63, zc 0.61, resid-z -0.15 [quiet], 1d 0.39%, |z20|=1.63; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.79, z20 -1.08, zc 0.36, resid-z -0.45 [quiet], 1d 0.28%, 1y-pct=2
- **Mechanism**: The recent drop in oil prices has led to a decrease in bond yields, as evidenced by the plunge in India's 10-year bond yield and the fall in UK bond yields. This move is likely driven by the transmission of global economic trends to domestic markets, particularly through the [VALID] metal_copper_channel and the [VALID] vix_equity_inverse channels. The drop in oil prices has reduced inflationary pressures, leading to a decrease in bond yields.
- **Gap**: No gap: the big raw move in bond yields is largely priced, with small resid_z values indicating that the move is explained by factor exposures
- **India take**: The Indian 10-year bond yield has already reacted to the drop in oil prices, logging its biggest plunge in 2 months. The move is likely to be expressed through the Indian bond market, particularly through the 10-year GoI bond yield.
- Watch next: ust_2y (down) — already moved; oil price drop reduces inflationary pressures
- Source: India 10-year bond yield logs biggest plunge in 2 months as oil rally falters — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/india-10-year-bond-yield-logs-biggest-plunge-in-2-months-as-oil-rally-falters/articleshow/132661306.cms
- Source: For 44 years, this investor held aces in the long-bond game. He just folded. — MarketWatch Top, 2026-07-27. https://www.marketwatch.com/story/for-44-years-this-investor-held-aces-in-the-long-bond-game-he-just-folded-dcd39375?mod=mw_rss_topstories
- Source: UK bond yields fall to one-week low as oil prices retreat — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-fall-to-one-week-low-as-oil-prices-retreat/articleshow/132656598.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 6.82] commodities · 2 series ↑
- brent [COMMODITIES]: last 90.63, z20 0.99, zc -1.03, resid-z -1.21 [quiet], 1d -6.35%, 1-session move -6.35% ≥ 1.5%
- wti [COMMODITIES]: last 84.04, z20 0.96, zc -0.97, resid-z -0.92 [quiet], 1d -5.90%, 1-session move -5.90% ≥ 1.5%
- **Mechanism**: The recent decline in crude oil prices, led by a pause in US strikes on Iran, has triggered a relief rally in Indian markets. This move is priced, as evidenced by the small resid_z values for brent and wti, indicating that the factor exposures have largely explained the move. The valid gold_silver_comove and metal_copper_channel suggest that the monetary metals and copper are co-moving, which may influence the Indian metal equities.
- **Gap**: No gap: the recent move in crude oil prices is largely explained by factor exposures, as indicated by the small resid_z values for brent and wti
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has already reacted with a 0.96 percent gain. The Nifty Midcap 100, which is correlated with brent, is still being watched for a potential move.
- Watch next: nifty_midcap_100 (up) — not yet - watch; Correlated with brent, historically leads by 5d
- Watch next: nifty_50 (up) — already moved; Closed at 23,995.95, up 228.50 points or 0.96 percent
- **India receivers**: nifty_midcap_100 (rho -0.618, z -0.07); nifty_50 (rho -0.465, z -0.52); dyn_jiofin_bo (rho -0.456, z -0.46)
- Source: India’s relief rally: Crude crash, ceasefire lift Sensex, Nifty out of five-day slump — BusinessLine Mkts, 2026-07-27. https://www.thehindubusinessline.com/markets/indias-relief-rally-crude-crash-ceasefire-lift-sensex-nifty-out-of-five-day-slump/article71272641.ece
- Source: Oil prices see largest one-day declines in two months after U.S. and Iran pause strikes — MarketWatch Top, 2026-07-27. https://www.marketwatch.com/story/oil-prices-see-largest-one-day-declines-in-two-months-amid-pause-in-strikes-d819160a?mod=mw_rss_topstories
- Source: US stock market today: S&P 500, Nasdaq futures jump up to 1.7% as oil prices tumble on easing US-Iran tensions — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-jump-up-to-1-7-as-oil-prices-tumble-on-easing-us-iran-tensions-11785151956723.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.65] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 2980.00, z20 3.65, zc -0.39, resid-z -0.86 [quiet], 1d 12.18%, |z20|=3.65
- **Mechanism**: The recent move in dyn_cartrade_ns is likely priced, given its small resid_z of -0.86, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is currently valid, may be a contributing factor to the move, as global copper prices can influence Indian metal equities. However, the lack of a strong correlation between dyn_cartrade_ns and other instruments, such as dow_jones, suggests that the move may be specific to the Indian market.
- **Gap**: No gap: the move in dyn_cartrade_ns is largely explained by factor exposures, with a small resid_z of -0.86, indicating that the price move is priced in.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has already reacted with a 1% gain, snapping a five-session losing streak. Other Indian metal equities, such as those in the metal_copper_channel, may also be affected.
- Watch next: nifty_50 (up) — already moved; broader market momentum
- Source: Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant Raj among top gainers — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-27-july-cartrade-tech-laurus-labs-infosys-atul-tbo-tek-anant-raj-among-top-gainers-11785144447038.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 3.97] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 51.45, z20 1.97, zc 1.15, resid-z -0.02 [quiet], 1d -0.55%, 1y-pct=99
- **Mechanism**: The recent surge in China's ChangXin Memory Technologies (CXMT) has sparked interest in semiconductor stocks globally, potentially influencing Indian markets through the metal_copper_channel, which is VALID with a corr20 of 0.51 and corr60 of 0.35. This channel suggests that global copper prices can lead Indian metal equities, which may be reacting to the broader sentiment shift in the technology sector.
- **Gap**: No gap: The event is a global semiconductor story, and its direct impact on Indian markets is not immediately clear, with resid_z of dyn_ohi being -0.02, indicating the move is largely priced in.
- **India take**: Indian metal equities, such as those in the Nifty Metal index, could potentially react to the global semiconductor story through the metal_copper_channel. However, no immediate reaction has been observed yet.
- Watch next: nifty_50 (up) — not yet - watch; Potential spill-over from China's semiconductor ambitions
- Watch next: hindalco (up) — not yet - watch; As a key metal equity, it may react to global copper price movements
- Source: Explainer: Why investors are betting big on China’s chipmaker CXMT — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/explainer-why-investors-are-betting-big-on-chinas-chipmaker-cxmt/articleshow/132654124.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [AMBER 3.9] dyn_bac ↑
- dyn_bac [EQUITIES]: last 62.67, z20 1.90, zc 0.85, resid-z -0.26 [quiet], 1d 1.01%, 1y-pct=100
- **India receivers**: nifty_fmcg (rho 0.352, z 0.63)

### [AMBER 3.83] nasdaq_100 ↓
- nasdaq_100 [INDICES]: last 28310.83, z20 -1.83, zc -0.77, resid-z 0.27 [quiet], 1d 0.62%, |z20|=1.83
- **Mechanism**: nasdaq_100 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.926 vs nasdaq_100
- Watch next: sp500 (co-move) — not yet - watch; rho 0.91 vs nasdaq_100
- Watch next: vix (inverse) — not yet - watch; rho -0.78 vs nasdaq_100
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.766 vs nasdaq_100
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.696 vs nasdaq_100
- Source: US stock market today: S&P 500, Nasdaq futures jump up to 1.7% as oil prices tumble on easing US-Iran tensions — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-jump-up-to-1-7-as-oil-prices-tumble-on-easing-us-iran-tensions-11785151956723.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market opens higher as pause in US-Iran hostilities lifts sentiment — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.0), 2025-10-07 (d=0.02)

### [AMBER 3.81] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.14, z20 -1.81, zc 0.32, resid-z 0.71 [quiet], 1d -0.45%, 1y-pct=1
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.626 via dyn_hdb, z -0.52, quiet); nifty_midcap_100 (rho 0.483 via dyn_hdb, z -0.07, quiet); dyn_jiofin_bo (rho 0.464 via dyn_hdb, z -0.46, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.626 vs dyn_hdb, historically leads by 1d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.511 vs dyn_hdb, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.559 vs dyn_hdb
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.527 vs dyn_hdb
- **India receivers**: nifty_50 (rho 0.626, z -0.52); nifty_midcap_100 (rho 0.483, z -0.07); dyn_jiofin_bo (rho 0.464, z -0.46)
- Source: Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-hdfc-bank-infosys-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132660092.cms
- Source: Mcap of nine of top-10 most valued firms erodes by Rs 2.74 lakh cr; HDFC Bank takes biggest hit — BusinessLine Mkts, 2026-07-26. https://www.thehindubusinessline.com/markets/mcap-of-nine-of-top-10-most-valued-firms-erodes-by-rs-274-lakh-cr-hdfc-bank-takes-biggest-hit/article71268854.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 3.76] indices · 3 series ↑
- ftse_100 [INDICES]: last 10781.64, z20 2.44, zc 1.17, resid-z 0.76 [quiet], 1d 0.40%, |z20|=2.44; 1y-pct=98
- dax [INDICES]: last 25503.16, z20 1.26, zc 1.29, resid-z 1.05 [quiet], 1d 1.64%, 1y-pct=98
- stoxx_50 [INDICES]: last 6341.03, z20 0.98, zc 1.08, resid-z 0.74 [quiet], 1d 0.96%, 1y-pct=98
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.588 via stoxx_50, z -0.07, quiet); nifty_50 (rho 0.57 via dax, z -0.52, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.684 vs ftse_100, historically leads by 3d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.6 vs dax, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.561 vs stoxx_50, historically leads by 5d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.535 vs ftse_100, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.531 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.588, z -0.07); nifty_50 (rho 0.57, z -0.52)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2025-12-01 (d=0.45)

## Watchlist (below surfacing floor)
nikkei_225 ↓ (3.66), commodities · 3 series ↑ (3.46), gold_silver_ratio ↑ (3.11), asx_200 ↑ (2.74), dyn_gs ↑ (2.65), dyn_hdbfs_bo ↓ (2.55), dyn_icicigi_bo ↓ (2.54), usd_cny ↓ (2.51), usd_jpy ↑ (2.42), dow_jones ↑ (2.4), dyn_havells_ns ↑ (2.4), dyn_lth ↑ (2.4)

## India macro
- nifty_50: 24003.6504 (1d 0.91%, z20 -0.52, flag none)
- nifty_midcap_100: 62286.1484 (1d 0.98%, z20 -0.07, flag none)
- usd_inr: 95.9000 (1d -1.01%, z20 0.11, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5949 (1d 0.07%, z20 0.48, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 64.9 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- INOXINDIA.NS (INOX INDIA LIMITED) score 60.8 — "India's next commodity cycle could be driven by scrap as organised metal recycling gains m"
- HDB (HDFC Bank Limited) score 54.3 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- BAC (Bank of America Corporation) score 53.2 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.6 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- IDBI.NS (IDBI BANK LIMITED) score 48.9 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 47.7 — "India's next commodity cycle could be driven by scrap as organised metal recycling gains m"
- COIN (Coinbase Global, Inc.) score 40.6 — "Global cues, softer crude signal positive start for Indian markets"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.1 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.7 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.6 — "Q1 Results Today Highlights: AU Small Finance Bank, IDFC First Bank, Dr. Reddy's Lab, Zen "
- COALINDIA.NS (COAL INDIA LTD) score 37.5 — "India's next commodity cycle could be driven by scrap as organised metal recycling gains m"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.4 — "Govt bonds rebound as easing US-Iran tensions drag crude oil lower"
- OHI (Omega Healthcare Investors, In) score 19.6 — "Explainer: Why investors are betting big on China’s chipmaker CXMT"
- CHKP (Check Point Software Technolog) score 15.2 — "Cube Highways Trust InvIT IPO: Focus shifts to allotment date. Latest GMP, step-by-step gu"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 14.3 — "Juniper Green Energy sets IPO price band at ₹214-225 per share; issue opens on July 30"
- LTH (Life Time Group Holdings, Inc.) score 14.1 — "Indo-MIM IPO: GMP jumps as issue subscribed 72.34 times"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.2 — "Tata Consumer Products: A tale of two halves with ‘growth businesses’ packing a punch"
- INFY (Infosys Limited) score 10.8 — "Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.0 — "Oil Market's Glut Narrative Just Blew Up"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 8.1 — "From financials to industrials: Here's how Nifty 500 composition has shifted over the year"
- VT (Vanguard Total World Stock Ind) score 7.1 — "Mangalam Worldwide Q1 Results: Profit rises 19% to Rs 12 crore"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.0 — "From financials to industrials: Here's how Nifty 500 composition has shifted over the year"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.8 — "Q1 Results today: Coal India, Tata Power, BEL, Coforge, among 68 companies to announce ear"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.5 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- META (Meta) score 6.4 — "India's next commodity cycle could be driven by scrap as organised metal recycling gains m"
- ETERNAL.NS (ETERNAL LIMITED) score 4.3 — "Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex "
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.3 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- GS (Goldman Sachs Group, Inc. (The) score 4.2 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- MS (Morgan Stanley) score 4.0 — "Infosys shares fall 3% as JPMorgan downgrades stock, Jefferies cuts target after Q1 result"
- PCJEWELLER.NS (PC JEWELLER LTD) score 3.4 — "Sebi clears IPOs of Intellius Recode, Nityas Gems & Jewellery"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 3.0 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- INDIGOPNTS.NS (INDIGO PAINTS LIMITED) score 2.9 — "Sensex jumps 530 pts as crude retreat; IndiGo, Tata Consumer lead gains"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 2.4 — "Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it?"
- NVDA (NVIDIA Corporation) score 2.2 — "AMD’s rivalry with Nvidia is increasingly moving into a new realm"
- AAPL (Apple Inc.) score 1.9 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 1.7 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.5 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.2 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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