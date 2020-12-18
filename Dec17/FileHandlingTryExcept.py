try:
    f = open("abc.txt", "a")
    f.write("This Is the program for File Handling using Exception Handling")
except IOError:
    print("Error : Can't Find File")
finally:
    f.close()
    print("Successful")
