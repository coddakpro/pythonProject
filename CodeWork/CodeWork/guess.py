import random

from CodeWork.rand_guess import guess

number_to_be_guessed = random.randint(1, 100)
greater_than_number = 1
less_than_number = 0
while number_to_be_guessed < 3:
    guess_number = int(input("Guess a number between 1 to 100: "))
    if guess_number > greater_than_number:
        less_than_number = greater_than_number
        greater_than_number = guess_number

        if guess_number < lowest_number:
             lowest_number = guess

        number_to_be_guessed += 1

    print("greater_than_number ", greater_than_number)
    print("less_than_number ", less_than_number)
    print("predicted number is ", number_to_be_guessed)
