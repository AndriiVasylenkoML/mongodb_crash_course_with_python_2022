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

todos2 = [{"name": "Patrick", "text": "My second todo!", "status": "open",
          "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}, {"name": "Mary", "text": "My third todo!", "status": "open", "tags": ["c++", "coding"], "date": datetime.datetime(2021, 1, 1, 10, 45)}]

todos = db.todos

# result = todos.insert_one(todo1)
# result = todos.insert_many(todos2)
# result = todos.find_one({"name": "Patrick"})
# result = todos.find_one({"tags": "c++"})

# Dont work.
# result = todos.find_one({"_id":  "67a9f76e78e7c80bd98b1a5f"})
# from bson.objectid import ObjectId
# result = todos.find_one({"_id": ObjectId("67a9f76e78e7c80bd98b1a5f")})
# print(result)

# Pymongo cursor object
# results = todos.find({"name": "Patrick"})
# print(results)
# for result in results:
#     print(result)


# print(todos.count_documents({"tags": "c++"}))
# print(todos.count_documents({"tags": "c#"}))


# d = datetime.datetime(2021, 2, 1)
# results = todos.find({"date": {"$lt": d}}) # $lt = less than (менше ніж)
# results = todos.find({"date": {"$gt": d}}) # $gt = greater than (більше ніж)
# results = todos.find({"date": {"$gt": d}}).sort("name")
# for result in results:
#     print(result)

## Delete data.  
# from bson.objectid import ObjectId
# result = todos.delete_one({"_id": ObjectId("67a9f76e78e7c80bd98b1a5f")})
# result = todos.delete_many({"name": "Patrick"})
# Delete all data.
# result = todos.delete_many({})

# result = todos.update_one({"tags": "c++"}, {"$set": {"status": "done"}})
# result = todos.update_many({"tags": "c++"}, {"$unset": {"status": None}})
result = todos.update_many({"tags": "c++"}, {"$set": {"status": "new open"}})