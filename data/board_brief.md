# Transmission Layer — board brief · 2026-07-15 16:55Z

data as of **2026-07-15** · 98 series · 14 red / 31 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.383, 7d in regime; vol-pct 0.589, breadth-off 0.176, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.45, contra nifty_50 corr20=0.37, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.45, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.01, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.25, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **7 of 87** scanned series survive multiplicity control (effective p ≤ 0.005110260660855737)
- **SETUP** dyn_blk → asx_200: leads 1d (ccf 0.509, β 0.2488, p 0.0); driver zc 4.37 → expected 1.817%. Type hit-rate 0.817 (n=2435).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.471, β 0.1411, p 0.0); driver zc 1.57 → expected 0.638%. Type hit-rate 0.817 (n=2435).
- **SETUP** dyn_mu → kospi: leads 1d (ccf 0.393, β 0.1934, p 0.0); driver zc -1.64 → expected -1.82%. Type hit-rate 0.817 (n=2435).
- **SETUP** dyn_blk → nikkei_225: leads 1d (ccf 0.375, β 0.4014, p 0.0); driver zc 4.37 → expected 2.932%. Type hit-rate 0.817 (n=2435).
- **SETUP** dyn_mu → aud_usd: leads 1d (ccf 0.318, β 0.0453, p 0.0); driver zc -1.64 → expected -0.427%. Type hit-rate 0.817 (n=2435).
- Track record · residual_reversion: hit-rate **0.482** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2435) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 18.84] dyn_patanjali_ns ↓
- dyn_patanjali_ns [EQUITIES]: last 347.00, z20 -16.84, zc -11.24, resid-z -12.12 [unexplained], 1d -14.86%, |z20|=16.84; 1y-pct=0
- **Mechanism**: The sharp decline in Patanjali Foods shares is attributed to heavy selling, with technical analysts warning of further downside. The stock's 20% plunge is not fully explained by factor exposures, as indicated by a resid_z of -12.24. This unexplained move may propagate through the metal_copper_channel, given the VALID status of this channel. However, the primary driver of the move appears to be idiosyncratic to Patanjali Foods, with no clear link to broader market or macro factors.
- **Gap**: No gap: the 20% decline in Patanjali Foods shares is largely priced in, given the stock's significant decline over the past year and the lack of clear catalysts for a reversal
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a decline. Further downside in Patanjali Foods may lead to additional selling pressure in related stocks, although the lack of a clear event-to-price gap suggests that the market has already digested the news.
- Watch next: dyn_tataelxsi_ns (down) — already moved; rho=0.418 with dyn_patanjali_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.418, z -1.67)
- Source: Patanjali Foods shares crash 20%, stock nearly halves in value in one year. What's ahead? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/patanjali-foods-shares-crash-20-stock-nearly-halves-in-value-in-one-year-whats-ahead/articleshow/132410105.cms
- Source: Patanjali Foods share price crashes 20%, extending losses for third straight session; what should investors do? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/patanjali-foods-share-price-crashes-20-extends-its-losses-for-third-session-what-should-investors-do-11784098857317.html
- Historical analogues: 2025-01-27 (d=0.01), 2026-05-28 (d=0.05), 2025-06-30 (d=0.06)

