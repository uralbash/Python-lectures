# coding=utf8
"""
    Лекция 4. Работа со строками и файлами
    Пример 6: Запись в файл
        
"""

filename = "myTextFile"
filename2 = "myTextFile2"

f1 = open(filename, "r")
f2 = open(filename2, "w")
for line in f1.readlines():
    f2.write(line)
f2.close()
f1.close()
