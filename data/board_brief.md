# Transmission Layer — board brief · 2026-09-16 09:17Z

data as of **2026-09-16** · 97 series · 12 red / 45 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.692, 5d in regime; vol-pct 0.55, breadth-off 0.833, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.55, corr60 -0.32, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.16, corr60 0.32, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.11, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.89, corr60 -0.84, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.04, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-07-23. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.17, corr60 0.16, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0013742758758317208)
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.26, β 0.0315, p 0.00024); driver zc -1.92 → expected -0.318%. Type hit-rate 0.823 (n=2057).
- Track record · residual_reversion: hit-rate **0.496** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2057) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.06] cross-asset · 16 series ↓
- tips_10y_real [RATES]: last 2.60, z20 2.73, zc 0.00, resid-z -0.81 [quiet], 1d 0.00%, |z20|=2.73; 1y-pct=99
- dyn_vt [EQUITIES]: last 158.02, z20 -2.66, zc -0.55, resid-z -0.67 [quiet], 1d -0.45%, |z20|=2.66
- ust_2y [RATES]: last 4.65, z20 2.64, zc 0.33, resid-z -0.45 [quiet], 1d 0.43%, |z20|=2.64; 1y-pct=100
- dyn_ms [EQUITIES]: last 206.23, z20 -2.60, zc -0.09, resid-z -1.98 [unexplained], 1d -0.17%, |z20|=2.60
- ust_10y [RATES]: last 4.97, z20 2.55, zc 0.20, resid-z -0.34 [quiet], 1d 0.20%, |z20|=2.55; 1y-pct=100
- sp500 [INDICES]: last 7585.51, z20 -2.24, zc -0.59, resid-z 0.30 [quiet], 1d -0.45%, |z20|=2.24
- dyn_bond [EQUITIES]: last 88.65, z20 -2.23, zc -0.33, resid-z -0.01 [quiet], 1d -0.11%, |z20|=2.23; 1y-pct=0
- russell_2000 [INDICES]: last 2869.79, z20 -2.20, zc -0.66, resid-z -0.52 [quiet], 1d -0.78%, |z20|=2.20
- dow_jones [INDICES]: last 52092.45, z20 -2.19, zc -0.78, resid-z -0.26 [quiet], 1d -0.63%, |z20|=2.19
- wti [COMMODITIES]: last 104.78, z20 2.01, zc -0.31, resid-z 1.23 [quiet], 1d -0.99%, |z20|=2.01; 1y-pct=96
- brent [COMMODITIES]: last 108.24, z20 1.94, zc -0.16, resid-z 0.66 [quiet], 1d -0.47%, |z20|=1.94; co-occur[inr_oil] suppressed: channel WEAK
- nasdaq_100 [INDICES]: last 28937.75, z20 -1.87, zc -0.62, resid-z 0.09 [quiet], 1d -0.65%, |z20|=1.87
- stoxx_50 [INDICES]: last 6254.65, z20 -1.87, zc 0.33, resid-z -0.16 [quiet], 1d 0.29%, |z20|=1.87
- ust_30y [RATES]: last 5.34, z20 1.73, zc -0.24, resid-z -0.58 [quiet], 1d -0.19%, |z20|=1.73; 1y-pct=99
- cac_40 [INDICES]: last 8103.42, z20 -1.66, zc 0.19, resid-z -0.09 [quiet], 1d 0.16%, |z20|=1.66
- dax [INDICES]: last 25428.88, z20 -1.63, zc 0.12, resid-z 0.22 [quiet], 1d 0.10%, |z20|=1.63
- **Mechanism**: cross-asset · 16 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.477 via dax, z -2.82, reacted); midcap_largecap_ratio (rho -0.4 via ust_2y, z -1.53, reacted)
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.564 vs sp500, historically leads by 1d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.506 vs cac_40, historically leads by 5d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.631 vs dyn_vt
- **India receivers**: nifty_midcap_100 (rho 0.477, z -2.82); midcap_largecap_ratio (rho -0.4, z -1.53)
- Source: What history says about longer-term bond yields after the first Fed hike — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/what-history-says-about-longer-term-bond-yields-after-the-first-fed-hike-53eaae9f?mod=mw_rss_topstories
- Source: Japan’s Oil Import Bill Soars 59% as Trade Deficit Deepens — OilPrice, 2026-09-16. https://oilprice.com/Latest-Energy-News/World-News/Japans-Oil-Import-Bill-Soars-59-as-Trade-Deficit-Deepens.html
- Source: Global Market: Japan bond yields rise as inflation concerns build ahead of Fed decision — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-bond-yields-rise-as-inflation-concerns-build-ahead-of-fed-decision/articleshow/134280079.cms

