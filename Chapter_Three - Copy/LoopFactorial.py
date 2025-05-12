number = int(input("Enter an integer for factorial: "))

if number < 0:
    print("Please enter a nonnegative integer.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i  
    print(f"{number}! = {factorial}")