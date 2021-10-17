import flask

app = flask.Flask(__name__)

#路由
@app.route("/")
def login():
    return "hello"

if __name__ == '__main__':
    app.run()