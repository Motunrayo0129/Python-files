binary = int(input('Enter binary number: '))

decimal = 0
values = 0

while binary > 0:
	if binary > 1:
	print('Invalid input')
	break

	last_digit = binary % 10
	decimal += last_digit * (2 ** values)

	binary //= 10
	values += 1

print(f'The decimal number is {decimal}')