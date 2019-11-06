import socket
serverip=('localhost',20001)
mgs=str.encode("Hi to server")
buffer=1024

clientsocket= socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

clientsocket.connect(serverip)

clientsocket.listen(1)

while(True):
	clientsocket.sendall(mgs)
	rmsg=clientsocket.recv(buffer)
	if(rmsg):
	   print(rmsg)
	   break
	else:
	   break	
   

 	
