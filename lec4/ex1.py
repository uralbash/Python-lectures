# coding=utf8
"""
    Лекция 4. Работа со строками и файлами
    Пример 1: 
        Вывод содержимого файла посимвольно
"""
filename = "myTextFile"

f = open(filename)
for char in f.read():
    print char

