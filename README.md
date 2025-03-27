# Technical Lesson: Imports & File I/O

## Learning Goals

- Use Python's import system to modularize and reuse code efficiently.
- Apply File Input/Output (I/O) to persist and retrieve data from external files.
- Handle file access safely with `with open()` and exception handling.
- Structure Python applications using standard configuration and modularization techniques.

## Introduction

In Python, separating code into modules and working with external files are essential for building real-world applications. This lesson will cover:

- Importing built-in or custom modules.
- Writing logs to an external file.
- Searching and filtering logs from a file.
- Preventing application crashes using exception handling.

Let’s consider a user activity tracking application where logs need to be written and retrieved from a file. The application currently supports:

- Writing hardcoded messages to the console.

However, it lacks:

- Persisting actions to a file for record-keeping.
- Filtering user activity logs by keywords.
- Handling errors like missing log files gracefully.

To solve these issues, we will:

1. Write logs to a file using `with open()` and the `datetime` module.  
2. Read logs from the file and filter based on keywords.  
3. Handle missing files using a `try-except` block.  
4. Organize logic using importable Python modules.

## Code Along

### Setting Up the Project

To get started, clone the repository and install any necessary requirements:

```bash
git clone <repo-url>
cd course-7-module-6-imports-and-file-io
pip install -r requirements.txt
```

Now, let's define the structure of our logger module.

### Writing Logs to a File

We will use the `datetime` module to timestamp actions and `with open()` to append to a file.

#### Example: `log_action()`

```python
from datetime import datetime

def log_action(action, log_file="data/user_logs.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {action}\n")
```

- Appends each action to `user_logs.txt` with a timestamp.  
- Uses `with open()` for automatic file closure.

### Searching Logs by Keyword

We can retrieve only the lines that match a search term.

#### Example: `search_logs()`

```python
def search_logs(keyword, log_file="data/user_logs.txt"):
    try:
        with open(log_file, "r") as file:
            matches = [line.strip() for line in file if keyword.lower() in line.lower()]
            if matches:
                print("\nFiltered Logs:")
                for match in matches:
                    print(match)
            else:
                print("No matching log entries found.")
    except FileNotFoundError:
        print("Log file not found.")
```

- Safely opens and reads the file.  
- Filters matching lines using a list comprehension.  
- Gracefully handles missing files.

### Building the CLI Entry Point

We will use `argparse` to allow users to log actions or search logs from the terminal.

#### Example: `main.py`

```python
import argparse
from logger import log_action, search_logs

def main():
    parser = argparse.ArgumentParser(description="User Log Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    log_parser = subparsers.add_parser("log", help="Log a user action")
    log_parser.add_argument("action", type=str, help="The action to log")

    search_parser = subparsers.add_parser("search", help="Search logs by keyword")
    search_parser.add_argument("keyword", type=str, help="Keyword to filter logs")

    args = parser.parse_args()

    if args.command == "log":
        log_action(args.action)
    elif args.command == "search":
        search_logs(args.keyword)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

## Best Practices for File I/O and Imports

- Always use `with open()` to safely handle files and automatically close them.  
- Use `try-except` blocks to catch errors such as missing files or permission issues.  
- Keep import statements at the top of your Python files.  
- Separate logic into reusable modules to improve organization and readability.  
- Avoid hardcoding file paths—use variables or configs when possible.

## Conclusion

By mastering Imports and File I/O, developers can:

- Structure Python applications for maintainability and reuse.  
- Persist data through external files safely and efficiently.  
- Handle errors without crashing the application.  
- Build scalable CLI tools that integrate clean code and modular design.

These foundational skills are essential for working with real-world data and building production-level Python applications.
