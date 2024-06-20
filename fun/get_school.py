# 通过选课和分数筛选可以考虑的学校

from pymongo import MongoClient


# 通过选课确定查询表
def get_school(type_sub, grade):
    # 通过选课确定查询表
    if type_sub == 'science':
        grade_line = '理科一分一段'
    else:
        grade_line = '文科一分一段'

    client = MongoClient(host='127.0.0.1', port=27017, username="admin", password="123456")

    # 指定数据库和集合
    db = client.school
    collection = db.test

    re = collection.find_one({'grade': grade_line}, {'_id': 0, 'grade': 0})
    # print(re.keys())
    print(re[grade])
    school_grade = re[grade]
    # 一分一段表最低和最高
    min_grade_line = int(list(re.keys())[0])
    max_grade_line = int(list(re.keys())[-2])
    # 将分数上下浮动15分获取相应排名
    num = 10
    if int(grade) + num >= max_grade_line:
        max_grade = max_grade_line
    else:
        max_grade = int(grade) + num

    if int(grade) - num <= min_grade_line:
        min_grade = min_grade_line
    else:
        min_grade = int(grade) - num

    min_grade = str(min_grade)
    max_grade = str(max_grade)
    # print(min_grade, re[min_grade], max_grade, re[max_grade])
    # 浮动15分排名
    min_rank = int(re[min_grade][-1])
    max_rank = int(re[max_grade][-1])
    # print(min_rank, max_rank)
    re = collection.find_one({'grade': grade_line}, {'_id': 0, 'grade': 0})

    # 确定选科
    if type_sub == 'science':
        type_sub = '理科'
    else:
        type_sub = '文科'
    re = collection.find_one({'type': type_sub}, {'_id': 0, 'type': 0})
    # 可以考虑的学校合集
    school_re = {}
    for k, v in re['batch'].items():
        if v[0][-1] == '-':
            print(k, v)
            continue
        if len(v) == 1 and (max_rank < int(v[0][-1]) < min_rank):
            school_re[k] = v
        elif len(v) != 1:
            school_min_line = int(v[0][-1])
            school_max_line = int(v[-1][-1])

            range1 = (max_rank, min_rank)
            range2 = (school_min_line, school_max_line)
            if ranges_overlap(range1, range2):
                school_re[k] = v
    # print(max_rank, min_rank)
    # print(school_re)
    return (school_grade, school_re)


def ranges_overlap(range1, range2):
    """
    判断两个范围是否有交集。

    参数:
    range1 (tuple): 第一个范围，以 (start, end) 的形式表示。
    range2 (tuple): 第二个范围，以 (start, end) 的形式表示。

    返回:
    bool: 如果两个范围有交集，返回 True；否则返回 False。
    """
    start1, end1 = range1
    start2, end2 = range2

    # 检查范围是否有交集
    return not (end1 < start2 or end2 < start1)


if __name__ == '__main__':
    get_school(type_sub='science', grade='489')
    # range1 = (3, 5)
    # range2 = (1, 8)
    #
    # if ranges_overlap(range1, range2):
    #     print("范围有交集")
    # else:
    #     print("范围没有交集")
