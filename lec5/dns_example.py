# coding: utf-8
#Модуль socket имеет несколько вспомогательных функций. В частности, функции для
#работы с системой доменных имен (DNS):

import socket
print "gethostbyname: ", socket.gethostbyname('www.onego.ru')
print "gethostbyaddr: ", socket.gethostbyaddr('93.158.134.3')
print "gethostname: ", socket.gethostname()

#В новых версиях Python появилась такая функция как socket.getservbyname(). Она
#позволяет преобразовывать наименования Интернет-сервисов в общепринятые номера
#портов:

for srv in 'http', 'ftp', 'imap', 'pop3', 'smtp', 'https':
    print socket.getservbyname(srv, 'tcp'), srv

