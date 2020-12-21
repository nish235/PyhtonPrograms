class Duck:
    def talk(self):
        print("Quack...Quack")


class Dog:
    def bark(self):
        print("Bow...Bow")


class Human:
    def talk(self):
        print("Hello...Hi")


def f1(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()


d = Duck()
f1(d)

h = Human()
f1(h)

d = Dog()
f1(d)
