# main.py
"""
Main entry point for the Financial Tracker CLI.
Orchestrates data loading, initialization, and the primary application loop.
"""

from add_expense import add_expense
from storage import load_expenses
from menu import show_menu, view_expenses_menu, view_summary, view_delete_expense_menu
from constants import CATEGORIES, EXPENSES_FILE


def main() -> None:
    """
    Main entry point of the application. Handles data loading and main loop.
    """
    expenses = load_expenses(EXPENSES_FILE)
    
    categories = CATEGORIES

    print("\n" + "*"*45)
    print("      PERSONAL FINANCIAL TRACKER v1.0")
    print("*"*45)
    print("Manage your daily expenses, track your budget")
    print("by category, and view monthly summaries.")
    print("*"*45)

    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses, categories)

        elif choice == "2":
            print("Viewing expenses...")
            view_expenses_menu(expenses)

        elif choice == "3":
            view_summary(expenses)

        elif choice == "4":
            view_delete_expense_menu(expenses)

        elif choice == "5":
            print("\n" + "="*45)
            print("   THANK YOU FOR USING FINANCIAL TRACKER!")
            print("   Your data is safe. See you next time!")
            print("="*45 + "\n")
            break
        else:
            print("Invalid option. Please try again.")

        
if __name__ == "__main__":
    main()