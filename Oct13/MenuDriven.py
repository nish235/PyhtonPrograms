print(" 1.Add")
print(" 2.Subtract")
print(" 3.Multiply")
print(" 4.Divide")

ch = int(input("\n Enter The Number (1-4) : "))

a = int(input("\n Enter 1st number : "))
b = int(input("\n Enter 2nd number : "))

if ch == 1:
    c = a + b
    print("\n Addition Is = ", c)
elif ch == 2:
    d = a - b
    print("\n Subtraction Is = ", d)
elif ch == 3:
    e = a * b
    print("\n Multiplication Is = ", e)
elif ch == 4:
    f = a / b
    print("\n Divison Is = ", f)
else:
    print("\n Invalid Input ")
