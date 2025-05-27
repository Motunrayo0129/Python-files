
print("""purchases between 1000 and 10000 receives a 5% discount
purchases between 10000 and 50000 receives a 10% discount
purchases between 10000 and 50000 receives a 20% discount""")

amount = int(input("Enter amount: "))

if amount <= 0 and amount < 1000:
	print("No discount")
	
elif amount > 1000 and amount <= 10000:
	discount_rateA = amount * 0.05
	discount_priceA = amount - discount_rateA
	print(f"The discount price is {discount_priceA:,}")

elif amount > 10000 and amount <= 50000:
	discount_rateB = amount * 0.10
	discount_priceB = amount - discount_rateB
	print(f"The discount price is {discount_priceB:,}")

elif amount > 50000:
	discount_rateC = amount * 0.20
	discount_priceC = amount - discount_rateC
	print(f"The discount price is {discount_priceC:,}")	




	
	
	