import socket

class YxHttpServer:
    def __init__(self, HOST = '', PORT = 8000, rootPath = ''):
        self.HOST = HOST
        self.PORT = PORT
        self.rootPath = rootPath
    """
    run server
    """
    def runServer(self):
        #configure socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST,self.PORT))
        print('begin service')
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
        print(b'server has stopped')
           
class ConnectionHandler:
    def __init__(self, connection, address, rootPath):
        self.connection = connection
        self.address = address
        self.rootPath = rootPath
        textHeaderFilePath = rootPath + '/textHeader.txt'
        jpgHeaderFilePath = rootPath + '/jpgHeader.txt'
        with open(textHeaderFilePath,mode='rb') as ft:
            textHeader = ft.read()
        with open(jpgHeaderFilePath,mode='rb') as jf:
            jpgHeader = jf.read()
        self.textHeader = textHeader
        self.jpgHeader = jpgHeader     
    """
    handle
    """
    def handle(self):
        returnCode = ''
        #get request string
        requestBytes = self.connection.recv(1024)
        requestStr = requestBytes.decode()
        requestInfo = 'from '+ str(self.address) + 'get request : '+ requestStr
        print(requestInfo)
        #request elements
        requestElements = requestStr.split(' ')
        try:
            if requestElements[0] == 'GET':
                self.handleGet(requestElements)
                returnCode =  'OK'
            elif requestElements[0] == 'POST':
                self.handlePost(requestElements)
                returnCode =  'OK'
            elif requestElements[0] == 'STOP':
                returnCode =  'STOP'
            else:
                raise Exception('no have this command')
        except Exception :
            errorText = self.textHeader + b"error"
            self.connection.sendall(errorText)
        #close connection
        self.connection.close()
        return returnCode
    """
    handle get request
    """
    def handleGet(self, requestElements):
        fileName = requestElements[1]
        filePath = self.rootPath + fileName
        fileType = (fileName.split('.'))[1]
        #make responseHeader
        if fileType == 'jpg':
            self.responseHeader = self.jpgHeader
        else:
            self.responseHeader = self.textHeader
        #open file
        try:
            requestFile = open(filePath,mode='rb')
        except FileNotFoundError :
            raise Exception('file not find')
        #send response
        self.responseBody = requestFile.read()
        self.connection.sendall(self.responseHeader + self.responseBody)
        #close file
        requestFile.close()
    """
    handle post request
    """
    def handlePost(self,requestElements):
        pass

