# Transmission Layer — board brief · 2026-07-14 16:49Z

data as of **2026-07-14** · 95 series · 12 red / 35 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.451, 6d in regime; vol-pct 0.667, breadth-off 0.235, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.25, corr60 -0.45, contra nifty_50 corr20=0.36, last shift 2026-05-19. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.95, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.47, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.01, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.0, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.15, corr60 0.26, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 84** scanned series survive multiplicity control (effective p ≤ 0.0005014137825609666)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.508, β 0.213, p 0.0); driver zc 1.7 → expected 0.641%. Type hit-rate 0.815 (n=2399).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.507, β 0.2084, p 0.0); driver zc 4.01 → expected 1.506%. Type hit-rate 0.815 (n=2399).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.393, β 0.3488, p 0.0); driver zc 4.01 → expected 2.522%. Type hit-rate 0.815 (n=2399).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.392, β 0.3145, p 0.0); driver zc 4.01 → expected 2.274%. Type hit-rate 0.815 (n=2399).
- **SETUP** dyn_gs → usd_brl: leads 1d (ccf -0.381, β -0.1583, p 0.0); driver zc 4.01 → expected -1.144%. Type hit-rate 0.815 (n=2399).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.308, β -0.106, p 3e-05); driver zc 4.01 → expected -0.766%. Type hit-rate 0.815 (n=2399).
- Track record · residual_reversion: hit-rate **0.478** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2399) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.89] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 790.35, z20 7.89, zc 7.65, resid-z 15.77 [unexplained], 1d 16.66%, |z20|=7.89
- **Mechanism**: The surge in Just Dial's stock price is driven by its strong Q1 FY27 earnings report, which has prompted brokerages to turn bullish, citing revenue growth, healthy cash reserves, and improving business fundamentals. This positive sentiment is propagating through the VALID vix_equity_inverse channel, where a vol spike would typically lead to an equity drawdown, but in this case, the strong earnings report is overriding this effect. The metal_copper_channel is also a potential mechanism, as global copper leads Indian metal equities, but its relevance to Just Dial's specific situation is less clear.
- **Gap**: No gap: the big raw move in Just Dial's stock price is largely priced in, given the strong Q1 FY27 earnings report and the resulting bullish sentiment from brokerages
- **India take**: The Indian instrument that expresses this move is Just Dial's stock itself, which has already reacted with a significant surge in price. Other Indian metal equities, such as those in the metal_copper_channel, may also be affected, but the direct impact is on Just Dial's stock.
- Watch next: nifty_50 (up) — not yet - watch; Just Dial's strong earnings report could have a positive impact on the broader Indian market
- **India receivers**: dyn_biocon_bo (rho 0.506, z 3.1)
- Source: Just Dial shares rocket 36% in two days! Why Citi, Kotak, others think Reliance-backed stock can rally up to 62%? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-36-in-two-days-why-citi-kotak-others-think-reliance-backed-stock-can-rally-up-to-62/articleshow/132382158.cms
- Source: Just Dial share price skyrockets 17% on strong Q1 results, new CEO, CFO announcement. Do you own? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/just-dial-share-price-skyrockets-17-on-strong-q1-results-new-ceo-cfo-announcement-do-you-own-11783922394287.html
- Source: Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-14-as-profit-rises-to-rs-166-crore-revenue-grows-10-yoy/articleshow/132356592.cms
- Historical analogues: 2026-06-18 (d=0.19), 2025-06-30 (d=0.52), 2026-01-07 (d=0.52)

