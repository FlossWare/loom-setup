"""Installer must accept both historical and canonical GitHub archive prefixes."""

from __future__ import annotations

from pathlib import Path

INSTALLER = Path(__file__).resolve().parents[1] / "scripts" / "install.sh"


def test_installer_accepts_renamed_archive_prefix() -> None:
    text = INSTALLER.read_text(encoding="utf-8")
    assert 'find "$TMP_SETUP" -mindepth 1 -maxdepth 1 -type d -print -quit' in text
    assert "coding-agent-setup-*" not in text
    assert "failed to unpack" in text and "artifact" in text
