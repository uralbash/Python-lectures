# coding: utf-8
#В некоторых случаях данные имеют повторяющиеся имена. В этом случае в качестве
#параметра urllib.urlencode() можно использовать вместо словаря
#последовательность пар имя-значение:

import urllib
data = [("n", "1"), ("n", "3"), ("n", "4"), ("button", "Привет"),]
enc_data = urllib.urlencode(data)
print enc_data

