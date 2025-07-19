import random

def generate_question(problem_type):
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    if problem_type == 1:
        question = f"How much is {num1} + {num2} ? "
        answer = num1 + num2

    elif problem_type == 2:
        question = f"How much is {num1} - {num2} ? "
        answer = num1 - num2

    elif problem_type == 3:
        question = f"How much is {num1} * {num2} ? "
        answer = num1 * num2

    elif problem_type == 4:
        question = f"How much is {num1} / {num2} ? "
        answer = num1 // num2

    elif problem_type == 5:
        return generate_question(random.randint(1, 4))

    else:
        question = "Invalid problem type!"
        answer = None

    return question, answer

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

def arithmetic_drill():
    print("""Welcome to Arithmetic Drill!
    Choose the type of arithmetic operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Random mix
    
    Type -1 to quit anytime. """)

    problem_type = int(input("Enter your choice: ? "))

    while True:
        question, answer = generate_question(problem_type)

        while True:
            user_answer = int(input(f"{question} \n Enter your answer: ? "))

            if user_answer == -1:
                print("Goodbye!")
                return
            elif user_answer == answer:
                print(get_feedback(True))
                break
            else:
                print(get_feedback(False))


arithmetic_drill()





