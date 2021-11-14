import flask
from flask import request, render_template, session, redirect
import checkor
import sqlite3

app = flask.Flask(__name__, static_url_path='')
app.secret_key = "fwefewfew16162"


# account = {"yyyz": "123456", "admin": "1qaz@WSX"}


# 路由
@app.route("/")
def login():
    # 请求上下文中的用户代理，客户段的系统信息
    print(request.user_agent)

    # session[""]
    a = session.get("user_info")
    if not a:
        return render_template("login.html")
    return render_template("main.html", asd=a)


@app.route("/ZhuXiao")
def logout():
    del session["user_info"]
    return render_template("login.html")


@app.route("/info", methods=["post"])
def info():
    u = request.form.get("username")
    session["user_info"] = u
    return render_template("main.html", asd=u)

    # 用户唯一校验
    # a = ""
    # 密码校验
    # a = pwdCheck(a, p)
    # if a:
    #     return render_template("login.html", msg=a)
    # else:
    #     # session是一个特殊的字典 {"":"","":""}
    #     session["user_info"] = u
    #     return render_template("main.html", asd=u)


@app.route("/train01")
def trainInfo():
    # return redirect("login.html")
    return redirect("https://www.chntrs.com")


def pwdCheck(a, p):
    if not checkor.pass_lens(p):
        a = '长度范围8-16'
    if not checkor.pass_char(p):
        a = ("至少包含三类字符（数字，字母，特殊字符）")
    if not checkor.pass_repeat(p):
        a = '字符不能连续重复3次及以上'
    return a


cx = None
cu = None


@app.before_first_request
def conDB():
    global cx
    global cu
    cx = sqlite3.connect("test.db", check_same_thread=False)
    cu = cx.cursor()
    # cu.execute("select * from user ")
    # ret = cu.fetchall()
    # print(ret)


@app.before_request
def checkUser():
    global cu
    # 非根目录访问及注销请求的时候进行用户校验
    if request.base_url != "http://127.0.0.1:5000/" and request.base_url != "http://127.0.0.1:5000/ZhuXiao":
        cu.execute("select * from user ")
        ret = cu.fetchall()
        username = session.get("user_info")
        if username:
            for i in ret:
                if username == i[1]:
                    break
            else:
                # 用户未找到
                return render_template("login.html", msg="用户不存在")

        u = request.form.get("username")
        p = request.form.get("password")
        if u and p:
            for i in ret:
                if u == i[1] and p == i[2]:
                    break
            else:
                return render_template("login.html", msg="用户不存在")


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
