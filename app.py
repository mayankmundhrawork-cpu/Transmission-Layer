"""Streamlit board — self-assembling terminal (v4).

Presentation layer only: reads committed data files and computes views
in-process. Nothing here fetches from the network at app-open.

Sections, top to bottom:
  status strip → headline metrics → EVENTS (selectivity layer) → drill-down
  → universe panel (what's tracked & why) → searchable class grid
  → release calendar → morning digest

Run: streamlit run app.py
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from digest import CHAT_PROMPT
from engine import AMBER_Z, RED_Z, Z_WIN_SHORT, build_snapshot
from events import build_events
from headlines import recent_items
from registry import CLASSES, load_universe
from release_calendar import build_calendar
from settings import UNIVERSE_CAP

DATA_DIR = Path(__file__).parent / "data"
FETCH_LOG = DATA_DIR / "fetch_log.json"
DIGEST_TXT = DATA_DIR / "digest_latest.txt"
PRICES_CSV = DATA_DIR / "prices.csv"

# ── palette (red/amber are FLAGS ONLY — nothing decorative) ────────────
BG, PANEL, TEXT = "#0b0d10", "#14171c", "#d8dde3"
MUT, DIM, ACCENT = "#8b949e", "#5c636d", "#5a7ea6"
GRIDLN, HEADLN = "#1b1f26", "#2a2f37"
RED, AMBER = "#e5484d", "#e0a83b"
MONO = "'JetBrains Mono','SF Mono','Menlo','Consolas',ui-monospace,monospace"

HEADLINE_IDS = ["sp500", "vix", "ust_10y", "hy_oas", "dxy", "brent",
                "comex_gold", "btc_usd", "usd_inr", "nifty_50"]
SPARK_WINDOW = 40

st.set_page_config(page_title="Transmission Layer", layout="wide")

st.markdown(f"""
<style>
  .block-container {{ padding-top: 1.2rem; padding-bottom: 2rem; max-width: 100%; }}
  [data-testid="stVerticalBlock"] {{ gap: 0.45rem; }}
  .tl-title {{ font-size: 20px; font-weight: 700; color: {TEXT};
               border-bottom: 1px solid {HEADLN}; padding-bottom: 4px; }}
  .sec {{ color: {ACCENT}; font-size: 11px; font-weight: 700; text-transform: uppercase;
          letter-spacing: 1px; margin: 14px 0 4px; border-bottom: 1px solid {GRIDLN};
          padding-bottom: 3px; }}
  .mono {{ font-family: {MONO}; font-variant-numeric: tabular-nums; }}
  .metastrip {{ color: {MUT}; font-size: 11px; margin: 4px 0 6px; font-family: {MONO}; }}
  .metastrip b {{ color: {TEXT}; }}

  .strip {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 2px 0 6px; }}
  .cell {{ background: {PANEL}; border: 1px solid {GRIDLN}; border-left: 2px solid {HEADLN};
           padding: 5px 11px; min-width: 100px; }}
  .cell .lbl {{ color: {MUT}; font-size: 10px; text-transform: uppercase; letter-spacing: .5px; }}
  .cell .val {{ font-family: {MONO}; font-variant-numeric: tabular-nums; font-size: 15px; color: {TEXT}; }}
  .cell .chg {{ font-family: {MONO}; font-variant-numeric: tabular-nums; font-size: 11px; color: {MUT}; }}
  .cell.red {{ border-left-color: {RED}; }} .cell.amber {{ border-left-color: {AMBER}; }}

  table.tl {{ border-collapse: collapse; width: 100%; }}
  table.tl th {{ color: {MUT}; font-size: 10px; font-weight: 600; text-transform: uppercase;
                 letter-spacing: .5px; text-align: right; padding: 3px 9px;
                 border-bottom: 1px solid {HEADLN}; white-space: nowrap; }}
  table.tl td {{ font-size: 12.5px; padding: 2px 9px; border-bottom: 1px solid {GRIDLN};
                 text-align: right; white-space: nowrap; color: {TEXT}; }}
  table.tl td.l, table.tl th.l {{ text-align: left; }}
  table.tl td.c {{ text-align: center; padding: 0 6px; }}
  table.tl td.num {{ font-family: {MONO}; font-variant-numeric: tabular-nums; }}
  table.tl td.note {{ text-align: left; color: {MUT}; font-size: 11px;
                      white-space: normal; max-width: 420px; }}
  table.tl td.id {{ text-align: left; color: {TEXT}; }}
  table.tl a {{ color: {ACCENT}; text-decoration: none; }}
  table.tl a:hover {{ text-decoration: underline; }}
  .spark {{ display: block; }}

  .evt {{ background: {PANEL}; border: 1px solid {GRIDLN}; border-left: 3px solid {HEADLN};
          padding: 10px 16px; margin-bottom: 7px; }}
  .evt.red {{ border-left-color: {RED}; background: rgba(229,72,77,0.06); }}
  .evt.amber {{ border-left-color: {AMBER}; background: rgba(224,168,59,0.05); }}
  .evt .top {{ display: flex; align-items: baseline; gap: 14px; }}
  .evt .score {{ font-family: {MONO}; font-size: 22px; color: {TEXT}; min-width: 56px; }}
  .evt .lbl {{ font-size: 14px; color: {TEXT}; letter-spacing: .3px; }}
  .evt .sub {{ color: {MUT}; font-size: 11px; margin-left: auto; font-family: {MONO}; }}
  .evt .members {{ display: flex; gap: 20px; flex-wrap: wrap; margin-top: 8px; }}
  .evt .mem {{ min-width: 150px; }}
  .evt .mem .mid {{ font-size: 11.5px; color: {TEXT}; }}
  .evt .mem .mz {{ font-family: {MONO}; font-size: 10px; color: {MUT}; }}
  .evt .news {{ margin-top: 8px; border-top: 1px dashed {GRIDLN}; padding-top: 6px; }}
  .evt .news .n {{ color: {MUT}; font-size: 11.5px; margin: 2px 0; }}
  .evt .news .n b {{ color: {ACCENT}; font-weight: 600; }}
  .watch {{ color: {DIM}; font-size: 11.5px; font-family: {MONO}; margin-top: 2px; }}

  .calm {{ color: {DIM}; border: 1px dashed {GRIDLN}; padding: 14px; text-align: center;
           font-size: 13px; letter-spacing: .3px; }}
  .calm-sub {{ font-size: 11px; color: {DIM}; margin-top: 7px; }}
  .recent {{ border-left: 2px solid {ACCENT}; background: {PANEL}; padding: 6px 12px;
             margin-bottom: 8px; font-size: 12px; }}
  .recent a {{ color: {ACCENT}; text-decoration: none; }}
  .drill-cap {{ color: {MUT}; font-size: 11px; margin: 2px 0 6px; }}
  .uni-note {{ color: {MUT}; font-size: 11px; margin: 4px 0; }}
