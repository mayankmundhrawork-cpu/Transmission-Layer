# Transmission Layer — board brief · 2026-10-14 20:12Z

data as of **2026-10-14** · 97 series · 11 red / 28 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.666, 8d in regime; vol-pct 0.684, breadth-off 0.647, Markov P(high-vol) 0.041)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.43, contra nifty_50 corr20=0.19, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.23, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.13, corr60 0.15, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.02, corr60 -0.08, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.27, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.72, corr60 0.23, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0031777392947298644)
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.564, β 0.348, p 0.0); driver zc -1.78 → expected -0.453%. Type hit-rate 0.823 (n=2126).
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.554, β 0.6364, p 0.0); driver zc -1.99 → expected -1.267%. Type hit-rate 0.823 (n=2126).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.551, β 0.6317, p 0.0); driver zc -1.99 → expected -1.258%. Type hit-rate 0.823 (n=2126).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.546, β 0.882, p 0.0); driver zc -1.78 → expected -1.148%. Type hit-rate 0.823 (n=2126).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.542, β 0.8831, p 0.0); driver zc -1.78 → expected -1.15%. Type hit-rate 0.823 (n=2126).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.541, β 0.8408, p 0.0); driver zc -1.56 → expected -0.904%. Type hit-rate 0.823 (n=2126).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.522, β 0.8299, p 0.0); driver zc -1.56 → expected -0.893%. Type hit-rate 0.823 (n=2126).
- **SETUP** russell_2000 → nikkei_225: leads 1d (ccf 0.507, β 0.6072, p 0.0); driver zc -1.84 → expected -1.244%. Type hit-rate 0.823 (n=2126).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.471, β 0.2817, p 0.0); driver zc -1.56 → expected -0.303%. Type hit-rate 0.823 (n=2126).
- **SETUP** russell_2000 → taiwan_weighted: leads 1d (ccf 0.465, β 0.5479, p 0.0); driver zc -1.84 → expected -1.122%. Type hit-rate 0.823 (n=2126).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.449, β 0.1978, p 0.0); driver zc -1.99 → expected -0.394%. Type hit-rate 0.823 (n=2126).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.407, β 0.7011, p 0.0); driver zc -1.99 → expected -1.396%. Type hit-rate 0.823 (n=2126).
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.406, β 0.2478, p 0.0); driver zc -1.53 → expected -0.761%. Type hit-rate 0.823 (n=2126).
- **SETUP** russell_2000 → aud_usd: leads 1d (ccf 0.4, β 0.1827, p 0.0); driver zc -1.84 → expected -0.374%. Type hit-rate 0.823 (n=2126).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.34, β 0.0758, p 0.0); driver zc -1.53 → expected -0.233%. Type hit-rate 0.823 (n=2126).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.29, β 0.3576, p 0.0); driver zc -1.78 → expected -0.466%. Type hit-rate 0.823 (n=2126).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.278, β 0.2416, p 0.0); driver zc -1.84 → expected -0.495%. Type hit-rate 0.823 (n=2126).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.264, β 0.3443, p 0.0); driver zc -1.78 → expected -0.448%. Type hit-rate 0.823 (n=2126).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.255, β 0.3085, p 2e-05); driver zc -1.56 → expected -0.332%. Type hit-rate 0.823 (n=2126).
- Track record · residual_reversion: hit-rate **0.492** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2126) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.22] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 73.94, z20 4.39, zc n/a, resid-z n/a [quiet], 1d 4.72%, GSR<75 (extreme low); |z20|=4.39
- comex_silver [COMMODITIES]: last 55.77, z20 -2.62, zc -2.96, resid-z -3.10 [unexplained], 1d -5.73%, |z20|=2.62
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.521 vs gold_silver_ratio, historically leads by 3d
- Source: Silver futures plunge 4% on MCX ahead of US CPI; rising oil adds pressure — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/commodities/silver-futures-plunge-4-on-mcx-ahead-of-us-cpi-rising-oil-adds-pressure/articleshow/134946048.cms
- Source: SPOT SILVER FALLS NEARLY 3% TO $57.58/OZ — DeItaone, 2026-10-14. https://t.me/walter_bloomberg/37071
- Source: Gold prices rise to Rs 1.50 lakh/10g; silver gains ahead of US economic data. Key levels to track — ET Markets, 2026-10-13. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-rise-to-rs-1-50-lakh/10g-silver-gains-ahead-of-us-economic-data-key-levels-to-track/articleshow/134908879.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.82] usd_inr ↓
- usd_inr [FX]: last 95.14, z20 -2.82, zc -1.25, resid-z -0.90 [quiet], 1d -0.66%, 20d range extreme; |z20|=2.82
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.425 via usd_inr, z 3.79, reacted); dyn_karurvysya_ns (rho -0.355 via usd_inr, z 1.7, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.425, z 3.79); dyn_karurvysya_ns (rho -0.355, z 1.7)
- Source: Rupee extends rise but falters past 95/$ on importer hedging, outflows — BusinessLine Mkts, 2026-10-14. https://www.thehindubusinessline.com/markets/forex/rupee-extends-rise-but-falters-past-95-on-importer-hedging-outflows/article71583244.ece
- Source: Rupee extends rise but falters past 95/USD on importer hedging, outflows — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-extends-rise-but-falters-past-95/usd-on-importer-hedging-outflows/articleshow/134939222.cms
- Source: Rupee rises 44 paise to 94.92 against US dollar in early trade — BusinessLine Mkts, 2026-10-14. https://www.thehindubusinessline.com/markets/forex/rupee-rises-44-paise-to-9492-against-us-dollar-in-early-trade/article71582257.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.7] cross-asset · 2 series ↑
- dyn_tataelxsi_ns [EQUITIES]: last 3623.10, z20 3.87, zc 2.60, resid-z 3.42 [unexplained], 1d 5.73%, |z20|=3.87
- nifty_it [INDICES]: last 30171.00, z20 2.90, zc 0.48, resid-z 0.84 [quiet], 1d 1.14%, |z20|=2.90
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-31 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho 0.86 via nifty_it, z 1.81, reacted); nifty_fmcg (rho 0.562 via dyn_tataelxsi_ns, z 0.28, quiet); dyn_justdial_bo (rho 0.54 via nifty_it, z 1.4, reacted); nifty_50 (rho 0.493 via dyn_tataelxsi_ns, z -0.7, quiet); dyn_tatatech_ns (rho 0.489 via nifty_it, z 1.81, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.562 vs dyn_tataelxsi_ns
- **India receivers**: dyn_techm_ns (rho 0.86, z 1.81); nifty_fmcg (rho 0.562, z 0.28); dyn_justdial_bo (rho 0.54, z 1.4); nifty_50 (rho 0.493, z -0.7)
- Source: Tata Elxsi stock rebounds as growth improves in Q2. Can it continue? — Mint Markets, 2026-10-14. https://www.livemint.com/market/mark-to-market/tata-elxsi-q2-results-stock-recovery-ai-growth-outlook-11791957021978.html
- Source: Tata Elxsi Q2 results impact: IT stock soars 7%- Buy, sell, or hold? Check highlights, target price, share price trend — Mint Markets, 2026-10-14. https://www.livemint.com/market/stock-market-news/tata-elxsi-q2-results-impact-it-stock-soars-7-buy-sell-or-hold-check-highlights-target-price-share-price-trend-11791906874922.html
- Source: Tata Elxsi shares jump 7% after Q2 results, but Morgan Stanley, Motilal Oswal reiterate bearish calls — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/stocks/news/tata-elxsi-shares-jump-7-after-q2-results-but-morgan-stanley-motilal-oswal-reiterate-bearish-calls/articleshow/134931786.cms
- Historical analogues: 2025-07-31 (d=0.34), 2025-01-30 (d=0.36), 2025-07-09 (d=0.4)

### [RED 5.79] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 89.85, z20 3.79, zc 3.51, resid-z 2.95 [unexplained], 1d 8.33%, |z20|=3.79
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho -0.425 via dyn_idbi_ns, z -2.82, reacted); dyn_havells_ns (rho 0.354 via dyn_idbi_ns, z 1.71, reacted)
- **India receivers**: usd_inr (rho -0.425, z -2.82); dyn_havells_ns (rho 0.354, z 1.71)
- Source: IDBI Bank stake sale: Will Fairfax’s entry benefit minority shareholders? What investors should know — Mint Markets, 2026-10-14. https://www.livemint.com/market/stock-market-news/idbi-bank-stake-sale-will-fairfax-s-entry-benefit-minority-shareholders-what-investors-should-know-11791975473321.html
- Source: IDBI Bank shares rally 13%, market value swells by Rs 11,460 crore amid muted market. What lies ahead? — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/stocks/news/idbi-bank-shares-rally-13-market-value-swells-by-rs-11460-crore-amid-muted-market-what-lies-ahead/articleshow/134934298.cms
- Source: IDBI Bank shares surge 13% today in a weak market - Q2 results expectations, share price trend — Mint Markets, 2026-10-14. https://www.livemint.com/market/stock-market-news/idbi-bank-shares-surge-13-today-in-a-weak-market-q2-results-expectations-share-price-trend-11791953348353.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

