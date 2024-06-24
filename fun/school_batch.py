import random

import fun.pymon


# 读取学校id
def school_id():
    client = fun.pymon.conn_mongo()

    # 指定数据库和集合
    db = client.school
    collection = db.test

    # 查看文档
    re = collection.find_one({}, {'_id': 0})
    return re


import time

import requests
import json


def get_batch(id):
    url = 'https://api.zjzw.cn/web/api/?e_sort=zslx_rank,min&e_sorttype=desc,desc&local_province_id=14&local_type_id=2&page=1&school_id={}&size=10&uri=apidata/api/gk/score/province&year=2023&signsafe=6269328736f928434a571fc703f38cb5'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    sign_dt = {}
    res = requests.get(url.format(id), headers=headers)
    time.sleep(random.randint(3, 5))
    f = open('school_batch.json', 'a')
    school_batch = json.loads(res.text, encoding='utf-8')
    ls = []

    if len(school_batch['data']['item']) != 0:
        school_name = school_batch['data']['item'][0]['name']
        for batch in school_batch['data']['item']:
            item = [batch['name'], batch['local_batch_name'], batch['min'], batch['min_section'],
                    batch['local_type_name']]
            ls.append([batch['local_batch_name'], batch['min'], batch['min_section']])
        sign_dt[school_name] = ls
        f = open('school_batch.json', 'a')
        f.write(str(sign_dt) + '\n')
    else:
        print("未在山西招生")


# 过滤条件
def filter_conditions(data_item):
    new_data_item = {}
    for key, value in data_item.items():
        new_records = [record for record in value if
                       '专科批' not in record[0] and '本科二批C段' not in record[0] and '本科提前批' not in record[0]]
        if new_records:
            new_data_item[key] = new_records
    return new_data_item


data = []
f = open('school_batch.json', 'r').readlines()
for line in f:
    data.append(eval(line.strip()))

# 过滤数据
filtered_data = [filter_conditions(item) for item in data if filter_conditions(item)]

dt = {}
# 打印结果
for item in filtered_data:
    dt.update(item)

singo_dt = {}
singo_dt['type'] = '文科'
singo_dt['batch'] = dt
print(singo_dt)

client = fun.pymon.conn_mongo()

# 指定数据库和集合
db = client.school
collection = db.test

# 插入文档
collection.insert_one(singo_dt)
