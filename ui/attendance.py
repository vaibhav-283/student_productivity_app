import customtkinter as ctk
from database.database import get_connection
import tkinter as tk
from tkinter import ttk

class AttendanceFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        self.header_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.header_frame, text="Attendance Tracker", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, sticky="w")
        self.btn_add = ctk.CTkButton(self.header_frame, text="+ Add Subject", command=self.add_subject_dialog)
        self.btn_add.grid(row=0, column=2, sticky="e")
        
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("Subject", "Attended", "Total", "Percentage"), show="headings")
        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Attended", text="Classes Attended")
        self.tree.heading("Total", text="Total Classes")
        self.tree.heading("Percentage", text="Attendance %")
        self.tree.pack(fill="both", expand=True)
        
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        
        self.btn_attend = ctk.CTkButton(self.actions_frame, text="Mark Attended (+1/+1)", fg_color="green", command=lambda: self.update_att(1, 1))
        self.btn_attend.pack(side="left", padx=(0, 10))
        
        self.btn_miss = ctk.CTkButton(self.actions_frame, text="Mark Missed (0/+1)", fg_color="red", command=lambda: self.update_att(0, 1))
        self.btn_miss.pack(side="left")
        
        self.refresh_table()

    def refresh_table(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT subject, classes_attended, total_classes FROM attendance")
        for row in cursor.fetchall():
            pct = (row[1] / row[2] * 100) if row[2] > 0 else 0
            self.tree.insert("", "end", values=(row[0], row[1], row[2], f"{pct:.1f}%"))
        conn.close()
        
    def update_att(self, attended, total):
        selected = self.tree.selection()
        if not selected: return
        subject = self.tree.item(selected[0])['values'][0]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE attendance SET classes_attended = classes_attended + ?, total_classes = total_classes + ? WHERE subject = ?", (attended, total, subject))
        conn.commit()
        conn.close()
        self.refresh_table()

    def add_subject_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add Subject")
        dialog.geometry("300x200")
        
        ctk.CTkLabel(dialog, text="Subject Name").pack(pady=(10, 0))
        entry_subject = ctk.CTkEntry(dialog, width=200)
        entry_subject.pack()
        
        def save():
            subject = entry_subject.get()
            if subject:
                conn = get_connection()
                try:
                    conn.cursor().execute("INSERT INTO attendance (subject, classes_attended, total_classes) VALUES (?, 0, 0)", (subject,))
                    conn.commit()
                except: pass
                conn.close()
                self.refresh_table()
                dialog.destroy()
                
        ctk.CTkButton(dialog, text="Save", command=save).pack(pady=20)
