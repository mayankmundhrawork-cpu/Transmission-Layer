# Transmission Layer — board brief · 2026-11-23 14:31Z

data as of **2026-11-23** · 97 series · 8 red / 41 amber · 8 events surfaced (34 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.887, 6d in regime; vol-pct 0.974, breadth-off 0.8, Markov P(high-vol) 1.0)
- [WEAK] **safe_haven_gold** — corr20 -0.19, corr60 -0.27, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.18, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.16, corr60 0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.06, corr60 -0.14, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.34, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 1.632545460550361e-05)
- **SETUP** dyn_bond → usd_jpy: leads 1d (ccf -0.405, β -0.7151, p 0.0); driver zc 1.9 → expected -0.504%. Type hit-rate 0.824 (n=2086).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.367, β -0.0936, p 0.0); driver zc 2.72 → expected -0.421%. Type hit-rate 0.824 (n=2086).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.334, β 0.0765, p 0.0); driver zc 2.18 → expected 0.488%. Type hit-rate 0.824 (n=2086).
- **SETUP** btc_usd → taiwan_weighted: leads 1d (ccf 0.329, β 0.2069, p 0.0); driver zc 2.18 → expected 1.32%. Type hit-rate 0.824 (n=2086).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.323, β -0.0765, p 0.0); driver zc 2.18 → expected -0.488%. Type hit-rate 0.824 (n=2086).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.318, β 0.3554, p 2e-05); driver zc -1.93 → expected -0.981%. Type hit-rate 0.824 (n=2086).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.312, β 0.0957, p 0.0); driver zc 2.18 → expected 0.611%. Type hit-rate 0.824 (n=2086).
- **SETUP** eth_usd → usd_mxn: leads 1d (ccf -0.285, β -0.0431, p 0.0); driver zc 2.01 → expected -0.36%. Type hit-rate 0.824 (n=2086).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.284, β 0.2448, p 0.0); driver zc -1.93 → expected -0.676%. Type hit-rate 0.824 (n=2086).
- **SETUP** eth_usd → aud_usd: leads 1d (ccf 0.279, β 0.0407, p 0.0); driver zc 2.01 → expected 0.34%. Type hit-rate 0.824 (n=2086).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.275, β 0.316, p 0.0); driver zc -2.9 → expected -1.169%. Type hit-rate 0.824 (n=2086).
- **SETUP** aud_usd → usd_cny: leads 1d (ccf -0.272, β -0.0811, p 0.0); driver zc -1.65 → expected 0.068%. Type hit-rate 0.824 (n=2086).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.262, β 0.2151, p 1e-05); driver zc -3.14 → expected -1.207%. Type hit-rate 0.824 (n=2086).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.257, β -0.029, p 0.00029); driver zc 2.1 → expected -0.759%. Type hit-rate 0.824 (n=2086).
- Track record · residual_reversion: hit-rate **0.508** (n=1151) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2086) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.12] cross-asset · 5 series ↓
- russell_2000 [INDICES]: last 2581.79, z20 -3.80, zc -1.93, resid-z 0.42 [priced], 1d -2.76%, |z20|=3.80
- dyn_rs [EQUITIES]: last 398.46, z20 -2.89, zc -2.43, resid-z -0.26 [moved], 1d -3.94%, |z20|=2.89
- dow_jones [INDICES]: last 49477.37, z20 -1.78, zc -1.48, resid-z 1.61 [unexplained], 1d 2.76%, |z20|=1.78
- vix [INDICES]: last 27.48, z20 1.19, zc 2.10, resid-z n/a [moved], 1d -23.43%, 1-session move -23.43% ≥ 15.0%; 1y-pct=97
- dyn_nvda [EQUITIES]: last 164.18, z20 -0.65, zc -4.36, resid-z 0.73 [priced], 1d 30.79%, 1y-pct=2
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-24 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.483 via dyn_rs, z 0.84, quiet); dyn_indusindbk_bo (rho -0.476 via dyn_rs, z 1.68, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.764 vs russell_2000
- Watch next: eth_usd (inverse) — not yet - watch; rho -0.539 vs vix, historically leads by 5d
- **India receivers**: dyn_bajfinance_ns (rho -0.483, z 0.84); dyn_indusindbk_bo (rho -0.476, z 1.68)
- Source: Nvidia brings back Jensen Huang as CEO, stock rallies 31% — Mint Markets, 2026-11-23. https://www.livemint.com/market/stock-market-news/nvidia-brings-back-jensen-huang-as-ceo-ai-chipmaker-stock-rallies-31-11795443628972.html
- Source: Nvidia stock soars as Jensen Huang returns as CEO — MarketWatch Top, 2026-11-23. https://www.marketwatch.com/story/nvidia-stock-bounces-as-trump-administration-pushes-for-rehiring-of-jensen-huang-08057c29?mod=mw_rss_topstories
- Source: Nasdaq futures soar 6% as Nvidia reinstates Jensen Huang; Nvidia surges over 26%: Stock Market Live Updates — ET Markets, 2026-11-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/stock-market-live-updates-dow-jones-nasdaq-sp-500-nvidia-meta-anthropic-amd-micron-tesla-ai-chip-earnings-fed-rate-treasury-yield-news-23rd-november-2026/liveblog/136104474.cms
- Historical analogues: 2025-10-24 (d=0.46), 2026-05-22 (d=0.54), 2025-08-25 (d=0.7)

### [RED 7.34] usd_inr ↓
- usd_inr [FX]: last 92.90, z20 -2.34, zc -0.43, resid-z 0.26 [quiet], 1d -0.42%, 20d range extreme; |z20|=2.34; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.446 via usd_inr, z -0.3, quiet); dyn_indianb_ns (rho -0.445 via usd_inr, z 0.88, quiet); dyn_havells_ns (rho -0.435 via usd_inr, z 1.15, reacted); dyn_tataelxsi_ns (rho -0.384 via usd_inr, z 0.54, quiet); dyn_bajfinance_ns (rho -0.362 via usd_inr, z 0.84, quiet)
- **India receivers**: nifty_it (rho -0.446, z -0.3); dyn_indianb_ns (rho -0.445, z 0.88); dyn_havells_ns (rho -0.435, z 1.15); dyn_tataelxsi_ns (rho -0.384, z 0.54)
- Source: Rupee reversal, debt supply drag India bonds in holiday-shortened week — ET Markets, 2026-11-23. https://economictimes.indiatimes.com/markets/bonds/rupee-reversal-debt-supply-drag-india-bonds-in-holiday-shortened-week/articleshow/136103987.cms
- Source: Rupee snaps 5-day rally; tumbles 30 paise to settle at 92.92 against US dollar — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/forex/rupee-snaps-5-day-rally-tumbles-30-paise-to-settle-at-9292-against-us-dollar/article71734316.ece
- Source: Rupee retreats with stocks as rally takes a breather, positive bias lingers — ET Markets, 2026-11-23. https://economictimes.indiatimes.com/markets/forex/rupee-retreats-with-stocks-as-rally-takes-a-breather-positive-bias-lingers/articleshow/136098391.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 7.19] commodities · 2 series ↓
- wti [COMMODITIES]: last 82.06, z20 -1.36, zc 0.37, resid-z -1.35 [quiet], 1d -2.29%, 1-session move -2.29% ≥ 1.5%
- brent [COMMODITIES]: last 88.19, z20 -1.29, zc 0.28, resid-z -1.63 [unexplained], 1d -4.73%, 1-session move -4.73% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.454 via wti, z 1.28, reacted)
- **India receivers**: nifty_fmcg (rho -0.454, z 1.28)
- Source: Brent Drops Below $90 as Wall Street Splits on 2027 Oil Outlook — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/Brent-Drops-Below-90-as-Wall-Street-Splits-on-2027-Oil-Outlook.html
- Source: Libya’s Oil Output Plunges as Armed Groups Shut Key Pipelines — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/Libyas-Oil-Output-Plunges-as-Armed-Groups-Shut-Key-Pipelines.html
- Source: Oil Prices Slide as AI Bubble Fears Rattle Global Markets — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Slide-as-AI-Bubble-Fears-Rattle-Global-Markets.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 5.19] cross-asset · 3 series ↓
- comex_silver [COMMODITIES]: last 43.53, z20 -1.87, zc -2.52, resid-z 0.20 [priced], 1d 6.07%, |z20|=1.87; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 84.30, z20 1.87, zc n/a, resid-z n/a [quiet], 1d -1.60%, |z20|=1.87; 1y-pct=99
- comex_gold [COMMODITIES]: last 3669.20, z20 -1.79, zc -2.37, resid-z -0.94 [priced], 1d 4.38%, |z20|=1.79; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.55 via comex_gold, z -0.51, quiet); dyn_karurvysya_ns (rho 0.497 via comex_gold, z 1.03, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.55 vs comex_gold, historically leads by 4d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.512 vs gold_silver_ratio, historically leads by 5d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.508 vs comex_silver, historically leads by 5d
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.501 vs comex_silver
- **India receivers**: dyn_muthootfin_ns (rho 0.55, z -0.51); dyn_karurvysya_ns (rho 0.497, z 1.03)
- Source: Exits from gold ETFs top $100 billion for 2026, even as inflows remain net positive — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/gold/exits-from-gold-etfs-top-100-billion-for-2026-even-as-inflows-remain-net-positive/article71734916.ece
- Source: Gold imports into India decline 40% in April-October: CTI — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/economy/gold-imports-into-india-decline-40-in-april-october-cti/article71734145.ece
- Source: Fund managers look to raise gold, silver exposure as price correction revives interest — Mint Markets, 2026-11-23. https://www.livemint.com/market/gold-silver-prices-fall-mutual-funds-increase-precious-metal-allocations-11795408683158.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 4.89] dxy ↑
- dxy [FX]: last 104.13, z20 1.89, zc -0.25, resid-z -0.29 [quiet], 1d 0.31%, 20d range extreme; |z20|=1.89; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.542 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 4.5] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 382.00, z20 -2.50, zc -0.29, resid-z -0.11 [quiet], 1d -2.05%, |z20|=2.50
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India unit Mahanadi's IPO fully subscribed on final day, led by institutional investors — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/coal-india-unit-mahanadis-ipo-fully-subscribed-on-final-day-led-by-institutional-investors/article71734460.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

