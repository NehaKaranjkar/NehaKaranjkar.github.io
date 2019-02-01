# This is the Server program
#
# Sequence of steps:
#	1. create a socket  
#	2. bind the socket to a host and port
#	3. start listening on this socket
#	4. accept an incoming connection from the client
#   5. send and receive data over the socket


import socket

#  create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				# use SOCK_STREAM for TCP
				# use SOCK_DGRAM for UDP

# bind it to a host and a port
host = 'localhost'
port = 43387  # arbitrarily chosen non-privileged port number
s.bind((host,port))

# start listening for TCP connections made to this socket
# the argument "1" is the max number of queued up clients allowed
s.listen(1) 
print("Server started...waiting for a connection from the client")

# accept a connection
c, addr = s.accept()
print("Connection initiated from ",addr)

# receive some bytes and print them
# the argument 1024 is the maximum number of characters to be read at a time
response = c.recv(1024)
print(response)

# send some bytes...
c.send("Whose there?")

# close the connection
c.close()
