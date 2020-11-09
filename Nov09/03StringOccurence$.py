def change(st1):
    char = st1[0]
    st1 = st1.replace(char, '$')
    st1 = char + st1[1:]

    return st1


print(change('nishant'))
