# Visual Notes — Transmission Layer v3 (terminal restyle)

Presentation-only pass. No data logic changed: `fetch.py`, `engine.py`,
`digest.py`, `release_calendar.py`, `config.py` are untouched. Only `app.py`,
`.streamlit/config.toml`, `requirements.txt` (+plotly), and `.gitignore` moved.

## What changed

### Block A — theme, layout, sparklines (commit `18c396f`)
- **`.streamlit/config.toml`**: near-black dark theme (`#0b0d10`), off-white text,
  muted-grey secondary, one steel-blue structural accent. Red/amber deliberately
  NOT themed — reserved for flags in `app.py`.
- **`app.py`** rebuilt as a dense terminal:
  - Fixed layout order: headline strip → anomaly panel → drill-down → calendar
    → digest → four-market tabs.
  - All numeric values in monospace tabular figures; custom HTML tables replace
    `st.dataframe` so numerics are scannable and aligned.
  - Inline flag-tinted SVG sparklines (40-session trend) on every series in the
    grid: red line for red flags, amber for amber, muted grey for calm.

### Block B — drill-down + anomaly centrepiece (commit `2f5fe1b`)
- **Drill-down (Plotly)**: a selectbox opens a dark chart for any series — price,
  MA20/MA50, 20-day mean & high/low range, amber ±1.5σ and red ±2.5σ z-bands,
  markers where flags fired, and a ringed latest point. Zoom + hover on. Defaults
  to the top-ranked flagged series. Clean enough to screenshot into a post.
- **Anomaly panel as centrepiece**: flags are now ranked cards (big score, flag
  dot, reason, per-series sparkline, z/last), not a table row. Co-occurrence flags
  render the linked group's members side by side so the divergence is *visible*.
  Empty state is deliberately calm ("empty is the correct resting state").

## Colour discipline (by design)
Red (`#e5484d`) and amber (`#e0a83b`) appear ONLY on flags — dots, row tints, card
borders, sparkline strokes, z-band shading, chart flag markers. Nothing decorative
uses them. Percentage changes are neutral grey (no directional green/red). The
calendar "due ≤3 days" highlight uses the steel-blue accent, not amber. On a calm
day the board is monochrome and a single flag is the loudest thing on screen.

## Data the engine doesn't expose (would improve future visuals)
These are the honest gaps I routed around rather than changing the engine:

1. **Historical flag time-series.** `engine.build_snapshot()` returns only each
   series' *latest* flag state. To draw "markers where flags fired" across history,
   the drill-down chart **recomputes** the rolling z-score in the presentation
   layer (`_z_series` in `app.py`), using the engine's imported `Z_WIN_SHORT`,
   `AMBER_Z`, `RED_Z` so it stays consistent. If the engine exposed a per-date
   flag history (e.g. a `flag_history(sid)` returning dated amber/red points), the
   chart markers would be authoritative rather than a faithful re-derivation, and
   any future divergence between the two would disappear. **Top candidate for a
   small engine addition.**
2. **Trailing series for sparklines.** Sparklines read `data/prices.csv` directly
   in `app.py` (same committed file the engine reads). Fine as-is; an engine
   accessor returning the trailing window per series would just centralise it.
3. **60-day z on the chart.** The grid shows z20 and z60, but the drill-down band
   is built on the 20-day window only (matches the framework's 20-day range
   language). A z60 band toggle would need no engine change — say the word.
4. **Percentile / framework-trigger history.** Only current percentile and
   framework triggers are exposed. Charting where a 52-week extreme or a named
   framework threshold historically fired would need the engine to surface those
   per-date, same shape as gap #1.

## Things you may want to tune
- **Sparkline window** = 40 sessions (`SPARK_WINDOW`); **chart window** = 252
  sessions (`CHART_WINDOW`). Both in `app.py`, easy to change.
- **Headline strip series** (`HEADLINE_IDS` in `app.py`): currently nifty_50,
  midcap_largecap_ratio, usd_inr, ust_10y, dxy, brent, comex_gold,
  gold_silver_ratio. Swap to taste.
- **Moving averages** on the chart are MA20 / MA50. Change to 100/200 if you
  prefer slower context.
- **Accent colour** `#5a7ea6` (steel blue) in both `config.toml` and `app.py`
  constants — the one knob for the non-flag structural colour.

## Deploy note
`requirements.txt` now includes **plotly**. When you push, Streamlit Cloud will
reinstall and the drill-down chart will render there. Nothing else is needed —
the app still reads only committed data files; nothing fetches at open.

## Not done (out of scope this pass)
Row-click selection from the grid into the chart (used a selectbox instead —
robust and dependency-free). Could be added later with `st.dataframe`
row-selection or a custom component if you want click-through from the grid.
