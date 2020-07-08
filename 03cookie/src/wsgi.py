#coding:utf-8
"""
@author: mcfee
@description:
@file: wsgi.py
@time: 2020/7/8 上午11:56
"""
from flask import Flask,redirect,url_for,make_response,request,session

app=Flask(__name__)
app.secret_key = 'secret string'
print(app.session_cookie_name)


@app.route('/set/<name>')
def set_cookie(name):
    print(request.cookies)
    response = make_response("222")
    response.set_cookie('name', name)
    #因为过期时间使用默认值，所以会在浏览会话结束时（关闭浏览器）过期
    return response

@app.route('/setname/<name>')
def hello_world(name):
    session['username'] = name
    # session=eyJ1c2VybmFtZSI6InpoYW5nc2FuIn0.Eeb8Qw.uaxRu1gRqM_ww3uf3rfzpQEcEM8;
    return "ok"

@app.route('/getname')
def hello_world1():
    # session=eyJ1c2VybmFtZSI6InpoYW5nc2FuIn0.Eeb8Qw.uaxRu1gRqM_ww3uf3rfzpQEcEM8;
    return session['username']