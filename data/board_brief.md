# Transmission Layer — board brief · 2026-11-24 02:54Z

data as of **2026-11-24** · 97 series · 7 red / 37 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 1.0, 7d in regime; vol-pct None, breadth-off 1.0, Markov P(high-vol) 1.0)
- [WEAK] **safe_haven_gold** — corr20 -0.19, corr60 -0.27, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.19, corr60 0.05, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.19, corr60 -0.01, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.34, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.002288413662045352)
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.574, β 0.3456, p 0.0); driver zc -1.93 → expected -0.954%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.567, β 0.434, p 0.0); driver zc -2.9 → expected -1.606%. Type hit-rate 0.821 (n=2070).
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.542, β 0.6415, p 0.0); driver zc -3.14 → expected -3.6%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.516, β 0.8483, p 0.0); driver zc -2.9 → expected -3.138%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.492, β 0.2827, p 0.0); driver zc -2.9 → expected -1.046%. Type hit-rate 0.821 (n=2070).
- **SETUP** vix → asx_200: leads 1d (ccf -0.485, β -0.0413, p 0.0); driver zc 2.1 → expected -1.082%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.485, β 0.1948, p 0.0); driver zc -3.22 → expected -1.307%. Type hit-rate 0.821 (n=2070).
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.483, β 0.2082, p 0.0); driver zc -2.02 → expected -0.569%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → taiwan_weighted: leads 1d (ccf 0.474, β 0.5996, p 0.0); driver zc -1.93 → expected -1.656%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.472, β -0.2658, p 0.0); driver zc -2.9 → expected 0.983%. Type hit-rate 0.821 (n=2070).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.458, β 0.2397, p 0.0); driver zc -2.21 → expected -0.571%. Type hit-rate 0.821 (n=2070).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.457, β 0.1914, p 0.0); driver zc -3.14 → expected -1.074%. Type hit-rate 0.821 (n=2070).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.45, β -0.0283, p 0.0); driver zc 2.1 → expected -0.741%. Type hit-rate 0.821 (n=2070).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.44, β -0.1807, p 0.0); driver zc -3.14 → expected 1.014%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → aud_usd: leads 1d (ccf 0.44, β 0.1988, p 0.0); driver zc -1.93 → expected -0.549%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_gs → taiwan_weighted: leads 1d (ccf 0.434, β 0.3683, p 0.0); driver zc -3.22 → expected -2.47%. Type hit-rate 0.821 (n=2070).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.429, β -0.0771, p 0.0); driver zc 2.1 → expected -2.02%. Type hit-rate 0.821 (n=2070).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.417, β 0.7318, p 0.0); driver zc -3.14 → expected -4.106%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.405, β 0.26, p 0.0); driver zc -4.36 → expected -3.642%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_bond → usd_jpy: leads 1d (ccf -0.405, β -0.7151, p 0.0); driver zc 1.9 → expected -0.504%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_gs → aud_usd: leads 1d (ccf 0.391, β 0.1181, p 0.0); driver zc -3.22 → expected -0.792%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → kospi: leads 1d (ccf 0.381, β 0.7255, p 0.0); driver zc -1.93 → expected -2.004%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → usd_brl: leads 1d (ccf -0.376, β -0.2492, p 0.0); driver zc -1.93 → expected 0.688%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.368, β 0.881, p 0.0); driver zc -2.9 → expected -3.259%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.367, β -0.0936, p 0.0); driver zc 2.72 → expected -0.421%. Type hit-rate 0.821 (n=2070).
- **SETUP** vix → kospi: leads 1d (ccf -0.357, β -0.0939, p 0.0); driver zc 2.1 → expected -2.459%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.355, β 0.077, p 0.0); driver zc -4.36 → expected -1.079%. Type hit-rate 0.821 (n=2070).
- **SETUP** dyn_gs → kospi: leads 1d (ccf 0.351, β 0.4407, p 0.0); driver zc -3.22 → expected -2.955%. Type hit-rate 0.821 (n=2070).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.33, β 0.0752, p 0.0); driver zc -1.66 → expected -0.46%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.318, β 0.3554, p 2e-05); driver zc -1.93 → expected -0.981%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.284, β 0.2448, p 0.0); driver zc -1.93 → expected -0.676%. Type hit-rate 0.821 (n=2070).
- **SETUP** russell_2000 → hang_seng: leads 1d (ccf 0.277, β 0.2636, p 0.0); driver zc -1.93 → expected -0.728%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.275, β 0.316, p 0.0); driver zc -2.9 → expected -1.169%. Type hit-rate 0.821 (n=2070).
- **SETUP** dax → asx_200: leads 1d (ccf 0.265, β 0.1935, p 0.00412); driver zc -2.24 → expected -0.502%. Type hit-rate 0.821 (n=2070).
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.265, β 0.2037, p 0.00777); driver zc -2.74 → expected -0.573%. Type hit-rate 0.821 (n=2070).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.262, β 0.2151, p 1e-05); driver zc -3.14 → expected -1.207%. Type hit-rate 0.821 (n=2070).
- **SETUP** sp500 → hang_seng: leads 1d (ccf 0.26, β 0.3203, p 0.0); driver zc -2.9 → expected -1.185%. Type hit-rate 0.821 (n=2070).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.257, β -0.029, p 0.00029); driver zc 2.1 → expected -0.759%. Type hit-rate 0.821 (n=2070).
- Track record · residual_reversion: hit-rate **0.508** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2070) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 8.16] cross-asset · 6 series ↓
- dyn_gs [EQUITIES]: last 823.79, z20 -2.14, zc -3.22, resid-z -0.65 [priced], 1d 4.19%, |z20|=2.14
- dyn_ms [EQUITIES]: last 172.65, z20 -2.03, zc -2.51, resid-z 0.74 [priced], 1d 4.21%, |z20|=2.03
- dow_jones [INDICES]: last 49599.89, z20 -1.68, zc -1.48, resid-z 1.61 [unexplained], 1d 3.02%, |z20|=1.68
- russell_2000 [INDICES]: last 2668.93, z20 -1.55, zc -1.93, resid-z 0.42 [priced], 1d 3.38%, |z20|=1.55
- vix [INDICES]: last 26.61, z20 1.01, zc 2.10, resid-z n/a [moved], 1d -25.86%, 1-session move -25.86% ≥ 15.0%; 1y-pct=95
- dyn_nvda [EQUITIES]: last 165.18, z20 -0.61, zc -4.36, resid-z -2.60 [unexplained], 1d 31.59%, 1y-pct=3
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.774 vs dyn_gs, historically leads by 3d
- Source: Asian stocks rally as Huang's Nvidia return revives AI trade — ET Markets, 2026-11-24. https://economictimes.indiatimes.com/markets/us-stocks/news/asian-stocks-rally-as-huangs-nvidia-return-revives-ai-trade/articleshow/136117829.cms
- Source: Wall Street soars on Huang's return to Nvidia, Treasury yields rise — ET Markets, 2026-11-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-wall-street-soars-on-huangs-return-to-nvidia-treasury-yields-rise/articleshow/136116751.cms
- Source: US stocks rally as Jensen Huang returns, Nvidia shares surge 31% — BusinessLine Mkts, 2026-11-24. https://www.thehindubusinessline.com/markets/us-stocks-rally-as-jensen-huang-returns-nvidia-shares-surge-31/article71736372.ece
- Historical analogues: 2026-05-22 (d=0.49), 2025-08-28 (d=0.79), 2025-08-14 (d=0.81)

