d = {}
n = int(input("Enter The Number : "))

for i in range(n):
    print("Enter Key : ")
    keys = input()
    print("Enter Value : ")
    values = int(input())
    d[keys] = values
print(d)
s = sum(d[item] for item in d)
print(s)

