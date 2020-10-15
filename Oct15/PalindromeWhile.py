num = int(input("Enter a number: "))

s = 0

temp = num
while temp > 0:
   dig = temp % 10
   s = s * 10 + dig
   temp = temp // 10

if s == num:
   print(num, "is a Palindrome number")
else:
   print(num, "is not a Palindrome number")