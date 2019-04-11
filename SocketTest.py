# -*- coding: utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect('127.0.0.1', 9000)
print(socket.recv(521).decode())
sock.send('Hi'.encode())
sock.close()
