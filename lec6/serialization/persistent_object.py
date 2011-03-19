# coding: utf-8
import shelve
s = shelve.open("somefile.db")
s['myobject'] = [1, 2, 3, 4, 'Привет Мир!']
s.close()
 
s = shelve.open("somefile.db")
print s['myobject']
