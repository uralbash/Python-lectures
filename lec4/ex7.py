# -*- coding: utf8 -*-
"""
    Лекция 4. Работа со строками и файлами
    Пример 7: Работа с файлами
        
"""


filename = "myTextFile"
filename2 = "myTextFile2"
log = "tmp/logfile"

# открытие и чтение текстового файла построчно
for line in open(filename):
    print(line)

# ведение лога
logfile = open(log, "w")
print>>logfile, "Какой-то текст"
print>>logfile, "Ещё какой-то текст"
logfile.close()
# проверка, открыт ли файл
print logfile.closed

# обработка ошибки открытия файла
try:
    myfile = open("несуществующий файл")
except IOError, err:
    print err.strerror

# создание и использование временного файла
# файл автоматически удаляется, как только он будет закрыт 
import tempfile
myfile = tempfile.TemporaryFile(bufsize = 0)
print myfile.name # полный путь
for i in range(10):
    print>>myfile, i
myfile.seek(0)
print("Сейчас во временном файле:\n" + myfile.read())
myfile.close()

# копирование файлов
import shutil
shutil.copyfile(filename, "123")

# удаление файла
import os
os.remove(filename2)
os.remove("123")

# перезапись содержимого файла
myfile = open(log, "w")
print>>myfile, "текст"
myfile.close()
# собственно перезапись
myfile = open(log, "r+")
data = myfile.read()
data += "добавленный текст"
myfile.seek(0, 0)
myfile.write(data)
myfile.truncate(myfile.tell())
myfile.close()
for line in open(log):
    print line
os.remove(log)
