from datetime import datetime

def log_action(action, log_file="data/user_logs.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as file:
            file.write(f"[{timestamp}] {action}\\n")
        print(f"✅ Logged: {action}")
    except Exception as e:
        print(f"❌ Failed to log action: {e}")
