from pymongo import MongoClient

# Configuración
MONGODB_URI = "mongodb://localhost:27017"
DB_NAME = "sistema_encuestas"

class MongoConnection:
    def __init__(self, uri=MONGODB_URI, db_name=DB_NAME):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        print(f"Connected to {self.db.name}")
        
    def get_collection(self, name):
        return self.db[name]
    
    def __enter__(self):
        print("MongoDB is connected")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        print("MongoDB is disconnected")

def db_connect():
    try:
        client = MongoClient(MONGODB_URI)
        db = client[DB_NAME]
        print(f"Connected to {db.name}")
        return db
    except Exception as error:
        print(f"Error: {error}")
        raise
    