import socket
serverip="127.0.0.1"
msg=str.encode("Hi from server")
port=20001
buffer=1024

serversocket= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serversocket.bind((serverip,port))

while(True):
   rmsg=serversocket.recvfrom(buffer)
   print(rmsg)
   serversocket.sendto(msg,rmsg[1])

 	
