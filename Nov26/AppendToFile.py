f = open("abc.txt", "a")
f.write("ginny\n")
f.close()

a = open("abc.txt", "r")
print(a.read())
