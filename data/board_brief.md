# Transmission Layer — board brief · 2026-10-26 16:48Z

data as of **2026-10-26** · 97 series · 19 red / 36 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.827, 16d in regime; vol-pct 0.78, breadth-off 0.875, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.37, contra nifty_50 corr20=0.42, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.16, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.2, corr60 0.08, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.78, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.19, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.04, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.55, corr60 0.25, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **8 of 89** scanned series survive multiplicity control (effective p ≤ 0.003389620038554586)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.464, β 0.242, p 0.0); driver zc -3.33 → expected -0.802%. Type hit-rate 0.822 (n=1928).
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.391, β 0.2243, p 0.0); driver zc -14.8 → expected -3.489%. Type hit-rate 0.822 (n=1928).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.375, β -0.2081, p 0.0); driver zc -14.8 → expected 3.236%. Type hit-rate 0.822 (n=1928).
- Track record · residual_reversion: hit-rate **0.504** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=1928) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.26] cross-asset · 5 series ↓
- ust_10y [RATES]: last 4.96, z20 -3.60, zc -3.33, resid-z -3.95 [unexplained], 1d -3.31%, |z20|=3.60
- ust_2y [RATES]: last 4.65, z20 -3.44, zc -2.66, resid-z -2.93 [unexplained], 1d -3.33%, |z20|=3.44
- tips_10y_real [RATES]: last 2.64, z20 -3.33, zc -2.43, resid-z -2.52 [unexplained], 1d -4.35%, 1d move -12.0bps ≥ 5bps; |z20|=3.33
- ust_30y [RATES]: last 5.29, z20 -2.82, zc -3.30, resid-z -3.38 [unexplained], 1d -2.40%, |z20|=2.82
- dyn_bond [EQUITIES]: last 88.65, z20 2.19, zc 0.46, resid-z 0.08 [quiet], 1d 0.18%, |z20|=2.19
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.547 vs dyn_bond
- Source: China's central bank sets up non-bank financial institution bond market swap facility — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/bonds/chinas-central-bank-sets-up-non-bank-financial-institution-bond-market-swap-facility/articleshow/135210676.cms
- Source: Asia-focused banks face bond market risks ahead of Q3 earnings — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/asia-focused-banks-face-bond-market-risks-ahead-of-q3-earnings/articleshow/135209404.cms
- Source: French bond selloff eases as country spared ratings downgrade — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/bonds/french-bond-selloff-eases-as-country-spared-ratings-downgrade/articleshow/135206922.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.03] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.22, z20 6.03, zc 2.55, resid-z 1.16 [moved], 1d 5.46%, |z20|=6.03
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Anthropic IPO: It’s official now! Artificial intelligence giant files papers to sell shares to public for first time — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/anthropic-ipo-it-s-official-now-artificial-intelligence-giant-files-papers-to-sell-shares-to-public-for-first-time-11793019537204.html
- Source: Kotak Mahindra Bank shares rise 2% as top Nifty gainer | Is it right time to book profits or wait? Target, stop loss — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/kotak-mahindra-bank-shares-rise-2-as-top-nifty-gainer-is-it-right-time-to-book-profits-or-wait-target-stop-loss-11792995247655.html
- Source: Silver prices at 2026 lowest;  ₹2,23,500 away from record high! Right time to buy for good returns? Target price per kg — Mint Markets, 2026-10-26. https://www.livemint.com/market/commodities/silver-prices-at-2026-lowest-rs-2-23-500-away-from-record-high-right-time-to-buy-for-good-returns-target-price-per-kg-11792992915881.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 7.97] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4033.10, z20 -2.58, zc 0.46, resid-z -2.09 [unexplained], 1d 0.63%, |z20|=2.58; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.19, z20 -2.02, zc 0.34, resid-z -0.01 [quiet], 1d 0.89%, |z20|=2.02; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 74.43, z20 1.65, zc n/a, resid-z n/a [quiet], 1d -0.26%, GSR<75 (extreme low); |z20|=1.65
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.508 vs comex_silver, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.516 vs comex_gold
- Source: Inflows into gold ETFs turned negative after 13 weeks as the yellow metal fell 4% last week — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/gold/inflows-into-gold-etfs-turned-negative-after-13-weeks-as-the-yellow-metal-fell-4-last-week/article71627333.ece
- Source: Gold gains as oil slide cools some inflation concerns — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/gold/gold-gains-as-oil-slide-cools-some-inflation-concerns/article71626429.ece
- Source: Why is gold price under pressure ahead of Dhanteras, Diwali? What should interested buyers do? Experts's views, target — Mint Markets, 2026-10-26. https://www.livemint.com/market/commodities/why-is-gold-price-under-pressure-ahead-of-dhanteras-diwali-what-should-interested-buyers-do-expertss-views-target-11793002314682.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 7.29] commodities · 2 series ↑
- wti [COMMODITIES]: last 102.93, z20 1.69, zc -0.11, resid-z 0.42 [quiet], 1d -0.33%, |z20|=1.69
- brent [COMMODITIES]: last 112.01, z20 1.46, zc -1.61, resid-z -1.10 [moved], 1d -4.04%, 1-session move -4.04% ≥ 1.5%; 1y-pct=96
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.367 via wti, z -2.12, reacted)
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.378 vs wti, historically leads by 4d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.573 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.367, z -2.12)
- Source: High crude prices, rise in lending rates take toll on small-cap stocks — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/commodities/high-crude-prices-rise-in-lending-rates-take-toll-on-small-cap-stocks/article71627090.ece
- Source: Why Saudi Just Abandoned Its Core Oil Rule — OilPrice, 2026-10-26. https://oilprice.com/Energy/Crude-Oil/Why-Saudi-Just-Abandoned-Its-Core-Oil-Rule.html
- Source: Is Wall Street Getting It All Wrong About AI, Oil, and Bonds? — OilPrice, 2026-10-26. https://oilprice.com/Energy/Energy-General/Is-Wall-Street-Getting-It-All-Wrong-About-AI-Oil-and-Bonds.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.75] cross-asset · 6 series ↓
- india_vix [INDICES]: last 17.13, z20 2.60, zc 0.27, resid-z n/a [quiet], 1d 1.62%, |z20|=2.60
- dyn_bajfinance_ns [EQUITIES]: last 918.70, z20 -2.44, zc -0.62, resid-z -0.89 [quiet], 1d -1.10%, |z20|=2.44
- dyn_swiggy_ns [EQUITIES]: last 185.75, z20 -2.16, zc 0.65, resid-z 1.05 [quiet], 1d 5.54%, |z20|=2.16; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 56466.80, z20 -2.12, zc 0.96, resid-z 1.25 [quiet], 1d 1.20%, |z20|=2.12
- dyn_jiofin_bo [EQUITIES]: last 205.40, z20 -2.00, zc 0.12, resid-z -0.25 [quiet], 1d 0.20%, |z20|=2.00; 1y-pct=0
- dyn_policybzr_ns [EQUITIES]: last 1023.00, z20 -0.44, zc 0.26, resid-z -0.35 [quiet], 1d 0.79%, 1y-pct=3
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.79).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.733 via india_vix, z 0.16, quiet); nifty_metal (rho 0.692 via nifty_midcap_100, z -1.24, reacted); nifty_fmcg (rho 0.603 via nifty_midcap_100, z -2.14, reacted); midcap_largecap_ratio (rho 0.597 via nifty_midcap_100, z -2.45, reacted); dyn_indusindbk_bo (rho -0.56 via india_vix, z -1.6, reacted)
- Watch next: nifty_50 (inverse) — not yet - watch; rho -0.733 vs india_vix, historically leads by 1d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.56 vs nifty_midcap_100, historically leads by 1d
- **India receivers**: nifty_50 (rho -0.733, z 0.16); nifty_metal (rho 0.692, z -1.24); nifty_fmcg (rho 0.603, z -2.14); midcap_largecap_ratio (rho 0.597, z -2.45)
- Source: Swiggy shares rise 6% after 4-session down episode; is this a relief rally or worst is over? Experts decode | Target, SL — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/swiggy-shares-rise-6-after-4-session-down-episode-is-this-a-relief-rally-or-worst-is-over-experts-decode-target-sl-11792998360954.html
- Source: Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bullish despite target price cuts — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/swiggy-shares-jump-5-a-day-after-q2-results-sparked-a-17-crash-why-brokerages-remain-bullish-despite-target-price-cuts/articleshow/135205591.cms
- Source: Mcap of eight of the top-10 firms erodes by ₹1.55 lakh cr; HDFC Bank, Bajaj Fin biggest laggards — BusinessLine Mkts, 2026-10-25. https://www.thehindubusinessline.com/markets/mcap-of-eight-of-the-top-10-firms-erodes-by-155-lakh-cr-hdfc-bank-bajaj-fin-biggest-laggards/article71622878.ece
- Historical analogues: 2025-07-21 (d=0.79), 2025-05-30 (d=0.88), 2025-07-10 (d=0.91)