### [RED 6.49] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 60979.55, z20 -2.82, zc 0.26, resid-z -0.54 [quiet], 1d 0.17%, |z20|=2.82
- india_vix [INDICES]: last 13.15, z20 2.81, zc -0.36, resid-z n/a [quiet], 1d -2.05%, |z20|=2.81
- dyn_jiofin_bo [EQUITIES]: last 225.85, z20 -2.25, zc -0.05, resid-z -0.94 [quiet], 1d -0.07%, |z20|=2.25; 1y-pct=0
- nifty_50 [INDICES]: last 23237.60, z20 -2.05, zc 0.94, resid-z -0.80 [quiet], 1d 0.51%, |z20|=2.05
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.618 via nifty_50, z -0.77, quiet); dyn_indianb_ns (rho 0.561 via nifty_midcap_100, z -1.66, reacted); nifty_it (rho 0.521 via nifty_50, z -1.71, reacted); dyn_techm_ns (rho 0.504 via nifty_50, z -0.97, quiet); midcap_largecap_ratio (rho -0.436 via nifty_50, z -1.53, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.618 vs nifty_50, historically leads by 3d
- Watch next: dyn_techm_ns (co-move) — not yet - watch; rho 0.504 vs nifty_50, historically leads by 3d
- **India receivers**: nifty_fmcg (rho 0.618, z -0.77); dyn_indianb_ns (rho 0.561, z -1.66); nifty_it (rho 0.521, z -1.71); dyn_techm_ns (rho 0.504, z -0.97)
- Source: Sensex today | Stock Market Live: Sensex rises 350 pts, Nifty crosses 23,200; IT drags while metals, FMCG shine ahead of Fed call — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-16th-september-2026/article71468722.ece
- Source: Sensex, Nifty hold morning gains at midday; IT drags as metals, FMCG shine ahead of Fed call — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/stock-markets/sensex-nifty-hold-morning-gains-at-midday-it-drags-as-metals-fmcg-shine-ahead-of-fed-call/article71471537.ece
- Source: Sensex rises 400 points, Nifty nears 23,250 as investors await Fed meeting outcome. What to expect? — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/sensex-rises-400-points-nifty-nears-23250-as-investors-await-fed-meeting-outcome-what-to-expect/articleshow/134279785.cms
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [AMBER 6.39] usd_inr ↑
- usd_inr [FX]: last 95.97, z20 1.39, zc 0.24, resid-z 0.23 [quiet], 1d 0.14%, 20d range extreme; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Rupee falls 3 paise to 95.91 against US dollar in early trade — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/forex/rupee-falls-3-paise-to-9591-against-us-dollar-in-early-trade/article71471039.ece
- Source: Rupee expected to stay under pressure with likely Fed rate hike adding to strain from high oil prices — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/forex/rupee-expected-to-stay-under-pressure-with-likely-fed-rate-hike-adding-to-strain-from-high-oil-prices/article71470982.ece
- Source: Rupee slumps 38 paise to close at 95.92 against US dollar — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/forex/rupee-slumps-38-paise-to-close-at-95-92-against-us-dollar/articleshow/134259296.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 5.27] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5430.00, z20 3.27, zc 0.52, resid-z 3.20 [unexplained], 1d 2.45%, |z20|=3.27; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Zee Entertainment shares surge 8% after 4-day losses; can it rise more? Experts decode — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/zee-entertainment-shares-surge-8-after-4-day-losses-can-it-rise-more-experts-decode-11789540738234.html
- Source: ITC shares edge higher after rise in select cigarette brands, experts see 10% rally in short term | Target, outlook — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/itc-shares-edge-higher-after-rise-in-select-cigarette-brands-experts-see-10-rally-in-short-term-target-outlook-11789536356887.html
- Source: From VBL, Power Grid to Paytm - 6 stocks experts recommend buying for the short term; do you own any? — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/from-vbl-power-grid-to-paytm-6-stocks-experts-recommend-buying-for-the-short-term-do-you-own-any-11789451473678.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 5.18] dyn_jef ↓
- dyn_jef [EQUITIES]: last 48.86, z20 -3.18, zc -0.90, resid-z -1.05 [quiet], 1d -2.48%, |z20|=3.18
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Solar Industries’ defence share may fall to 22-25% by FY30 after Omnia deal: Jefferies — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-defence-share-may-fall-to-22-25-by-fy30-after-omnia-deal-jefferies/articleshow/134280191.cms
- Source: Solar Industries shares plunge 17% in 2 days. Why Jefferies, Nuvama still see up to 46% upside — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-shares-plunge-17-in-2-days-why-jefferies-nuvama-still-see-up-to-46-upside/articleshow/134279133.cms
- Source: Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estimates after new UPI charges — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-jump-7-as-jefferies-other-brokerages-raise-target-prices-and-earnings-estimates-after-new-upi-charges/articleshow/134278132.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [RED 5.02] dyn_bac ↓
- dyn_bac [EQUITIES]: last 59.49, z20 -3.02, zc 0.01, resid-z -4.20 [unexplained], 1d 0.03%, |z20|=3.02
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho 0.384 via dyn_bac, z 0.33, quiet)
- **India receivers**: eur_inr (rho 0.384, z 0.33)
- Source: WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expects the Federal Reserve to raise rates in September, according to a WSJ survey. Most forecast 50 basis points of total tightening in 2026, while Bank of America, Deutsche Bank and RBC see 75bps. Market angle: exp — DeItaone, 2026-09-15. https://t.me/walter_bloomberg/35811
- Source: The 10 most overvalued housing markets in America — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-10-most-overvalued-housing-markets-in-america-6d28efdf?mod=mw_rss_topstories
- Source: TRUMP: “DON’T KILL THE GOLDEN GOOSE” President Trump says America’s AI and data center boom is happening because the U.S. holds a commanding global lead. He urged against measures that could slow the industry’s expansion, warning policymakers: “Don’t kill the Golden Goose!” — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35759
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 5.01] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -2.18, zc -0.11, resid-z -0.09 [quiet], 1d -0.03%, |z20|=2.18
- gbp_usd [FX]: last 1.35, z20 -1.76, zc -0.57, resid-z -0.66 [quiet], 1d -0.22%, |z20|=1.76
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.38 via gbp_usd, z -1.34, reacted)
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.642 vs eur_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.553 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_muthootfin_ns (rho 0.38, z -1.34)
- Source: Piero Cipollone: The future of euro cash: trusted today, designed for tomorrow — ECB press, 2026-09-14. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260914_1~91d3436449.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 4.26] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 750.70, z20 -2.26, zc -0.58, resid-z -0.66 [quiet], 1d -1.13%, |z20|=2.26
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.563 via dyn_tatatech_ns, z -1.71, reacted); dyn_tataelxsi_ns (rho 0.468 via dyn_tatatech_ns, z -1.74, reacted); dyn_techm_ns (rho 0.456 via dyn_tatatech_ns, z -0.97, quiet)
- **India receivers**: nifty_it (rho 0.563, z -1.71); dyn_tataelxsi_ns (rho 0.468, z -1.74); dyn_techm_ns (rho 0.456, z -0.97)
- Source: Tata Group stocks fall up to 7% after Tuesday’s IPO-buzz rally. Which stocks led the losses? — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/tata-group-stocks-fall-up-to-7-after-tuesdays-ipo-buzz-rally-which-stocks-led-the-losses/articleshow/134281314.cms
- Source: RIL, HUL, Nestle, Tata Consumer, Hyundai shares on the rise today | Key things to know — Mint Markets, 2026-09-16. https://www.livemint.com/market/stock-market-news/ril-hul-nestle-tata-consumer-muthoot-hyundai-shares-on-the-rise-today-key-things-to-know-11789539484574.html
- Source: Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, Blue Star, Allen Blenders, Tata Communications, Mazagon Dock — BusinessLine Mkts, 2026-09-16. https://www.thehindubusinessline.com/markets/buzzing-stocks-for-sept-16-bharat-forge-titagarh-rail-bhel-cochin-shipyard-thermax-blue-star-allen-blenders-tata-communications-mazagon-dock/article71470888.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↓ (4.09), dyn_icicigi_bo ↓ (3.62), nikkei_225 ↓ (3.57), gold_silver_ratio ↓ (3.4), usd_mxn ↑ (3.14), dyn_indusindbk_bo ↓ (3.13), dyn_hdb ↓ (2.92), commodities · 2 series ↑ (2.74), dyn_lenskart_ns ↑ (2.54), ust_2s10s ↓ (2.35), nifty_metal ↓ (2.29), dyn_tech ↑ (2.18)

