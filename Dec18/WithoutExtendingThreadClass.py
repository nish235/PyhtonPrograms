from threading import *


class Test:
    def display(self):
        for j in range(10):
            print("Child Thread")


obj = Test()
t = Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread")
