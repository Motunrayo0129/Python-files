num_student = int(input("Enter the number of students: "))

number_of_failures = 0
number_of_passes = 0
for i in range(num_student):
    validate = int(input("Enter a number '1' for pass '2' for fail : "))
    while(validate != 1 and validate != 2):
        validate = int(input("invalid input. Enter a number '1' for pass '2' for fail : "))
    if(validate == 1):
        number_of_passes += 1

    elif(validate == 2):
        number_of_failures += 1
print(f"{number_of_failures}  are the number of failures")
print(f"{number_of_passes}  are the number of passes")



