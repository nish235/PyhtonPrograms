d = 7
for x in range(4, 0, -1):
    for y in range(x, 5):
        print(" ", end="")
    for z in range(1, d + 1):
        print(chr(d + 64), end="")
    d -= 2
    print()

