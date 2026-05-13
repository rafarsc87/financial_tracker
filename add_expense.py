# add_expense.py
"""
This module handles the creation and validation of new expense entries.
It manages user input for expense details and ensures data is persisted.
"""

from datetime import datetime
from typing import List, Dict
from storage import save_expenses

def categories_list() -> List[str]:
    """
    Returns a list of predefined expense categories.
    
    Returns:
        List[str]: A list containing the valid category names.
    """
    return ["Food", "Transport", "Entertainment", "Utilities"]


def add_expense(expenses: List[Dict], categories: List[str]) -> None:
    """
    Interactive prompt to collect expense data from the user and update the list.
    
    Args:
        expenses (List[Dict]): The current list of expense dictionaries.
        categories (List[str]): The list of allowed categories for validation.
    """
    name = input("Enter expense name: ")
    
    while True:
        try:
            amount = float(input("Enter expense amount (ex: 10.50): $"))
            if amount <= 0:
                print("Amount cannot be zero or negative. Please enter a valid number.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    while True:
        
        print("\nAvailable categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        choice = input(f"Choose a category (1-{len(categories)}): ").strip()
        if choice.isdigit():
            choice_idx = int(choice)
            if 1 <= choice_idx <= len(categories):
                category = categories[choice_idx - 1]
                break
        print("Invalid choice. Please select a valid number.")
    
    while True:
        try:
            date = input("Enter expense date (YYYY-MM): ")
            datetime.strptime(date, "%Y-%m")
            break
        except ValueError:
            print("Invalid date format. Please enter a valid date (YYYY-MM).")
    
    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }
    
    expenses.append(expense)
    expenses.sort(key=lambda x: x["date"], reverse=False) 
    save_expenses("expenses.json", expenses)

    print("\n>>> Expense added successfully! <<<\n")
    

def print_expenses(expenses: List[Dict]) -> None: 
    """
    A debug utility to print raw expense details to the console.
    
    Args:
        expenses (List[Dict]): The list of expenses to print.
    """
    for expense in expenses:
        print(f"Name: {expense['name']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")
        print("-" * 20)
