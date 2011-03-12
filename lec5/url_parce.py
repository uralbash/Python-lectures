# coding: utf-8
#Функции для анализа URL
"""
Согласно документу RFC 2396 URL должен строиться по следующему шаблону:
scheme://netloc/path;parameters?query#fragment
где
scheme - Адресная схема. Например: http, ftp, gopher.
netloc - Местонахождение в сети.
path - Путь к ресурсу.
params - Параметры.
query - Строка запроса.
fragment - Идентификатор фрагмента.
"""
import urllib

print "urllib.quote: ", urllib.quote("rnd@onego.ru")
print "urllib.quote: ", urllib.quote("a = b + c")
print "urllib.quote: ", urllib.quote("0/1/1")
print "urllib.quote: ", urllib.quote("0/1/1", safe="")
print ""
print "urllib.unquote: ", urllib.unquote('a%20%3D%20b%20%2B%20c')

from urlparse import urlsplit, urlunsplit
URL = "http://google.com/search?q=Python"
print "urlsplit: ", urlsplit(URL)
print "urlunsplit: ", urlunsplit(('http', 'google.com', '/search', 'q=Python', ''))

#Еще одна функция того же модуля urlparse позволяет корректно соединить две части URL - базовую и относительную:

import urlparse
print "urljoin", urlparse.urljoin('http://python.onego.ru', 'itertools.html')