### [RED 8.29] commodities · 2 series ↑
- brent [COMMODITIES]: last 84.81, z20 2.46, zc 0.72, resid-z 0.93 [quiet], 1d 1.81%, 1-session move +1.81% ≥ 1.5%; |z20|=2.46; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 79.12, z20 1.88, zc 0.51, resid-z 0.72 [quiet], 1d 1.25%, |z20|=1.88
- **Mechanism**: The recent surge in oil prices, driven by renewed U.S.-Iran hostilities and supply concerns, is propagating through the commodities channel, with Brent and WTI crude oil prices increasing by 1.81% and 1.25% respectively. This move is priced, given the relatively small resid_z values of 0.93 and 0.72, indicating that the factor exposures explain a significant portion of the price movement. The valid gold_silver_comove and metal_copper_channel may also contribute to the transmission of this move to other markets.
- **Gap**: No gap: the recent oil price surge is largely explained by the factor exposures, with small resid_z values indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted to the WTI price increase with a z20 score of 1.35. Further transmission to Indian metal equities may occur through the valid metal_copper_channel.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price increase
- **India receivers**: nifty_midcap_100 (rho -0.513, z 1.35)
- Source: Oil’s Oversupply Narrative Just Died — OilPrice, 2026-07-14. https://oilprice.com/Energy/Crude-Oil/Oils-Oversupply-Narrative-Just-Died.html
- Source: Venezuela’s Oil Revival Faces a Critical Services Bottleneck — OilPrice, 2026-07-14. https://oilprice.com/Energy/Energy-General/Venezuelas-Oil-Revival-Faces-a-Critical-Services-Bottleneck.html
- Source: Oil Jumps Above $87 as Russia-Ukraine Black Sea Attacks Escalate — OilPrice, 2026-07-14. https://oilprice.com/Latest-Energy-News/World-News/Oil-Jumps-Above-87-as-Russia-Ukraine-Black-Sea-Attacks-Escalate.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.53] usd_inr ↑
- usd_inr [FX]: last 96.19, z20 2.53, zc 1.94, resid-z 1.26 [moved], 1d 0.91%, 20d range extreme; |z20|=2.53; 1y-pct=98; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The surge in crude oil prices and geopolitical tensions in West Asia have led to a rise in the USD/INR exchange rate, as investors seek safe-haven assets and the import bill for India increases. This move is priced, given the big raw move in USD/INR with a relatively small resid_z of 1.26. The valid channels, such as the vix_equity_inverse and metal_copper_channel, do not directly contribute to this move, but the weak inr_oil_channel and dxy_inr_channel are consistent with the observed price action.
- **Gap**: No gap: the move in USD/INR is largely priced, with a small resid_z and a big raw move, indicating that the market has already adjusted to the new information
- **India take**: The Indian rupee has already reacted to the surge in crude oil prices, with the eur_inr also moving in tandem. The RBI's potential intervention to stabilize the currency may influence the future trajectory of the USD/INR exchange rate.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment due to geopolitical tensions
- **India receivers**: eur_inr (rho 0.395, z 1.74)
- Source: Crude surge, geopolitical jitters pull D-Street lower; Rupee hits month’s low — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/crude-surge-geopolitical-jitters-pull-d-street-lower-rupee-hits-months-low/article71221009.ece
- Source: Rupee falls 62 paise to close at 96.30 against US dollar — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/markets/forex/rupee-falls-62-paise-to-close-at-9630-against-us-dollar/article71220909.ece
- Source: Rupee slides past 96/USD to one-month low as oil climbs; RBI likely intervenes — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-slides-past-96/usd-to-one-month-low-as-oil-climbs-rbi-likely-intervenes/articleshow/132388783.cms
- Historical analogues: 2024-11-06 (d=0.01), 2024-10-24 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.71] commodities · 3 series ↑
- corn [COMMODITIES]: last 461.00, z20 3.40, zc 4.21, resid-z 3.48 [unexplained], 1d 5.31%, |z20|=3.40
- wheat [COMMODITIES]: last 647.25, z20 3.22, zc 1.86, resid-z 1.60 [unexplained], 1d 3.23%, |z20|=3.22; 1y-pct=97
- soybeans [COMMODITIES]: last 1192.75, z20 1.51, zc -0.76, resid-z -1.18 [quiet], 1d -0.77%, |z20|=1.51
- **Mechanism**: The recent decline in Indian edible oil imports, led by a fall in palm and soybean oil shipments, may propagate through the commodities channel, influencing prices of corn, wheat, and soybeans. The move in these commodities is largely unexplained by factors, with high resid_z values. However, the big raw move with small resid_z in soybeans is PRICED, not an anomaly.
- **Gap**: No gap: the recent move in commodities is largely priced in, with soybeans already reacting and the Indian transmission candidates, such as dyn_justdial_bo and dyn_adanient_bo, having reacted.
- **India take**: The Indian instrument dyn_justdial_bo, which has a rho of 0.497 with corn, has already reacted to the move in commodities. Similarly, dyn_adanient_bo, which has a rho of -0.353 with soybeans, has also reacted.
- Watch next: corn (up) — not yet - watch; unexplained move with high resid_z
- Watch next: wheat (up) — not yet - watch; unexplained move with high resid_z
- **India receivers**: dyn_justdial_bo (rho 0.497, z 7.89); dyn_adanient_bo (rho -0.353, z 1.41)
- Source: Indian edible oil imports decline 30% in June as palm and soybean oil shipments fall — BusinessLine Mkts, 2026-07-14. https://www.thehindubusinessline.com/economy/agri-business/indian-edible-oil-imports-decline-30-in-june-as-palm-and-soybean-oil-shipments-fall/article71220483.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [AMBER 5.72] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.32, z20 1.79, zc 0.24, resid-z 0.27 [quiet], 1d 0.43%, |z20|=1.79; 1y-pct=100
- ust_30y [RATES]: last 5.06, z20 1.74, zc 0.27, resid-z 0.32 [quiet], 1d 0.20%, |z20|=1.74; 1y-pct=97
- ust_10y [RATES]: last 4.56, z20 1.64, zc 0.44, resid-z 0.56 [quiet], 1d 0.44%, |z20|=1.64; 1y-pct=96
- dyn_bond [EQUITIES]: last 91.14, z20 -1.62, zc 0.76, resid-z 0.14 [quiet], 1d 0.24%, 1y-pct=4
- ust_2y [RATES]: last 4.21, z20 1.40, zc 0.93, resid-z 1.21 [quiet], 1d 1.20%, 1y-pct=99
- **Mechanism**: The recent spike in oil prices has led to a rise in Indian government bond yields, with the 10-year yield hitting a three-week high. This increase in yields is likely to propagate through the financial markets, affecting various asset classes. The valid gold_silver_comove and metal_copper_channel may also play a role in transmitting this shock to Indian metal equities.
- **Gap**: No gap: The big raw move in tips_10y_real and ust_10y with small resid_z indicates that the move is largely priced in, leaving no significant event-to-price gap.
- **India take**: The Indian 10-year government bond yield has already reacted to the oil price spike, and the Nifty 50 may come under pressure due to the weaker rupee and rising bond yields. The metal_copper_channel may also affect Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Weaker rupee and declining stock values in Mumbai
- Watch next: usd_inr (up) — not yet - watch; Oil up -> import bill -> INR weakens
- Source: Oil spike jolts Indian bonds, 10-year yield hits three-week high — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/oil-spike-jolts-indian-bonds-10-year-yield-hits-three-week-high/articleshow/132391105.cms
- Source: Higher oil prices to rising bond yields: 5 key risks that could keep the Indian stock market under pressure in 2026 — Mint Markets, 2026-07-14. https://www.livemint.com/market/stock-market-news/higher-oil-prices-to-rising-bond-yields-5-key-risks-that-could-keep-the-indian-stock-market-under-pressure-in-2026-11784014632183.html
- Source: SBI raises $200 million through bond tap in — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/sbi-raises-200-million-through-bond-tap-in/articleshow/132385450.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.69] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 530.30, z20 3.69, zc 0.44, resid-z 1.35 [quiet], 1d 3.85%, |z20|=3.69
- **Mechanism**: The recent surge in Kalyan Jewellers' stock price is driven by the company's strong Q1 business update, which has led to a significant increase in its market value. This move is priced, given the small resid_z of 1.43, indicating that the factor exposures can explain a large portion of the move. The metal_copper_channel and gold_silver_comove channels are valid and may contribute to the propagation of this move, but the primary driver is the company-specific news.
- **Gap**: No gap: the move is largely explained by the company's strong Q1 business update and is priced in, given the small resid_z
- **India take**: The Indian instruments that express this move are nifty_midcap_100, dyn_pcjeweller_ns, and midcap_largecap_ratio, which have already reacted to Kalyan Jewellers' surge. The Nifty 50 has not yet reacted significantly, but its rho with Kalyan Jewellers is relatively low at 0.396.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to Kalyan Jewellers' surge
- Watch next: dyn_pcjeweller_ns (down) — already moved; reacted to Kalyan Jewellers' surge
- Watch next: midcap_largecap_ratio (down) — already moved; reacted to Kalyan Jewellers' surge
- **India receivers**: nifty_midcap_100 (rho 0.56, z 1.35); dyn_indianb_ns (rho 0.487, z 0.11); dyn_pcjeweller_ns (rho 0.437, z 1.11); nifty_50 (rho 0.396, z -0.23)
- Source: Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. Time to buy or book profits? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/kalyan-jewellers-shares-skyrocket-50-in-5-days-market-value-swells-by-rs-18200-crore-time-to-buy-or-book-profits/articleshow/132382065.cms
- Source: Top Gainers & Losers on 13 July: Newgen Software, Kalyan Jewellers, TCS, Voltas, Paytm, Bajaj Auto among top gainers — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-13-july-newgen-software-kalyan-jewellers-tcs-voltas-paytm-bajaj-auto-among-top-gainers-11783936105519.html
- Source: Kalyan Jewellers shares surge 12%, jump 50% in just 4 sessions; is there more steam left? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/kalyan-jewellers-shares-surge-almost-10-jump-47-in-just-4-sessions-is-there-more-steam-left-11783922565597.html
- Historical analogues: 2026-01-07 (d=1.76), 2026-06-15 (d=1.78), 2025-07-02 (d=2.84)

