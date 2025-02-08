from pymongo import MongoClient
import datetime

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/')

# result = client['test']['todos'].aggregate([])

# print(client.list_collection_names())

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

todo1 = {"name": "Patrick", "text": "My first todo!", "status": "open",
         "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}

todo2 = [{"name": "Patrick", "text": "My second todo!", "status": "open",
          "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}, {"name": "Mary", "text": "My third todo!", "status": "open", "tags": ["python", "coding"], "date": datetime.datetime(2021, 1, 1, 10, 45)}]

todos = db.todos

# result = todos.insert_one(todo1)
result = todos.insert_many(todo2)

print(result)
