"""
Prompt the user to enter the principal amount, annual interest rate, duration in years.
Initialize their variable.
Use the formula to calculate their monthly payment.
p is the principal amount.
r is the rate.
n is the duration.
Convert the annual interest rate to a monthly percentage rate.
Multiply number of months in a year from the duration of year.
Display the monthly payment.
"""

principal = float(input("Enter the principal loan amount"))
loan_duration = int (input("Enter the loan duration")) * 12
loan_rate = int(input("Enter the rate: ")) / 100 / 12



a = float (principal) * (loan_rate*(1 + loan_rate)**loan_duration)
b = float((1 + loan_rate)**loan_duration - 1)

monthly_payment = (a / b)

print("Your monthly payment is $", round (monthly_payment, 2)) 