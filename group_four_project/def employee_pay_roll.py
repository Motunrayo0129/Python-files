def employee_pay_roll(employee_name, hours_worked, hourly_pay_rate, federal_tax_rate, state_tax_rate):
    gross_pay = hours_worked * hourly_pay_rate
    fed_tax = gross_pay * (federal_tax_rate / 100)
    sta_tax = gross_pay * (state_tax_rate / 100)
    deduction = fed_tax + sta_tax
    net_pay = gross_pay - deduction
    
    return {
        "Name": employee_name,
        "Gross Pay": gross_pay,
        "Federal Tax": fed_tax,
        "State Tax": sta_tax,
        "Total Deduction": deduction,
        "Net Pay": net_pay
    }

# List to store employee payroll records
employees = []

while True:
    print("""
______________________________________________
         LIST OF EMPLOYEES PAYROLL            
______________________________________________
PRESS=======>   
    1. Add employee payroll.
    2. View employee payroll.
    3. Update employee payroll.
    4. Exit.
=============================================
""")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        name = input("Enter employee name: ").strip()
        hours_worked = float(input("Enter hours worked per week: "))
        hourly_pay_rate = float(input("Enter hourly pay rate: "))
        federal_tax_rate = float(input("Enter federal tax rate (%): "))
        state_tax_rate = float(input("Enter state tax rate (%): "))

        payroll_data = employee_pay_roll(name, hours_worked, hourly_pay_rate, federal_tax_rate, state_tax_rate)
        employees.append(payroll_data)
        print(f"\nPayroll added for {name}.")

    elif choice == "2":
        print("\nEmployee Payroll Records:")
        for employee in employees:
            print(f"\nName: {employee['Name']}")
            print(f"Gross Pay: ${employee['Gross Pay']:.2f}")
            print(f"Federal Tax Deduction: ${employee['Federal Tax']:.2f}")
            print(f"State Tax Deduction: ${employee['State Tax']:.2f}")
            print(f"Total Deduction: ${employee['Total Deduction']:.2f}")
            print(f"Net Pay: ${employee['Net Pay']:.2f}")

    elif choice == "3":
        update_name = input("Enter employee name to update payroll: ").strip()
        for employee in employees:
            if employee["Name"].lower() == update_name.lower():
                print("\nUpdating payroll for:", employee["Name"])
                employee["Hours Worked"] = float(input("Enter new hours worked per week: ") or employee["Hours Worked"])
                employee["Hourly Pay Rate"] = float(input("Enter new hourly pay rate: ") or employee["Hourly Pay Rate"])
                employee["Federal Tax Rate"] = float(input("Enter new federal tax rate (%): ") or employee["Federal Tax Rate"])
                employee["State Tax Rate"] = float(input("Enter new state tax rate (%): ") or employee["State Tax Rate"])
                print("Payroll updated successfully.")
                break
        else:
            print("Employee not found.")

    elif choice == "4":
        print("Exiting payroll system.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")