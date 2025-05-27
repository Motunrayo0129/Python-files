investment_amount = int(input("Enter investment amount: "))
rate = float(input("Enter interest rate: "))/100
years_of_investment = int(input("Enter years of investment: "))
for number in range(0, years_of_investment, 1):
	interest_rate = float(investment_amount * rate) 
	investment_amount += interest_rate 
	print(f"The return amount for {number + 1} years is {investment_amount:,.2f}")