#!/usr/bin/python3
"""
Simple TCP Client
Copyright: Juan Antonio Gil Chamorro (M4luk0)
"""

# Libraries
import socket

# We create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the IP and port and wait for the connection.
ip_and_port = ('127.0.0.1', 10000) # Change this if you want
print('Connecting to ' + ip_and_port[0] + ' in port ' + str(ip_and_port[1]))

# We connect and send "hola", if we receive "adios", close the connection.
sock.connect(ip_and_port)
sock.send(b'hola')
data = sock.recv(16)
print(data)
if data == b'adios':
    sock.close()
