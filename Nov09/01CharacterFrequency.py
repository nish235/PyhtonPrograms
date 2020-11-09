def frequency(st1):
    d = {}
    for n in st1:
        keys = d.keys()
        if n in keys:
            d[n] += 1
        else:
            d[n] = 1
    return d


print(frequency('We Are learning Python'))
