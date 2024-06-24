# 通过学校名称获取文理科所有转移排名
import time

import requests
import json
import random

import fun.pymon

import fun.pymon


# 插入文理科各专业批次线
def get_school_major(school_name):
    from fun.school_major import school_id

    school_id = school_id(school_name)
    # 获取2023年文理科具体批次
    url = "https://api.zjzw.cn/web/api/?e_sort=zslx_rank,min&e_sorttype=desc,desc&local_province_id=14&local_type_id={}&page=1&school_id={}&size=10&uri=apidata/api/gk/score/province&year=2023"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    target_dt = {
        'school_name': school_name,
        'type': 'major_batch'
    }

    # 获取文理科专业批次线
    for mojar_type in ['1', '2']:
        response = requests.get(url.format(mojar_type, school_id), headers=headers).text
        response = json.loads(response, encoding='utf-8')
        batch_ls = []
        for batch in response['data']['item']:
            batch_ls.append((batch['local_batch_id'], batch["local_batch_name"]))
        temp_dt = {}
        for batch in batch_ls:
            re = get_school_majors_batch(batch[0], school_id, mojar_type)
            temp_dt[batch[1]] = re
        if mojar_type == '1':
            target_dt['理科'] = temp_dt
        else:
            target_dt['文科'] = temp_dt

    client = fun.pymon.conn_mongo()

    # 指定数据库和集合
    db = client.school
    collection = db.test

    # 插入文档
    collection.insert_one(target_dt)


# 获取单个批次线
def get_school_majors_batch(batch_id, school_id, major_type):
    url = 'https://api.zjzw.cn/web/api/?local_batch_id={}&local_province_id=14&local_type_id={}&page={}&school_id={}&size=10&special_group=&uri=apidata/api/gk/score/special&year=2023'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    response = requests.get(url.format(batch_id, major_type, '1', school_id), headers=headers).text
    response = json.loads(response)
    major_num = int(response['data']['numFound'])

    batch_dt = {}
    if major_num < 10:
        for item in response['data']['item']:
            batch_dt[item['spname']] = [item['min'], item['min_section']]
    else:
        for item in response['data']['item']:
            batch_dt[item['spname']] = [item['min'], item['min_section']]
        page = major_num // 10 + 1
        for page in range(2, page + 1):
            response = requests.get(url.format(batch_id, major_type, str(page), school_id), headers=headers).text
            response = json.loads(response)
            for item in response['data']['item']:
                batch_dt[item['spname']] = [item['min'], item['min_section']]
            time.sleep(random.randint(3, 5))
    return batch_dt


# 判断mongo中是否存在专业 有就查询返回 没有就查询插入然后返回
def bol_major(school_name):
    # print(school_name)
    client = fun.pymon.conn_mongo()

    # 指定数据库和集合
    db = client.school
    collection = db.test

    # 插入文档
    re = collection.find_one({'school_name': school_name, 'type': 'major_batch'}, {'_id': 0, 'type': 0})
    if re is None:
        get_school_major(school_name)
        re = collection.find_one({'school_name': school_name, 'type': 'major_batch'})
        return re
    else:
        return re


# 目标json格式
dt = {
    'school_name': '山西医科大学',
    'type': 'major_batch',
    "理科": {"本科二批B段": {'护理学': [466, 50253], '运动康复': [461, 52938],
                             '信息管理与信息系统（医学信息学方向）': [460, 53488]}
             },
    "文科": []
}

if __name__ == '__main__':
    # get_school_major('西南石油大学')
    re = bol_major('西南石油大学')

