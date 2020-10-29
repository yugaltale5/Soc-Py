#!/usr/bin/python
#client.py
import socket
import time
s = socket.socket()
port = 12345
s.connect(('127.0.0.1',port))
print("wait for 3 sec")
time.sleep(3)
print("Client Side")
print ("conected to server on port side %s" % port)
print s.recv(12345)
s.close()
#client 
