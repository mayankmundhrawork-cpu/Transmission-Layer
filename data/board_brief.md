# Transmission Layer — board brief · 2026-09-24 15:03Z

data as of **2026-09-24** · 97 series · 8 red / 40 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.586, 5d in regime; vol-pct 0.485, breadth-off 0.688, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.36, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.06, corr60 0.23, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.1, corr60 0.12, last shift 2026-08-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.79, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.08, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.04, last shift 2026-08-04. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.17, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **10 of 89** scanned series survive multiplicity control (effective p ≤ 0.0110852468861653)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1096) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2307) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 19.17] cross-asset · 4 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1207.20, z20 -15.51, zc -12.58, resid-z -17.81 [unexplained], 1d -36.00%, |z20|=15.51; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 60992.25, z20 -1.74, zc -3.09, resid-z -2.18 [unexplained], 1d -2.24%, |z20|=1.74
- nifty_50 [INDICES]: last 23063.10, z20 -1.73, zc -3.22, resid-z -2.74 [unexplained], 1d -1.64%, |z20|=1.73; 1y-pct=3
- india_vix [INDICES]: last 12.62, z20 1.44, zc 3.88, resid-z n/a [moved], 1d 21.98%, 1-session move +21.98% ≥ 15.0%
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.641 via nifty_50, z -1.0, reacted); midcap_largecap_ratio (rho 0.587 via nifty_midcap_100, z -0.39, quiet); nifty_metal (rho 0.536 via nifty_midcap_100, z -0.49, quiet); nifty_fmcg (rho 0.529 via nifty_50, z -0.21, quiet); dyn_techm_ns (rho 0.524 via nifty_50, z -0.8, quiet)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.529 vs nifty_50, historically leads by 3d
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.524 vs nifty_50, historically leads by 3d
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.587 vs nifty_midcap_100
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.536 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.641, z -1.0); midcap_largecap_ratio (rho 0.587, z -0.39); nifty_metal (rho 0.536, z -0.49); nifty_fmcg (rho 0.529, z -0.21)
- Source: PB Fintech put option buyers laughing all the way to the bank — BusinessLine Mkts, 2026-09-24. https://www.thehindubusinessline.com/markets/pb-fintech-put-option-buyers-laughing-all-the-way-to-the-bank/article71504146.ece
- Source: Market wrap: Cipla, ONGC, HDFC Life, Bajaj Finance top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-cipla-ongc-hdfc-life-bajaj-finance-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134462526.cms
- Source: Stock market prediction for tomorrow: Sensex, Nifty outlook for Friday | Kospi, Taiwan cues to watch | 25 Sept 2026 — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/stock-market-prediction-for-tomorrow-sensex-nifty-outlook-for-friday-kospi-taiwan-cues-to-watch-25-sept-2026-11790250994537.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 10.94] natgas ↑
- natgas [COMMODITIES]: last 3.22, z20 5.94, zc 2.05, resid-z 2.88 [unexplained], 1d 6.48%, 1-session move +6.48% ≥ 5.0%; |z20|=5.94
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.068 vs natgas, historically leads by 4d
- Source: U.S. to Back Argentina’s First LNG Export Project With $6 Billion Loan — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/US-to-Back-Argentinas-First-LNG-Export-Project-With-6-Billion-Loan.html
- Source: Southeast Asia Keeps Building Gas Plants Despite Hormuz LNG Shock — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Southeast-Asia-Keeps-Building-Gas-Plants-Despite-Hormuz-LNG-Shock.html
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 8.36] fx · 4 series ↓
- usd_mxn [FX]: last 17.63, z20 4.70, zc 4.69, resid-z 4.83 [unexplained], 1d 2.01%, |z20|=4.70
- gbp_usd [FX]: last 1.32, z20 -3.51, zc -2.59, resid-z -2.78 [unexplained], 1d -0.92%, |z20|=3.51
- aud_usd [FX]: last 0.70, z20 -3.48, zc -2.91, resid-z -3.02 [unexplained], 1d -1.25%, |z20|=3.48
- eur_usd [FX]: last 1.14, z20 -2.90, zc -2.03, resid-z -1.88 [unexplained], 1d -0.61%, |z20|=2.90; 1y-pct=2
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.609 via usd_mxn, z -15.51, reacted); dyn_icicigi_bo (rho -0.492 via gbp_usd, z 1.47, reacted); dyn_muthootfin_ns (rho 0.459 via aud_usd, z -0.53, quiet); dyn_inoxindia_ns (rho -0.458 via usd_mxn, z -0.93, quiet); nifty_midcap_100 (rho -0.408 via usd_mxn, z -1.74, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.52 vs gbp_usd
- **India receivers**: dyn_policybzr_ns (rho -0.609, z -15.51); dyn_icicigi_bo (rho -0.492, z 1.47); dyn_muthootfin_ns (rho 0.459, z -0.53); dyn_inoxindia_ns (rho -0.458, z -0.93)
- Source: Philip R. Lane: The Outlook for the Euro Area Economy — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260923_1~ac21bf46e3.en.pdf
- Source: Almost ten million people took part in ECB survey on new euro banknotes — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260923~6ebddaf01e.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 7.04] cross-asset · 9 series ↓
- dyn_ms [EQUITIES]: last 195.66, z20 -2.40, zc -0.75, resid-z -1.67 [unexplained], 1d -1.37%, |z20|=2.40
- dyn_bond [EQUITIES]: last 87.84, z20 -2.05, zc -0.84, resid-z 0.59 [quiet], 1d -0.33%, |z20|=2.05; 1y-pct=0
- dyn_gs [EQUITIES]: last 920.42, z20 -2.05, zc -0.90, resid-z -0.41 [quiet], 1d -1.70%, |z20|=2.05
- russell_2000 [INDICES]: last 2823.32, z20 -1.91, zc -0.44, resid-z -0.26 [quiet], 1d -0.54%, |z20|=1.91
- dow_jones [INDICES]: last 51217.01, z20 -1.86, zc -0.73, resid-z -1.17 [quiet], 1d -0.57%, |z20|=1.86
- ust_2y [RATES]: last 4.71, z20 1.27, zc -0.80, resid-z -1.41 [quiet], 1d -1.05%, 1y-pct=98
- tips_10y_real [RATES]: last 2.63, z20 1.22, zc 0.20, resid-z -0.25 [quiet], 1d 0.38%, 1y-pct=99
- ust_10y [RATES]: last 4.96, z20 1.00, zc 0.00, resid-z -0.34 [quiet], 1d 0.00%, 1y-pct=97
- ust_30y [RATES]: last 5.29, z20 0.26, zc 0.00, resid-z -0.16 [quiet], 1d 0.00%, 1y-pct=96
- **Mechanism**: cross-asset · 9 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.724 vs dyn_ms, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.627 vs dyn_bond, historically leads by 5d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.614 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.588 vs dyn_ms, historically leads by 4d
- Watch next: wti (inverse) — not yet - watch; rho -0.521 vs dyn_bond, historically leads by 3d
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks edge lower as crude gains on Mideast uncertainty, eyes on Trump-Xi talks — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-trump-xi-china-talks-iran-war-hormuz-brent-crude-oil-inflation-fed-rate-treasury-yields-meta-apple-tesla-amazon-ai-chip-stock-price-news-24th-september-2026/liveblog/134462304.cms
- Source: Treasury rout, oil spike bleed Indian bonds; 10-year yield jumps most in over 2 months — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/bonds/treasury-rout-oil-spike-bleed-indian-bonds-10-year-yield-jumps-most-in-over-2-months/articleshow/134461900.cms
- Source: US stock market LIVE updates: Nasdaq, S&P open lower amid surging Treasury yields; Oracle shares crash 5% — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/us-stock-market-live-updates-nasdaq-s-p-500-futures-fall-up-to-1-as-bond-sell-off-lifts-fed-rate-hike-bets-11790246230298.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.56), 2025-05-12 (d=0.64)

