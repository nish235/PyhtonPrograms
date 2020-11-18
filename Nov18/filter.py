def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


l1 = [0, 5, 10, 15, 20, 25, 30]
l2 = list(filter(isEven, l1))
print(l2)