### [RED 5.19] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 84.98, z20 1.88, zc n/a, resid-z n/a [quiet], 1d 0.01%, |z20|=1.88; 1y-pct=99
- comex_silver [COMMODITIES]: last 42.92, z20 -1.79, zc -0.01, resid-z 0.20 [quiet], 1d -0.03%, |z20|=1.79; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3647.00, z20 -1.69, zc -0.01, resid-z -3.12 [unexplained], 1d -0.03%, |z20|=1.69; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.588 via comex_gold, z -0.51, quiet); dyn_karurvysya_ns (rho 0.509 via comex_gold, z 1.03, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.547 vs comex_silver, historically leads by 4d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.533 vs gold_silver_ratio, historically leads by 5d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.522 vs comex_silver, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.588, z -0.51); dyn_karurvysya_ns (rho 0.509, z 1.03)
- Source: Gold Rebounds as Huang’s Return to Nvidia Revives Risk Appetite — Mint Markets, 2026-11-23. https://www.livemint.com/market/gold-rebounds-as-huang-s-return-to-nvidia-revives-risk-appetite-11795469022718.html
- Source: Gold rises as bargain hunters step in after steep weekly drop — Mint Markets, 2026-11-23. https://www.livemint.com/market/gold-rises-as-bargain-hunters-step-in-after-steep-weekly-drop-11795461578266.html
- Source: SPOT GOLD EXTENDS GAINS, UP NEARLY 4% TO $3,673.36/OZ — DeItaone, 2026-11-23. https://t.me/walter_bloomberg/39037
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 4.84] rates · 2 series ↑
- hy_oas [RATES]: last 3.76, z20 4.01, zc 3.00, resid-z 0.45 [priced], 1d 6.82%, |z20|=4.01; 1y-pct=100
- ig_oas [RATES]: last 0.98, z20 3.23, zc 2.78, resid-z 0.71 [priced], 1d 4.26%, |z20|=3.23; 1y-pct=100
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.46 via ig_oas, z -1.13, reacted); nifty_it (rho 0.385 via ig_oas, z -0.3, quiet)
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.696 vs hy_oas, historically leads by 5d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.516 vs hy_oas, historically leads by 2d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.537 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.46, z -1.13); nifty_it (rho 0.385, z -0.3)
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [RED 4.76] dxy ↑
- dxy [FX]: last 104.25, z20 1.76, zc 0.01, resid-z -0.35 [quiet], 1d 0.00%, 20d range extreme; |z20|=1.76; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho -0.35 via dxy, z 1.68, reacted)
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.561 vs dxy, historically leads by 1d
- **India receivers**: dyn_indusindbk_bo (rho -0.35, z 1.68)
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 4.5] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 382.00, z20 -2.50, zc -0.29, resid-z -0.11 [quiet], 1d -2.05%, |z20|=2.50
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India unit Mahanadi's IPO fully subscribed on final day, led by institutional investors — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/coal-india-unit-mahanadis-ipo-fully-subscribed-on-final-day-led-by-institutional-investors/article71734460.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

