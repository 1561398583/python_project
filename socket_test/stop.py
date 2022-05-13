# Written by Vamei
# Client side
import socket

# Address
HOST = '192.168.1.100'
PORT = 8000

request = b'STOP'

# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send message
s.sendall(request)
# receive message

s.close()
