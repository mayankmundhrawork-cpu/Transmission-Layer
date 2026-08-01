"""Archive layer tests (§3.4, §5).

The append-only property is the one that must not be merely documented. If an
entry can be mutated, then "reproducible from a git commit plus an archive
snapshot" is a claim rather than a fact.
"""
from __future__ import annotations

import datetime as dt
import sqlite3

import pytest

from src.archive.store import Archive, ArchiveError, content_hash, iso, utc_now


@pytest.fixture
def archive(tmp_path):
    with Archive(tmp_path / "archive") as arc:
        yield arc


def _put(arc, content=b"hello", key="2015-01-15", source="nse.bhavcopy"):
    return arc.put(
        source=source, doc_key=key, url=f"https://example.test/{key}",
        content=content, headers={"Content-Type": "text/csv"}, http_status=200,
    )


# --- append-only ------------------------------------------------------------

def test_archive_entry_cannot_be_updated(archive):
    entry = _put(archive)
    with pytest.raises(sqlite3.IntegrityError, match="append-only"):
        archive._conn.execute(
            "UPDATE archive_entry SET url = 'tampered' WHERE entry_id = ?",
            (entry.entry_id,),
        )


def test_archive_entry_cannot_be_deleted(archive):
    entry = _put(archive)
    with pytest.raises(sqlite3.IntegrityError, match="append-only"):
        archive._conn.execute(
            "DELETE FROM archive_entry WHERE entry_id = ?", (entry.entry_id,)
        )


def test_fetch_ledger_cannot_be_rewritten(archive):
    archive.log_attempt(source="nse.bhavcopy", doc_key="2015-01-15", outcome="ok")
    with pytest.raises(sqlite3.IntegrityError, match="append-only"):
        archive._conn.execute("UPDATE fetch_ledger SET outcome = 'blocked'")
    with pytest.raises(sqlite3.IntegrityError, match="append-only"):
        archive._conn.execute("DELETE FROM fetch_ledger")


def test_refetch_creates_a_new_entry_not_an_overwrite(archive):
    """§3.4: re-fetching the same document later is a new observation."""
    t1 = dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc)
    t2 = dt.datetime(2024, 6, 1, tzinfo=dt.timezone.utc)
    e1 = archive.put(source="nse.delisted", doc_key="delisted", url="u",
                     content=b"same bytes", fetched_at=t1)
    e2 = archive.put(source="nse.delisted", doc_key="delisted", url="u",
                     content=b"same bytes", fetched_at=t2)

    assert e1.entry_id != e2.entry_id
    assert e1.content_hash == e2.content_hash, "identical bytes share one blob"
    entries = archive.entries(source="nse.delisted", doc_key="delisted")
    assert len(entries) == 2
    assert archive.latest_entry("nse.delisted", "delisted").entry_id == e2.entry_id
    assert archive.stats()["distinct_blobs"] == 1, "content-addressed: one blob, two entries"


def test_revised_document_keeps_both_versions(archive):
    """A source that silently republishes a corrected file must not erase the
    original — that original is what an as-of query for the earlier date needs."""
    archive.put(source="nse.delisted", doc_key="delisted", url="u", content=b"v1",
                fetched_at=dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc))
    archive.put(source="nse.delisted", doc_key="delisted", url="u", content=b"v2",
                fetched_at=dt.datetime(2024, 2, 1, tzinfo=dt.timezone.utc))
    entries = archive.entries(source="nse.delisted", doc_key="delisted")
    assert [archive.read_entry(e) for e in entries] == [b"v1", b"v2"]


# --- content addressing -----------------------------------------------------

def test_blob_is_content_addressed_and_readable(archive):
    entry = _put(archive, content=b"payload")
    assert entry.content_hash == content_hash(b"payload")
    assert archive.read(entry.content_hash) == b"payload"
    assert archive.blob_path(entry.content_hash).exists()


def test_blob_is_written_read_only(archive):
    entry = _put(archive, content=b"payload")
    mode = archive.blob_path(entry.content_hash).stat().st_mode
    assert not mode & 0o200, "blobs must not be owner-writable"


def test_corrupted_blob_is_detected(archive):
    entry = _put(archive, content=b"payload")
    path = archive.blob_path(entry.content_hash)
    path.chmod(0o600)
    path.write_bytes(b"tampered")
    with pytest.raises(ArchiveError, match="corruption"):
        archive.read(entry.content_hash)
    assert archive.verify(), "verify() must report the corruption"


def test_verify_passes_on_intact_archive(archive):
    for i in range(3):
        _put(archive, content=f"doc-{i}".encode(), key=f"2015-01-{i + 10}")
    assert archive.verify() == []


