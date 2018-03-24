from pymongo import MongoClient
import pymongo

client = MongoClient()
db  = client.faces

##result = db.faces.insert_one(
##    {
##        "name" :"Akash kumar",
##        "path" :"images/akash.jpg"
##        
##    })
##print("One item Inserted with Object Id: ",result.inserted_id)

cursor = db.faces.find()
#db.faces.delete_many({"path": "images/myself.jpg"})

for item in cursor:
    print(item.get('name'))
    print(item.get('path'))
    
    print("-------------------------------")


##result = db.faces.create_index([('path', pymongo.ASCENDING)],unique=True)
#print(sorted(list(db.faces.index_information())))
