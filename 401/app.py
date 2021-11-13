import flask
from flask import request, render_template, session, redirect
import checkor

app = flask.Flask(__name__, static_url_path='')
app.secret_key = "fwefewfew16162"

account = {"yyyz": "123456", "admin": "1qaz@WSX"}


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
    print("get请求获得的参数值:" + request.args.get("t"))
    return render_template("login.html")


@app.route("/info", methods=["post"])
def info():
    # post请求的参数获取方法request.form.get("") ，get 请求获取方式request.args.get("")
    u = request.form.get("username")
    p = request.form.get("password")
    for i, j in account.items():
        if u == i and p == j:
            # session是一个特殊的字典 {"":"","":""}
            session["user_info"] = u
            return render_template("main.html", asd=u)
    else:
        return render_template("login.html", msg="用户名或密码错误")

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


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
