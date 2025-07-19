import random

def generate_random_number():
    return random.randint(1,9), random.randint(1,9)

def get_feedback(is_correct):
    responses = {
        True: [
            "Very good!",
            "Nice work!",
            "Keep up the good work!"
        ],
        False: [
            "No. Please try again.",
            "Wrong. Try once more.",
            "No. Keep trying."
        ]
    }
    index = random.randint(0, 2)
    return responses[is_correct][index]

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
            if answer == correct_answer:
                print(get_feedback(is_correct = True))

            else:
                print(get_feedback(is_correct = False))
            break




multiplication_drill()
