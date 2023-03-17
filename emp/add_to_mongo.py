import pymongo
import csv

myclient = pymongo.MongoClient("mongodb+srv://deon:eskORBUto@mdb.j3dojkz.mongodb.net/test")

mycluster = myclient["Assignment-1"]
mydb = mycluster["Assignments070(2)"]

mydb.delete_many({})

with open('employee_data.csv') as csvfile:
    
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        mydb.insert_one(row)


# query = {"semester": "3", "section": "D", "avg_marks": {"$gte": 75}}

# results = mydb.find(query)
#print(results[0])
for result in mydb.find({}):
    print("EMP CODE:", result["EMP CODE"],end=" ,")
    print("EMP NAME:", result["EMP NAME"],end=" ,")
    print("BASIC SALARY:", result["BASIC SALARY"],end=" ,")
    print("DA:", result["DA"],end=" ,")
    print("GROSS SALARY:", result["GROSS SALARY"],end=" ,")
    print("NET SALARY:", result["NET SALARY"],end=" ,")
    print("IC:", result["IC"],end=" ,")
    print("PF:", result["PF"],end=" ,")
    print("TOTAL-DEDUCTIONS:", result["TOTAL-DEDUCTIONS"],end=" ,")
    print()

