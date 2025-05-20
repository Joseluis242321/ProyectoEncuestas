import tkinter as tk
from pymongo import MongoClient
from collections import defaultdict
from bson import ObjectId

class AdminResultsWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Resumen de Encuestas (Admin)")
        self.master.geometry("700x500")

        self.text = tk.Text(master, wrap=tk.WORD)
        self.text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.mostrar_resumen()

    def mostrar_resumen(self):
        
        client = MongoClient('mongodb://localhost:27017/')
        db = client['sistema_encuestas']
        encuestas = db['encuestas'].find()

        for encuesta in encuestas:
            self.text.insert(tk.END, f"\n📋 Encuesta: {encuesta.get('titulo', 'Sin título')}\n")
            self.text.insert(tk.END, f"📝 Descripción: {encuesta.get('descripcion', '')}\n\n")

            resumen = defaultdict(lambda: defaultdict(int))

            for respuesta_usuario in encuesta.get("respuestas", []):
                for r in respuesta_usuario.get("respuestas", []):
                    pregunta = r.get("pregunta", "Pregunta desconocida")
                    respuesta = r.get("respuesta", "Sin respuesta")
                    resumen[pregunta][respuesta] += 1

            for pregunta, respuestas in resumen.items():
                self.text.insert(tk.END, f"❓ {pregunta}\n")
                for resp, count in respuestas.items():
                    self.text.insert(tk.END, f"    ➤ {resp}: {count} respuesta(s)\n")
                self.text.insert(tk.END, "\n")