## India macro
- nifty_50: 23237.5996 (1d 0.51%, z20 -2.05, flag amber)
- nifty_midcap_100: 60979.5508 (1d 0.17%, z20 -2.82, flag red)
- usd_inr: 95.9700 (1d 0.14%, z20 1.39, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6242 (1d -0.34%, z20 -1.53, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 63.3 — "Positive bias seen for Indian stocks at open, but analysts advise caution"
- COALINDIA.NS (COAL INDIA LTD) score 62.9 — "Positive bias seen for Indian stocks at open, but analysts advise caution"
- INDIANB.NS (INDIAN BANK) score 62.6 — "Positive bias seen for Indian stocks at open, but analysts advise caution"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 62.0 — "Positive bias seen for Indian stocks at open, but analysts advise caution"
- COIN (Coinbase Global, Inc.) score 57.1 — "Global Market: KOSPI climbs as chip stocks lead gains before Fed outcome"
- BAC (Bank of America Corporation) score 49.6 — "Global Market: Bank of Japan poised for rate hike as oil prices fuel inflation"
- HDB (HDFC Bank Limited) score 44.9 — "Global Market: Bank of Japan poised for rate hike as oil prices fuel inflation"
- OHI (Omega Healthcare Investors, In) score 44.8 — "Smallcap, midcap stocks give 85 multibaggers but pro investors are betting elsewhere"
- BOND (PIMCO Active Bond Exchange-Tra) score 44.0 — "Stocks, bonds hold ground before Fed; oil slips: Markets wrap"
- IDBI.NS (IDBI BANK LIMITED) score 42.0 — "Global Market: Bank of Japan poised for rate hike as oil prices fuel inflation"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.0 — "Global Market: Bank of Japan poised for rate hike as oil prices fuel inflation"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.0 — "Global Market: Bank of Japan poised for rate hike as oil prices fuel inflation"
- CHKP (Check Point Software Technolog) score 38.9 — "Hero Motors IPO GMP jumps 23% on Day 1; check key dates, review, subscription. Should you "
- TECHM.NS (TECH MAHINDRA LIMITED) score 34.7 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 34.7 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- TECH (Bio-Techne Corp) score 34.7 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- 301077.SZ (CHINASTARS) score 28.3 — "China Could Curb Fuel Exports as Diesel and Gasoline Stocks Sink"
- SEPN (Septerna, Inc.) score 24.5 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.1 — "Dividend record date alert: Last chance to buy Asian Energy, Bharat Rasayan, IRCON, MSTC, "
- LTH (Life Time Group Holdings, Inc.) score 21.7 — "Manika Plastech IPO Day 3: GMP at 7%, subscription reaches 8.3 times. Key details"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.0 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.0 — "Buzzing stocks for Sept 16: Bharat Forge, Titagarh Rail, BHEL, Cochin Shipyard, Thermax, B"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.7 — "SS Retail IPO opens today: GMP signals 31% listing gain. Here's all you need to know"
- NVDA (NVIDIA Corporation) score 9.4 — "BESSENT: TRUMP COMPLETELY ALIGNED WITH NVIDIA'S JENSEN HUANG"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.9 — "TRUMP BLASTS SUPREME COURT OVER MAJOR RULINGS President Trump sharply criticized the U.S. "
- JIOFIN.BO (Jio Financial Services Limited) score 8.3 — "Multibagger small cap stock Network People Services share price surges 18% today: Here’s w"
- JEF (Jefferies Financial Group Inc.) score 8.3 — "Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estim"
- MS (Morgan Stanley) score 7.7 — "Yes Bank shares jump 4% as Citi, Morgan Stanley see lender as key beneficiary of new UPI c"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.2 — "Dividend record date alert: Last chance to buy Asian Energy, Bharat Rasayan, IRCON, MSTC, "
- VT (Vanguard Total World Stock Ind) score 6.9 — "Chinese Solar Panels Drop to 12 Cents a Watt, Rooftop Installs Surge Worldwide"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.8 — "PC Jeweller share price plunges 6% today, falls 13% in a week | Here's why"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.6 — "Indonesia's new finance minister faces an uphill battle on fiscal credibility"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.2 — "Suzlon Energy, Adani Power share prices fall: Check 1-week, 1-year and 5-year returns"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 6.1 — "ITC shares edge higher after rise in select cigarette brands, experts see 10% rally in sho"
- META (Meta) score 5.6 — "Sensex, Nifty hold morning gains at midday; IT drags as metals, FMCG shine ahead of Fed ca"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.0 — "ICICI Prudential MF, Kotak MF top buyers in SS Retail's Rs 146 crore anchor round before I"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.1 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.6 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
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