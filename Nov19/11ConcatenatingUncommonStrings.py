def uncommon(st1, st2):
    set1 = set(st1)
    set2 = set(st2)

    common = list(set1 & set2)
    result = [ch for ch in st1 if ch not in common] + [ch for ch in st2 if ch not in common]
    return ''.join(result)


s1 = 'abcdpqrs'
s2 = 'xyzabcde'
print("Original Substrings:\n", s1 + "\n", s2)
print("\nAfter concatenating uncommon characters:")
print(uncommon(s1, s2))
