from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    """Append a user action with a timestamp to the log file."""
    # TODO: Ensure the log file directory exists
    # TODO: Generate current timestamp
    # TODO: Open the log file in append mode
    # TODO: Write a formatted log entry with timestamp and action
    # TODO: Print confirmation message to the user
    pass

def search_logs(keyword, log_file=LOG_PATH):
    """Search the log file for lines that match a keyword."""
    # TODO: Try opening the log file for reading
    # TODO: Read each line and filter for lines that include the keyword (case insensitive)
    # TODO: Print matched log lines or a 'not found' message
    # TODO: Handle FileNotFoundError gracefully
    pass