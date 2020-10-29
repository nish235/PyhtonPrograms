import array as arr
a = arr.array('i', [])
print(a)

for i in range(0, 100):
    a.insert(i, i)
print(a)

# string
s = str(a)
for i in s:
    print(i, end="")
print("\n", type(s))

# list
l1 = list(a)
print(l1)

# Tuple
t = tuple(a)
print(t)

# Set
s = set(a)
print(s)
