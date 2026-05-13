# Software Requirements Specification - Financial Tracker

## 1. Project Overview
A Command Line Interface (CLI) application designed to help users track their monthly expenses, categorize spending, and analyze financial habits through summaries.

## 2. Functional Requirements

### 2.1 Expense Entry
- **FR1:** The system shall allow users to input an expense name.
- **FR2:** The system shall validate that the expense amount is a positive numerical value.
- **FR3:** The system shall allow users to select a category from a predefined list (Food, Transport, Entertainment, Utilities).
- **FR4:** The system shall require a date input in the format `YYYY-MM` and validate it against standard calendar rules.

### 2.2 Data Visualization
- **FR5:** The system shall display a list of all expenses in a formatted table.
- **FR6:** The system shall allow users to filter the expense list by a specific month.
- **FR7:** The system shall allow users to filter the expense list by category.

### 2.3 Financial Summaries
- **FR8:** The system shall calculate the grand total of all recorded expenses.
- **FR9:** The system shall provide a breakdown of total spending per category.
- **FR10:** The system shall generate a monthly report including the total spent and a detailed breakdown by category for that specific period.

### 2.4 Data Persistence
- **FR11:** All data shall be stored in a JSON file (`expenses.json`) to ensure data is retained between sessions.
- **FR12:** The system shall automatically load data from the storage file upon execution.

## 3. Technical Requirements

### 3.1 Environment
- **Language:** Python 3.8+
- **External Dependencies:** None (Standard Library only).

### 3.2 Design Constraints
- **Architecture:** Modular design separating logic (`add`, `view`, `calculate`) from data access (`storage`) and presentation (`display`).
- **Error Handling:** The system must handle invalid user inputs (incorrect dates, non-numeric amounts, invalid menu choices) without crashing.

## 4. User Interface
- **UI1:** The application shall utilize a text-based menu system for navigation.
- **UI2:** The system shall provide visual feedback (e.g., success messages) after data operations.
- **UI3:** Tables and summary boxes shall be used to improve readability of financial data.
