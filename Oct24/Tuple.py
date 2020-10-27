t1 = ()
print(type(t1))

t1 = (23,)
print(type(t1))

t1 = (23, 34)
print(type(t1))

print(t1[0], t1[-1])

l1 = [2, 3, 4]
t1 = tuple(l1)
print(t1)

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d
print(t)

a, b, c, d = t
print(a, b, c, d)

