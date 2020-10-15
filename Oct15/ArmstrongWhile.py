
num = int(input("Enter a number: "))

s = 0

temp = num
while temp > 0:
   dig = temp % 10
   s = s + dig ** 3
   temp = temp // 10

if s == num:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")
