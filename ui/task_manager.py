import customtkinter as ctk
from database.database import get_connection
import tkinter as tk
from tkinter import ttk

class TaskManagerFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        self.header_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.header_frame, text="Task Manager", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, sticky="w")
        
        self.btn_add = ctk.CTkButton(self.header_frame, text="+ Add Task", command=self.add_task_dialog)
        self.btn_add.grid(row=0, column=2, sticky="e")
        
        # Table
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2a2d2e", foreground="white", rowheight=30, fieldbackground="#2a2d2e")
        style.map("Treeview", background=[("selected", "#1f538d")])
        
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Title", "Subject", "Deadline", "Priority", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        
        self.tree.column("ID", width=30)
        self.tree.pack(fill="both", expand=True)
        
        # Action Buttons
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        
        self.btn_complete = ctk.CTkButton(self.actions_frame, text="Mark Complete", fg_color="green", command=self.mark_complete)
        self.btn_complete.pack(side="left", padx=(0, 10))
        
        self.btn_delete = ctk.CTkButton(self.actions_frame, text="Delete Task", fg_color="red", command=self.delete_task)
        self.btn_delete.pack(side="left")
        
        self.refresh_table()

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, subject, deadline, priority, status FROM tasks ORDER BY deadline")
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()
        
    def mark_complete(self):
        selected = self.tree.selection()
        if not selected: return
        task_id = self.tree.item(selected[0])['values'][0]
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        self.refresh_table()
        
    def delete_task(self):
        selected = self.tree.selection()
        if not selected: return
        task_id = self.tree.item(selected[0])['values'][0]
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        self.refresh_table()

    def add_task_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Task")
        dialog.geometry("400x500")
        
        ctk.CTkLabel(dialog, text="Title").pack(pady=(10, 0))
        entry_title = ctk.CTkEntry(dialog, width=200)
        entry_title.pack()
        
        ctk.CTkLabel(dialog, text="Subject").pack(pady=(10, 0))
        entry_subject = ctk.CTkEntry(dialog, width=200)
        entry_subject.pack()
        
        ctk.CTkLabel(dialog, text="Deadline (YYYY-MM-DD)").pack(pady=(10, 0))
        entry_deadline = ctk.CTkEntry(dialog, width=200)
        entry_deadline.pack()
        
        ctk.CTkLabel(dialog, text="Priority").pack(pady=(10, 0))
        priority_var = ctk.StringVar(value="Medium")
        opt_priority = ctk.CTkOptionMenu(dialog, values=["High", "Medium", "Low"], variable=priority_var)
        opt_priority.pack()
        
        def save():
            title = entry_title.get()
            subject = entry_subject.get()
            deadline = entry_deadline.get()
            priority = priority_var.get()
            
            if title and subject and deadline:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO tasks (title, subject, deadline, priority, status) VALUES (?, ?, ?, ?, 'Pending')",
                               (title, subject, deadline, priority))
                conn.commit()
                conn.close()
                self.refresh_table()
                dialog.destroy()
                
        btn_save = ctk.CTkButton(dialog, text="Save Task", command=save)
        btn_save.pack(pady=20)
