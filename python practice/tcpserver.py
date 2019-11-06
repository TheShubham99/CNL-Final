import socket
serverip=('localhost',20001)
msg=str.encode("Hi from server")
port=20001
buffer=1024

serversocket= socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
serversocket.bind(serverip)

serversocket.listen(1)
while(True):
   connection,clientaddress = serversocket.accept()
   print(clientaddress)
   print(connection)
   while(True):
      rmsg=connection.recv(buffer)
      if(rmsg):
         print(rmsg)
         connection.sendall(msg)
      else:
         break	  
	  
	  	
 	
