# Written by Vamei
# Client side
import socket

# Address
HOST = '192.168.1.100'
PORT = 8000

f1 = open('5.jpg','wb')

request = b'GET new1.jpg'

# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send message
s.sendall(request)
# receive message
responseHead = ''
while True:
    reply   = s.recv(1)
    if reply == b'\n':
        break
    responseHead += reply.decode()
print(responseHead)
responseList = responseHead.split('=')
fileSize = int(responseList[1])
content =  s.recv(fileSize)

f1.write(content)
print('receive data and save to file')
# close connection
s.close()
f1.close()