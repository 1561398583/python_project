import socket

# Address
HOST = '192.168.1.100'
PORT = 8000

f1 = open('hello.txt','wb')

request = b'GET hello.html'

# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send message
s.sendall(request)

content =  s.recv(1024)

f1.write(content)
print('receive data and save to file')
# close connection
s.close()
f1.close()