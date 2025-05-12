total_gallons = 0
total_miles = 0

while True:
	miles = float(input('Enter the miles driven (-1 to end): '))
	
	if miles == -1:
		break

	gallons = float(input('Enter the gallons used (-1 to end): '))

	mpg = miles / gallons
	print(f"The miles per gallons for this tank was {mpg:.2f} ")

	total_miles += miles
	total_gallons += gallons
	
	if total_gallons > 0:
		overall_mpg = total_miles / total_gallons
		print(f'Overall average miles/gallons was {overall_mpg:.2f}')
	
	else:
		print('No valid data entered')