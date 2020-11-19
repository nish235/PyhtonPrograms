def decor(c):
    def mul(a, b):
        if a % 2 == 0 and b % 2 != 0:
            print(a * b)
        else:
            c(a, b)

    return mul


@decor
def add(a, b):
    print(a / b)


add(2, 3)
add(3, 3)
