# 通过学校id获取学校批次线分数
import json
import random
import time

import requests


def get_batch(name, id):
    url = 'https://api.zjzw.cn/web/api/?e_sort=zslx_rank,min&e_sorttype=desc,desc&local_province_id=14&local_type_id={}&page=1&school_id={}&size=10&uri=apidata/api/gk/score/province&year=2023&signsafe=6269328736f928434a571fc703f38cb5'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    f = open('2c.txt', 'a', encoding='utf-8')

    for major_type in ['1', '2']:
        time.sleep(random.randint(1, 3))
        url = url.format(major_type, id)
        response = requests.get(url, headers=headers).text
        if '本科二批C段' in response or '专科批' in response:
            f.write(name + ':' + str(id) + '\n')
            break
        else:
            print(name+'在山西没有2B以下批次')


# 获取2c分数线
def get_2c_line():
    from fun.school_batch import school_id
    school_id = school_id()
    for item in school_id['school_id'][1297:]:
        name = list(item.keys())[0]
        id = item[name]
        # print(name)
        get_batch(name, id)


if __name__ == '__main__':
    get_2c_line()
