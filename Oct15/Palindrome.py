

n = int(input("Enter 3 Digit Number : "))
num = n

n1 = int(num % 10)
num = int(num / 10)
n2 = int(num % 10)
num = int(num / 10)
n3 = int(num % 10)
num = int(num / 10)

rev = n1*100 + n2*10 + n3
if n == rev:
    print(n, "Is A Palindrome Number")
else:
    print(n, "Is Not A Palindrome Number")



