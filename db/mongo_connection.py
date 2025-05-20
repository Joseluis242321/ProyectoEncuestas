from pymongo import MongoClient

class MongoConnection:
    def __init__(self, uri="mongodb://localhost:27017", db_name="sistema_encuestas"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name):
        return self.db[name]
    
    def db_connect():
        client = MongoClient('mongodb://localhost:27017/')
        db = client['sistema_encuestas']
        return db
