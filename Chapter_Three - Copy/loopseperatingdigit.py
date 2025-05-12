num = int(input("Enter a five-digit integer: "))

divisor = 10000
while divisor > 0:
    digit = num // divisor  
    print(digit, end=" ")  
    num %= divisor  
    divisor //= 10   

print() 