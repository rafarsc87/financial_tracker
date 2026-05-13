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
