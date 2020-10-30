s = 4
p = 0
for x in range(s, -(s + 1), -1):
    for y in range(1, abs(x) + 1):
        print(" ", end="")
    for z in range(s, abs(x) - 1, -1):
        print(chr(p + 65) + " ", end="")
    if x > 0:
        p += 1
    else:
        p -= 1
    print()
