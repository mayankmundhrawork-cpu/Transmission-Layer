"""SYNTH_V2 · S4 — base-rate reconstruction (matching rule + outcome).

The setup IS the live detector predicate re-run on strictly-prior data. For
each historical driver-event date t this module rebuilds the channel state
POINT-IN-TIME (synth_channels.build_channels on prices.loc[:t] — never today's
channels.json, section A of S4_METHODOLOGY.md) and calls the unchanged
synth_detect.detect_transmission_gaps on prices.loc[:t]. Whatever it returns is
the reconstructed trigger population — the same object the live board emits,
graded on data it could actually have seen at t.

The OUTCOME ("did the gap close?") is the only forward-looking quantity and is
never a trigger input: from t+1..t+K (K = clamp(lead_lag,5,15)) the target's
cumulative return is projected onto the implied direction; CLOSED = it catches
>= CLOSE_FRAC of the outstanding gap (both 0.5 and 1.0 stored), first-touch,
with time-to-touch. A material against-move separates FADED_AGAINST from
FADED_FLAT.

THIS FILE COMPUTES NO HEADLINE HIT RATE YET. `python synth_baserates.py` runs
the reconstruction AUDIT: trigger population + resolved outcomes on a few
pairs, so the outcome definition can be checked on the rows before any rate is
aggregated (owner gate).
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

K_MIN, K_MAX = 5, 15          # resolution horizon clamp (sessions)
CLOSE_FRACS = (0.5, 1.0)      # headline 0.5, purist 1.0 — store both
AGAINST_FRAC = 0.5            # against-move this large => FADED_AGAINST
CENSOR_MIN_FRAC = 0.6         # need this fraction of K valid forward obs to
#                               call a FADE; else the window is right-censored
#                               (matrix edge or data gaps) — never a fade.
#                               A close that already happened still counts.


def driver_event_dates(prices: pd.DataFrame, driver: str) -> list:
    """Every session t where the live market adapter would have fired on the
    driver, judged PIT (its own |zc| history strictly before t)."""
    from conditional import zc_frame
    from synth_events import _move_event
    if driver not in prices.columns:
        return []
    zc = zc_frame(prices, [driver])
    if driver not in zc.columns:
        return []
    s = zc[driver].dropna()
    r = prices[driver].pct_change(fill_method=None)
    out = []
    for pos in range(len(s)):
        e = _move_event(driver, s, r, pos)
        if e is not None:
            out.append((s.index[pos], e))
    return out


def resolve_outcome(prices: pd.DataFrame, trig: dict) -> dict:
    """Grade a trigger forward. Outstanding gap = expected - realised-at-t;
    caught(k) = target cum return t+1..t+k projected onto the implied dir."""
    tgt = trig["target"]
    t = pd.Timestamp(trig["asof"])
    lead = int(trig.get("lead_lag") or 1)
    K = int(min(max(lead, K_MIN), K_MAX))
    idx = prices.index
    if t not in idx or tgt not in prices.columns:
        return {"outcome": "NO_DATA", "K": K}
    pos = idx.get_loc(t)
    avail = len(idx) - 1 - pos                       # sessions after t on matrix
    fwd = prices[tgt].pct_change(fill_method=None).iloc[pos + 1:pos + 1 + K]
    expected = trig["expected_pct"] / 100.0
    realized0 = trig["actual_pct"] / 100.0
    gap = expected - realized0                      # outstanding implied move
    gap_mag = abs(gap)
    idir = trig["implied_dir"]
    cum, c05, c10, against, path = 1.0, None, None, False, []
    for k, r in enumerate(fwd.to_numpy(), 1):
        if np.isnan(r):
            path.append(None)
            continue
        cum *= (1.0 + r)
        caught = float((cum - 1.0) * idir)
        path.append(round(caught * 100, 3))
        if gap_mag > 0:
            if c05 is None and caught >= CLOSE_FRACS[0] * gap_mag:
                c05 = k
            if c10 is None and caught >= CLOSE_FRACS[1] * gap_mag:
                c10 = k
            if caught <= -AGAINST_FRAC * gap_mag:
                against = True
    n = sum(1 for p in path if p is not None)
    # right-censoring (point B applied to history): a window that ran off the
    # matrix (avail<K) or is too sparse (n<0.6K) cannot be called a fade — we
    # don't know if it would have closed. A close that already fired counts.
    censored = min(avail, K) < K or n < CENSOR_MIN_FRAC * K
    outcome = ("CLOSED" if c05 else
               "CENSORED" if censored else
               "FADED_AGAINST" if against else
               "FADED_FLAT")
    return {"K": K, "window_n": n, "avail_sessions": int(avail),
            "gap_pct": round(gap * 100, 3),
            "closed_05": bool(c05), "closed_10": bool(c10),
            "ttt_05": c05, "ttt_10": c10, "outcome": outcome,
            "caught_path_pct": path}


def _filter_relations(relations: dict, drivers: set) -> dict:
    """Only pairs whose leader (driver) is in `drivers` — keeps the PIT
    channel rebuild cheap for a targeted reconstruction."""
    pairs = [p for p in relations.get("pairs", [])
             if p.get("leader") in drivers or p.get("follower") in drivers]
    return {**relations, "pairs": pairs}


def reconstruct(prices: pd.DataFrame, drivers: list, relations: dict,
                full_floor: bool = True, timing_out: list | None = None) -> list:
    """Reconstructed trigger population for `drivers` with forward outcomes.
    full_floor=True rebuilds ALL channels PIT so the cross-sectional strength
    floor is exact; False restricts to the drivers' pairs (faster, floor
    approximate — only safe for strong audit pairs). If `timing_out` is given,
    (date, seconds) is appended per event-date so the per-date cost can be
    profiled (flat = healthy; growth toward recent dates = accidental O(n^2))."""
    import time as _time
    from synth_channels import build_channels
    from synth_detect import detect_transmission_gaps

    rel = relations if full_floor else _filter_relations(relations, set(drivers))
    by_date: dict[pd.Timestamp, list] = defaultdict(list)
    for drv in drivers:
        for t, e in driver_event_dates(prices, drv):
            by_date[t].append(e)

    keep = ("id", "kind", "asof", "driver", "target", "driver_class",
            "target_class", "beta_pair", "expected_pct", "actual_pct",
            "residual_sigma", "shortfall_sigma", "gap_bar_sigma", "implied_dir",
            "channel_state", "channel_rho", "channel_stability", "lead_lag")
    triggers = []
    for t in sorted(by_date):
        t0 = _time.monotonic()
        pt = prices.loc[:t]
        ch = build_channels(pt, relations=rel, changepoints=False,
                            persist=False)["channels"]
        gaps = detect_transmission_gaps(pt, ch, by_date[t], [])
        for g in gaps:
            if g["driver"] not in drivers:
                continue
            row = {k: g[k] for k in keep}
            row.update(resolve_outcome(prices, g))
            row["beta_pit"] = g["beta_pair"]     # PIT beta used (section A)
            triggers.append(row)
        if timing_out is not None:
            timing_out.append((f"{t:%Y-%m-%d}", round(_time.monotonic() - t0, 3)))
    return triggers


# ── coverage (owner gate: denominators before any pooled rate) ───────────
def _session_ord(prices: pd.DataFrame) -> dict:
    return {d: i for i, d in enumerate(prices.index)}


def cluster_labels(trigs: list, sess_ord: dict) -> list:
    """Connected-component label per trigger via a SINGLE union-find over the
    three correlated-outcome structures the audit exposed:
      (1) same (driver, date)  — fan-out (one pulse, many targets)
      (2) same (target, date)  — shared target path (the hy_oas case: two
                                 drivers, one target-date, ONE outcome)
      (3) same (driver, target) within K_MAX sessions — overlapping windows

    The closure is TRANSITIVE ACROSS AXES BY DESIGN: all edges feed one
    union-find, so if A~B on driver-date and B~C on target-date, A-B-C become
    one component even though A and C share nothing directly. This is correct —
    they are linked through a common outcome path and are not independent draws
    — and it means the clustered N is LOWER than a naive per-axis minimum: one
    dense driver-date can transitively swallow a large component. Conservative
    by construction (owner: rather INSUFFICIENT than an inflated numerator)."""
    n = len(trigs)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    by_dd, by_td, by_ch = defaultdict(list), defaultdict(list), defaultdict(list)
    for i, t in enumerate(trigs):
        by_dd[(t["driver"], t["asof"])].append(i)
        by_td[(t["target"], t["asof"])].append(i)
        by_ch[(t["driver"], t["target"])].append(i)
    for grp in list(by_dd.values()) + list(by_td.values()):
        for j in grp[1:]:
            union(grp[0], j)
    for idxs in by_ch.values():
        idxs.sort(key=lambda i: trigs[i]["asof"])
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                oa = sess_ord.get(pd.Timestamp(trigs[idxs[a]]["asof"]))
                ob = sess_ord.get(pd.Timestamp(trigs[idxs[b]]["asof"]))
                if oa is not None and ob is not None and abs(oa - ob) < K_MAX:
                    union(idxs[a], idxs[b])
    roots = [find(i) for i in range(n)]
    relabel = {r: k for k, r in enumerate(dict.fromkeys(roots))}
    return [relabel[r] for r in roots]


def cluster_count(trigs: list, sess_ord: dict) -> int:
    return len(set(cluster_labels(trigs, sess_ord))) if trigs else 0


def build_coverage(prices=None, relations=None, n_min: int = 8) -> dict:
    """Reconstruct over the FULL driver universe and report, per pooling level,
    raw trigger count vs independent-cluster count vs their ratio, and whether
    the level clears N_MIN on CLUSTERS (not rows). No pooled rate is computed —
    this is the denominator audit that decides whether a rate is even honest."""
    if prices is None:
        prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                             parse_dates=True).sort_index()
    if relations is None:
        from relations import load_relations
        relations = load_relations()
    import json
    drivers = sorted({p["leader"] for p in relations["pairs"]} |
                     {p["follower"] for p in relations["pairs"]})
    timing: list = []
    trg = reconstruct(prices, drivers, relations, full_floor=True,
                      timing_out=timing)
    gradeable = [t for t in trg if t["outcome"] in
                 ("CLOSED", "FADED_FLAT", "FADED_AGAINST")]
    sess = _session_ord(prices)

    # global connected-component id per gradeable trigger — materialised so any
    # drill-down (a cluster's members) is a cheap read, never a 35-min recompute
    glabels = cluster_labels(gradeable, sess)
    for t, lab in zip(gradeable, glabels):
        t["global_cluster"] = lab
        t["k_dd"] = f"{t['driver']}|{t['asof']}"     # axis keys for inspection
        t["k_td"] = f"{t['target']}|{t['asof']}"
        t["k_ch"] = f"{t['driver']}|{t['target']}"
    # timing profile: flat is healthy, growth toward recent dates is a smell
    secs = [s for _, s in timing]
    third = max(1, len(secs) // 3)
    timing_profile = {
        "n_dates": len(timing), "total_s": round(sum(secs), 1),
        "per_date_min_s": round(min(secs), 3) if secs else None,
        "per_date_max_s": round(max(secs), 3) if secs else None,
        "first_third_avg_s": round(sum(secs[:third]) / third, 3) if secs else None,
        "last_third_avg_s": round(sum(secs[-third:]) / third, 3) if secs else None,
    }

    def level_row(trigs):
        raw = len(trigs)
        cl = cluster_count(trigs, sess) if trigs else 0
        return {"raw": raw, "clusters": cl,
                "ratio": round(raw / cl, 2) if cl else None,
                "clears_n_min": cl >= n_min}

    # global
    glob = level_row(gradeable)
    # class-pair
    by_cp = defaultdict(list)
    for t in gradeable:
        by_cp[(t["driver_class"], t["target_class"])].append(t)
    class_pairs = {f"{a}->{b}": level_row(ts) for (a, b), ts in
                   sorted(by_cp.items(), key=lambda kv: -len(kv[1]))}
    # pair
    by_pair = defaultdict(list)
    for t in gradeable:
        by_pair[(t["driver"], t["target"])].append(t)
    pair_rows = {f"{a}->{b}": level_row(ts) for (a, b), ts in by_pair.items()}
    pairs_clearing = [k for k, v in pair_rows.items() if v["clears_n_min"]]
    top_pairs = sorted(pair_rows.items(), key=lambda kv: -kv[1]["clusters"])[:6]

    # worked example: the hy_oas same-target-date collapse
    hy = [t for t in gradeable if t["target"] == "hy_oas"]
    hy_dates = defaultdict(list)
    for t in hy:
        hy_dates[t["asof"]].append(t["driver"])
    worked = {d: drv for d, drv in hy_dates.items() if len(drv) > 1}

    cov = {
        "data_window": f"{prices.index.min():%Y-%m-%d}..{prices.index.max():%Y-%m-%d}",
        "n_min": n_min, "n_drivers": len(drivers),
        "triggers_raw": len(trg),
        "triggers_censored": sum(1 for t in trg if t["outcome"] == "CENSORED"),
        "triggers_gradeable": len(gradeable),
        "clustering": "transitive union-find across (driver,date)+(target,date)"
                      "+(same-channel within K_MAX); clustered N is <= per-axis min",
        "timing_profile": timing_profile,
        "global": glob,
        "class_pair": class_pairs,
        "pair_level": {
            "n_pairs": len(pair_rows),
            "pairs_clearing_n_min_on_clusters": pairs_clearing,
            "top_pairs_by_clusters": {k: v for k, v in top_pairs},
        },
        "worked_collapse_hy_oas": worked,
    }
    synth = DATA_DIR / "synth"
    (synth / "coverage.json").write_text(json.dumps(cov, indent=2),
                                         encoding="utf-8")
    # full per-trigger population (incl. censored) — materialise once, query
    # many; every follow-up about the table is a read against this file
    (synth / "reconstruction_population.json").write_text(
        json.dumps({"data_window": cov["data_window"],
                    "n_triggers": len(trg), "triggers": trg}, indent=2),
        encoding="utf-8")
    return cov


# ── viability verdict (pre-registered reading lens, owner sign-off) ──────
N_MIN_DEFAULT = 8
RATIO_VETO = 2.0     # a level clearing N_MIN but with raw:cluster worse than
#                      this is fan-out inflating toward the floor from below —
#                      CONDITIONAL at best, never a clean CLEAR (rule fixed
#                      BLIND, before the numbers, so the ratio column decides
#                      viability and a reassuring numerator can't move it).


def _verdict(row: dict, n_min: int, ratio_veto: float) -> str:
    if row["clusters"] < n_min:
        return "INSUFFICIENT"
    if row["ratio"] is not None and row["ratio"] > ratio_veto:
        return "CONDITIONAL"      # clears on count, vetoed by fan-out ratio
    return "CLEAR"


def viability_table(pop_path: Path | str | None = None,
                    n_min: int = N_MIN_DEFAULT,
                    ratio_veto: float = RATIO_VETO) -> dict:
    """Read the materialised population (NO reconstruction) and, per class-pair
    setup family, report the tightest level that clears N_MIN on CLUSTERS with
    its raw:cluster ratio and the pre-registered verdict. The taxonomy is the
    registry `market` field UNCHANGED — never coarsened at the pooling layer to
    rescue a cell (that would be the exposure-feed temptation in a new costume).
    """
    import json
    p = Path(pop_path) if pop_path else DATA_DIR / "synth" / "reconstruction_population.json"
    pop = json.loads(p.read_text(encoding="utf-8"))
    trg = pop["triggers"]
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()
    sess = _session_ord(prices)
    gradeable = [t for t in trg if t["outcome"] in
                 ("CLOSED", "FADED_FLAT", "FADED_AGAINST")]

    def row(ts):
        raw = len(ts)
        cl = cluster_count(ts, sess)
        r = round(raw / cl, 2) if cl else None
        d = {"raw": raw, "clusters": cl, "ratio": r}
        d["verdict"] = _verdict(d, n_min, ratio_veto)
        return d

    glob = row(gradeable)
    # global is the COARSEST bucket — it pools INDICES->INDICES with FX->FX
    # etc. into one "all-transmission" reference class with no shared mechanism.
    # It answers "do cross-asset setups in general resolve," never a claim about
    # the specific setup on the board. So it is CAPPED at CONDITIONAL: a
    # last-resort reference class, never a clean CLEAR (owner ruling — enforced
    # verdict, not a qualifier a reader must notice).
    if glob["verdict"] == "CLEAR":
        glob["verdict"] = "CONDITIONAL"
        glob["capped"] = "global_is_last_resort_bucket"
    by_cp, by_pair = defaultdict(list), defaultdict(list)
    for t in gradeable:
        by_cp[(t["driver_class"], t["target_class"])].append(t)
        by_pair[(t["driver"], t["target"])].append(t)
    pair_rows = {pr: row(ts) for pr, ts in by_pair.items()}

    families = {}
    for (dc, tc), ts in sorted(by_cp.items(), key=lambda kv: -len(kv[1])):
        cp = row(ts)
        # pairs inside this class-pair that clear at pair-level (expected ~none)
        pairs_in = [pr for pr in pair_rows if market_class(pr[0]) == dc
                    and market_class(pr[1]) == tc]
        pair_clears = [f"{a}->{b}" for (a, b) in pairs_in
                       if pair_rows[(a, b)]["verdict"] == "CLEAR"]
        # tightest clearing level for a candidate in this family: pair -> cp ->
        # global -> INSUFFICIENT
        if pair_clears:
            headline = "pair"
        elif cp["verdict"] != "INSUFFICIENT":
            headline = "class_pair"
        elif glob["verdict"] != "INSUFFICIENT":
            headline = "global"
        else:
            headline = "none"
        families[f"{dc}->{tc}"] = {
            "class_pair": cp,
            "n_pairs": len(pairs_in),
            "pairs_clearing_at_pair_level": pair_clears,
            "headline_level": headline,
            "headline_verdict": (cp["verdict"] if headline == "class_pair"
                                 else glob["verdict"] if headline == "global"
                                 else "CLEAR" if headline == "pair"
                                 else "INSUFFICIENT"),
        }
    return {"n_min": n_min, "ratio_veto": ratio_veto,
            "global": glob, "families": families}


def market_class(sid: str) -> str | None:
    from synth_classes import market_of
    return market_of(sid)


# ── pooled hit rates (cluster-as-unit) + display contract ────────────────
def _wilson(k: int, n: int, z: float = 1.96) -> tuple:
    """Wilson 95% interval for k/n. n is the CLUSTER count (effective sample),
    never the raw trigger count."""
    if n == 0:
        return (None, None, None)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = (z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)) / d
    return (round(p, 3), round(max(0.0, centre - half), 3),
            round(min(1.0, centre + half), 3))


EDGE_LB_MIN = 0.5    # a CLEAR (sample-adequate) family whose Wilson LOWER bound
#                      is below this is not distinguishable from a coin flip —
#                      no demonstrated edge, regardless of a friendly midpoint.
#                      Adequacy and edge are ORTHOGONAL gates (owner): enough
#                      episodes to HAVE a rate does not mean the rate is signal.


def edge_finding(rate05: dict, miss: dict) -> dict:
    """The practitioner-facing conclusion, separate from sample adequacy. If the
    Wilson lower bound sits below a coin flip AND the misses skew AGAINST the
    implied direction, the honest surface is NOT the rate — it is 'no reliable
    edge; the misses hurt', with the rate and skew shown as the EVIDENCE for
    that verdict (never laundered into a percentage that looks like signal)."""
    lo = rate05["wilson95"][0]
    against, flat = miss["faded_against"], miss["faded_flat"]
    against_dom = against > flat
    if lo is None:
        return {"finding": "INSUFFICIENT", "basis": "no episodes"}
    if lo < EDGE_LB_MIN and against_dom:
        return {"finding": "NO_RELIABLE_EDGE",
                "basis": f"Wilson lower bound {lo} < {EDGE_LB_MIN} (indistinct "
                         f"from a coin flip) AND misses against-dominated "
                         f"({against} against vs {flat} flat) — this reference "
                         f"class does not reliably transmit and the misses skew "
                         f"against the implied direction (they lose, not merely "
                         f"fail to gain)."}
    if lo < EDGE_LB_MIN:
        return {"finding": "NO_DEMONSTRATED_EDGE",
                "basis": f"Wilson lower bound {lo} < {EDGE_LB_MIN} — no edge "
                         f"demonstrable at this sample; misses are flat-"
                         f"dominated ({flat} flat vs {against} against), so "
                         f"benign rather than adverse."}
    return {"finding": "PROVISIONAL_EDGE",
            "basis": f"Wilson lower bound {lo} >= {EDGE_LB_MIN} — a demonstrable "
                     f"lean even at the floor; still an interval, not a point."}


def _episode_category(legs: list) -> str:
    """One 3-way outcome per independent episode by majority vote of its legs:
    CLOSED (>=0.5 threshold) else the dominant miss type. FADED_AGAINST is the
    dangerous miss — the target drifts against the implied direction, where a
    practitioner acting on the rate actually loses, not merely fails to gain."""
    if sum(l["closed_05"] for l in legs) * 2 >= len(legs):
        return "CLOSED"
    against = sum(1 for l in legs if l["outcome"] == "FADED_AGAINST")
    flat = sum(1 for l in legs if l["outcome"] == "FADED_FLAT")
    return "FADED_AGAINST" if against >= flat else "FADED_FLAT"


def family_clusters(gradeable: list, sess_ord: dict, dc: str, tc: str) -> list:
    """Clusters for one class-pair family, each with member legs and episode
    outcomes at BOTH thresholds (0.5 and 1.0) plus a 3-way category — the rate
    is one observation per INDEPENDENT episode, not per correlated leg."""
    fam = [t for t in gradeable if t["driver_class"] == dc
           and t["target_class"] == tc]
    if not fam:
        return []
    labels = cluster_labels(fam, sess_ord)
    groups: dict[int, list] = defaultdict(list)
    for t, lab in zip(fam, labels):
        groups[lab].append(t)
    out = []
    for lab, legs in groups.items():
        out.append({
            "cluster": lab, "n_legs": len(legs),
            "episode_closed_05": sum(l["closed_05"] for l in legs) * 2 >= len(legs),
            "episode_closed_10": sum(l["closed_10"] for l in legs) * 2 >= len(legs),
            "category": _episode_category(legs),
            "legs": [{"driver": l["driver"], "target": l["target"],
                      "date": l["asof"], "outcome": l["outcome"],
                      "closed_05": l["closed_05"], "closed_10": l["closed_10"],
                      "ttt_05": l["ttt_05"], "ttt_10": l["ttt_10"],
                      "gap_pct": l.get("gap_pct")}
                     for l in legs],
        })
    return out


def family_rate(gradeable: list, sess_ord: dict, dc: str, tc: str) -> dict:
    """Episode-level hit rate at BOTH thresholds with Wilson CI on the CLUSTER
    count, and the miss column split into flat vs against. The headline is the
    INTERVAL, not the point estimate; the 0.5-vs-1.0 gap is the shape of
    resolution; against-fades are the real downside risk."""
    cl = family_clusters(gradeable, sess_ord, dc, tc)
    n = len(cl)
    k05 = sum(1 for c in cl if c["episode_closed_05"])
    k10 = sum(1 for c in cl if c["episode_closed_10"])
    p05, lo05, hi05 = _wilson(k05, n)
    p10, lo10, hi10 = _wilson(k10, n)
    cats = [c["category"] for c in cl]
    legs = [l for c in cl for l in c["legs"]]
    rate_05 = {"closed": k05, "point": p05, "wilson95": [lo05, hi05]}
    miss = {"faded_flat": cats.count("FADED_FLAT"),
            "faded_against": cats.count("FADED_AGAINST")}
    return {
        "class_pair": f"{dc}->{tc}", "clusters": n,
        "rate_05": rate_05,
        "rate_10": {"closed": k10, "point": p10, "wilson95": [lo10, hi10]},
        "miss_split_episodes": miss,
        "edge": edge_finding(rate_05, miss),
        "leg_level": {"n": len(legs),
                      "closed_05": sum(l["closed_05"] for l in legs),
                      "closed_10": sum(l["closed_10"] for l in legs),
                      "faded_against": sum(1 for l in legs
                                           if l["outcome"] == "FADED_AGAINST"),
                      "faded_flat": sum(1 for l in legs
                                        if l["outcome"] == "FADED_FLAT")},
        "clusters_detail": cl}


def base_rate_record(driver: str, target: str, pop: dict | None = None,
                     n_min: int = N_MIN_DEFAULT,
                     ratio_veto: float = RATIO_VETO) -> dict:
    """DISPLAY CONTRACT: resolve the base rate for a live (driver -> target)
    candidate. Back-off pair -> class-pair -> global(CONDITIONAL) ->
    INSUFFICIENT. The record ALWAYS carries `frame: reference_class` (never a
    per-instance claim, section B) and, when INSUFFICIENT, its own denominators
    so the absence of a rate defends itself — a bare INSUFFICIENT invites a
    later 'fix' by loosening a bucket; one that shows '3 episodes in 2y, below
    the 8-cluster floor' does not."""
    import json
    if pop is None:
        p = DATA_DIR / "synth" / "reconstruction_population.json"
        pop = json.loads(p.read_text(encoding="utf-8"))
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()
    sess = _session_ord(prices)
    grad = [t for t in pop["triggers"] if t["outcome"] in
            ("CLOSED", "FADED_FLAT", "FADED_AGAINST")]
    dc, tc = market_class(driver), market_class(target)
    window = pop.get("data_window", "")

    def rate_at(subset, level, cap_conditional=False):
        n = cluster_count(subset, sess)
        raw = len(subset)
        ratio = round(raw / n, 2) if n else None
        if n < n_min:
            return {"level": level, "verdict": "INSUFFICIENT",
                    "frame": "reference_class", "clusters": n, "raw": raw,
                    "ratio": ratio,
                    "basis": f"{level} reference class: {n} independent "
                             f"episodes ({raw} legs) over {window}, below the "
                             f"{n_min}-cluster floor. Too rare to rate."}
        verdict = "CONDITIONAL" if (cap_conditional or
                                    (ratio and ratio > ratio_veto)) else "CLEAR"
        extra = {}
        if level.startswith("class_pair"):
            fr = family_rate(grad, sess, dc, tc)
            r05, r10 = fr["rate_05"], fr["rate_10"]
            rate, ci = r05["point"], r05["wilson95"]
            # edge is a SECOND gate: a sample-adequate family can still be a
            # coin flip. The practitioner-facing finding is the edge verdict.
            extra = {"rate_10": r10, "miss_split_episodes": fr["miss_split_episodes"],
                     "edge": fr["edge"]}
        else:
            labels = cluster_labels(subset, sess)
            groups: dict[int, list] = defaultdict(list)
            for t, lab in zip(subset, labels):
                groups[lab].append(t)
            k = sum(1 for legs in groups.values()
                    if sum(l["closed_05"] for l in legs) * 2 >= len(legs))
            rate, lo, hi = _wilson(k, n)
            ci = [lo, hi]
        return {"level": level, "verdict": verdict, "frame": "reference_class",
                "clusters": n, "raw": raw, "ratio": ratio,
                # headline is the INTERVAL; point estimate lives inside it
                "rate_point": rate, "wilson95": ci, **extra,
                "basis": f"{level} reference class, N={n} independent episodes, "
                         f"Wilson95 {ci}, raw:cluster {ratio}:1"
                         f"{' (fan-out vetoed)' if verdict=='CONDITIONAL' and ratio and ratio>ratio_veto else ''}."}

    pair = [t for t in grad if t["driver"] == driver and t["target"] == target]
    r = rate_at(pair, f"pair {driver}->{target}")
    if r["verdict"] != "INSUFFICIENT":
        return {"instance": f"{driver}->{target}", **r}
    cp = [t for t in grad if t["driver_class"] == dc and t["target_class"] == tc]
    r = rate_at(cp, f"class_pair {dc}->{tc}")
    if r["verdict"] != "INSUFFICIENT":
        return {"instance": f"{driver}->{target}", **r}
    r = rate_at(grad, "global", cap_conditional=True)   # last resort
    return {"instance": f"{driver}->{target}", **r}


