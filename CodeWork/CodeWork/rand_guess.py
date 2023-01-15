import random

number_to_be_guessed = random.randint(1, 100)
guess = int(input("Guess a number between 1 to 100: "))
number_of_guess = 1
while guess < 2:
    guess += 1
    if guess < number_to_be_guessed:
        print("First number greater than guess number!")
    if guess > number_to_be_guessed:
        print("Second number greater than guess number!")
        break

    else:
        guess = int(input("Guess a number between 1 to 100: "))

    if guess == 2:
        print("Try again later, its unfortunate you failed", number_to_be_guessed)
