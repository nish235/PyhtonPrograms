d = {}
n = int(input("Enter The Number : "))

for i in range(n):
    print("Enter Name Of Student : ")
    keys = input()
    print("Enter The Marks Obtained : ")
    values = int(input())
    d[keys] = values
print(d)

