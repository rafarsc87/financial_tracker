# view_expenses.py
"""
Module for displaying and filtering expense data.
"""

from typing import List, Dict


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