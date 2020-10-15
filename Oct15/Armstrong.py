

num = int(input("Enter 3 Digit Number : "))
temp = num

n1 = int(num % 10)
num = int(num / 10)
n2 = int(num % 10)
num = int(num / 10)
n3 = int(num % 10)
num = int(num / 10)

s = n1**3 + n2**3 + n3**3

print(s)

if s == temp:
    print(num, "Is A Armstrong Number")
else:
    print(num, "Its Not A Armstrong Number")
