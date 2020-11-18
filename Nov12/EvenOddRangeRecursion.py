def check(n):
    if n < 2:
        return n % 2 == 0
    return check(n - 2)


n = int(input("Enter number:"))
print("Even : ")
for n in range(1, n):
    if check(n):
        print(n, end=" ")
print("\nOdd : ")
for n in range(1, n):
    if check(n) == False:
        print(n, end=" ")


