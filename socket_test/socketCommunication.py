import socket

class SocketCommunicater:
    def __init__(self,HOST='',PORT=''):
        self.HOST = '192.168.1.100'
        self.PORT = 8000
        self.address = '(192.168.1.100:8000)'

    def run(self):
        # connect socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        print('socket has begin.')
        while True:
            keyboardStr = input('@:')
            if keyboardStr == 'Q':
                break
            s.send(keyboardStr.encode())
            remoteBytes = s.recv(1024)
            remoteStr = remoteBytes.decode()
            print('FROM '+self.address + ' GET TEXT\r\n' + remoteStr)
        #close socket
        s.close()
        print('socket has closed.')


communicater = SocketCommunicater()
communicater.run()