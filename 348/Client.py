# This is the client program

# Sequence:
#
# 1. Create a socket
# 2. Connect it to the server process. 
#	We need to know the server's hostname and port.
# 3. Send and receive data 

import socket

# create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# The first argument should be AF_INET
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service

# connect to the server
host='localhost'
port=43387  # this is the server's port number, which the client needs to know
s.connect((host,port))

# send some bytes
s.send("Knock knock..")

# read a response
response = s.recv(1024)
print(response)


# close the connection
s.close()
