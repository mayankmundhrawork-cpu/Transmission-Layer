# UI Notes — Terminal Design System (v4 UI pass)

The board's visual contract. Any future UI work builds on these tokens; if a
change can't be expressed with them, the system (not the change) gets extended.

## Palette — the only colours allowed on screen

| Token | Hex | Carries |
|---|---|---|
| `bg0` | `#060708` | page background (near-true-black, neutral) |
| `bg1` | `#0d0f11` | input fields, code blocks — nothing else |
| `g1` | `#f2f4f6` | primary text, price lines, open-session, emphasis |
| `g2` | `#b8bfc7` | secondary data (table body, member rows, news) |
| `g3` | `#7d8590` | labels, metadata, axis text, table headers |
| `g4` | `#4e555e` | dim: calm sparklines, watchlist, empty states, closed-session |
| `r1` | `#23272d` | primary rules — zone/section/table-header borders |
| `r2` | `#141619` | faint rules — row dividers, chart grid |
| `accent` | `#7d9cba` | desaturated steel: section labels, links, tab underline, calendar "soon", drill-down range markers. Structural ONLY |
| `red` | `#e5484d` | **flags only** |
| `amber` | `#e0a83b` | **flags only** |

Flag tints (meaning-carrying, not decoration): row/card backgrounds at
rgba(red, 0.055–0.10) / rgba(amber, 0.045–0.08); chart z-band fills at 0.05/0.07.
These are the only filled areas anywhere.

**The discipline:** hierarchy is brightness (g1→g4), grouping is rules (r1/r2)
or a 2px left-edge bar, and if red or amber is on screen, something is flagged.
Accent vs amber verified clearly distinct on the calendar (steel vs yellow).

## Type — one family, three sizes

Family: `'JetBrains Mono','SF Mono','Menlo','Consolas',ui-monospace,monospace`
applied to **everything** (body, labels, inputs, tabs, charts), with
`font-variant-numeric: tabular-nums` globally.

| Size | Style | Used for |
|---|---|---|
| 10px | UPPERCASE, +1.2–1.4px tracking, 600, `g3`/`accent` | section labels, table headers, micro-meta, tabs, feed names |
| 12.5px | 400, `g1`/`g2` | all data rows, news lines, body |
| 15px / 20px | 400/600, `g1` | headline-strip values / event scores — the only two large sizes |

Weights 400/600 only. Escape hatch (not yet used): if headline text at 12.5px
mono feels like work on Windows ClearType after a live-with-it day, bump ONLY
`.evt .news .n` to 13px. Do not reintroduce a proportional face.

## Spacing & structure

- 4px base rhythm; data rows ~22px line-height; zones separated by
  section-label + 1px `r1` rule (`.sec`), 16px above.
- **Rules, never boxes**: no border-radius anywhere (`* { border-radius: 0 }`),
  no shadows, no cards. Grouping = 2px left-edge bar (+ flag tint when flagged).
- No animation; hover is a colour shift only (0.08s).
- Status bar: single 11px line — brand / as-of / series counts / flag dots /
  events / fetch / session cluster (open desk `g1`, closed `g4`).

## Streamlit chrome kill-list (and the fights)

Hidden: `#MainMenu`, `header[data-testid="stHeader"]`, `footer`,
`stToolbar`, `stDecoration`, `stStatusWidget`.

Restyled via BaseWeb anchors: text input, `[data-baseweb="select"]`,
`[data-baseweb="popover"]`/`[data-baseweb="menu"]` (the portal-rendered
dropdown — without these two the open state flashes default purple),
`button[data-baseweb="tab"]` + `tab-highlight`/`tab-border`, expander, `pre`.

**Compromises hit (framework limits, cosmetic only):**
1. The global mono override converts Material-icon ligatures to literal text
   ("arrow_right") — icon glyphs are hidden outright
   (`[data-testid="stIconMaterial"] { display:none }`). If a future Streamlit
   renames the testid, the symptom returns as stray icon-name text.
2. `st.code`'s copy button styling is only partially reachable; it inherits
   the dark scheme acceptably.
3. Emotion class names (`st-emotion-cache-*`) are unstable across Streamlit
   versions — every override here anchors on `data-testid`/`data-baseweb`
   attributes instead. Keep it that way.

## Charts (Plotly)

paper/plot `bg0`; grid `r2`; axis/labels mono 10px `g3`; price `g1` 1.6px;
MA20 `g3` 1px, MA50 + 20d-mean `g4` 1px; 20d hi/lo `accent` dotted (structural);
z-bands amber/red fills only; hoverlabel plate `bg1` bordered `r1`; modebar
`hover`-only, logo off, icons tinted `g3`. Inline sparklines are hand-rolled
SVG (no modebar concern): flag-coloured stroke, `g4` when calm.

## Display-layer additions & observations (not folded silently)

- **Market-session cluster** in the status bar is new display logic (UTC
  clock math, approx cash hours IST/LDN/NY, no holiday calendar). Flagged in
  the design direction and approved.
- **Observation, out of scope for this pass:** RSS titles carry HTML entities
  (`S&amp;P`) into `data/digest_latest.txt` and the events panel — that's
  `digest.py`/`headlines.py` territory (an `html.unescape` at ingest), a
  data-layer one-liner to consider separately, not a UI fix.
