# Transmission Layer — board brief · 2026-08-27 00:56Z

data as of **2026-08-27** · 98 series · 13 red / 31 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 1d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.31, corr60 -0.4, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.86, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.35, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.02, last shift 2026-07-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.29, corr60 -0.15, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.02, corr60 -0.08, last shift 2026-07-01. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.32, corr60 0.2, last shift 2026-07-09. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **7 of 90** scanned series survive multiplicity control (effective p ≤ 0.0046548004134630006)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.499** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2249) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 13.88] usd_inr ↓
- usd_inr [FX]: last 93.55, z20 -8.88, zc -6.86, resid-z -5.49 [unexplained], 1d -2.27%, 20d range extreme; |z20|=8.88
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Rupee slide, valuation rules put foreign asset disclosure scheme out of reach for many — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-slide-valuation-rules-put-foreign-asset-disclosure-scheme-out-of-reach-for-many/articleshow/133553250.cms
- Source: Rupee rises 24 paise to close at 95.46 against US dollar — BusinessLine Mkts, 2026-08-25. https://www.thehindubusinessline.com/markets/forex/rupee-rises-24-paise-to-close-at-9546-against-us-dollar/article71388440.ece
- Source: Oil fall lifts rupee to over one-week high after central bank keeps lid on losses — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/forex/oil-fall-lifts-rupee-to-over-one-week-high-after-central-bank-keeps-lid-on-losses/articleshow/133505392.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 6.7] commodities · 3 series ↑
- wheat [COMMODITIES]: last 764.25, z20 3.38, zc -0.06, resid-z 6.21 [unexplained], 1d -0.16%, |z20|=3.38; 1y-pct=99
- corn [COMMODITIES]: last 537.00, z20 2.94, zc -0.03, resid-z 4.56 [unexplained], 1d -0.05%, |z20|=2.94; 1y-pct=99
- soybeans [COMMODITIES]: last 1263.25, z20 2.38, zc -0.04, resid-z 2.83 [unexplained], 1d -0.04%, |z20|=2.38; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho -0.518 via wheat, z -8.88, reacted); dyn_idbi_ns (rho 0.36 via wheat, z 6.15, reacted)
- **India receivers**: usd_inr (rho -0.518, z -8.88); dyn_idbi_ns (rho 0.36, z 6.15)
- Source: Wheat soars to daily limit on Black Sea export worries, corn at lifetime highs — Mint Markets, 2026-08-26. https://www.livemint.com/market/wheat-soars-to-daily-limit-on-black-sea-export-worries-corn-at-lifetime-highs-11787773711563.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 6.25] tips_10y_real ↓
- tips_10y_real [RATES]: last 2.32, z20 -3.25, zc -1.58, resid-z -1.86 [unexplained], 1d -2.52%, 1d move -6.0bps ≥ 5bps; |z20|=3.25
- **Mechanism**: tips_10y_real ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-10 (d=0.0), 2025-05-22 (d=0.07)

### [RED 6.15] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 95.25, z20 6.15, zc 2.47, resid-z 3.78 [unexplained], 1d 7.86%, |z20|=6.15
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.413 via dyn_idbi_ns, z 2.43, reacted); nifty_metal (rho 0.383 via dyn_idbi_ns, z 2.5, reacted); dyn_muthootfin_ns (rho 0.376 via dyn_idbi_ns, z 2.36, reacted)
- **India receivers**: dyn_cartrade_ns (rho 0.413, z 2.43); nifty_metal (rho 0.383, z 2.5); dyn_muthootfin_ns (rho 0.376, z 2.36)
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

### [RED 5.52] dyn_dks ↓
- dyn_dks [EQUITIES]: last 129.71, z20 -3.52, zc 0.35, resid-z -12.14 [unexplained], 1d 4.34%, |z20|=3.52; 1y-pct=0
- **Mechanism**: dyn_dks ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PRICE TARGET CUT • $APP: PT cut to $475 from $500 by Needham • $CHWY: PT cut to $37 from $42 by Morgan Stanley • $CPRT: PT cut to $25 from $26 by Barclays • $DKS: PT cut to $150 from $280 by Barclays; PT cut to $180 from $300 by BTIG; PT cut to $205 from $260 by D.A. — DeItaone, 2026-08-26. https://t.me/walter_bloomberg/35087
- Source: Dick’s Sporting Goods slumps after earnings miss: What’s next? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/dicks-sporting-goods-slumps-after-earnings-miss-whats-next/slideshow/133532630.cms
- Source: Dick’s Sporting Goods’ epic drop hits other footwear giants, as shoppers sour on retro sneakers — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/dicks-sporting-goods-stock-is-having-its-worst-day-ever-as-sneakers-arent-selling-without-deeper-discounts-5a868358?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-01 (d=0.0), 2025-08-15 (d=0.12)

