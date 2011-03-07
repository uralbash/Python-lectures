# coding=utf8
"""
    Лекция 4. Работа со строками и файлами
    Пример 2: 
        Чтение из файла, линия за линией
"""
filename = "myTextFile"

f = open(filename)
for line in f.readlines():
    print line

