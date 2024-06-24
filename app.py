from flask import Flask, render_template, request, session

from os import urandom

app = Flask(__name__, static_url_path='')

import fun.pymon

client = fun.pymon.conn_mongo()

# 指定数据库和集合
db = client.school
collection = db.test

app.secret_key = urandom(50)


@app.route('/')
def hello_world():  # put application's code here
    session.clear()
    return render_template('index.html', num=0)


# 查询可考虑学校
@app.route('/school', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        type_sub = result['gender']
        grade = result['grade']
        import fun.get_school
        get_school = fun.get_school.get_school
        # 获取可以上的学校
        school_grade, re_dt = get_school(type_sub, grade)
        session['type'] = type_sub
        session['grade'] = school_grade
        session['num'] = grade
        num = grade
        return render_template('index.html', grade=school_grade, re_dt=re_dt, num=num)


@app.route('/school_major/<school_name>/')
def school_major(school_name):
    import fun.get_school_major
    bol_major = fun.get_school_major.bol_major

    re = bol_major(school_name)
    type_sub = session['type']
    if type_sub == 'science':
        major_dt = re['理科']
    else:
        major_dt = re['文科']
    num = session.get('num')
    grade = session.get('grade')

    return render_template('school_major.html', school_name=re['school_name'], major_dt=major_dt, type_sub=type_sub,
                           num=num, grade=grade)


if __name__ == '__main__':
    app.run()
