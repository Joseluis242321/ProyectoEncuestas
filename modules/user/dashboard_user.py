import tkinter as tk
from tkinter import messagebox

class DashboardUser:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Panel del Usuario")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f6fa")
        self.username = username
        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text=f"Bienvenido Usuario: {self.username}",
                 font=("Helvetica", 16, "bold"), bg="#f5f6fa", fg="#2c3e50").pack(pady=20)

        btn_frame = tk.Frame(self.root, bg="#f5f6fa")
        btn_frame.pack(pady=40)

        tk.Button(btn_frame, text="Responder Encuesta", font=("Helvetica", 12),
                  width=30, command=self.responder_encuesta).pack(pady=15)

        tk.Button(btn_frame, text="Cerrar Sesión", font=("Helvetica", 12),
                  width=30, command=self.root.destroy).pack(pady=20)

    def responder_encuesta(self):
        messagebox.showinfo("Responder Encuesta", "Aquí se responderá la encuesta (implementación pendiente).")
