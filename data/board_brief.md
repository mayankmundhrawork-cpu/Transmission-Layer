# Transmission Layer — board brief · 2026-09-15 14:59Z

data as of **2026-09-15** · 97 series · 25 red / 33 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.749, 1d in regime; vol-pct 0.616, breadth-off 0.882, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.56, corr60 -0.3, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.06, corr60 0.09, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.84, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.15, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.17, corr60 0.14, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2069) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 12.16] cross-asset · 18 series ↓
- dyn_ms [EQUITIES]: last 202.38, z20 -3.88, zc -1.05, resid-z -0.11 [quiet], 1d -2.03%, |z20|=3.88
- tips_10y_real [RATES]: last 2.60, z20 3.69, zc 1.10, resid-z 1.46 [quiet], 1d 1.96%, 1d move +5.0bps ≥ 5bps; |z20|=3.69; 1y-pct=100
- ust_2y [RATES]: last 4.63, z20 3.12, zc 1.16, resid-z 1.39 [quiet], 1d 1.54%, |z20|=3.12; 1y-pct=100
- ust_10y [RATES]: last 4.96, z20 3.00, zc 0.20, resid-z 0.38 [quiet], 1d 0.20%, |z20|=3.00; 1y-pct=100
- dyn_vt [EQUITIES]: last 157.71, z20 -2.99, zc -0.78, resid-z 0.03 [quiet], 1d -0.64%, |z20|=2.99
- stoxx_50 [INDICES]: last 6230.25, z20 -2.63, zc -0.51, resid-z -0.64 [quiet], 1d -0.48%, |z20|=2.63
- dow_jones [INDICES]: last 51895.78, z20 -2.61, zc -1.24, resid-z -2.31 [unexplained], 1d -1.00%, |z20|=2.61
- sp500 [INDICES]: last 7577.39, z20 -2.44, zc -0.73, resid-z -0.05 [quiet], 1d -0.56%, |z20|=2.44
- wti [COMMODITIES]: last 104.13, z20 2.33, zc 0.92, resid-z 0.54 [quiet], 1d 2.70%, 1-session move +2.70% ≥ 1.5%; |z20|=2.33; 1y-pct=96
- vix [INDICES]: last 17.58, z20 2.29, zc 0.32, resid-z n/a [quiet], 1d 2.81%, |z20|=2.29
- ust_30y [RATES]: last 5.35, z20 2.27, zc -0.47, resid-z -0.34 [quiet], 1d -0.37%, |z20|=2.27; 1y-pct=99
- russell_2000 [INDICES]: last 2866.49, z20 -2.27, zc -0.76, resid-z -0.70 [quiet], 1d -0.89%, |z20|=2.27
- dyn_bond [EQUITIES]: last 88.64, z20 -2.24, zc -0.36, resid-z -0.80 [quiet], 1d -0.12%, |z20|=2.24; 1y-pct=0
- cac_40 [INDICES]: last 8084.03, z20 -2.04, zc -0.46, resid-z -0.79 [quiet], 1d -0.42%, |z20|=2.04
- dax [INDICES]: last 25396.93, z20 -1.99, zc -0.19, resid-z -0.10 [quiet], 1d -0.17%, |z20|=1.99
- nasdaq_100 [INDICES]: last 28941.60, z20 -1.85, zc -0.61, resid-z -0.62 [quiet], 1d -0.64%, |z20|=1.85
- ftse_100 [INDICES]: last 10659.70, z20 -1.52, zc -0.57, resid-z -0.97 [quiet], 1d -0.35%, |z20|=1.52
- brent [COMMODITIES]: last 102.91, z20 1.36, zc -0.89, resid-z -1.34 [quiet], 1d -2.62%, 1-session move -2.62% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: cross-asset · 18 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.517 via ftse_100, z -1.12, reacted); nifty_midcap_100 (rho 0.477 via dax, z -4.2, reacted); dyn_techm_ns (rho 0.419 via ftse_100, z -0.31, quiet); midcap_largecap_ratio (rho -0.397 via ust_2y, z -0.81, quiet); nifty_50 (rho 0.386 via ftse_100, z -3.0, reacted)
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.557 vs sp500, historically leads by 1d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.508 vs cac_40, historically leads by 5d
- **India receivers**: nifty_it (rho 0.517, z -1.12); nifty_midcap_100 (rho 0.477, z -4.2); dyn_techm_ns (rho 0.419, z -0.31); midcap_largecap_ratio (rho -0.397, z -0.81)
- Source: Shutting down East-West pipeline making crude oil more expensive for Indian refiners — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/commodities/shutting-down-east-west-pipeline-making-crude-oil-more-expensive-for-indian-refiners/article71468752.ece
- Source: Why one Wall Street firm thinks this year’s stock-market rally is running out of road — MarketWatch Top, 2026-09-15. https://www.marketwatch.com/story/wells-fargo-just-cuts-its-s-p-500-price-target-will-others-follow-e32f968a?mod=mw_rss_topstories
- Source: Bond yields hit 4-month high as RBI OMO sales, global headwinds weigh — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/stock-markets/bond-yields-hit-4-month-high-as-rbi-omo-sales-global-headwinds-weigh/article71468684.ece

