#!/usr/bin/python
#client.py
import socket
s = socket.socket()
port = 12345
s.connect(('127.0.0.1',port))
print "conected to server on port %s" % port
print s.recv(12345)
s.close()
