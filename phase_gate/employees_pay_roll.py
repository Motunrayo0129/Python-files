def employee_pay_roll(employee_name, hours_worked, hourly_pay_rate, federal_tax_rate, state_tax_rate)
    gross_pay = hours_worked * hourly_pay_rate
    fed_tax = gross_pay * 100 / federal_tax_rate
    sta_tax = gross_pay * 100 / state_tax_rate
    deduction = fed_tax + sta_tax
    net_pay = gross_pay - deduction
    return f"The gross pay is {gross_pay}\n The federal tax rate is {fed_tax}\n The state tax rate is{sta_tax}\n The total deduction is {deduction}\n And the net pay per week is {net_pay}"


no_of_employee = int(input("Enter numbers employee: "))
employee = []

while true:
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
    