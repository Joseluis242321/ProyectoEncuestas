import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

class AsignarEncuestaWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Asignar Encuestas a Usuarios")
        self.master.geometry("600x400")
        self.db = MongoClient("mongodb://localhost:27017/")["sistema_encuestas"]

        self.usuarios = [u["username"] for u in self.db["usuarios"].find({"rol": "user"})]
        self.encuestas = list(self.db["encuestas"].find())

        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.master, text="Selecciona una encuesta:", font=("Arial", 12)).pack(pady=10)
        self.encuesta_combo = ttk.Combobox(self.master, state="readonly",
                                           values=[f"{e['titulo']} ({str(e['_id'])[:6]})" for e in self.encuestas])
        self.encuesta_combo.pack()

        tk.Label(self.master, text="Selecciona usuarios:", font=("Arial", 12)).pack(pady=10)
        self.lista_usuarios = tk.Listbox(self.master, selectmode=tk.MULTIPLE, height=10)
        for usuario in self.usuarios:
            self.lista_usuarios.insert(tk.END, usuario)
        self.lista_usuarios.pack(pady=10, fill=tk.X, padx=20)

        tk.Button(self.master, text="Asignar", command=self.asignar_usuarios).pack(pady=20)

    def asignar_usuarios(self):
        idx = self.encuesta_combo.current()
        if idx == -1:
            messagebox.showerror("Error", "Selecciona una encuesta.")
            return

        seleccionados = self.lista_usuarios.curselection()
        if not seleccionados:
            messagebox.showerror("Error", "Selecciona al menos un usuario.")
            return

        encuesta_id = self.encuestas[idx]["_id"]
        usuarios_asignados = [self.lista_usuarios.get(i) for i in seleccionados]

        self.db["encuestas"].update_one(
            {"_id": encuesta_id},
            {"$set": {"dirigido_a": usuarios_asignados}}
        )

        messagebox.showinfo("Éxito", "Encuesta asignada a usuarios correctamente.")
        self.master.destroy()
