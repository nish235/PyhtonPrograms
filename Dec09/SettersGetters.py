class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input("Enter Number Of Students : "))
for i in range(n):
    s = Student()
    name = input("Enter Name : ")
    s.setName(name)
    marks = int(input("Enter Marks : "))
    s.setMarks(marks)

print("Hi", s.getName())
print("Your Marks Are : ", s.getMarks())
print()
