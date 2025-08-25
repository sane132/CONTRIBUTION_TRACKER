import os
from datetime import datetime

def display_menu(title, options):
    """Displays a menu and gets a valid integer choice from the user."""
    print(f"\n{title}")
    print("=" * len(title))
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    return get_int_input("\nSelect an option: ", min_val=1, max_val=len(options))

def get_int_input(prompt, min_val=None, max_val=None):
    """Prompts for and validates integer input."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_float_input(prompt, min_val=None):
    """Prompts for and validates float input."""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_date_input():
    """Prompts for and validates date input in YYYY-MM-DD format."""
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_success(message):
    """Prints a message in green color."""
    print(f"\033[92m{message}\033[0m")

def print_error(message):
    """Prints a message in red color."""
    print(f"\033[91m{message}\033[0m")

def print_warning(message):
    """Prints a message in yellow color."""
    print(f"\033[93m{message}\033[0m")