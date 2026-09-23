# Transmission Layer — board brief · 2026-09-23 19:40Z

data as of **2026-09-23** · 97 series · 9 red / 37 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.376, 4d in regime; vol-pct 0.127, breadth-off 0.625, Markov P(high-vol) 0.026)
- [INVERTED] **safe_haven_gold** — corr20 -0.52, corr60 -0.37, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.09, corr60 0.29, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.12, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.07, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.06, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.4, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0015243893761345273)
- **SETUP** dyn_tna → asx_200: leads 1d (ccf 0.57, β 0.1126, p 0.0); driver zc -1.53 → expected -0.568%. Type hit-rate 0.822 (n=2406).
- **SETUP** dyn_tna → nikkei_225: leads 1d (ccf 0.502, β 0.2051, p 0.0); driver zc -1.53 → expected -1.035%. Type hit-rate 0.822 (n=2406).
- **SETUP** dyn_tna → taiwan_weighted: leads 1d (ccf 0.466, β 0.1855, p 0.0); driver zc -1.53 → expected -0.936%. Type hit-rate 0.822 (n=2406).
- **SETUP** dyn_tna → kospi: leads 1d (ccf 0.354, β 0.2129, p 0.0); driver zc -1.53 → expected -1.074%. Type hit-rate 0.822 (n=2406).
- **SETUP** dyn_tna → nifty_metal: leads 1d (ccf 0.271, β 0.1012, p 0.00123); driver zc -1.53 → expected -0.51%. Type hit-rate 0.822 (n=2406).
- **SETUP** dyn_tna → nifty_midcap_100: leads 1d (ccf 0.259, β 0.0751, p 1e-05); driver zc -1.53 → expected -0.379%. Type hit-rate 0.822 (n=2406).
- Track record · residual_reversion: hit-rate **0.495** (n=1098) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2406) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.35] natgas ↑
- natgas [COMMODITIES]: last 3.15, z20 5.35, zc 1.97, resid-z 2.83 [unexplained], 1d 6.34%, 1-session move +6.34% ≥ 5.0%; |z20|=5.35
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.111 vs natgas, historically leads by 4d
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Source: TotalEnergies to Develop Offshore Gas Field to Boost Nigeria LNG Supply — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-to-Develop-Offshore-Gas-Field-to-Boost-Nigeria-LNG-Supply.html
- Source: Washington Needs This LNG Deal More Than Beijing Does — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Washington-Needs-This-LNG-Deal-More-Than-Beijing-Does.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 8.75] cross-asset · 8 series ↑
- dyn_ms [EQUITIES]: last 198.63, z20 -2.23, zc -0.42, resid-z 0.15 [quiet], 1d -0.79%, |z20|=2.23
- dyn_bond [EQUITIES]: last 88.10, z20 -1.89, zc -3.15, resid-z -0.26 [priced], 1d -1.06%, 1y-pct=0
- ust_2y [RATES]: last 4.76, z20 1.72, zc 0.00, resid-z 0.00 [quiet], 1d 0.00%, |z20|=1.72; 1y-pct=99
- russell_2000 [INDICES]: last 2844.79, z20 -1.65, zc -1.43, resid-z -1.55 [unexplained], 1d -1.59%, |z20|=1.65
- dow_jones [INDICES]: last 51569.46, z20 -1.54, zc -0.74, resid-z -0.16 [quiet], 1d -0.57%, |z20|=1.54
- tips_10y_real [RATES]: last 2.62, z20 1.25, zc -1.19, resid-z -1.38 [quiet], 1d -2.24%, 1d move -6.0bps ≥ 5bps; 1y-pct=98
- ust_10y [RATES]: last 4.96, z20 1.11, zc -1.02, resid-z -0.67 [quiet], 1d -1.00%, 1y-pct=98
- ust_30y [RATES]: last 5.29, z20 0.28, zc -1.21, resid-z -0.83 [quiet], 1d -0.94%, 1y-pct=96
- **Mechanism**: cross-asset · 8 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.381 via ust_2y, z 0.98, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.747 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.728 vs dyn_ms, historically leads by 4d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.615 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.59 vs dyn_ms, historically leads by 4d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.569 vs russell_2000, historically leads by 1d
- **India receivers**: midcap_largecap_ratio (rho -0.381, z 0.98)
- Source: Wall Street falls as oil prices, Treasury yields rise — Mint Markets, 2026-09-23. https://www.livemint.com/market/wall-street-falls-as-oil-prices-treasury-yields-rise-11790188753276.html
- Source: 10-year US Treasury yields surges over 5.05% to 19-year high — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/10-year-us-treasury-yields-surges-over-5-05-to-19-year-high/articleshow/134441042.cms
- Source: U.S. MORTGAGE RATE TOPS 7% FOR FIRST TIME SINCE 2025 The average U.S. 30-year fixed mortgage rate jumped to 7.12%, its highest level since May 2024. Rates have climbed as Fed tightening, higher oil prices and rising Treasury yields increase borrowing costs. The surge is hitting housing demand, with  — DeItaone, 2026-09-23. https://t.me/walter_bloomberg/36047
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.59), 2025-05-12 (d=0.67)

