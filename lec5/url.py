# coding: utf-8
#Функция urllib.urlopen() создает файлоподобный объект, который читает методом
#read(). Другие методы этого объекта: readline(), readlines(), fileno(), close()
#работают как и у обычного файла, а также есть метод info(), который возвращает
#соответствующий полученному с сервера Message-объект.
import urllib
doc = urllib.urlopen("http://python.onego.ru").read()
print doc[:40] 

