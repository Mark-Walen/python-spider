import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
connection = db.students

condition = {'name': 'Jordan'}
student = connection.find_one(condition)
student['age'] = 20
result = connection.update_one(condition, {'$set': student})
print(result)