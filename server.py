#!/usr/bin/python
import socket
s = socket.socket()
print ("socket created")
port = 12345
s.bind(('',port))
print ("Socket binded to %s" %(port))
s.listen(5)
print ("Socket is listening")
while True:
    c,addr = s.accept()
print ("Got connected from",addr)
c.send('Thank u for connecting')
c.close()