### [RED 8.86] cross-asset · 4 series ↓
- india_vix [INDICES]: last 13.47, z20 5.20, zc 0.74, resid-z n/a [quiet], 1d 9.56%, |z20|=5.20
- nifty_midcap_100 [INDICES]: last 60876.10, z20 -4.20, zc -0.40, resid-z -0.44 [quiet], 1d -2.12%, |z20|=4.20
- nifty_50 [INDICES]: last 23118.60, z20 -3.00, zc -0.61, resid-z -0.80 [quiet], 1d -1.19%, |z20|=3.00; 1y-pct=4
- dyn_jiofin_bo [EQUITIES]: last 226.00, z20 -2.50, zc -0.35, resid-z 0.41 [quiet], 1d -1.74%, |z20|=2.50; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.622 via nifty_50, z -1.86, reacted); dyn_indianb_ns (rho 0.554 via nifty_midcap_100, z -3.34, reacted); nifty_it (rho 0.51 via nifty_50, z -1.12, reacted); dyn_indusindbk_bo (rho 0.464 via nifty_50, z -3.42, reacted); dyn_techm_ns (rho 0.463 via nifty_50, z -0.31, quiet)
- **India receivers**: nifty_fmcg (rho 0.622, z -1.86); dyn_indianb_ns (rho 0.554, z -3.34); nifty_it (rho 0.51, z -1.12); dyn_indusindbk_bo (rho 0.464, z -3.42)
- Source: Crude shock, bond jitters send Sensex, Nifty into a rout — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/crude-shock-bond-jitters-send-sensex-nifty-into-a-rout/article71468059.ece
- Source: Expert View: Don’t wait for Nifty to stabilise, buy the dip, says Shweta Rajani of Anand Rathi Wealth — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/expert-view-don-t-wait-for-nifty-to-stabilise-buy-the-dip-says-shweta-rajani-of-anand-rathi-wealth-11789471660373.html
- Source: CAS crash: Nifty plunges 462 points in less than 30 seconds. Will Sebi’s review break trend? — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/stocks/news/cas-crash-nifty-plunges-462-points-in-less-than-30-seconds-will-sebis-review-break-trend/articleshow/134260167.cms
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 7.4] brent_wti_spread ↓
- brent_wti_spread [DERIVED]: last -1.22, z20 -7.40, zc n/a, resid-z n/a [quiet], 1d -128.44%, |z20|=7.40; 1y-pct=2
- **Mechanism**: brent_wti_spread ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho -0.41 via brent_wti_spread, z 0.37, quiet)
- **India receivers**: eur_inr (rho -0.41, z 0.37)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-04 (d=0.0), 2026-05-06 (d=0.01)

