# lib/main.py

import argparse
# TODO: Import log_action and search_logs from logger module
from logger import log_action, search_logs

def main():
    parser = argparse.ArgumentParser(description="User Log Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Log subcommand
    log_parser = subparsers.add_parser("log", help="Log a user action")
    log_parser.add_argument("action", type=str, help="The action to log")

    # Search subcommand
    search_parser = subparsers.add_parser("search", help="Search log file")
    search_parser.add_argument("keyword", type=str, help="Keyword to search in logs")

    args = parser.parse_args()

    # TODO: Route commands to appropriate logger function based on args.command
    if args.command == "log":
        log_action(args.action)
    # Call log_action function with the appropriate argument
    elif args.command == "search":
        search_logs(args.keyword)
    # Call search_logs function with the appropriate argument
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
