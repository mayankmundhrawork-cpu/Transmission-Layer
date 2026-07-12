"""Board brief — the dashboard's full state as one LLM-ready markdown file.

Assembles everything a writing session needs into data/board_brief.md:
status, events with theses + India transmission + citations, watchlist,
India macro, squawk tape, universe with evidence, open hypotheses and
journal intents, and the article-writing prompt.

Written by every scheduled run (after the overnight pass), so a fresh
Claude conversation can be fed the live board with zero copy-paste.
Optionally mirrors to a GitHub Gist when GIST_TOKEN + GIST_ID are set,
giving a stable public raw URL for auto-fetch.

Run: python brief.py
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
BRIEF_MD = DATA_DIR / "board_brief.md"

METHODOLOGY = """---
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
prints enter as today's provisional observation."""

WRITING_PROMPT = """---
## How to use this brief (instruction to the assistant)
You are helping draft a macro article for an audience of Indian market
practitioners. Work ONLY from the data above — never invent numbers.
Priorities: (1) the event-to-price gap — what the news implies that price
has not yet reflected; (2) the transmission chain into Indian instruments,
using the INDIA lines and laggards; (3) historical precedent where given.
A sceptical 'no gap here' is a valid conclusion. Cite specifics (levels,
z-scores, dates) from the brief. The owner's hypotheses and journal intents
show what they are already thinking — engage with them directly."""


def _fmt(v, dp=2):
    try:
        return f"{v:.{dp}f}"
    except (TypeError, ValueError):
        return "n/a"


