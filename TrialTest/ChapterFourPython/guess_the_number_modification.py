import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    guess_counter = 0

    print("Guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        guess_counter += 1

        if guess < 1 or guess > 100:
            print("Invalid guess.")
            continue
        elif guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Congratulations, you guessed it in " + str(guess_counter) + " guesses.")
            break

        if guess_counter >= 10:
            print("Either you know the secret or you got lucky.")
        else:
            print("You should be able to do better!")

guess_the_number()

