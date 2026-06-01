#delete_expense.py
"""
Module responsible for the deletion logic of expense records.
Ensures that the data is updated in the storage after a removal.
"""

from typing import List, Dict
from constants import EXPENSES_FILE
from storage import save_expenses


def delete_expense_by_index(expenses: List[Dict], index: int) -> Dict:
    """
    Removes an expense record from the list based on the provided index.
    
    Args:
        expenses (List[Dict]): The current list of expense records.
        index (int): The 0-based index of the expense to be removed.
        
    Returns:
        Dict: The expense record that was successfully deleted.
    """
    
            
    deleted_expense = expenses.pop(index)
    save_expenses(EXPENSES_FILE, expenses)
            
    return deleted_expense
