num = int(input("Enter a number: "))

s = 0

temp = num
while temp > 0:
   dig = temp % 10
   s = s * 10 + dig
   temp = temp // 10

print("Reverse Of the Number is :", s)