### [RED 9.6] dyn_nuvoco_ns ↑
- dyn_nuvoco_ns [EQUITIES]: last 376.30, z20 7.60, zc 3.42, resid-z 4.01 [unexplained], 1d 10.22%, |z20|=7.60
- **Mechanism**: The surge in Nuvoco Vistas' stock price is driven by strong Q1 FY27 results, with better-than-expected realisation and EBITDA of ₹570 crore. This move is unexplained by factor exposures, with a high resid_z of 4.01, indicating a potential anomaly. The metal_copper_channel, which is currently valid, may also be contributing to the move, as global copper leads Indian metal equities.
- **Gap**: No gap: the stock's 12% rally is largely priced in, given the strong Q1 results and bullish views from brokerages
- **India take**: Indian instruments such as Nuvoco Vistas, Just Dial, and PC Jeweller have already reacted to the move, with Nuvoco Vistas' stock price surging 12% on the strong Q1 results. The Nifty Midcap 100 index has also moved in response to the event.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to Nuvoco Vistas' strong Q1 results
- **India receivers**: dyn_justdial_bo (rho 0.514, z 3.96); nifty_midcap_100 (rho 0.451, z 1.74); dyn_pcjeweller_ns (rho 0.403, z 2.49)
- Source: Broker’s Call: Nuvoco Vistas (Accumulate) — BusinessLine Mkts, 2026-07-15. https://www.thehindubusinessline.com/markets/brokers-call-nuvoco-vistas-accumulate/article71224959.ece
- Source: Nuvoco Vistas share price rallies 12% on strong Q1 results FY27. Should you buy or sell? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/nuvoco-vistas-share-price-rallies-12-on-strong-q1-results-fy27-should-you-buy-or-sell-11784091753229.html
- Source: Nuvoco Vistas shares soar 10% after strong Q1. Why Nomura, Choice see up to 47% upside? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/nuvoco-vistas-shares-soar-10-after-strong-q1-why-nomura-choice-see-up-to-47-upside/articleshow/132406082.cms
- Historical analogues: 2025-08-12 (d=0.03), 2025-08-05 (d=0.05), 2025-07-29 (d=0.05)

### [RED 8.27] dyn_pypl ↑
- dyn_pypl [EQUITIES]: last 54.99, z20 6.27, zc 6.55, resid-z 0.99 [moved], 1d 16.10%, |z20|=6.27
- **Mechanism**: The surge in PayPal shares following a reported $53 billion buyout offer from Stripe and Advent International has triggered a rally in the US markets, with the S&P 500 and Dow Jones Industrial Average rising. This move is likely to propagate through the VALID vix_equity_inverse channel, where a vol spike would typically lead to an equity drawdown, but in this case, the positive news has led to a rise in equities. The metal_copper_channel may also play a role, as global copper leads Indian metal equities, potentially influencing the Indian market.
- **Gap**: No gap: the big raw move in dyn_pypl has a relatively small resid_z of 0.99, indicating that the move is largely priced in and not an anomaly
- **India take**: The Indian instruments dyn_patanjali_ns and dyn_pcjeweller_ns have already reacted to the move in dyn_pypl, with dyn_patanjali_ns having a negative correlation and dyn_pcjeweller_ns having a positive correlation. The metal_copper_channel may also influence the Indian metal equities.
- Watch next: dyn_patanjali_ns (down) — already moved; rho=-0.615 via dyn_pypl
- Watch next: dyn_pcjeweller_ns (up) — already moved; rho=0.359 via dyn_pypl
- **India receivers**: dyn_patanjali_ns (rho -0.615, z -16.84); dyn_pcjeweller_ns (rho 0.359, z 2.49)
- Source: PayPal’s battered stock is getting a record boost from a report of buyout interest — MarketWatch Top, 2026-07-15. https://www.marketwatch.com/story/a-53-billion-lifeline-stripe-and-advent-reportedly-team-up-to-bid-for-battered-paypal-3bc6fcc2?mod=mw_rss_topstories
- Source: PayPal shares jump over 15% after Stripe, Advent make $53 billion buyout offer — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/paypal-shares-jump-over-15-after-stripe-advent-make-53-billion-buyout-offer/articleshow/132418333.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-04-16 (d=0.05)

