d = 3
for x in range(d, -(d + 1), -1):
    for y in range(d, abs(x) - 1, -1):
        print(chr(abs(y - 68)), end="  ")
    print()

