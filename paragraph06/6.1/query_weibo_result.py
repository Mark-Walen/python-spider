# 对于多条数据的查询，可以使用find方法。
import pymongo
# from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['weibo']
connection = db['weibo']
# result = connection.find_one({'name': 'Channing'})
# result = connection.find_one({'_id': ObjectId('5f54aeb20b4dbe8ac7c68d00')})
# results = connection.find({'gender': 'male'})
# 计数
# count = connection.count_documents({'gender': 'male'})
# print(count)
# print(type(results))
# for result in results:
#     print(result)
# 排序
# results = connection.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results])
# 偏移
results = connection.find()
print([result for result in results])
