from socket import *
cliSock = socket(AF_INET, SOCK_DGRAM)
srvIP = '127.1.1.1'
srvPt= 8888
rqst = "...request.byte stream"

count= 0 
cliSock.sendto(rqst.encode(),(srvIP, srvPt))
reply,srvIPPt = cliSock.recvfrom(2048)
print("Server reply message is ", reply)
print("Server-IP, Server-Port", srvIPPt)
cliSock.close()