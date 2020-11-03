n = 5
a = 1
b = n * 2 - 1
for x in range(1, n+1):
    for y in range(1, n * 2 + 1):
        if y == a or y == b:
            print(chr(x+64), end="")
        else:
            print(" ", end="")
    a += 1
    b -= 1
    print()
