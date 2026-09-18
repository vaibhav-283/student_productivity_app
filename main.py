import customtkinter as ctk
from database.database import init_db
from ui.dashboard import DashboardFrame
from ui.study_tracker import StudyTrackerFrame
from ui.task_manager import TaskManagerFrame
from ui.attendance import AttendanceFrame
from ui.expenses import ExpensesFrame
from ui.analytics import AnalyticsFrame
from ui.settings import SettingsFrame

# Set appearance mode and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class StudentProductivityApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Productivity Dashboard")
        self.geometry("1000x700")
        
        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Initialize Database
        init_db()

        # Navigation Sidebar
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Productivity Hub",
                                                   font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Sidebar Buttons
        self.btn_dashboard = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="🏠 Dashboard",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.show_dashboard)
        self.btn_dashboard.grid(row=1, column=0, sticky="ew")

        self.btn_study = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="📚 Study Tracker",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_study)
        self.btn_study.grid(row=2, column=0, sticky="ew")
        
        self.btn_tasks = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="✅ Tasks",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_tasks)
        self.btn_tasks.grid(row=3, column=0, sticky="ew")
        
        self.btn_attendance = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="📅 Attendance",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_attendance)
        self.btn_attendance.grid(row=4, column=0, sticky="ew")

        self.btn_expenses = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="💰 Expenses",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_expenses)
        self.btn_expenses.grid(row=5, column=0, sticky="ew")

        self.btn_analytics = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="📊 Analytics",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_analytics)
        self.btn_analytics.grid(row=6, column=0, sticky="ew")

        self.btn_settings = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="⚙ Settings",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_settings)
        self.btn_settings.grid(row=7, column=0, sticky="ew")
        
        # Profile Info
        self.profile_label = ctk.CTkLabel(self.navigation_frame, text="Student Profile\nComputer Science\nSemester 1", font=ctk.CTkFont(size=12))
        self.profile_label.grid(row=8, column=0, padx=20, pady=20, sticky="s")


        # Create Frames
        self.frames = {}
        
        self.frames["dashboard"] = DashboardFrame(self, self)
        self.frames["study"] = StudyTrackerFrame(self, self)
        self.frames["tasks"] = TaskManagerFrame(self, self)
        self.frames["attendance"] = AttendanceFrame(self, self)
        self.frames["expenses"] = ExpensesFrame(self, self)
        self.frames["analytics"] = AnalyticsFrame(self, self)
        self.frames["settings"] = SettingsFrame(self, self)
        
        # Default view
        self.show_dashboard()

    def select_button(self, name):
        buttons = [self.btn_dashboard, self.btn_study, self.btn_tasks, self.btn_attendance, self.btn_expenses, self.btn_analytics, self.btn_settings]
        for btn in buttons:
            btn.configure(fg_color="transparent")
        
        if name == "dashboard": self.btn_dashboard.configure(fg_color=("gray75", "gray25"))
        elif name == "study": self.btn_study.configure(fg_color=("gray75", "gray25"))
        elif name == "tasks": self.btn_tasks.configure(fg_color=("gray75", "gray25"))
        elif name == "attendance": self.btn_attendance.configure(fg_color=("gray75", "gray25"))
        elif name == "expenses": self.btn_expenses.configure(fg_color=("gray75", "gray25"))
        elif name == "analytics": self.btn_analytics.configure(fg_color=("gray75", "gray25"))
        elif name == "settings": self.btn_settings.configure(fg_color=("gray75", "gray25"))

    def hide_all_frames(self):
        for frame in self.frames.values():
            frame.grid_forget()

    def show_dashboard(self):
        self.hide_all_frames()
        self.select_button("dashboard")
        self.frames["dashboard"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.frames["dashboard"].refresh_data()

    def show_study(self):
        self.hide_all_frames()
        self.select_button("study")
        self.frames["study"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_tasks(self):
        self.hide_all_frames()
        self.select_button("tasks")
        self.frames["tasks"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_attendance(self):
        self.hide_all_frames()
        self.select_button("attendance")
        self.frames["attendance"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_expenses(self):
        self.hide_all_frames()
        self.select_button("expenses")
        self.frames["expenses"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_analytics(self):
        self.hide_all_frames()
        self.select_button("analytics")
        self.frames["analytics"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.frames["analytics"].refresh_charts()

    def show_settings(self):
        self.hide_all_frames()
        self.select_button("settings")
        self.frames["settings"].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)


if __name__ == "__main__":
    app = StudentProductivityApp()
    app.mainloop()
