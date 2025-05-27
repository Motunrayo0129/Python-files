accounts = []


def create_account(name, phone_number, balance = 0.0):
	account[name, phone, balance]
	accounts.append(account)
	return f"Account created for {name} with balance: {balance}"

def deposit_money(name, amount):
    for client in range(len(accounts)): 
        if accounts[client][0] == name:  
            updated_balance = accounts[client][2] + amount 
            
            accounts[client] = (accounts[client][0], accounts[client][1], updated_balance)
            
            return f"Deposited {amount} into {name}'s account. New balance: {updated_balance}"

    return "Account not found."

def withdrawn_money(name, amount):
    for client in range(len(accounts)): 
        if accounts[client][2] <= amount:  
            updated_balance = accounts[client][2] - amount 
            
            accounts[client] = (accounts[client][0], accounts[client][1], updated_balance)
           
            return f"money withdrawn {amount} into {name}'s account. New balance: {updated_balance}"

            return "Insufficient funds"	

def negative_amount(name, amount):
    for client in range(len(accounts)): 
        if accounts[client][2] <= 0:  
                       
            return "Cannot perform transaction on negative input"

def limited_access(name, amount):
    for client in range(len(accounts)): 
        if accounts[client][2] > 10000:  
                       
            return "Limit exceeded" 

def deposit_money(name, amount):
    for client in range(len(accounts)): 
        if accounts[client][0] == name:  
            updated_balance = accounts[client][2] + amount 
            accounts[client] = (accounts[client][0], accounts[client][1], updated_balance)
            
            return f"Deposited {amount} into {name}'s account. New balance: {updated_balance}"

        if amount >= 50000:
            return "Large deposit detected"
            

                            

 

  




