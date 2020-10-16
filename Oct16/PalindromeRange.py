num = int(input("Enter The Number : "))

for i in range(1, num+1):
    t = i
    rev = 0
    while t > 0:
        rem = t % 10
        rev = (rev * 10) + rem
        t = t // 10
    if i == rev:
        print(" ", i, end=" ")
