# -*- coding: cp1251 -*-
"""
    Лекция 4. Работа со строками и файлами
    Пример 8: определение каталога запущенного скрипта
        
"""

import os
import sys

print os.path.realpath(os.path.dirname(sys.argv[0]))
print os.path.realpath(os.path.dirname(sys.modules['__main__'].__file__))

