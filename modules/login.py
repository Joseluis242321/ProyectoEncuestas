import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from models.user import User
from modules.register import RegisterWindow
from modules.admin.dashboard_admin import DashboardAdmin
from modules.user.dashboard_user import DashboardUser
import os


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Encuestas - Login")
        self.root.geometry("600x500")
        self.root.minsize(500, 350)
        self.root.configure(bg="#f0f4f7")
        self.user_model = User()
        self.setup_gui()

    def setup_gui(self):
        font_title = ("Helvetica", 20, "bold")
        font_header = ("Helvetica", 14, "bold")
        font_label = ("Helvetica", 11)
        font_entry = ("Helvetica", 11)

        main_frame = tk.Frame(self.root, bg="#f0f4f7")
        main_frame.pack(expand=True, fill="both")


        tk.Label(main_frame, text="Sistema de Encuestas", font=font_title,
                bg="#f0f4f7", fg="#2c3e50").pack(pady=(20, 5))

        try:
            ruta_imagen = os.path.join("img", "encuestas.png")
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((120, 120))
            self.logo_img = ImageTk.PhotoImage(imagen)
            tk.Label(main_frame, image=self.logo_img, bg="#f0f4f7").pack(pady=(0, 15))
        except Exception as e:
            print(f"⚠️ No se pudo cargar la imagen: {e}")

        frame = tk.Frame(main_frame, bg="white", bd=2, relief="ridge")
        frame.pack(pady=10)

        tk.Label(frame, text="Iniciar Sesión", font=font_header,
                bg="white", fg="#34495e").pack(pady=10)

        tk.Label(frame, text="Usuario:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(5, 0))
        self.username_entry = tk.Entry(frame, font=font_entry)
        self.username_entry.pack(padx=30, fill="x")

        tk.Label(frame, text="Contraseña:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
        self.password_entry = tk.Entry(frame, font=font_entry, show="*")
        self.password_entry.pack(padx=30, fill="x")

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
