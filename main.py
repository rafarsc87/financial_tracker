# main.py
"""
This is the main entry point of the application. It will display the main menu and handle user
input to navigate through the different features of the application. 
It will also load the expenses from the storage module and 
pass them to the appropriate functions when needed.
The main function in this module is main(), which will be called when the program is run.
"""


from datetime import datetime
from typing import List, Dict
from add_expense import add_expense, categories_list
from storage import load_expenses
from view_expenses import get_expenses_by_category, get_expenses_by_month
from display_expenses import render_header, render_table, render_summary_box, wait_for_user
from calculate_summary import calculate_summary


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
    render_table(filtered_expenses)


def handle_category_filter(expenses: List[Dict]) -> None:
    """
    Prompts the user to select a category and displays filtered expenses in a table.
    """
    categories = categories_list()
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
    render_table(filtered_expenses)


def handle_summary_by_category(expenses: List[Dict]) -> None:
    """
    Displays the total expenditure for a specific user-selected category.
    """
    categories = categories_list()
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
            total, category_totals = calculate_summary(filtered_expenses, categories_list())
            print(f"\n--- Summary for {month} ---")
            print(f"Grand Total: ${total:.2f}")
            for category, total in category_totals.items():
                print(f"  {category:<15}: ${total:>8.2f}")
            wait_for_user()
            break
        except ValueError:
            print("Invalid date format. Please enter a valid date (YYYY-MM).")
        


def show_menu() -> str:
    """
    Renders the main menu and returns the user's choice.
    """
    render_header("Main Menu", "=")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Summary")
    print("4. Exit")
    return input("Choose an option: ")


def view_expenses_menu(expenses: List[Dict]) -> None:
    """
    Handles the navigation for the expense viewing sub-menu.
    """
    while True:
            render_header("View Options", "-")
            print("1. View all expenses")
            print("2. View expenses by month or category")
            print("3. Return to main menu")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                render_table(expenses)
            elif choice == "2":
                while True:
                    print("Filter by:")
                    print("1. Month")
                    print("2. Category")
                    print("3. Return to previous menu")
                    
                    filter_choice = input("Choose an option: ")
                    
                    if filter_choice == "1":
                        handle_month_filter(expenses)

                    elif filter_choice == "2":
                        handle_category_filter(expenses)

                    elif filter_choice == "3":
                        break
                    else:
                        print("Invalid option. Please try again.")
            elif choice == "3":
                print("Returning to main menu...")
                break
            else:
                print("Invalid option. Please try again.")


def view_summary(expenses: List[Dict]) -> None:
    """
    Handles the navigation for the financial summary sub-menu.
    """
    while True:
        render_header("Summary Options", "-")
        print("1. Total Expenses")
        print("2. Expenses by Category")
        print("3. Expenses by Month")
        print("4. Return to main menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            total_expenses, _ = calculate_summary(expenses, categories_list())
            render_summary_box("GRAND TOTAL", total_expenses)
            wait_for_user()
        elif choice == "2":
            handle_summary_by_category(expenses)
        elif choice == "3":
            handle_summary_by_month(expenses)
        elif choice == "4":
            print("Returning to main menu...")
            break
    


def main() -> None:
    """
    Main entry point of the application. Handles data loading and main loop.
    """
    expenses = load_expenses("expenses.json")
    
    categories = categories_list()

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
            print("\n" + "="*45)
            print("   THANK YOU FOR USING FINANCIAL TRACKER!")
            print("   Your data is safe. See you next time!")
            print("="*45 + "\n")
            break
        else:
            print("Invalid option. Please try again.")

        
if __name__ == "__main__":
    main()