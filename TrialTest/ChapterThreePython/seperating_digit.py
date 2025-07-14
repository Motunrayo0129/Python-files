number = int(input("Enter a five digit number: "))
if 10000 <= number <= 99999:
    divisor = 10000

    for _ in range(5):
        digit = number // divisor
        number -= digit * divisor
        divisor //= 10
        print(digit, end = ' ')
else:
    print("That number is too large. enter five digit numbers.")