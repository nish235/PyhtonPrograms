import functools

l1 = [1, 3, 5, 6, 2]

print("The Sum Of List Is : ", end=" ")
print(functools.reduce(lambda a, b: a + b, l1))

print("The Maximum element of the list is : ", end=" ")
print(functools.reduce(lambda a, b: a if a > b else b, l1))
