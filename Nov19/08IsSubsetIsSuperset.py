x = set(["a", "b", "c", "d", "e", "f"])
y = set(["a", "c", "e"])

print("If y is subset of x")
print(y.issubset(x))
print(x.issubset(y))
print("If x is superset of y")
print(x.issuperset(y))
print(y.issuperset(x))
