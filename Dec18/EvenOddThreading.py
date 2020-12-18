from threading import *


class Even(Thread):
    def run(self):
        for j in range(10):
            if j % 2 == 0:
                print("Even : ", j)


class Odd(Thread):
    def run(self):
        for i in range(10):
            if i % 2 != 0:
                print("Odd  : ", i)


t1 = Even()
t2 = Odd()
t1.start()
t2.start()