### [AMBER 4.95] crypto · 2 series ↓
- eth_usd [CRYPTO]: last 2429.04, z20 -2.12, zc -0.70, resid-z -0.16 [quiet], 1d -2.71%, |z20|=2.12
- btc_usd [CRYPTO]: last 81799.00, z20 -1.72, zc -0.76, resid-z -0.09 [quiet], 1d -1.56%, |z20|=1.72
- **Mechanism**: crypto · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-11-05 (z-distance 0.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Bitcoin Slides as Wall Street Risk Pullback Tests Bullish Turn — Mint Markets, 2026-10-14. https://www.livemint.com/market/bitcoin-slides-as-wall-street-risk-pullback-tests-bullish-turn-11792003663551.html
- Source: Bitcoin hovers near $83K as Asian stock sell-off triggers over $800 million in crypto liquidations — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-hovers-near-83k-as-asian-stock-sell-off-triggers-over-800-million-in-crypto-liquidations/articleshow/134939967.cms
- Source: MICHAEL SAYLOR PREDICTS BITCOIN WILL SURGE BACK ABOVE $100,000 Strategy ($MSTR ) Chairman Michael Saylor says Bitcoin's bear market is over, predicting a return above $100,000. Key takeaways: * Bitcoin: Trading near $83,000. * Bottom: Saylor believes BTC bottomed just below $60,000. * Forecast: Expe — DeItaone, 2026-10-13. https://t.me/walter_bloomberg/37031
- Historical analogues: 2025-11-05 (d=0.09), 2025-06-05 (d=0.09), 2026-06-09 (d=0.15)

### [AMBER 4.89] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.91, z20 0.95, zc 0.74, resid-z 0.80 [quiet], 1d 1.39%, 1y-pct=97
- ust_30y [RATES]: last 5.60, z20 0.87, zc 0.00, resid-z 0.11 [quiet], 1d 0.00%, 1y-pct=97
- ust_10y [RATES]: last 5.24, z20 0.79, zc 0.38, resid-z 0.49 [quiet], 1d 0.38%, 1y-pct=96
- ust_2y [RATES]: last 4.80, z20 0.26, zc 0.81, resid-z 0.85 [quiet], 1d 1.05%, 1y-pct=96
- dyn_bond [EQUITIES]: last 87.27, z20 -0.25, zc 0.63, resid-z 1.21 [quiet], 1d 0.22%, 1y-pct=4
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.533 vs ust_30y
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.09 vs tips_10y_real, historically leads by 1d
- Source: Rising bond yields and higher inflation leave the Fed trapped in a rate-hike dilemma — MarketWatch Top, 2026-10-14. https://www.marketwatch.com/story/rising-bond-yields-and-higher-inflation-leave-the-fed-trapped-in-a-rate-hike-dilemma-d34ba326?mod=mw_rss_topstories
- Source: TWO-YEAR U.S. TREASURY YIELDS HIT HIGHEST LEVEL SINCE SEPT 29, LAST UP 12.72 BASIS POINTS AT 4.92% — DeItaone, 2026-10-14. https://t.me/walter_bloomberg/37073
- Source: Global Market: Asian investors pour money into hedge funds as bond markets falter — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-asian-investors-pour-money-into-hedge-funds-as-bond-markets-falter/articleshow/134937550.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 4.5] dyn_bac ↓
- dyn_bac [EQUITIES]: last 51.40, z20 -2.50, zc -3.24, resid-z 0.82 [moved], 1d -4.74%, |z20|=2.50
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: 5 Challenges Facing South America’s Copper Boom — OilPrice, 2026-10-14. https://oilprice.com/Metals/Commodities/5-Challenges-Facing-South-Americas-Copper-Boom.html
- Source: Big Tech Pushes Back Against Paying for America's Aging Power Grid — OilPrice, 2026-10-14. https://oilprice.com/Energy/Energy-General/Big-Tech-Pushes-Back-Against-Paying-for-Americas-Aging-Power-Grid.html
- Source: Bank of America adds a profit miss to the misery of a $1.2 billion government fine — MarketWatch Top, 2026-10-14. https://www.marketwatch.com/story/bank-of-america-adds-a-profit-miss-to-the-misery-of-a-1-2-billion-government-fine-d4420bfa?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-23 (d=0.03), 2025-03-31 (d=0.12)

