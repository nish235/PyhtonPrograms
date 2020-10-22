n = 1
for x in range(1, 6):
    for y in range(5, x, -1):
        print(" ", end=" ")
    for z in range(1, n + 1):
        print(chr(abs(z - x) + 65), end=" ")
    n += 2
    print(" ")
