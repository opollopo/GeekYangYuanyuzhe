import flask
from flask import request, render_template
import checkor

app = flask.Flask(__name__,static_url_path='')

#路由
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/info",methods=["post"])
def info():
    u = request.form.get("username")
    p = request.form.get("password")
    # 用户唯一校验
    a = ""
    # 密码校验
    a = pwdCheck(a, p)
    if a:
        return render_template("login.html", msg=a)
    else:
        return a


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