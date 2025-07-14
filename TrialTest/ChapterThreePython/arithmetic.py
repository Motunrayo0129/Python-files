sum = 0
average = 0
largest = 0
smallest = 1000000000000
for num in range(1, 4):
    numbers = int(input("Enter a number: "))
    sum += numbers
    average = sum / num

    if numbers > largest:
        largest = numbers
    elif numbers < smallest:
        smallest = numbers

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest is: {largest}")
print(f"The smallest is: {smallest}")



