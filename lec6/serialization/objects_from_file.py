import cPickle

f = open("pickled.dat", "r")

p = cPickle.Unpickler(f)

data = p.load()
print data

data = p.load()
print data

f.close()
