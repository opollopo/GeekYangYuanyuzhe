import sqlite3
import flask
from flask import render_template,request
import random

a = flask.Flask(__name__)
a.debug = True

@a.route("/")
def login():
    cu.execute("select * from guess_number ")
    a = cu.fetchall()
    return render_template("main.html",msg2=a)

@a.route("/create", methods=["post"])
def creat_room():
    """生成目标数字，创建房间号"""
    room_num = random.randint(1, 20)
    target_num = random.randint(1, 200)
    u = request.form.get("username")
    cu.execute("insert into guess_number ( room, number, people) VALUES (%d, %d, '%s');" % (room_num, target_num, u))
    cx.commit()

    cu.execute("select * from guess_number ")
    a = cu.fetchall()
    return render_template("main.html", msg2=a)

@a.route("/join", methods=["post"])
def online_public():
    """加入房间"""
    # 获取房间号
    room_number = int(request.form.get("room_num"))
    cu.execute("select * from guess_number ")
    a = cu.fetchall()
    y = None
    for i in a:
        if room_number == i[1]:
            y = i[2]
            break
    else:
        return render_template("main.html", m="房间号不存在")
    return render_template("guess.html", v_y=y)

@a.before_first_request
def conDB():
    global cx
    global cu
    cx = sqlite3.connect("test.db", check_same_thread=False)
    cu = cx.cursor()

a.run()