### [AMBER 4.36] cross-asset · 2 series ↓
- btc_usd [CRYPTO]: last 60020.25, z20 -1.52, zc -1.66, resid-z 0.15 [priced], 1d -6.11%, |z20|=1.52; 1y-pct=2
- dyn_coin [EQUITIES]: last 108.82, z20 -1.52, zc -1.38, resid-z 1.63 [unexplained], 1d 6.72%, 1y-pct=0
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.15).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.628 vs btc_usd, historically leads by 5d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.546 vs btc_usd
- Source: BLACKROCK'S BITCOIN ETF POSTS RECORD $541 MILLION DAILY OUTFLOW BlackRock's iShares Bitcoin Trust recorded its largest-ever daily outflow on Thursday, with investors withdrawing $541 million, according to DWF Labs. Across U.S. Bitcoin ETFs, investors have withdrawn nearly $4 billion in November, put — DeItaone, 2026-11-23. https://t.me/walter_bloomberg/39021
- Source: Crypto investment amid fall: As Bitcoin hovers near $60K levels, experts answer if investors can expect recovery — Mint Markets, 2026-11-23. https://www.livemint.com/market/cryptocurrency/crypto-investment-amid-fall-as-bitcoin-hovers-near-60000-levels-experts-answer-if-investors-can-expect-recovery-markets-11795426061415.html
- Source: TCS vs Infosys vs Wipro shares: Despite global AI bloodbath, why are Indian IT stocks rising? Experts decode — Mint Markets, 2026-11-23. https://www.livemint.com/market/stock-market-news/tcs-vs-infosys-vs-wipro-shares-despite-global-ai-bloodbath-why-are-indian-it-stocks-rising-experts-decode-11795416602297.html
- Historical analogues: 2026-05-22 (d=0.15), 2026-04-02 (d=0.16), 2025-10-22 (d=0.28)

