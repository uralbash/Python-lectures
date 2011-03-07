# -*- coding: cp1251 -*-
"""
    Лекция 4. Работа со строками и файлами
    Пример 8: Обработка файлов
        
"""
import os
import random
import linecache
import stat
import time
import datetime
import shutil

filename = "myTextFile"
filename2 = "myTextFile2"
log = "tmp/logfile"
log1 = "tmp/logfile1"
binfile = "get_response.png"

def _print(argStr):
    print unicode(argStr, 'cp1251')

# чтение строк файла в обратном порядке
for line in reversed(open(filename).readlines()):
    print line

# чтение строк файла в случайном порядке
lines = open(filename).readlines()
random.shuffle(lines)
for line in lines:
    print line

# чтение нужной строки файла по номеру
line = linecache.getline(filename, 2) # вторая строка
print line
line = open(filename).readlines()[1] # вторая строка
print line

# чтение бинарного файла
bmp_file = open(binfile, "rb")
buff = bmp_file.read(10) # первые 10 байт
print buff
print bmp_file.tell() # текущая позиция в файле.
bmp_file.seek(0) # возврат в начало файла
print bmp_file.tell()
buff = bmp_file.read(2) # первые 2 байта
print buff
bmp_file.close()

# запись бинарного файла
bmp_file = open(binfile, "rb")
buff = bmp_file.read()
bmp_file.close()
bmp_file = open(log, "wb")
bmp_file.write(buff)
bmp_file.close()

# некоторые атрибуты файлов
fstat = os.stat(filename)
print stat.S_ISDIR(fstat.st_mode) # признак папки
print stat.S_ISREG(fstat.st_mode) # признак обычного файла
print fstat.st_size # размер файла, в байтах
st_atime = fstat.st_atime # время последнего доступа (число секунд с начала эпохи, 1970 г.)
a,b,c,d,e,f,g,h,i = time.localtime(st_atime)
print datetime.datetime(a,b,c,d,e,f,g)
st_mtime = fstat.st_mtime # время последней модификации
a,b,c,d,e,f,g,h,i = time.localtime(st_mtime)
print datetime.datetime(a,b,c,d,e,f,g)
st_ctime = fstat.st_ctime # время создания
a,b,c,d,e,f,g,h,i = time.localtime(st_ctime)
print datetime.datetime(a,b,c,d,e,f,g)

# установка некоторых атрибутов
open(log, "w").close()
# задание текущего времени последнего доступа и модификации
os.utime(log, None)
# задание указанного времени последнего доступа и модификации
os.utime(log, (1, 1))
# снятие и установка атрибута "только чтение"
os.chmod(log, stat.S_IREAD) # поставить read-only
os.chmod(log, stat.S_IWRITE) # снять read-only

# обработка ошибки удаления файла
try:
    os.remove("несущестувующий файл")
except OSError, err:
    _print("Ошибка удаления файла.")

# перебор файлов в каталоге
for filename in os.listdir("./"):
    print filename

# поиск файлов по маске
import glob
[_print(filename) for filename in glob.glob("*.png")]

# рекурсивный перебор каталогов
for root, dirs, files in os.walk(log):
    _print("root: " + root)
    if len(dirs):
        _print("dirs:")
        [_print(dir) for dir in dirs]
    if len(files):
        _print("files:")
        [_print(file) for file in files]

# создание каталога
os.mkdir("tmp/newdir")
os.mkdir("tmp/newdir/1")
# удаление каталога со всем содержимым
shutil.rmtree("tmp/newdir") # осторожно!

# переименование файла
open(log, "w").close()
os.rename(log, log1)
# разбор пути (папка, имя файла, расширение)
print "basename: ",os.path.basename(filename)
print "dirname: ", os.path.dirname(filename)
print "split: ", os.path.split(filename)
print "splitext: ", os.path.splitext(filename)