</style>
""", unsafe_allow_html=True)


# ── helpers ────────────────────────────────────────────────────────────
def _fmt(v, dp: int = 2, suffix: str = "") -> str:
    if v is None:
        return "·"
    try:
        if isinstance(v, float) and math.isnan(v):
            return "·"
        return f"{v:.{dp}f}{suffix}"
    except (TypeError, ValueError):
        return "·"


def _flag_color(flag: str) -> str:
    return {"red": RED, "amber": AMBER}.get(flag, DIM)


def _flag_dot(flag: str) -> str:
    glyph = {"red": "●", "amber": "●", "none": "·", "missing": "×"}.get(flag, "·")
    return f'<span style="color:{_flag_color(flag)}">{glyph}</span>'


def _row_bg(flag: str) -> str:
    if flag == "red":
        return "background:rgba(229,72,77,0.10);"
    if flag == "amber":
        return "background:rgba(224,168,59,0.08);"
    return ""


def _spark(vals: list[float], flag: str, w: int = 96, h: int = 20) -> str:
    clean = [v for v in vals if v is not None and not (isinstance(v, float) and math.isnan(v))]
    color = _flag_color(flag)
    if len(clean) < 2:
        return f'<svg class="spark" width="{w}" height="{h}"></svg>'
    lo, hi = min(clean), max(clean)
    rng = (hi - lo) or 1.0
    pad, n = 2, len(clean)
    pts = [f"{pad + (w - 2*pad) * i / (n - 1):.1f},"
           f"{pad + (h - 2*pad) * (1 - (v - lo) / rng):.1f}" for i, v in enumerate(clean)]
    lx, ly = pts[-1].split(",")
    return (f'<svg class="spark" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'preserveAspectRatio="none">'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" '
            f'stroke-width="1.3" stroke-linejoin="round"/>'
            f'<circle cx="{lx}" cy="{ly}" r="1.6" fill="{color}"/></svg>')


def _age(ts_iso: str) -> str:
    try:
        dt = datetime.fromisoformat(ts_iso)
        h = (datetime.now(timezone.utc) - dt).total_seconds() / 3600
        if h < 1:
            return f"{int(h*60)}m"
        if h < 48:
            return f"{int(h)}h"
        return f"{int(h//24)}d"
    except Exception:
        return "·"


@st.cache_data(show_spinner=False)
def _load_prices() -> pd.DataFrame:
    if not PRICES_CSV.exists():
        return pd.DataFrame()
    return pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()


def _trend(prices_df: pd.DataFrame, sid: str) -> list[float]:
    if prices_df.empty or sid not in prices_df.columns:
        return []
    return prices_df[sid].dropna().tail(SPARK_WINDOW).tolist()


# ── drill-down chart (unchanged mechanics from v3) ─────────────────────
CHART_WINDOW = 252
PLOT_FONT = "Consolas, Menlo, monospace"


def _z_series(s: pd.Series):
    m = s.shift(1).rolling(Z_WIN_SHORT).mean()
    sd = s.shift(1).rolling(Z_WIN_SHORT).std(ddof=0)
    return (s - m) / sd, m, sd


def _drilldown_fig(sid: str, cur_flag: str) -> go.Figure:
    s_full = prices[sid].dropna()
    z_full, mean_full, sd_full = _z_series(s_full)
    disp = s_full.tail(CHART_WINDOW)
    idx = disp.index
    price = disp
    mean, sd, z = mean_full.reindex(idx), sd_full.reindex(idx), z_full.reindex(idx)
    ma20 = s_full.rolling(Z_WIN_SHORT).mean().reindex(idx)
    ma50 = s_full.rolling(50).mean().reindex(idx)
    rng_hi = s_full.rolling(Z_WIN_SHORT).max().reindex(idx)
    rng_lo = s_full.rolling(Z_WIN_SHORT).min().reindex(idx)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=idx, y=mean + RED_Z * sd, line=dict(width=0),
                             showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean - RED_Z * sd, fill="tonexty",
                             fillcolor="rgba(229,72,77,0.05)", line=dict(width=0),
                             name="±2.5σ", hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean + AMBER_Z * sd, line=dict(width=0),
                             showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean - AMBER_Z * sd, fill="tonexty",
                             fillcolor="rgba(224,168,59,0.07)", line=dict(width=0),
                             name="±1.5σ", hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=rng_hi, line=dict(color=ACCENT, width=0.7, dash="dot"),
                             name="20d hi/lo", hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=rng_lo, line=dict(color=ACCENT, width=0.7, dash="dot"),
                             showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean, line=dict(color=MUT, width=1, dash="dash"),
                             name="20d mean", hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=ma20, line=dict(color="#6aa0c8", width=1), name="MA20"))
    fig.add_trace(go.Scatter(x=idx, y=ma50, line=dict(color="#7d8590", width=1), name="MA50"))
    fig.add_trace(go.Scatter(x=idx, y=price, line=dict(color=TEXT, width=1.6),
                             name=sid, customdata=z,
                             hovertemplate="%{x|%Y-%m-%d}<br>" + sid +
                                           " %{y:.2f}<br>z=%{customdata:.2f}<extra></extra>"))
    za = z.abs()
    am = (za >= AMBER_Z) & (za < RED_Z)
    rm = za >= RED_Z
    if am.any():
        fig.add_trace(go.Scatter(x=idx[am], y=price[am], mode="markers",
                                 marker=dict(color=AMBER, size=5), name="amber",
                                 hovertemplate="%{x|%Y-%m-%d} amber<extra></extra>"))
    if rm.any():
        fig.add_trace(go.Scatter(x=idx[rm], y=price[rm], mode="markers",
                                 marker=dict(color=RED, size=6), name="red",
                                 hovertemplate="%{x|%Y-%m-%d} red<extra></extra>"))
    last_color = {"red": RED, "amber": AMBER}.get(cur_flag, ACCENT)
    fig.add_trace(go.Scatter(x=[idx[-1]], y=[price.iloc[-1]], mode="markers",
                             marker=dict(color="rgba(0,0,0,0)", size=13,
                                         line=dict(width=2, color=last_color)),
                             name="latest", hovertemplate="latest %{y:.2f}<extra></extra>"))
    fig.update_layout(template="plotly_dark", height=400, paper_bgcolor=BG,
                      plot_bgcolor=BG, font=dict(family=PLOT_FONT, color=TEXT, size=11),
                      margin=dict(l=44, r=12, t=28, b=28), hovermode="x unified",
                      legend=dict(orientation="h", yanchor="bottom", y=1.0, x=0,
                                  font=dict(size=9), bgcolor="rgba(0,0,0,0)"),
                      xaxis=dict(gridcolor=GRIDLN, zeroline=False),
                      yaxis=dict(gridcolor=GRIDLN, zeroline=False))
    return fig


# ── load everything (read-only) ────────────────────────────────────────
snap = build_snapshot()
prices = _load_prices()
universe = load_universe()
headlines = recent_items()

st.markdown('<div class="tl-title">THE TRANSMISSION LAYER</div>', unsafe_allow_html=True)

if "error" in snap:
    st.error(snap["error"])
    st.stop()

by_id = {r["id"]: r for r in snap["series"]}
red_n = sum(1 for r in snap["series"] if r["flag"] == "red")
amber_n = sum(1 for r in snap["series"] if r["flag"] == "amber")
missing_n = sum(1 for r in snap["series"] if r["flag"] == "missing")
members = universe.get("members", {})
n_dyn = len(members)
n_backbone = len(snap["series"]) - n_dyn

fetched_at = ""
if FETCH_LOG.exists():
    try:
        fetched_at = json.loads(FETCH_LOG.read_text()).get("fetched_at", "")[:16]
    except Exception:
        pass

ev = build_events(snap, prices, headlines)
counts = ev["counts"]

st.markdown(
    f'<div class="metastrip">as of <b>{snap.get("last_data_date") or "·"}</b> · '
    f'universe <b>{len(snap["series"])}</b> '
    f'(backbone {n_backbone} + news-tracked <b>{n_dyn}</b>/{UNIVERSE_CAP}) · '
    f'<span style="color:{RED}">red {red_n}</span> · '
    f'<span style="color:{AMBER}">amber {amber_n}</span> · '
    f'events <b>{len(ev["events"])}</b> (suppressed {counts.get("suppressed", 0)}) · '
    f'headlines {len(headlines)} · fetch {fetched_at or "·"}</div>',
    unsafe_allow_html=True)


# ── 1) headline strip ──────────────────────────────────────────────────
cells = []
for sid in HEADLINE_IDS:
    r = by_id.get(sid)
    if not r or r.get("last") is None:
        continue
    flag = r["flag"]
    cls = "cell " + (flag if flag in ("red", "amber") else "")
    dot = f' {_flag_dot(flag)}' if flag in ("red", "amber") else ""
    cells.append(
        f'<div class="{cls.strip()}"><div class="lbl">{sid}{dot}</div>'
        f'<div class="val">{_fmt(r["last"], 2)}</div>'
        f'<div class="chg">{_fmt(r["d1_pct"], 2, "%")} · 5d {_fmt(r["d5_pct"], 2, "%")}</div></div>')
st.markdown(f'<div class="strip">{"".join(cells)}</div>', unsafe_allow_html=True)


# ── 2) events — the board's loud layer ─────────────────────────────────
st.markdown('<div class="sec">◈ Events</div>', unsafe_allow_html=True)
if not ev["events"]:
    st.markdown(
        f'<div class="calm">◦ No events — calm session.'
        f'<div class="calm-sub">{len(snap["series"])} series watched · '
        f'{counts.get("flagged", 0)} sub-threshold flags absorbed · '
        f'an empty board is the correct resting state</div></div>',
        unsafe_allow_html=True)
else:
    html = []
    for e in ev["events"]:
        mems = []
        for m in e["members"][:8]:
            sp = _spark(_trend(prices, m["id"]), m["flag"], w=130, h=24)
            nm = m["name"] if m["dynamic"] else m["id"]
            mems.append(
                f'<div class="mem"><div class="mid">{_flag_dot(m["flag"])} {nm}</div>'
                f'{sp}<div class="mz">z {_fmt(m["z20"], 2)} · {_fmt(m["last"], 2)} · '
                f'1d {_fmt(m["d1_pct"], 2, "%")}</div></div>')
        news = "".join(
            f'<div class="n"><b>{n["feed"]}</b> · {_age(n["ts"])} · {n["title"]}</div>'
            for n in e["news"])
        news_block = f'<div class="news">{news}</div>' if news else ""
        reasons = "; ".join(dict.fromkeys(
            r for m in e["members"] for r in m["reasons"][:2]))[:180]
        html.append(
            f'<div class="evt {e["level"]}"><div class="top">'
            f'<span class="score">{e["score"]:.2f}</span>'
            f'<span class="lbl">{_flag_dot(e["level"])} {e["label"]}</span>'
            f'<span class="sub">{reasons}</span></div>'
            f'<div class="members">{"".join(mems)}</div>{news_block}</div>')
    st.markdown("".join(html), unsafe_allow_html=True)

if ev["watchlist"]:
    wl = " · ".join(f'{w["label"]} {w["score"]:.1f}' for w in ev["watchlist"][:12])
    st.markdown(f'<div class="watch">watchlist (below floor): {wl}</div>',
                unsafe_allow_html=True)


# ── 3) drill-down ──────────────────────────────────────────────────────
st.markdown('<div class="sec">Drill-down</div>', unsafe_allow_html=True)
chartable = [r["id"] for r in snap["series"] if r["id"] in prices.columns]
if chartable:
    default_id = chartable[0]
    for e in ev["events"]:
        for m in e["members"]:
            if m["id"] in chartable:
                default_id = m["id"]
                break
        else:
            continue
        break
    sel = st.selectbox("series", chartable, index=chartable.index(default_id),
                       label_visibility="collapsed")
    st.markdown('<div class="drill-cap">price · MA20/50 · 20d mean &amp; range · '
                'z-bands · flag markers · ringed latest. Zoom + hover on.</div>',
                unsafe_allow_html=True)
    st.plotly_chart(_drilldown_fig(sel, by_id[sel]["flag"]),
                    use_container_width=True,
                    config={"displayModeBar": True, "scrollZoom": True})


# ── 4) universe — what's tracked and why ───────────────────────────────
st.markdown('<div class="sec">Universe · news-tracked layer</div>', unsafe_allow_html=True)
if not members:
    st.markdown('<div class="calm">No news-admitted members yet — the universe '
                'assembles as headlines repeat across feeds.</div>', unsafe_allow_html=True)
else:
    head = ('<tr><th class="l">symbol</th><th class="l">name</th><th class="l">class</th>'
            '<th>score</th><th>age</th><th>quiet</th><th class="l">why tracked '
            '(admitting evidence)</th></tr>')
    rows_html = []
    now = datetime.now(timezone.utc)
    for sym, m in sorted(members.items(), key=lambda kv: -kv[1].get("score", 0)):
        ev0 = (m.get("evidence") or [{}])[0]
        age_d = _age(m.get("added", ""))
        quiet = _age(m.get("last_mention", ""))
        rows_html.append(
            f'<tr><td class="id mono">{sym}</td>'
            f'<td class="l">{m.get("name","")[:32]}</td>'
            f'<td class="l" style="color:{MUT}">{m.get("cls","")}</td>'
            f'<td class="num">{m.get("score", 0):.2f}</td>'
            f'<td class="num">{age_d}</td><td class="num">{quiet}</td>'
            f'<td class="note">{ev0.get("title","")[:110]}'
            f'<span style="color:{DIM}"> — {ev0.get("feed","")}</span></td></tr>')
    st.markdown(f'<table class="tl">{head}{"".join(rows_html)}</table>',
                unsafe_allow_html=True)

cands = universe.get("candidates", {})
if cands:
    top = sorted(cands.items(), key=lambda kv: -kv[1]["score"])[:8]
    line = " · ".join(f'{c["display"]} {c["score"]:.1f}({len(c.get("feeds", []))}f)'
                      for _, c in top)
    st.markdown(f'<div class="uni-note">candidates pending admission '
                f'(need score ≥2 across ≥2 feeds): {line}</div>', unsafe_allow_html=True)


# ── 5) grid — searchable, class-tabbed ─────────────────────────────────
st.markdown('<div class="sec">Grid · full universe</div>', unsafe_allow_html=True)
query = st.text_input("filter", placeholder="filter by id / name / symbol …",
                      label_visibility="collapsed").strip().lower()

by_class: dict[str, list] = {c: [] for c in CLASSES}
for r in snap["series"]:
    if query:
        hay = f'{r["id"]} {r.get("name","")} {r.get("symbol","")}'.lower()
        if query not in hay:
            continue
    by_class.setdefault(r["market"], []).append(r)


def _metric_table(rows: list[dict]) -> str:
    head = ('<tr><th class="c"></th><th class="l">series</th><th class="l">trend</th>'
            '<th>last</th><th>1d%</th><th>5d%</th><th>z20</th><th>z60</th>'
            '<th>1y%</th><th class="l">note</th></tr>')
    out = []
    for r in rows:
        flag = r["flag"]
        sp = _spark(_trend(prices, r["id"]), flag)
        label = r["id"]
        if r.get("dynamic"):
            label = f'{r["id"]}<span style="color:{DIM}"> · {r.get("name","")[:22]}</span>'
        out.append(
            f'<tr style="{_row_bg(flag)}"><td class="c">{_flag_dot(flag)}</td>'
            f'<td class="id">{label}</td><td class="l">{sp}</td>'
            f'<td class="num">{_fmt(r["last"], 2)}</td>'
            f'<td class="num">{_fmt(r["d1_pct"], 2, "%")}</td>'
            f'<td class="num">{_fmt(r["d5_pct"], 2, "%")}</td>'
            f'<td class="num">{_fmt(r["z20"], 2)}</td>'
            f'<td class="num">{_fmt(r["z60"], 2)}</td>'
            f'<td class="num">{_fmt(r["pct_1y"], 0)}</td>'
            f'<td class="note">{"; ".join(r["reasons"]) if r["reasons"] else ""}</td></tr>')
    return f'<table class="tl">{head}{"".join(out)}</table>'


nonempty = [c for c in CLASSES if by_class.get(c)]
if not nonempty:
    st.markdown('<div class="calm">No series match the filter.</div>', unsafe_allow_html=True)
else:
    tabs = st.tabs([f"{c} ({len(by_class[c])})" for c in nonempty])
    for tab, cls_name in zip(tabs, nonempty):
        with tab:
            st.markdown(_metric_table(by_class[cls_name]), unsafe_allow_html=True)


# ── 6) release calendar ────────────────────────────────────────────────
st.markdown('<div class="sec">Release calendar</div>', unsafe_allow_html=True)
cal = build_calendar()
if cal["recent"]:
    links = " · ".join(
        f'<a href="{r["url"]}" target="_blank">{r["name"]}</a> ({r["released_date"]})'
        for r in cal["recent"])
    st.markdown(f'<div class="recent"><b>Released &lt;24h:</b> {links}</div>',
                unsafe_allow_html=True)
if cal["upcoming"]:
    head = ('<tr><th>days</th><th class="l">date</th><th class="l">release</th>'
            '<th class="l">market</th><th class="l">threshold</th><th class="l">link</th></tr>')
    body = []
    for r in cal["upcoming"]:
        edge = f"border-left:2px solid {ACCENT};" if r["soon"] else \
               "border-left:2px solid transparent;"
        dcol = ACCENT if r["soon"] else TEXT
        body.append(
            f'<tr style="{edge}"><td class="num" style="color:{dcol}">T-{r["days_until"]}d</td>'
            f'<td class="l num">{r["next_date"]}</td><td class="l">{r["name"]}</td>'
            f'<td class="l" style="color:{MUT}">{r["market"]}</td>'
            f'<td class="note">{r["threshold"]}</td>'
            f'<td class="l"><a href="{r["url"]}" target="_blank">open</a></td></tr>')
    st.markdown(f'<table class="tl">{head}{"".join(body)}</table>', unsafe_allow_html=True)


# ── 7) morning digest ──────────────────────────────────────────────────
st.markdown('<div class="sec">Morning digest</div>', unsafe_allow_html=True)
if not DIGEST_TXT.exists():
    st.markdown('<div class="calm">No digest yet — the scheduled workflow '
                'regenerates it.</div>', unsafe_allow_html=True)
else:
    digest_text = DIGEST_TXT.read_text(encoding="utf-8")
    header = digest_text.splitlines()[0] if digest_text else ""
    st.markdown(f'<div class="drill-cap">{header.strip("= ")} · copy via the icon '
                f'top-right</div>', unsafe_allow_html=True)
    st.code(digest_text, language="text")
    with st.expander("Chat prompt to paste with the digest"):
        st.code(CHAT_PROMPT, language="text")

st.markdown(
    f'<div class="drill-cap">Flags: red |z|≥2.5 or framework+|z|≥bar · amber |z|≥bar '
    f'(bar 1.5 backbone / 2.0 news-tracked), pct≤5/≥95, or framework · events cluster '
    f'correlated same-direction flags; floor {counts.get("surfaced", 0) and ""}3.2 · '
    f'red/amber mark flags only.</div>', unsafe_allow_html=True)
