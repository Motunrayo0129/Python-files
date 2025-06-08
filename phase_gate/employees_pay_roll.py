def employee_pay_roll(employee_name, hours_worked, hourly_pay_rate, federal_tax_rate, state_tax_rate):
    gross_pay = hours_worked * hourly_pay_rate
    fed_tax = gross_pay * (federal_tax_rate /100)
    sta_tax = gross_pay * (state_tax_rate / 100)
    deduction = fed_tax + sta_tax
    net_pay = gross_pay - deduction

    return  {
        "Employee Name": employee_name,  
        "Gross Pay": gross_pay,
        "Federal Tax Deduction": fed_tax,
        "State Tax Deduction": sta_tax,
        "Total Deduction": deduction,
        "Net Pay": net_pay
    }


payroll_records = []

while True:
    print(""" 
______________________________________________
    LIST OF EMPLOYEES PAYROLL. 
_______________________________________________
PRESS=======>
    1. Add employee payroll.
    2. View employee payroll.
    3. Update employee payroll.
    4. Exit.
=============================================
    """)
    choice = int(input("Enter option: "))
    if choice == 1:
        num_employees = int(input("Enter number of employees: "))
        
        for employee in range(num_employees):
            employee_name = input("Enter employee name: ").lower()

            duplicate_name = False
            for record in payroll_records:
                if record["Employee Name"].lower() == employee_name:
                    duplicate_name = True 
                    contine
 
            hours_worked = float(input("Enter hours worked per week: "))
            hourly_pay_rate = float(input("Enter amount per hour: "))
            federal_tax_rate = float(input("Enter federal tax rate: "))
            state_tax_rate = float(input("Enter state tax rate: "))

            payroll_data = employee_pay_roll(employee_name, hours_worked, hourly_pay_rate, federal_tax_rate, state_tax_rate)
            payroll_records.append(payroll_data)
            print(f"\nPayroll succesfully added")

    elif choice == 2:
        print("\nPayroll Records:")
        for record in payroll_records:
            print(f"\nEmployee: {record['Employee Name']}")
            print(f"Gross Pay: ${record['Gross Pay']:.2f}")
            print(f"Federal Tax Deduction: ${record['Federal Tax Deduction']:.2f}")
            print(f"State Tax Deduction: ${record['State Tax Deduction']:.2f}")
            print(f"Total Deduction: ${record['Total Deduction']:.2f}")
            print(f"Net Pay: ${record['Net Pay']:.2f}")

    elif choice == 3:
        update_name = input("Enter employee name to update payroll: ").strip()
        for record in payroll_records:
            if record["Employee Name"].lower() == update_name.lower():
                print("\nUpdating payroll for:", record["Employee Name"])
                record["Hours Worked"] = float(input("Enter new hours worked per week: ") or record["Hours Worked"])
                record["Hourly Pay Rate"] = float(input("Enter new hourly pay rate: ") or record["Hourly Pay Rate"])
                record["Federal Tax Rate"] = float(input("Enter new federal tax rate (%): ") or record["Federal Tax Rate"])
                record["State Tax Rate"] = float(input("Enter new state tax rate (%): ") or record["State Tax Rate"])
                print("Payroll updated successfully.")
                break
        else:
            print("Employee not found.")

    elif choice == 4:
        print("Exiting Employee Payroll System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")