### [RED 5.1] dyn_biocon_bo ↑
- dyn_biocon_bo [EQUITIES]: last 437.30, z20 3.10, zc 2.71, resid-z 3.65 [unexplained], 1d 6.52%, |z20|=3.10; 1y-pct=100
- **Mechanism**: dyn_biocon_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-26 (z-distance 0.01).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.506 via dyn_biocon_bo, z 7.89, reacted)
- **India receivers**: dyn_justdial_bo (rho 0.506, z 7.89)
- Source: Rs 1,839 crore Biocon block deal: ICICI Pru MF biggest buyer along with Citi and Goldman Sachs — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/rs-1839-crore-biocon-block-deal-icici-pru-mf-biggest-buyer-along-with-citi-and-goldman-sachs/articleshow/132393595.cms
- Source: Biocon among 4 midcap stocks that hit 52-week highs and rallied up to 21% in a month — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/biocon-among-4-midcap-stocks-that-hit-52-week-highs-and-rallied-up-to-21-in-a-month/slideshow/132389833.cms
- Source: Biocon shares jump 6% as Mylan likely exits drugmaker after Rs 3,481 crore stake sale — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/biocon-shares-jump-6-as-mylan-likely-exits-drugmaker-after-rs-3481-crore-stake-sale/articleshow/132381476.cms
- Historical analogues: 2025-12-26 (d=0.01), 2024-11-13 (d=0.04), 2025-07-31 (d=0.08)

