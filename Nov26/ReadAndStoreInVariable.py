f = open("abc.txt", "r")
l1 = []
for i in f:
    l1.append(i)
print(l1)
f.close()
