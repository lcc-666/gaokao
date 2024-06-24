
def conn_mongo():
    from pymongo import MongoClient
    client = MongoClient(host='127.0.0.1', port=27017, username="admin", password="123456")
    return client
