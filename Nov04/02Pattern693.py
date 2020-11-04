n = 9
a = n//2+1
p = 1
for x in range(1, n+1):
    for y in range(1, n+1):
        if y == a or y == n-a+1:
            print(a, end=" ")
        else:
            print(" ", end=" ")
    if x <= n/2:
        a -= 1
        p += 1
    else:
        a += 1
        p -= 1
    print()
