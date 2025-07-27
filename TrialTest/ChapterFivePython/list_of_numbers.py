def multiply_numbers(list_of_numbers, number):
	result =[]
	for value in list_of_numbers:
		answer = value * number
		result.append(answer)
	return result


print(multiply_numbers([3, 4, 6, 7, 10], 4))