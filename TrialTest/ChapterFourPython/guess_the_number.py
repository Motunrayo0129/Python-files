import random
def guess_the_number():
    secret_number = random.randint(1, 1000)
    guess_count = 0

    print("Guess a number between 1 and 1000.")

    while True:
        guess = int(input("Enter your guess: "))
        guess_count += 1
        if guess < 1 or guess > 1000:
            print("Invalid guess. Enter again.")
            continue
        elif guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations, you guessed it in {guess_count} guesses.")
            break

    replay = input("Do you want to play again? (yes/no): ")
    if replay == "yes":
        guess_the_number()
    else:
        print("Bye.Thank you for playing.")



guess_the_number()





