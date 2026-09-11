# Transmission Layer — board brief · 2026-09-11 14:25Z

data as of **2026-09-11** · 98 series · 7 red / 41 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.579, 1d in regime; vol-pct 0.452, breadth-off 0.706, Markov P(high-vol) 0.03)
- [INVERTED] **safe_haven_gold** — corr20 -0.5, corr60 -0.35, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.89, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.01, corr60 0.27, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.13, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.87, corr60 -0.85, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.17, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.18, corr60 0.11, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_dell → taiwan_weighted: leads 1d (ccf 0.368, β 0.1478, p 1e-05); driver zc 2.24 → expected 1.738%. Type hit-rate 0.82 (n=2041).
- **SETUP** eth_usd → usd_brl: leads 1d (ccf -0.266, β -0.0514, p 0.0); driver zc 1.88 → expected -0.374%. Type hit-rate 0.82 (n=2041).
- Track record · residual_reversion: hit-rate **0.497** (n=1135) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2041) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.2] commodities · 2 series ↑
- brent [COMMODITIES]: last 104.96, z20 2.37, zc -0.73, resid-z -0.41 [quiet], 1d -2.48%, 1-session move -2.48% ≥ 1.5%; |z20|=2.37
- wti [COMMODITIES]: last 99.60, z20 2.21, zc -0.86, resid-z -0.49 [quiet], 1d -2.81%, 1-session move -2.81% ≥ 1.5%; |z20|=2.21
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.508 vs wti, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.627 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.562 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.512 vs brent
- Source: Crude oil price dips to $104, world shares mixed following Wall Street losses — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/commodities/crude-oil-price-dips-to-104-world-shares-mixed-following-wall-street-losses/article71456727.ece
- Source: Pulse of the Street: oil surge and rate hike fears trigger a market sell-off — Mint Markets, 2026-09-11. https://www.livemint.com/market/pulse-of-the-street-oil-surge-and-rate-hike-fears-trigger-a-market-selloff-11789130520769.html
- Source: Debunking the Viral Claim That America Has Only 14 Days of Oil Left — OilPrice, 2026-09-11. https://oilprice.com/Energy/Crude-Oil/Debunking-the-Viral-Claim-That-America-Has-Only-14-Days-of-Oil-Left.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.54] cross-asset · 4 series ↓
- india_vix [INDICES]: last 12.24, z20 2.88, zc 0.67, resid-z n/a [quiet], 1d 3.75%, |z20|=2.88
- nifty_midcap_100 [INDICES]: last 62199.10, z20 -2.39, zc -0.39, resid-z -0.39 [quiet], 1d -0.26%, |z20|=2.39
- nifty_50 [INDICES]: last 23398.10, z20 -2.37, zc -0.61, resid-z -0.69 [quiet], 1d -0.34%, |z20|=2.37
- dyn_jiofin_bo [EQUITIES]: last 230.00, z20 -1.89, zc -0.35, resid-z 0.38 [quiet], 1d -0.50%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.624 via nifty_50, z -1.77, reacted); dyn_indianb_ns (rho 0.551 via nifty_midcap_100, z -2.13, reacted); nifty_it (rho 0.51 via nifty_50, z -2.31, reacted); dyn_techm_ns (rho 0.47 via nifty_50, z -1.48, reacted); dyn_indusindbk_bo (rho 0.461 via nifty_50, z -1.86, reacted)
- **India receivers**: nifty_fmcg (rho 0.624, z -1.77); dyn_indianb_ns (rho 0.551, z -2.13); nifty_it (rho 0.51, z -2.31); dyn_techm_ns (rho 0.47, z -1.48)
- Source: Sensex, Nifty fall even as easing oil prices, buying in HDFC Bank, IT stocks help pare losses — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/sensex-nifty-fall-even-as-easing-oil-prices-buying-in-hdfc-bank-it-stocks-help-pare-losses/article71456335.ece
- Source: Market wrap: HDFC Bank, Dr Reddys, Hindalco, JSW Steel top gainers and losers on Nifty and Sensex on Friday — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-hdfc-bank-dr-reddys-hindalco-jsw-steel-top-gainers-and-losers-on-nifty-and-sensex-on-friday/articleshow/134062966.cms
- Source: Sensex today | Stock Market Highlights: Sensex down 120 pts, Nifty closes at 23,398, logs 5th weekly loss as oil fears grip markets — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-11th-september-2026/article71453005.ece
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [AMBER 6.34] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 89.11, z20 -2.41, zc 0.50, resid-z -1.11 [quiet], 1d 0.18%, |z20|=2.41; 1y-pct=0
- ust_10y [RATES]: last 4.83, z20 2.24, zc 0.66, resid-z 0.45 [quiet], 1d 0.63%, |z20|=2.24; 1y-pct=100
- ust_2y [RATES]: last 4.43, z20 2.06, zc 0.72, resid-z 0.72 [quiet], 1d 0.91%, |z20|=2.06; 1y-pct=100
- tips_10y_real [RATES]: last 2.46, z20 1.52, zc 0.76, resid-z 0.72 [quiet], 1d 1.23%, |z20|=1.52; 1y-pct=99
- ust_30y [RATES]: last 5.28, z20 1.23, zc 0.75, resid-z 0.53 [quiet], 1d 0.57%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.534 vs dyn_bond
- Watch next: dxy (inverse) — not yet - watch; rho -0.53 vs dyn_bond
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.324 vs ust_2y, historically leads by 1d
- Source: I’m locked into a 10-year annuity and now I’m strapped for cash. What are my options? — MarketWatch Top, 2026-09-11. https://www.marketwatch.com/story/im-locked-into-a-10-year-annuity-and-now-im-strapped-for-cash-what-are-my-options-e6463c91?mod=mw_rss_topstories
- Source: MSE facilitates India’s first tokenised corporate bond under SEBI’s Demat 2.0 pilot — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/mse-facilitates-indias-first-tokenised-corporate-bond-under-sebis-demat-20-pilot/article71456088.ece
- Source: India 10-year yield tops 7% as oil rout extends losses into fourth week — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/bonds/india-10-year-yield-tops-7-as-oil-rout-extends-losses-into-fourth-week/articleshow/134066329.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 4.52] indices · 2 series ↓
- nikkei_225 [INDICES]: last 64006.42, z20 -1.69, zc -1.45, resid-z -1.20 [quiet], 1d -1.94%, |z20|=1.69
- shanghai_comp [INDICES]: last 3886.80, z20 -1.58, zc -1.72, resid-z -1.27 [moved], 1d -1.21%, |z20|=1.58
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-16 (z-distance 0.84).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho -0.537 via shanghai_comp, z -1.48, reacted); nifty_it (rho -0.466 via shanghai_comp, z -2.31, reacted); midcap_largecap_ratio (rho 0.385 via shanghai_comp, z 1.12, reacted)
- Watch next: kospi (co-move) — not yet - watch; rho 0.835 vs nikkei_225
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.776 vs nikkei_225
- Watch next: usd_mxn (inverse) — not yet - watch; rho -0.515 vs nikkei_225, historically leads by 3d
- **India receivers**: dyn_techm_ns (rho -0.537, z -1.48); nifty_it (rho -0.466, z -2.31); midcap_largecap_ratio (rho 0.385, z 1.12)
- Source: Global Market: Japan's Nikkei falls 3% as oil surge, US rate hike fears weigh — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-3-as-oil-surge-us-rate-hike-fears-weigh/articleshow/134045193.cms
- Source: How Asian markets, crude will impact Sensex, Nifty 50: What GIFT Nifty, Nikkei, Kospi, Taiwan index signals for India — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/how-asian-markets-crude-will-impact-sensex-nifty-50-what-gift-nifty-nikkei-kospi-taiwan-index-signals-for-india-11789089499149.html
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Friday | Kospi, Taiwan Index, Nikkei cues to watch | 11 Sept — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-friday-kospi-taiwan-index-nikkei-cues-to-watch-11-sept-11789033761629.html
- Historical analogues: 2025-07-16 (d=0.84), 2025-12-23 (d=1.2), 2026-06-12 (d=1.31)

