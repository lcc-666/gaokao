import random

import requests
import json
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}


# 获取所有大学的school的id并插入mongo



def get_school_id(url):
    res = requests.get(url, headers=headers)

    obj = json.loads(res.text)
    school_ls = obj['data']['item']
    school_info_ls = []

    f = open('school_info.json', 'a+', encoding='utf-8')

    for school in school_ls:
        item = {school['name']: school['school_id']}
        f.write(str(item) + "\n")


ls = []
f = open('school_info.json', 'r+', encoding='utf-8')
for school in f.readlines():
    ls.append(eval(school.strip()))

school_info = {'school_id': ls}
print(school_info)

import fun.pymon

client = fun.pymon.conn_mongo()

# 指定数据库和集合
db = client.school
collection = db.test
collection.insert_one(school_info)