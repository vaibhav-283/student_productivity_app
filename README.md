# Student Productivity Dashboard

A modern, interactive desktop application built in Python for college students to track their study sessions, tasks, attendance, and expenses.

## Features
- **Dashboard**: Get an overview of your productivity with a real-time summary.
- **Study Tracker**: Time your study sessions.
- **Task Manager**: Add, track, and complete assignments.
- **Attendance Tracker**: Keep track of your attended classes and percentages.
- **Expense Tracker**: Manage student expenses.
- **Analytics**: Visualize data over time.

## Technology Used
- **Python 3**
- **CustomTkinter**: For a modern dark-themed GUI
- **SQLite3**: For robust data storage
- **Matplotlib**: For chart generation

## Installation Instructions
1. Make sure you have Python 3 installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
```bash
python main.py
```

## Project Structure
The project uses a clean modular structure to separate concerns:
- `database/`: SQLite initialization and connection logic
- `models/`: Data structures
- `ui/`: CustomTkinter interface components
- `main.py`: The entry point that ties everything together

## Concepts Demonstrated
This project demonstrates several core Python concepts:
- Variables, Loops, and Functions
- Object-Oriented Programming (Classes)
- File handling and SQLite Database operations (CRUD)
- GUI programming with CustomTkinter
- Exception handling and data validation
