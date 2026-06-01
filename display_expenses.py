# display_expenses.py
"""
Utility module for UI rendering components such as headers, 
tables, and summary boxes for the CLI.
"""

from typing import List, Dict


def render_header(title: str, style: str = "=") -> None:
    """
    Prints a stylized header to divide menu sections.
    """
    print("\n" + style * 45)
    print(f"   {title.upper()}")
    print(style * 45)


def render_summary_box(title: str, value: float) -> None:
    """
    Prints a highlighted box for financial totals.
    """
    print("\n" + "#" * 30)
    print(f"  {title}: ${value:,.2f}")
    print("#" * 30)


def wait_for_user() -> None:
    """
    Pauses execution until the user presses Enter.
    """
    input("\nPress Enter to continue...")


def render_table(expenses: List[Dict], show_index: bool = True) -> None:
    """
    Displays expense records in a formatted table.

    Args:
        expenses (List[Dict]): Expense records to display.
        show_index (bool): Whether to display row numbers.
    """
    if not expenses:
        print("\n[!] No records found to display.")
        return

    if show_index:
        print(f"\n{'No.':<5} | {'Name':<20} | {'Amount':<10} | {'Category':<15} | {'Date':<10}")
        print("-" * 80)
        for i, e in enumerate(expenses, 1):
            print(f"{i:<5} | {e['name']:<20} | ${e['amount']:<9.2f} | {e['category']:<15} | {e['date']:<10}")
        print("-" * 80)
    else:     
        print(f"\n{'Name':<20} | {'Amount':<10} | {'Category':<15} | {'Date':<10}")
        print("-" * 65)
        for e in expenses:
            print(f"{e['name']:<20} | ${e['amount']:<9.2f} | {e['category']:<15} | {e['date']:<10}")
        print("-" * 65)