import random
def generate_question(level):
    if level == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        print("invalid level")

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
    print("""Welcome to Multiplication Drill!
    Choose difficulty level:
    1. Easy(single digit number)
    2. Medium(double digit number)
    
    Type -1 to quit""")

    level = int(input("Choose difficulty level: "))

    while True:
        number1, number2 = generate_question(level)
        correct_answer = number1 * number2

        while True:
            print(f"What is {number1} x {number2} ?")
            answer = int(input("Enter your answer: "))
            if answer == -1:
                print("Thanks for playing! see you next time!")
                return

            if answer == correct_answer:
                print(get_feedback(True))
                break

            else:
                print(get_feedback(False))


multiplication_drill()
