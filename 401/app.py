import flask
from flask import request
import checkor

app = flask.Flask(__name__)

#路由
@app.route("/")
def login():
    return """<form action="/info" method="post">
        用户名：<input type="text" name="username"></br>
        密 码:<input type="text" name="password"></br>
        <button>登陆</button>
    </form>"""

@app.route("/info")
def info():
    u = request.form.get("username")
    p = request.form.get("password")
    if not checkor.pass_char(p):
        print("至少包含三类字符（数字，字母，特殊字符）")
    return "登陆成功"


if __name__ == '__main__':
    app.run()