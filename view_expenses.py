# view_expenses.py
"""
This module provides functionality to display and filter expenses.
It allows viewing all records or filtering by specific criteria like month or category.
"""

from datetime import datetime
from typing import List, Dict


def display_expenses(expenses: List[Dict]) -> None:
    """
    Formats and prints a list of expenses in a tabular format.
    
    Args:
        expenses (List[Dict]): The list of expenses to display.
    """
    if not expenses:
        print("\n[!] No expenses found to display.")
        return
    
    print(f"\n{'Name':<20} | {'Amount':<10} | {'Category':<15} | {'Date':<10}")
    print("-" * 65)
    for e in expenses:
        print(f"{e['name']:<20} | ${e['amount']:<9.2f} | {e['category']:<15} | {e['date']:<10}")
    print("-" * 65 + "\n")


def get_expenses_by_month(month: str, expenses: List[Dict]) -> List[Dict]: 
    """
    Filters the expenses list by a specific month string.
    
    Args:
        month (str): The month to filter by (Format: YYYY-MM).
        expenses (List[Dict]): The full list of expenses.
        
    Returns:
        List[Dict]: A list containing only expenses from the specified month.
    """
    filtered_expenses = [e for e in expenses if e["date"] == month]
    return filtered_expenses
    

def get_expenses_by_category(category: str, expenses: List[Dict]) -> List[Dict]: 
    """
    Filters the expenses list by a specific category name.
    
    Args:
        category (str): The category name to filter by.
        expenses (List[Dict]): The full list of expenses.
        
    Returns:
        List[Dict]: A list containing only expenses from the specified category.
    """
    filtered_expenses = [e for e in expenses if e["category"] == category]
    return filtered_expenses


def display_menu(expenses: List[Dict]) -> None:
    """
    Sub-menu for navigating different viewing and filtering options.
    Used primarily for standalone testing of the view module.
    
    Args:
        expenses (List[Dict]): The current list of expenses.
    """
    if not expenses:
        print("No expenses found.")
        return
    else:
        while True:
            print("View Expenses:")
            print("1. View all expenses")
            print("2. View expenses by month or category")
            print("3. Return to main menu")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                display_expenses(expenses)
            elif choice == "2":
                while True:
                    print("Filter by:")
                    print("1. Month")
                    print("2. Category")
                    print("3. Return to previous menu")
                    
                    filter_choice = input("Choose an option: ")
                    
                    if filter_choice == "1":
                        while True:
                            try:
                                month = input("Enter the month (YYYY-MM): ")
                                datetime.strptime(month, "%Y-%m")
                                break
                            except ValueError:
                                print("Invalid date format. Please enter a valid date (YYYY-MM).")
                        
                        filtered_expenses = get_expenses_by_month(month, expenses)
                        display_expenses(filtered_expenses)

                    elif filter_choice == "2":
                        while True:
                            try:
                                category = input(f"Enter the category (Food, Transport, Entertainment, Utilities): ").strip().title()
                                if category in ["Food", "Transport", "Entertainment", "Utilities"]:
                                    break
                                else:
                                    print("Invalid category. Please enter a valid category.")
                            except (ValueError, IndexError):
                                print("Invalid category. Please enter a valid category.")

                        
                        filtered_expenses = get_expenses_by_category(category, expenses)
                        display_expenses(filtered_expenses)
                    elif filter_choice == "3":
                        break
                    else:
                        print("Invalid option. Please try again.")
            elif choice == "3":
                print("Returning to main menu...")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":  
    expenses_debug = [
        {"name": "Bar", "amount": 70.0, "category": "Entertainment", "date": "2026-01"},
        {"name": "Rent", "amount": 600.0, "category": "Utilities", "date": "2026-01"},
        {"name": "Lunch", "amount": 35.5, "category": "Food", "date": "2026-02"},
        {"name": "Gas", "amount": 145.0, "category": "Transport", "date": "2026-02"},
        {"name": "Lunch", "amount": 35.5, "category": "Food", "date": "2026-03"},
        {"name": "Bus Ticket", "amount": 2.75, "category": "Transport", "date": "2026-03"},
        {"name": "Movie", "amount": 12.0, "category": "Entertainment", "date": "2026-04"},
        {"name": "Electricity Bill", "amount": 60.0, "category": "Utilities", "date": "2026-04"}
    ]
    

    print("Testing view_expenses function with sample data...")
    while True:
        debug_choice = input(f"Press 1 do an empty test, 2 to use debug data or 3 to exit: ")
        if debug_choice == "1":
            print("\nTesting with empty expenses list...\n")
            display_menu([])
        elif debug_choice == "2":
            print("Testing with sample expenses data...")
            display_menu(expenses_debug)
        elif debug_choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")