### [AMBER 4.29] dyn_meta ↑
- dyn_meta [EQUITIES]: last 653.58, z20 2.29, zc 0.55, resid-z 2.62 [unexplained], 1d 1.43%, |z20|=2.29
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.365 via dyn_meta, z -2.39, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.365, z -2.39)
- Source: META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight and raised its price target to $820 from $640, implying roughly 24% upside. The bank sees significant new revenue opportunities from AI agents, subscriptions and enterprise AI services beyond advertising. — DeItaone, 2026-09-10. https://t.me/walter_bloomberg/35569
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [AMBER 4.15] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 765.60, z20 -2.15, zc -0.81, resid-z -0.59 [quiet], 1d -1.73%, |z20|=2.15
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.575 via dyn_tatatech_ns, z -2.31, reacted); dyn_tataelxsi_ns (rho 0.506 via dyn_tatatech_ns, z -2.28, reacted); dyn_techm_ns (rho 0.475 via dyn_tatatech_ns, z -1.48, reacted)
- **India receivers**: nifty_it (rho 0.575, z -2.31); dyn_tataelxsi_ns (rho 0.506, z -2.28); dyn_techm_ns (rho 0.475, z -1.48)
- Source: Tata Steel share price falls 3%, among top Nifty 50 laggards; what experts say — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/tata-steel-share-price-falls-3-among-top-nifty-50-laggards-what-experts-say-11789119888853.html
- Source: Tata Motors PV Share Price Live Updates: Tata Motors PV experiences a modest increase — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-motors-pv-share-price-live-11-sep-2026/liveblog/134044063.cms
- Source: Enviro Infra Engineers shares rise 5% on Rs 224 crore wind EPC order from Tata Power RE — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/stocks/news/enviro-infra-engineers-shares-rise-5-on-rs-224-crore-wind-epc-order-from-tata-power-re/articleshow/133994920.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.13] dyn_indianb_ns ↓
- dyn_indianb_ns [EQUITIES]: last 853.50, z20 -2.13, zc -0.18, resid-z -0.20 [quiet], 1d -0.35%, |z20|=2.13
- **Mechanism**: dyn_indianb_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.551 via dyn_indianb_ns, z -2.39, reacted); dyn_jiofin_bo (rho 0.474 via dyn_indianb_ns, z -1.89, reacted); nifty_50 (rho 0.39 via dyn_indianb_ns, z -2.37, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.551, z -2.39); dyn_jiofin_bo (rho 0.474, z -1.89); nifty_50 (rho 0.39, z -2.37)
- Source: Stocks to Watch Today: Indian Bank, Hindustan Zinc, Wipro, Shakti Pumps and more — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/stocks-in-focus-today-indian-bank-hindustan-zinc-wipro-shakti-pumps-and-more/article71450006.ece
- Source: NSE IPO: Indian Bank to divest 17.91% of its stake via OFS — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/nse-ipo-indian-bank-to-divest-1791-of-its-stake-via-ofs/article71448395.ece
- Source: NSE IPO: Indian Bank to divest up to 17.91% of its holding in National Stock Exchange via Offer for Sale — Mint Markets, 2026-09-09. https://www.livemint.com/market/stock-market-news/nse-ipo-indian-bank-to-divest-up-to-17-91-of-its-holding-in-national-stock-exchange-via-offer-for-sale-11788967087644.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-06 (d=0.0), 2024-11-05 (d=0.01)

