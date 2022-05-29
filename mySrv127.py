from socket import *
# Create UDP server socket SOCK_DGRAM for UDP datagram packetS	
srvSock = socket(AF_INET, SOCK_DGRAM)
srvPort= 8888


# Bind UDP socket to port 8888 to excjanges messages on all available interfaces ('', serPort)
srvSock.bind( ('127.1.1.1',srvPort))   # ..('127.0.0.8', srvPort) restricts connections to this adapter
print ("Server is ready to receive on UDP port: " + str(srvPort))
count= 0 
while count < 9:                                              # server answers 9 queries
	rqst,cliAddr =srvSock.recvfrom(2048)                      # wait for a query
	print(',client', cliAddr, 'requested: ', rqst.decode())    # print incoming query
	# prepare the message to be sent
	reply = '\n1700003646> Client '+ cliAddr[0] + ' : ' + str(cliAddr[1]) + ' requested > ' + rqst.decode()
	srvSock.sendto(reply.encode(), cliAddr)                   # send the reply to the client
	count += 1
# Close the server socket
srvSock.close()




