# Transmission Layer — board brief · 2026-07-15 00:12Z

data as of **2026-07-15** · 95 series · 9 red / 32 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.451, 6d in regime; vol-pct 0.667, breadth-off 0.235, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.25, corr60 -0.45, contra nifty_50 corr20=0.37, last shift 2026-05-19. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.47, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.01, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.0, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.15, corr60 0.26, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 84** scanned series survive multiplicity control (effective p ≤ 0.0012379021807737978)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.508, β 0.213, p 0.0); driver zc 1.78 → expected 0.671%. Type hit-rate 0.817 (n=2349).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.507, β 0.2084, p 0.0); driver zc 5.08 → expected 1.908%. Type hit-rate 0.817 (n=2349).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.393, β 0.3488, p 0.0); driver zc 5.08 → expected 3.194%. Type hit-rate 0.817 (n=2349).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.309, β -0.1042, p 2e-05); driver zc 5.08 → expected -0.954%. Type hit-rate 0.817 (n=2349).
- Track record · residual_reversion: hit-rate **0.478** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2349) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.89] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 790.35, z20 7.89, zc 7.65, resid-z 15.81 [unexplained], 1d 16.66%, |z20|=7.89
- **Mechanism**: The surge in Just Dial's stock price is driven by its strong Q1 FY27 earnings report, which has prompted brokerages to turn bullish, citing revenue growth, healthy cash reserves, and improving business fundamentals. This positive sentiment is propagating through the VALID vix_equity_inverse channel, where a vol spike would typically lead to an equity drawdown, but in this case, the strong earnings report is overriding this effect. The metal_copper_channel is also a potential mechanism, as global copper leads Indian metal equities, but its relevance to Just Dial's specific situation is less clear.
- **Gap**: No gap: the big raw move in Just Dial's stock price is largely priced in, given the strong Q1 FY27 earnings report and the resulting bullish sentiment from brokerages
- **India take**: The Indian instrument that expresses this move is Just Dial's stock itself, which has already reacted with a significant surge in price. Other Indian metal equities, such as those in the metal_copper_channel, may also be affected, but the direct impact is on Just Dial's stock.
- Watch next: nifty_50 (up) — not yet - watch; Just Dial's strong earnings report could have a positive impact on the broader Indian market
- **India receivers**: dyn_biocon_bo (rho 0.505, z 3.1)
- Source: Just Dial shares rocket 36% in two days! Why Citi, Kotak, others think Reliance-backed stock can rally up to 62%? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-36-in-two-days-why-citi-kotak-others-think-reliance-backed-stock-can-rally-up-to-62/articleshow/132382158.cms
- Source: Just Dial share price skyrockets 17% on strong Q1 results, new CEO, CFO announcement. Do you own? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/just-dial-share-price-skyrockets-17-on-strong-q1-results-new-ceo-cfo-announcement-do-you-own-11783922394287.html
- Source: Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-14-as-profit-rises-to-rs-166-crore-revenue-grows-10-yoy/articleshow/132356592.cms
- Historical analogues: 2026-06-18 (d=0.19), 2025-06-30 (d=0.52), 2026-01-07 (d=0.52)

