f = open("abc.txt", "r")

l1 = []
for i in f:
  s = i.strip()
  line = s.split()
  l1.append(line)

f.close()

print(l1)
