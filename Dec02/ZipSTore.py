from zipfile import *
f = ZipFile("file.zip", "r", ZIP_STORED)
names = f.namelist()
for name in names:
    print("File Name:", name)
    print("The Content of this file:")
    f1 = open(name, "r")
    print(f.read)
    print()
