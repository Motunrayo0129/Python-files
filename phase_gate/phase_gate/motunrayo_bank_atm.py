def deposit(balance, amount):
    if amount > 0:
        new_balance = amount + balance
        print(f"Transaction successful")
        return new_balance
    else:
        print("Amount must be greater than 0")
        return balance
                
def withdraw(balance, amount, transactions):
    percentage = (balance * 100) / 90
    charges = 100
    if amount % 500 != 0:
        print("Enter multiple of 500 or 1000 only: ")
        return balance, transactions
    if amount <= 0: 
        print("Invalid amount. Amount shoud be greater than zero")
        return balance, transactions
    if amount > 20000 or amount > percentage:
        print("withdrawal limit exceeded! maximum transaction is 20000 per transaction")
        return balance, transactions
    if balance >= (amount + charges):
        balance -= (amount + charges)
        transactions.append(f"Withdrawal amount {amount} , transaction fees: {charges} and your new balance is {balance}")     
        print(f"Transaction successful!\n withrawal amount: {amount}\n transaction fees: {charges}\n new balance {balance}")

    else:
        print("Insufficient fund for this transaction.")
        return balance, transactions    





balance = float(input("Enter your starting balance: "))
transactions = []
while True:
    print(""" 
    __________________________________________________

	   Welcome To Motunrayo Banking Atm App.
    __________________________________________________
    		| Enter option |
    		|______________|
     1. Deposit
     2. Withdraw
     3. Account statement
     4. exit """)

    user_choice = input("Enter option: ")
    if user_choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance = deposit(balance, amount) 
    elif user_choice == "2":
        while True:
            amount = float(input("Enter amount you want to withdrawn: "))
            balance = withdraw(balance, amount, transactions)
            choice = input("Do you want to withdraw more? (enter 1 to withdraw) ")   
            if choice != "1":
                break
    elif user_choice == "3":
        if transactions:
            print("\n Account statement: ")
            for transaction in transactions:  
                print(transaction)
            #if balance is None:
                #print(f"Final balance: 0.00 ")
            if balance is True:
                balance = withdraw(balance, amount, transactions)
                print(transactions.append)
        else:
            print("No transaction recorded.")
    elif user_choice == "4":
        print("Goodbye to Motunrayo banking Atm app")
        break
    else:
        print("Invalid choice. please select a valid option.")

            

                            

 

  




