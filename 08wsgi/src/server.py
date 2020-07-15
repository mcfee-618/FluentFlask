# coding:utf-8
"""
@author: mcfee
@description:
@file: server.py
@time: 2020/7/15 上午11:50
"""
import socket


def req(client):
    buf = client.recv(1024)
    print(buf)
    msg = "HTTP/1.1 200 OK\r\n\r\n"
    client.send(('%s' % msg).encode())
    msg = "Hello, World! xxx this is socket with no wsgi!!!"
    client.send(('%s' % msg).encode())


def main():
    ip_port = ("localhost", 9000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(ip_port)
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        req(conn)
        conn.close()


if __name__ == "__main__":
    main()
