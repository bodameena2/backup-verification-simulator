<<<<<<< HEAD
import os
import shutil
import sqlite3
import time
import glob

import pytest

from app import mock_backup
from app.mock_backup import SOURCE_DB, BACKUPS_DIR, init_source_db, corrupt_backup, cleanup_old_backups


def setup_module(module):
    # Ensure clean state
    if os.path.exists(SOURCE_DB):
        os.remove(SOURCE_DB)
    if os.path.exists(BACKUPS_DIR):
        for f in glob.glob(os.path.join(BACKUPS_DIR, "*.db")):
            os.remove(f)


def teardown_module(module):
    # Clean created files
    if os.path.exists(SOURCE_DB):
        os.remove(SOURCE_DB)
    if os.path.exists(BACKUPS_DIR):
        for f in glob.glob(os.path.join(BACKUPS_DIR, "*.db")):
            os.remove(f)


def test_init_source_db_creates_db_and_populates_tables():
    init_source_db()
    assert os.path.exists(SOURCE_DB)

    conn = sqlite3.connect(SOURCE_DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    users_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM transactions")
    txn_count = cur.fetchone()[0]
    conn.close()

    assert users_count == 100
    assert txn_count == 500


def test_corrupt_backup_drops_users_table(tmp_path):
    init_source_db()
    backup_path = tmp_path / "test_backup.db"
    shutil.copy2(SOURCE_DB, backup_path)

    corrupt_backup(str(backup_path), rand_val=0.1)

    conn = sqlite3.connect(backup_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    row = cur.fetchone()
    conn.close()

    assert row is None


def test_corrupt_backup_empties_transactions(tmp_path):
    init_source_db()
    backup_path = tmp_path / "test_backup2.db"
    shutil.copy2(SOURCE_DB, backup_path)

    corrupt_backup(str(backup_path), rand_val=0.25)

    conn = sqlite3.connect(backup_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM transactions")
    count = cur.fetchone()[0]
    conn.close()

    assert count == 0


def test_corrupt_backup_negative_amounts(tmp_path):
    init_source_db()
    backup_path = tmp_path / "test_backup3.db"
    shutil.copy2(SOURCE_DB, backup_path)

    corrupt_backup(str(backup_path), rand_val=0.5)

    conn = sqlite3.connect(backup_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM transactions WHERE amount < 0")
    neg_count = cur.fetchone()[0]
    conn.close()

    assert neg_count > 0


def test_cleanup_old_backups_keeps_most_recent(tmp_path):
    # create backups dir
    d = tmp_path / "backups"
    d.mkdir()

    # create 5 dummy backup files with different mtimes
    files = []
    for i in range(5):
        p = d / f"b{i}.db"
        p.write_text("x")
        files.append(str(p))
        time.sleep(0.01)

    # Monkeypatch module BACKUPS_DIR to our tmp dir for testing
    orig = mock_backup.BACKUPS_DIR
    mock_backup.BACKUPS_DIR = str(d)

    try:
        cleanup_old_backups(keep=2)
        remaining = sorted(glob.glob(os.path.join(str(d), "*.db")))
        assert len(remaining) == 2
    finally:
        mock_backup.BACKUPS_DIR = orig
=======
import glob
import os
import sqlite3

from app import mock_backup


def count_rows(db_path, table_name):
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        return cursor.fetchone()[0]
    finally:
        conn.close()


def test_init_source_db_creates_expected_tables_and_rows(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    mock_backup.init_source_db()

    assert os.path.exists(mock_backup.SOURCE_DB)
    assert count_rows(mock_backup.SOURCE_DB, "users") == 100
    assert count_rows(mock_backup.SOURCE_DB, "transactions") == 500


def test_create_backup_without_corruption_copies_source_database(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(mock_backup.random, "random", lambda: 0.9)

    mock_backup.create_backup()

    backups = glob.glob(os.path.join(mock_backup.BACKUPS_DIR, "*.db"))
    assert len(backups) == 1
    assert count_rows(backups[0], "users") == 100
    assert count_rows(backups[0], "transactions") == 500


def test_corrupt_backup_can_create_negative_transaction_amounts(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mock_backup.init_source_db()

    mock_backup.corrupt_backup(mock_backup.SOURCE_DB, rand_val=0.50)

    conn = sqlite3.connect(mock_backup.SOURCE_DB)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM transactions WHERE amount < 0")
        negative_amounts = cursor.fetchone()[0]
    finally:
        conn.close()

    assert negative_amounts > 0


def test_cleanup_old_backups_keeps_latest_files_and_removes_sandbox(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    os.makedirs(mock_backup.BACKUPS_DIR, exist_ok=True)
    os.makedirs("database/sandbox", exist_ok=True)

    for index in range(5):
        path = os.path.join(mock_backup.BACKUPS_DIR, f"backup_{index}.db")
        with open(path, "w", encoding="utf-8") as file:
            file.write("backup")
        os.utime(path, (index, index))

    sandbox_path = "database/sandbox/sandbox_database.db"
    with open(sandbox_path, "w", encoding="utf-8") as file:
        file.write("sandbox")

    mock_backup.cleanup_old_backups(keep=2)

    remaining = sorted(os.path.basename(path) for path in glob.glob(os.path.join(mock_backup.BACKUPS_DIR, "*.db")))
    assert remaining == ["backup_3.db", "backup_4.db"]
    assert not os.path.exists(sandbox_path)
>>>>>>> 8f8e9ae6d3a64d69cdcb2697c043aba3aa99a759
