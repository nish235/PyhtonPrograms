from threading import *
import time


def display():
    for i in range(5):
        print("Sita Thread")
        time.sleep(1)


t = Thread(target=display)
t.start()
print(t.is_alive())
t.join()
print(t.is_alive())
for i in range(5):
    print("Ram Thread")
