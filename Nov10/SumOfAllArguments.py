def add(*args):
    t = 0
    for i in args:
        t = t + i
    return t


print(add(2, 4, 6, 8))
