f = open('abc.txt')
f1 = open('xyz.txt', 'a')
for i in f.readlines():
    f1.write(i)
f.close()
f1.close()
print("Data Copied Successfully")
