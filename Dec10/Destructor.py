import time


class Test:
    def __init__(self):
        print("Object Initialization...")

    def __del__(self):
        print("Fulfilling Last Wish and Performing Clean up Activities...")


t1 = Test()
t1 = None
time.sleep(5)
print("End Of Application")
