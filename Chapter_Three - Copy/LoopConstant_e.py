def factorial(n):
    result = 1
    for numbers in range(1, n + 1):
        result *= numbers
    return result

number = 10  
e_value = sum(1 / factorial(i) for i in range(number))

print(f"Approximation of e using {number} terms: {e_value}")