### [AMBER 6.06] commodities · 2 series ↑
- brent [COMMODITIES]: last 100.89, z20 0.22, zc -0.78, resid-z -1.25 [quiet], 1d -2.12%, 1-session move -2.12% ≥ 1.5%
- wti [COMMODITIES]: last 95.12, z20 0.06, zc 1.13, resid-z 0.77 [quiet], 1d 3.21%, 1-session move +3.21% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.657 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.617 vs brent
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.545 vs brent
- Source: US stocks: US stocks open lower as oil gains on Mideast uncertainty, eyes on Trump-Xi talks — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-us-stocks-open-lower-as-oil-gains-on-mideast-uncertainty-eyes-on-trump-xi-talks/articleshow/134464197.cms
- Source: Saudi Arabia Sells 100 Million Barrels of Crude to Asia via Hormuz — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Sells-100-Million-Barrels-of-Crude-to-Asia-via-Hormuz.html
- Source: Rupee falls 22 paise as crude, dollar demand rise — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-falls-22-paise-as-crude-dollar-demand-rise/articleshow/134462424.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 5.63] dxy ↑
- dxy [FX]: last 101.28, z20 2.63, zc 0.51, resid-z 0.54 [quiet], 1d 0.17%, 20d range extreme; |z20|=2.63; 1y-pct=96
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.28] dyn_meta ↑
- dyn_meta [EQUITIES]: last 767.59, z20 2.28, zc 1.15, resid-z -0.26 [quiet], 1d 3.16%, |z20|=2.28; 1y-pct=100
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.453 via dyn_meta, z -1.05, reacted)
- **India receivers**: dyn_havells_ns (rho -0.453, z -1.05)
- Source: Meta wants to put its Muse AI assistant on your face — but will consumers buy in? — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/meta-gets-price-target-boost-as-jpmorgan-says-muse-agent-has-potential-to-become-the-top-ai-application-since-chatgpt-280ca648?mod=mw_rss_topstories
- Source: Meta gets price-target boost as JPMorgan says Muse agent has potential to become the top AI application since ChatGPT — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/meta-gets-price-target-boost-as-jpmorgan-says-muse-agent-has-potential-to-become-the-top-ai-application-since-chatgpt-280ca648?mod=mw_rss_topstories
- Source: Can Meta’s VR ambitions create a new catalyst for Unity stocks? — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/news/can-metas-vr-ambitions-create-a-new-catalyst-for-unity-stocks/slideshow/134453567.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [AMBER 4.06] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5640.00, z20 2.06, zc 0.65, resid-z 0.25 [quiet], 1d -1.40%, |z20|=2.06; 1y-pct=99
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.369 via dyn_4417_t, z -0.43, quiet)
- **India receivers**: dyn_justdial_bo (rho 0.369, z -0.43)
- Source: IPO reality check! Is GMP a useful signal or just market noise? Here’s what experts think — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/ipos/fpos/ipo-reality-check-is-gmp-a-useful-signal-or-just-market-noise-heres-what-experts-think/articleshow/134452734.cms
- Source: HDFC Bank share price down 25% in 2026 - Opportunity for bottom fishing ahead of new CEO appointment? Experts decode — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-down-25-in-2026-opportunity-for-bottom-fishing-ahead-of-new-ceo-appointment-experts-decode-11790221093029.html
- Source: World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn — CNBC Economy, 2026-09-24. https://www.cnbc.com/2026/09/24/hormuz-blacksea-ukraine-iran-food-security-united-nations-.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↓ (4.03), comex_gold ↓ (3.89), dyn_tech ↑ (3.59), nasdaq_100 ↑ (3.56), dyn_voltas_ns ↓ (3.46), comex_copper ↑ (3.42), gold_silver_ratio ↓ (3.16), dyn_jiofin_bo ↓ (3.0), dyn_indusindbk_bo ↓ (2.98), sofr ↑ (2.14), dyn_hdb ↓ (2.11), usd_brl ↑ (1.93)

