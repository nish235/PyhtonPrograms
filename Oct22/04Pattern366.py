n = 1
for x in range(5, 0, -1):
    for y in range(x, 0, -1):
        print(" ", end=" ")
    for z in range(n, 0, -1):
        print(chr(z + 64), end=" ")
    n += 2
    print(" ")
