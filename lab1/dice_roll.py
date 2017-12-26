#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dice_roll.py: Roll a pair of dice."""

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dice..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    # TODO try changing the number of dice thrown using a loop
    # number_of_dice = 2
    # i = 0
    # while i < number_of_dice:
    #     print "Dice {d}: {v}".format(d=i+1, v=random.randint(min, max))
    #     i += 1

    roll_again = raw_input("Would you like to roll the dice again?")

print "\nThanks for playing!"
