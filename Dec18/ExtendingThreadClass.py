from threading import *


class MyThread(Thread):
    def run(self):
        for j in range(10):
            print("Child Thread")


t = MyThread()
t.start()
for i in range(10):
    print("Main Thread")
