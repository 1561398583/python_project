import  httpServer1

HOST = ''
PORT = 8001
rootPath = 'E:\python_work\socket_test'
server1 = httpServer1.YxHttpServer(HOST,PORT,rootPath)
server1.runServer()