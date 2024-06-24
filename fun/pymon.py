def conn_mongo():
    from pymongo import MongoClient
    host = 'mongo'
    client = MongoClient(host=host, port=27017, username="admin", password="123456", authSource='admin',
                         authMechanism='SCRAM-SHA-1')
    return client