### [RED 5.86] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 159.33, z20 -2.54, zc -0.67, resid-z -0.79 [quiet], 1d -3.11%, |z20|=2.54
- btc_usd [CRYPTO]: last 79788.15, z20 -2.27, zc -0.76, resid-z -1.00 [quiet], 1d -1.59%, |z20|=2.27
- eth_usd [CRYPTO]: last 2310.31, z20 -1.83, zc -0.81, resid-z -1.13 [quiet], 1d -3.09%, |z20|=1.83
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.53).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.378 via btc_usd, z -2.1, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.378, z -2.1)
- Source: India’s crude steel output rises 5.6% in Jan-Sept even as global production dips — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/commodities/indias-crude-steel-output-rises-56-in-jan-sept-even-as-global-production-dips/article71620869.ece
- Source: Bitcoin hovers near $80,000 and Ethereum tests $2,300 as macro and geopolitical risks weigh on crypto markets — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-hovers-near-80000-and-ethereum-tests-2300-as-macro-and-geopolitical-risks-weigh-on-crypto-markets/articleshow/135210501.cms
- Source: Global Market: European shares flat as investors assess earnings, France turmoil — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/global-market-european-shares-flat-as-investors-assess-earnings-france-turmoil/articleshow/135209743.cms
- Historical analogues: 2026-05-22 (d=0.53), 2025-10-16 (d=0.56), 2025-04-10 (d=0.65)

