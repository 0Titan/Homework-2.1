def is_palindrome(s):
    A = [a.lower() for a in s if a.isalpha()]
    return A == A[::-1]
print(is_palindrome('Шалаш'))
