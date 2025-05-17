from db.mongo_connection import MongoConnection
from bson import ObjectId

class Encuesta:
    def __init__(self):
        self.db = MongoConnection().get_collection("encuestas")

    def crear_encuesta(self, titulo, descripcion, creado_por, preguntas):
        encuesta = {
            "titulo": titulo,
            "descripcion": descripcion,
            "preguntas": preguntas,
            "creado_por": creado_por,
            "respuestas": [],
            "estado": "activa"
        }
        resultado = self.db.insert_one(encuesta)
        return str(resultado.inserted_id)

    def obtener_encuestas(self):
        return list(self.db.find())

    def obtener_encuesta_por_id(self, encuesta_id):
        return self.db.find_one({"_id": ObjectId(encuesta_id)})

    def actualizar_encuesta(self, encuesta_id, datos_actualizados):
        self.db.update_one({"_id": ObjectId(encuesta_id)}, {"$set": datos_actualizados})

    def eliminar_encuesta(self, encuesta_id):
        self.db.delete_one({"_id": ObjectId(encuesta_id)})
