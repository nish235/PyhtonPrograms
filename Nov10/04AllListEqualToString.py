x = ["a", "b", "c", "d", "e", "f"]
y = ["a", "a", "a", "a", "a", "a"]

print(all(z == 'b' for z in x))
print(all(z == 'a' for z in y))
