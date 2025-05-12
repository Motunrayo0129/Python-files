sum = 0
product = 1
average = 0
largest = None 
smallest = None 

for number in range(0, 3, 1):
	integers = int(input('Enter an integer: '))

	sum += integers
	product *= integers
	average = sum / 3
	if smallest is None or integers < smallest:
		smallest = integers
	if largest is None or integers > largest:
		largest =  integers

print(f'The sum of the integers is {sum}')
print(f'The product of the integers is {product}')
print(f'The largest of the integers is {largest}')
print(f'The smallest of the integers is {smallest}')
print(f'The average of the integers is {average}')


		
	