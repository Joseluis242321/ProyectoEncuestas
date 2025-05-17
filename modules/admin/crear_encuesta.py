import tkinter as tk
from tkinter import messagebox
from models.encuesta import Encuesta


class CrearEncuestaWindow:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.encuesta_model = Encuesta()

        self.root.title("Crear Encuesta")
        self.root.geometry("700x600")
        self.root.configure(bg="#ecf0f1")

        self.preguntas = []

        self.setup_gui()

    def setup_gui(self):
        font_label = ("Helvetica", 11)
        font_entry = ("Helvetica", 11)

        tk.Label(self.root, text="Título de la Encuesta:", bg="#ecf0f1", font=font_label).pack(anchor="w", padx=20, pady=(10, 0))
        self.titulo_entry = tk.Entry(self.root, font=font_entry)
        self.titulo_entry.pack(fill="x", padx=20)

        tk.Label(self.root, text="Descripción:", bg="#ecf0f1", font=font_label).pack(anchor="w", padx=20, pady=(10, 0))
        self.descripcion_entry = tk.Entry(self.root, font=font_entry)
        self.descripcion_entry.pack(fill="x", padx=20)

        tk.Button(self.root, text="Agregar Pregunta", command=self.agregar_pregunta, bg="#2980b9", fg="white").pack(pady=10)

        self.preguntas_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.preguntas_frame.pack(fill="both", expand=True, padx=20)

        tk.Button(self.root, text="Guardar Encuesta", command=self.guardar_encuesta, bg="#27ae60", fg="white").pack(pady=10)

    def agregar_pregunta(self):
        frame = tk.Frame(self.preguntas_frame, bg="#dfe6e9", pady=5, padx=5, bd=1, relief="groove")
        frame.pack(fill="x", pady=5)

        entry = tk.Entry(frame, font=("Helvetica", 11), width=40)
        entry.pack(side="left", padx=(0, 10))

        tipo_var = tk.StringVar(value="Texto")
        tipo_menu = tk.OptionMenu(frame, tipo_var, "Texto", "Opción Múltiple", command=lambda _: mostrar_opciones())
        tipo_menu.config(width=15)
        tipo_menu.pack(side="left", padx=(0, 10))

        eliminar_btn = tk.Button(frame, text="X", command=lambda: self.eliminar_pregunta(frame), bg="#e74c3c", fg="white")
        eliminar_btn.pack(side="left")

        opciones_frame = tk.Frame(frame, bg="#bdc3c7")
        opciones_frame.pack(fill="x", padx=10, pady=5)
        opciones_frame.pack_forget()  # Oculto por defecto

        opciones_list = []

        def agregar_opcion():
            opcion_frame = tk.Frame(opciones_frame, bg="#ecf0f1")
            opcion_frame.pack(fill="x", pady=2)

            opcion_entry = tk.Entry(opcion_frame, font=("Helvetica", 10), width=50)
            opcion_entry.pack(side="left", padx=(5, 10))

            eliminar_opcion_btn = tk.Button(opcion_frame, text="Eliminar", command=opcion_frame.destroy, bg="#c0392b", fg="white")
            eliminar_opcion_btn.pack(side="left")

            opciones_list.append(opcion_entry)

        def mostrar_opciones():
            if tipo_var.get() == "Opción Múltiple":
                opciones_frame.pack(fill="x", padx=10, pady=5)
                agregar_btn.pack()
            else:
                opciones_frame.pack_forget()
                agregar_btn.pack_forget()

        agregar_btn = tk.Button(opciones_frame, text="Agregar Opción", command=agregar_opcion, bg="#2980b9", fg="white")
        agregar_btn.pack_forget()

        self.preguntas.append((entry, tipo_var, opciones_list))

    def eliminar_pregunta(self, frame):
        frame.destroy()
        self.preguntas = [p for p in self.preguntas if p[0].winfo_exists()]

    def guardar_encuesta(self):
        titulo = self.titulo_entry.get().strip()
        descripcion = self.descripcion_entry.get().strip()

        if not titulo or not descripcion:
            messagebox.showwarning("Campos requeridos", "Título y descripción son obligatorios.")
            return

        if not self.preguntas:
            messagebox.showwarning("Sin preguntas", "Debes agregar al menos una pregunta.")
            return

        preguntas_finales = []
        for entry, tipo_var, opciones_widgets in self.preguntas:
            texto = entry.get().strip()
            tipo = tipo_var.get().lower()

            if not texto:
                continue

            opciones = []
            if tipo == "opción múltiple":
                for ow in opciones_widgets:
                    if ow.winfo_exists():
                        valor = ow.get().strip()
                        if valor:
                            opciones.append(valor)

                if len(opciones) < 2:
                    messagebox.showwarning("Opciones insuficientes", f"La pregunta '{texto}' debe tener al menos 2 opciones.")
                    return

            preguntas_finales.append({
                "texto": texto,
                "tipo": "opcion" if tipo == "opción múltiple" else "texto",
                "opciones": opciones
            })

        if not preguntas_finales:
            messagebox.showwarning("Validación", "Todas las preguntas están vacías.")
            return

        self.encuesta_model.crear_encuesta(titulo, descripcion, self.usuario, preguntas_finales)
        messagebox.showinfo("Éxito", "Encuesta guardada correctamente.")
        self.root.destroy()
