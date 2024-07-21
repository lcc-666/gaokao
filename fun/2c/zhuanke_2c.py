# 将2c和专科单独插入mongo
from fun.pymon import conn_mongo

if __name__ == '__main__':
    client = conn_mongo()
    db = client.school
    collection = db.test

    re=collection.find_one({'type': '2c'})

    school_dt = {}
    f = open('2c.txt', 'r', encoding='utf-8')
    for line in f:
        line = line.strip().split(':')
        school_dt.update({line[0]: line[1]})
    f.close()
    f = open('school_info.json', 'r', encoding='utf-8').readlines()
    for line in f:
        school_dt.update(eval(line.strip()))
    dt = {'type': '2c', 'school_id': school_dt}
    collection.insert_one(dt)
