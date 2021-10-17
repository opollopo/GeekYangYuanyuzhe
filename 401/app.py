import flask
from flask import request
import checkor

app = flask.Flask(__name__,static_url_path='')

#路由
@app.route("/")
def login():
    return """<form action="/info" method="post">
        用户名：<input type="text" name="username"></br>
        密 码:<input type="text" name="password"></br>
        <button>登陆</button>
    </form>"""

@app.route("/info",methods=["post"])
def info():
    u = request.form.get("username")
    p = request.form.get("password")
    a = "登陆成功"
    if not checkor.pass_lens(p):
        a = '长度范围8-16'
    if not checkor.pass_char(p):
        a = ("至少包含三类字符（数字，字母，特殊字符）")
    if not checkor.pass_repeat(p):
        a = '字符不能连续重复3次及以上'
    return a


if __name__ == '__main__':
    print(app.url_map)
    app.run()