### [RED 7.76] usd_inr ↑
- usd_inr [FX]: last 96.30, z20 2.76, zc 2.18, resid-z 1.44 [moved], 1d 1.02%, 20d range extreme; |z20|=2.76; 1y-pct=99; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent surge in crude oil prices and geopolitical tensions in West Asia have led to a risk-off sentiment, causing the Indian rupee to depreciate against the US dollar. The increase in crude oil prices has also led to a rise in India's import bill, further weakening the INR. The VALID metal_copper_channel and gold_silver_comove channels suggest that the monetary metals are co-moving, and the ratio extremes are rotations, which may influence the Indian metal equities.
- **Gap**: No gap: The usd_inr move is largely priced, with a resid_z of 1.44, which is relatively low compared to the z20 level of 2.76, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the USDINR currency pair, which has already reacted to the surge in crude oil prices and geopolitical tensions. The Nifty 50 index may also be affected due to the risk-off sentiment.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment due to geopolitical tensions
- Source: Crude surge, geopolitical jitters pull D-Street lower; Rupee hits month’s low — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/crude-surge-geopolitical-jitters-pull-d-street-lower-rupee-hits-months-low/article71221009.ece
- Source: Rupee falls 62 paise to close at 96.30 against US dollar — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/forex/rupee-falls-62-paise-to-close-at-9630-against-us-dollar/article71220909.ece
- Source: Rupee slides past 96/USD to one-month low as oil climbs; RBI likely intervenes — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-slides-past-96/usd-to-one-month-low-as-oil-climbs-rbi-likely-intervenes/articleshow/132388783.cms
- Historical analogues: 2024-11-06 (d=0.01), 2024-10-24 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.65] cross-asset · 5 series ↑
- ust_10y [RATES]: last 4.62, z20 2.72, zc 0.44, resid-z 0.56 [quiet], 1d 1.32%, |z20|=2.72; 1y-pct=99
- ust_30y [RATES]: last 5.10, z20 2.28, zc 0.27, resid-z 0.32 [quiet], 1d 0.79%, |z20|=2.28; 1y-pct=98
- tips_10y_real [RATES]: last 2.36, z20 2.27, zc 0.24, resid-z 0.27 [quiet], 1d 1.72%, |z20|=2.27; 1y-pct=100
- ust_2y [RATES]: last 4.26, z20 2.15, zc 0.93, resid-z 1.21 [quiet], 1d 1.19%, |z20|=2.15; 1y-pct=100
- dyn_bond [EQUITIES]: last 91.18, z20 -1.51, zc 0.93, resid-z 0.14 [quiet], 1d 0.29%, 1y-pct=4
- **Mechanism**: The recent spike in oil prices has led to a rise in Indian government bond yields, with the 10-year yield hitting a three-week high. This move is priced, as evidenced by the high z20 levels and low resid_z values for the UST series. The valid gold_silver_comove and metal_copper_channel suggest that the move in global markets is being transmitted to Indian markets through commodity channels.
- **Gap**: No gap: the move in UST yields is largely explained by factor exposures, with low resid_z values indicating that the move is priced
- **India take**: The Indian 10-year government bond yield is likely to follow the move in UST yields, with the valid metal_copper_channel suggesting that the move in global markets will be transmitted to Indian markets. The Nifty 50 may come under pressure due to the weaker rupee and rising bond yields.
- Watch next: nifty_50 (down) — not yet - watch; weaker rupee and declining stock values in Mumbai
- Source: Oil spike jolts Indian bonds, 10-year yield hits three-week high — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/oil-spike-jolts-indian-bonds-10-year-yield-hits-three-week-high/articleshow/132391105.cms
- Source: Higher oil prices to rising bond yields: 5 key risks that could keep the Indian stock market under pressure in 2026 — Mint Markets, 2026-07-14. https://www.livemint.com/market/stock-market-news/higher-oil-prices-to-rising-bond-yields-5-key-risks-that-could-keep-the-indian-stock-market-under-pressure-in-2026-11784014632183.html
- Source: SBI raises $200 million through bond tap in — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/sbi-raises-200-million-through-bond-tap-in/articleshow/132385450.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.5] cross-asset · 4 series ↑
- dyn_gs [EQUITIES]: last 1141.67, z20 2.83, zc 5.08, resid-z -0.28 [priced], 1d 9.16%, |z20|=2.83; 1y-pct=100
- dyn_ms [EQUITIES]: last 228.05, z20 1.76, zc 1.78, resid-z -0.20 [priced], 1d 3.15%, 1y-pct=100
- sp500 [INDICES]: last 7544.29, z20 1.12, zc 0.49, resid-z 0.02 [quiet], 1d 0.39%, 1y-pct=96
- dow_jones [INDICES]: last 52526.74, z20 0.78, zc 0.07, resid-z -0.47 [quiet], 1d 0.05%, 1y-pct=98
- **Mechanism**: The recent move in US equities, led by the S&P 500 and Nasdaq, is driven by cooler inflation data and solid bank earnings, which has improved market sentiment. This move is likely to propagate through the validated transmission setups, such as dyn_gs and dyn_ms leading the ASX 200 and Nikkei 225. The metal_copper_channel and gold_silver_comove channels are also valid and may play a role in the transmission of this move to Indian markets.
- **Gap**: No gap: the recent move in US equities is largely priced in, with high z20 levels and low resid_z values indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is dyn_justdial_bo, which has already reacted with a high z20 level of 7.89. The metal_copper_channel and gold_silver_comove channels may also play a role in transmitting this move to Indian metal equities.
- Watch next: dyn_gs (up) — already moved; priced move with high z20 level
- Watch next: dyn_ms (up) — already moved; priced move with high z20 level
- Watch next: nasdaq_100 (up) — not yet - watch; high correlation with S&P 500 and historically leads by 5 days
- **India receivers**: dyn_justdial_bo (rho 0.486, z 7.89)
- Source: This overlooked index is a better investment than the S&P 500 — MarketWatch Top, 2026-07-14. https://www.marketwatch.com/story/this-overlooked-index-is-a-better-investment-than-the-s-p-500-74c7e698?mod=mw_rss_topstories
- Source: Wall Street has set a sky-high bar for companies to clear this earnings season. They just might pull it off. — MarketWatch Top, 2026-07-14. https://www.marketwatch.com/story/wall-street-has-set-a-sky-high-bar-for-companies-to-clear-this-earnings-season-they-just-might-pull-it-off-45731862?mod=mw_rss_topstories
- Source: US stocks today: S&P 500 and Nasdaq end higher on cool inflation data, solid bank earnings — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-sp-500-and-nasdaq-end-higher-on-cool-inflation-data-solid-bank-earnings/articleshow/132400813.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.32), 2024-11-11 (d=0.55)

