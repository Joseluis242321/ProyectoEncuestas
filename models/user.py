from db.mongo_connection import MongoConnection

class User:
    def __init__(self):
        self.db = MongoConnection().get_collection("usuarios")

    def validar_usuario(self, username, password):
        return self.db.find_one({"username": username, "password": password})

    def crear_usuario(self, username, password, rol):
        if self.db.find_one({"username": username}):
            return False
        self.db.insert_one({"username": username, "password": password, "rol": rol})
        return True
