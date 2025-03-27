import os
import shutil
from logger import log_action, search_logs, LOG_PATH

def setup_module(module):
    """Ensure the data directory is clean before each test session."""
    if os.path.exists("data"):
        shutil.rmtree("data")

def test_log_action_creates_file():
    log_action("User test entry")
    assert os.path.exists(LOG_PATH)

def test_log_action_appends_entry():
    log_action("Another test entry")
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
    assert any("Another test entry" in line for line in lines)

def test_search_logs_finds_keyword(capsys):
    log_action("Test: password reset success")
    search_logs("password")
    captured = capsys.readouterr()
    assert "password reset success" in captured.out

def test_search_logs_handles_no_match(capsys):
    search_logs("notfoundkeyword")
    captured = capsys.readouterr()
    assert "No matching log entries found." in captured.out

def test_search_logs_handles_missing_file(capsys):
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)
    search_logs("anything")
    captured = capsys.readouterr()
    assert "Log file not found" in captured.out