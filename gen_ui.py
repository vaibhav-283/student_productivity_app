import os

base_dir = r'C:\Users\User\.gemini\antigravity\scratch\student_productivity_dashboard'

def make_file(path, content=''):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

ui_dashboard = r'''
import customtkinter as ctk
from database.database import get_connection

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.label = ctk.CTkLabel(self, text="Welcome to your Dashboard!", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, pady=20)
        
        self.stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.stats_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        self.study_label = ctk.CTkLabel(self.stats_frame, text="Total Study Hours\n0 hrs", font=ctk.CTkFont(size=16))
        self.study_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.tasks_label = ctk.CTkLabel(self.stats_frame, text="Completed Tasks\n0", font=ctk.CTkFont(size=16))
        self.tasks_label.grid(row=0, column=1, padx=20, pady=10)

    def refresh_data(self):
        # Refresh logic here connecting to sqlite
        pass
'''

ui_study = r'''
import customtkinter as ctk

class StudyTrackerFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Study Tracker", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
'''

ui_tasks = r'''
import customtkinter as ctk

class TaskManagerFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Task Manager", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
'''

ui_attendance = r'''
import customtkinter as ctk

class AttendanceFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Attendance Tracker", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
'''

ui_expenses = r'''
import customtkinter as ctk

class ExpensesFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Expense Tracker", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
'''

ui_analytics = r'''
import customtkinter as ctk

class AnalyticsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Analytics", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
        
    def refresh_charts(self):
        pass
'''

ui_settings = r'''
import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Settings", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
'''

make_file('ui/dashboard.py', ui_dashboard)
make_file('ui/study_tracker.py', ui_study)
make_file('ui/task_manager.py', ui_tasks)
make_file('ui/attendance.py', ui_attendance)
make_file('ui/expenses.py', ui_expenses)
make_file('ui/analytics.py', ui_analytics)
make_file('ui/settings.py', ui_settings)

print("UI components created.")
