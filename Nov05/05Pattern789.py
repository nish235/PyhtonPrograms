n = 5
c = n // 2 + 1
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y == c:
            print("o", end=" ")
        elif x == c or y == c:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()

