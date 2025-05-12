number = int(input("Enter a five-digit integer: "))

num_digits = len(str(number))

if num_digits != 5:
    print("Please enter a valid five-digit integer.")
else:
    divisor = 10**(num_digits - 1)  
    while divisor > 0:
        digit = number // divisor  
        print(digit, end=" ") 
        number %= divisor  
        divisor //= 10 