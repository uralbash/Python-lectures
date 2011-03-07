# coding=utf8
"""
    Лекция 4. Работа со строками и файлами
    Пример 4: Итерация по линиям без сохранения объекта с дескриптором файл в
    переменной
        
"""
filename = "myTextFile"

# Вариант 1
for line in open(filename):
    print line

# Вариант 2
for line in file(filename):
    print line