### [AMBER 4.99] equities · 2 series ↑
- dyn_gs [EQUITIES]: last 1121.52, z20 2.16, zc 4.01, resid-z -0.28 [priced], 1d 7.23%, |z20|=2.16; 1y-pct=100
- dyn_ms [EQUITIES]: last 227.74, z20 1.70, zc 1.70, resid-z -0.20 [priced], 1d 3.01%, 1y-pct=100
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.654 vs dyn_gs, historically leads by 4d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.566 vs dyn_gs, historically leads by 2d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.553 vs dyn_gs, historically leads by 3d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.515 vs dyn_gs, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.513 vs dyn_gs, historically leads by 3d
- Source: Goldman Sachs profit tops estimates on trading boom, corporate deal spree — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/us-stocks/news/goldman-sachs-profit-tops-estimates-on-trading-boom-corporate-deal-spree/articleshow/132395970.cms
- Source: Rs 1,839 crore Biocon block deal: ICICI Pru MF biggest buyer along with Citi and Goldman Sachs — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/rs-1839-crore-biocon-block-deal-icici-pru-mf-biggest-buyer-along-with-citi-and-goldman-sachs/articleshow/132393595.cms
- Source: Goldman Sachs stock picks! RIL, HDFC Bank, Adani Power, among 14 names brokerage is bullish on — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/goldman-sachs-stock-picks-ril-hdfc-bank-adani-power-among-14-names-brokerage-is-bullish-on/slideshow/132380450.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-11 (d=0.15), 2025-08-13 (d=0.16)

