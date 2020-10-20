import array as arr

n = [2, 5, 62, 5, 42, 52, 48, 5]
a1 = arr.array('i', n)

print(a1[2:5])
print(a1[:-5])
print(a1[5:])
print(a1[:])