### [RED 7.94] fx · 4 series ↓
- usd_mxn [FX]: last 17.51, z20 4.27, zc 4.05, resid-z 4.01 [unexplained], 1d 1.72%, |z20|=4.27
- gbp_usd [FX]: last 1.32, z20 -3.46, zc -2.67, resid-z -2.53 [unexplained], 1d -0.96%, |z20|=3.46
- aud_usd [FX]: last 0.70, z20 -3.21, zc -2.51, resid-z -2.53 [unexplained], 1d -1.08%, |z20|=3.21
- eur_usd [FX]: last 1.14, z20 -3.04, zc -2.18, resid-z -1.72 [unexplained], 1d -0.67%, |z20|=3.04; 1y-pct=4
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.418 via gbp_usd, z -0.18, quiet); dyn_muthootfin_ns (rho 0.401 via aud_usd, z -0.31, quiet); dyn_inoxindia_ns (rho 0.351 via aud_usd, z 0.3, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.55 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.418, z -0.18); dyn_muthootfin_ns (rho 0.401, z -0.31); dyn_inoxindia_ns (rho 0.351, z 0.3)
- Source: Philip R. Lane: The Outlook for the Euro Area Economy — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260923_1~ac21bf46e3.en.pdf
- Source: Almost ten million people took part in ECB survey on new euro banknotes — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260923~6ebddaf01e.en.html
- Source: Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic and global orders — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/stocks/news/sterling-and-wilson-renewable-energy-shares-rally-8-after-securing-rs-985-crore-domestic-and-global-orders/articleshow/134402652.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.94] dxy ↑
- dxy [FX]: last 101.10, z20 2.94, zc 1.70, resid-z 1.14 [moved], 1d 0.56%, 20d range extreme; |z20|=2.94
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.23] wti ↓
- wti [COMMODITIES]: last 92.66, z20 -0.23, zc -0.70, resid-z -1.00 [quiet], 1d -2.04%, 1-session move -2.04% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.976 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.627 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.601 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.544 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.525 vs wti
- Source: Wall Street falls as oil prices, Treasury yields rise — Mint Markets, 2026-09-23. https://www.livemint.com/market/wall-street-falls-as-oil-prices-treasury-yields-rise-11790188753276.html
- Source: Imperial Oil Becomes First Major Alberta Energy Company to Oppose Separatism — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/Imperial-Oil-Becomes-First-Major-Alberta-Energy-Company-to-Oppose-Separatism.html
- Source: EIA Reports 3M Barrel Crude Build as Distillate Stocks Fall 12% Below Average — OilPrice, 2026-09-23. https://oilprice.com/Energy/Energy-General/EIA-Reports-3M-Barrel-Crude-Build-as-Distillate-Stocks-Fall-12-Below-Average.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 5.16] cross-asset · 2 series ↑
- nasdaq_100 [INDICES]: last 30469.73, z20 2.32, zc -0.60, resid-z -0.03 [quiet], 1d -0.84%, |z20|=2.32; 1y-pct=97
- dyn_nvda [EQUITIES]: last 225.66, z20 0.81, zc -0.57, resid-z -0.10 [quiet], 1d -1.40%, 1y-pct=96
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.927 vs nasdaq_100, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.912 vs nasdaq_100, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.66 vs nasdaq_100, historically leads by 2d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.607 vs nasdaq_100
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.567 vs nasdaq_100
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US 10-year Treasury yield tops 5% for first time since 2007; Nasdaq slumps over 1% — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks slide as oil, strong data drive bond yields higher — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: The Nasdaq’s rapid rise to a record is sending a message to investors: Don’t wait for a pullback to buy — MarketWatch Top, 2026-09-22. https://www.marketwatch.com/story/the-nasdaqs-rapid-rise-to-a-record-is-sending-a-message-to-investors-dont-wait-for-a-pullback-to-buy-5f533ed8?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.11), 2025-08-28 (d=0.2)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.40 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.366 via dyn_4417_t, z 0.69, quiet)
- **India receivers**: dyn_justdial_bo (rho 0.366, z 0.69)
- Source: Sebi board is set to grow. Experts say it's missing one safeguard it needs most — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/sebi-board-expansion-securities-markets-code-2025-appointmentprocess-11788844688106.html
- Source: How to invest amid heightened uncertainty? Look at multi-asset allocation funds, say experts — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/how-to-invest-amid-heightened-uncertainty-look-at-multi-asset-allocation-funds-say-experts-11790078842845.html
- Source: Vedanta Aluminium stock jumps 4% days after hitting 52-week low! Can it reclaim demerger level? Experts decode outlook — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/vedanta-aluminium-stock-jumps-4-days-after-hitting-52-week-low-can-it-reclaim-demerger-level-experts-decode-outlook-11790062916085.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [AMBER 4.73] crypto · 2 series ↑
- btc_usd [CRYPTO]: last 84447.35, z20 1.90, zc -0.56, resid-z -0.25 [quiet], 1d -2.00%, |z20|=1.90
- eth_usd [CRYPTO]: last 2674.99, z20 1.75, zc -0.69, resid-z -0.03 [quiet], 1d -2.82%, |z20|=1.75
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-15 (z-distance 0.02).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.361 via eth_usd, z -0.2, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.536 vs btc_usd, historically leads by 1d
- **India receivers**: dyn_cartrade_ns (rho 0.361, z -0.2)
- Source: Bitcoin holds near $86,000 as spot Bitcoin ETF inflows hit 11-month high of $999 million — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-86000-as-spot-bitcoin-etf-inflows-hit-11-month-high-of-999-million/articleshow/134432852.cms
- Source: $3 trillion crypto comeback: Can Bitcoin bulls reclaim $100K and push higher? — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/3-trillion-crypto-comeback-can-bitcoin-bulls-reclaim-100k-and-push-higher/articleshow/134412450.cms
- Source: Bitcoin jumps nearly 5% to cross $85,000 as strong ETF inflows and institutional buying boost crypto momentum — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-jumps-nearly-5-to-cross-85000-as-strong-etf-inflows-and-institutional-buying-boost-crypto-momentum/articleshow/134406404.cms
- Historical analogues: 2026-01-15 (d=0.02), 2026-04-16 (d=0.05), 2024-11-21 (d=0.09)

