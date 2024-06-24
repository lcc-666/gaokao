# 获取一分一段表

import requests
import json
import time
import fun.pymon

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

url = 'https://static-data.gaokao.cn/www/2.0/section2021/2023/14/2/3/lists.json'
response = requests.get(url, headers=headers)
re = json.loads(response.text)
re_ls = {"grade": '文科一分一段'}
for v in re['data']['section_list'].values():
    for i in v:
        re_ls[i['score']] = [i['num'], i['total']]
        # print(i['score'], i['num'], i['total'])
print(re_ls)

client = fun.pymon.conn_mongo()

# 指定数据库和集合
db = client.school
collection = db.test


collection.insert_one(re_ls)