### [AMBER 4.15] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 707.90, z20 2.15, zc 1.33, resid-z 1.01 [quiet], 1d -2.75%, |z20|=2.15
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.565 via dyn_tatatech_ns, z 1.68, reacted); dyn_jiofin_bo (rho 0.508 via dyn_tatatech_ns, z -0.01, quiet); nifty_midcap_100 (rho 0.495 via dyn_tatatech_ns, z 0.83, quiet); dyn_tataelxsi_ns (rho 0.495 via dyn_tatatech_ns, z 0.54, quiet); dyn_indianb_ns (rho 0.459 via dyn_tatatech_ns, z 0.88, quiet)
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.508 vs dyn_tatatech_ns, historically leads by 1d
- **India receivers**: dyn_indusindbk_bo (rho 0.565, z 1.68); dyn_jiofin_bo (rho 0.508, z -0.01); nifty_midcap_100 (rho 0.495, z 0.83); dyn_tataelxsi_ns (rho 0.495, z 0.54)
- Source: Tata Steel dips 7% as APL Apollo plunge on ₹28,000 cr deal; Hindalco under pressure — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/tata-steel-dips-7-as-apl-apollo-tumbles-on-28000-crore-deal-hindalco-also-under-pressure/article71733581.ece
- Source: Tata Steel shares fall 5% as investors weigh  ₹32,000 cr APL Apollo acquisition plan | Should you buy? Check key levels — Mint Markets, 2026-11-23. https://www.livemint.com/market/stock-market-news/tata-steel-shares-fall-5-as-investors-weigh-rs-32-000-cr-apl-apollo-acquisition-plan-should-you-buy-check-key-levels-11795406091656.html
- Source: Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, Waaree Energies, Premier Explosives, Maruti Suzuki, Texmaco Rail, RVNL, Ashoka Buildcon — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/stocks-to-watch-nov-23-tata-steel-apl-apollo-tubes-indusind-bank-nse-adani-energy-waaree-energies-premier-explosives-maruti-suzuki-texmaco-rail-rvnl-ashoka-buildcon/article71733190.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.03] natgas ↑
- natgas [COMMODITIES]: last 3.53, z20 2.03, zc 1.16, resid-z 1.34 [quiet], 1d 3.37%, |z20|=2.03
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: South Korea Asks Qatar for Priority LNG Once Hormuz Reopens — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/South-Korea-Asks-Qatar-for-Priority-LNG-Once-Hormuz-Reopens.html
- Source: European Natural Gas Prices Surge 8.6% as Cold Snap Looms — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/European-Natural-Gas-Prices-Surge-86-as-Cold-Snap-Looms.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
dyn_kaynes_ns ↓ (4.03), dyn_cochinship_ns ↓ (3.78), indices · 3 series ↓ (3.76), comex_copper ↓ (3.59), dyn_coin ↓ (3.5), indices · 3 series ↓ (3.43), indices · 2 series ↓ (3.3), dyn_301077_sz ↓ (3.28), fx · 2 series ↓ (3.16), dyn_tgt ↑ (2.94), usd_mxn ↑ (2.83), rates · 2 series ↑ (2.72)

