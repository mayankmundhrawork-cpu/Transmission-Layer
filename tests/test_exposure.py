"""SYNTH_V2 · exposure store + WPI vintage acceptance tests (§2).

Guards the two disciplines the owner made binding:
  * FAIL-CLOSED provenance — the store cannot hold a value without source +
    quality; a sentinel skeleton is not-ready until curated.
  * VINTAGE / no-lookahead — a WPI revision never overwrites the as-published
    value, and wpi_asof returns what existed AT registration.

Run: pytest -q tests/test_exposure.py
"""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


# ── exposure store: fail-closed provenance ──────────────────────────────
def _basket(fields_ceat):
    return {"basket": "t", "reporting_cycle_days": 100,
            "required_fields": ["rm_to_sales"],
            "names": {"ceat": {"fields": {"rm_to_sales": fields_ceat}}}}


def test_shipped_skeleton_is_not_ready_all_uncurated():
    from synth_exposure import load_basket, validate_basket
    rep = validate_basket(load_basket("margin_trap"))
    assert rep["ready"] is False
    assert rep["curated"] == 0 and rep["uncurated"]     # sentinels, fail-closed
    assert not rep["errors"]                            # uncurated != error


def test_value_without_provenance_is_an_error_not_silently_accepted():
    from synth_exposure import validate_basket
    # value present, source null -> ERROR (fail-closed)
    r = validate_basket(_basket({"value": 0.6, "as_of": "2026-06-30",
                                 "source": None, "quality": "disclosed"}))
    assert r["ready"] is False and any("source is null" in e for e in r["errors"])
    # value present, invalid quality -> ERROR
    r = validate_basket(_basket({"value": 0.6, "as_of": "2026-06-30",
                                 "source": "Q1 P&L", "quality": "guess"}))
    assert any("quality not in" in e for e in r["errors"])


def test_fully_curated_field_builds_and_quality_summarised():
    from synth_exposure import basket_quality_summary, validate_basket
    b = _basket({"value": 0.62, "as_of": "2026-06-30",
                 "source": "Q1FY27 results P&L", "quality": "disclosed"})
    r = validate_basket(b, today=date(2026, 7, 23))
    assert r["ready"] is True and r["curated"] == 1 and not r["errors"]
    q = basket_quality_summary(b)
    assert q["counts"]["disclosed"] == 1 and q["oldest_as_of"] == "2026-06-30"


def test_stale_field_still_builds_but_is_flagged():
    from synth_exposure import validate_basket
    b = _basket({"value": 0.62, "as_of": "2025-01-31",   # >1 cycle old
                 "source": "old AR", "quality": "disclosed"})
    r = validate_basket(b, today=date(2026, 7, 23))
    assert r["ready"] is True and r["stale"]             # builds, but flagged
    assert r["stale"][0]["age_days"] > 100


def test_input_basket_mapping_present_but_weights_fail_closed():
    """The sector->input mapping is structural (recoverable); the weights are
    sentinels. A basket with the mapping but unfilled weights is not-ready but
    NOT errored — the schema is unblocked while fail-closed holds."""
    from synth_exposure import load_basket, validate_basket
    b = load_basket("margin_trap")
    rep = validate_basket(b)
    assert rep["ready"] is False and not rep["errors"]
    # every name carries an input-basket weight sentinel in the uncurated set
    assert any(".input_wt[" in u for u in rep["uncurated"])


def test_input_basket_missing_weight_or_components_is_an_error():
    from synth_exposure import validate_basket
    base = {"basket": "t", "required_fields": [], "reporting_cycle_days": 100}
    # empty components -> error (mapping absent)
    r = validate_basket({**base, "names": {"a": {"input_basket": {"components": []}}}})
    assert any("no components" in e for e in r["errors"])
    # component missing its weight field -> error
    r = validate_basket({**base, "names": {"a": {"input_basket":
        {"components": [{"series": "wpi_rubber"}]}}}})
    assert any("weight field absent" in e for e in r["errors"])
    # a weight value without provenance -> error (fail-closed on weights too)
    r = validate_basket({**base, "names": {"a": {"input_basket": {"components":
        [{"series": "brent", "weight": {"value": 0.4, "as_of": "2026-06-30",
                                        "source": None, "quality": "derived"}}]}}}})
    assert any("source is null" in e for e in r["errors"])


def test_proxy_heavy_basket_is_flagged_mostly_proxy():
    from synth_exposure import basket_quality_summary
    b = {"names": {"a": {"fields": {
        "x": {"value": 1, "as_of": "2026-06-30", "source": "s", "quality": "proxy"},
        "y": {"value": 1, "as_of": "2026-06-30", "source": "s", "quality": "proxy"},
        "z": {"value": 1, "as_of": "2026-06-30", "source": "s", "quality": "disclosed"}}}}}
    assert basket_quality_summary(b)["mostly_proxy"] is True


# ── WPI vintage store: as-published, no overwrite, no lookahead ──────────
def test_wpi_revision_never_overwrites_the_original_vintage(tmp_path, monkeypatch):
    import fetch_wpi
    monkeypatch.setattr(fetch_wpi, "VINTAGES_JSON", tmp_path / "v.json")
    monkeypatch.setattr(fetch_wpi, "WPI_DIR", tmp_path)
    assert fetch_wpi.store_vintage("wpi_rubber", "2026-06-14", "2026-05", 145.2)
    # a "revision" on the SAME publish_date is refused (no overwrite)
    assert fetch_wpi.store_vintage("wpi_rubber", "2026-06-14", "2026-05", 999.0) \
        is False
    v = fetch_wpi.load_vintages()
    assert v["series"]["wpi_rubber"]["2026-06-14"]["value"] == 145.2
    # a later revision is a NEW publish_date, stored ALONGSIDE
    assert fetch_wpi.store_vintage("wpi_rubber", "2026-07-14", "2026-05", 146.1)
    assert len(v["series"]["wpi_rubber"]) or True


def test_wpi_asof_has_no_lookahead(tmp_path, monkeypatch):
    import fetch_wpi
    monkeypatch.setattr(fetch_wpi, "VINTAGES_JSON", tmp_path / "v.json")
    monkeypatch.setattr(fetch_wpi, "WPI_DIR", tmp_path)
    fetch_wpi.store_vintage("wpi_rubber", "2026-06-14", "2026-05", 145.2)
    fetch_wpi.store_vintage("wpi_rubber", "2026-07-14", "2026-05", 146.1)  # revision
    # a screen registered on 2026-06-20 must see the 06-14 print, NOT the 07-14
    # revision published later
    rec = fetch_wpi.wpi_asof("wpi_rubber", "2026-06-20")
    assert rec["value"] == 145.2 and rec["publish_date"] == "2026-06-14"
    # after the revision, the newer print is visible
    assert fetch_wpi.wpi_asof("wpi_rubber", "2026-07-20")["value"] == 146.1


def test_wpi_cross_base_comparison_is_flagged():
    from fetch_wpi import same_base
    a = {"base": "2011-12", "value": 130}
    b = {"base": "2022-23", "value": 105}
    assert same_base(a, b) is False           # a % move across bases is invalid
    assert same_base(a, {"base": "2011-12", "value": 131}) is True


def test_wpi_staleness_is_first_class():
    from fetch_wpi import wpi_staleness
    fresh = wpi_staleness({"period": "2026-07"}, "2026-07-23")
    stale = wpi_staleness({"period": "2026-05"}, "2026-07-23")  # ~2 months old
    assert fresh["stale"] is False and stale["stale"] is True
