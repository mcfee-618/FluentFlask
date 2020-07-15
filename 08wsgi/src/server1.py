#coding:utf-8
"""
@author: mcfee
@description:
@file: server1.py
@time: 2020/7/15 上午11:54
"""
from wsgiref.simple_server import make_server


def wsgireq(env, res):
    print(env)
    res("200 OK", [("Content-Type", "text/html")])
    body = "<h1>Hello World!, this is the wsgi response!</h1>"
    return [body.encode("utf-8")]


if __name__ == "__main__":
    httpd = make_server("127.0.0.1", 8000, wsgireq)
    print("Serving http on port 8000")
    httpd.serve_forever()