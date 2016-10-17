#!/usr/bin/env python

# Imports first

import socket as s
from termcolor import cprint

# Create a TCP/ IP socket to listen on

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

# Prevent from 'address already in use' upon server restart

server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

# Bind the server to port 8081 on all interfaces

server_address = ('0.0.0.0', 8081)
print 'starting up on %s port %s' %server_address
server_socket.bind(server_address)

# listen to connection

server_socket.listen(5)

# Wait for incoming connection

connection, client_address = server_socket.accept()
print 'connection from', connection.getpeername()

# Name exchanges

# Server's Name

server_name = raw_input('Choose your nickname: ')
connection.send(server_name)

#Client's Name

print "Please wait, Peer is choosing name"
peer_name = connection.recv(1000)
print "Your peer's name is: " + str(peer_name)

message = 1
print "Welcome to Nchat!. Press 0 to exit conversation.\n Start typing after your nickname"
while message != '0':
    cprint(str(peer_name) + ": " + str(connection.recv(1024)), 'red')
    message = raw_input(str(server_name) + ": ")
    connection.send(message)

# Close the connection from this side

connection.shutdown(s.SHUT_RD | s.SHUT_WR )
connection.close()
server_socket.close()