### [RED 6.38] rates · 4 series ↑
- ust_10y [RATES]: last 4.62, z20 2.72, zc 0.44, resid-z 0.56 [quiet], 1d 1.32%, |z20|=2.72; 1y-pct=99
- ust_30y [RATES]: last 5.10, z20 2.28, zc 0.27, resid-z 0.32 [quiet], 1d 0.79%, |z20|=2.28; 1y-pct=98
- tips_10y_real [RATES]: last 2.36, z20 2.27, zc 0.24, resid-z 0.27 [quiet], 1d 1.72%, |z20|=2.27; 1y-pct=100
- ust_2y [RATES]: last 4.26, z20 2.15, zc 0.93, resid-z 1.21 [quiet], 1d 1.19%, |z20|=2.15; 1y-pct=100
- **Mechanism**: The recent spike in oil prices and global market anxiety have led to a rise in Euro zone bond yields, which has been transmitted to the Indian bond market, causing the 10-year yield to hit a three-week high. This move is priced, as evidenced by the high z20 levels and low resid_z values for the US Treasury series, indicating that the move is largely explained by factor exposures.
- **Gap**: No gap: The move in bond yields is largely explained by factor exposures, with high z20 levels and low resid_z values, indicating that the market has priced in the recent developments.
- **India take**: The Indian 10-year bond yield has reacted to the global developments, hitting a three-week high, and the Nifty 50 may follow suit with a decline due to risk-off sentiment. The metal_copper_channel, which is a valid channel, may also lead to a decline in Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment due to oil price spike and global market anxiety may lead to a decline in Indian equities
- Source: 10-year bond yield may trade in 6.60-6.90% range over the next month: PGIM India MF's Puneet Pal — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/10-year-bond-yield-may-trade-in-6-60-6-90-range-over-the-next-month-pgim-india-mfs-puneet-pal/articleshow/132409495.cms
- Source: Euro zone bond yields tick higher along with oil prices after big swings — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-along-with-oil-prices-after-big-swings/articleshow/132409354.cms
- Source: Oil spike jolts Indian bonds, 10-year yield hits three-week high — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/bonds/oil-spike-jolts-indian-bonds-10-year-yield-hits-three-week-high/articleshow/132391105.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [RED 5.96] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 801.65, z20 3.96, zc 0.14, resid-z 0.39 [quiet], 1d 1.43%, |z20|=3.96
- **Mechanism**: The recent surge in Just Dial's stock price is driven by strong Q1 FY27 earnings, prompting brokerages to turn bullish and predict further upside. This move is priced, given the small resid_z of 0.39, indicating that the stock's move is largely explained by its factor exposures. The metal_copper_channel and gold_silver_comove channels are valid, but they do not directly influence the stock's move. Instead, the vix_equity_inverse channel suggests that the equity market's volatility may impact the stock's price.
- **Gap**: No gap: the stock's move is largely priced, with a small resid_z of 0.39, indicating that the market has already accounted for the earnings report and brokerages' positive views.
- **India take**: Indian instruments such as dyn_nuvoco_ns and dyn_biocon_bo have reacted to Just Dial's surge, given their correlations with the stock. However, the broader Indian market has not shown a significant reaction yet.
- Watch next: dyn_nuvoco_ns (up) — already moved; reacted to Just Dial's surge due to rho=0.514 correlation
- **India receivers**: dyn_nuvoco_ns (rho 0.514, z 7.6); dyn_biocon_bo (rho 0.499, z 2.13); dyn_patanjali_ns (rho 0.018, z -16.84)
- Source: Just Dial shares rocket 36% in two days! Why Citi, Kotak, others think Reliance-backed stock can rally up to 62%? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-36-in-two-days-why-citi-kotak-others-think-reliance-backed-stock-can-rally-up-to-62/articleshow/132382158.cms
- Historical analogues: 2026-06-18 (d=0.19), 2025-06-30 (d=0.52), 2026-01-07 (d=0.52)

### [AMBER 5.66] cross-asset · 4 series ↑
- dyn_gs [EQUITIES]: last 1130.80, z20 2.00, zc -0.16, resid-z -0.28 [quiet], 1d -0.81%, 1y-pct=99
- dyn_ms [EQUITIES]: last 226.84, z20 1.34, zc -0.19, resid-z -0.20 [quiet], 1d -0.36%, 1y-pct=99
- sp500 [INDICES]: last 7539.48, z20 0.94, zc -0.07, resid-z 0.02 [quiet], 1d -0.05%, 1y-pct=96
- dow_jones [INDICES]: last 52518.31, z20 0.69, zc 0.03, resid-z -0.23 [quiet], 1d 0.02%, 1y-pct=98
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.473 via dyn_gs, z 3.96, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.909 vs sp500, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.633 vs dyn_gs, historically leads by 4d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.566 vs dyn_gs, historically leads by 1d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.551 vs dyn_gs, historically leads by 2d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.523 vs dyn_gs, historically leads by 3d
- **India receivers**: dyn_justdial_bo (rho 0.473, z 3.96)
- Source: JP Morgan moving closer to a milestone no bank has ever reached: A $1 trillion market value — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/jp-morgan-moving-closer-to-a-milestone-no-bank-has-ever-reached-a-1-trillion-market-value/articleshow/132418396.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Source: Morgan Stanley beats profit estimates on dealmaking boost, strong trading — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/morgan-stanley-beats-profit-estimates-on-dealmaking-boost-strong-trading/articleshow/132416647.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.32), 2024-11-11 (d=0.55)