### [RED 5.23] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3125.00, z20 3.23, zc 0.23, resid-z 1.37 [quiet], 1d 0.60%, |z20|=3.23
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.48 via dyn_adanient_bo, z -1.06, reacted); nifty_midcap_100 (rho 0.442 via dyn_adanient_bo, z 1.3, reacted); dyn_indusindbk_bo (rho 0.421 via dyn_adanient_bo, z -1.74, reacted); nifty_fmcg (rho 0.373 via dyn_adanient_bo, z -1.76, reacted)
- **India receivers**: nifty_50 (rho 0.48, z -1.06); nifty_midcap_100 (rho 0.442, z 1.3); dyn_indusindbk_bo (rho 0.421, z -1.74); nifty_fmcg (rho 0.373, z -1.76)
- Source: Adani’s Cemindia is said to near up to $524 million share sale — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adanis-cemindia-is-said-to-near-up-to-524-million-share-sale/articleshow/133536591.cms
- Source: Adani Ports or Gujarat Pipavav: Which stock benefits more from Gujarat concession extensions? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adani-ports-or-gujarat-pipavav-which-stock-benefits-more-from-gujarat-concession-extensions/articleshow/133532117.cms
- Source: Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharashtra | shares rise — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/gautam-adanis-adani-energy-solutions-wins-rs-4-700-crore-transmission-project-in-maharashtra-shares-rise-11787717367517.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.94] cross-asset · 2 series ↓
- dyn_techm_ns [EQUITIES]: last 1571.00, z20 -2.11, zc -1.20, resid-z -1.08 [quiet], 1d -1.81%, |z20|=2.11
- nifty_it [INDICES]: last 30318.85, z20 -1.69, zc -1.02, resid-z -0.51 [quiet], 1d -1.47%, |z20|=1.69
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.607 via nifty_it, z -1.38, reacted); dyn_tatatech_ns (rho 0.519 via nifty_it, z -0.43, quiet); nifty_50 (rho 0.483 via nifty_it, z -1.06, reacted); midcap_largecap_ratio (rho -0.355 via dyn_techm_ns, z 1.73, reacted)
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.519 vs nifty_it, historically leads by 3d
- **India receivers**: dyn_tataelxsi_ns (rho 0.607, z -1.38); dyn_tatatech_ns (rho 0.519, z -0.43); nifty_50 (rho 0.483, z -1.06); midcap_largecap_ratio (rho -0.355, z 1.73)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Daily Performance — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-live-updates-26-aug-2026/liveblog/133527928.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [AMBER 4.86] cross-asset · 3 series ↑
- comex_copper [COMMODITIES]: last 6.71, z20 1.54, zc 0.00, resid-z 0.08 [quiet], 1d 0.00%, |z20|=1.54; 1y-pct=99; co-occur[metal_copper] suppressed: channel WEAK
- dax [INDICES]: last 26314.46, z20 0.75, zc 0.24, resid-z 0.19 [quiet], 1d 0.18%, 1y-pct=97
- stoxx_50 [INDICES]: last 6474.15, z20 0.12, zc 0.38, resid-z 0.09 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-25 (z-distance 0.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.493 via dax, z 1.3, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.67 vs comex_copper, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.612 vs dax, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.607 vs stoxx_50, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.594 vs stoxx_50, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.567 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.493, z 1.3)
- Source: Stocks in news: Tata Power, Jio Financial Services, Bharat Electronics and Hindustan Copper — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/stocks-in-news-tata-power-jio-financial-services-bharat-electronics-and-hindustan-copper/articleshow/133550824.cms
- Source: Top Gainers & Losers on 26 Aug: SBFC Finance, Capri Global, Hindustan Copper, SAIL, OLA, Vedanta among top gainers — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-26-aug-sbfc-finance-capri-global-hindustan-copper-sail-ola-vedanta-among-top-gainers-11787739634109.html
- Source: Hindustan Copper shares up 5.6%, OFS opened for retail investors today — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/hindustan-copper-shares-up-56-ofs-opened-for-retail-investors-today/article71392239.ece
- Historical analogues: 2025-07-25 (d=0.44), 2025-10-14 (d=0.48), 2024-10-03 (d=0.55)

## Watchlist (below surfacing floor)
natgas ↑ (4.74), midcap_largecap_ratio ↑ (4.73), crypto · 2 series ↑ (4.68), dyn_icicigi_bo ↓ (4.48), dyn_muthootfin_ns ↑ (4.36), dyn_mrna ↑ (4.08), dyn_karurvysya_ns ↑ (3.73), indices · 2 series ↑ (3.64), comex_gold ↑ (3.54), dyn_lenskart_ns ↑ (3.28), cross-asset · 2 series ↑ (3.27), dyn_tech ↑ (3.17)

