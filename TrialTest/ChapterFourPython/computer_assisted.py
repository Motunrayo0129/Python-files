import random

def generate_random_number():
    return random.randint(1,9), random.randint(1,9)

def multiplication_drill():
    print("Multiplication drill")
    print("Type '-1' to exit the program")
    while True:
        number1, number2 = generate_random_number()
        correct_answer = number1 * number2

        while True:
            print(f"How much {number1} times {number2} ? ")
            answer = int(input())
            if answer == -1:
                print("Bye.Thank you for playing.")
                return
            if answer != correct_answer:
                print("No. please try again")

            else:
                print("Very good!")
            break




multiplication_drill()
