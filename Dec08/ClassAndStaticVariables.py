class Student:
    stream = 'IT'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


a = Student('Ram', 1)
b = Student('Sham', 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)
print(Student.stream)