## India macro
- nifty_50: 24207.7500 (1d -0.52%, z20 -1.06, flag none)
- nifty_midcap_100: 64099.0508 (1d -0.10%, z20 1.30, flag amber)
- usd_inr: 93.5461 (1d -2.27%, z20 -8.88, flag red)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6479 (1d 0.42%, z20 1.73, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.1 — "Stock recommendations for 27 August from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 79.1 — "Stock recommendations for 27 August from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 77.8 — "Banks Moving Forward With Global Stablecoin Consortium, Sources Say"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 76.9 — "Stock recommendations for 27 August from MarketSmith India"
- BAC (Bank of America Corporation) score 71.7 — "Banks Moving Forward With Global Stablecoin Consortium, Sources Say"
- HDB (HDFC Bank Limited) score 65.6 — "Banks Moving Forward With Global Stablecoin Consortium, Sources Say"
- IDBI.NS (IDBI BANK LIMITED) score 60.8 — "Banks Moving Forward With Global Stablecoin Consortium, Sources Say"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.8 — "Banks Moving Forward With Global Stablecoin Consortium, Sources Say"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.8 — "Banks Moving Forward With Global Stablecoin Consortium, Sources Say"
- BOND (PIMCO Active Bond Exchange-Tra) score 53.7 — "There’s so much betting against long-term bonds that a turnaround could catch investors of"
- COIN (Coinbase Global, Inc.) score 53.4 — "Global Oil Security Looks Shakier as Conflicts Hit 45 Million Bpd of Supply"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.2 — "WHITE HOUSE TO ANNOUNCE NEW DRUG PRICING DEALS WITH BIOTECHS"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.4 — "WHITE HOUSE TO ANNOUNCE NEW DRUG PRICING DEALS WITH BIOTECHS"
- TECH (Bio-Techne Corp) score 48.3 — "WHITE HOUSE TO ANNOUNCE NEW DRUG PRICING DEALS WITH BIOTECHS"
- OHI (Omega Healthcare Investors, In) score 46.7 — "Retail investors turn selective as IPO appetite loses steam in 2026"
- LTH (Life Time Group Holdings, Inc.) score 35.0 — "IRAN IS STILL IN WARTIME SITUATION, ITS NUCLEAR SITES HAVE NOT BEEN SECURED FOR INSPECTION"
- NVDA (NVIDIA Corporation) score 29.8 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks end near flat a"
- 301077.SZ (CHINASTARS) score 29.8 — "Aramco Finds a New Way to Keep Saudi Crude Flowing to China"
- CHKP (Check Point Software Technolog) score 28.6 — "Today’s Gold Rate, Aug 26: Check gold rates in Delhi, Mumbai, Chennai"
- JIOFIN.BO (Jio Financial Services Limited) score 20.6 — "Stocks in news: Tata Power, Jio Financial Services, Bharat Electronics and Hindustan Coppe"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 18.4 — "Retail investors turn selective as IPO appetite loses steam in 2026"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.5 — "Gift City’s global trading push gathers pace, but foreign firms hold back"
- MS (Morgan Stanley) score 16.9 — "JPMORGAN CHASE RECENTLY EVALUATED PURSUING ITS OWN STABLECOIN: WSJ"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.6 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.4 — "Stocks in news: Tata Power, Jio Financial Services, Bharat Electronics and Hindustan Coppe"
- META (Meta) score 14.0 — "Meta dodges ‘Big Tobacco’ nightmare with $18 billion settlement in child-safety lawsuit"
- PCJEWELLER.NS (PC JEWELLER LTD) score 13.5 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.2 — "Tata Power loses challenge to $490 million arbitration award"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.0 — "Tata Power loses challenge to $490 million arbitration award"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.2 — "Adani’s Cemindia is said to near up to $524 million share sale"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.3 — "Stocks in news: Tata Power, Jio Financial Services, Bharat Electronics and Hindustan Coppe"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.6 — "ICICI Prudential AMC shares: Prudential Corporation to divest up to 2% equity, stock up 49"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.4 — "I just had my first baby and don’t want to go back to work. Is quitting for a year a bad i"
- VT (Vanguard Total World Stock Ind) score 6.6 — "Healthcare stock Park Medi World jumps 3%, rises for 5th consecutive session after this ca"
- DKS (Dick's Sporting Goods Inc) score 4.6 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.7 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 3.5 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.6 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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