### [RED 5.69] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 530.30, z20 3.69, zc 0.44, resid-z 1.34 [quiet], 1d 3.85%, |z20|=3.69
- **Mechanism**: The recent surge in Kalyan Jewellers' stock price is driven by the company's strong Q1 business update, which has led to a significant increase in its market value. This move is priced, given the small resid_z of 1.43, indicating that the factor exposures can explain a large portion of the move. The metal_copper_channel and gold_silver_comove channels are valid and may contribute to the propagation of this move, but the primary driver is the company-specific news.
- **Gap**: No gap: the move is largely explained by the company's strong Q1 business update and is priced in, given the small resid_z
- **India take**: The Indian instruments that express this move are nifty_midcap_100, dyn_pcjeweller_ns, and midcap_largecap_ratio, which have already reacted to Kalyan Jewellers' surge. The Nifty 50 has not yet reacted significantly, but its rho with Kalyan Jewellers is relatively low at 0.396.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to Kalyan Jewellers' surge
- Watch next: dyn_pcjeweller_ns (down) — already moved; reacted to Kalyan Jewellers' surge
- Watch next: midcap_largecap_ratio (down) — already moved; reacted to Kalyan Jewellers' surge
- **India receivers**: nifty_midcap_100 (rho 0.56, z 1.35); dyn_indianb_ns (rho 0.486, z 0.11); dyn_pcjeweller_ns (rho 0.436, z 1.11); nifty_50 (rho 0.397, z -0.23)
- Source: Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. Time to buy or book profits? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/kalyan-jewellers-shares-skyrocket-50-in-5-days-market-value-swells-by-rs-18200-crore-time-to-buy-or-book-profits/articleshow/132382065.cms
- Source: Top Gainers & Losers on 13 July: Newgen Software, Kalyan Jewellers, TCS, Voltas, Paytm, Bajaj Auto among top gainers — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-13-july-newgen-software-kalyan-jewellers-tcs-voltas-paytm-bajaj-auto-among-top-gainers-11783936105519.html
- Source: Kalyan Jewellers shares surge 12%, jump 50% in just 4 sessions; is there more steam left? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/kalyan-jewellers-shares-surge-almost-10-jump-47-in-just-4-sessions-is-there-more-steam-left-11783922565597.html
- Historical analogues: 2026-01-07 (d=1.76), 2026-06-15 (d=1.78), 2025-07-02 (d=2.84)

