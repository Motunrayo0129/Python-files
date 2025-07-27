def get_invoices(id, products_description, quantity, price):
    invoices = []
    for product in range(len(products_description)):
        total_price = price[product] * quantity[product]
        invoices.append([id[product], quantity[product], products_description[product], total_price])
        print("id \t product \t quantity \t price \t ")
    return invoices



invoices =[[20, 2, 'laptop', 334.56], [15, 1, 'standing_fan', 345.67]]
print('ID\t \t Product \t Quantity \t Price \t ')
print('_' * 50)
for invoice in invoices:
    print(f'{invoice[0]}\t{invoice[2]}\t\t{invoice[1]}\t\t${invoice[3]:.2f}')