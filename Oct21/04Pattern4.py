for i in range(1, 6):
    num = 1
    for z in range(i):
        print('    ', end='')
    for k in range(i, 6):
        print(num, '', end='')
        num += 1
    print('\n')
