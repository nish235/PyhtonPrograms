d = 3
for x in range(d, -(d + 1), -1):
    for y in range(abs(x), d + 1):
        print(y, end=" ")
    print()

