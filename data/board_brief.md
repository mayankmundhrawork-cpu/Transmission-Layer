# Transmission Layer — board brief · 2026-08-31 10:49Z

data as of **2026-08-31** · 98 series · 9 red / 27 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.269, 2d in regime; vol-pct 0.175, breadth-off 0.364, Markov P(high-vol) 0.014)
- [WEAK] **safe_haven_gold** — corr20 -0.17, corr60 -0.39, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.02, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.34, corr60 -0.83, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.21, corr60 -0.14, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.08, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.28, corr60 0.2, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0006496287948376533)
- **SETUP** dxy → eur_usd: leads 1d (ccf -0.836, β -0.9038, p 0.0); driver zc 1.63 → expected -0.492%. Type hit-rate 0.823 (n=2047).
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.726, β -0.78, p 0.0); driver zc 1.63 → expected -0.425%. Type hit-rate 0.823 (n=2047).
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.651, β 0.9285, p 0.0); driver zc 1.63 → expected 0.506%. Type hit-rate 0.823 (n=2047).
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.57, β -0.8502, p 0.0); driver zc 1.63 → expected -0.463%. Type hit-rate 0.823 (n=2047).
- **SETUP** dxy → usd_mxn: leads 1d (ccf 0.409, β 0.5915, p 0.0); driver zc 1.63 → expected 0.322%. Type hit-rate 0.823 (n=2047).
- Track record · residual_reversion: hit-rate **0.497** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2047) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.03] cross-asset · 2 series ↑
- wti [COMMODITIES]: last 86.33, z20 1.19, zc -0.07, resid-z 0.00 [quiet], 1d 3.51%, 1-session move +3.51% ≥ 1.5%
- dow_jones [INDICES]: last 53546.79, z20 -0.06, zc -0.06, resid-z 0.28 [quiet], 1d -0.04%, 1y-pct=95
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.98 vs wti
- Watch next: sp500 (co-move) — not yet - watch; rho 0.741 vs dow_jones, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.662 vs dow_jones, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.626 vs dow_jones, historically leads by 1d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.574 vs dow_jones, historically leads by 5d
- Source: Global market: European shares dip as fresh US-Iran strikes push oil, bond yields higher — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-dip-as-fresh-us-iran-strikes-push-oil-bond-yields-higher/articleshow/133649880.cms
- Source: Brent oil tops $90 after first U.S. and Iran fighting in a month — MarketWatch Top, 2026-08-31. https://www.marketwatch.com/story/brent-oil-tops-90-after-first-u-s-and-iran-fighting-in-a-month-3b818e19?mod=mw_rss_topstories
- Source: Asian Refiners Turn to Argentina as Iran War Disrupts Oil Supply — OilPrice, 2026-08-31. https://oilprice.com/Latest-Energy-News/World-News/Asian-Refiners-Turn-to-Argentina-as-Iran-War-Disrupts-Oil-Supply.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-22 (d=0.26), 2024-10-17 (d=0.37)

### [RED 5.76] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1717.70, z20 3.76, zc 2.53, resid-z 2.38 [unexplained], 1d 6.27%, |z20|=3.76; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy share price hits lifetime high | Delivers 423% returns from IPO price — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-hits-lifetime-high-delivers-423-returns-from-ipo-price-11788162211726.html
- Source: Ather Energy shares rally 4% after launch of Konarc electric scooter at Rs 99,999. Buy, sell or hold the stock? — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-rally-4-after-launch-of-konarc-electric-scooter-at-rs-99999-buy-sell-or-hold-the-stock/articleshow/133643336.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 5.16] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 138.38, z20 3.16, zc 1.40, resid-z 1.32 [quiet], 1d 3.87%, |z20|=3.16
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.387 via dyn_chkp, z 1.44, reacted)
- **India receivers**: dyn_karurvysya_ns (rho -0.387, z 1.44)
- Source: Nomura initiates coverage on Clean Max Enviro with Buy call. Check upside potential, key reasons — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/nomura-initiates-coverage-on-clean-max-enviro-with-buy-call-check-upside-potential-key-reasons/articleshow/133643047.cms
- Source: Annu Projects IPO allotment likely today; Here's how to check your status — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/ipos/fpos/annu-projects-ipo-allotment-likely-today-heres-how-to-check-your-status/articleshow/133641219.cms
- Source: Annu Projects IPO share allotment in focus today: How to check status online? What GMP signals about stock listing? — Mint Markets, 2026-08-31. https://www.livemint.com/market/ipo/annu-projects-ipo-share-allotment-in-focus-today-how-to-check-status-online-what-gmp-signals-about-stock-listing-11788142613817.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2024-10-18 (d=0.02)

