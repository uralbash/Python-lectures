# coding: utf-8
#Клиент вначале создает точно такой же сокет, что и сервер. Первый клиентский
#метод – connect() – позволяет соединиться с сервером. Второй метод – send() –
#отсылает данные на сервер. Третий метод – recv() – получает данные с сервера.
#Четвертый метод – close() – закрывает сокет.
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.connect((host, port))
s.send('hello')  
data = s.recv(1000000) 
print 'received', data, len(data), 'bytes'
s.close()

