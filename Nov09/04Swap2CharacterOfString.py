def char(a, b):
    x = b[:2] + a[2:]
    y = a[:2] + b[2:]

    return x + ' ' + y


print(char('nishant', 'rohit'))
