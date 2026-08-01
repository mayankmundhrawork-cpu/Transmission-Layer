"""NSE fetcher and bhavcopy-parser tests (§5, CP2).

The bhavcopy is the price series, the listing record, and the raw material for
the point-in-time universe. A parser bug here is not a parser bug — it is a
silent, uniform distortion of every factor the platform will ever compute.
"""
from __future__ import annotations

import datetime as dt

import pandas as pd
import pytest

from src.archive.fetchers.nse import (
    BHAVCOPY_COLUMNS, NseBhavcopyFetcher, NseFnoBanFetcher,
    candidate_trading_days, parse_bhavcopy,
)
from src.archive.http import PoliteSession, SourceBlocked
from src.archive.store import Archive
from tests.platform.fixtures import (
    BHAVCOPY_LEGACY, BHAVCOPY_SECWISE, BHAVCOPY_UDIFF, HTML_ERROR_PAGE, zipped,
)
from tests.platform.test_http import FakeResponse, FakeSession


@pytest.fixture
def archive(tmp_path):
    with Archive(tmp_path / "archive") as arc:
        yield arc


def fetcher_with(archive, responses):
    fake = FakeSession(responses)
    session = PoliteSession(session=fake, sleep=lambda _: None, min_interval_s=0.0)
    f = NseBhavcopyFetcher(archive, session=session)
    return f, fake


# --- parsing ----------------------------------------------------------------

def test_legacy_layout_parses_to_canonical_schema():
    frame = parse_bhavcopy(BHAVCOPY_LEGACY)
    assert list(frame.columns) == BHAVCOPY_COLUMNS
    rel = frame[frame["symbol"] == "RELIANCE"].iloc[0]
    assert rel["isin"] == "INE002A01018"
    assert rel["series"] == "EQ"
    assert rel["close"] == pytest.approx(1015.50)
    assert rel["volume"] == pytest.approx(1_000_000)
    assert rel["turnover"] == pytest.approx(1_015_500_000.0)
    assert rel["date"] == pd.Timestamp("2015-01-15")


def test_secwise_turnover_is_converted_from_lakhs_to_rupees():
    """The file publishes ₹ lakhs. A missed 1e5 gives a liquidity screen that
    is wrong by five orders of magnitude and still looks plausible plotted."""
    frame = parse_bhavcopy(BHAVCOPY_SECWISE)
    rel = frame[frame["symbol"] == "RELIANCE"].iloc[0]
    assert rel["turnover"] == pytest.approx(20155.00 * 1e5)
    # cross-check against volume x average price: ~₹20.2 crore
    assert rel["turnover"] == pytest.approx(rel["volume"] * 2015.5, rel=0.01)


def test_secwise_carries_delivery_data():
    frame = parse_bhavcopy(BHAVCOPY_SECWISE)
    rel = frame[frame["symbol"] == "RELIANCE"].iloc[0]
    assert rel["deliv_qty"] == pytest.approx(400_000)
    assert rel["deliv_pct"] == pytest.approx(40.0)


def test_udiff_layout_parses_and_drops_derivatives():
    frame = parse_bhavcopy(BHAVCOPY_UDIFF)
    assert set(frame["symbol"]) == {"RELIANCE", "TINYCO"}, "F&O rows must be filtered out"
    rel = frame[frame["symbol"] == "RELIANCE"].iloc[0]
    assert rel["close"] == pytest.approx(3140.00)
    assert rel["turnover"] == pytest.approx(6_280_000_000.0)
    assert rel["isin"] == "INE002A01018"


def test_all_three_layouts_produce_identical_columns():
    frames = [parse_bhavcopy(b) for b in (BHAVCOPY_LEGACY, BHAVCOPY_SECWISE, BHAVCOPY_UDIFF)]
    assert all(list(f.columns) == BHAVCOPY_COLUMNS for f in frames)


def test_non_equity_series_are_dropped():
    """N1 is a debt series — it is not an equity and must not enter the universe."""
    frame = parse_bhavcopy(BHAVCOPY_LEGACY)
    assert "SOMEBOND" not in set(frame["symbol"])


def test_trade_to_trade_series_are_kept():
    """BE/BZ are surveillance series but genuinely investable. Dropping them
    would remove exactly the stressed smallcaps a risk factor must see."""
    frame = parse_bhavcopy(BHAVCOPY_LEGACY)
    assert "TINYCO" in set(frame["symbol"])
    assert frame[frame["symbol"] == "TINYCO"].iloc[0]["series"] == "BE"


def test_zero_price_rows_are_dropped():
    """A suspended scrip prints zeros; a zero close would poison every return."""
    frame = parse_bhavcopy(BHAVCOPY_LEGACY)
    assert "SUSPENDCO" not in set(frame["symbol"])
    assert (frame["close"] > 0).all()


def test_zipped_bhavcopy_is_unwrapped():
    plain = parse_bhavcopy(BHAVCOPY_LEGACY)
    zipd = parse_bhavcopy(zipped(BHAVCOPY_LEGACY))
    pd.testing.assert_frame_equal(plain, zipd)


def test_explicit_trade_date_overrides_file_contents():
    frame = parse_bhavcopy(BHAVCOPY_LEGACY, dt.date(2015, 1, 15))
    assert (frame["date"] == pd.Timestamp("2015-01-15")).all()


