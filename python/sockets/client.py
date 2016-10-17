#!/usr/bin/env python

# Imports first

import sys
import socket as s
from termcolor import cprint
# Initializing the Connection

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
address_to_connect = (sys.argv[1], int(sys.argv[2]))
client_socket.connect(address_to_connect)

# Name exchanges

# Server's Name

print "Please wait, Peer is choosing name"
peer_name = client_socket.recv(1000)
print "Your peer's name is: " + str(peer_name)

# Client's Name

client_name = raw_input('Choose your nickname: ')
client_socket.send(client_name)

#Conversation Started!

message = 1
print "Welcome to Nchat!. Press 0 to exit conversation.\n Start typing when you see your nickname."
while message != '0':
    message = raw_input(str(client_name) + ": ")
    client_socket.send(message)
    cprint(str(peer_name) + ": " + str(client_socket.recv(1024)), 'blue')

client_socket.close()

