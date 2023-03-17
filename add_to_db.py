import pymongo
import csv

myclient = pymongo.MongoClient("mongodb+srv://deon:eskORBUto@mdb.j3dojkz.mongodb.net/test")

mycluster = myclient["Assignment-1"]
mydb = mycluster["Assignments070"]

mydb.delete_many({})

with open('data.csv') as csvfile:
    
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        mydb.insert_one(row)


# query = {"semester": "3", "section": "D", "avg_marks": {"$gte": 75}}

results = mydb.find(query)
#print(results[0])
for result in mydb.find({"semester": "4", "section": "A", "avg_marks": { '$gte': "75"}}):
    print("Name:", result["name"],end=" ,")
    print("SRN:", result["srn"],end=" ,")
    print("Semester:", result["semester"],end=" ,")
    print("Section:", result["section"],end=" ,")
    print("Average Marks:", result["avg_marks"],end=" ,")
    print()

