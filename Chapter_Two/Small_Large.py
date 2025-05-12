num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

largest = num1
smallest = num1

if num2 > largest:
	largest = num2
if num3 > largest:
	largest = num3
print(largest, "Is the largest")

if num2 < smallest:
	smallest = num2
if num3 < smallest:
	smallest = num3
print(smallest, "Is the smallest")



