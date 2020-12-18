class EvenOdd(Exception):
    pass


a = int(input("Enter The Number : "))

if a % 2 == 0:
    raise EvenOdd("Even Number")
else:
    raise EvenOdd("Odd Number")
