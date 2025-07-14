total_gallons = 0
total_miles = 0

while True:
    miles = int(input("Enter the number of miles or (-1 to quit): ) : "))
    if miles == -1:
        break
    gallons = int(input("Enter the number of gallons or (-1 to quit): "))
    mpg = miles / gallons
    print(f"The miles per gallons for this tank was {mpg:.2f} ")

    if total_gallons > 0:
        overall_mpg = total_miles / total_gallons
        print(f'Overall average miles/gallons was {overall_mpg:.2f}')

    else:
        print('No valid data entered')

