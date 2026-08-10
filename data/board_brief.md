# Transmission Layer — board brief · 2026-08-10 08:03Z

data as of **2026-08-10** · 98 series · 7 red / 33 amber · 7 events surfaced (16 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.322, 1d in regime; vol-pct 0.478, breadth-off 0.167, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.39, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.37, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.06, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.23, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.12, corr60 0.17, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.568, β -0.4371, p 0.0); driver zc -1.61 → expected 0.77%. Type hit-rate 0.827 (n=2362).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.395, β 0.2375, p 0.0); driver zc -1.61 → expected -0.418%. Type hit-rate 0.827 (n=2362).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.365, β -0.2213, p 0.0); driver zc -1.61 → expected 0.39%. Type hit-rate 0.827 (n=2362).
- Track record · residual_reversion: hit-rate **0.493** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2362) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.33] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4416.00, z20 3.68, zc 0.87, resid-z 0.24 [quiet], 1d 1.73%, |z20|=3.68; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.47, z20 3.09, zc 0.65, resid-z -0.48 [quiet], 1d 1.80%, |z20|=3.09; co-occur[gold_silver] same-direction (channel VALID)
- dyn_vt [EQUITIES]: last 161.29, z20 2.41, zc 0.86, resid-z 1.02 [quiet], 1d 0.86%, |z20|=2.41; 1y-pct=100
- dyn_nvda [EQUITIES]: last 223.98, z20 2.37, zc 0.88, resid-z -0.17 [quiet], 1d 2.28%, |z20|=2.37; 1y-pct=98
- russell_2000 [INDICES]: last 3033.98, z20 2.28, zc 0.86, resid-z 0.90 [quiet], 1d 1.08%, |z20|=2.28; 1y-pct=99
- sp500 [INDICES]: last 7755.61, z20 2.18, zc 0.61, resid-z -0.45 [quiet], 1d 0.59%, |z20|=2.18; 1y-pct=100
- stoxx_50 [INDICES]: last 6535.17, z20 2.13, zc 0.21, resid-z -0.06 [quiet], 1d 0.17%, |z20|=2.13; 1y-pct=100
- dow_jones [INDICES]: last 54029.50, z20 1.96, zc 0.27, resid-z -0.16 [quiet], 1d 0.27%, |z20|=1.96; 1y-pct=99
- dax [INDICES]: last 26367.21, z20 1.93, zc 0.23, resid-z 0.36 [quiet], 1d 0.18%, |z20|=1.93; 1y-pct=100
- cac_40 [INDICES]: last 8715.77, z20 1.92, zc 0.01, resid-z -0.04 [quiet], 1d 0.01%, |z20|=1.92; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.65, z20 1.64, zc 0.51, resid-z -2.12 [unexplained], 1d 1.14%, |z20|=1.64; 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.50, z20 -1.35, zc n/a, resid-z n/a [quiet], 1d -0.06%, GSR<75 (extreme low)
- **Mechanism**: The recent move in global equities and commodities is driven by the improved earnings outlook and AI-driven revenue growth, as highlighted by J.P. Morgan's raised S&P 500 year-end target to 8,000. This optimism is transmitted to Indian markets through correlated instruments such as Nifty 50 and Nifty Midcap 100. The VALID gold_silver_comove and metal_copper_channel also support the current move.
- **Gap**: No gap: The current move in global equities and commodities is largely priced in, with small resid_z values indicating that the move is explained by factor exposures.
- **India take**: Indian instruments such as Nifty 50 and Nifty Midcap 100 have already reacted to the global equity move, while Nifty FMCG has not yet reacted and is worth watching. The metal sector, represented by Nifty Metal, has also reacted to the global metal move.
- Watch next: nifty_50 (up) — reacted; Already reacted to global equity move
- Watch next: nifty_metal (up) — reacted; Already reacted to global metal move
- Watch next: nifty_fmcg (up) — not yet - watch; Has not yet reacted to global equity move
- **India receivers**: nifty_fmcg (rho -0.543, z 0.54); nifty_50 (rho 0.538, z 1.24); nifty_midcap_100 (rho 0.516, z 2.09); nifty_metal (rho 0.483, z 2.05)
- Source: Q1 Results Today Live: Kwality Pharma, Ramco Industries Q1 PAT up, Vi, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Source: J.P. Morgan raises S&P 500 year-end target to 8,000 on AI and earnings optimism — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/jp-morgan-raises-sp-500-year-end-target-to-8000-on-ai-and-earnings-optimism/article71327198.ece
- Source: Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results, Sky Gold, Dynamatic Tech, Quality Power, Anant Raj shares gain after Q1, Kaynes Tech, Ola, Oswal Pumps, Jamna Auto, Apollo Micro shares in red — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [RED 4.51] dyn_heromotoco_ns ↑
- dyn_heromotoco_ns [EQUITIES]: last 5876.50, z20 2.51, zc 1.40, resid-z 1.61 [unexplained], 1d 2.65%, |z20|=2.51
- **Mechanism**: The recent surge in Hero MotoCorp's stock price can be attributed to its Q1 earnings beating street estimates, driven by strong sales of premium bikes and EVs. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The global copper market often leads Indian metal equities, and a rise in Hero MotoCorp's stock could be a precursor to a broader move in the metal sector.
- **Gap**: No gap: the move in Hero MotoCorp's stock is largely priced in, given the strong earnings report and the current market regime of RISK_ON
- **India take**: The Indian instrument that expresses this move is dyn_havells_ns, which has already reacted with a rho of 0.447 via dyn_heromotoco_ns. The Nifty Midcap 100 index has also reacted, with a rho of 0.387 via dyn_heromotoco_ns.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to dyn_heromotoco_ns
- **India receivers**: dyn_havells_ns (rho 0.447, z 1.23); nifty_midcap_100 (rho 0.387, z 2.09)
- Source: Hero MotoCorp gains speed as premium bikes, EVs fuel Q1 — Mint Markets, 2026-08-10. https://www.livemint.com/market/mark-to-market/hero-motocorp-q1fy27-earnings-stock-margin-ev-growth-11786338356204.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [RED 4.19] fx · 3 series ↑
- usd_mxn [FX]: last 17.13, z20 -2.87, zc -1.03, resid-z -0.83 [quiet], 1d -0.42%, |z20|=2.87; 1y-pct=1
- aud_usd [FX]: last 0.71, z20 2.27, zc 1.09, resid-z 1.17 [quiet], 1d 0.56%, |z20|=2.27
- eur_usd [FX]: last 1.16, z20 1.90, zc 0.91, resid-z 1.09 [quiet], 1d 0.34%, |z20|=1.90
- **Mechanism**: The recent move in FX markets, particularly in usd_mxn, aud_usd, and eur_usd, is driven by a combination of factors, including a risk-on regime and correlated instrument movements. However, the resid_z values indicate that the moves are largely priced, with only small unexplained components. The metal_copper_channel and gold_silver_comove channels are valid and may play a role in transmitting the move to Indian markets.
- **Gap**: No gap: the moves in usd_mxn, aud_usd, and eur_usd are largely priced, with small resid_z values indicating that the unexplained component is minimal
- **India take**: The Indian instrument dyn_muthootfin_ns, which is correlated with usd_mxn, has not yet reacted to the move. However, given the valid metal_copper_channel, Indian metal equities may be affected.
- Watch next: usd_mxn (down) — already moved; resid_z is small, indicating a priced move
- **India receivers**: dyn_muthootfin_ns (rho -0.575, z -0.99)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 4.1] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 261.45, z20 2.10, zc -0.06, resid-z -0.44 [quiet], 1d -0.26%, |z20|=2.10; 1y-pct=99
- **Mechanism**: The recent Q1 results of Cupid, with a threefold rise in profit and 159% surge in revenue, have not been fully priced in by the market, as indicated by the quiet move label and low resid_z of -0.17. This suggests that the market has not fully reacted to the positive earnings surprise. The valid metal_copper_channel may play a role in transmitting this move to Indian metal equities.
- **Gap**: No gap: the event has been largely priced in, as evidenced by the low resid_z and quiet move label
- **India take**: Indian metal equities, such as those in the Nifty Metal index, may react positively to Cupid's strong Q1 results, although the response has not yet materialized. The metal_copper_channel may facilitate this transmission.
- Watch next: nifty_metal (up) — not yet - watch; Cupid's strong Q1 results may positively impact the broader metal sector
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 3.81] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.29, z20 1.81, zc 0.23, resid-z -0.46 [quiet], 1d 0.55%, 1y-pct=100
- **Mechanism**: The dyn_tech move is driven by a quiet, priced move with a small resid_z, indicating that the current price level is largely explained by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential equity upside, supported by the historical analogue aftermath of dyn_tech, which shows a +20d median return of 2.55%. The metal_copper_channel also provides a potential transmission mechanism for the move to affect Indian metal equities.
- **Gap**: No gap: the dyn_tech move is largely priced, with a small resid_z of -0.46, indicating that the current price level is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is dyn_inoxindia_ns, which has a rho of -0.406 with dyn_tech and is currently quiet. The move may affect Indian metal equities via the metal_copper_channel.
- Watch next: dyn_inoxindia_ns (up) — not yet - watch; rho=-0.406 via dyn_tech
- **India receivers**: dyn_inoxindia_ns (rho -0.406, z 0.38)
- Source: Global Market: Shanghai, Hong Kong stocks rise as consumer gains offset tech weakness — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-shanghai-hong-kong-stocks-rise-as-consumer-gains-offset-tech-weakness/articleshow/133090625.cms
- Source: Q1 Results Today Live: Vodafone Idea, Bosch, Lloyds Metals, Bharat Forge, Gland Pharma, Zee Entertainment, Hindustan Copper, KEC International to announce Q1 results, Sky Gold, Dynamatic Tech, Quality Power, Anant Raj shares gain after Q1, Kaynes Tech, Ola, Oswal Pumps, Jamna Auto, Apollo Micro shares in red — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-vodafone-idea-bosch-lloyds-metals-bharat-forge-gland-pharma-zee-entertainment-hindustan-copper-kec-international-results-10-august-2026/article71317192.ece
- Source: Nifty opens flat as Titan, Tech Mahindra lead gains; markets eye US inflation data — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/nifty-opens-flat-as-titan-tech-mahindra-lead-gains-markets-eye-us-inflation-data/article71326945.ece
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
- Watch next: brent (co-move) — not yet - watch; rho 0.536 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.508 vs ust_10y, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 3.3] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 172.00, z20 3.30, zc 2.03, resid-z 0.09 [moved], 1d 10.31%, |z20|=3.30
- **Mechanism**: dyn_pltr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho 0.399 via dyn_pltr, z 1.92, reacted)
- **India receivers**: dyn_atherenerg_ns (rho 0.399, z 1.92)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

