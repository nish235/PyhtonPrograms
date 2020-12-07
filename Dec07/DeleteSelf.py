class demo:
    def __init__(self):
        self.a = 2
        self.b = 3
        del self.a


d = demo()
print(d.a)
print(d.b)
