import pymongo
import json
from bson import ObjectId
from datetime import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")


print(" List the databases")
for db in myclient.list_databases():
    print(db)


db = myclient['fireworks']

collection_names = db.list_collection_names()

print(" List of collections")
for coll_name in collection_names:
    print(coll_name)

print(" Save in json files")

outputFile = "launches.json"
collection = db['launches']
documents = collection.find()
with open(outputFile,"w") as file:
    json.dump(list(documents), file, cls=JSONEncoder)

outputFile = "fireworks.json"
collection = db['fireworks']
documents = collection.find()
with open(outputFile,"w") as file:
    json.dump(list(documents), file, cls=JSONEncoder)

outputFile = "workflows.json"
collection = db['workflows']
documents = collection.find()
with open(outputFile,"w") as file:
    json.dump(list(documents), file, cls=JSONEncoder)