### [AMBER 5.21] commodities · 2 series ↑
- brent [COMMODITIES]: last 85.14, z20 2.38, zc 0.00, resid-z 1.04 [quiet], 1d 0.01%, |z20|=2.38; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 79.75, z20 2.14, zc 0.01, resid-z 0.93 [quiet], 1d 0.03%, |z20|=2.14
- **Mechanism**: The recent rise in Brent and WTI crude oil prices, driven by falling US crude oil and gasoline inventories, may propagate through the metal_copper_channel, potentially affecting Indian metal equities. However, the inr_oil_channel is weak, which could limit the transmission of oil price movements to the Indian rupee.
- **Gap**: No gap: the move in Brent and WTI is largely priced, with resid_z values of 1.04 and 0.93, respectively, indicating that the price movement is largely explained by factor exposures.
- **India take**: The Nifty Midcap 100 has already reacted to the WTI price movement, and further movements in Indian metal equities may be influenced by the metal_copper_channel. However, the weak inr_oil_channel limits the direct impact of oil prices on the Indian rupee.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price movement
- **India receivers**: nifty_midcap_100 (rho -0.515, z 1.35)
- Source: The Next Oil Rally May Depend On China, Not The Middle East — OilPrice, 2026-07-15. https://oilprice.com/Energy/Crude-Oil/The-Next-Oil-Rally-May-Depend-On-China-Not-The-Middle-East.html
- Source: Canada Ties New West Coast Pipeline to Oil Sands Expansion — OilPrice, 2026-07-14. https://oilprice.com/Energy/Crude-Oil/Canada-Ties-New-West-Coast-Pipeline-to-Oil-Sands-Expansion.html
- Source: US Crude Oil, Gasoline Inventories Still Falling — OilPrice, 2026-07-14. https://oilprice.com/Latest-Energy-News/World-News/US-Crude-Oil-Gasoline-Inventories-Still-Falling.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.1] dyn_biocon_bo ↑
- dyn_biocon_bo [EQUITIES]: last 437.30, z20 3.10, zc 2.71, resid-z 3.63 [unexplained], 1d 6.52%, |z20|=3.10; 1y-pct=100
- **Mechanism**: The recent sale of Mylan's 5.64% stake in Biocon for ₹3,679 crore has led to a surge in Biocon's shares, indicating strong institutional demand. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The surge in Biocon's shares may also be influenced by the VALID gold_silver_comove channel, as the pharmaceutical company's performance can be linked to the broader market trends.
- **Gap**: No gap: the big raw move in Biocon's shares is accompanied by a relatively small resid_z, indicating that the move is largely priced in.
- **India take**: The Indian instrument that expresses this move is dyn_justdial_bo, which has already reacted to the surge in Biocon's shares. The strong institutional demand for Biocon's shares may also have a positive impact on the broader Indian market, particularly the pharmaceutical sector.
- Watch next: dyn_justdial_bo (up) — already moved; rho=0.506 via dyn_biocon_bo
- **India receivers**: dyn_justdial_bo (rho 0.505, z 7.89)
- Source: Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/stock-markets/mylan-exits-biocon-sells-entire-564-stake-for-3679-crore-via-block-deals/article71222744.ece
- Source: Rs 1,839 crore Biocon block deal: ICICI Pru MF biggest buyer along with Citi and Goldman Sachs — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/rs-1839-crore-biocon-block-deal-icici-pru-mf-biggest-buyer-along-with-citi-and-goldman-sachs/articleshow/132393595.cms
- Source: Biocon among 4 midcap stocks that hit 52-week highs and rallied up to 21% in a month — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/biocon-among-4-midcap-stocks-that-hit-52-week-highs-and-rallied-up-to-21-in-a-month/slideshow/132389833.cms
- Historical analogues: 2025-12-26 (d=0.01), 2024-11-13 (d=0.04), 2025-07-31 (d=0.08)

