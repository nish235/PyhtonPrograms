class InsufficientAmount(Exception):
    pass


w = 100000
bal = 50000

if w < bal:
    print("Successful")
else:
    raise InsufficientAmount("Hello")