def test_missing_blob_is_an_error_not_a_none(archive):
    with pytest.raises(ArchiveError, match="missing"):
        archive.read("0" * 64)


# --- ledger -----------------------------------------------------------------

def test_ledger_records_failures(archive):
    archive.log_attempt(source="nse.bhavcopy", doc_key="2015-08-15",
                        outcome="skipped", error="holiday")
    archive.log_attempt(source="nse.bhavcopy", doc_key="2015-01-16",
                        outcome="blocked", error="refused")
    outcomes = archive.stats()["ledger_outcomes"]
    assert outcomes == {"skipped": 1, "blocked": 1}
    assert len(archive.attempts(outcome="blocked")) == 1


def test_unknown_outcome_rejected(archive):
    with pytest.raises(ArchiveError, match="unknown outcome"):
        archive.log_attempt(source="s", doc_key="k", outcome="probably-fine")


def test_gaps_are_explainable_from_the_ledger(archive):
    """The point of logging failures: a missing date must have a recorded reason."""
    for key, outcome in [("2015-01-15", "ok"), ("2015-01-16", "skipped"),
                         ("2015-01-19", "network_error")]:
        if outcome == "ok":
            _put(archive, key=key)
        archive.log_attempt(source="nse.bhavcopy", doc_key=key, outcome=outcome)

    archived = set(archive.doc_keys("nse.bhavcopy"))
    attempted = {a["doc_key"] for a in archive.attempts(source="nse.bhavcopy")}
    assert attempted - archived == {"2015-01-16", "2015-01-19"}
    reasons = {a["doc_key"]: a["outcome"] for a in archive.attempts(source="nse.bhavcopy")}
    assert reasons["2015-01-16"] == "skipped"
    assert reasons["2015-01-19"] == "network_error"


# --- timestamps -------------------------------------------------------------

def test_naive_timestamps_are_rejected(archive):
    """A naive fetch timestamp silently localised is a look-ahead bug waiting
    for someone to run the pipeline in a different timezone."""
    with pytest.raises(ArchiveError, match="timezone-aware"):
        archive.put(source="s", doc_key="k", url="u", content=b"x",
                    fetched_at=dt.datetime(2024, 1, 1))


def test_timestamps_round_trip_as_utc(archive):
    ts = dt.datetime(2024, 3, 1, 9, 30, tzinfo=dt.timezone(dt.timedelta(hours=5, minutes=30)))
    entry = archive.put(source="s", doc_key="k", url="u", content=b"x", fetched_at=ts)
    assert entry.fetched_at == ts
    assert entry.fetched_at.utcoffset() == dt.timedelta(0), "stored in UTC"
    assert iso(ts).endswith("Z")


# --- queries ----------------------------------------------------------------

def test_has_and_doc_keys(archive):
    _put(archive, key="2015-01-15")
    _put(archive, key="2015-01-16")
    assert archive.has("nse.bhavcopy", "2015-01-15")
    assert not archive.has("nse.bhavcopy", "2015-01-17")
    assert archive.doc_keys("nse.bhavcopy") == ["2015-01-15", "2015-01-16"]


def test_iter_documents_yields_latest_only(archive):
    archive.put(source="s", doc_key="k", url="u", content=b"old",
                fetched_at=dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc))
    archive.put(source="s", doc_key="k", url="u", content=b"new",
                fetched_at=dt.datetime(2024, 2, 1, tzinfo=dt.timezone.utc))
    docs = list(archive.iter_documents("s"))
    assert len(docs) == 1 and docs[0][1] == b"new"


def test_entries_filter_by_since(archive):
    archive.put(source="s", doc_key="a", url="u", content=b"1",
                fetched_at=dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc))
    archive.put(source="s", doc_key="b", url="u", content=b"2",
                fetched_at=dt.datetime(2024, 3, 1, tzinfo=dt.timezone.utc))
    recent = archive.entries(since=dt.datetime(2024, 2, 1, tzinfo=dt.timezone.utc))
    assert [e.doc_key for e in recent] == ["b"]


def test_headers_and_meta_round_trip(archive):
    entry = archive.put(source="s", doc_key="k", url="u", content=b"x",
                        headers={"Content-Type": "text/csv"}, meta={"layout": "legacy"})
    assert entry.headers["Content-Type"] == "text/csv"
    assert entry.meta["layout"] == "legacy"


def test_source_and_key_are_required(archive):
    with pytest.raises(ArchiveError):
        archive.put(source="", doc_key="k", url="u", content=b"x")


def test_archive_survives_reopen(tmp_path):
    with Archive(tmp_path / "arc") as a:
        entry = _put(a, content=b"durable")
    with Archive(tmp_path / "arc") as b:
        assert b.read(entry.content_hash) == b"durable"
        assert b.has("nse.bhavcopy", "2015-01-15")
