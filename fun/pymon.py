def conn_mongo():
    from pymongo import MongoClient
    host = '127.0.0.1'
    client = MongoClient(host=host, port=27017, username="admin", password="123456", authSource='admin',
                         authMechanism='SCRAM-SHA-256')
    return client
