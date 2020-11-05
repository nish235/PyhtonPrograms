n = "we are learning python"
d = {}

for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(str(d))
