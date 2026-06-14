<<<<<<< HEAD
import os

from app.github_integration import file_github_issue


def test_file_github_issue_returns_none_when_not_configured(monkeypatch):
    # Ensure env vars are not set
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.delenv("GITHUB_REPO", raising=False)

    res = file_github_issue("title", "body")
    assert res is None
=======
from app.github_integration import file_github_issue


def test_file_github_issue_returns_none_when_credentials_are_missing(monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.delenv("GITHUB_REPO", raising=False)

    issue_url = file_github_issue("Backup failed", "Validation failed.")

    assert issue_url is None
>>>>>>> 8f8e9ae6d3a64d69cdcb2697c043aba3aa99a759
