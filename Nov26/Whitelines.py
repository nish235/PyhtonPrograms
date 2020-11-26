f = open("abc.txt", 'w')

l1 = ["sunny\n", "bunny\n", "binny\n", "shinny\n"]
f.writelines(l1)
print("List of lines written to the file successfully")
f.close()