### [AMBER 4.12] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.12, zc n/a, resid-z n/a [quiet], 1d 0.08%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.436 via midcap_largecap_ratio, z -2.37, reacted); nifty_midcap_100 (rho 0.431 via midcap_largecap_ratio, z -2.39, reacted); nifty_fmcg (rho -0.398 via midcap_largecap_ratio, z -1.77, reacted)
- **India receivers**: nifty_50 (rho -0.436, z -2.37); nifty_midcap_100 (rho 0.431, z -2.39); nifty_fmcg (rho -0.398, z -1.77)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
usd_jpy ↓ (4.11), dyn_icicigi_bo ↓ (3.99), dyn_pcjeweller_ns ↑ (3.78), asx_200 ↓ (3.73), gold_silver_ratio ↑ (3.68), indices · 4 series ↓ (3.64), dyn_hdb ↓ (3.53), cross-asset · 2 series ↓ (3.14), dyn_atherenerg_ns ↑ (3.08), dyn_qcom ↑ (2.9), hang_seng ↓ (2.89), dyn_dell ↑ (2.67)

## India macro
- nifty_50: 23398.0996 (1d -0.34%, z20 -2.37, flag amber)
- nifty_midcap_100: 62199.1016 (1d -0.26%, z20 -2.39, flag amber)
- usd_inr: 95.5400 (1d 0.45%, z20 0.69, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6583 (1d 0.08%, z20 1.12, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 92.7 — "Xi in India, bank capital injections, EU-China trade"
- COALINDIA.NS (COAL INDIA LTD) score 89.6 — "Xi in India, bank capital injections, EU-China trade"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.8 — "Xi in India, bank capital injections, EU-China trade"
- INDIANB.NS (INDIAN BANK) score 68.5 — "FRANCE DEBT CANCELLATION PLAN SLAMMED AS “DANGEROUS” Bank of France chief Emmanuel Moulin "
- BAC (Bank of America Corporation) score 65.2 — "TRUMP SUGGESTS ELECTION MAY LIMIT IRAN ESCALATION President Donald Trump said the upcoming"
- COIN (Coinbase Global, Inc.) score 63.4 — "APPLE’S $1,999 FOLDABLE FACES DEMAND TEST Apple’s new iPhone Duo starts at $1,999, but ana"
- HDB (HDFC Bank Limited) score 55.5 — "FRANCE DEBT CANCELLATION PLAN SLAMMED AS “DANGEROUS” Bank of France chief Emmanuel Moulin "
- OHI (Omega Healthcare Investors, In) score 52.3 — "Awfis Space Solutions share price jumps nearly 20% despite weak Sensex, Nifty 50; what sho"
- IDBI.NS (IDBI BANK LIMITED) score 51.5 — "FRANCE DEBT CANCELLATION PLAN SLAMMED AS “DANGEROUS” Bank of France chief Emmanuel Moulin "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.5 — "FRANCE DEBT CANCELLATION PLAN SLAMMED AS “DANGEROUS” Bank of France chief Emmanuel Moulin "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 51.5 — "FRANCE DEBT CANCELLATION PLAN SLAMMED AS “DANGEROUS” Bank of France chief Emmanuel Moulin "
- CHKP (Check Point Software Technolog) score 44.8 — "IGL stock outlook by Motilal Oswal: Buy for 27% upside; check target price - 'Margins bott"
- BOND (PIMCO Active Bond Exchange-Tra) score 43.7 — "Global Market: Eurozone bonds slide as energy prices stoke inflation fears"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.2 — "TRUMP DISMISSES AI EXTINCTION FEARS President Donald Trump says he has “no” concerns that "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.1 — "TRUMP DISMISSES AI EXTINCTION FEARS President Donald Trump says he has “no” concerns that "
- TECH (Bio-Techne Corp) score 38.1 — "TRUMP DISMISSES AI EXTINCTION FEARS President Donald Trump says he has “no” concerns that "
- LTH (Life Time Group Holdings, Inc.) score 33.9 — "U.S. DIESEL BREAKS $6 FOR FIRST TIME EVER The U.S. average diesel price surpassed $6 a gal"
- 301077.SZ (CHINASTARS) score 31.3 — "TRUMP DISMISSES AI EXTINCTION FEARS President Donald Trump says he has “no” concerns that "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.7 — "GULF STATES WEIGH TALKS WITH IRAN OVER HORMUZ Gulf states are considering rare talks with "
- SEPN (Septerna, Inc.) score 14.9 — "China's Crude Imports Set to Hold at 7.2 Million Bpd in September"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.6 — "Molbio Diagnostics shares surge over 50% in just 3 days! What is driving the rally?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.3 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- JIOFIN.BO (Jio Financial Services Limited) score 12.6 — "WHAT TO WATCH TODAY — U.S. MARKETS 8:00 AM ET — 🛒 Kroger Earnings 8:30 AM ET — 🇺🇸 August C"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.2 — "US AVERAGE RETAIL DIESEL PRICE RISES PAST $6 A GALLON: AAA"
- MS (Morgan Stanley) score 10.9 — "MUNI YIELDS SURGE TO HIGHEST SINCE APRIL 2025 U.S. 10-year municipal bond yields jumped to"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.7 — "Dividend stocks alert! Last chance to qualify- Kalyan Jewellers, Aarti Industries, Blue Je"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.1 — "Tata Steel share price falls 3%, among top Nifty 50 laggards; what experts say"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.1 — "Tata Steel share price falls 3%, among top Nifty 50 laggards; what experts say"
- META (Meta) score 8.9 — "Vedanta Aluminium Metal shares dip over 3% | Here's why Anil Agarwal-owned stock is nosedi"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 7.6 — "Cochin Shipyard shares crash nearly 9% - Is it opportunity to buy? Should you take fresh e"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.1 — "Joint finances, joint risks: A couple’s roadmap to starting up"
- VT (Vanguard Total World Stock Ind) score 7.0 — "Smartworld Developers raises Rs 800 cr from Kotak Realty Fund for two projects in Gurugram"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.0 — "ICICI Bank Share Price Live Updates: Rs 1.09 crore remittance sent home by an Indian worki"
- JEF (Jefferies Financial Group Inc.) score 6.8 — "Jefferies cuts KEI Industries target price by 11%. Will UltraTech’s entry put the company "
- NVDA (NVIDIA Corporation) score 6.6 — "NVDA - NVIDIA’S HUANG SEES CYBERSECURITY AS AI’S NEXT BIG MARKET Nvidia CEO Jensen Huang s"
- QCOM (QUALCOMM Incorporated) score 2.1 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.9 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 0.8 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
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