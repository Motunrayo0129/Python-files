def deposit_amount(deposit):
    deposit > 0:
    balance = deposit_amount
    return balance

    return "Amount must be greater than 0"
                
def withdrawn_amount(balance, withdrawal):
wthdrawal_percentage = (balance / 100) * 90
        if withdrawal % 500 == 0:
            if withdrawal > 0 & withdrawal <= withdrawal_percentage:
                charges = 100
                updated_balance = balance - withdrawal - charges
                print("Transaction successful.")
                print(f"Withdrawal amount: {withdrawal}\n charges: {charges}\n remaining balance: {updated_balance}")

            else: 
                print("Invalid amount: amount should not be greater than 90% of your balance")

                return updated_balance
       
        else: 
                print("Enter multiple of 500 or 100 only")
  

withdrawal_amount = 0
print(""" 
__________________________________________________
	Welcome To Motunrayo Banking Atm
__________________________________________________
 """)
new_amount = int(input("Enter deposit amount: "))
balance = 0;
print(deposit_money(balance, new_amount))

print("Do you want to withdraw: Enter 1 for yes and 2 for no:  ")
choice = int(input("Enter your choice: "))
if choice == 1:
    while new_amount > 0:
        withdraw = int(input("Enter amount: "))
        print(withdrawn_amount(withdraw, balance))
        ask = int (input("Do you want to make another withdrawal: press 1 to continue: "))
        if ask == 1:
            withdrawal_amount = True
    
        else:
            new_amount = false
    break

        

    


            

                            

 

  




