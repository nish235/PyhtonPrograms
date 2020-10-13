a = float(input('Enter first side  : '))
b = float(input('Enter second side : '))
c = float(input('Enter third side  : '))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The Area Of Triangle with Sides {0}, {1} and {2} is {3}'.format(a, b, c, area))
