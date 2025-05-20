import tkinter as tk
from modules.admin.crear_encuesta import CrearEncuestaWindow
from modules.admin.admin_view import AdminResultsWindow

class DashboardAdmin:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Panel de Administración")
        self.root.geometry("800x600")
        self.root.configure(bg="#ecf0f1")
        self.username = username
        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text=f"Bienvenido Admin: {self.username}",
                 font=("Helvetica", 16, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=20)

        btn_frame = tk.Frame(self.root, bg="#ecf0f1")
        btn_frame.pack(pady=30)

        tk.Button(btn_frame, text="Crear Encuesta", font=("Helvetica", 12),
                  width=25, command=self.crear_encuesta).pack(pady=10)

        tk.Button(btn_frame, text="Ver Resultados", font=("Helvetica", 12),
                  width=25, command=self.ver_resultados).pack(pady=10)

        tk.Button(btn_frame, text="Gestionar Usuarios", font=("Helvetica", 12),
                  width=25, command=self.gestionar_usuarios).pack(pady=10)

        tk.Button(btn_frame, text="Cerrar Sesión", font=("Helvetica", 12),
                  width=25, command=self.cerrar_sesion).pack(pady=20)

    def crear_encuesta(self):
        nueva_ventana = tk.Toplevel(self.root)
        CrearEncuestaWindow(nueva_ventana, self.username)

    def ver_resultados(self):
        ventana = tk.Toplevel(self.root)
        AdminResultsWindow(ventana)
        
    def cerrar_sesion(self):
        from modules.login import LoginWindow
        self.root.destroy()
        ventana_login = tk.Tk()
        LoginWindow(ventana_login)
        ventana_login.mainloop()

    def gestionar_usuarios(self):
        tk.messagebox.showinfo("Gestionar Usuarios", "Aquí se gestionarán los usuarios (implementación pendiente).")
