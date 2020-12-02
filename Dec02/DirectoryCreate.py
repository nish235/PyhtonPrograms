import os
name = input("Enter your name : ")
for char in name:
    print(char)
    os.mkdir(char)
    print(char + " Directory successfully created")
