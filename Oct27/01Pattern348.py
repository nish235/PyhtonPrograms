i = 1
for x in range(5, 0, -1):
    for y in range(x, 0, -1):
        print(" ", end=" ")
    for z in range(1, i+1):
        print(z, end=" ")
    i += 2
    print()
