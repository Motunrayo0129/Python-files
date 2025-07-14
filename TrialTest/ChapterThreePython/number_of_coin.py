price = float(input('Enter the purchase from(0 to 1.00): '))

if price < 0 or price > 1:
    print('Invalid input. Price valid from 0 to 1')
else:
    change = float((1 - price) * 100)

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    if quarters:
        print(f'Your change is {quarters} quarter(s)')
    if dimes:
        print(f'{dimes} dime(s)')
    if nickels:
        print(f'{nickels} nickel(s)')
    if pennies:
        print(f'{pennies} penny(ies)')
