"""Size factors (§8)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.factors.base import Factor, FactorContext, register


class LogFreeFloatMarketCap(Factor):
    """log(free-float market cap). Lower is better (the size premium).

    Banz (1981); Fama & French (1992) for the SMB construction.

    §8 is specific that this must use **free float**, not full market cap.
    Indian promoter holdings run 50-75%, so the two diverge sharply and a
    full-cap size factor is substantially a promoter-holding factor in
    disguise. Both are stored; this one uses float.
    """

    name = "log_free_float_mcap"
    category = "size"
    higher_is_better = False

    def compute(self, ctx: FactorContext) -> pd.Series:
        cap = ctx.free_float_market_cap
        return np.log(cap.where(cap > 0))


class LogMarketCap(Factor):
    """log(full market cap). Stored alongside float cap for comparison (§8)."""

    name = "log_mcap"
    category = "size"
    higher_is_better = False

    def compute(self, ctx: FactorContext) -> pd.Series:
        cap = ctx.market_cap
        return np.log(cap.where(cap > 0))


register(LogFreeFloatMarketCap())
register(LogMarketCap())
