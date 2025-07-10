from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    """Append a user action with a timestamp to the log file."""
    # TODO: Ensure the log file directory exists
    directory = os.path.dirname(log_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # TODO: Generate current timestamp
    # TODO: Open the log file in append mode
    # TODO: Write a formatted log entry with timestamp and action
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_logs.txt", "a") as file:
        file.write(f"[{timestamp}] {action}\n")
        
    # TODO: Print confirmation message to the user
    print("Action logged successfully.")
   

def search_logs(keyword, log_file=LOG_PATH):
    """Search the log file for lines that match a keyword."""
    # TODO: Try opening the log file for reading
    # TODO: Read each line and filter for lines that include the keyword (case insensitive)
    # TODO: Print matched log lines or a 'not found' message
    # TODO: Handle FileNotFoundError gracefully
    try:
        with open(log_file, "r") as file:
            found = False
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("No matches found.")
    except FileNotFoundError:
        print("Log file not found.")


# Usage
log_action("User logged in")
log_action("User updated profile")
search_logs("profile")