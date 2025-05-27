''' def get_cube(number):
	if number <= 10:
		return number ** 3
	
	return "invalid number" '''

def get_cube(number):
	if number in range(1, 11):
		return number ** 3
	raise ValueError