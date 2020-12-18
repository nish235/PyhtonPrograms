class Error(Exception):
    pass


class Small(Error):
    pass


class Large(Error):
    pass


n = 10

while True:
    try:
        num = int(input("Enter The Number : "))
        if num < n:
            raise Small
        elif num > n:
            raise Large
        break
    except Small:
        print("This value is small...Try Again!")
        print()
    except Large:
        print("This value is large...Try Again!")
        print()

print("You guessed it correct...")
