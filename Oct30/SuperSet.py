# Write a Python program to check if a given set is superset of itself and superset of another given set

s = {11, 12, 13, 14, 20, 30}
print("Whether Superset Of Itself :")
print(s.issuperset(s))
x = {1, 2, 3, 4, 5, 6}
print("Whether Superset to Another Set : ")
print(x.issuperset(s))
