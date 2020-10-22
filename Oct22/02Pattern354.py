n = 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(" ", end=" ")
    for k in range(n, 0, -1):
        print(k, end=" ")
    n += 2
    print(" ")
