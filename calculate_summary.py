# calculate_summary.py
"""
This module provides logic for aggregating financial data.
It calculates grand totals and categorizes spending for reporting.
"""

import datetime
from typing import List, Dict, Tuple

categories_list: List[str] = ["Food", "Transport", "Entertainment", "Utilities"]


def calculate_summary(expenses: List[Dict], categories_list: List[str]) -> Tuple[float, Dict[str, float]]:
    """
    Calculates the grand total of expenses and a breakdown per category.

    Args:
        expenses (List[Dict]): The list of expense records.
        categories_list (List[str]): The list of categories to aggregate.

    Returns:
        Tuple[float, Dict[str, float]]: A tuple containing the total sum and a dictionary of category totals.
    """
    total_expenses = sum(expense["amount"] for expense in expenses)
    category_totals = {category: float(sum(expense["amount"] for expense in expenses if expense["category"] == category)) for category in categories_list}
    return float(total_expenses), category_totals


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
    
    summary = calculate_summary(expenses_debug, categories_list)

    while True:
        try:
            print("Choosing the summary option...")
            user_choice = input("Choose a summary option (1. Total Expenses, 2. Category Totals, 3.By Month, 4.Exit): ")
            
            if user_choice == "1":
                total_expenses, _ = calculate_summary(expenses_debug, categories_list)
                print(f"Total Expenses: ${total_expenses:.2f}")
            elif user_choice == "2":
                category = input("Enter the category to filter by: ")
                if category not in categories_list:
                    print("Invalid category. Please try again.")
                else:
                    filtered_expenses = [expense for expense in expenses_debug if expense["category"] == category]
                    total_expenses, category_totals = calculate_summary(filtered_expenses, categories_list)
                    print(f"Total Expenses for {category}: ${total_expenses:.2f}")
                    
            elif user_choice == "3":
                month = input("Enter the month to filter by (YYYY-MM): ")
                try:
                    datetime.datetime.strptime(month, "%Y-%m")
                    filtered_expenses = [expense for expense in expenses_debug if expense["date"] == month]
                    total_expenses, category_totals = calculate_summary(filtered_expenses, categories_list)
                    print(f"Total Expenses for {month}: ${total_expenses:.2f}")
                    for category, total in category_totals.items():
                        print(f"{category}: ${total:.2f}")
                except ValueError:
                    print("Invalid date format. Please enter a valid date (YYYY-MM).")
            elif user_choice == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")
            
            continue
        except KeyboardInterrupt:
            print("Exiting program.")
            break