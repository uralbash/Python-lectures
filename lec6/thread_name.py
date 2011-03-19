import threading

class TestThread(threading.Thread):
    def run(self):
        print 'Hello, my name is', self.getName()

cazaril = TestThread()
cazaril.setName('Cazaril')
cazaril.start()

ista = TestThread()
ista.setName('Ista')
ista.start()

TestThread().start()
TestThread().start()

