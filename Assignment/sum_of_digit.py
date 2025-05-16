def sum_of_digit(number):
	total = 0
	while number > 0:
		total += number % 10
		number //= 10

	return total

user_input = int(input('Enter number from 1 to 10000: '))
	if user_input <= 10000:
		total_digit = sum_of_digit(user_input)
		print(f'{total_digit} are the sum of your digits')
	
	else:
		print("Invalid input, enter number between 1 to 10,000.")
 