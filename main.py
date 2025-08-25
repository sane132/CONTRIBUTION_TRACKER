#!/usr/bin/env python3
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from lib.models import create_tables
    from lib.cli import CLI
except ImportError as e:
    print(f"Import error: {e}")
    print("Current Python path:")
    for path in sys.path:
        print(f"  {path}")
    raise

def main():
    """
    Main function to initialize the application.
    It creates the database tables and starts the CLI.
    """
    create_tables()
    cli = CLI()
    cli.run()

if __name__ == "__main__":
    main()