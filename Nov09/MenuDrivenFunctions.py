def armstrong():
    num = int(input("Enter a number: "))
    s = 0

    temp = num
    while temp > 0:
        dig = temp % 10
        s = s + dig ** 3
        temp = temp // 10

    if s == num:
        print(num, "is an Armstrong number")
        print()
    else:
        print(num, "is not an Armstrong number")
        print()
    menu()


def palindrome():
    num = int(input("Enter a number: "))
    s = 0

    temp = num
    while temp > 0:
        dig = temp % 10
        s = s * 10 + dig
        temp = temp // 10

    if s == num:
        print(num, "is a Palindrome number")
        print()
    else:
        print(num, "is not a Palindrome number")
        print()
    menu()


def reverse():
    num = int(input("Enter a number: "))
    s = 0

    temp = num
    while temp > 0:
        dig = temp % 10
        s = s * 10 + dig
        temp = temp // 10

    print("Reverse Of the Number is :", s)
    print()
    menu()


def even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is an Even number")
        print()
    else:
        print(num, "is a Odd Number")
        print()
    menu()


def qu():
    print("Exiting Program!!  Bye !! ")


def menu():
    print("Choose Options To Perform : ")
    print("1.Armstrong")
    print("2.Palindrome")
    print("3.Reverse")
    print("4.Even Or Odd")
    print("5.Exit")
    print("Enter Your Choice :")
    choice = int(input())
    if choice == 1:
        armstrong()
    elif choice == 2:
        palindrome()
    elif choice == 3:
        reverse()
    elif choice == 4:
        even()
    elif choice == 5:
        qu()
    else:
        print("Invalid Choice")
        menu()


menu()
