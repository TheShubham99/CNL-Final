import socket
serverip=("127.0.0.1",20001)
mgs=str.encode("Hi to server")
buffer=1024

clientsocket= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while(True):
   clientsocket.sendto(mgs,serverip)
   rmsg=clientsocket.recvfrom(buffer)
   print(rmsg)
   

 	
