from socket import *
s = socket(AF_INET,SOCK_DGRAM)
msg = "Hello World!"
s.sendto(msg,("server.com",10000))
data, addr = s.recvfrom(10000)