### [AMBER 4.27] dyn_301077_sz ↓
- dyn_301077_sz [EQUITIES]: last 20.40, z20 -2.27, zc -0.98, resid-z -0.36 [quiet], 1d -2.58%, |z20|=2.27
- **Mechanism**: dyn_301077_sz ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Source: China sentences 3 more Myanmar crime bosses to death in scam centre crackdown — SCMP Economy, 2026-10-13. https://www.scmp.com/news/china/politics/article/3370757/china-sentences-3-more-myanmar-crime-bosses-death-scam-centre-crackdown?utm_source=rss_feed
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

## Watchlist (below surfacing floor)
dyn_cartrade_ns ↑ (4.25), shanghai_comp ↓ (4.11), vix ↑ (3.95), dyn_rs ↑ (3.78), eur_usd ↓ (3.63), natgas ↑ (3.58), dyn_4417_t ↑ (3.48), dxy ↑ (3.46), russell_2000 ↓ (3.36), kospi ↓ (3.34), dyn_dell ↓ (3.31), usd_cny ↓ (2.73)

## India macro
- nifty_50: 22622.6992 (1d -0.44%, z20 -0.70, flag amber)
- nifty_midcap_100: 59398.1484 (1d -0.10%, z20 -0.62, flag none)
- usd_inr: 95.1400 (1d -0.66%, z20 -2.82, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6256 (1d 0.34%, z20 -0.33, flag none)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · India trade / CAD data T-1d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.3 — "China's Coal Imports Fall 6% as Prices Hit Nearly 3-Year High"
- INDIANB.NS (INDIAN BANK) score 82.5 — "US stocks: US market slides as hot CPI data fuels rate-hike bets; chips, banks weigh"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.3 — "India’s Largest IPO: Jio Platforms sets ₹1,065-1,119 price band, below street estimates"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.9 — "India’s Largest IPO: Jio Platforms sets ₹1,065-1,119 price band, below street estimates"
- BAC (Bank of America Corporation) score 77.6 — "US stocks: US market slides as hot CPI data fuels rate-hike bets; chips, banks weigh"
- HDB (HDFC Bank Limited) score 70.0 — "US stocks: US market slides as hot CPI data fuels rate-hike bets; chips, banks weigh"
- IDBI.NS (IDBI BANK LIMITED) score 67.7 — "US stocks: US market slides as hot CPI data fuels rate-hike bets; chips, banks weigh"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 67.7 — "US stocks: US market slides as hot CPI data fuels rate-hike bets; chips, banks weigh"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 67.7 — "US stocks: US market slides as hot CPI data fuels rate-hike bets; chips, banks weigh"
- TECHM.NS (TECH MAHINDRA LIMITED) score 58.3 — "AI BOOM FUELS SHARPEST COMPUTER PRICE INFLATION IN TWO DECADES The massive AI infrastructu"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 56.6 — "AI BOOM FUELS SHARPEST COMPUTER PRICE INFLATION IN TWO DECADES The massive AI infrastructu"
- TECH (Bio-Techne Corp) score 56.6 — "AI BOOM FUELS SHARPEST COMPUTER PRICE INFLATION IN TWO DECADES The massive AI infrastructu"
- COIN (Coinbase Global, Inc.) score 53.7 — "Pearl Global: This multibagger textile stock gets back-to-back target price upgrades—shoul"
- OHI (Omega Healthcare Investors, In) score 49.3 — "Zetwerk raises ₹2,251 crore from 99 anchor investors ahead of October 15 IPO"
- TGT (Target Corporation) score 38.5 — "U.S. INFLATION STAYS ABOVE FED TARGET FOR 66 STRAIGHT MONTHS September CPI rose 3.7% YoY, "
- CHKP (Check Point Software Technolog) score 35.1 — "Reliance Jio IPO: Good news for RIL shareholders! Check what the reservation quota is for "
- BOND (PIMCO Active Bond Exchange-Tra) score 34.5 — "Rising bond yields and higher inflation leave the Fed trapped in a rate-hike dilemma"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.3 — "GASOLINE DRIVES MORE THAN HALF OF U.S. INFLATION SURGE Gasoline prices jumped 9.1% in Sept"
- LTH (Life Time Group Holdings, Inc.) score 27.4 — "PRESIDENT TRUMP'S SCHEDULE — WEDNESDAY, OCTOBER 14, 2026 All times Eastern (ET) 🔸 11:00 AM"
- SEPN (Septerna, Inc.) score 24.7 — "U.S. INFLATION RUNS HOTTER THAN HEADLINE NUMBERS SUGGEST Unrounded September CPI rose 0.64"
- 301077.SZ (CHINASTARS) score 23.0 — "China's Coal Imports Fall 6% as Prices Hit Nearly 3-Year High"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.6 — "Jio Platforms IPO confirms RIL reservation quota — How will it impact Reliance share price"
- JIOFIN.BO (Jio Financial Services Limited) score 17.9 — "SEBI continues curbs on Rajesh Exports, flags gaps in financial disclosures"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.2 — "Q2 Earnings Results Live Updates: Tata Technologies Q2 profit rises 4% YoY to Rs 171.4 cro"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.2 — "Q2 Earnings Results Live Updates: Tata Technologies Q2 profit rises 4% YoY to Rs 171.4 cro"
- RS (Reliance, Inc.) score 15.9 — "Jio IPO: 5 strengths that put the Reliance-backed digital giant in spotlight"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.4 — "TWO-YEAR U.S. TREASURY YIELDS HIT HIGHEST LEVEL SINCE SEPT 29, LAST UP 12.72 BASIS POINTS "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.3 — "Buzzing stocks: Watch out for these 16 stocks including Adani Enterprises, Polycab, ICICI "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 11.2 — "These unpopular solutions could rescue Social Security’s finances. Here’s who could pay th"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "Indian families keep just 14% abroad, global peers 30-40%: Prithipal Singh on going global"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.6 — "These unpopular solutions could rescue Social Security’s finances. Here’s who could pay th"
- VT (Vanguard Total World Stock Ind) score 8.6 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- GS (Goldman Sachs Group, Inc. (The) score 7.8 — "BlackRock, Goldman Sachs, Nomura among key investors as Zetwerk mops up Rs 2,251 crore in "
- JEF (Jefferies Financial Group Inc.) score 7.7 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- NVDA (NVIDIA Corporation) score 6.7 — "Nvidia pledges $250 million in computing resources to boost UK AI safety research"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.5 — "Bajaj Broking rolls out algorithm trading platform for retail investors"
- META (Meta) score 4.8 — "Lemonn adds commodity derivatives, enters MCX with six metals and energy contracts"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.9 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.2 — "Piero Cipollone: Interview with Corriere della Sera"
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