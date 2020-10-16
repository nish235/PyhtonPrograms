st = input(' Enter the string : ')
l = len(st)
p = l-1
index = 0
while index < p:
    if st[index] == st[p]:
        index = index + 1
        p = p-1
        print(" String is a palindrome")
        break
    else:
        print(" String is not a palindrome")
        break
