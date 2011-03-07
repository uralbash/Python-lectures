# -*- coding: cp1251 -*-
"""
    Лекция 4. Работа со строками и файлами
    Пример 10: Пример простейшего скрипта для резервного копирования файлов, с ведением лога
        
"""

import shutil, sys, os, datetime

# каталог запущенного скрипта
path = os.path.realpath(os.path.dirname(sys.argv[0]))
print path

# путь к файлу лога (рядом с самим скриптом, в той же папке)
logpath = path + "/backup.log"

# открытие файла лога на добавление (если файла нет, он будет создан)
logfile = open(logpath, "a")

# записываем в лог текущие дату и время
print >> logfile, datetime.datetime.now()
print >> logfile, ''

# копирование файла поверх существующего (бэкап)
try:
    #shutil.copyfile("\\\\Comp1Name\\e$:\\Folder\\file.ext", "\\\\Comp2Name\\c$:\\Backups\\file.ext")
    shutil.copyfile("myTextFile", "backups/myTextFile")
    print >> logfile, "successfully"
except:
    print >> logfile, sys.exc_info()[0] # тип ошибки
    print >> logfile, sys.exc_info()[1] # текст ошибки
print >> logfile, '=================================================='
logfile.close()

