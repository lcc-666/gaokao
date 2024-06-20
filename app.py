from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017, username="admin", password="123456")

# 指定数据库和集合
db = client.school
collection = db.test


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


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
        return render_template('school_ls.html', grade=school_grade, re_dt=re_dt, num=grade)

@app.route('/school_major/<school_name>/')
def school_major(school_name):
    from fun.school_major import school_id
    school_id=school_id(school_name)
    url='https://www.gaokao.cn/school/{}/provinceline'
    return redirect(url.format(school_id))





if __name__ == '__main__':
    app.run()