### [RED 6.64] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4320.20, z20 -1.92, zc -0.58, resid-z -0.61 [quiet], 1d -0.73%, |z20|=1.92; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 63.74, z20 -1.56, zc 0.13, resid-z 1.02 [quiet], 1d 0.35%, |z20|=1.56; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.78, z20 0.32, zc n/a, resid-z n/a [quiet], 1d -1.07%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.703 vs comex_gold, historically leads by 5d
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.636 vs comex_gold, historically leads by 5d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.535 vs comex_gold, historically leads by 4d
- Source: Hindustan Zinc, GMDC, NMDC to Vedanta | 6 stocks that could strike gold in India’s big critical minerals push — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/hindustan-zinc-gmdc-nmdc-to-vedanta-6-stocks-that-could-strike-gold-in-india-s-big-critical-minerals-push-11789471241301.html
- Source: TCS partners with Dubai Gold & Commodities Exchange for next-gen derivatives market infrastructure — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/commodities/tcs-partners-with-dubai-gold-commodities-exchange-for-next-gen-derivatives-market-infrastructure/article71467785.ece
- Source: Today’s Gold Rate: Latest gold prices in Coimbatore, Nagpur, Jaipur & other cities — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-september-15-2026/article71467231.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 6.38] usd_inr ↑
- usd_inr [FX]: last 95.94, z20 1.38, zc 1.66, resid-z 2.06 [unexplained], 1d 0.96%, 20d range extreme; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Rupee slumps 38 paise to close at 95.92 against US dollar — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/forex/rupee-slumps-38-paise-to-close-at-95-92-against-us-dollar/articleshow/134259296.cms
- Source: Rupee drops with stocks, bonds as oil, inflation and Fed worries mount — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rupee-drops-with-stocks-bonds-as-oil-inflation-and-fed-worries-mount/article71467588.ece
- Source: RBI likely intervened to shield rupee as oil prices climb, traders say — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rbi-likely-intervened-to-shield-rupee-as-oil-prices-climb-traders-say/article71466683.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 6.08] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5360.00, z20 4.08, zc 1.56, resid-z -0.59 [moved], 1d 8.83%, |z20|=4.08; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: From VBL, Power Grid to Paytm - 6 stocks experts recommend buying for the short term; do you own any? — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/from-vbl-power-grid-to-paytm-6-stocks-experts-recommend-buying-for-the-short-term-do-you-own-any-11789451473678.html
- Source: HDFC Bank share price jumps over 6% in 3 days | Experts see 15% more upside, check target price — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-jumps-over-6-in-3-days-experts-see-15-more-upside-check-target-price-11789444548891.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 5.08] dyn_jef ↓
- dyn_jef [EQUITIES]: last 48.99, z20 -3.08, zc -0.81, resid-z -1.87 [unexplained], 1d -2.22%, |z20|=3.08
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Even Nikhil Kamath is a YouTuber! Jefferies calls Zerodha co-founder a ‘renowned YouTube Podcaster’ - Why this matters? — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/even-nikhil-kamath-is-a-youtuber-jefferies-calls-zerodha-co-founder-a-renowned-youtube-podcaster-why-this-matters-11789460259445.html
- Source: Coforge shares fall over 3%. What are Jefferies, Emkay saying after Chairman, independent director exit? — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/stocks/news/coforge-shares-fall-over-3-what-are-jefferies-emkay-saying-after-chairman-independent-director-exit/articleshow/134256354.cms
- Source: HDFC Bank share price target: What are Jefferies, 3 other foreign brokerages saying as CEO hunt intensifies? — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-share-price-target-what-are-jefferies-3-other-foreign-brokerages-saying-as-ceo-hunt-intensifies/articleshow/134253758.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [RED 4.97] dyn_bac ↓
- dyn_bac [EQUITIES]: last 59.54, z20 -2.97, zc 0.06, resid-z -0.35 [quiet], 1d 0.12%, |z20|=2.97
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: The 10 most overvalued housing markets in America — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-10-most-overvalued-housing-markets-in-america-6d28efdf?mod=mw_rss_topstories
- Source: TRUMP: “DON’T KILL THE GOLDEN GOOSE” President Trump says America’s AI and data center boom is happening because the U.S. holds a commanding global lead. He urged against measures that could slow the industry’s expansion, warning policymakers: “Don’t kill the Golden Goose!” — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35759
- Source: BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7,400 from 7,100, signaling increased confidence in the equity rally. BofA also introduced a 12-month target of 7,800, pointing to further upside for U.S. stocks beyond year-end. — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35746
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
indices · 2 series ↓ (4.85), dyn_tatatech_ns ↓ (4.39), eur_usd ↓ (4.34), dyn_icicigi_bo ↓ (4.18), dyn_ohi ↑ (4.18), usd_mxn ↑ (3.86), nifty_metal ↓ (3.5), dyn_indusindbk_bo ↓ (3.42), dyn_indianb_ns ↓ (3.34), dyn_lenskart_ns ↑ (3.01), asx_200 ↓ (2.86), hang_seng ↓ (2.66)

