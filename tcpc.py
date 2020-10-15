from socket import *
s = socket(AF_INET,SOCK_STREAM)
print ("TCP")
s.connect(("www.python.org",80)) # Connect
s.send("GET /index.html HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response
s.close()
