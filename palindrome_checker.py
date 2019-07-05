def is_palindrome(string):
    first = 0
    last = len(string) - 1
    while first <= last:
        if string[first] == string[last]:
            first += 1
            last -= 1
        else:
            return False
    print("{} is a palindrome".format(palindrome))

palindrome = 'Mallam'
is_palindrome(palindrome.lower())