## India macro
- nifty_50: 23118.5996 (1d -1.19%, z20 -3.00, flag red)
- nifty_midcap_100: 60876.1016 (1d -2.12%, z20 -4.20, flag red)
- usd_inr: 95.9450 (1d 0.96%, z20 1.38, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6332 (1d -0.94%, z20 -0.81, flag none)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 60.9 — "AAPL - INDIAN CONSUMER REGULATOR INVESTIGATES APPLE'S SOFTWARE WARRANTY TERMS, DOCUMENTS S"
- COALINDIA.NS (COAL INDIA LTD) score 60.4 — "AAPL - INDIAN CONSUMER REGULATOR INVESTIGATES APPLE'S SOFTWARE WARRANTY TERMS, DOCUMENTS S"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 59.3 — "AAPL - INDIAN CONSUMER REGULATOR INVESTIGATES APPLE'S SOFTWARE WARRANTY TERMS, DOCUMENTS S"
- INDIANB.NS (INDIAN BANK) score 58.8 — "AAPL - INDIAN CONSUMER REGULATOR INVESTIGATES APPLE'S SOFTWARE WARRANTY TERMS, DOCUMENTS S"
- COIN (Coinbase Global, Inc.) score 53.1 — "Global Market: Morgan Stanley turns hawkish, sees two Fed rate hikes in 2026"
- BAC (Bank of America Corporation) score 50.1 — "Global Market: Bank of Korea signals caution ahead after split rate vote"
- HDB (HDFC Bank Limited) score 43.3 — "Global Market: Bank of Korea signals caution ahead after split rate vote"
- IDBI.NS (IDBI BANK LIMITED) score 41.0 — "Global Market: Bank of Korea signals caution ahead after split rate vote"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.0 — "Global Market: Bank of Korea signals caution ahead after split rate vote"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.0 — "Global Market: Bank of Korea signals caution ahead after split rate vote"
- OHI (Omega Healthcare Investors, In) score 40.9 — "Bitcoin trades near $77,000 range as investors await US Fed’s September rate decision"
- CHKP (Check Point Software Technolog) score 37.1 — "ACME Solar shares jump 6% after HSBC raises target price - Check investment rationale"
- BOND (PIMCO Active Bond Exchange-Tra) score 37.0 — "U.S. 10-YEAR YIELD HITS HIGHEST SINCE 2007 The 10-year Treasury yield climbed above 5%, re"
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.4 — "NHAI extends debarment to PNC Infratech; stock hits 52-week low"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.4 — "NHAI extends debarment to PNC Infratech; stock hits 52-week low"
- TECH (Bio-Techne Corp) score 35.4 — "NHAI extends debarment to PNC Infratech; stock hits 52-week low"
- 301077.SZ (CHINASTARS) score 24.9 — "IRAN’S FOREIGN MINISTER TO VISIT CHINA Iranian Foreign Minister Abbas Araghchi will visit "
- SEPN (Septerna, Inc.) score 22.7 — "IRAN’S FOREIGN MINISTER TO VISIT CHINA Iranian Foreign Minister Abbas Araghchi will visit "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.9 — "Indonesia Eyes Guyana and Suriname Oil Investments for Energy Security"
- LTH (Life Time Group Holdings, Inc.) score 20.2 — "Infosys, HCLTech, TCS, other IT stocks soar up to 6%; Nifty IT rallies 5% as global AI slo"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.2 — "Afcons Infra stock surges on Tata Sons listing hopes. Is a re-rating on the cards?"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.2 — "Afcons Infra stock surges on Tata Sons listing hopes. Is a re-rating on the cards?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "An AI bubble is no longer Wall Street’s biggest fear. This stock-market risk just took its"
- NVDA (NVIDIA Corporation) score 9.0 — "NVIDIA, Palantir and Booz Allen Hamilton will limit use of ANTHROPIC models"
- JIOFIN.BO (Jio Financial Services Limited) score 7.7 — "EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services;"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.1 — "Can SS Retail IPO deliver long-term growth for high-risk investors?"
- MS (Morgan Stanley) score 6.9 — "Global Market: Morgan Stanley turns hawkish, sees two Fed rate hikes in 2026"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.9 — "All that glitters... in jewellers’ IPO boom"
- JEF (Jefferies Financial Group Inc.) score 6.3 — "HDFC Bank share price target: What are Jefferies, 3 other foreign brokerages saying as CEO"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.2 — "Tech picks: Adani Ports, Data Patterns among 5 stocks that could give up to 23% returns in"
- VT (Vanguard Total World Stock Ind) score 6.1 — "3 SME IPOs open today: Vama Wovenfab, Shakti Polytarp and Quanto Agroworld. Check GMP and "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.7 — "LIC Housing Finance among 5 F&O stocks with sharp rise in futures open interest"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 4.9 — "HDFC Bank share price jumps over 6% in 3 days | Experts see 15% more upside, check target "
- META (Meta) score 4.3 — "Gold and silver prices crash up to 2% on MCX- What is driving precious metals down?"
- BZ=F (Brent Crude Oil Last Day Finan) score 4.2 — "Dividend record date alert: Last chance to buy today for cash reward; Hindustan Copper, Ba"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.7 — "ICICI Securities says buy this NBFC stock, sees 59% upside after an 80% jump in 6 months -"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.3 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.7 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.1 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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