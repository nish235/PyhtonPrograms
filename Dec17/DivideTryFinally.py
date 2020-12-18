a = int(input("Enter a : "))
b = int(input("Enter b : "))


def divide(x, y):
    try:
        res = x // y
    except ZeroDivisionError:
        print("Sorry ! You Are Dividing By Zero ")
    finally:
        print("This Is Always Be Executed ")


divide(a, b)
