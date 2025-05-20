import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from modules.user.responder_encuesta import ResponderEncuestaWindow

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
                  width=30, command=self.cerrar_sesion).pack(pady=20)

    def responder_encuesta(self):
        ventana = tk.Toplevel(self.root)
        ResponderEncuestaWindow(ventana, self.username)

    def cerrar_sesion(self):
        from modules.login import LoginWindow
        self.root.destroy()
        ventana_login = tk.Tk()
        LoginWindow(ventana_login)
        ventana_login.mainloop()