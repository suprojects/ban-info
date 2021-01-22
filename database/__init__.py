from pymongo import MongoClient

URI = "mongodb+srv://roj:qwertyuiop@cluster0.pmqx1.mongodb.net/ban"
client = MongoClient(URI)
db = client["ban"]
