# handlers.py
"""
This module contains the main event handlers for user interactions in the CLI.
It includes functions to handle menu navigation, filtering expenses, calculating summaries, and deleting records.
"""


from datetime import datetime
from typing import List, Dict
from constants import CATEGORIES
from view_expenses import get_expenses_by_month, get_expenses_by_category
from calculate_summary import calculate_summary
from delete_expense import delete_expense_by_index
from display_expenses import wait_for_user, render_table


def handle_month_filter(expenses: List[Dict]) -> None:
    """
    Prompts the user for a month and displays filtered expenses in a table.
    """
    while True:
        try:
            month = input("Enter the month (YYYY-MM): ")
            datetime.strptime(month, "%Y-%m")
            break
        except ValueError:
                print("Invalid date format. Please enter a valid date (YYYY-MM).")
                        
    filtered_expenses = get_expenses_by_month(month, expenses)
    render_table(filtered_expenses, show_index=False)


def handle_category_filter(expenses: List[Dict]) -> None:
    """
    Prompts the user to select a category and displays filtered expenses in a table.
    """
    categories = CATEGORIES
    print("\nSelect a category to filter:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    choice = input(f"Choice (1-{len(categories)}): ")
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        category = categories[int(choice) - 1]
    else:
        print("Invalid selection.")
        return

    filtered_expenses = get_expenses_by_category(category, expenses)
    render_table(filtered_expenses, show_index=False)


def handle_summary_by_category(expenses: List[Dict]) -> None:
    """
    Displays the total expenditure for a specific user-selected category.
    """
    categories = CATEGORIES
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    choice = input(f"Select category for summary (1-{len(categories)}): ")
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        category = categories[int(choice) - 1]
        _, category_totals = calculate_summary(expenses, categories)
        print(f"\n>>> Total for {category}: ${category_totals[category]:.2f}\n")
        wait_for_user()
    else:
        print("Invalid selection.")


def handle_summary_by_month(expenses: List[Dict]) -> None:
    """
    Displays a detailed financial summary for a specific month, including category breakdown.
    """
    while True:
        month = input("Enter the month to filter by (YYYY-MM): ")
        try:
            datetime.strptime(month, "%Y-%m")
            filtered_expenses = [expense for expense in expenses if expense["date"] == month]
            total, category_totals = calculate_summary(filtered_expenses, CATEGORIES)
            print(f"\n--- Summary for {month} ---")
            print(f"Grand Total: ${total:.2f}")
            for category, total in category_totals.items():
                print(f"  {category:<15}: ${total:>8.2f}")
            wait_for_user()
            break
        except ValueError:
            print("Invalid date format. Please enter a valid date (YYYY-MM).")
        

def handle_delete_expense_by_index(expenses: List[Dict]) -> None:
    """
    Prompts the user for the index of the expense to delete and updates the list.
    Args:
        expenses (List[Dict]): The current list of expense records.
    """
    while True:
        render_table(expenses, show_index=True) 
        
        index_str = input("\nEnter the number of the expense to delete (or 0 to cancel): ")
        
        if index_str == "0":
            print("Deletion cancelled.")
            return
            
        if not index_str.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        index = int(index_str) - 1
        if not (0 <= index < len(expenses)):
            print("Invalid index. Please enter a valid number from the list.")
            continue

        expense = expenses[index]
        
        while True:
            confirm = input(f"\nDelete '{expense['name']}' (${expense['amount']:.2f}, {expense['category']}, {expense['date']})? (y/n): ").lower().strip()
            
            if confirm == 'y':
                deleted = delete_expense_by_index(expenses, index)
                print(f"\n>>> Expense '{deleted['name']}' has been successfully deleted. <<<\n")
                wait_for_user()
                return
            elif confirm == 'n':
                print("Deletion cancelled.")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")