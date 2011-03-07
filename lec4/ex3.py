# coding=utf8
"""
    Лекция 4. Работа со строками и файлами
    Пример 3: Итерация по линиям
        
"""
filename = "myTextFile"

f = open(filename)
for line in f:
    print line