### [RED 5.79] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1575.00, z20 3.79, zc 4.51, resid-z 4.21 [unexplained], 1d 14.13%, |z20|=3.79
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.384 via dyn_atherenerg_ns, z -2.12, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.384, z -2.12)
- Source: Q2 Results Today Highlights: Tata Consumer Q2 profit declines, Aequs, Dalmia Bharat PAT declines q-o-q, Ather Energy & ITC Hotels jump after Q2 results, BoM, TMB, IOB, Mankind Pharma, APL Apollo Q2 PAT rise, Paytm, KFin Tech, Nazara to announce Q2 results — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/q2-results-today-highlights-paytm-tata-consumer-mankind-pharma-rec-itc-hotels-iob-ather-aegis-logistics-supreme-ind-aequs-nazara-sona-blw-tmb-bom-infosys-kotak-idfc-results-26-october-2026/article71625561.ece
- Source: Ather Energy shares skyrocket 19% after EV maker swings to Rs 1.26 crore profit in Q2 — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-skyrocket-19-after-ev-maker-swings-to-rs-1-26-crore-profit-in-q2/articleshow/135209355.cms
- Source: Q2 Results Today Live: Ather Energy logs profit in Q2, ITC Hotels surge after Q2 results, TMB, IOB, APL Apollo, Supreme Industries Q2 PAT rise, Paytm, Tata Consumer, Dalmia Bharat, KFin Tech, Mankind Pharma, BOM, Sona BLW, Nazara, Aequs to announce Q2 results — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-paytm-tata-consumer-mankind-pharma-rec-itc-hotels-iob-ather-aegis-logistics-supreme-ind-aequs-nazara-sona-blw-tmb-bom-infosys-kotak-idfc-results-26-october-2026/article71625561.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 5.03] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 159.84, z20 3.03, zc 0.22, resid-z 0.79 [quiet], 1d 0.51%, |z20|=3.03
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.351 via dyn_chkp, z -1.6, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.351, z -1.6)
- Source: How to check Jio Platforms IPO allotment status online on mobile by direct link of NSE and Kfin Tech websites — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/how-to-check-jio-platforms-ipo-allotment-status-online-on-mobile-by-direct-link-of-nse-and-kfin-tech-websites-11793024495583.html
- Source: Top 3 stocks to buy tomorrow: Laurus Labs, MCX, Coforge by market expert; check stop-loss, target price for Tue, 27 Oct — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/top-3-stocks-to-buy-tomorrow-laurus-labs-mcx-coforge-by-market-expert-check-stop-loss-target-price-for-tue-27-oct-11793014330701.html
- Source: Dividend stock down 4% today; declares  ₹12 per share dividend, record date fixed | Check yield, stock split history — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/dividend-stock-down-4-today-declares-rs-12-per-share-dividend-record-date-fixed-check-yield-stock-split-history-11793011222536.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

