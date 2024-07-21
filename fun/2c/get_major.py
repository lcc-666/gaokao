# 将专科学校信息插入mongo

if __name__ == '__main__':
    from fun.pymon import conn_mongo

    client = conn_mongo()
    db = client.school
    collection = db.test

    f = open('school_info.json', 'r', encoding='utf-8').readlines()

    re = collection.find_one()
    for item in set(f):
        re['school_id'].append(eval(item.strip()))

    collection.update_one({'_id': re['_id']}, {'$set': {'school_id': re['school_id']}})
