import tkinter as tk
from tkinter import ttk, messagebox
from models.user import User

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuario")
        self.root.geometry("520x380")
        self.root.minsize(480, 360)
        self.root.configure(bg="#f0f4f7")
        self.user_model = User()
        self.setup_gui()

    def setup_gui(self):
        font_title = ("Helvetica", 18, "bold")
        font_label = ("Helvetica", 11)
        font_entry = ("Helvetica", 11)

        tk.Label(self.root, text="Sistema de Encuestas", font=font_title,
                 bg="#f0f4f7", fg="#2c3e50").pack(pady=(15, 5))

        tk.Label(self.root, text="Registro de Usuario", font=("Helvetica", 14),
                 bg="#f0f4f7", fg="#34495e").pack(pady=(0, 10))

        frame = tk.Frame(self.root, bg="white", bd=2, relief="ridge")
        frame.place(relx=0.5, rely=0.55, anchor="center", width=420, height=250)

        tk.Label(frame, text="Nombre de usuario:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(12, 0))
        self.username_entry = tk.Entry(frame, font=font_entry)
        self.username_entry.pack(padx=30, fill="x")

        tk.Label(frame, text="Contraseña:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
        self.password_entry = tk.Entry(frame, font=font_entry, show="*")
        self.password_entry.pack(padx=30, fill="x")

        tk.Label(frame, text="Rol:", font=font_label, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
        self.role_combobox = ttk.Combobox(frame, font=font_entry, values=["user", "admin"], state="readonly")
        self.role_combobox.current(0)
        self.role_combobox.pack(padx=30, fill="x")

        tk.Button(frame, text="Registrar", bg="#16a085", fg="white",
                  font=font_label, command=self.registrar_usuario).pack(pady=18)

    def registrar_usuario(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        rol = self.role_combobox.get().strip().lower()

        if not username or not password or not rol:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        if rol not in ['admin', 'user']:
            messagebox.showerror("Rol inválido", "El rol debe ser 'admin' o 'user'.")
            return

        success = self.user_model.crear_usuario(username, password, rol)
        if not success:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")
            return

        messagebox.showinfo("Registro exitoso", f"Usuario '{username}' registrado como '{rol}'.")
        self.root.destroy()
