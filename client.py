import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input("Enter your name : ")

c.send(bytes(name,'utf-8'))

#server will be made in sometime
