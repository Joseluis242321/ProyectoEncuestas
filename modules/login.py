import tkinter as tk
from tkinter import messagebox
from models.user import User
from modules.register import RegisterWindow
from modules.admin.dashboard_admin import DashboardAdmin
from modules.user.dashboard_user import DashboardUser


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Encuestas - Login")
        self.root.geometry("600x400")
        self.root.minsize(500, 350)
        self.root.configure(bg="#f0f4f7")
        self.user_model = User()
        self.setup_gui()

    def setup_gui(self):
        font_title = ("Helvetica", 20, "bold")
        font_header = ("Helvetica", 14, "bold")
        font_label = ("Helvetica", 11)
        font_entry = ("Helvetica", 11)

        # Título general
        tk.Label(self.root, text="Sistema de Encuestas", font=font_title,
                 bg="#f0f4f7", fg="#2c3e50").pack(pady=20)

        # Marco de login
        frame = tk.Frame(self.root, bg="white", bd=2, relief="ridge")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=260)

        tk.Label(frame, text="Iniciar Sesión", font=font_header,
                 bg="white", fg="#34495e").pack(pady=10)

        # Usuario
        tk.Label(frame, text="Usuario:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(5, 0))
        self.username_entry = tk.Entry(frame, font=font_entry)
        self.username_entry.pack(padx=30, fill="x")

        # Contraseña
        tk.Label(frame, text="Contraseña:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
        self.password_entry = tk.Entry(frame, font=font_entry, show="*")
        self.password_entry.pack(padx=30, fill="x")

        # Botones
        button_frame = tk.Frame(frame, bg="white")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Iniciar Sesión", bg="#27ae60", fg="white",
                  font=font_label, width=14, command=self.login).pack(side="left", padx=10)
        tk.Button(button_frame, text="Registrarse", bg="#2980b9", fg="white",
                  font=font_label, width=14, command=self.abrir_registro).pack(side="left", padx=10)

    def abrir_registro(self):
        reg_window = tk.Toplevel(self.root)
        RegisterWindow(reg_window)
        
    def login(self):
        user = self.username_entry.get().strip()
        pwd = self.password_entry.get().strip()

        if not user or not pwd:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return

        usuario = self.user_model.validar_usuario(user, pwd)

        if usuario:
            rol = usuario['rol']
            self.root.destroy()

            new_root = tk.Tk()
            if rol == "admin":
                DashboardAdmin(new_root, user)
            else:
                DashboardUser(new_root, user)

            new_root.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas o usuario no existe.")
