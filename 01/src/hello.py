#coding:utf-8
"""
@author: mcfee
@description:
@file: hello.py
@time: 2020/7/6 下午5:05
"""
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route("/add",defaults={'tid':288}) ##设置默认值的要在匹配规则的上面
@app.route('/add/<int:tid>')
def add(tid):
    return str(tid)

@app.route('/test1')
def test_url():
    return url_for("test_url",_external=True)