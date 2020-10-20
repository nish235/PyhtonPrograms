import array as arr

n = arr.array('i', [1, 2, 3])

n.append(4)
print(n)

n.extend([5, 6, 7])
print(n)