### [RED 5.61] commodities · 2 series ↑
- wheat [COMMODITIES]: last 680.25, z20 4.78, zc 4.67, resid-z 3.82 [unexplained], 1d 7.76%, |z20|=4.78; 1y-pct=100
- corn [COMMODITIES]: last 468.75, z20 3.91, zc 6.40, resid-z 5.38 [unexplained], 1d 8.07%, |z20|=3.91; 1y-pct=98
- **Mechanism**: The recent surge in wheat and corn prices, with z20 levels of 4.78 and 3.91 respectively, is driven by unexplained factors as indicated by their resid_z values of 3.82 and 5.38. This move is not fully priced in as the r2 values are low at 0.032 and 0.07. The historical analogues suggest a potential for further upside in wheat and corn prices, with median returns of 5.39% and 6.5% over the next 20 days.
- **Gap**: No gap: the current price move in wheat and corn is largely unexplained by factors, but the historical analogues and low r2 values suggest that the move is not yet fully priced in
- **India take**: The Indian instrument dyn_patanjali_ns has already reacted to the move in corn, with a rho of -0.533. However, other Indian metal equities may also be affected through the valid metal_copper_channel.
- Watch next: wheat (up) — unexplained; unexplained move with low r2 value
- Watch next: corn (up) — unexplained; unexplained move with low r2 value
- **India receivers**: dyn_patanjali_ns (rho -0.533, z -16.84)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.16), 2024-10-11 (d=0.33)

### [AMBER 5.15] commodities · 2 series ↑
- brent [COMMODITIES]: last 84.78, z20 2.32, zc 0.02, resid-z 0.14 [quiet], 1d 0.06%, |z20|=2.32; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 79.49, z20 2.10, zc 0.08, resid-z 0.16 [quiet], 1d 0.19%, |z20|=2.10
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.507 via wti, z 1.74, reacted)
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.575 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.525 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.5 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.539 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.507, z 1.74)
- Source: America’s oil refiners could more than triple profits as Iran war sparks massive boom — MarketWatch Top, 2026-07-15. https://www.marketwatch.com/story/americas-oil-refiners-could-more-than-triple-profits-as-iran-war-sparks-massive-boom-c3ad5d33?mod=mw_rss_topstories
- Source: U.S. Crude Inventories Fall 1.7 Million Barrels As Iran Tensions Rattle Markets — OilPrice, 2026-07-15. https://oilprice.com/Energy/Crude-Oil/US-Crude-Inventories-Fall-17-Million-Barrels-As-Iran-Tensions-Rattle-Markets.html
- Source: Russia’s Oil Export Surge Runs Into a 135 Million-Barrel Traffic Jam — OilPrice, 2026-07-15. https://oilprice.com/Latest-Energy-News/World-News/Russias-Oil-Export-Surge-Runs-Into-a-135-Million-Barrel-Traffic-Jam.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

## Watchlist (below surfacing floor)
crypto · 2 series ↑ (5.1), dyn_kalyankjil_ns ↑ (5.03), midcap_largecap_ratio ↑ (4.95), dyn_blk ↑ (4.75), dyn_bac ↑ (4.59), gold_silver_ratio ↑ (4.49), dyn_pcjeweller_ns ↑ (4.49), dyn_atherenerg_ns ↑ (4.26), dyn_meta ↑ (4.22), usd_inr ↑ (4.15), dyn_biocon_bo ↑ (4.13), natgas ↓ (3.99)