# ── audit (owner gate: check CLOSED-calling before any rate) ─────────────
def _counter_move_exclusion_demo(prices, relations):
    """Show the ruling-6 counter-move logic refusing to score dyn_gs->dyn_mu on
    the Goldman event date: detect emits NO trigger, and the target's forward
    path runs AWAY from the implied direction — a false laggard correctly
    never counted."""
    from synth_channels import build_channels
    from synth_detect import detect_transmission_gaps
    drv, tgt = "dyn_gs", "dyn_mu"
    evs = driver_event_dates(prices, drv)
    if not evs:
        return
    t, e = evs[-1]
    pt = prices.loc[:t]
    ch = build_channels(pt, relations=_filter_relations(relations, {drv}),
                        changepoints=False, persist=False)["channels"]
    gaps = detect_transmission_gaps(pt, ch, [e], [])
    emitted = any(g["target"] == tgt for g in gaps)
    # what the trigger WOULD have claimed, and where the target actually went
    from synth_channels import pair_beta_series
    r = prices.pct_change(fill_method=None)
    beta = pair_beta_series(r, drv, tgt).reindex(prices.index)
    pos = prices.index.get_loc(t)
    exp = float(beta.iloc[pos] * r[drv].iloc[pos]) * 100
    day0 = float(r[tgt].iloc[pos]) * 100
    fwd5 = float((1 + r[tgt].iloc[pos + 1:pos + 6].dropna()).prod() - 1) * 100
    print(f"\nCOUNTER-MOVE EXCLUSION (ruling 6) — {drv} -> {tgt} @ {t:%Y-%m-%d}")
    print(f"  implied (beta*drv_ret) = {exp:+.2f}%  | target day0 = {day0:+.2f}%"
          f"  | target next-5d = {fwd5:+.2f}%")
    print(f"  detector emitted a trigger for this pair: {emitted}  "
          f"(expected: False)")
    print(f"  -> target moved HARD against the implied +{exp:.0f}%; it is the "
          f"target's own story, not a laggard. Never scored as a close.")


