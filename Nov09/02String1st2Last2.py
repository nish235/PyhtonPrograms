def string(st1):
    if len(st1) < 2:
        return ''
    return st1[0:2] + st1[-2:]


print(string('Nishant'))

