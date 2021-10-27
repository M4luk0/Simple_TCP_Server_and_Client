#!/usr/bin/python3
"""
Simple TCP Server
Copyright: Juan Antonio Gil Chamorro (M4luk0)
"""

# Libraries
import socket

# We create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify IP and port and we start listening
ip_and_port = ('127.0.0.1', 10000) # Change this
print('Starting server in ' + ip_and_port[0] + ' port ' + str(ip_and_port[1]))
sock.bind(ip_and_port)
sock.listen(1)

# We wait for a connection and when it connects we send "adios" and close the connection.
print("Waiting to a connection...")
connection, client_address = sock.accept()
print("Connection from", client_address)
data = connection.recv(4096)
print(data)
connection.send(b'adios')
connection.close()
sock.close()
