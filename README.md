# 🧩 Algorithmic Sudoku Solver with Custom HMI

This project is a desktop application designed to solve complex 9x9 Sudoku puzzles. It showcases core engineering skills in **algorithmic implementation**, **data workflow management**, and **Human-Machine Interface (HMI) design** for non-technical users.

---

## 💻 Technology Stack

| Component | Technology Used | Notes |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core programming language. |
| **GUI Framework** | **Tkinter** | Used to create the attractive and interactive graphical user interface. |
| **Image Integration** | **PILLOW** (PIL) | Used to integrate and manage image assets within the GUI (e.g., icons, logos). |
| **Process Control** | `subprocess` | Used to automatically launch and terminate helper Python scripts (`solver.py`). |

## ✨ Key Features

* **Recursive Algorithm Implementation:** Uses a highly efficient **recursion/backtracking algorithm** to systematically solve the Sudoku grid, demonstrating a strong foundation in structured problem-solving.
* **Data Serialization Workflow:** Manages a clear data pipeline:
    1.  User input is saved to a plain text file (`boarddata.txt`).
    2.  `solver.py` extracts, solves, and saves the solution to a separate file (`board.txt`).
    3.  The main GUI retrieves the final solution for display.
* **Robust Error Handling:** Includes a feature to **decline and provide feedback** when a user enters an unsolvable Sudoku puzzle, confirming systematic logic.
* **Intuitive Interface:** Features an attractive GUI enabling non-coder user interaction, complete with built-in navigation buttons like 'Home', 'Menu', and 'About Us'.

## 🚀 Steps to Run This Solver Locally

1.  **Copy Files:** Copy the entire repository, ensuring all Python files (e.g., `sudoku.py`, `solver.py`) and image assets are included.
2.  **Install Python:** Ensure you have a recent version of Python 3 installed on your system.
3.  **Install Dependencies:** Run the following command to install the required external library:
    ```bash
    pip install Pillow
    ```
    *(Note: Tkinter is included with a standard Python installation.)*
4.  **Execute the Application:** Run the main Python script from your terminal:
    ```bash
    python sudoku.py
    ```
5.  **Interact:** Enter the unsolved Sudoku numbers into the blank spaces and click the solve button to obtain the completed grid.