### [RED 4.91] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.67, z20 1.91, zc n/a, resid-z n/a [quiet], 1d 0.64%, 52-wk extreme (pct=100); |z20|=1.91; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.486 via midcap_largecap_ratio, z -1.48, reacted); nifty_fmcg (rho -0.397 via midcap_largecap_ratio, z -2.48, reacted); dyn_inoxindia_ns (rho 0.395 via midcap_largecap_ratio, z 2.81, reacted); nifty_it (rho -0.371 via midcap_largecap_ratio, z 0.3, quiet); dyn_techm_ns (rho -0.368 via midcap_largecap_ratio, z 0.41, quiet)
- **India receivers**: nifty_50 (rho -0.486, z -1.48); nifty_fmcg (rho -0.397, z -2.48); dyn_inoxindia_ns (rho 0.395, z 2.81); nifty_it (rho -0.371, z 0.3)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.42] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 66.39, z20 -1.42, zc n/a, resid-z n/a [quiet], 1d -0.68%, GSR<75 (extreme low)
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho -0.456 via gold_silver_ratio, z 0.05, quiet); nifty_midcap_100 (rho -0.4 via gold_silver_ratio, z 1.81, reacted); dyn_stylebaaza_ns (rho -0.4 via gold_silver_ratio, z 0.72, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.891 vs gold_silver_ratio
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.576 vs gold_silver_ratio, historically leads by 4d
- **India receivers**: nifty_metal (rho -0.456, z 0.05); nifty_midcap_100 (rho -0.4, z 1.81); dyn_stylebaaza_ns (rho -0.4, z 0.72)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 4.06] commodities · 3 series ↑
- wheat [COMMODITIES]: last 772.50, z20 2.74, zc 1.52, resid-z 1.56 [unexplained], 1d 0.72%, |z20|=2.74; 1y-pct=100
- corn [COMMODITIES]: last 536.00, z20 2.62, zc 0.27, resid-z -0.16 [quiet], 1d 4.69%, |z20|=2.62; 1y-pct=100
- soybeans [COMMODITIES]: last 1283.00, z20 2.25, zc 1.54, resid-z 1.29 [moved], 1d 0.53%, |z20|=2.25; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho -0.361 via corn, z -1.21, reacted)
- **India receivers**: dyn_coalindia_ns (rho -0.361, z -1.21)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 3.98] natgas ↑
- natgas [COMMODITIES]: last 2.90, z20 1.98, zc -0.20, resid-z -0.23 [quiet], 1d 0.38%, |z20|=1.98
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.045 vs natgas, historically leads by 4d
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.003 vs natgas, historically leads by 4d
- Source: China’s August LNG Imports Set to Drop as High Prices Hit Demand — Mint Markets, 2026-08-31. https://www.livemint.com/market/chinas-august-lng-imports-set-to-drop-as-high-prices-hit-demand-11788153975524.html
- Source: Data Centers Are Driving a New U.S. Natural Gas Buildout — OilPrice, 2026-08-30. https://oilprice.com/Energy/Energy-General/Data-Centers-Are-Driving-a-New-US-Natural-Gas-Buildout.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 3.47] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 663.00, z20 1.47, zc -0.46, resid-z -0.75 [quiet], 1d 4.22%, 1y-pct=100
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: MSCI Rejig: Adani Energy, Lenskart, Groww to see inflows; Reliance weight trimmed — Mint Markets, 2026-08-31. https://www.livemint.com/market/stock-market-news/msci-rejig-adani-energy-lenskart-groww-to-see-inflows-reliance-weight-trimmed-11788149469073.html
- Source: Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey has just started — ET Markets, 2026-08-31. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-shares-to-rally-40-nomura-initiates-coverage-with-buy-says-its-growth-journey-has-just-started/articleshow/133641032.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

## Watchlist (below surfacing floor)
brent_wti_spread ↓ (3.44), dyn_hdb ↓ (2.95), dyn_inoxindia_ns ↑ (2.81), dyn_icicigi_bo ↓ (2.78), dyn_tech ↑ (2.7), dyn_bond ↓ (2.67), dyn_tataelxsi_ns ↓ (2.61), nifty_fmcg ↓ (2.48), usd_cny ↓ (2.39), dyn_tatatech_ns ↑ (2.18), hy_oas ↓ (2.07), dyn_dks ↓ (1.99)