def audit():
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()
    from relations import load_relations
    rel = load_relations()

    drivers = ["sp500", "stoxx_50", "dax", "nikkei_225", "bovespa", "cac_40",
               "brent", "wti", "dxy", "ust_10y", "india_vix", "hy_oas"]
    print(f"reconstruction audit over {prices.index.min():%Y-%m-%d}.."
          f"{prices.index.max():%Y-%m-%d}  drivers={drivers}")
    trg = reconstruct(prices, drivers, rel, full_floor=False)
    graded = [t for t in trg if t["outcome"] in
              ("CLOSED", "FADED_FLAT", "FADED_AGAINST")]
    censored = [t for t in trg if t["outcome"] == "CENSORED"]
    n_closed = sum(t["closed_05"] for t in graded)
    print(f"triggers reconstructed: {len(trg)} | gradeable: {len(graded)} "
          f"| right-censored (excluded): {len(censored)} | CLOSED@0.5: "
          f"{n_closed} | (NO rate computed — audit only)")

    def show(t):
        print(f"  {t['driver']:>10} -> {t['target']:<16} {t['asof']} "
              f"K={t['K']:>2} exp={t['expected_pct']:+6.2f}% "
              f"day0={t['actual_pct']:+6.2f}% gap={t['gap_pct']:+6.2f}% "
              f"short={t['shortfall_sigma']:.2f}s n={t['window_n']} "
              f"{t['outcome']:13} ttt05={t['ttt_05']} ttt10={t['ttt_10']} "
              f"path%={t['caught_path_pct']}")

    closes = sorted((t for t in graded if t["closed_05"]),
                    key=lambda t: (t["ttt_05"] or 99))
    print("\nGENUINE CLOSES (first-touch early = clean transmission):")
    for t in closes[:3]:
        show(t)
    near = [t for t in closes if t["ttt_05"] and t["ttt_05"] >= t["K"] - 1]
    print("\nFIRST-TOUCH LATE IN THE WINDOW (drift warning — ttt near K):")
    for t in (near[:2] or [None]):
        show(t) if t else print("  (none — this macro set has short "
                                "lead-lags so K floored at 5)")
    fades = [t for t in graded if not t["closed_05"]]
    print("\nFADES (full window available, target did NOT close):")
    for t in fades[:3]:
        show(t)
    print("\nRIGHT-CENSORED (near matrix edge / too sparse — NOT graded as "
          "fades; incl. the golden-day bovespa legs):")
    for t in censored[:4]:
        show(t)

    _counter_move_exclusion_demo(prices, rel)


if __name__ == "__main__":
    audit()
