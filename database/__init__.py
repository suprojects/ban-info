from pymongo import MongoClient

URI = "mongodb+srv://alpha:LjvpahvVijuVf4KP@cluster0.wia0s.mongodb.net/baninforobot"
client = MongoClient(URI)
db = client["baninforobot"]
