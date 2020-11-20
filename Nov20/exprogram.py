import exmodule

print("=== Menu Driven ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

ch = int(input("Enter Your Choice : "))
x = int(input("Enter x : "))
y = int(input("Enter y : "))

if ch == 1:
    print(exmodule.add1(x, y))
elif ch == 2:
    print(exmodule.sub1(x, y))
elif ch == 3:
    print(exmodule.mul1(x, y))
elif ch == 4:
    print(exmodule.div1(x, y))
elif ch == 5:
    print("Exiting")
else:
    print("Invalid Input")
