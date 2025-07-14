fifty_above = 0
fifty_below = 0

while(True):
	numbers = int(input("Enter number from 1 to 100 or (-1 to quit): "))
	if numbers == -1:
		break
	if numbers <= 50:
		fifty_below += 1
		print(f"The total number below 50 are {fifty_below}")
	
	elif numbers <= 100:
		fifty_above += 1
		print(f"The total number below 50 are {fifty_above}")
	else:
		print("Invalid input")
		