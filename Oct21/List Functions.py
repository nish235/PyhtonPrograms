# append
a = [1, 2, 3]
a.append(4)
print('Updated list: ', a)

# insert
a = [1, 2, 3]
a.insert(3, 6)
print('Updated list: ', a)

# extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print('Updated list: ', a)

# remove
a = [12, 23, 34, 45, 56, 67]
a.remove(45)
print('Updated list: ', a)

# pop
a = [12, 23, 34, 45, 56, 67]
p = a.pop(2)
print('Popped Value: ', p)
print('Updated list: ', a)
p1 = a.pop()
print('Popped Value: ', p1)
print('Updated list: ', a)
