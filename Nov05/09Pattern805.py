for x in range(1, 7):
    if x % 2 != 0:
        c = x + 1
    else:
        c = x
    for y in range(6, c, -1):
        print(" ", end=" ")
    for z in range(0, c):
        print("*", end=" ")
    print()