## India macro
- nifty_50: 24080.4004 (1d -0.39%, z20 -1.48, flag none)
- nifty_midcap_100: 64226.6992 (1d 0.24%, z20 1.81, flag amber)
- usd_inr: 95.1520 (1d -0.33%, z20 -0.44, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6672 (1d 0.64%, z20 1.91, flag red)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 61.6 — "Sashidhar Jagdishan not to seek third term as HDFC Bank chief"
- COALINDIA.NS (COAL INDIA LTD) score 60.6 — "India emerges as key petrol supplier to Russia as refinery attacks disrupt fuel supplies"
- INOXINDIA.NS (INOX INDIA LIMITED) score 60.2 — "India emerges as key petrol supplier to Russia as refinery attacks disrupt fuel supplies"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 59.4 — "India emerges as key petrol supplier to Russia as refinery attacks disrupt fuel supplies"
- BAC (Bank of America Corporation) score 54.0 — "Sashidhar Jagdishan not to seek third term as HDFC Bank chief"
- HDB (HDFC Bank Limited) score 48.6 — "Sashidhar Jagdishan not to seek third term as HDFC Bank chief"
- IDBI.NS (IDBI BANK LIMITED) score 46.9 — "Sashidhar Jagdishan not to seek third term as HDFC Bank chief"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 46.9 — "Sashidhar Jagdishan not to seek third term as HDFC Bank chief"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 46.9 — "Sashidhar Jagdishan not to seek third term as HDFC Bank chief"
- COIN (Coinbase Global, Inc.) score 38.1 — "Iran War Adds $330 Billion to Global Energy Import Bill"
- TECHM.NS (TECH MAHINDRA LIMITED) score 34.3 — "10 years, 1,800 survey sites: inside China’s hi-tech push to map linguistic diversity"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 33.5 — "10 years, 1,800 survey sites: inside China’s hi-tech push to map linguistic diversity"
- TECH (Bio-Techne Corp) score 33.5 — "10 years, 1,800 survey sites: inside China’s hi-tech push to map linguistic diversity"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.4 — "Indian govt bond yields to remain range-bound at 6.6-6.9%, limiting near-term trading wind"
- OHI (Omega Healthcare Investors, In) score 32.4 — "Cash market volumes fall to five-month low as CAS swings rattle investors"
- LTH (Life Time Group Holdings, Inc.) score 26.6 — "China-Nepal floods: 9 Chinese tunnel experts sent to aid rescue in race against time"
- 301077.SZ (CHINASTARS) score 25.5 — "China-Nepal floods: 9 Chinese tunnel experts sent to aid rescue in race against time"
- CHKP (Check Point Software Technolog) score 22.8 — "Today’s Gold Rate, Aug 29: Check gold rates in Delhi, Mumbai, Chennai"
- NVDA (NVIDIA Corporation) score 21.5 — "Nvidia stock under pressure. What’s behind the pullback?"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.1 — "Mexico’s Green Energy Push Is Finally Gaining Momentum"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.5 — "20 stocks, 100% returns: How retail investors tapped a multibagger wave in deeper Indian m"
- JIOFIN.BO (Jio Financial Services Limited) score 11.8 — "Bank of England chief warns new AI models threaten global financial stability"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.8 — "Career finance official moves into pole position to become Shanghai’s next mayor"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Steel Share Price Live Updates: Tata Steel's Daily Performance Update"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Tata Steel Share Price Live Updates: Tata Steel's Daily Performance Update"
- MS (Morgan Stanley) score 9.1 — "HDFC Bank shares gain 3% as CEO Jagdishan rejects new term; Morgan Stanley, Jefferies, oth"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.6 — "Coal India to launch IPOs of South Eastern Coalfields and Mahanadi Coalfields this fiscal"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.2 — "Adani Ent Share Price Live Updates: Adani Enterprises Falls Below Key Moving Average"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "Bank of England chief warns new AI models threaten global financial stability"
- META (Meta) score 8.0 — "Hindustan Zinc, Vedanta, Nalco and other metal stocks slide up to 5%. Here's why"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.3 — "Lalithaa Jewellery to open stores in Malaysia, Singapore"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.2 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.7 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.6 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- VT (Vanguard Total World Stock Ind) score 3.9 — "TRUMP: US ENTERS AGREEMENT WITH VENEZUELA ON BIGGEST OIL DEAL IN WORLD HISTORY US SECURES "
- DKS (Dick's Sporting Goods Inc) score 1.7 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 1.3 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.2 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.0 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.0 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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