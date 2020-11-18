n = int(input("Enter The Number : "))
print("Even : ")
for n in range(n):
    x = lambda n: n if n % 2 == 0 else ""
    print(x(n))
print("Odd : ")
for n in range(n):
    x = lambda n: n if n % 2 == 1 else ""
    print(x(n))