### [RED 4.84] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.84, zc n/a, resid-z n/a [quiet], 1d 0.27%, 52-wk extreme (pct=98); |z20|=1.84; 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.84, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly relate to this event, but the vix_equity_inverse channel may influence the broader market sentiment.
- **Gap**: No gap: the move is largely priced in, as indicated by the None resid_z value
- **India take**: The Indian instruments, such as nifty_midcap_100 and dyn_kalyankjil_ns, have already reacted to this move, while others like dyn_indianb_ns and dyn_swiggy_ns remain quiet. The reaction in the Indian market is likely to be limited, given the priced-in nature of the event.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.544, z 1.35); dyn_kalyankjil_ns (rho 0.39, z 3.69); dyn_indianb_ns (rho 0.365, z 0.11); dyn_swiggy_ns (rho 0.351, z 0.43)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
crypto · 2 series ↑ (4.82), dyn_bac ↑ (4.15), dyn_olaelec_ns ↓ (4.15), dyn_meta ↑ (4.12), natgas ↓ (4.08), dyn_cartrade_ns ↑ (4.03), dyn_cupid_ns ↑ (3.71), gold_silver_ratio ↑ (3.63), dyn_adanient_bo ↑ (3.41), commodities · 2 series ↑ (3.35), usd_jpy ↑ (2.69), ig_oas ↑ (2.6)

## India macro
- nifty_50: 24035.1504 (1d -0.73%, z20 -0.23, flag none)
- nifty_midcap_100: 62774.2500 (1d -0.46%, z20 1.35, flag amber)
- usd_inr: 96.2989 (1d 1.02%, z20 2.76, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6118 (1d 0.27%, z20 1.84, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 36.8 — "Oil spike jolts Indian bonds, 10-year yield hits three-week high"
- COIN (Coinbase Global, Inc.) score 36.5 — "Multibagger Signature Global shares to be in focus on Wednesday after Q1 pre-sales rise 25"
- INDIANB.NS (INDIAN BANK) score 36.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500 and Nasdaq end h"
- HDB (HDFC Bank Limited) score 35.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500 and Nasdaq end h"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 33.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500 and Nasdaq end h"
- CHKP (Check Point Software Technolog) score 16.6 — "Your Social Security check could go up by $74 a month next year"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 15.9 — "Millworks Technologies IPO day 1: Issue fully subscribed; GMP hints at over 80% listing po"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 14.2 — "Trump’s Hormuz Toll Could Upend Global Energy Trade"
- BOND (PIMCO Active Bond Exchange-Tra) score 12.0 — "Oil spike jolts Indian bonds, 10-year yield hits three-week high"
- VT (Vanguard Total World Stock Ind) score 11.6 — "Alpine Texworld IPO off to a slow start; subscribed 0.28 times on Day 1; GMP indicates mod"
- SKHYV (SK hynix Inc. American Deposit) score 10.8 — "Global Market Update | SK Hynix set to gain as South Korea eases capital-raising rules"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.6 — "Your monthly Netflix bill is up 29% in just over a year. Critics say Washington needs to f"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.9 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 7.3 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "Adani ducks headwinds to record a huge jump in realty fortune; at cusp of being richest in"
- META (Meta) score 5.3 — "Vedanta AGM: Anil Agarwal maps aggressive expansion after demerger, targets scale-up acros"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.9 — "Defence stocks to buy or sell: Kotak expects defence upcycle to continue, prefers HAL over"
- BAC (Bank of America Corporation) score 4.8 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500 and Nasdaq end h"
- MS (Morgan Stanley) score 4.6 — "JPMorgan posts record profit on big gains from dealmaking, stock trading"
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "Rs 1,839 crore Biocon block deal: ICICI Pru MF biggest buyer along with Citi and Goldman S"
- BIOCON.BO (BIOCON LTD.) score 4.5 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- SWIGGY.NS (SWIGGY LIMITED) score 3.9 — "Top Gainers & Losers on 14 July: HCL Tech, Ceat, Swiggy, Anant Raj, Newgen Software Tech a"
- MU (Micron Technology, Inc.) score 3.1 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- CUPID.NS (CUPID LIMITED) score 3.0 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.0 — "CUBA'S NATIONAL ELECTRIC GRID COLLAPSES, SAYS CUBA'S STATE MEDIA"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 2.5 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- JEF (Jefferies Financial Group Inc.) score 2.0 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- LGDS (JPMorgan Fundamental Data Scie) score 1.9 — "JPMorgan posts record profit on big gains from dealmaking, stock trading"
- MCAP (MCAP Inc.) score 1.8 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.4 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- BLK (BlackRock, Inc.) score 1.1 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.1 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 0.8 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 0.7 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 0.6 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.5 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
- WULF (TeraWulf Inc.) score 0.4 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"

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