## India macro
- nifty_50: 25366.4004 (1d -1.68%, z20 0.97, flag none)
- nifty_midcap_100: 61403.8516 (1d -1.00%, z20 0.83, flag none)
- usd_inr: 92.9000 (1d -0.42%, z20 -2.34, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4207 (1d 0.70%, z20 -1.13, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 71.6 — "Indian markets nearing end of consolidation phase, financials and consumption look attract"
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.9 — "Indian markets nearing end of consolidation phase, financials and consumption look attract"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 67.5 — "Indian markets nearing end of consolidation phase, financials and consumption look attract"
- INDIANB.NS (INDIAN BANK) score 53.3 — "Indian markets nearing end of consolidation phase, financials and consumption look attract"
- BAC (Bank of America Corporation) score 39.9 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- HDB (HDFC Bank Limited) score 36.6 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.9 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- IDBI.NS (IDBI BANK LIMITED) score 34.9 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.9 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- NVDA (NVIDIA Corporation) score 32.0 — "Trump wants Jensen Huang back at Nvidia. What will it take to stop the tech selloff?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 31.7 — "Tech outages are fueling a new doomsday economy"
- OHI (Omega Healthcare Investors, In) score 31.5 — "Tata Steel shares fall 5% as investors weigh  ₹32,000 cr APL Apollo acquisition plan | Sho"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 29.4 — "Tech outages are fueling a new doomsday economy"
- TECH (Bio-Techne Corp) score 29.4 — "Tech outages are fueling a new doomsday economy"
- TGT (Target Corporation) score 29.3 — "98% up in 5 years! APL Apollo shares crash 15% today; here's why | Check stock returns, ta"
- COIN (Coinbase Global, Inc.) score 22.3 — "Global crude oil prices may fall to $70 by end-2027 as supply surplus looms"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.8 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- BLLN (BillionToOne, Inc.) score 19.4 — "The $25 Billion Problem Facing Australia’s Hydropower Revolution"
- CHKP (Check Point Software Technolog) score 19.2 — "Crude Check: Forms a base"
- 301077.SZ (CHINASTARS) score 17.4 — "Why a slow-paced show about broken friendships is China’s antidote to AI fatigue"
- BOND (PIMCO Active Bond Exchange-Tra) score 15.1 — "India bonds give up marginal opening gains as profit booking takes over"
- LTH (Life Time Group Holdings, Inc.) score 14.8 — "IPO Street set for year-end revival; 29 firms eye ₹42,000 crore as sentiment improves"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.9 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.9 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 11.5 — "Shriram Finance set to join Sensex as Trent exits on December 21"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.0 — "MCX vs NSE vs BSE shares comparison: Which exchange stock to buy for a better return? Expe"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.4 — "Shriram Finance set to join Sensex as Trent exits on December 21"
- JIOFIN.BO (Jio Financial Services Limited) score 9.4 — "Indian markets nearing end of consolidation phase, financials and consumption look attract"
- META (Meta) score 7.5 — "Ahead of FY28 budget, aluminium product makers seek duty-free imports for primary metal"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.1 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.0 — "Mahindra Last Mile Mobility eyes IPO in 18 months; plans expansion into new products: Chai"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.0 — "A 66-year-old nurse faces retirement with just $500 saved. Who’s to blame?"
- MS (Morgan Stanley) score 4.2 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- GS (Goldman Sachs Group, Inc. (The) score 3.8 — "Rupee retreats, Goldman calls it a 'port of stability' in AI storm"
- SCHD (Schwab US Dividend Equity ETF) score 3.3 — "Smallcap dividend stars: 5 stocks under  ₹100 with high dividend yield - Jagran Prakashan,"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.1 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- CRWV (CoreWeave, Inc.) score 2.0 — "TECH STOCKS SLIDE AS AI SELL-OFF ACCELERATES Technology and AI-linked stocks face broad se"
- RS (Reliance, Inc.) score 1.6 — "Reliance Industries shares: After 13% surge in 1 month, JPMorgan sees another 23% upside i"
- ETERNAL.NS (ETERNAL LIMITED) score 1.4 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.3 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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