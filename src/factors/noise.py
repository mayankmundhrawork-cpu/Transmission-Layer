"""Seeded-noise control factor (§17 CP8).

A factor with no predictive content by construction. It exists permanently in
the library, not just in the test suite, because it is the calibration check
for the entire evaluation harness: if the harness ever reports this as
significant after correction, the harness is broken and every other result it
has produced is suspect.

The score is a deterministic function of (ISIN, as-of date), so it is stable
across runs — a control that changed every run could not be compared against
its own history — while being independent across dates and names, which is what
makes it genuinely predictively empty.

§17 CP8: "run the harness on a deliberately random factor (seeded noise) and
confirm it reports NOT SIGNIFICANT after correction."
"""
from __future__ import annotations

import hashlib

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register


class SeededNoise(Factor):
    """Deterministic pseudo-random score. No predictive content by construction."""

    name = "seeded_noise"
    category = "control"

    def __init__(self, seed: int = 20240101) -> None:
        self.seed = seed

    def compute(self, ctx: FactorContext) -> pd.Series:
        values = {}
        for isin in ctx.universe:
            # Hash the (seed, date, isin) triple so the value is reproducible
            # but carries no information about anything.
            digest = hashlib.sha256(
                f"{self.seed}|{ctx.as_of_date}|{isin}".encode()
            ).digest()
            draw = int.from_bytes(digest[:8], "big") / 2 ** 64
            values[isin] = float(draw)
        return pd.Series(values, dtype="float64")


class LookAheadCanary(Factor):
    """DIAGNOSTIC ONLY — a factor that would be significant if the harness leaked.

    Scores each name by its own forward return, which the platform makes
    impossible to obtain: `FactorContext` is bounded at the as-of date and
    exposes no future data. So this factor computes to all-NaN, and a run
    against it reports nothing.

    Its purpose is the inverse of the noise control. Noise checks that the
    harness does not manufacture significance from nothing; this checks that the
    harness *could* detect significance if it were there — and, more usefully,
    that there is no accessible path to future returns. If this factor ever
    produces non-NaN scores, something has handed research code a time machine.
    """

    name = "lookahead_canary"
    category = "control"

    def compute(self, ctx: FactorContext) -> pd.Series:
        # There is deliberately no way to ask the context for anything after
        # ctx.as_of_date, so this can only ever return NaN.
        future = ctx.closes.loc[ctx.closes.index > pd.Timestamp(ctx.as_of_date)]
        if future.empty:
            return pd.Series(np.nan, index=pd.Index(ctx.universe), dtype="float64")
        return future.iloc[-1] / ctx.last_close - 1.0  # pragma: no cover


register(SeededNoise())
register(LookAheadCanary())