## Watchlist (below surfacing floor)
dyn_indianb_ns ↑ (2.49), dyn_lth ↑ (2.41), dyn_icicigi_bo ↓ (2.36), usd_cny ↓ (2.21), bovespa ↓ (2.09), nifty_midcap_100 ↑ (2.09), dyn_indusindbk_bo ↑ (2.06), nifty_metal ↑ (2.05), shanghai_comp ↑ (1.99), dyn_atherenerg_ns ↑ (1.92), corn ↑ (1.9), asx_200 ↑ (1.78)

## India macro
- nifty_50: 24588.4492 (1d 0.07%, z20 1.24, flag none)
- nifty_midcap_100: 63943.3984 (1d 0.76%, z20 2.09, flag amber)
- usd_inr: 95.2500 (1d -0.06%, z20 -1.25, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6005 (1d 0.69%, z20 0.78, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.6 — "From infrastructure to energy storage: The expanding role of zinc in India’s development j"
- COALINDIA.NS (COAL INDIA LTD) score 75.8 — "From infrastructure to energy storage: The expanding role of zinc in India’s development j"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.5 — "From infrastructure to energy storage: The expanding role of zinc in India’s development j"
- INDIANB.NS (INDIAN BANK) score 57.1 — "ISRAEL'S NETANYAHU: AS LONG AS I AM PRIME MINISTER, THERE WILL BE NO PALESTINIAN STATE IN "
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.4 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Current Price and Market Perfor"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 45.0 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Current Price and Market Perfor"
- BAC (Bank of America Corporation) score 44.4 — "ISRAEL'S NETANYAHU: AS LONG AS I AM PRIME MINISTER, THERE WILL BE NO PALESTINIAN STATE IN "
- COIN (Coinbase Global, Inc.) score 43.5 — "AAPL - APPLE TURNS TO CHINA AS CHIP SHORTAGE BITES Apple is testing memory chips from Chin"
- TECH (Bio-Techne Corp) score 43.4 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Current Price and Market Perfor"
- HDB (HDFC Bank Limited) score 40.8 — "ISRAEL'S NETANYAHU: AS LONG AS I AM PRIME MINISTER, THERE WILL BE NO PALESTINIAN STATE IN "
- IDBI.NS (IDBI BANK LIMITED) score 39.0 — "ISRAEL'S NETANYAHU: AS LONG AS I AM PRIME MINISTER, THERE WILL BE NO PALESTINIAN STATE IN "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.9 — "ISRAEL'S NETANYAHU: AS LONG AS I AM PRIME MINISTER, THERE WILL BE NO PALESTINIAN STATE IN "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.4 — "ISRAEL'S NETANYAHU: AS LONG AS I AM PRIME MINISTER, THERE WILL BE NO PALESTINIAN STATE IN "
- OHI (Omega Healthcare Investors, In) score 35.6 — "Molbio Diagnostics raises ₹281 cr from anchor investors ahead of IPO"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.0 — "Hitachi Energy jumps 7% after Q1 results. Here's why Nomura initiated coverage on stock"
- CHKP (Check Point Software Technolog) score 27.8 — "Milky Mist Dairy Food IPO opens tomorrow, GMP signals 20% listing gain. Check price band, "
- LTH (Life Time Group Holdings, Inc.) score 25.7 — "IRANIAN PRESIDENT PEZESHKIAN SAYS NOW IS THE BEST TIME FOR AN AGREEMENT BECAUSE IRAN IS 'S"
- 301077.SZ (CHINASTARS) score 21.6 — "AAPL - APPLE TURNS TO CHINA AS CHIP SHORTAGE BITES Apple is testing memory chips from Chin"
- BOND (PIMCO Active Bond Exchange-Tra) score 19.0 — "Foreign flows into Indian bonds may remain muted despite tax relief: SBI Funds"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.4 — "Tata Consumer Share Price Live Updates: Tata Consumer's Performance Overview"
- JIOFIN.BO (Jio Financial Services Limited) score 9.7 — "SBI shares slip post Q1 beat; what Jefferies, JM Financial say"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.5 — "Aye Finance share price rises 4% in a lacklustre market, jumps over 35% YTD"
- MS (Morgan Stanley) score 9.4 — "J.P. Morgan raises S&P 500 year-end target to 8,000 on AI and earnings optimism"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.1 — "SpaceX’s stock just had one of its best days ever — with the first lockup expiration now b"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.8 — "Q1 Results Today Live: Kwality Pharma, Ramco Industries Q1 PAT up, Vi, Bosch, Lloyds Metal"
- VT (Vanguard Total World Stock Ind) score 7.4 — "HASSETT: TAKE OUT GOVT WORKERS, WORLD CUP, JOBS ROSE 100,000"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.2 — "SBI shares slip post Q1 beat; what Jefferies, JM Financial say"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.1 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- META (Meta) score 6.1 — "Alphabet vs Meta: Which stock is the better long-term bet?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "How Adani’s $125 billion capex boom is creating new winners on Dalal Street"
- AAPL (Apple Inc.) score 5.2 — "AAPL - APPLE TESTS CHINESE MEMORY CHIPS FOR IPHONES, MACBOOKS Apple is testing memory chip"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.8 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 4.6 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- PLTR (Palantir Technologies Inc.) score 4.1 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- NVDA (NVIDIA Corporation) score 3.8 — "Two reasons why Nvidia’s stock saw its biggest weekly surge in more than a year"
- AMZN (Amazon.com, Inc.) score 3.0 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 2.7 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"
- MSFT (Microsoft Corporation) score 2.5 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- SNDK (Sandisk Corporation) score 2.1 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
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