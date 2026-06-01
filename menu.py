# menu.py

"""
This module contains the main menu rendering and navigation logic for the CLI application.
It defines the main menu structure and the functions to display sub-menus for viewing expenses, calculating summaries, and deleting records. It serves as the central hub for user interaction.
"""
from typing import List, Dict
from display_expenses import render_header, render_table, render_summary_box, wait_for_user
from handlers import handle_month_filter, handle_category_filter, handle_summary_by_category, handle_summary_by_month, handle_delete_expense_by_index
from calculate_summary import calculate_summary
from constants import CATEGORIES


def show_menu() -> str:
    """
    Renders the main menu and returns the user's choice.
    """
    render_header("Main Menu", "=")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Summary")
    print("4. Delete Expense")
    print("5. Exit")
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
                render_table(expenses, show_index=False)
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
            total_expenses, _ = calculate_summary(expenses, CATEGORIES)
            render_summary_box("GRAND TOTAL", total_expenses)
            wait_for_user()
        elif choice == "2":
            handle_summary_by_category(expenses)
        elif choice == "3":
            handle_summary_by_month(expenses)
        elif choice == "4":
            print("Returning to main menu...")
            break
    

def view_delete_expense_menu(expenses: List[Dict]) -> None:
    """
    Handles the navigation for the expense deletion sub-menu.
    """
    while True:
        render_header("Delete Expense", "-")
        print("1. Delete an expense by index")
        print("2. Return to main menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            handle_delete_expense_by_index(expenses)
        elif choice == "2":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option. Please try again.")