i = 1
for x in range(1, 6):
    for y in range(5, x, -1):
        print(" ", end=" ")
    for z in range(1, i+1):
        print(abs(z - x), end=" ")
    i += 2
    print()
