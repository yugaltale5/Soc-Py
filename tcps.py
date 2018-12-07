from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",9000))
#s.bind(("127.0.0.1",8000))
s.listen(5)
while True:
 c,a = s.accept()
 print "Received connection from", a
 c.send("Glad u connected! %s\n" % a[0])
 c.close()
