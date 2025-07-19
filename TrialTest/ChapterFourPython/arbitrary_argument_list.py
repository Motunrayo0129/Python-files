def numbers(*args):
    result = 1
    for number in args:
        result = result * number
    return result

print(numbers(3, 6, 12))