## Watchlist (below surfacing floor)
dyn_bac ↓ (4.28), dyn_meta ↑ (4.21), gold_silver_ratio ↓ (4.01), midcap_largecap_ratio ↑ (3.98), comex_gold ↓ (3.63), comex_copper ↑ (3.56), dyn_tech ↑ (3.55), dyn_voltas_ns ↓ (2.99), ust_2s10s ↓ (2.68), sofr ↑ (2.6), taiwan_weighted ↑ (2.31), dyn_icicigi_bo ↓ (2.18)

## India macro
- nifty_50: 23446.8008 (1d 0.50%, z20 -0.69, flag none)
- nifty_midcap_100: 62391.4492 (1d 0.70%, z20 -0.38, flag none)
- usd_inr: 95.7300 (1d 0.02%, z20 0.81, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6610 (1d 0.20%, z20 0.98, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 69.7 — "NLC India raises ₹500 crore via issuance of commercial papers"
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.9 — "NLC India raises ₹500 crore via issuance of commercial papers"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 67.2 — "NLC India raises ₹500 crore via issuance of commercial papers"
- INDIANB.NS (INDIAN BANK) score 53.7 — "SEBI plans to review merchant banking and IPO rules"
- COIN (Coinbase Global, Inc.) score 52.7 — "Global Market: European shares edge higher as lower oil prices lift sentiment"
- OHI (Omega Healthcare Investors, In) score 48.5 — "Top stocks in focus today: Investors must watch GHCL, Max Estates, Bharat Dynamics shares "
- BAC (Bank of America Corporation) score 46.3 — "SEBI plans to review merchant banking and IPO rules"
- HDB (HDFC Bank Limited) score 44.0 — "Sedemac Mechatronics block deal: A91, Xponentia, HDFC Life likely to offload 10% stake: Re"
- CHKP (Check Point Software Technolog) score 42.1 — "Nifty outlook, guide tomorrow: Why 23,600 matters; bullish candle formed, check resistance"
- IDBI.NS (IDBI BANK LIMITED) score 39.3 — "SEBI plans to review merchant banking and IPO rules"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.3 — "SEBI plans to review merchant banking and IPO rules"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.3 — "SEBI plans to review merchant banking and IPO rules"
- BOND (PIMCO Active Bond Exchange-Tra) score 31.8 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks slide as oil, strong data driv"
- SEPN (Septerna, Inc.) score 28.6 — "Stock market prediction for today: Sensex, Nifty outlook for Thursday | Kospi, Taiwan cues"
- TECHM.NS (TECH MAHINDRA LIMITED) score 28.1 — "IRAN DEFENDS NUCLEAR RIGHTS, SIGNALS OPENNESS TO TALKS Iranian President Masoud Pezeshkian"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 28.1 — "IRAN DEFENDS NUCLEAR RIGHTS, SIGNALS OPENNESS TO TALKS Iranian President Masoud Pezeshkian"
- TECH (Bio-Techne Corp) score 28.1 — "IRAN DEFENDS NUCLEAR RIGHTS, SIGNALS OPENNESS TO TALKS Iranian President Masoud Pezeshkian"
- LTH (Life Time Group Holdings, Inc.) score 27.6 — "U.S. MORTGAGE RATE TOPS 7% FOR FIRST TIME SINCE 2025 The average U.S. 30-year fixed mortga"
- 301077.SZ (CHINASTARS) score 24.1 — "DEMOCRATS PUSH TRUMP FOR U.S.-CHINA AI DEAL Seventeen Democratic senators are urging Presi"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 22.8 — "Top breakout stocks to buy today: Aptus, KRBL, Tata Steel, Radico, GNFC by Sumeet Bagadia "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 22.8 — "Top breakout stocks to buy today: Aptus, KRBL, Tata Steel, Radico, GNFC by Sumeet Bagadia "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.4 — "IRAN'S PRESIDENT PEZESHKIAN: IRAN NEEDS NUCLEAR ENERGY NOT NUCLEAR BOMB"
- JIOFIN.BO (Jio Financial Services Limited) score 17.9 — "The ingredients for a financial reckoning are all in place"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.3 — "FED’S BARR SIGNALS MORE RATE HIKES AHEAD Fed Governor Michael Barr says further rate hikes"
- META (Meta) score 11.1 — "Why physical gold sales lost sheen on Ganesha Chaturthi? Will yellow metal regain its glit"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.3 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.2 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "The real estate portfolio of Zendaya and Tom Holland, plus her plans for a room just for h"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.5 — "Sebi board is set to grow. Experts say it's missing one safeguard it needs most"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.2 — "The digitalisation of money, payments and finance"
- PINELABS.NS (PINE LABS LIMITED) score 6.1 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- VT (Vanguard Total World Stock Ind) score 5.5 — "‘Built for the World in India’: Nippon AMC’s Sikka sees manufacturing opportunity amid glo"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.1 — "Stylam Industries gets BUY from ICICI Direct; 21% upside seen — check price target"
- MS (Morgan Stanley) score 4.9 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- GS (Goldman Sachs Group, Inc. (The) score 4.7 — "Goldman Sees China Oil Imports Staying Subdued in Fourth Quarter"
- TNA (Direxion Small Cap Bull 3X ETF) score 4.4 — "Small-cap stocks trade at nearly twice Nifty 50 valuation, says VK Vijayakumar"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.1 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 3.6 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- VOLTAS.NS (VOLTAS LTD) score 1.1 — "Voltas share price: Nuvama upgrades rating but Jefferies cuts target price after analyst m"
- DELL (Dell Technologies Inc.) score 0.1 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"

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