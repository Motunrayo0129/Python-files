number = int(input("Enter a five digit number: "))
if 10000 <= number <= 99999:
    first_digit = number // 10000
    second_digit = (number // 1000) % 10
    third_digit = (number // 100) % 10
    fourth_digit = (number // 10) % 10
    fifth_digit = number % 10

    if first_digit == fifth_digit and second_digit == fourth_digit:
        print(f'{number} is a palindrome')
    else:
        print(f'{number} is not a palindrome')

else:
    print("Enter a five digit number")
