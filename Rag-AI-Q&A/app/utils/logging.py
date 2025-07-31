from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
db = client.qa_logs
collection = db.queries


def log_query(data):
    collection.insert_one(data)
