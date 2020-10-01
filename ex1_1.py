import socket
s = socket(AF_INET,SOCK_STREAM)
s.connect(("www.python.org",80))
s.send("GET /index.html HTTP/1.0\r\n\r\n")
chunks = []
while True:
chunk=s.recv(16384)
{if not chunk: 
              break}
chunks.append(chunk)
s.close()
response = "".join(chunks)
print (response)
