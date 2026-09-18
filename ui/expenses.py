import customtkinter as ctk

class ExpensesFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=10)
        self.label = ctk.CTkLabel(self, text="Expense Tracker", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)
