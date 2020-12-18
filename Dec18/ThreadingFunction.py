from threading import *


class Even(Thread):
    def run(self):
        for j in range(10):
            if j % 2 == 0:
                print(current_thread().getName(), j,current_thread().ident)


class Odd(Thread):
    def run(self):
        for i in range(10):
            if i % 2 != 0:
                print(current_thread().getName(), i,current_thread().ident)


t1 = Even()
t2 = Odd()
t1.setName("Even")
t2.setName("Odd")
t1.start()
t2.start()

current_thread().setName("Hello")
print(current_thread().getName())
