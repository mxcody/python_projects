"""
Guess the Number
Author: Cody
June 19, 2021

This game has a user guess a number between 1 and 100 with a limited amount of attempts.
"""

import random
the_number = random.randrange (1, 101)
counter = 0

while True:
    user_guess = input("Guess a number between 1 and 100: ")
    if not user_guess.isdigit():
        print("Please enter a number!")
    else:
        user_guess = int(user_guess)

        if user_guess == the_number:
            print("Congrats! You win the game!")
            break
        else:
            counter += 1
            if user_guess < the_number:
                print("It's higher!")
            if user_guess > the_number:
                print("It's lower!")
        if counter == 7:
            print("The number was: ", the_number)
            break
            
# end of program