## Watchlist (below surfacing floor)
natgas ↓ (5.02), indices · 2 series ↓ (4.9), cross-asset · 2 series ↑ (4.83), dyn_meta ↓ (4.6), cross-asset · 2 series ↑ (4.53), dyn_tgt ↓ (4.41), dyn_sepn ↑ (4.21), dyn_tech ↑ (4.21), dyn_hdb ↓ (4.09), usd_cny ↓ (3.71), dyn_rs ↑ (3.63), sofr ↑ (3.31)

## India macro
- nifty_50: 22753.1992 (1d 0.68%, z20 0.16, flag none)
- nifty_midcap_100: 56466.8008 (1d 1.20%, z20 -2.12, flag amber)
- usd_inr: 95.1750 (1d 0.49%, z20 -0.66, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4817 (1d 0.51%, z20 -2.45, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.4 — "Up 174% in 1 year! Can Monolithisch India shares rise further? Experts decode"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 73.8 — "Up 174% in 1 year! Can Monolithisch India shares rise further? Experts decode"
- INOXINDIA.NS (INOX INDIA LIMITED) score 73.5 — "Up 174% in 1 year! Can Monolithisch India shares rise further? Experts decode"
- INDIANB.NS (INDIAN BANK) score 70.6 — "RED SEA SHIPPING RECOVERS, BUT COSTS REMAIN HIGH Bank of America reports Red Sea shipping "
- BAC (Bank of America Corporation) score 63.8 — "APOLLO: AI HAS DELIVERED “ZERO PAYOFF” OUTSIDE BIG TECH Apollo Chief Economist Torsten Slo"
- HDB (HDFC Bank Limited) score 58.2 — "RED SEA SHIPPING RECOVERS, BUT COSTS REMAIN HIGH Bank of America reports Red Sea shipping "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.4 — "RED SEA SHIPPING RECOVERS, BUT COSTS REMAIN HIGH Bank of America reports Red Sea shipping "
- IDBI.NS (IDBI BANK LIMITED) score 56.9 — "RED SEA SHIPPING RECOVERS, BUT COSTS REMAIN HIGH Bank of America reports Red Sea shipping "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.9 — "RED SEA SHIPPING RECOVERS, BUT COSTS REMAIN HIGH Bank of America reports Red Sea shipping "
- TGT (Target Corporation) score 45.6 — "Multibagger stock to buy: Up 150% in 2026 so far! Will rally sustain in defence-engineerin"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.3 — "APOLLO: AI HAS DELIVERED “ZERO PAYOFF” OUTSIDE BIG TECH Apollo Chief Economist Torsten Slo"
- COIN (Coinbase Global, Inc.) score 43.1 — "HSBC CUTS GLOBAL EQUITIES TO NEUTRAL FROM MAX OVERWEIGHT"
- OHI (Omega Healthcare Investors, In) score 40.6 — "Global Market: European shares flat as investors assess earnings, France turmoil"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.1 — "APOLLO: AI HAS DELIVERED “ZERO PAYOFF” OUTSIDE BIG TECH Apollo Chief Economist Torsten Slo"
- TECH (Bio-Techne Corp) score 36.1 — "APOLLO: AI HAS DELIVERED “ZERO PAYOFF” OUTSIDE BIG TECH Apollo Chief Economist Torsten Slo"
- CHKP (Check Point Software Technolog) score 30.7 — "Dividend stock down 4% today; declares  ₹12 per share dividend, record date fixed | Check "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 28.1 — "ING WARNS EURO COULD FALL FURTHER ON FRENCH DEBT CONCERNS ING says the euro remains vulner"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.6 — "FRANCE'S 10-YR BOND YIELD DOWN 5.3 BPS TO 4.9685% AFTER MOODY'S MAINTAINS SOVEREIGN RATING"
- LTH (Life Time Group Holdings, Inc.) score 23.7 — "Jio Platforms IPO listing on Oct 28: Time, expectations share price & key details"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 23.4 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 22.3 — "MAJOR OIL SPILL SPREADS OFF UAE COAST AMID IRAN WAR Satellite images show an expanding oil"
- 301077.SZ (CHINASTARS) score 21.3 — "China's central bank sets up non-bank financial institution bond market swap facility"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 20.7 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- RS (Reliance, Inc.) score 17.0 — "Reliance's Jio Platforms IPO allotment today, 26 Oct: Check status online, latest GMP pric"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.5 — "Market wrap: Dr Reddys, JSW Steel, Shriram Finance, Tata Consumer top gainers and losers o"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.5 — "Market wrap: Dr Reddys, JSW Steel, Shriram Finance, Tata Consumer top gainers and losers o"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.0 — "OCTOBER HOLD PRICED IN. WALL STREET EYES DECEMBER HIKE. Goldman Sachs expects the Fed to h"
- META (Meta) score 13.4 — "Meta plans to raise up to $95 billion to fund AI and data centre expansion"
- SEPN (Septerna, Inc.) score 13.0 — "RED SEA SHIPPING RECOVERS, BUT COSTS REMAIN HIGH Bank of America reports Red Sea shipping "
- JIOFIN.BO (Jio Financial Services Limited) score 12.9 — "China's central bank sets up non-bank financial institution bond market swap facility"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.9 — "MUSK SAYS UKRAINE VIOLATED STARLINK TERMS Elon Musk claims Ukraine used Starlink for offen"
- JEF (Jefferies Financial Group Inc.) score 11.4 — "IndusInd Bank shares rise 2% after Q2 results. Why Jefferies cut target price despite lend"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.7 — "Top stocks to buy: Adani Energy, AU Small Finance Bank, BPCL, IDFC First Bank — Jefferies "
- VT (Vanguard Total World Stock Ind) score 7.9 — "World shares mostly advance after decline on Wall Street, oil prices fall more than 1%"
- GS (Goldman Sachs Group, Inc. (The) score 7.5 — "OCTOBER HOLD PRICED IN. WALL STREET EYES DECEMBER HIKE. Goldman Sachs expects the Fed to h"
- INFY (Infosys Limited) score 5.2 — "Infosys shares fall 4% after IT major lowers FY27 guidance. What are Goldman Sachs, Nomura"
- SWIGGY.NS (SWIGGY LIMITED) score 5.0 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- WIT (Wipro Limited) score 3.9 — "Top IT stocks to buy after Q2 results: TCS vs Infosys vs Wipro vs HCL vs Tech Mahindra - W"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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