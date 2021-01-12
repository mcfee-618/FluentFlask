import inspect
from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    from utils import cheese # 下面附上utils模块的实现
    cheese()
    return "hello_world"

app.run()