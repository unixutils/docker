#!/bin/python
import socket
import sys

webserver = 'container-web'
port = 80  # web

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = socket.gethostbyname( webserver )
except socket.gaierror:
    print('webservername could not be resolved. Exiting')
    sys.exit()

# Connect to web server
print('# Connecting to server, ' + webserver + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print('# Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print 'Send failed'
    sys.exit()

# Receive data from web server
print('# Receive data from server')
reply = s.recv(4096)

print reply

