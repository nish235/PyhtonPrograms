import string


def pan(str1, alphabet=string.ascii_lowercase):
    alpha = set(alphabet)
    return alpha <= set(str1.lower())


print(pan('The quick brown fox jumps over the lazy dog'))
