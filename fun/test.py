from pymongo import MongoClient


client = MongoClient(host='127.0.0.1', port=27017, username="admin", password="123456")

# 指定数据库和集合
db = client.school
collection = db.test

# 插入文档
info = {'name': 'ls', 'age': 32}
collection.insert_one(info)

# 查看文档
re = collection.find_one()
print(re)

# 修改文档
collection.update_one({'name': 'zs'}, {'$set': {"age": 35}})

# 删除文档
collection.delete_one({'name': 'zs'})
