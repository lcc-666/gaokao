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
    time.sleep(random.randint(1, 3))
    obj = json.loads(res.text)
    school_ls = obj['data']['item']

    school_id = []
    school_dt = {}
    for school in school_ls:
        school_id.append(str(school['school_id']))
        school_dt[school['school_id']] = school['name']
    url = 'https://mnzy.gaokao.cn/api/app/v2/v1/queryUniversityRateList?province=%E5%B1%B1%E8%A5%BF&gradeType=%E6%9C%AC%E7%A7%91&classify=%E7%90%86%E7%A7%91&subjects=%E7%90%86%E7%A7%91&score=660&zsgkIds='
    id_str = ",".join(school_id)
    url = url + id_str
    bol_shanxi(url, school_dt)


# 判断这个专科是否在山西招生
def bol_shanxi(url, school_dt):
    res = requests.get(url, headers=headers)
    time.sleep(random.randint(1, 3))

    obj = json.loads(res.text)
    if obj != {'code': 200, 'msg': 'OK', 'body': []}:
        for item in obj['body']:
            if item['enrollProbability'] == None:
                id = item['zsgkId']
                del school_dt[id]

        f = open('school_info.json', 'a+', encoding='utf-8')
        for k, v in school_dt.items():
            print(k, v)
            f.write("{'" + v + "':" + str(k) + '}\n')


if __name__ == '__main__':
    for page in range(1, 77):
        print(page)
        url = 'https://api.zjzw.cn/web/api/?keyword=&page={}&province_id=&ranktype=&request_type=1&school_type=6001&size=20&top_school_id=[2691,1523,1404,2291,3485,764,1390,3052,3117,1496,1278]&type=&uri=apidata/api/gkv3/school/lists'
        get_school_id(url.format(page))