## Watchlist (below surfacing floor)
crypto · 2 series ↑ (4.95), dyn_qessf ↓ (4.86), midcap_largecap_ratio ↑ (4.84), natgas ↓ (4.55), dyn_meta ↑ (4.2), dyn_bac ↑ (4.15), dyn_olaelec_ns ↓ (4.15), dyn_cartrade_ns ↑ (4.03), indices · 2 series ↑ (3.85), gold_silver_ratio ↑ (3.75), dyn_cupid_ns ↑ (3.71), dyn_adanient_bo ↑ (3.41)

## India macro
- nifty_50: 24035.1504 (1d -0.73%, z20 -0.23, flag none)
- nifty_midcap_100: 62774.2500 (1d -0.46%, z20 1.35, flag amber)
- usd_inr: 96.1900 (1d 0.91%, z20 2.53, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6118 (1d 0.27%, z20 1.84, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-1d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 39.5 — "Oil spike jolts Indian bonds, 10-year yield hits three-week high"
- COIN (Coinbase Global, Inc.) score 37.1 — "Thomson Reuters to sell 51% stake in global print business to KKR for $500 million"
- INDIANB.NS (INDIAN BANK) score 35.7 — "Moody's affirms SBI, HDFC Bank ratings on strong asset quality"
- HDB (HDFC Bank Limited) score 34.5 — "Moody's affirms SBI, HDFC Bank ratings on strong asset quality"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 32.6 — "Moody's affirms SBI, HDFC Bank ratings on strong asset quality"
- CHKP (Check Point Software Technolog) score 17.8 — "Your Social Security check could go up by $74 a month next year"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 17.0 — "Millworks Technologies IPO day 1: Issue fully subscribed; GMP hints at over 80% listing po"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 13.1 — "Govt reviews fresh bids for IDBI Bank as stake sale process gathers pace"
- BOND (PIMCO Active Bond Exchange-Tra) score 12.9 — "Oil spike jolts Indian bonds, 10-year yield hits three-week high"
- VT (Vanguard Total World Stock Ind) score 12.5 — "Alpine Texworld IPO off to a slow start; subscribed 0.28 times on Day 1; GMP indicates mod"
- SKHYV (SK hynix Inc. American Deposit) score 11.6 — "Global Market Update | SK Hynix set to gain as South Korea eases capital-raising rules"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.5 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "12 stocks held by 100+ MFs in June surged up to 105% in just over 6 months"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 7.8 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.3 — "Adani ducks headwinds to record a huge jump in realty fortune; at cusp of being richest in"
- META (Meta) score 5.7 — "Vedanta AGM: Anil Agarwal maps aggressive expansion after demerger, targets scale-up acros"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.3 — "Defence stocks to buy or sell: Kotak expects defence upcycle to continue, prefers HAL over"
- MS (Morgan Stanley) score 5.0 — "JPMorgan posts record profit on big gains from dealmaking, stock trading"
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "Rs 1,839 crore Biocon block deal: ICICI Pru MF biggest buyer along with Citi and Goldman S"
- SWIGGY.NS (SWIGGY LIMITED) score 4.2 — "Top Gainers & Losers on 14 July: HCL Tech, Ceat, Swiggy, Anant Raj, Newgen Software Tech a"
- BIOCON.BO (BIOCON LTD.) score 3.7 — "Biocon among 4 midcap stocks that hit 52-week highs and rallied up to 21% in a month"
- MU (Micron Technology, Inc.) score 3.4 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- CUPID.NS (CUPID LIMITED) score 3.2 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 2.7 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- JEF (Jefferies Financial Group Inc.) score 2.2 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.1 — "GE Vernova, Atlanta Electricals among top beneficiaries of India's transmission expansion"
- BAC (Bank of America Corporation) score 2.0 — "Bank of America Q2 net income rises on higher trading activities"
- LGDS (JPMorgan Fundamental Data Scie) score 2.0 — "JPMorgan posts record profit on big gains from dealmaking, stock trading"
- MCAP (MCAP Inc.) score 1.9 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.5 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- BLK (BlackRock, Inc.) score 1.2 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.2 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 0.8 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 0.7 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 0.6 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
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