### [AMBER 4.15] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 707.90, z20 2.15, zc 1.33, resid-z 1.01 [quiet], 1d -2.75%, |z20|=2.15
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.568 via dyn_tatatech_ns, z 1.68, reacted); dyn_jiofin_bo (rho 0.504 via dyn_tatatech_ns, z -0.01, quiet); nifty_midcap_100 (rho 0.492 via dyn_tatatech_ns, z 0.83, quiet); dyn_tataelxsi_ns (rho 0.492 via dyn_tatatech_ns, z 0.54, quiet); dyn_indianb_ns (rho 0.457 via dyn_tatatech_ns, z 0.88, quiet)
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.504 vs dyn_tatatech_ns, historically leads by 1d
- **India receivers**: dyn_indusindbk_bo (rho 0.568, z 1.68); dyn_jiofin_bo (rho 0.504, z -0.01); nifty_midcap_100 (rho 0.492, z 0.83); dyn_tataelxsi_ns (rho 0.492, z 0.54)
- Source: Tata Steel dips 7% as APL Apollo plunge on ₹28,000 cr deal; Hindalco under pressure — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/tata-steel-dips-7-as-apl-apollo-tumbles-on-28000-crore-deal-hindalco-also-under-pressure/article71733581.ece
- Source: Tata Steel shares fall 5% as investors weigh  ₹32,000 cr APL Apollo acquisition plan | Should you buy? Check key levels — Mint Markets, 2026-11-23. https://www.livemint.com/market/stock-market-news/tata-steel-shares-fall-5-as-investors-weigh-rs-32-000-cr-apl-apollo-acquisition-plan-should-you-buy-check-key-levels-11795406091656.html
- Source: Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, Waaree Energies, Premier Explosives, Maruti Suzuki, Texmaco Rail, RVNL, Ashoka Buildcon — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/stocks-to-watch-nov-23-tata-steel-apl-apollo-tubes-indusind-bank-nse-adani-energy-waaree-energies-premier-explosives-maruti-suzuki-texmaco-rail-rvnl-ashoka-buildcon/article71733190.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 3.92] natgas ↑
- natgas [COMMODITIES]: last 3.54, z20 1.92, zc 0.00, resid-z 1.34 [quiet], 1d 0.00%, |z20|=1.92
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: South Korea Asks Qatar for Priority LNG Once Hormuz Reopens — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/South-Korea-Asks-Qatar-for-Priority-LNG-Once-Hormuz-Reopens.html
- Source: European Natural Gas Prices Surge 8.6% as Cold Snap Looms — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/European-Natural-Gas-Prices-Surge-86-as-Cold-Snap-Looms.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
usd_inr ↓ (3.9), comex_copper ↓ (3.77), dyn_tgt ↑ (3.6), wti ↓ (3.5), tips_10y_real ↑ (3.42), dyn_tech ↑ (3.36), fx · 2 series ↓ (3.08), dyn_lth ↑ (2.92), usd_mxn ↑ (2.74), dyn_4417_t ↑ (2.62), dyn_crwv ↓ (2.56), eur_inr ↓ (2.07)

