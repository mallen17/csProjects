#File: HW3.py
#Author: Max Allen
#UT EID: mca2773
#Course: CS303E

import random

# This is my setup. I need to establish variables before the loop.
print("I'm thinking of a number from 1 to 1000. " +
      "Try to guess my number! (Enter 0 to stop playing.")
guess = 0
#num = random.randint(1, 1000)
num = 458
count = 0
# Keeps going until the win condition is met.
while num != guess:
    guess = int(input("Please enter your guess: "))
    count += 1
    if guess == 0:
        print("Goodbye!")
        num = 0
    elif guess < num and guess > 0:
        print("Your guess is too low.")
    elif guess > num and guess < 1000:
        print("Your guess is too high.")
    elif guess == num:
        print("That's correct! You Win!")
        print(f"You guessed my number in {count} guesses.")
    else:
        print("Your guess must be between 1 to 1000.")

