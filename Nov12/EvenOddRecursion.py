def check(n):
    if n < 2:
        return n % 2 == 0
    return check(n - 2)


num = int(input("Enter number:"))
if check(num):
    print("Number is even!")
else:
    print("Number is odd!")
