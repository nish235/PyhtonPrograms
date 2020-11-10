def infinite():
    x = 0
    while True:
        yield x
        x = x + 1


n = infinite()

for i in n:
    print(i)
