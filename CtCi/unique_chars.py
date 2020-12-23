def is_unique(n):

    ascii_dict = {}
    ascii_number = range(0, 256)
    for i in ascii_number:
        ascii_dict[chr(i)] = False
    for char in n:
        if ascii_dict[str(char)] == False:
            ascii_dict[str(char)] = True
        else:
            return False
    return True

print(is_unique("ab"))
print(is_unique("acdefggf"))
print(is_unique("acdefg"))
print(is_unique(""))
