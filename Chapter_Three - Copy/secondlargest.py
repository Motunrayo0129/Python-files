largest = None
second_largest = None
 
for numbers in range(11):
	numbers = int(input('Enter an integers: '))

	if largest is None or numbers > largest:
		second_largest = largest

		largest = numbers
	elif second_largest is None or numbers > second_largest:
		second_largest =numbers

print(f'The largest number is {largest}')
print(f'The second largest number is {second_largest}') 