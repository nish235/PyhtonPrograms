import array as arr

n = arr.array('i', [1, 2, 3, 5, 7, 10])

n[0] = 0
print(n)

n[2:5] = arr.array('i', [4, 6, 8])
print(n)
