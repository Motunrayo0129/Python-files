principal_amount = int(input('Enter amount of investment: '))
rate = 0.07
for number_of_years in range(0, 30, 1):
	interest_rate = float(principal_amount * rate)
	principal_amount += interest_rate
	print(f"The return amount for {number_of_years + 1} years is {principal_amount:,.2f}")