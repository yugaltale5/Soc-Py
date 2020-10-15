import socket
s = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
ip=socket.gethostbyname("www.google.com")
print ip
