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
        encuestas = list(db['encuestas'].find())
        respuestas = list(db['respuestas'].find())

        resumen_total = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        for r in respuestas:
            encuesta_id = str(r.get("encuesta_id"))
            pregunta = r.get("pregunta", "Desconocida")
            respuesta = r.get("respuesta", "Sin respuesta")
            resumen_total[encuesta_id][pregunta][respuesta] += 1

        for encuesta in encuestas:
            eid = str(encuesta['_id'])
            self.text.insert(tk.END, f"\n📋 Encuesta: {encuesta.get('titulo', 'Sin título')}\n")
            self.text.insert(tk.END, f"📝 Descripción: {encuesta.get('descripcion', '')}\n\n")

            resumen = resumen_total.get(eid, {})
            for pregunta, respuestas in resumen.items():
                self.text.insert(tk.END, f"❓ {pregunta}\n")
                for resp, count in respuestas.items():
                    self.text.insert(tk.END, f"    ➤ {resp}: {count} respuesta(s)\n")
                self.text.insert(tk.END, "\n")
