num = int(input("Enter The Number : "))

for i in range(1, num+1):
    t = i
    s = 0
    while t > 0:
        d = t % 10
        s = d ** 3
        t = t // 10
    if i == s:
        print(" ", i, end=" ")
