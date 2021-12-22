#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""hangman.py: Let's play a game of hangman."""

# importing the time module
import time, random

# welcoming the user
name = input("What is your name? ")

print(f"Hello {name}, Time to play hangman!\n")

# wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# here we set the secret
words = ["knowledge", "character", "citizenship", "programming", "skywalker"]

# pick a random word from the list above
word = random.choice(words)

# creates an variable with an empty value
guesses = ""

# determine the number of turns
turns = 10
#turns = len(word) + 4

# Create a while loop

# check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word.upper():

    # see if the character is in the players guess
        if char in guesses:
            # print then out the character
            print(f"{char}", end=" ")
        else:
            # if not found, print a dash
            print("_", end=" ")

            # and increase the failed counter with one
            failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print("\nYou won!")

        # exit the script
        break

    # ask the user go guess a character
    guess = input("\nGuess a character: ").upper()

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word.upper():

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print incorrect guess
        print(f"Sorry there is no {guess}.\n")

        # how many turns are left
        print(f"You have {turns} more guesses...")

        # if the turns are equal to zero
        if turns == 0:

        # print "You did not guess the word. Better luck next time."
            print("You did not guess the word. Better luck next time.\n")
