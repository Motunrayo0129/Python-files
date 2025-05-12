def countdown():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n >= 1:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a valid integer. Please try again.")

    for i in range(n, 0, -1):
        print(i)
    print("Blast off!")

countdown()