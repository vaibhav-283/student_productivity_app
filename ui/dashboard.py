import customtkinter as ctk
from database.database import get_connection
import sqlite3

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.controller = controller
        
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Title
        self.title_label = ctk.CTkLabel(self, text="Dashboard Overview", font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky="nw", padx=20)
        
        # Stats Cards
        self.card_study = self.create_card(1, 0, "📚 Total Study Hours", "0 hrs", "green")
        self.card_tasks = self.create_card(1, 1, "✅ Completed Tasks", "0", "blue")
        self.card_attendance = self.create_card(1, 2, "📅 Average Attendance", "0%", "orange")
        
        self.card_expenses = self.create_card(2, 0, "💰 Monthly Expenses", "$0", "red")
        self.card_productivity = self.create_card(2, 1, "🎯 Productivity Score", "0%", "purple")
        self.card_pending = self.create_card(2, 2, "📝 Pending Tasks", "0", "yellow")
        
        # Priorities Section
        self.priorities_frame = ctk.CTkFrame(self, corner_radius=10)
        self.priorities_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)
        
        ctk.CTkLabel(self.priorities_frame, text="🎯 TODAY'S PRIORITIES", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10, padx=20, anchor="w")
        
        self.priorities_text = ctk.CTkTextbox(self.priorities_frame, height=100, wrap="word", state="disabled", fg_color="transparent")
        self.priorities_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def create_card(self, row, col, title, value, color):
        frame = ctk.CTkFrame(self, corner_radius=10)
        frame.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        
        lbl_title = ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=14))
        lbl_title.pack(pady=(20, 5))
        
        lbl_value = ctk.CTkLabel(frame, text=value, font=ctk.CTkFont(size=28, weight="bold"))
        lbl_value.pack(pady=(5, 20))
        
        return lbl_value # Return the value label so we can update it

    def refresh_data(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Study Hours
        cursor.execute("SELECT SUM(duration_minutes) FROM study_sessions")
        total_mins = cursor.fetchone()[0] or 0
        self.card_study.configure(text=f"{total_mins/60:.1f} hrs")
        
        # Completed Tasks
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'Completed'")
        completed = cursor.fetchone()[0]
        self.card_tasks.configure(text=str(completed))
        
        # Pending Tasks
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE status != 'Completed'")
        pending = cursor.fetchone()[0]
        self.card_pending.configure(text=str(pending))
        
        # Attendance
        cursor.execute("SELECT SUM(classes_attended), SUM(total_classes) FROM attendance")
        att_data = cursor.fetchone()
        if att_data[1] and att_data[1] > 0:
            avg_att = (att_data[0] / att_data[1]) * 100
            self.card_attendance.configure(text=f"{avg_att:.1f}%")
        else:
            self.card_attendance.configure(text="N/A")
            
        # Expenses (Current Month roughly)
        cursor.execute("SELECT SUM(amount) FROM expenses")
        exp = cursor.fetchone()[0] or 0
        self.card_expenses.configure(text=f"${exp:.2f}")
        
        # Priorities Logic
        priorities = ""
        cursor.execute("SELECT title, deadline FROM tasks WHERE status != 'Completed' ORDER BY deadline LIMIT 3")
        for task in cursor.fetchall():
            priorities += f"🔴 Complete Task: {task[0]} (Due: {task[1]})\n"
            
        if not priorities:
            priorities = "✅ You're all caught up! Consider doing some extra studying."
            
        self.priorities_text.configure(state="normal")
        self.priorities_text.delete("1.0", "end")
        self.priorities_text.insert("1.0", priorities)
        self.priorities_text.configure(state="disabled")
        
        conn.close()
