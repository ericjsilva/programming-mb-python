#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""hangman.py: Let's play a game of hangman."""

# importing the time module
import time, random

# welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play hangman!"

print "\n"

# wait for 1 second
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

# here we set the secret
words = ["knowledge", "character", "citizenship", "programming", "skywalker"]

# pick a random word from the list above
word = random.choice(words)

# creates an variable with an empty value
guesses = ''

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
            print char,

        else:

        # if not found, print a dash
            print "_",

        # and increase the failed counter with one
            failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print "\nYou won"

    # exit the script
        break

    print

    # ask the user go guess a character
    guess = raw_input("Guess a character: ").upper()

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

     # turns counter decreases with 1 (now 9)
        turns -= 1

    # print wrong
        print "Wrong\n"

    # how many turns are left
        print "You have", + turns, 'more guesses'

    # if the turns are equal to zero
        if turns == 0:

        # print "You Loose"
            print "You Loose\n"