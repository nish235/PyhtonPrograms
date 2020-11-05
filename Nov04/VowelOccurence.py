n = "We are learning python"
lo = n.lower()
d = {}
for i in "aeiou":
    count = lo.count(i)
    d[i] = count
print(d)
