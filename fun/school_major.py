import fun.pymon

def school_id(name):
    client = fun.pymon.conn_mongo()

    # 指定数据库和集合
    db = client.school
    collection = db.test

    # 查看文档
    re = collection.find_one({}, {'_id': 0})
    # print(re['school_id'])
    for item in re['school_id']:
        if name in item.keys():
            return item[name]

if __name__ == '__main__':
    school_id('九江学院')