#coding:utf-8
"""
@author: mcfee
@description:
@file: hello.py
@time: 2020/7/7 下午6:34
"""
from flask import Flask, request
app = Flask(__name__)
@app.route('/hello')
def hello():
    name = request.args.get('name', 'Flask')
    #为了避免错误，使用get（）方法获取数据，如果没有对应的值则返回None；get（）方法的第二个参数可以设置默认值
    return name

@app.route('/hello1/<any(value1,value2):name>',)
def hello1(name):
    return name

@app.before_request
def before():
    print("before")


print(app.url_map)