def build_brief() -> str:
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    from india import india_receivers
    from registry import load_universe
    from relations import laggards_for, load_relations
    from research import event_key, load_bundles
    from thesis import load_theses

    snap = build_snapshot()
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0, parse_dates=True)
    hl = recent_items()
    ev = build_events(snap, prices, hl)
    by_id = {r["id"]: r for r in snap["series"]}
    rel = load_relations()
    theses = load_theses().get("theses", {})
    bundles = load_bundles().get("bundles", {})
    uni = load_universe()

    now = datetime.now(timezone.utc)
    red = sum(1 for r in snap["series"] if r["flag"] == "red")
    amber = sum(1 for r in snap["series"] if r["flag"] == "amber")

    L: list[str] = []
    L.append(f"# Transmission Layer — board brief · {now:%Y-%m-%d %H:%M}Z")
    L.append(f"\ndata as of **{snap.get('last_data_date')}** · "
             f"{len(snap['series'])} series · {red} red / {amber} amber · "
             f"{len(ev['events'])} events surfaced "
             f"({ev['counts'].get('suppressed', 0)} suppressed)")

    # ── regime & assumption health (measured, gates everything below) ───
    try:
        from assumptions import load_assumptions_state
        from regime import load_regime
        reg = load_regime()
        comp = reg.get("components", {})
        L.append("\n## Regime & assumption health (measured at generation)")
        L.append(f"- **Regime: {reg.get('label')}** (score {reg.get('score')}, "
                 f"{reg.get('days_in_regime')}d in regime; vol-pct "
                 f"{comp.get('vol_pct')}, breadth-off {comp.get('breadth_off')}, "
                 f"Markov P(high-vol) {reg.get('markov', {}).get('p_highvol')})")
        for name, a in load_assumptions_state().get("assumptions", {}).items():
            extra = (f", contra {a['contra_series']} corr20={a['contra_corr20']}"
                     if a.get("contra_corr20") is not None else "")
            cp = (f", last shift {a['last_changepoint']}"
                  if a.get("last_changepoint") else "")
            L.append(f"- [{a['status']}] **{name}** — corr20 {a['corr20']}, "
                     f"corr60 {a['corr60']}{extra}{cp}. Channel: {a['channel']}")
    except Exception:
        pass

    # ── events ──────────────────────────────────────────────────────────
    L.append("\n## Events (ranked)")
    if not ev["events"]:
        L.append("None — calm session. That is a valid state.")
    for e in ev["events"]:
        k = event_key([m["id"] for m in e["members"]])
        L.append(f"\n### [{e['level'].upper()} {e['score']}] {e['label']}")
        for m in e["members"]:
            L.append(f"- {m['id']} [{m['market']}]: last {_fmt(m.get('last'))}, "
                     f"z20 {_fmt(m.get('z20'))}, zc {_fmt(m.get('zc'))}, "
                     f"resid-z {_fmt(m.get('resid_z'))} "
                     f"[{m.get('move_label', 'n/a')}], 1d {_fmt(m.get('d1_pct'))}%, "
                     f"{'; '.join(m.get('reasons', []))}")
        t = theses.get(k, {}).get("thesis", {})
        if t.get("mechanism"):
            L.append(f"- **Mechanism**: {t['mechanism']}")
        if t.get("gap"):
            L.append(f"- **Gap**: {t['gap']}")
        if t.get("india_take"):
            L.append(f"- **India take**: {t['india_take']}")
        for r in (t.get("responders") or [])[:5]:
            L.append(f"- Watch next: {r.get('id')} ({r.get('expect')}) — "
                     f"{r.get('status')}; {r.get('why', '')}")
        try:
            ind = india_receivers([m["id"] for m in e["members"]], by_id, rel)
            if ind:
                L.append("- **India receivers**: " + "; ".join(
                    f"{x['id']} (rho {x.get('rho')}, z {x.get('z20')})"
                    for x in ind[:4]))
        except Exception:
            pass
        b = bundles.get(k, {})
        for a in (b.get("articles") or [])[:3]:
            if a.get("citation"):
                L.append(f"- Source: {a['citation']}")
        ana = (b.get("analogues") or {}).get("analogues") or []
        if ana:
            L.append("- Historical analogues: " + ", ".join(
                f"{x['date']} (d={x['distance']})" for x in ana[:3]))

    wl = ev.get("watchlist", [])
    if wl:
        L.append("\n## Watchlist (below surfacing floor)")
        L.append(", ".join(f"{w['label']} ({w['score']})" for w in wl[:12]))

    # ── india macro ─────────────────────────────────────────────────────
    L.append("\n## India macro")
    for sid in ("nifty_50", "nifty_midcap_100", "usd_inr", "goi_10y",
                "india_cpi_yoy", "goi_ust_spread", "midcap_largecap_ratio"):
        r = by_id.get(sid)
        if r and r.get("last") is not None:
            L.append(f"- {sid}: {_fmt(r['last'], 4)} (1d {_fmt(r.get('d1_pct'))}%, "
                     f"z20 {_fmt(r.get('z20'))}, flag {r['flag']})")
    try:
        from release_calendar import build_calendar
        cal = build_calendar()
        nxt = [r for r in cal["upcoming"] if r["market"] == "INDIA"][:4]
        L.append("- Next India prints: " + " · ".join(
            f"{r['name']} T-{r['days_until']}d" for r in nxt))
    except Exception:
        pass

    # ── squawk tape ─────────────────────────────────────────────────────
    try:
        from squawk import load_squawk
        items = load_squawk().get("items", [])[:12]
        if items:
            L.append("\n## Squawk (latest wire headlines)")
            for it in items:
                L.append(f"- [{(it.get('ts') or '')[:16]}Z] {it['text'][:180]}")
    except Exception:
        pass

    # ── universe ────────────────────────────────────────────────────────
    members = uni.get("members", {})
    if members:
        L.append("\n## News-tracked universe (why each is watched)")
        for sym, m in sorted(members.items(), key=lambda kv: -kv[1].get("score", 0)):
            ev0 = (m.get("evidence") or [{}])[0]
            L.append(f"- {sym} ({m.get('name', '')[:30]}) score {m.get('score', 0):.1f} — "
                     f"\"{ev0.get('title', '')[:90]}\"")

    # ── owner's thinking ────────────────────────────────────────────────
    try:
        from journal import load_journal
        j = load_journal()
        hyps = [h for h in j.get("hypotheses", []) if not h.get("archived")]
        trades = [t for t in j.get("trades", []) if t.get("status") != "closed"]
        if hyps:
            L.append("\n## Open hypotheses")
            for h in hyps[:8]:
                L.append(f"- {h.get('text', '')[:200]}")
                verdict = (h.get("evaluation") or {}).get("verdict")
                if verdict:
                    L.append(f"  - LLM evaluation verdict: {verdict}")
        if trades:
            L.append("\n## Journal — open trade intents")
            for t in trades[:8]:
                L.append(f"- {t.get('instrument')} {t.get('side')} @ "
                         f"{t.get('level', '?')} — {t.get('rationale', '')[:140]}")
    except Exception:
        pass

    L.append("\n" + METHODOLOGY)
    L.append("\n" + WRITING_PROMPT)
    return "\n".join(L)


def publish_gist(text: str) -> bool:
    """Optional mirror to a Gist (stable public raw URL for auto-fetch).
    Needs GIST_TOKEN (gist-scoped PAT) + GIST_ID. Silently skipped if unset."""
    token = (os.environ.get("GIST_TOKEN") or "").strip()
    gid = (os.environ.get("GIST_ID") or "").strip()
    if not token or not gid:
        return False
    import requests
    try:
        r = requests.patch(
            f"https://api.github.com/gists/{gid}",
            headers={"Authorization": f"Bearer {token}",
                     "Accept": "application/vnd.github+json"},
            json={"files": {"board_brief.md": {"content": text}}}, timeout=20)
        r.raise_for_status()
        return True
    except Exception as e:
        print(f"  WARN gist publish failed: {str(e)[:120]}", file=sys.stderr)
        return False


def main() -> int:
    text = build_brief()
    BRIEF_MD.write_text(text, encoding="utf-8")
    gist = publish_gist(text)
    print(f"brief: {len(text)} chars -> {BRIEF_MD.name}"
          f"{' + gist mirror' if gist else ' (gist mirror off)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
