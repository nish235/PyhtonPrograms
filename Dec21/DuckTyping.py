class Duck:
    def talk(self):
        print("Quack...Quack")


class Dog:
    def talk(self):
        print("Bow...Bow")


class Cat:
    def talk(self):
        print("Meow...Meow")


class Goat:
    def talk(self):
        print("Myah...Myah")


def f1(obj):
    obj.talk()


l1 = [Duck(), Cat(), Dog(), Goat()]
for obj in l1:
    f1(obj)
