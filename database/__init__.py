from pymongo import MongoClient
from secrets import URI

client = MongoClient(URI)
db = client["ban-bot"]