## India macro
- nifty_50: 24073.4492 (1d 0.09%, z20 -0.06, flag none)
- nifty_midcap_100: 63001.5508 (1d 0.36%, z20 1.74, flag amber)
- usd_inr: 96.2450 (1d -0.06%, z20 2.15, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6171 (1d 0.27%, z20 1.95, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 54.7 — "Nifty 50 above 27,000? PL Capital raises target, sees more upside in Indian stock markets "
- HDB (HDFC Bank Limited) score 52.0 — "HDFC AMC Q1 Results: Net profit rises 12% to Rs 837 crore, revenue up 14%"
- INOXINDIA.NS (INOX INDIA LIMITED) score 47.6 — "Nifty 50 above 27,000? PL Capital raises target, sees more upside in Indian stock markets "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.6 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- COIN (Coinbase Global, Inc.) score 42.4 — "Global Market: Foreign investors add $132 billion to US securities in May as equity demand"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.7 — "India bonds recover on softer US rate outlook; oil risk caps gains"
- BAC (Bank of America Corporation) score 22.3 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- CHKP (Check Point Software Technolog) score 18.0 — "SBI Funds Management IPO Day 2: Issue booked 2.77x so far. Check GMP, key dates, issue det"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.9 — "Oil Prices Climb for Fourth Day as Iran Threatens New Energy Chokepoints"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 16.4 — "Market wrap: Eternal, UltraTech Cement among top gainers and losers on Nifty and Sensex to"
- VT (Vanguard Total World Stock Ind) score 12.8 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- SKHYV (SK hynix Inc. American Deposit) score 12.0 — "Global Market: SK Hynix jumps 13% as easing US inflation, AI memory optimism lift chip sto"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.9 — "101 equity mutual funds doubled money in 5 years; 4 did it in just 3 years. Should you inv"
- IDBI.NS (IDBI BANK LIMITED) score 7.5 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- MS (Morgan Stanley) score 6.9 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.7 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- META (Meta) score 6.4 — "Global Market: China Q2 growth slows to 4.3% yoy; Asia, metals stocks likely to remain vol"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 6.3 — "Tata Elxsi shares fall 5% as margin miss weighs on sentiment"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 6.2 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.1 — "PL Capital raises Nifty target to 27,019; favours banks, NBFCs, capital goods and defence"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.0 — "Adani ducks headwinds to record a huge jump in realty fortune; at cusp of being richest in"
- GS (Goldman Sachs Group, Inc. (The) score 4.8 — "Earnings Boost: Why Goldman Sachs shares jumped to record highs"
- PYPL (PayPal Holdings, Inc.) score 4.0 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BLK (BlackRock, Inc.) score 3.9 — "BlackRock assets hit record $15 trillion on boost from buoyant markets, ETF inflows"
- BIOCON.BO (BIOCON LTD.) score 3.8 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- SWIGGY.NS (SWIGGY LIMITED) score 3.3 — "Top Gainers & Losers on 14 July: HCL Tech, Ceat, Swiggy, Anant Raj, Newgen Software Tech a"
- NUVOCO.NS (NUVOCO VISTAS CORP LTD) score 2.9 — "Broker’s Call: Nuvoco Vistas (Accumulate)"
- MU (Micron Technology, Inc.) score 2.7 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- LGDS (JPMorgan Fundamental Data Scie) score 2.6 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- CUPID.NS (CUPID LIMITED) score 2.6 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.5 — "CUBA'S NATIONAL ELECTRIC GRID COLLAPSES, SAYS CUBA'S STATE MEDIA"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 2.1 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.9 — "Ather Energy shares rally 6% after Hero MotoCorp approves Rs 1,000 crore additional invest"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.9 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"
- JEF (Jefferies Financial Group Inc.) score 1.7 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- MCAP (MCAP Inc.) score 1.5 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.2 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- KNACK.BO (KNACK PACKAGING LIMITED) score 0.9 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 0.6 — "Is Broadcom stock a buy after Apple's massive chip pact?"
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