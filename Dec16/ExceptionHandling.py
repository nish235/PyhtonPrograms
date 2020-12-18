print("Before")

a, b = 2, 4
print(a + b)
l1 = [1, 2, 3, 4, 5]

try:
    # c = 4/0
    for i in range(6):
        print(l1[i])

except ZeroDivisionError as ob1:
    print("Error Generated", ob1)
except IndexError as ob2:
    print("Error Generated", ob2)
