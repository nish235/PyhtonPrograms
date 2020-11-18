def wish(name):
    print("hello", name, "good morning")


def decor(fun):
    def inner(name):
        if name == "sunny":
            print("hello sunny bad morning")
        else:
            fun(name)

    return inner


@decor
def wish(name):
    print("hello", name, "good morning")


wish("Durga")
wish("ravi")
wish("sunny")
