# storage.py
"""
This module handles data persistence, including loading and saving
expenses to a JSON file.
"""

import json
from typing import List, Dict


def load_expenses(filename: str) -> List[Dict]:
    """
    Loads the expense data from a JSON file.
    
    Args:
        filename (str): The path to the JSON file.
        
    Returns:
        List[Dict]: A list of expense records, or an empty list if the file is missing.
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def save_expenses(filename: str, expenses: List[Dict]) -> None:
    """
    Saves the list of expenses to a JSON file with indentation.
    
    Args:
        filename (str): The path where the JSON file will be saved.
        expenses (List[Dict]): The list of expenses to persist.
    """
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)
    


if __name__ == "__main__":
    expenses = [
        {
            "name": "Lunch",
            "amount": 35.5,
            "category": "Food",
            "date": "2023-04"
        }
    ]
    filename = "expenses.json"
    save_expenses(filename, expenses)
    expenses = load_expenses(filename)
    print(expenses)