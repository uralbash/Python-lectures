import cPickle

flights = {"1":"A", "2":"B","3":"C"}
times = ["230pm", "320pm", "420pm"]

f = open("pickled.dat", "w")

p = cPickle.Pickler(f)

p.dump(flights)
p.dump(times)
f.close()

f = open("pickled.dat", "r")
data = f.read()
print data
f.close()
