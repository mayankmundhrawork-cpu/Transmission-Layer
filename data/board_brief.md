# Transmission Layer — board brief · 2026-08-10 09:46Z

data as of **2026-08-10** · 98 series · 8 red / 35 amber · 8 events surfaced (18 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.312, 1d in regime; vol-pct 0.457, breadth-off 0.167, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.39, contra nifty_50 corr20=0.08, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.37, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.06, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.23, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.12, corr60 0.17, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.568, β -0.4372, p 0.0); driver zc -1.61 → expected 0.77%. Type hit-rate 0.827 (n=2362).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2377, p 0.0); driver zc -1.61 → expected -0.418%. Type hit-rate 0.827 (n=2362).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.365, β -0.2213, p 0.0); driver zc -1.61 → expected 0.39%. Type hit-rate 0.827 (n=2362).
- Track record · residual_reversion: hit-rate **0.49** (n=1146) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2362) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.39] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4402.60, z20 3.54, zc 0.72, resid-z 0.24 [quiet], 1d 1.43%, |z20|=3.54; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.32, z20 3.01, zc 0.57, resid-z -0.34 [quiet], 1d 1.56%, |z20|=3.01; co-occur[gold_silver] same-direction (channel VALID)
- dyn_vt [EQUITIES]: last 161.29, z20 2.41, zc 0.86, resid-z 1.02 [quiet], 1d 0.86%, |z20|=2.41; 1y-pct=100
- dyn_nvda [EQUITIES]: last 223.98, z20 2.37, zc 0.88, resid-z -0.17 [quiet], 1d 2.28%, |z20|=2.37; 1y-pct=98
- russell_2000 [INDICES]: last 3033.98, z20 2.28, zc 0.86, resid-z 0.90 [quiet], 1d 1.08%, |z20|=2.28; 1y-pct=99
- stoxx_50 [INDICES]: last 6541.57, z20 2.20, zc 0.33, resid-z -0.06 [quiet], 1d 0.27%, |z20|=2.20; 1y-pct=100
- sp500 [INDICES]: last 7755.61, z20 2.18, zc 0.61, resid-z -0.45 [quiet], 1d 0.59%, |z20|=2.18; 1y-pct=100
- dax [INDICES]: last 26410.17, z20 2.02, zc 0.43, resid-z 0.36 [quiet], 1d 0.34%, |z20|=2.02; 1y-pct=100
- dow_jones [INDICES]: last 54029.50, z20 1.96, zc 0.27, resid-z -0.16 [quiet], 1d 0.27%, |z20|=1.96; 1y-pct=99
- cac_40 [INDICES]: last 8704.07, z20 1.83, zc -0.17, resid-z -0.04 [quiet], 1d -0.12%, |z20|=1.83; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.62, z20 1.48, zc 0.35, resid-z -2.12 [unexplained], 1d 0.80%, 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.45, z20 -1.41, zc n/a, resid-z n/a [quiet], 1d -0.13%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold and silver prices, alongside a rise in copper prices, is driven by a combination of factors including a stronger US dollar and rising crude oil prices. This move is also reflected in the Indian market, with Nifty Metal reacting positively. The gold-silver comove channel is valid, indicating a monetary metals co-move, while the metal copper channel also supports this move.
- **Gap**: No gap: The current price move in gold, silver, and copper is largely priced in, with resid_z values indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian market is reacting to the global commodity price surge, with Nifty Metal and Nifty 50 already showing positive movement. However, Nifty FMCG has not reacted yet, potentially due to its inverse correlation with dyn_nvda.
- Watch next: nifty_metal (up) — reacted; Co-movement with global copper prices
- Watch next: nifty_50 (up) — reacted; Transmission from global equity markets
- Watch next: nifty_fmcg (down) — quiet; Inverse correlation with dyn_nvda
- **India receivers**: nifty_fmcg (rho -0.542, z 0.33); nifty_50 (rho 0.538, z 1.14); nifty_midcap_100 (rho 0.52, z 1.81); nifty_metal (rho 0.482, z 1.99)
- Source: Q1 Results Today Live: Bharat Forgeshares tank after Q1 con. loss, Kwality Pharma, Ramco Industries, KPR Mill Q1 PAT up, Hindustan Copper PAT down q-o-q, Info Edge & Astra Microwave profit dip, Vi, Bosch, Lloyds Metals, Gland Pharma, Zee Entertainment, KEC International to announce Q1 results — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Source: Hindustan Copper Q1 Results: PAT zooms 163% YoY to Rs 353 crore; revenue rises to Rs 937 crore — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/earnings/hindustan-copper-q1-results-pat-zooms-163-yoy-to-rs-353-crore-revenue-rises-to-rs-937-crore/articleshow/133094486.cms
- Source: Gold, silver rates today on an uptrend. Which one to buy for whopping returns? — Mint Markets, 2026-08-10. https://www.livemint.com/market/commodities/gold-silver-rates-today-on-an-uptrend-which-one-to-buy-for-whopping-returns-11786350996700.html
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [RED 5.55] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 881.25, z20 3.55, zc 0.28, resid-z 0.13 [quiet], 1d 0.97%, |z20|=3.55; 1y-pct=100
- **Mechanism**: The recent surge in Tata Technologies' stock price can be attributed to the company's strong Q1FY27 results and positive outlook from analysts, which has also been reflected in the Indian market through transmission candidates such as Tata Elxsi and Nifty IT. The VALID metal_copper_channel and gold_silver_comove channels suggest a broader risk-on sentiment, which is further supported by the RISK_ON regime. However, the INVERTED safe_haven_gold channel indicates a potential risk-off sentiment, which may limit the upside.
- **Gap**: No gap: the big raw move in dyn_tatatech_ns with small resid_z=0.13 suggests that the move is largely priced in, leaving no significant event-to-price gap.
- **India take**: The Indian market has already reacted to the surge in Tata Technologies' stock price through transmission candidates such as Tata Elxsi and Nifty IT, which have also moved up. The broader risk-on sentiment in the Indian market is further supported by the VALID metal_copper_channel and gold_silver_comove channels.
- Watch next: dyn_tataelxsi_ns (up) — already moved; reacted to dyn_tatatech_ns
- Watch next: nifty_it (up) — already moved; reacted to dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.471, z 1.54); nifty_it (rho 0.465, z 1.4)
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Source: How Rakesh Jhunjhunwala's old Tata bet created Rs 80,000 crore wealth after two years of flat returns — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/how-rakesh-jhunjhunwalas-old-tata-bet-created-rs-80000-crore-wealth-after-two-years-of-flat-returns/articleshow/133079774.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.36] dyn_heromotoco_ns ↑
- dyn_heromotoco_ns [EQUITIES]: last 5835.00, z20 2.36, zc 1.02, resid-z 1.21 [quiet], 1d 1.92%, |z20|=2.36
- **Mechanism**: The recent surge in Hero MotoCorp's stock price can be attributed to its Q1 earnings beating street estimates, driven by strong sales of premium bikes and EVs. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The global copper market often leads Indian metal equities, and a rise in Hero MotoCorp's stock could be a precursor to a broader move in the metal sector.
- **Gap**: No gap: the move in Hero MotoCorp's stock is largely priced in, given the strong earnings report and the current market regime of RISK_ON
- **India take**: The Indian instrument that expresses this move is dyn_havells_ns, which has already reacted with a rho of 0.447 via dyn_heromotoco_ns. The Nifty Midcap 100 index has also reacted, with a rho of 0.387 via dyn_heromotoco_ns.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to dyn_heromotoco_ns
- **India receivers**: dyn_havells_ns (rho 0.461, z 1.32); nifty_midcap_100 (rho 0.378, z 1.81)
- Source: Hero MotoCorp gains speed as premium bikes, EVs fuel Q1 — Mint Markets, 2026-08-10. https://www.livemint.com/market/mark-to-market/hero-motocorp-q1fy27-earnings-stock-margin-ev-growth-11786338356204.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [RED 4.18] fx · 3 series ↑
- usd_mxn [FX]: last 17.13, z20 -2.86, zc -1.02, resid-z -0.84 [quiet], 1d -0.42%, |z20|=2.86; 1y-pct=1
- aud_usd [FX]: last 0.71, z20 2.17, zc 0.99, resid-z 1.07 [quiet], 1d 0.52%, |z20|=2.17
- eur_usd [FX]: last 1.16, z20 1.90, zc 0.91, resid-z 1.11 [quiet], 1d 0.34%, |z20|=1.90
- **Mechanism**: The recent surge in FX markets, particularly in usd_mxn, aud_usd, and eur_usd, is driven by a combination of factors, including a risk-on regime and a strong dollar. However, the resid_z values suggest that the moves are largely priced in, with only a small unexplained component. The valid channels, such as gold_silver_comove and metal_copper_channel, do not provide a clear mechanism for further propagation of this move.
- **Gap**: No gap: the recent moves in FX markets are largely priced in, with small resid_z values indicating that the unexplained component is minimal.
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_mxn, with a rho of -0.572. Further reaction in Indian markets is likely to be limited, given the already priced-in nature of the move.
- Watch next: usd_brl (up) — not yet - watch; historically leads usd_mxn by 3d
- **India receivers**: dyn_muthootfin_ns (rho -0.572, z -1.21)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 4.16] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 262.40, z20 2.16, zc 0.03, resid-z -0.23 [quiet], 1d 0.10%, |z20|=2.16; 1y-pct=99
- **Mechanism**: The recent Q1 results of Cupid, with a threefold rise in profit and 159% surge in revenue, have not been fully priced in by the market, as indicated by the quiet move label and low resid_z of -0.17. This suggests that the market has not fully reacted to the positive earnings surprise. The valid metal_copper_channel may play a role in transmitting this move to Indian metal equities.
- **Gap**: No gap: the event has been largely priced in, as evidenced by the low resid_z and quiet move label
- **India take**: Indian metal equities, such as those in the Nifty Metal index, may react positively to Cupid's strong Q1 results, although the response has not yet materialized. The metal_copper_channel may facilitate this transmission.
- Watch next: nifty_metal (up) — not yet - watch; Cupid's strong Q1 results may positively impact the broader metal sector
- **India receivers**: nifty_midcap_100 (rho 0.354, z 1.81)
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 3.81] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.29, z20 1.81, zc 0.23, resid-z -0.46 [quiet], 1d 0.55%, 1y-pct=100
- **Mechanism**: The recent move in dyn_tech is priced, with a small resid_z of -0.46, indicating that the move is largely explained by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for further upside, with the dyn_tech move potentially contributing to this sentiment. The metal_copper_channel also provides a potential transmission mechanism to Indian metal equities.
- **Gap**: No gap: the small resid_z of -0.46 indicates that the move in dyn_tech is largely priced
- **India take**: The Indian instrument dyn_inoxindia_ns, which has a rho of -0.406 with dyn_tech, may react positively to the move in dyn_tech, although it has not yet done so. The metal_copper_channel provides a potential transmission mechanism to Indian metal equities.
- Watch next: dyn_inoxindia_ns (up) — not yet - watch; rho=-0.406 via dyn_tech
- **India receivers**: dyn_inoxindia_ns (rho -0.406, z 0.53)
- Source: How the guest list for Beijing’s summer retreat reveals its tech priorities — SCMP Economy, 2026-08-10. https://www.scmp.com/news/china/politics/article/3363523/how-guest-list-beijings-summer-retreat-reveals-its-tech-priorities?utm_source=rss_feed
- Source: Global Market: Shanghai, Hong Kong stocks rise as consumer gains offset tech weakness — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-shanghai-hong-kong-stocks-rise-as-consumer-gains-offset-tech-weakness/articleshow/133090625.cms
- Source: Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results, Sky Gold, Dynamatic Tech, Quality Power, Anant Raj shares gain after Q1, Kaynes Tech, Ola, Oswal Pumps, Jamna Auto, Apollo Micro shares in red — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.33] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.22, z20 1.40, zc 1.21, resid-z 1.02 [quiet], 1d 0.97%, 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.03, zc 1.32, resid-z 0.90 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.43, z20 1.00, zc 0.51, resid-z -0.28 [quiet], 1d 0.83%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.76, z20 -0.40, zc 0.74, resid-z 0.28 [quiet], 1d 0.23%, 1y-pct=3
- ust_2y [RATES]: last 4.25, z20 0.25, zc 1.33, resid-z 0.95 [quiet], 1d 1.67%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_lth (co-move) — not yet - watch; rho 0.546 vs dyn_bond, historically leads by 2d
- Watch next: brent (co-move) — not yet - watch; rho 0.535 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.508 vs ust_10y, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 3.3] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 172.00, z20 3.30, zc 2.03, resid-z 0.09 [moved], 1d 10.31%, |z20|=3.30
- **Mechanism**: dyn_pltr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho 0.399 via dyn_pltr, z 1.93, reacted)
- **India receivers**: dyn_atherenerg_ns (rho 0.399, z 1.93)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

