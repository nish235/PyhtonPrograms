num = int(input("Enter The Number : "))


def fact():
    f = 1
    if num < 0:
        print("Negative Number")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            f = f * i
        print("The factorial of", num, "is", f)


fact()