def test_unrecognised_layout_is_rejected_loudly():
    with pytest.raises(Exception, match="unrecognised bhavcopy layout"):
        parse_bhavcopy(b"COL_A,COL_B\n1,2\n")


# --- URL construction -------------------------------------------------------

def test_url_candidates_are_era_appropriate(archive):
    f = NseBhavcopyFetcher(archive)
    old = f.urls_for("2012-03-15")
    assert all("BhavCopy_NSE_CM" not in u for u in old), "UDiFF did not exist in 2012"
    assert any("cm15MAR2012bhav.csv.zip" in u for u in old)

    new = f.urls_for("2024-07-05")
    assert new[0].endswith("BhavCopy_NSE_CM_0_0_0_20240705_F_0000.csv.zip"), \
        "newest layout should be tried first"
    assert any("sec_bhavdata_full_05072024.csv" in u for u in new)


def test_fno_ban_url_format(archive):
    assert NseFnoBanFetcher(archive).urls_for("2024-07-05")[0].endswith(
        "fo_secban_05072024.csv"
    )


# --- fetching + caching -----------------------------------------------------

def test_fetch_archives_and_logs_ok(archive):
    f, fake = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),               # prime
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),            # document
    ])
    entry = f.fetch("2015-01-15")
    assert entry is not None
    assert archive.has("nse.bhavcopy", "2015-01-15")
    assert entry.meta["layout"] == "legacy"
    assert [a["outcome"] for a in archive.attempts()] == ["ok"]


def test_refetch_is_a_cache_hit_with_no_network_call(archive):
    """CP2: re-running a backfill must not re-request anything."""
    f, fake = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),
    ])
    f.fetch("2015-01-15")
    calls_after_first = len(fake.calls)

    entry = f.fetch("2015-01-15")  # FakeSession raises on any extra request
    assert entry is not None
    assert len(fake.calls) == calls_after_first, "cache hit must not touch the network"
    assert [a["outcome"] for a in archive.attempts()] == ["ok", "cache_hit"]


def test_force_refetch_bypasses_the_cache(archive):
    f, fake = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),
    ])
    f.fetch("2015-01-15")
    f.fetch("2015-01-15", force=True)
    assert len(archive.entries(source="nse.bhavcopy", doc_key="2015-01-15")) == 2


def test_html_error_page_is_not_archived_as_a_bhavcopy(archive):
    """A 200 carrying an HTML error page is NSE's favourite failure mode. It
    must fall through to the next candidate URL, not be stored as data."""
    f, fake = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(200, HTML_ERROR_PAGE),        # udiff path: junk
        FakeResponse(200, HTML_ERROR_PAGE),        # secwise path: junk
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),  # legacy path: real
    ])
    entry = f.fetch("2024-07-05")
    assert entry is not None
    assert entry.meta["layout"] == "legacy"
    assert archive.read_entry(entry) != HTML_ERROR_PAGE


def test_all_urls_404_records_skipped_and_returns_none(archive):
    """A trading holiday: every candidate 404s. That is `skipped`, not a failure."""
    f, _ = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(404), FakeResponse(404), FakeResponse(404), FakeResponse(404),
    ])
    assert f.fetch("2015-08-15") is None
    assert archive.attempts()[-1]["outcome"] == "skipped"
    assert not archive.has("nse.bhavcopy", "2015-08-15")


def test_block_halts_and_is_recorded(archive):
    f, _ = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(403),
    ])
    with pytest.raises(SourceBlocked):
        f.fetch("2015-01-15")
    assert archive.attempts()[-1]["outcome"] == "blocked"


def test_fetch_many_halts_on_block(archive):
    f, _ = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),
        FakeResponse(403),
    ])
    summary = f.fetch_many(["2015-01-15", "2015-01-16", "2015-01-19"])
    assert summary.blocked is True
    assert summary.ok == 1
    assert summary.attempted < 3, "must stop rather than walk into a longer ban"


def test_fetch_many_counts_cache_hits(archive):
    f, _ = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),
    ])
    f.fetch("2015-01-15")
    summary = f.fetch_many(["2015-01-15"])
    assert (summary.cache_hits, summary.ok, summary.failed) == (1, 0, 0)


def test_frame_reads_from_archive_not_network(archive):
    f, fake = fetcher_with(archive, [
        FakeResponse(200, b"<html>home</html>"),
        FakeResponse(200, zipped(BHAVCOPY_LEGACY)),
    ])
    f.fetch("2015-01-15")
    before = len(fake.calls)
    frame = f.frame("2015-01-15")
    assert frame is not None and not frame.empty
    assert len(fake.calls) == before


# --- calendar ---------------------------------------------------------------

def test_candidate_trading_days_excludes_weekends():
    days = candidate_trading_days(dt.date(2024, 7, 1), dt.date(2024, 7, 14))
    assert "2024-07-06" not in days and "2024-07-07" not in days  # Sat/Sun
    assert len(days) == 10
    assert days[0] == "2024-07-01"


def test_candidate_trading_days_is_inclusive():
    days = candidate_trading_days(dt.date(2024, 7, 1), dt.date(2024, 7, 1))
    assert days == ["2024-07-01"]
