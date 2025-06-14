from datetime import datetime

def get_items(products):
    items = []
    subtotal = 0

    for product_name, price, quantity in products:
        item_total = price * quantity
        subtotal += item_total
        items.append((product_name, quantity, price, item_total))

    return items, subtotal

def calculate_totals(subtotal, discount_rate):
    discount = subtotal * (discount_rate / 100)
    vat = subtotal * (7.5 / 100)
    total = subtotal - discount + vat
    return discount, vat, total

def generate_receipt(items, subtotal, discount, vat, total, cashier_name, customer_name):
    now = datetime.now()
    formatted_datetime = now.strftime("%d-%m-%Y %I:%M:%S %p")

    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    print("TELEPHONE: 08121135541")
    print(f"DATE: {formatted_datetime}\nCASHIER: {cashier_name}\nCUSTOMER: {customer_name}")
    print("=" * 74)
    print("Itemized Receipt")
    print("=" * 74)
    print(f"{'Item':<15} {'Quantity':<10} {'Price':<10} {'Total':<10}")
    print("-" * 74)

    for item in items:
        product_name, quantity, price, item_total = item
        print(f"{product_name:<15} {quantity:<10} {price:<10.2f} {item_total:<10.2f}")  # Indented

    print("-" * 74)
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"VAT: {vat:.2f}")
    print("=" * 74)
    print(f"Total Amount: {total:.2f}")

def process_payment(total, amount_paid):
    """Handles payment validation and allows retrying if the amount is insufficient."""
    while amount_paid < total:
        print(f"Insufficient fund. The total amount is {total:.2f}, but you entered {amount_paid:.2f}.")
        amount_paid = float(input("Enter a valid amount: "))

    balance = amount_paid - total

    print("=" * 74)
    print(f"Bill Total: {total:.2f}")
    print(f"Amount Paid: {amount_paid:.2f}")
    print(f"Balance: {balance:.2f}")

customer_name = input("Enter customer name: ")
cashier_name =  input("Enter your name (CASHIER'S NAME): ")
products = []
while True:
    product_name = input("Enter product name: ")
    price = float(input("Enter price per unit: "))
    quantity = int(input("Enter quantity: "))
    products.append((product_name, price, quantity))
    response = int(input("Add more items? (Enter '1' for Yes/Enter '2' for No): "))
    while(response != 1 and response != 2): 
        response = int(input("Invalid input. Enter 1 or 2: "))
    if response == 2:
        break
discount_rate = float(input("Enter discount percentage: "))
items, subtotal = get_items(products)
discount, vat, total = calculate_totals(subtotal, discount_rate)
print("=" * 74)
print(f"Total Amount Due: {total:.2f}")

amount_paid = float(input("How much did the customer give you: "))
generate_receipt(items, subtotal, discount, vat, total, cashier_name, customer_name)
process_payment(total, amount_paid)

 
    