## India macro
- nifty_50: 23063.0996 (1d -1.64%, z20 -1.73, flag amber)
- nifty_midcap_100: 60992.2500 (1d -2.24%, z20 -1.74, flag amber)
- usd_inr: 95.9450 (1d 0.27%, z20 1.17, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6446 (1d -0.62%, z20 -0.39, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.5 — "NSE Share Price Highlights: NSE ends with 2% listing gain, India's largest stock exchange "
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.0 — "NSE Share Price Highlights: NSE ends with 2% listing gain, India's largest stock exchange "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.4 — "NSE Share Price Highlights: NSE ends with 2% listing gain, India's largest stock exchange "
- INDIANB.NS (INDIAN BANK) score 62.7 — "Treasury rout, oil spike bleed Indian bonds; 10-year yield jumps most in over 2 months"
- COIN (Coinbase Global, Inc.) score 54.4 — "Global Market: European shares edge lower as Middle East tensions, US-China talks in focus"
- HDB (HDFC Bank Limited) score 50.9 — "Why PB Fintech, HDFC Life, ICICI Pru, Max Financial stocks crashed after IRDAI reform"
- OHI (Omega Healthcare Investors, In) score 48.1 — "NSE shares list with gains on debut day: How much Radhakishan Damani, Raamdeo Agrawal & ot"
- BAC (Bank of America Corporation) score 47.1 — "PB Fintech put option buyers laughing all the way to the bank"
- CHKP (Check Point Software Technolog) score 42.7 — "Sensex, Nifty crash today: What led to 'Thursday Tank' - Top impact made by these news; ch"
- IDBI.NS (IDBI BANK LIMITED) score 41.2 — "PB Fintech put option buyers laughing all the way to the bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.2 — "PB Fintech put option buyers laughing all the way to the bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.2 — "PB Fintech put option buyers laughing all the way to the bank"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.6 — "PB Fintech shares crash 36%, bloodbath wipes off Rs 31,426 cr from m-cap after IRDAI’s ref"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.6 — "PB Fintech shares crash 36%, bloodbath wipes off Rs 31,426 cr from m-cap after IRDAI’s ref"
- TECH (Bio-Techne Corp) score 38.6 — "PB Fintech shares crash 36%, bloodbath wipes off Rs 31,426 cr from m-cap after IRDAI’s ref"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.1 — "Bond crisis worsens! US 30-year Treasury yields surge to highest level since 2004. What li"
- LTH (Life Time Group Holdings, Inc.) score 30.3 — "NSE IPO listing time today: Check share listing price prediction ahead of BSE debut - Will"
- SEPN (Septerna, Inc.) score 29.5 — "Stock market prediction for tomorrow: Sensex, Nifty outlook for Friday | Kospi, Taiwan cue"
- 301077.SZ (CHINASTARS) score 24.6 — "Global Market: European shares edge lower as Middle East tensions, US-China talks in focus"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.7 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"
- JIOFIN.BO (Jio Financial Services Limited) score 21.6 — "Why PB Fintech, HDFC Life, ICICI Pru, Max Financial stocks crashed after IRDAI reform"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.8 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.8 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.7 — "Dividend, stock split record date alert: Last chance to buy today - Noble Polymers, Naturi"
- META (Meta) score 13.1 — "Meta wants to put its Muse AI assistant on your face — but will consumers buy in?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.2 — "Just One Commodity Vessel Left the Strait of Hormuz on Wednesday"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.9 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.8 — "Can IRDAI’s insurance reforms impact NBFCs? Jefferies warns L&T Finance, Piramal Finance, "
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.7 — "PB Fintech shares crash 36%, bloodbath wipes off Rs 31,426 cr from m-cap after IRDAI’s ref"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.6 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.5 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- MS (Morgan Stanley) score 6.9 — "Morgan Stanley employee accidentally leaks bank’s Asia investment pipeline details"
- VT (Vanguard Total World Stock Ind) score 6.5 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- PINELABS.NS (PINE LABS LIMITED) score 5.1 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "Goldman Sachs buys stake in small-cap stock that has surged 50% in less than two months"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.4 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 3.0 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- VOLTAS.NS (VOLTAS LTD) score 1.9 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 1.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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