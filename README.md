# Financial Tracker CLI Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A Command Line Interface (CLI) application designed to help users track their monthly expenses, categorize spending, and analyze financial habits through summaries. This application provides a simple yet effective way to manage personal finances directly from the terminal.

## ✨ Features

### Expense Entry
-   **Input Details:** Allows users to input an expense name, amount, category, and date.
-   **Amount Validation:** Ensures the expense amount is a positive numerical value.
-   **Category Selection:** Users can select a category from a predefined list (Food, Transport, Entertainment, Utilities).
-   **Date Validation:** Requires a date input in `YYYY-MM` format and validates it against standard calendar rules.

### Data Visualization
-   **Formatted Table Display:** Presents a list of all expenses in a clear, formatted table.
-   **Filter by Month:** Users can filter the expense list to view records from a specific month.
-   **Filter by Category:** Users can filter the expense list to view records belonging to a specific category.

### Financial Summaries
-   **Grand Total:** Calculates and displays the grand total of all recorded expenses.
-   **Category Breakdown:** Provides a detailed breakdown of total spending per category.
-   **Monthly Reports:** Generates a comprehensive monthly report including the total spent and a detailed breakdown by category for that specific period.

### Data Persistence
-   **JSON Storage:** All expense data is stored persistently in a `expenses.json` file.
-   **Automatic Loading:** The system automatically loads existing data from `expenses.json` upon execution, ensuring data is retained between sessions.

## 🚀 Installation

1.  **Prerequisites:** Ensure you have Python 3.8 or higher installed on your system.

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/rafarsc87/financial-tracker.git
    cd financial-tracker
    ```
    *(If you downloaded the files directly, navigate to the project directory.)*

3.  **No External Dependencies:** This project uses only the Python Standard Library. No `pip install` is required.

## 💡 Usage

To run the application, navigate to the project directory in your terminal and execute the `main.py` script:

```bash
python main.py
```

Follow the on-screen menu prompts to interact with the application:
-   Add new expenses.
-   View all expenses or filter them by month/category.
-   Generate financial summaries (total expenses, category breakdown, monthly reports).

## 📂 Project Structure

The application is modularized into several Python files, each responsible for a specific part of the functionality:

-   `main.py`: The primary entry point, managing the main menu and overall application flow.
-   `add_expense.py`: Handles user input for adding new expenses and performs data validation.
-   `view_expenses.py`: Provides functions to display and filter expense records based on various criteria.
-   `display_expenses.py`: Contains UI utility functions for rendering stylized headers, tabular data, and summary boxes.
-   `calculate_summary.py`: Implements the logic for aggregating financial data, calculating grand totals, and category-wise spending.
-   `storage.py`: Manages data persistence, responsible for loading and saving expense records to `expenses.json`.
-   `expenses.json`: (Automatically created/updated) The JSON file where all your expense data is stored.

## 🛠️ Requirements

-   Python 3.8+
-   Standard Library only (no external packages needed)

## 📄 License   
This project is licensed under the MIT License - see the `LICENSE` file for details.

## 👨‍💻 Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-salgado-940ab9406)

## 👨‍💻 Developed By

Rafael Salgado
*Building Python Backend Applications*

