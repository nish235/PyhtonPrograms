import array as arr

n = arr.array('i', [1, 2, 3, 4, 4, 5, 6])

n.pop()
print(n)

n.pop(1)
print(n)

n.remove(3)
print(n)

n.index(1)
print(n)
