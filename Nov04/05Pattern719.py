n = 7
a = 1
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if y <= a or y >= n-a+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    if x <= n/2:
        a += 1
    else:
        a -= 1
    print()
