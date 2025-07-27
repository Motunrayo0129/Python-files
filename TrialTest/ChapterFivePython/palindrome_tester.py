def string_palindrome(string):
    string = string.lower()
    stack = []
    stack.append(string)
    for char in string:
        if string[0] == string[-1] and string[1] == string[-2]:
            return True
        else:
            return False

print(string_palindrome('hello'))