## India macro
- nifty_50: 25366.4004 (1d -1.68%, z20 0.97, flag none)
- nifty_midcap_100: 61403.8516 (1d -1.00%, z20 0.83, flag none)
- usd_inr: 92.9000 (1d 0.24%, z20 -1.90, flag amber)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4207 (1d 0.70%, z20 -1.13, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 68.6 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.3 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 63.9 — "Nestle India Share Price Highlights: Nestle India Stock Price History"
- NVDA (NVIDIA Corporation) score 53.4 — "NVDA - *NVIDIA BOARD REINSTATES JENSEN HUANG AS PRESIDENT AND CEO"
- INDIANB.NS (INDIAN BANK) score 49.3 — "Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens"
- BAC (Bank of America Corporation) score 38.4 — "Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens"
- HDB (HDFC Bank Limited) score 33.5 — "Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.1 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- OHI (Omega Healthcare Investors, In) score 32.0 — "BLACKROCK'S BITCOIN ETF POSTS RECORD $541 MILLION DAILY OUTFLOW BlackRock's iShares Bitcoi"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 31.9 — "Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens"
- IDBI.NS (IDBI BANK LIMITED) score 31.9 — "Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.9 — "Banks sell-off ends four-week rally; Nifty slumps 1.75%, Rupee weakens"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.1 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- TECH (Bio-Techne Corp) score 30.1 — "Tech Mahindra Share Price Highlights: Tech Mahindra Stock Price History"
- TGT (Target Corporation) score 29.0 — "SPCX - JEFFERIES INITIATES SPACEX AT BUY WITH $210 TARGET, SEES MASSIVE AI GROWTH POTENTIA"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.4 — "Japan’s Electricity Prices Surge to 2022 High as Cold Weather Arrives"
- CHKP (Check Point Software Technolog) score 20.1 — "Ashish Kacholia portfolio stock already up 36% in 2026, SBI Securities sees 15% more retur"
- COIN (Coinbase Global, Inc.) score 19.8 — "Global crude oil prices may fall to $70 by end-2027 as supply surplus looms"
- BLLN (BillionToOne, Inc.) score 19.2 — "BLACKROCK'S BITCOIN ETF POSTS RECORD $541 MILLION DAILY OUTFLOW BlackRock's iShares Bitcoi"
- 301077.SZ (CHINASTARS) score 16.5 — "Peterson: Here’s what Bessent’s about-face on Jensen Huang reveals about Trump and China"
- LTH (Life Time Group Holdings, Inc.) score 14.1 — "Mahanadi Coalfields IPO subscribed 1.52 times on final day"
- BOND (PIMCO Active Bond Exchange-Tra) score 13.4 — "India bonds give up marginal opening gains as profit booking takes over"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 11.2 — "Climate Finance Dispute Derails COP31 Negotiations"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 10.7 — "Jensen Huang is NVIDIA CEO again! What does it mean for Indian IT and tech shares? Experts"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.5 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.5 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.4 — "Climate Finance Dispute Derails COP31 Negotiations"
- JIOFIN.BO (Jio Financial Services Limited) score 9.4 — "Taiwan Meets With TSMC, Financial Firms in Bid to Calm Markets"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.2 — "NVDA - NVIDIA SHARES EXTEND PREMARKET GAINS, LAST UP 27%"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "Amazon may have just found a ‘cheap’ way to get a lot more out of its chips"
- META (Meta) score 7.7 — "The Energy Transition Needs More Metals but Less Extraction"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.3 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 4.0 — "Nasdaq surges 6%, Dow soars 1,400 pts as markets rebound on Huang’s return: Stock Market L"
- MS (Morgan Stanley) score 3.7 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- GS (Goldman Sachs Group, Inc. (The) score 3.4 — "Rupee retreats, Goldman calls it a 'port of stability' in AI storm"
- CRWV (CoreWeave, Inc.) score 2.8 — "Oracle and CoreWeave stocks stage big gains as investors bet the AI cash will keep flowing"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.8 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- RS (Reliance, Inc.) score 1.4 — "Reliance Industries shares: After 13% surge in 1 month, JPMorgan sees another 23% upside i"
- ETERNAL.NS (ETERNAL LIMITED) score 1.3 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.2 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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