import socket

class TextHttpServer:
    def __init__(self, HOST = '', PORT = 8001, rootPath = ''):
        self.HOST = ''
        self.PORT = 8001
        self.rootPath = 'E:/python_work/text'
    """
    run server
    """
    def runServer(self):
        #configure socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST,self.PORT))
        print('begin text service')
        while True:
            # passively wait, 3: maximum number of connections in the queue
            s.listen(3)
            # accept and establish connection
            conn, addr = s.accept()
            # receive message
            handler = ConnectionHandler(conn, addr, self.rootPath)
            result = handler.handle()
            if result == 'STOP':
                break
        print(b'text server has stopped')
           
class ConnectionHandler:
    def __init__(self, connection, address, rootPath):
        self.connection = connection
        self.address = address
        self.rootPath = rootPath   
    """
    handle
    """
    def handle(self):
        returnCode = 'OK'
        #get request string
        requestBytes = self.connection.recv(1024)
        requestFileName = requestBytes.decode()
        requestInfo = 'from '+ str(self.address) + 'get request : '+ requestFileName
        print(requestInfo)
        filePath = self.rootPath + requestFileName
        #open file
        try:
            requestFile = open(filePath,mode='rb')
        except FileNotFoundError :
            self.responseBody = b''
        else:
            self.responseBody = requestFile.read()
            requestFile.close()
        #send response
        self.connection.sendall(self.responseBody)
        #close connection
        self.connection.close()
        return returnCode
   
server = TextHttpServer()
server.runServer()