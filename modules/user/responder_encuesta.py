import tkinter as tk
from tkinter import messagebox
from db.mongo_connection import MongoConnection as db # Asegúrate de tener esta función correctamente
from bson import ObjectId

class ResponderEncuestaWindow:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.root.title("Responder Encuesta")
        self.root.geometry("600x500")
        self.db = db.db_connect()
        self.setup_gui()

    def setup_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Seleccione una encuesta:", font=("Helvetica", 12, "bold")).pack(pady=10)
        self.lista = tk.Listbox(self.root, width=60)
        self.lista.pack(pady=10)

        self.encuestas = list(self.db.encuestas.find({"estado": "activa"}))
        
        for e in self.encuestas:
            self.lista.insert(tk.END, f"{e['titulo']} - {e['descripcion']}")

        tk.Button(self.root, text="Responder", bg="#27ae60", fg="white", command=self.cargar_encuesta).pack(pady=10)

    def cargar_encuesta(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Debes seleccionar una encuesta.")
            return

        encuesta = self.encuestas[seleccion[0]]
        self.mostrar_formulario(encuesta)

    def mostrar_formulario(self, encuesta):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.preguntas_widgets = []

        tk.Label(self.root, text=f"Encuesta: {encuesta['titulo']}", font=("Helvetica", 14, "bold")).pack(pady=10)

        for i, p in enumerate(encuesta.get("preguntas", [])):
            tk.Label(self.root, text=f"{i+1}. {p['texto']}", font=("Helvetica", 11)).pack(anchor="w", padx=20, pady=5)

            if p["tipo"] == "texto":
                entry = tk.Entry(self.root, width=60)
                entry.pack(padx=20)
                self.preguntas_widgets.append(("texto", p["texto"], entry))
            elif p["tipo"] == "opcion":
                var = tk.StringVar()
                for opcion in p.get("opciones", []):
                    tk.Radiobutton(self.root, text=opcion, variable=var, value=opcion).pack(anchor="w", padx=40)
                self.preguntas_widgets.append(("opcion", p["texto"], var))

        tk.Button(self.root, text="Enviar Respuestas", bg="#2980b9", fg="white",
                  command=lambda: self.enviar_respuestas(encuesta)).pack(pady=15)
    def enviar_respuestas(self, encuesta):
        respuestas_colectadas = []
        for tipo, texto, widget in self.preguntas_widgets:
            valor = widget.get().strip()
            if not valor:
                messagebox.showerror("Error", "Todas las preguntas deben ser respondidas.")
                return
            respuestas_colectadas.append({"pregunta": texto, "respuesta": valor})

        # Agregar al array "respuestas" del documento encuesta
        self.db.encuestas.update_one(
            {"_id": ObjectId(encuesta["_id"])},
            {"$push": {
                "respuestas": {
                    "usuario": self.usuario,
                    "respuestas": respuestas_colectadas
                }
            }}
        )

        messagebox.showinfo("Gracias", "Tus respuestas han sido registradas.")
        self.root.destroy()