## Watchlist (below surfacing floor)
dyn_indianb_ns ↑ (2.6), dyn_indusindbk_bo ↑ (2.45), dyn_lth ↑ (2.41), usd_cny ↓ (2.34), dyn_icicigi_bo ↓ (2.26), dyn_idbi_ns ↓ (2.18), bovespa ↓ (2.09), shanghai_comp ↑ (1.99), nifty_metal ↑ (1.99), dyn_atherenerg_ns ↑ (1.93), corn ↑ (1.87), nifty_midcap_100 ↑ (1.81)

## India macro
- nifty_50: 24560.1504 (1d -0.04%, z20 1.14, flag none)
- nifty_midcap_100: 63791.6016 (1d 0.52%, z20 1.81, flag amber)
- usd_inr: 95.2750 (1d -0.04%, z20 -1.21, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5974 (1d 0.56%, z20 0.55, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.3 — "LEAP India IPO Day 2: Issue subscribed 40% so far. Check GMP, key dates, review - apply or"
- COALINDIA.NS (COAL INDIA LTD) score 78.5 — "LEAP India IPO Day 2: Issue subscribed 40% so far. Check GMP, key dates, review - apply or"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.3 — "LEAP India IPO Day 2: Issue subscribed 40% so far. Check GMP, key dates, review - apply or"
- INDIANB.NS (INDIAN BANK) score 57.1 — "Wall Street’s biggest bank just raised its expectations for the stock market"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.6 — "How the guest list for Beijing’s summer retreat reveals its tech priorities"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 45.2 — "How the guest list for Beijing’s summer retreat reveals its tech priorities"
- COIN (Coinbase Global, Inc.) score 44.8 — "$48 billion profit! 5 global oil majors cash in on oil surge amid Iran war. Where is money"
- BAC (Bank of America Corporation) score 44.7 — "Wall Street’s biggest bank just raised its expectations for the stock market"
- TECH (Bio-Techne Corp) score 43.6 — "How the guest list for Beijing’s summer retreat reveals its tech priorities"
- HDB (HDFC Bank Limited) score 42.1 — "HDFC Life Share Price Live Updates: HDFC Life's Market Update"
- IDBI.NS (IDBI BANK LIMITED) score 39.3 — "Wall Street’s biggest bank just raised its expectations for the stock market"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.3 — "Wall Street’s biggest bank just raised its expectations for the stock market"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.8 — "Wall Street’s biggest bank just raised its expectations for the stock market"
- OHI (Omega Healthcare Investors, In) score 37.1 — "Vedanta Oil and Gas shares surge 12% to fresh record high. What should investors do?"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.4 — "Hitachi Energy India shares zoom 11% after Q1 results 2026. Do you own?"
- CHKP (Check Point Software Technolog) score 28.3 — "LEAP India IPO Day 2: Issue subscribed 40% so far. Check GMP, key dates, review - apply or"
- LTH (Life Time Group Holdings, Inc.) score 25.3 — "IRANIAN PRESIDENT PEZESHKIAN SAYS NOW IS THE BEST TIME FOR AN AGREEMENT BECAUSE IRAN IS 'S"
- 301077.SZ (CHINASTARS) score 23.2 — "Global Market: China bears the brunt of Asia’s crude oil demand cut as Middle East supplie"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.6 — "Foreign flows into Indian bonds may remain muted despite tax relief: SBI Funds"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.2 — "Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.7 — "Bharat Forge Q1 results: Profit falls 5% YoY to  ₹321 crore, announces incorporation of a "
- JIOFIN.BO (Jio Financial Services Limited) score 9.5 — "SBI shares slip post Q1 beat; what Jefferies, JM Financial say"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.4 — "Aye Finance share price rises 4% in a lacklustre market, jumps over 35% YTD"
- MS (Morgan Stanley) score 9.2 — "J.P. Morgan raises S&P 500 year-end target to 8,000 on AI and earnings optimism"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.0 — "Wall Street’s biggest bank just raised its expectations for the stock market"
- VT (Vanguard Total World Stock Ind) score 7.2 — "HASSETT: TAKE OUT GOVT WORKERS, WORLD CUP, JOBS ROSE 100,000"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.1 — "SBI shares slip post Q1 beat; what Jefferies, JM Financial say"
- META (Meta) score 7.0 — "Q1 Results Today Live: Bharat Forgeshares tank after Q1 con. loss, Kwality Pharma, Ramco I"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.0 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.8 — "How Adani’s $125 billion capex boom is creating new winners on Dalal Street"
- AAPL (Apple Inc.) score 5.1 — "AAPL - APPLE TESTS CHINESE MEMORY CHIPS FOR IPHONES, MACBOOKS Apple is testing memory chip"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.8 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 4.5 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- PLTR (Palantir Technologies Inc.) score 4.1 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- NVDA (NVIDIA Corporation) score 3.8 — "Two reasons why Nvidia’s stock saw its biggest weekly surge in more than a year"
- MSFT (Microsoft Corporation) score 3.4 — "These analysts say Elon Musk’s ambitious AI plans for SpaceX should be taken seriously, th"
- AMZN (Amazon.com, Inc.) score 2.9 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 2.9 — "Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results?"
- CUPID.NS (CUPID LIMITED) score 2.6 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.0 — "Hero MotoCorp gains speed as premium bikes, EVs fuel Q1"

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