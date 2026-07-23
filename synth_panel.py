"""SYNTH_V2 · in-app tick (data layer for the read-only board panel).

The cadence split (owner ruling 1): the 2h CI batch is the durable truth; the
3-min in-app tick recomputes the FULL deterministic board (Stages 1-4) on LIVE
prices, reusing the committed channels/bus. This module is Streamlit-free and
testable — app.py wraps `synth_tick` in st.cache_data(ttl=180) and renders.

Live prices: fetch_yf_batch_live upserts a PROVISIONAL last bar per yfinance
series onto the committed matrix; on any failure the committed matrix stands and
`prices_stale=True` (never crash). The LLM is EVENT-TRIGGERED: the tick returns
the surfaced candidate ids so the caller fires Groq only for candidates that are
new vs the prior tick (app-side, zero Actions minutes) — everything else uses
the deterministic scaffold card.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"


def committed_prices() -> pd.DataFrame:
    return pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()


def live_prices(base: pd.DataFrame | None = None) -> tuple[pd.DataFrame, bool, int]:
    """(matrix, prices_stale, n_upserted). Upserts a provisional live bar per
    yfinance series; failures leave the committed matrix and flag stale."""
    prices = committed_prices() if base is None else base.copy()
    try:
        from fetch import fetch_yf_batch_live
        from registry import load_registry
        specs = [s for s in load_registry()
                 if s.get("source") == "yfinance" and s.get("symbol")
                 and s["id"] in prices.columns]
        sym2id = {s["symbol"]: s["id"] for s in specs}
        live = fetch_yf_batch_live(list(sym2id))
    except Exception:
        return prices, True, 0
    if not live:
        return prices, True, 0
    n = 0
    for sym, (bar_date, px) in live.items():
        sid = sym2id.get(sym)
        if not sid:
            continue
        d = pd.Timestamp(bar_date).normalize()
        try:
            prices.loc[d, sid] = float(px)      # provisional row (fresh-wins)
            n += 1
        except Exception:
            continue
    return prices.sort_index(), False, n


def surfaced_ids(board: dict) -> set:
    return {e["instance"] for e in board.get("surfaced", [])}


def synth_tick(client=None, use_live: bool = True) -> dict:
    """Full deterministic board on live prices (Stages 1-4), reusing committed
    channels/bus. `client` fires the LLM; None = deterministic scaffold cards.
    Returns the board plus prices_stale / n_live for the panel header."""
    from synth_detect import build_candidates
    from synth_output import build_board

    if use_live:
        prices, stale, n_live = live_prices()
    else:
        prices, stale, n_live = committed_prices(), False, 0

    # detectors on live prices; committed channels/bus (2h truth); no file write
    cand_state = build_candidates(prices=prices, persist=False)
    board = build_board(candidates_state=cand_state, prices_df=prices,
                        client=client, persist=False)
    board["prices_stale"] = stale
    board["n_live_bars"] = n_live
    return board
