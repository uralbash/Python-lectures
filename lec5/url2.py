# coding: utf-8
#С помощью функции urllib.urlopen() можно делать и более сложные вещи, например,
#передавать web-серверу данные формы. Как известно, данные заполненной web-формы
#могут быть переданы на web-сервер с использованием метода GET или метода POST.
#Метод GET связан с кодированием всех передаваемых параметров после знака "?" в
#URL, а при методе POST данные передаются в теле HTTP-запроса. Оба варианта
#передачи представлены ниже:

import urllib
data = {"search": "Python"}
enc_data = urllib.urlencode(data)

# метод GET
f = urllib.urlopen("http://searchengine.com/search" + "?" + enc_data)
print "Метод GET: ", f.read()

# метод POST
f = urllib.urlopen("http://searchengine.com/search", enc_data)
print "Метод POST: ", f.read()

